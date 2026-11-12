from openai import OpenAI

client = OpenAI(api_key="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")
modelos = client.models.list()

for m in modelos:
    print(m.id)