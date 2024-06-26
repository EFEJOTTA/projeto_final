import openai
import pandas as pd

def summarize_review(review_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Resuma a seguinte avaliação: {review_text}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def process_with_openai(file_path, api_key):
    openai.api_key = api_key
    df = pd.read_csv(file_path)
    df['summary'] = df['text'].apply(summarize_review)
    df.to_csv('C:/Users/lipef/Desktop/Trabalho_A2-ICD/src/reviews_summarized.csv', index=False)
    return df

if __name__ == "__main__":
    file_path = 'C:/Users/lipef/Desktop/Trabalho_A2-ICD/src/reviews_clean.csv'
    api_key = 'CHAVE-DA-API'
    process_with_openai(file_path, api_key)
