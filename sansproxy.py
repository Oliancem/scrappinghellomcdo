from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random



def run_survey():
    # Configurer le navigateur
    driver = webdriver.Chrome()

    # Accéder au site
    driver.get("https://survey2.medallia.eu/?hellomcdo")

    # Cliquer sur le bouton commencer l'enquete
    bouton = driver.find_element(By.CLASS_NAME, "button_buttonCaption")
    bouton.click()

    time.sleep(2)

    # Cliquer sur le premier bouton
    bouton_initial = driver.find_element(By.ID, "onf_q_mc_q_age_2")
    bouton_initial.click()

    time.sleep(2)

    bouton = driver.find_element(By.CLASS_NAME, "button_buttonCaption")
    bouton.click()

    time.sleep(2)

    # Remplir la date
    date_field = driver.find_element(By.ID, "cal_q_mc_q_date_")
    date_field.clear()
    date_field.send_keys("12/01/2025")

    time.sleep(2)

    random_value = random.randint(0, 23)
    formatted_value = f"{random_value:02}"

    # Générer un nombre aléatoire entre 0 et 60    # Remplir les minutes
    date_field = driver.find_element(By.ID, "spl_rng_q_mc_q_hour")
    date_field.clear()
    date_field.send_keys(formatted_value)


    random_value = random.randint(0, 60)
    formatted_value = f"{random_value:02}"

    # Remplir les minutes
    date_field = driver.find_element(By.ID, "spl_rng_q_mc_q_minute")
    date_field.clear()
    date_field.send_keys(formatted_value)

    # Attendre un peu pour observer
    time.sleep(2)

    # Remplir le restaurant
    date_field = driver.find_element(By.ID, "spl_rng_q_mc_q_idrestaurant")
    date_field.clear()
    date_field.send_keys("535")

    time.sleep(2)

    # Cliquer sur le bouton suivant
    bouton = driver.find_element(By.ID, "buttonNext")
    bouton.click()

    time.sleep(2)

    # Cliquer sur d'autres boutons avec des IDs spécifiques
    bouton_initial = driver.find_element(By.ID, "onf_q_where_did_you_place_your_order_3")
    bouton_initial.click()

    time.sleep(2)

    bouton = driver.find_element(By.ID, "buttonNext")
    bouton.click()

    time.sleep(2)

    bouton_initial = driver.find_element(By.ID, "onf_q_feedback_m_based_upon_this_visit_to_this_6_1")
    bouton_initial.click()

    time.sleep(2)

    bouton = driver.find_element(By.ID, "buttonNext")
    bouton.click()

    time.sleep(2)

    bouton_initial = driver.find_element(By.ID, "onf_q_mc_q_quality_of_food_and_drink_1")
    bouton_initial.click()
    bouton_initial = driver.find_element(By.ID, "onf_q_mc_q_friendliness_crew_1")
    bouton_initial.click()
    bouton_initial = driver.find_element(By.ID, "onf_q_feedback_m_the_exterior_aspect_of_the_res_1")
    bouton_initial.click()
    bouton_initial = driver.find_element(By.ID, "onf_q_mc_q_speed_service_2")
    bouton_initial.click()

    time.sleep(2)

    bouton = driver.find_element(By.ID, "buttonNext")
    bouton.click()

    time.sleep(2)

    bouton_initial = driver.find_element(By.ID, "onf_q_feedback_m_was_your_order_accurate_1")
    bouton_initial.click()

    time.sleep(1)

    bouton = driver.find_element(By.ID, "buttonNext")
    bouton.click()

    time.sleep(2)

    bouton_initial = driver.find_element(By.ID, "onf_q_feedback_m_did_you_experience_a_problem_d_2")
    bouton_initial.click()

    time.sleep(2)

    bouton = driver.find_element(By.ID, "buttonFinish")
    bouton.click()

    time.sleep(5)

    # Fermer le navigateur
    driver.quit()

# Faire tourner le script en boucle 20 fois avec une pause de 5 minutes entre chaque exécution
for i in range(100):
    print(f"Exécution {i + 1} sur 100...")
    run_survey()
    if i < 99:  # Ne pas attendre après la dernière itération
        time.sleep(20)  # Attendre 5 minutes (300 secondes)
