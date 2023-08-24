import openai

openai.api_key = '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'

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                               messages=[{"role": "user", 
                                                          "content": "tell me if the following 3 tweets are related to flood emergency or not. return a sequence of True and False:\
                                                          The water is up again, that man is trying to flood the internet, please send help here flood"}])
print(chat_completion)