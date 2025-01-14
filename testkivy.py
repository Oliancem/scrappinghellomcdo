from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from kivy.app import App
from kivy.uix.button import Button
from threading import Thread


def run_survey():
    """
    Exécute le script Selenium pour remplir le formulaire en ligne.
    """
    try:
        # Configurer le navigateur
        driver = webdriver.Chrome()

        # Accéder au site
        driver.get("https://survey2.medallia.eu/?hellomcdo")

        # Cliquer sur le bouton commencer l'enquête
        bouton = driver.find_element(By.CLASS_NAME, "button_buttonCaption")
        bouton.click()

        time.sleep(2)

        # Remplir les champs et cliquer sur les boutons
        driver.find_element(By.ID, "onf_q_mc_q_age_2").click()
        time.sleep(2)

        driver.find_element(By.CLASS_NAME, "button_buttonCaption").click()
        time.sleep(2)

        driver.find_element(By.ID, "cal_q_mc_q_date_").send_keys("12/01/2025")
        time.sleep(2)

        driver.find_element(By.ID, "spl_rng_q_mc_q_hour").send_keys("19")
        time.sleep(2)

        random_value = random.randint(0, 60)
        driver.find_element(By.ID, "spl_rng_q_mc_q_minute").send_keys(f"{random_value:02}")
        time.sleep(2)

        driver.find_element(By.ID, "spl_rng_q_mc_q_idrestaurant").send_keys("535")
        time.sleep(2)

        driver.find_element(By.ID, "buttonNext").click()
        time.sleep(2)

        # Répéter pour d'autres étapes spécifiques
        ids_to_click = [
            "onf_q_where_did_you_place_your_order_3",
            "onf_q_feedback_m_based_upon_this_visit_to_this_6_1",
            "onf_q_mc_q_quality_of_food_and_drink_1",
            "onf_q_mc_q_friendliness_crew_1",
            "onf_q_feedback_m_the_exterior_aspect_of_the_res_1",
            "onf_q_mc_q_speed_service_2",
            "onf_q_feedback_m_was_your_order_accurate_1",
            "onf_q_feedback_m_did_you_experience_a_problem_d_2",
        ]

        for element_id in ids_to_click:
            driver.find_element(By.ID, element_id).click()
            time.sleep(2)

            if element_id != "onf_q_feedback_m_did_you_experience_a_problem_d_2":
                driver.find_element(By.ID, "buttonNext").click()
                time.sleep(2)

        # Terminer l'enquête
        driver.find_element(By.ID, "buttonFinish").click()
        time.sleep(5)

    finally:
        # Fermer le navigateur après l'exécution
        driver.quit()


def run_in_loop():
    """
    Exécute le script en boucle 20 fois avec une pause de 5 minutes entre chaque exécution.
    """
    for i in range(20):
        print(f"Exécution {i + 1} sur 20...")
        run_survey()
        if i < 19:  # Ne pas attendre après la dernière exécution
            time.sleep(300)  # Attendre 5 minutes


class MyApp(App):
    def build(self):
        """
        Crée l'interface graphique avec un bouton pour démarrer le script.
        """
        button = Button(text="Lancer le script en boucle")
        button.bind(on_press=lambda x: Thread(target=run_in_loop).start())
        return button


if __name__ == "__main__":
    MyApp().run()
