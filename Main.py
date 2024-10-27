# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import whisper
import warnings

warnings.filterwarnings("ignore")

# Load the Whisper model
model = whisper.load_model("base")

def transcribe(url):
    # Download and transcribe audio from the provided URL
    with open('.temp', 'wb') as f:
        f.write(requests.get(url).content)
    result = model.transcribe('.temp')
    return result["text"].strip()

def click_checkbox(driver):
    # Switch to the reCAPTCHA iframe and click the checkbox
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
    driver.find_element(By.ID, "recaptcha-anchor").click()
    driver.switch_to.default_content()

def request_audio_version(driver):
    # Switch to the challenge iframe and request the audio version of the CAPTCHA
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
    driver.find_element(By.ID, "recaptcha-audio-button").click()

def solve_audio_captcha(driver):
    # Transcribe the audio CAPTCHA and enter the response
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
    audio_url = driver.find_element(By.ID, "audio-source").get_attribute('src')
    text = transcribe(audio_url)
    driver.find_element(By.ID, "audio-response").send_keys(text)
    driver.find_element(By.ID, "recaptcha-verify-button").click()

if __name__ == "__main__":
    # Initialize the Chrome WebDriver using ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  
    # Open the demo reCAPTCHA page
    driver.get("https://ebill.leco.lk/Home/CaptchaChallenge/0508964808")
    
    # Perform actions to solve the reCAPTCHA
    click_checkbox(driver)
    time.sleep(1)
    request_audio_version(driver)
    time.sleep(1)
    solve_audio_captcha(driver)
    time.sleep(10)

    # Close the driver
    driver.quit()
