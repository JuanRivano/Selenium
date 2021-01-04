from Conexion import connectChrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import  time

def BuscarRegistroCivil(rut):
    driver=connectChrome("https://www.registrocivil.cl/principal/servicios-en-linea")
    driver.switch_to.frame("IframeOI")
    try:
        name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "title_1")))
    except:
        print("No carga pagina")
    titulo1=driver.find_element_by_id('title_1')
    titulo2=driver.find_element_by_id('title_0')
    titulo1.click()
    titulo2.click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[7]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[1]/div/ins').click()
    driver.find_element_by_class_name('inputRunCertificado').send_keys(rut)
    driver.find_element_by_xpath('//button[starts-with(@id,"btn_agregarCarro_1")]').click()
    time.sleep(2)
    driver.find_element_by_id('carro_solicitanteInputEmail').send_keys('juanrivano@gmail.com')
    driver.find_element_by_id('carro_solicitanteInputEmailConfirm').send_keys('juanrivano@gmail.com')
    driver.find_element_by_id('carro_btnContinuar').click()
    time.sleep(1)