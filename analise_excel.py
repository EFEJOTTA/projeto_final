import pandas as pd

def export_to_excel(file_path):
    df = pd.read_csv(file_path)
    df.to_excel('C:/Users/lipef/Desktop/Trabalho_A2-ICD/data/final/reviews_final.xlsx', index=False)

if __name__ == "__main__":
    file_path = 'C:/Users/lipef/Desktop/Trabalho_A2-ICD/data/processed/reviews_summarized.csv'
    export_to_excel(file_path)
