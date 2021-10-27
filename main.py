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

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        time1 = time.time()
        for url in urls:
            futures.append(executor.submit(get_page, page_url=url))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
        time2 = time.time()
        print(f'Took {time2-time1:.2f} s')


def run():
    schedule.every(1).minute.do(get_collect_metrics)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    run()
