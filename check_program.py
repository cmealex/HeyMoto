import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://heymoto.ro/programator/index.php/home")
time.sleep(1)
assert "Login programator" in driver.title
driver.find_element_by_id("txt_username").send_keys("alexsam20032003@yahoo.com")
driver.find_element_by_id("txt_password").send_keys("33Locked")
driver.find_element_by_id("btn_login").click()
time.sleep(2)
assert "Scoala de soferi Hey Moto" in driver.title
driver.find_element_by_partial_link_text("Calendar teorie").click()
time.sleep(2)

tabel_programator = driver.find_element_by_xpath("//table[contains(@class,'tableProgramari')]")
tbody_programator = tabel_programator.find_element_by_tag_name("tbody")
trs = tbody_programator.find_elements_by_tag_name("tr")
open_slots = []
for i in trs:
    tds = i.find_elements_by_tag_name("td")
    for j in tds:
        if "programare" in j.get_attribute("class"):
            open_slots.append(j.get_attribute("data-date"))
if len(open_slots)>0:
    msg = open_slots
    # print(open_slots)
driver.close()


def send_email(user, pwd, recipient, subject, body):
    import smtplib
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

to_list = ["salexcme@gmail.com"]
send_email("alexrinf", "4Testing", to_list, "Liber la programator HeyMoto", msg)