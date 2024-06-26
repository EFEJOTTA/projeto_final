import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df.fillna('valor_padrão', inplace=True)
    df['text_length'] = df['text'].apply(len)
    df.to_csv('C:/Users/lipef/Desktop/Trabalho_A2-ICD/src/reviews_clean.csv', index=False)
    return df

if __name__ == "__main__":
    file_path = 'C:/Users/lipef/Desktop/Trabalho_A2-ICD/src/reviews.csv'
    clean_data(file_path)
