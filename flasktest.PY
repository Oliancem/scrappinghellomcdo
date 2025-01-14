from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Initialisation de l'application Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Votre fonction pour exécuter le script Selenium
def run_survey():
    # Configurer le navigateur
    driver = webdriver.Chrome()

    try:
        # Accéder au site
        driver.get("https://survey2.medallia.eu/?hellomcdo")

        # Cliquer sur le bouton commencer l'enquête
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

        # Générer un nombre aléatoire pour l'heure
        random_hour = random.randint(0, 23)
        date_field = driver.find_element(By.ID, "spl_rng_q_mc_q_hour")
        date_field.clear()
        date_field.send_keys(f"{random_hour:02}")

        # Générer un nombre aléatoire pour les minutes
        random_minute = random.randint(0, 59)
        date_field = driver.find_element(By.ID, "spl_rng_q_mc_q_minute")
        date_field.clear()
        date_field.send_keys(f"{random_minute:02}")

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

    finally:
        # Fermer le navigateur
        driver.quit()

# Route Flask pour exécuter le script Selenium
@app.route('/run', methods=['GET'])
def run():
    try:
        run_survey()
        return jsonify({"status": "success", "message": "Survey completed successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
