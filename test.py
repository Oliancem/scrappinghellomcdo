from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import random
import requests

# Fonction pour tester un proxy
def test_proxy(proxy):
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.ok:
            print(f"Proxy {proxy} is working. Your IP: {response.json()['origin']}")
            return True
        else:
            print(f"Proxy {proxy} returned status code {response.status_code}")
            return False
    except Exception as e:
        print(f"Error occurred while testing proxy {proxy}: {e}")
        return False

# Liste de proxies (remplacez par vos proxies réels)
proxy_list = [
    "http://tl-88627f419d25533eb42b27d76200cd40ccd52df45ce03e363bef7256f39ada05-country-FR-session-C650b:lkv93z5jb8l7@proxy.toolip.io:31113",
]

# Sélectionner un proxy aléatoire et tester s'il est fonctionnel
def get_working_proxy():
    while True:
        proxy = random.choice(proxy_list)
        if test_proxy(proxy):
            return proxy

# Obtenir un proxy valide
working_proxy = get_working_proxy()
print(f"Using proxy: {working_proxy}")

# Configurer le navigateur pour utiliser le proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={working_proxy}")

# Lancer le navigateur avec le proxy
driver = webdriver.Chrome(options=chrome_options)

# Accéder au site
driver.get("https://survey2.medallia.eu/?hellomcdo")

time.sleep(2)

# Cliquer sur le bouton commencer l'enquête
bouton = driver.find_element(By.CLASS_NAME, "button_buttonCaption")
bouton.click()

# Étape 1 : Cliquer sur le premier bouton
bouton_initial = driver.find_element(By.ID, "onf_q_mc_q_age_2")  # Exemple d'ID du bouton
bouton_initial.click()

time.sleep(2)

# Cliquer sur le bouton suivant
bouton = driver.find_element(By.CLASS_NAME, "button_buttonCaption")
bouton.click()

time.sleep(2)

# Localiser le champ de date par son ID
date_field = driver.find_element(By.ID, "cal_q_mc_q_date_")
date_field.clear()
date_field.send_keys("12/01/2024")

time.sleep(2)

# Localiser et remplir l'heure
date_field = driver.find_element(By.ID, "spl_rng_q_mc_q_hour")
date_field.clear()
date_field.send_keys("19")

# Générer un nombre aléatoire entre 0 et 60
random_value = random.randint(0, 60)
formatted_value = f"{random_value:02}"

# Localiser le champ de minute et le remplir avec la valeur aléatoire
date_field = driver.find_element(By.ID, "spl_rng_q_mc_q_minute")
date_field.clear()
date_field.send_keys(formatted_value)

time.sleep(2)

# Remplir le champ de restaurant
date_field = driver.find_element(By.ID, "spl_rng_q_mc_q_idrestaurant")
date_field.clear()
date_field.send_keys("535")

time.sleep(2)

# Cliquer sur le bouton suivant
bouton = driver.find_element(By.ID, "buttonNext")
bouton.click()

time.sleep(2)

# Le navigateur restera ouvert pour observer les résultats
