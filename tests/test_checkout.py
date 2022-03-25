import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from tests.BaseClass import BaseClass


class TestExample(BaseClass):


    @pytest.mark.smoke
    def test_guestcheckout(self, setup_teardown):

        log = self.get_logger()
        firefox_options = webdriver.FirefoxOptions()
        #firefox_options.headless = True
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        log.info("Driver object initialized to Firefox")

        driver.get("https://askomdch.com/")
        driver.maximize_window()

        btn_shopnow = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                      ((By.CSS_SELECTOR, "a.wp-block-button__link")))

        btn_shopnow.click()

        txt_search = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                     ((By.CSS_SELECTOR, "input#woocommerce-product-search-field-0")))

        txt_search.send_keys("blue shoes")

        btn_search = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                     ((By.XPATH, "//button[@value='Search']")))

        btn_search.click()

        btn_addtocart = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                        ((By.CSS_SELECTOR, "button.single_add_to_cart_button")))

        btn_addtocart.click()

        btn_viewcart = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                       ((By.XPATH, "//a[@class='button wc-forward'][@tabindex=1]")))

        btn_viewcart.click()

        btn_proceedtocheckout = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                                ((By.XPATH, "//a[contains(.,'Proceed to checkout')]")))

        btn_proceedtocheckout.click()

        # Enter details at the checkout page

        driver.find_element(By.CSS_SELECTOR, "input#billing_first_name").send_keys("Gibberish")
        driver.find_element(By.CSS_SELECTOR, "input#billing_last_name").send_keys("Gibberish")

        driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(driver, 10).
                              until(expected_conditions.visibility_of_element_located
                                    ((By.XPATH, "//span[@id='select2-billing_country-container']"))))

        moveto_country_drpdwn = driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']")
        ActionChains(driver).move_to_element(moveto_country_drpdwn).click().perform()

        country_txt_drpdwn = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                             ((By.CSS_SELECTOR, "input.select2-search__field")))
        country_txt_drpdwn.send_keys("India")

        ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//li[text()='India']")).click().perform()

        WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located
                                        ((By.XPATH, "//div[@class='blockUI blockOverlay']")))

        # drpdwn_country = Select(driver.find_element(By.ID, "billing_country"))
        # drpdwn_country.select_by_value("India")

        driver.find_element(By.CSS_SELECTOR, "input#billing_address_1").send_keys("Street1")
        driver.find_element(By.CSS_SELECTOR, "input#billing_city").send_keys("Pune")

        driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(driver, 10).
                              until(expected_conditions.visibility_of_element_located
                                    ((By.XPATH, "//span[@id='select2-billing_state-container']"))))

        moveto_state_drpdwn = driver.find_element(By.XPATH, "//span[@id='select2-billing_state-container']")

        ActionChains(driver).move_to_element(moveto_state_drpdwn).click().perform()

        state_txt_drpdwn = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                           ((By.CSS_SELECTOR, "input.select2-search__field")))
        state_txt_drpdwn.send_keys("Maharashtra")
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//li[text()='Maharashtra']")).click().perform()

        WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located
                                        ((By.XPATH, "//div[@class='blockUI blockOverlay']")))

        driver.find_element(By.CSS_SELECTOR, "input#billing_postcode").send_keys("401401")
        driver.find_element(By.CSS_SELECTOR, "input#billing_email").send_keys("gibberish@gmail.com")

        driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(driver, 10).
                              until(expected_conditions.element_to_be_clickable
                                    ((By.XPATH, "//label[@for='payment_method_bacs']"))))

        radio_banktransfer = driver.find_element(By.XPATH, "//label[@for='payment_method_bacs']")

        WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located
                                        ((By.XPATH, "//div[@class='blockUI blockOverlay']")))

        if radio_banktransfer.is_selected() == False:
            radio_banktransfer.click()

        btn_placeorder = driver.find_element(By.ID, "place_order")
        btn_placeorder.click()

        lbl_success_order = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located
                                                            ((By.XPATH,
                                                              "//p[text()='Thank you. Your order has been received.']")))

        assert 'Thank you. Your order has been received.', lbl_success_order.text

        driver.close()

    @pytest.mark.regression
    def test_userchekcout(self, setup_teardown):
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.headless = True
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

        driver.get("https://askomdch.com/")
        driver.maximize_window()

        btn_shopnow = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                      ((By.CSS_SELECTOR, "a.wp-block-button__link")))

        btn_shopnow.click()

        txt_search = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                     ((By.CSS_SELECTOR, "input#woocommerce-product-search-field-0")))

        txt_search.send_keys("blue shoes")

        btn_search = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                     ((By.XPATH, "//button[@value='Search']")))

        btn_search.click()

        btn_addtocart = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                        ((By.CSS_SELECTOR, "button.single_add_to_cart_button")))

        btn_addtocart.click()

        btn_viewcart = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                       ((By.XPATH, "//a[@class='button wc-forward'][@tabindex=1]")))

        btn_viewcart.click()

        btn_proceedtocheckout = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                                ((By.XPATH, "//a[contains(.,'Proceed to checkout')]")))

        btn_proceedtocheckout.click()

        #######

        driver.find_element(By.CSS_SELECTOR, "a.showlogin").click()

        username = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                   ((By.ID, "username")))
        username.send_keys("gibuser1")

        password = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                                   ((By.ID, "password")))
        password.send_keys("password")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located
                                        ((By.XPATH, "//button[@type='submit']")))

        WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located
                                        ((By.XPATH, "//div[@class='blockUI blockOverlay']")))

        """
        overlay = driver.find_elements(By.XPATH, "//div[@class='blockUI blockOverlay']")
    
        while len(overlay) > 0:
            print("overlay size: ", len(overlay))
            WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located
                                            ((By.XPATH, "//div[@class='blockUI blockOverlay']")))
    
            overlay = driver.find_elements(By.XPATH, "//div[@class='blockUI blockOverlay']")
        
        radio_banktransfer = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable
                                                             ((By.XPATH, "//label[@for='payment_method_bacs']")))
    
        
        if radio_banktransfer.is_selected() == False:
            radio_banktransfer.click()
        """

        btn_placeorder = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable
                                                         ((By.ID, "place_order")))

        btn_placeorder.click()

        lbl_success_order = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located
                                                            ((By.XPATH,
                                                              "//p[text()='Thank you. Your order has been received.']")))

        assert 'Thank you. Your order has been received.', lbl_success_order.text

        driver.close()

