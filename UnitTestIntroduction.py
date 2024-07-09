import unittest
from selenium import webdriver
from Utils import (
    TEXT_TO_FIND,
    MEDICAL_CENTER_URL,
    BTN_MAKE_APPOINTMENT_TEXT,
    USER_PASSWORD,
    USER_NAME,
)
from selenium.webdriver.common.by import By
import os
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()


# Defino una clase que hereda de unittest para definir en ella mi prueba
class MedicvalCenterTest(unittest.TestCase):
    def setUp(self) -> None:
        """Esta funcion se ejecuta antes de iniciar la prueba"""
        self.driver = webdriver.Chrome()

    ###dEFINO LAS PRUEBAS AQUI
    def test_suma(self):
        """Este es el codigo de la prueba de acceso"""
        # dado los valores de4 a y b
        a: int = 2
        b: int = 7
        # Accion.... suma a y b
        suma: int = a + b
        # Then Comprueba que es 9
        self.assertEqual(suma, 9)

    def test_medical_center_registration_form_test(self):
        f"""Esta prueba testea el login del sitio web especificado en {MEDICAL_CENTER_URL} """
        self.driver.get(MEDICAL_CENTER_URL)
        # abre este sitio
        self.driver.get(MEDICAL_CENTER_URL)
        # Busca un elemento por su id y haz click sobre el
        self.driver.find_element(By.ID, "btn-make-appointment").click()
        # Busca el elemento por su id y limpia su valor
        self.driver.find_element(By.ID, "txt-username").clear()
        # escribe jhon doe
        self.driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        # Busca el elemento por su id y limpia su valor
        self.driver.find_element(By.ID, "txt-password").clear()
        # escribe "ThisIsNotAPassword"
        self.driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        # Hacer una captura de pantalla antes de loggin
        self.driver.get_screenshot_as_file("capturas/captura_antes_login.png")
        # Busca un elemento por su id y haz click sobre el
        self.driver.find_element(By.ID, "btn-login").click()
        # Hacer una captura de pantalla luego de loggin
        self.driver.get_screenshot_as_file("capturas/captura_despues_login.png")
        # Busca un elemento con este texto
        text_found = self.driver.find_element(
            By.XPATH, "//h2[normalize-space()='Make Appointment']"
        ).text
        self.assertEqual(TEXT_TO_FIND, text_found)
        self.driver.find_element(By.ID, "menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        self.assertAlmostEqual(
            self.driver.find_element(By.ID, "btn-make-appointment").text,
            BTN_MAKE_APPOINTMENT_TEXT,
        )

    def test_invalid_login(self):
        f"""Esta prueba testea el login del sitio web especificado en {MEDICAL_CENTER_URL} """
        self.driver.get(MEDICAL_CENTER_URL)
        # abre este sitio
        self.driver.get(MEDICAL_CENTER_URL)
        # Busca un elemento por su id y haz click sobre el
        self.driver.find_element(By.ID, "btn-make-appointment").click()
        # Busca el elemento por su id y limpia su valor
        self.driver.find_element(By.ID, "txt-username").clear()
        # escribe jhon doe
        self.driver.find_element(By.ID, "txt-username").send_keys(USER_NAME)
        # Busca el elemento por su id y limpia su valor
        self.driver.find_element(By.ID, "txt-password").clear()
        # escribe "ThisIsNotAPassword"
        self.driver.find_element(By.ID, "txt-password").send_keys(USER_PASSWORD)
        # Hacer una captura de pantalla antes de loggin
        self.driver.get_screenshot_as_file(
            "capturas/login_not_ok/captura_antes_login.png"
        )
        # Busca un elemento por su id y haz click sobre el
        self.driver.find_element(By.ID, "btn-login").click()
        # Hacer una captura de pantalla luego de loggin
        self.driver.get_screenshot_as_file(
            "capturas/login_not_ok/captura_despues_login.png"
        )
        # Busca un elemento con este texto
        msg = self.driver.find_element(By.XPATH, "//p[@class='lead text-danger']")
        self.assertIsNotNone(msg)

    def tearDown(self) -> None:
        """Esta funcion se ejecuta cuando acaba la prueba"""
        self.driver.quit()

    def crear_carpeta(self, carpeta):
        """Funcion para crear una carpeta a partir de uhna ruta especificada en los parametros"""
        if not os.path.exists(carpeta):  # si la carpeta no existe
            os.mkdir(carpeta)  # crea una nueva carpeta


if __name__ == "__main__":
    unittest.main()
    # lanza la ejecucion de las pruebas
    # Crea una instancia de la clase y ejecuta:
    # 1.setup
    # 2. medical_center_registration_form y medical_center_access
    # 3. ejecuta el tearDown
