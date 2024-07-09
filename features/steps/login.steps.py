import os
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller


def before_all(context):
    chromedriver_autoinstaller.install()


@given("Que tengo un navegador abierto")
def open_browser(contexto):
    contexto.driver = webdriver.Chrome()
    contexto.driver.implicitly_wait(30)


@when('Entro al sitio "{string}"')
def open_site(contexto, string):
    contexto.driver.get(string)


@when('Hago click en el boton con id "{id}"')
def cklick_on_make_appointment(contexto, id):
    contexto.driver.find_element(By.ID, id).click()


@when('Escribo "{username}" en el campo con id "{id}"')
def enter_username(contexto, username, id):
    user_name_element = contexto.driver.find_element(By.ID, id)
    user_name_element.clear()
    user_name_element.send_keys(username)


@then(
    'Deberia encontrar en la pagina el elemento con Xpath "{xpath}" que contenga el texto "{text}"'
)
def found_element_with_text(contexto, xpath, text):
    element_found = contexto.driver.find_element(By.XPATH, xpath)
    text_found = element_found.text
    assert text_found == text


@then('Deberia encontrar en la pagina el elemento con Xpath "{xpath}"')
def found_element_by_xpath(contexto, xpath):
    element_found = contexto.driver.find_element(By.XPATH, xpath)
    assert element_found


@when('Hago una captura de pantalla con nombre "{captura_name}"')
def Make_screenshot(context, captura_name):
    escenario_name = context.scenario.name.replace(" ", "-")
    Crear_carpeta("capturas")
    path = os.path.join("capturas", escenario_name)
    Crear_carpeta(path)
    captura_name = captura_name.replace(" ", "_")
    context.driver.get_screenshot_as_file(f"{path}/{captura_name}.png")


def Crear_carpeta(carpeta_path):
    if not os.path.exists(carpeta_path):
        os.mkdir(carpeta_path)


@when('Identificar los elementos con xpath: "{xpath}"')
def Shearch_all_images(context, xpath):
    context.elementos_found = context.driver.find_elements(
        By.XPATH, xpath
    )  # cuando crea esta variable la crea global


@then("Hacer captura de elementos")
def take_screenshot_for_every_element(context):
    escenario_name = context.scenario.name.replace(" ", "-")
    Crear_carpeta("capturas")
    count = 1
    path = os.path.join("capturas", escenario_name)
    Crear_carpeta(path)
    for elemento in context.elementos_found:
        if elemento.size["width"] > 0 and elemento.size["height"] > 0:
            file_path = os.path.join(path, f"{count}.png")
            elemento.screenshot(file_path)
            count += 1


def after_scenario(context, scenario):
    context.driver.quit()
