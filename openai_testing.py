import openai

# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)

# create a completion
completion = openai.Completion.create(model="ada", prompt="How are you?")

# print the completion
print(completion.choices[0].text)

