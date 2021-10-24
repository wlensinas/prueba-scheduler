# Schedule Library imported
import schedule
import time
import requests
import concurrent.futures
from datetime import datetime


def get_page(page_url, timeout=10):
    response = requests.get(url=page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return page_url + " - " + page_status


def get_collect_metrics():
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'hora de ejecucion: {hora}')
    urls = [
        'https://www.google.com/',
        'https://api.github.com',
        'https://www.infobae.com/',
        'https://www.ambito.com/',
        'https://www.mercadolibre.com.ar/']

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in urls:
            futures.append(executor.submit(get_page, page_url=url))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


schedule.every(1).minute.do(get_collect_metrics)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
