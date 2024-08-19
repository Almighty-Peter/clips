from openai import OpenAI

api_key=''
client = OpenAI(api_key=api_key)

def textToText(prompt,system_message):
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    )

    return(completion.choices[0].message.content)

def get_embedding(text, model="text-embedding-3-large"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding
