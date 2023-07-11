import json
from typing import Dict

from nested_lookup import nested_lookup
from scrapfly import ScrapeConfig, ScrapflyClient

scrapfly = ScrapflyClient('scp-live-9c311e68659743f0ab0aa81833ffc18e')
BASE_CONFIG = {
    # Twitter.com requires Anti Scraping Protection bypass feature.
    # for more: https://scrapfly.io/docs/scrape-api/anti-scraping-protection
    "asp": True,
    # Twitter.com is javascript-powered web application so it requires
    # headless browsers for scraping
    "render_js": True,
    "country": "CA",  # set prefered country here, for example Canada
}

def parse_tweet(data: Dict) -> Dict:
    """Parse Twitter tweet JSON dataset for the most important fields"""
    result = jmespath.search(
        """{
        created_at: legacy.created_at,
        attached_urls: legacy.entities.urls[].expanded_url,
        attached_urls2: legacy.entities.url.urls[].expanded_url,
        attached_media: legacy.entities.media[].media_url_https,
        tagged_users: legacy.entities.user_mentions[].screen_name,
        tagged_hashtags: legacy.entities.hashtags[].text,
        favorite_count: legacy.favorite_count,
        bookmark_count: legacy.bookmark_count,
        quote_count: legacy.quote_count,
        reply_count: legacy.reply_count,
        retweet_count: legacy.retweet_count,
        quote_count: legacy.quote_count,
        text: legacy.full_text,
        is_quote: legacy.is_quote_status,
        is_retweet: legacy.retweeted,
        language: legacy.lang,
        user_id: legacy.user_id_str,
        id: legacy.id_str,
        conversation_id: legacy.conversation_id_str,
        source: source,
        views: views.count
    }""",
        data,
    )
    result["poll"] = {}
    poll_data = jmespath.search("card.legacy.binding_values", data) or []
    for poll_entry in poll_data:
        key, value = poll_entry["key"], poll_entry["value"]
        if "choice" in key:
            result["poll"][key] = value["string_value"]
        elif "end_datetime" in key:
            result["poll"]["end"] = value["string_value"]
        elif "last_updated_datetime" in key:
            result["poll"]["updated"] = value["string_value"]
        elif "counts_are_final" in key:
            result["poll"]["ended"] = value["boolean_value"]
        elif "duration_minutes" in key:
            result["poll"]["duration"] = value["string_value"]
    user_data = jmespath.search("core.user_results.result", data)
    if user_data:
        result["user"] = parse_user(user_data)
    return result

async def scrape_tweet(url: str) -> Dict:
    """
    Scrape a single tweet page for Tweet thread e.g.:
    https://twitter.com/Scrapfly_dev/status/1667013143904567296
    Return parent tweet, reply tweets and recommended tweets
    """
    result = await scrapfly.async_scrape(ScrapeConfig(
        url, 
        asp= True,
        render_js= True,
        country= "CA",
    ))
    
    # capture background requests and extract ones that request Tweet data
    _xhr_calls = result.scrape_result["browser_data"]["xhr_call"]
    tweet_call = [f for f in _xhr_calls if "TweetDetail" in f["url"]]
    tweets = []
    for xhr in tweet_call:
        if not xhr["response"]:
            continue
        data = json.loads(xhr["response"]["body"])
        # find tweet_results key recursive as that's where tweet data is located
        xhr_tweets = nested_lookup("tweet_results", data)
        tweets.extend([parse_tweet(tweet["result"]) for tweet in xhr_tweets])

    # Now that we have all tweets we can parse them into a thread
    # The first tweet is the parent, the rest are replies or suggested tweets
    parent = tweets.pop(0)
    replies = []
    other = []
    for tweet in tweets:
        if tweet["conversation_id"] == parent["conversation_id"]:
            replies.append(tweet)
        else:
            other.append(tweet)
    return {
        "tweet": parent,
        "replies": replies,
        "other": other,  # ads, recommended etc
    }
  
if __name__ == "__main__":
    import asyncio
    asyncio.run(scrape_tweet("https://syndication.twitter.com/srv/timeline-profile/screen-name/scrapfly_dev"))
