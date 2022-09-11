from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait

driver = webdriver.Chrome("C:/Users/kirtishb/Downloads/chromedriver/chromedriver.exe")

driver.get("http://illin3692/evtgen/evt_update.php?accountMain=ComcastMidMarket&envSelected=Env94_R15_PROD&typeSelected=Ordering")


select = driver.find_element_by_id( 'accountVals')  #get the select element            
options = select.find_elements_by_tag_name("option") #get all the options into a list

optionsList = []

for option in options: #iterate over the options, place attribute value in list
    optionsList.append(option.get_attribute("value"))
    print(option.text)

print(optionsList)

# for optionValue in optionsList:
#     print("starting loop on option %s", optionValue)
#     select = Select(driver.find_element_by_id('accountVals'))
#     select.select_by_value(optionValue)


# print("Hello " + driver.title)

# print("hello" + str(driver.find_element_by_id("accountVals")))