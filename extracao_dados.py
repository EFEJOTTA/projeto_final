import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_reviews(url):
    '''
    
    Essa função realiza a coleta das reviews da Amazon.
    
    Paâmetros:
    url (str): URL da página da Amazon de onde serão extraídas as reviews.
    
    Retorna:
    pd.DataFrame: DataFrame que possui as reviews extraídas.
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    reviews = []
    for review in soup.find_all('div', class_='ui-review-capability'):
        rating = review.find('p', class_='ui-review-capability__rating__average ui-review-capability__rating__average--desktop').text
        text = review.find('div', class_='ae-evaluateList-box').text
        reviews.append({'rating': rating, 'text': text})

    df = pd.DataFrame(reviews)
    df.to_csv('C:/Users/lipef/Desktop/Trabalho_A2-ICD/src/reviews.csv', index=False)
    return df

if __name__ == "__main__":
    url = 'https://www.mercadolivre.com.br/notebook-samsung-galaxy-book2-i5-1235u-windows-11-home-8gb-256gb-ssd-grafite/p/MLB27983182?pdp_filters=deal%3AMLB779362-1#polycard_client=homes-korribanSearchPromotions&searchVariation=MLB27983182&position=3&search_layout=grid&type=product&tracking_id=cce7ae91-cd3f-443d-87d0-78b1353eaf56&c_id=/home/promotions-recommendations/element&c_uid=fb1e5f5b-0809-4e3f-9cb7-2ba1943b0476'
    extract_reviews(url)
