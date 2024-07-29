from openai import OpenAI

api_key='open ai api key'
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
