from openai import OpenAI

client = OpenAI(api_key="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")
modelos = client.models.list()

for m in modelos:
    print(m.id)