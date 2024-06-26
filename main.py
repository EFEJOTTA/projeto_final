from extracao_dados import extract_reviews
from limpeza_dados import clean_data
from processamento_API import process_with_openai
from analise_excel import export_to_excel

def main():
    url = 'https://www.mercadolivre.com.br/notebook-samsung-galaxy-book2-i5-1235u-windows-11-home-8gb-256gb-ssd-grafite/p/MLB27983182?pdp_filters=deal%3AMLB779362-1#polycard_client=homes-korribanSearchPromotions&searchVariation=MLB27983182&position=3&search_layout=grid&type=product&tracking_id=cce7ae91-cd3f-443d-87d0-78b1353eaf56&c_id=/home/promotions-recommendations/element&c_uid=fb1e5f5b-0809-4e3f-9cb7-2ba1943b0476'
    api_key = 'CHAVE-DA-API'
    
    # Extração de dados
    print("Extraindo dados...")
    extract_reviews(url)
    
    # Limpeza de dados
    print("Limpando dados...")
    clean_data('C:/Users/lipef/Desktop/Trabalho_A2-ICD/src/reviews.csv')
    
    # Processamento com OpenAI
    print("Processando dados com OpenAI...")
    process_with_openai('C:/Users/lipef/Desktop/Trabalho_A2-ICD/src/reviews_clean.csv', api_key)
    
    # Análise de dados
    print("Exportando dados para Excel...")
    export_to_excel('C:/Users/lipef/Desktop/Trabalho_A2-ICD/src/reviews_summarized.csv')
    
    print("Projeto concluído com sucesso!")

if __name__ == "__main__":
    main()
