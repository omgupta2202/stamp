from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from .models import *
import time, json
from django.http import HttpResponse, JsonResponse, FileResponse
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .forms import *
import os
from django.conf import settings
import pandas as pd
from datetime import datetime
from django.core.serializers import serialize
import urllib3
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def home(request):
    return render(request, 'app/app.html')

def save_search_data(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        district_registered = request.POST.get('district_registered')
        district_search = request.POST.get('district_search')
        financial_year = request.POST.get('financial_year')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        search_registered_sampada = request.POST.get('search_registered_sampada') == 'on'
        # district = request.POST.get('district')
        # tehsil = request.POST.get('tehsil')
        # type_of_area = request.POST.get('type_of_area')
        # sub_area_type = request.POST.get('sub_area_type')
        # ward_number_patwari_number = request.POST.get('ward_number_patwari_number')
        # mohalla_colony_name_society_road = request.POST.get('mohalla_colony_name_society_road')
        khasra_number = request.POST.get('khasra_number')
        transacting_party_first_name = request.POST.get('transacting_party_first_name')
        transacting_party_middle_name = request.POST.get('transacting_party_middle_name')
        transacting_party_last_name = request.POST.get('transacting_party_last_name')
        transacting_party_mother_name = request.POST.get('transacting_party_mother_name')
        transacting_party_father_name = request.POST.get('transacting_party_father_name')
        organization_name = request.POST.get('organization_name')

        registration = Details(
            username= username,
            district_registered=district_registered,
            district_search=district_search,
            search_registered_sampada=search_registered_sampada,
            financial_year=financial_year,
            from_date=from_date,
            to_date=to_date,
            # district=district,
            # tehsil=tehsil,
            # type_of_area=type_of_area,
            # sub_area_type=sub_area_type,
            # ward_number_patwari_number=ward_number_patwari_number,
            # mohalla_colony_name_society_road=mohalla_colony_name_society_road,
            khasra_number=khasra_number,
            transacting_party_first_name=transacting_party_first_name,
            transacting_party_middle_name=transacting_party_middle_name,
            transacting_party_last_name=transacting_party_last_name,
            transacting_party_mother_name=transacting_party_mother_name,
            transacting_party_father_name=transacting_party_father_name,
            organization_name=organization_name,
        )
        registration.save()
        print("Data has been collected and saved to the database.")
        return render(request, 'app/app.html')
    else:
        return HttpResponse("Invalid request method.")

district_instance = None
tehsil_instance = None
type_of_area_instance = None
sub_area_type_instance = None
ward_number_patwari_number_instance = None
mohalla_colony_name_society_road_instance = None

def open_login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    username= username
    password= password
    notification_file = f'notification_{username}.txt'
    notification_path = os.path.join(settings.MEDIA_ROOT, notification_file)
    if os.path.exists(notification_path):
        os.remove(notification_path)
    details_instance = Details.objects.get(username = username)
    district_registered = details_instance.district_registered
    district_search = details_instance.district_search
    search_registered_sampada = details_instance.search_registered_sampada
    financial_year = details_instance.financial_year
    from_date = details_instance.from_date
    to_date = details_instance.to_date
    # district = details_instance.district
    # tehsil = details_instance.tehsil
    # type_of_area = details_instance.type_of_area
    # sub_area_type = details_instance.sub_area_type
    # ward_number_patwari_number = details_instance.ward_number_patwari_number
    # mohalla_colony_name_society_road = details_instance.mohalla_colony_name_society_road
    khasra_number = details_instance.khasra_number
    transacting_party_first_name = details_instance.transacting_party_first_name
    transacting_party_middle_name = details_instance.transacting_party_middle_name
    transacting_party_last_name = details_instance.transacting_party_last_name
    transacting_party_mother_name = details_instance.transacting_party_mother_name
    transacting_party_father_name = details_instance.transacting_party_father_name
    organization_name = details_instance.organization_name
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("window-size=1400,1500")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = '/home/ubuntu/google-chrome'
    chrome_driver_path = "/home/ubuntu/chromedriver"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://www.mpigr.gov.in:8080/IGRS/')

    captcha_filename = f'captcha_{username}_value.txt'
    file_path = os.path.join(settings.MEDIA_ROOT, captcha_filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    
    
    
    captcha_filename_form = f'captcha_{username}_value2.txt'
    file_path_form = os.path.join(settings.MEDIA_ROOT, captcha_filename_form)
    
    district_filename = f'district_{username}_value2.txt'
    district_file_path = os.path.join(settings.MEDIA_ROOT, district_filename)
    if os.path.exists(district_file_path):
        os.remove(district_file_path)
    
    tehsil_filename = f'tehsil_{username}_value2.txt'
    tehsil_file_path = os.path.join(settings.MEDIA_ROOT, tehsil_filename)
    if os.path.exists(tehsil_file_path):
        os.remove(tehsil_file_path)
    
    image_filename = f'captcha_{username}.png'
    image_path = os.path.join(settings.MEDIA_ROOT, image_filename) 
    if os.path.exists(image_path):
        os.remove(image_path)
    
    image_filename_form = f'captcha_{username}_form.png'
    image_path_form = os.path.join(settings.MEDIA_ROOT, image_filename_form) 
    if os.path.exists(image_path_form):
        os.remove(image_path_form)
        
    type_of_area_filename = f'type_of_area_{username}_value2.txt'
    type_of_area_file_path = os.path.join(settings.MEDIA_ROOT, type_of_area_filename)
    if os.path.exists(type_of_area_file_path):
        os.remove(type_of_area_file_path)
        
    sub_area_type_filename = f'sub_area_type_{username}_value2.txt'
    sub_area_type_file_path = os.path.join(settings.MEDIA_ROOT, sub_area_type_filename)
    if os.path.exists(sub_area_type_file_path):
        os.remove(sub_area_type_file_path)
    
    ward_number_patwari_number_filename = f'ward_number_patwari_number_{username}_value2.txt'
    ward_number_patwari_number_file_path = os.path.join(settings.MEDIA_ROOT, ward_number_patwari_number_filename)
    if os.path.exists(ward_number_patwari_number_file_path):
        os.remove(ward_number_patwari_number_file_path)
        
    mohalla_colony_name_society_road_filename = f'mohalla_colony_name_society_road_{username}_value2.txt'
    mohalla_colony_name_society_road_file_path = os.path.join(settings.MEDIA_ROOT, mohalla_colony_name_society_road_filename)
    if os.path.exists(mohalla_colony_name_society_road_file_path):
        os.remove(mohalla_colony_name_society_road_file_path)
        
    changedDropdown_filename = f'changedDropdown_{username}.txt'
    changedDropdown_file_path = os.path.join(settings.MEDIA_ROOT, changedDropdown_filename)
    if os.path.exists(changedDropdown_file_path):
        os.remove(changedDropdown_file_path)

    notify = "mpigr site opened."
    with open(notification_path, 'w') as file:
        file.write(notify)
            
    loc_name = r'untitled'
    loc = os.path.join(settings.MEDIA_ROOT, loc_name) 
    if not os.path.exists(loc):
        os.makedirs(loc)
        
    def login():
        username_input = driver.find_element(By.NAME, "userId")
        username_input.send_keys(username)
        
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        
        language_radio = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][name="language"][value="en"]')
        language_radio.click()

        captcha_element = driver.find_element(By.XPATH, "//img[@src='/IGRS/jcaptcha']")
        captcha_screenshot = captcha_element.screenshot_as_png

        notify = "Username and Password filled and language selected as english. Enter Captcha"
        with open(notification_path, 'w') as file:
            file.write(notify)

        with open(image_path, 'wb') as file:
            file.write(captcha_screenshot)
            
        # Read content from the file

        max_wait_time = 240  # You can adjust this value

        # Wait for the file to exist
        start_time = time.time()
        while not os.path.exists(file_path):
            # Check if the maximum wait time has been exceeded
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                notify = "Time limit exceeded. Some problem occured with mpigr site."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                break

            # Wait for a short duration before checking again
            time.sleep(1)
        with open(file_path, 'r') as file:
            captcha_content = file.read()

        notify = "Captcha entered. Wait for a while."
        with open(notification_path, 'w') as file:
            file.write(notify)
        # Find the captcha code input field and enter the content
        captcha_code_input = driver.find_element(By.ID, "capthca")
        captcha_code_input.send_keys(captcha_content)

        
        login_button = driver.find_element(By.NAME, "Button")
        login_button.click()
    login()
    
    try:
        wait = WebDriverWait(driver, 3)
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        if password_input:
            notify = "Captcha was incorrect. Please refresh the page and login again."
            with open(notification_path, 'w') as file:
                file.write(notify)
            return HttpResponse("Captcha was incorrect. Please reload the homepage and start with step 2 again.")
    except:
        pass

    def newsearch():
        try:
            print("Waiting for the page to load...")
            wait = WebDriverWait(driver, 15)  # Adjust the timeout as needed
            element = wait.until(EC.presence_of_element_located((By.ID, 'ulaitem0_5')))
        
            if element:
                print("Opening New Search...")
                element.click()
                time.sleep(1)
                driver.find_element(By.ID, 'ulaitem0_5_1').click()
                time.sleep(1)
                driver.find_element(By.ID, 'ulitem0_5_1_0').click()
                time.sleep(1)
                driver.find_element(By.LINK_TEXT, 'NEW SEARCH').click()
            else:
                print("An error occurred. The element was not found within the timeout.")
                notify = "An error occurred. Either the captcha was wrong or some problem occured with mpigr site. Please refresh page and start step 2 again."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                driver.quit()
                return HttpResponse("Captcha was incorrect. Please reload the homepage and start with step 2 again.")
        except NoSuchElementException as e:
            print("Capthca was incorrect. Please start with step 2 again.")
            driver.quit()
            return HttpResponse("Captcha was incorrect. Please reload the homepage and start with step 2 again.")
    newsearch()
    
    district_dropdown = driver.find_element(By.NAME, "dsearchdto.hdnRegDistId")
    select = Select(district_dropdown)
    select.select_by_value(district_registered)
    time.sleep(1)
    
    district_parts = district_search.split("~")
    district_value = district_parts[1]
    district_name_input = driver.find_element(By.NAME, "dsearchdto.hdnDistName")
    district_name_input.clear()
    district_name_input.send_keys(district_value)
    time.sleep(1)

    if search_registered_sampada:
        driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][name="dsearchdto.radiobutton"][value="n"]').click()
    else:
        driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][name="dsearchdto.radiobutton"][value="o"]').click()
    time.sleep(1)
        
    def calendar():
        select_element = driver.find_element(By.NAME, "dsearchdto.fiscalYearId")
        select = Select(select_element)
        select.select_by_value(financial_year)
        
        calendar_button = driver.find_element(By.XPATH,"//a[contains(@href, 'show_calendar')]")
        calendar_button.click()
        
        #from date
        desired_date = Details.objects.values('from_date').first()['from_date']
        desired_date_string = desired_date.strftime('%B %d, %Y')
        desired_month, desired_day, desired_year = desired_date_string.split()
        desired_day = desired_day
        
        driver.switch_to.window(driver.window_handles[-1])
    
        while True:
            
            current_month_and_year = driver.find_element(By.TAG_NAME, 'b').text
            # print(current_month_and_year)
            
            parts = current_month_and_year.split()
            current_month = parts[0]
            current_year = parts[1] if len(parts) > 1 else ''
            # print(current_month)
            # print(current_year) 

            if current_month == desired_month and current_year == desired_year:
                break
            next_month_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'documentsearchtypeAone.fromDate')]")
            next_month_link = next_month_links[1]
            next_month_link.click()

        desired_date_string = desired_date.strftime('%d/%m/%Y')
        date_element = driver.find_element(By.XPATH, f"//a[@onclick=\"self.opener.document.documentsearchtypeAone.fromDate.value='{desired_date_string}';window.close();\"]")
        date_element.click()
        driver.switch_to.window(driver.window_handles[0])
        
        #to date
        desired_date = Details.objects.values('to_date').first()['to_date']
        desired_date_string = desired_date.strftime('%B %d, %Y')
        desired_month, desired_day, desired_year = desired_date_string.split()
        desired_day = desired_day
        
        calendar_button = driver.find_element(By.XPATH,"//a[contains(@href, 'documentsearchtypeAone.toDate')]")
        calendar_button.click()
        
        driver.switch_to.window(driver.window_handles[-1])

        while True:
            
            current_month_and_year = driver.find_element(By.TAG_NAME, 'b').text
            parts = current_month_and_year.split()
            current_month = parts[0]
            current_year = parts[1] if len(parts) > 1 else ''
            if current_month == desired_month and current_year == desired_year:
                break
            next_month_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'documentsearchtypeAone.toDate')]")
            next_month_link = next_month_links[1]
            next_month_link.click()

        desired_date_string = desired_date.strftime('%d/%m/%Y')
        date_element = driver.find_element(By.XPATH, f"//a[@onclick=\"self.opener.document.documentsearchtypeAone.toDate.value='{desired_date_string}';window.close();\"]")
        date_element.click()
        driver.switch_to.window(driver.window_handles[0])
    calendar()
    notify = "Page Loading. Please wait!"
    with open(notification_path, 'w') as file:
            file.write(notify)
    
    def districtSearchBeforeSelections():
        global district_instance
        district_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.distId"))
        )
        select = Select(district_dropdown)
        district_options = [option.text for option in select.options if option.text != 'Select']
        for district_name in district_options:
            districts = District.objects.get_or_create(name=district_name)
        print(districts)
        select = Select(district_dropdown)
        notify = "Initial District and From Date, To Date in Calendar filled. Please continue ahead."
        with open(notification_path, 'w') as file:
            file.write(notify)
    districtSearchBeforeSelections()
    
    def district():
        global district_instance
        district_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.distId"))
        )       
        select = Select(district_dropdown)
        max_wait_time = 240
        start_time = time.time()
        while not os.path.exists(district_file_path):
            # Check if the maximum wait time has been exceeded
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                notify = "District not entered within specified time."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                break
            time.sleep(1)
        notify = "Please fill other details..."
        with open(notification_path, 'w') as file:
            file.write(notify)
        with open(district_file_path, 'r') as file:
            district_instance = file.read()
            print(district_instance)
            select.select_by_visible_text(district_instance)
        
        if os.path.exists(district_file_path):
            os.remove(district_file_path)
        
        tehsil_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.tehisilId"))
        )
        district_instance = District.objects.get(name=district_instance)
        select = Select(tehsil_dropdown)
        tehsil_options = [option.text for option in select.options if option.text != 'Select']
        print(tehsil_options)
        tehsils = None
        for tehsil_name in tehsil_options:
            tehsils = Tehsil.objects.get_or_create(name=tehsil_name, state=district_instance)
        print(tehsils)
        
    def tehsil():
        # global district_instance
        # global tehsil_instance
        
        tehsil_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.tehisilId"))
        )
        # district_instance = District.objects.get(name=district_instance)
        select = Select(tehsil_dropdown)
        # tehsil_options = [option.text for option in select.options if option.text != 'Select']
        # print(tehsil_options)
        # for tehsil_name in tehsil_options:
        #     tehsils = Tehsil.objects.get_or_create(name=tehsil_name, state=district_instance)
        # print(tehsils)
        max_wait_time = 240
        start_time = time.time()
        while not os.path.exists(tehsil_file_path):
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                notify ="Details not found within the specified time."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                break
            time.sleep(1)
        global tehsil_instance
        with open(tehsil_file_path, 'r') as file:
            global tehsil_instance
            tehsil_instance = file.read()
            print(tehsil_instance)
            select.select_by_visible_text(tehsil_instance)
        
        if os.path.exists(tehsil_file_path):
            os.remove(tehsil_file_path)

        global type_of_area_instance
        type_of_area_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.areaTypeId"))
        )
        tehsil_instance = Tehsil.objects.get(name=tehsil_instance)
        select = Select(type_of_area_dropdown)
        type_of_area_options = [option.text for option in select.options if option.text != 'Select']
        type_of_areas = None
        if type_of_area_options is not None:
            print(type_of_area_options)
        for type_of_area_name in type_of_area_options:
            type_of_areas = TypeOfArea.objects.get_or_create(name=type_of_area_name, tehsil=tehsil_instance)
        print(type_of_areas)
    
    def area():
        # global tehsil_instance
        # global type_of_area_instance
        type_of_area_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.areaTypeId"))
        )
        # tehsil_instance = Tehsil.objects.get(name=tehsil_instance)
        select = Select(type_of_area_dropdown)
        # type_of_area_options = [option.text for option in select.options if option.text != 'Select']
        # print(type_of_area_options)
        # for type_of_area_name in type_of_area_options:
        #     type_of_areas = TypeOfArea.objects.get_or_create(name=type_of_area_name, tehsil=tehsil_instance)
        # print(type_of_areas)
        max_wait_time = 240
        start_time = time.time()
        while not os.path.exists(type_of_area_file_path):
            # Check if the maximum wait time has been exceeded
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                notify ="Details not found within the specified time."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                break

            # Wait for a short duration before checking again
            time.sleep(1)
        global type_of_area_instance
        global tehsil_instance
        with open(type_of_area_file_path, 'r') as file:
            global type_of_area_instance
            type_of_area_instance = file.read()
            print(type_of_area_instance)
            select.select_by_visible_text(type_of_area_instance)
        
        if os.path.exists(type_of_area_file_path):
            os.remove(type_of_area_file_path)


        sub_area_type_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.subAreaTypeId"))
        )
        type_of_area_instance = TypeOfArea.objects.get(name=type_of_area_instance, tehsil=tehsil_instance)
        select = Select(sub_area_type_dropdown)
        sub_area_type_options = [option.text for option in select.options if option.text != 'Select']
        print(sub_area_type_options)
        for sub_area_type_name in sub_area_type_options:
            sub_area_types = SubArea.objects.get_or_create(name=sub_area_type_name, typeofarea=type_of_area_instance)
        print(sub_area_types)
        
    def sub():
        # global type_of_area_instance
        # global tehsil_instance
        # global sub_area_type_instance
        sub_area_type_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.subAreaTypeId"))
        )
        # type_of_area_instance = TypeOfArea.objects.get(name=type_of_area_instance, tehsil=tehsil_instance)
        select = Select(sub_area_type_dropdown)
        # sub_area_type_options = [option.text for option in select.options if option.text != 'Select']
        # print(sub_area_type_options)
        # for sub_area_type_name in sub_area_type_options:
        #     sub_area_types = SubArea.objects.get_or_create(name=sub_area_type_name, typeofarea=type_of_area_instance)
        # print(sub_area_types)
        max_wait_time = 240
        start_time = time.time()
        while not os.path.exists(sub_area_type_file_path):
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                notify ="Details not found within the specified time."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                break
            time.sleep(1)
        global type_of_area_instance
        global sub_area_type_instance
        with open(sub_area_type_file_path, 'r') as file:
            global sub_area_type_instance
            sub_area_type_instance = file.read()
            print(sub_area_type_instance)
            select.select_by_visible_text(sub_area_type_instance)
        if os.path.exists(sub_area_type_file_path):
            os.remove(sub_area_type_file_path)
        
        ward_number_patwari_number_filename = f'ward_number_patwari_number_{username}_value2.txt'
        ward_number_patwari_number_file_path = os.path.join(settings.MEDIA_ROOT, ward_number_patwari_number_filename)
        if os.path.exists(ward_number_patwari_number_file_path):
            os.remove(ward_number_patwari_number_file_path)
        
        ward_number_patwari_number_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.subAreaWardMappingId"))
        )
        sub_area_type_instance = SubArea.objects.get(name=sub_area_type_instance, typeofarea=type_of_area_instance)
        select = Select(ward_number_patwari_number_dropdown)
        ward_number_patwari_number_options = [option.text for option in select.options if option.text != 'Select']
        ward_number_patwari_number_options
        ward_number_patwari_numbers = None
        for ward_number_patwari_number_name in ward_number_patwari_number_options:
            ward_number_patwari_numbers = WardPatwariNumber.objects.get_or_create(name=ward_number_patwari_number_name, subarea=sub_area_type_instance)
        if ward_number_patwari_numbers is not None:
            print(ward_number_patwari_numbers)
    
    def ward():
        # global type_of_area_instance
        # global sub_area_type_instance
        # ward_number_patwari_number_filename = f'ward_number_patwari_number_{username}_value2.txt'
        # ward_number_patwari_number_file_path = os.path.join(settings.MEDIA_ROOT, ward_number_patwari_number_filename)        
        ward_number_patwari_number_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.subAreaWardMappingId"))
        )
        # sub_area_type_instance = SubArea.objects.get(name=sub_area_type_instance, typeofarea=type_of_area_instance)
        select = Select(ward_number_patwari_number_dropdown)
        # ward_number_patwari_number_options = [option.text for option in select.options if option.text != 'Select']
        # print(ward_number_patwari_number_options)
        # for ward_number_patwari_number_name in ward_number_patwari_number_options:
        #     ward_number_patwari_numbers = WardPatwariNumber.objects.get_or_create(name=ward_number_patwari_number_name, subarea=sub_area_type_instance)
        
        # print(ward_number_patwari_numbers)
        global ward_number_patwari_number_instance
        global sub_area_type_instance
        max_wait_time = 240
        start_time = time.time()
        while not os.path.exists(ward_number_patwari_number_file_path):
            # Check if the maximum wait time has been exceeded
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                notify ="Details not found within the specified time."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                break

            # Wait for a short duration before checking again
            time.sleep(1)
        with open(ward_number_patwari_number_file_path, 'r') as file:
            global ward_number_patwari_number_instance
            ward_number_patwari_number_instance = file.read()
            print(ward_number_patwari_number_instance)
            select.select_by_visible_text(ward_number_patwari_number_instance)
        if os.path.exists(ward_number_patwari_number_file_path):
            os.remove(ward_number_patwari_number_file_path)
        
        mohalla_colony_name_society_road_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.mohallaId"))
        )
        ward_number_patwari_number_instance = WardPatwariNumber.objects.get(name=ward_number_patwari_number_instance, subarea=sub_area_type_instance)
        select = Select(mohalla_colony_name_society_road_dropdown)
        mohalla_colony_name_society_road_options = [option.text for option in select.options if option.text != 'Select']
        print(mohalla_colony_name_society_road_options)
        mohalla_colony_name_society_roads = None
        for mohalla_colony_name_society_road_name in mohalla_colony_name_society_road_options:
            mohalla_colony_name_society_roads = SocietyName.objects.get_or_create(name=mohalla_colony_name_society_road_name, ward=ward_number_patwari_number_instance)
        if mohalla_colony_name_society_roads is not None:
            print(mohalla_colony_name_society_roads)
    
    def mohalla():
        # global ward_number_patwari_number_instance
        # global mohalla_colony_name_society_road_instance
        # global sub_area_type_instance
        mohalla_colony_name_society_road_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dsearchdto.mohallaId"))
        )
        # ward_number_patwari_number_instance = WardPatwariNumber.objects.get(name=ward_number_patwari_number_instance, subarea=sub_area_type_instance)
        select = Select(mohalla_colony_name_society_road_dropdown)
        # mohalla_colony_name_society_road_options = [option.text for option in select.options if option.text != 'Select']
        # print(mohalla_colony_name_society_road_options)
        # for mohalla_colony_name_society_road_name in mohalla_colony_name_society_road_options:
        #     mohalla_colony_name_society_roads = SocietyName.objects.get_or_create(name=mohalla_colony_name_society_road_name, ward=ward_number_patwari_number_instance)
        # print(mohalla_colony_name_society_roads)
        global mohalla_colony_name_society_road_instance
        max_wait_time = 240
        start_time = time.time()
        while not os.path.exists(mohalla_colony_name_society_road_file_path):
            # Check if the maximum wait time has been exceeded
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                notify ="Details not found within the specified time."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                break
            # Wait for a short duration before checking again
            time.sleep(1)
        with open(mohalla_colony_name_society_road_file_path, 'r') as file:
            mohalla_colony_name_society_road_instance = file.read()
            print(mohalla_colony_name_society_road_instance)
            select.select_by_visible_text(mohalla_colony_name_society_road_instance)
        if os.path.exists(mohalla_colony_name_society_road_file_path):
            os.remove(mohalla_colony_name_society_road_file_path)
        notify ="Details filled successfully. Please clcik on submit."
        with open(notification_path, 'w') as file:
                    file.write(notify)
    
    
    switch = {
        'district': district,
        'tehsil': tehsil,
        'area': area,
        'sub': sub,
        'ward': ward,
        'mohalla': mohalla,
    }

    while True:
        max_wait_time = 240
        start_time = time.time()
        while not os.path.exists(changedDropdown_file_path):
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                break
            time.sleep(1)
        with open(changedDropdown_file_path, 'r') as file:
            choice = file.read().strip()
        if choice == "default":
            pass
        if choice == "done":
            break
        func = switch.get(choice)
        func()
        if os.path.exists(changedDropdown_file_path):
            os.remove(changedDropdown_file_path)

    if(khasra_number):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.khasraNumber")
        khasra_input.send_keys(khasra_number)
        time.sleep(1)
        
    if(transacting_party_first_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyFirstName")
        khasra_input.send_keys(transacting_party_first_name)
        time.sleep(1)
        
    if(transacting_party_middle_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyMiddName")
        khasra_input.send_keys(transacting_party_middle_name)
        time.sleep(1)
        
    if(transacting_party_last_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyLastName")
        khasra_input.send_keys(transacting_party_last_name)
        time.sleep(1)
    
    if(transacting_party_mother_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyMotName")
        khasra_input.send_keys(transacting_party_mother_name)
        time.sleep(1)
        
    if(transacting_party_father_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyFatName")
        khasra_input.send_keys(transacting_party_father_name)
        time.sleep(1)
        
    if(organization_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.orgName")
        khasra_input.send_keys(organization_name)
        time.sleep(1)
        
    def cap_form():
        #captcha for form
        if os.path.exists(file_path_form):
            os.remove(file_path_form)
        captcha_element = driver.find_element(By.XPATH, "//img[@src='/IGRS/jcaptcha']")
        captcha_screenshot = captcha_element.screenshot_as_png
        
        with open(image_path_form, 'wb') as file:
            file.write(captcha_screenshot)
        notify ="Please click on Show Captcha button and submit captcha."
        with open(notification_path, 'w') as file:
            file.write(notify)
        
        max_wait_time = 300
        start_time = time.time()
        while not os.path.exists(file_path_form):
            if time.time() - start_time > max_wait_time:
                print("File not found within the specified time.")
                notify ="Captcha not entered within specified time. Please start with step 2 again."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                error_message = "Sorry, some problem occurred. Please try again."
                return HttpResponse(error_message, status=500)
                break
            time.sleep(1)
        with open(file_path_form, 'r') as file:
            captcha_content = file.read()
        captcha_code_input = driver.find_element(By.ID, "capthca")
        captcha_code_input.send_keys(captcha_content)
        next_button = driver.find_element(By.NAME, "next")
        next_button.click()
    
    cap_form()
    while True:
        try:
            wait = WebDriverWait(driver, 2)
            captcha_element = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@src='/IGRS/jcaptcha']")))
            if captcha_element:
                notify ="Captcha is wrong. Please click on show captcha and submit captcha again."
                with open(notification_path, 'w') as file:
                    file.write(notify)
                cap_form()
        except:
            notify = "Verifying Captcha"
            with open(notification_path, 'w') as file:
                file.write(notify)
            wait = WebDriverWait(driver, 15)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lastFormValue")))
            break
    element= driver.find_element(By.CLASS_NAME, "lastFormValue")
    text_content = element.text
    expected_text = "Data Not Available for Given Search Criteria"
    if text_content == expected_text:
        notify = text_content
        # Do something with the 'notify' variable, such as writing it to a file
        with open(notification_path, 'w') as file:
            file.write(notify)
        file_content = notify
        response = FileResponse(file_content, as_attachment=True)
        response = HttpResponse(file_content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="NoDataFound.xlsx"'
        return response

    # Creating a empty DataFrame
    data = {
        "Sr. No.": [],
        "Registration No.": [],
        "Date of Reg.":[],
        "Buyer Name": [],
        "Buyer's Address": [],
        "Buyer's Number": [],
        "Seller Name": [],
        "Seller's Address": [],
        "Seller's Number": [],
        "Ward/Patwari Halka": [],
        "Ward/Patwari Halka Name": [],
        "Property Address": [],
        "Plot No.": [],
        "North": [],
        "South": [],
        "East": [],
        "West": []
    }
    df = pd.DataFrame(data)

    def collection(i, date):
    # Function of Collectiong Data from the Profile
        row = {}
            
        try:
            reg_td =  driver.find_element(By.XPATH, "//td[contains(text(), 'e Registration Number')]")
            reg = reg_td.find_element(By.XPATH, "./following-sibling::td").text.strip()
        except:
            reg = "None"

        try:
            bfnm_td =  driver.find_element(By.XPATH, "//td[contains(text(), 'First Name')]")
            bfnm = bfnm_td.find_element(By.XPATH, "./following-sibling::td").text.strip()
            blnm_td =  driver.find_element(By.XPATH, "//td[contains(text(), 'Last Name')]")
            blnm = blnm_td.find_element(By.XPATH, "./following-sibling::td").text.strip()
            bname = bfnm + " " + blnm  
        except:
            try:
                bname_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Authorized Person Name')]")
                bname = bname_td[0].find_element(By.XPATH, "./following-sibling::td").text.strip()
            except:
                bname = "None"

        try:
            add_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Address')]")
            badd = add_td[0].find_element(By.XPATH, "./following-sibling::td").text.strip()
        except:
            badd = "None"
        try:
            ph_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Mobile Number')]")
            bph = ph_td[0].find_element(By.XPATH, "./following-sibling::td").text.strip()
        except:
            bph = "None"

        try:
            try:
                snm_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Authorized Person Name')]")
                snm = snm_td[-1].find_element(By.XPATH, "./following-sibling::td").text.strip()
                add_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Address')]")
                sadd = add_td[-2].find_element(By.XPATH, "./following-sibling::td").text.strip()
                if '@' in sadd:
                    sadd = add_td[-3].find_element(By.XPATH, "./following-sibling::td").text.strip()
            except:
                sfnm_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'First Name')]")
                sfnm = sfnm_td[-1].find_element(By.XPATH, "./following-sibling::td").text.strip()
                slnm_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Last Name')]")
                slnm = slnm_td[-1].find_element(By.XPATH, "./following-sibling::td").text.strip()
                snm = sfnm + " " + slnm  
                add_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Address')]")
                sadd = add_td[-3].find_element(By.XPATH, "./following-sibling::td").text.strip()
                if '@' in sadd:
                    sadd = add_td[-4].find_element(By.XPATH, "./following-sibling::td").text.strip()
            ph_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Mobile Number')]")
            sph = ph_td[-1].find_element(By.XPATH, "./following-sibling::td").text.strip()
        except:
            snm = "None"
            sadd= "None"
            sph = "None"
        try:
            halka_td =  driver.find_element(By.XPATH, "//td[contains(text(), 'Ward/Patwari Halka')]")
            halka = halka_td.find_element(By.XPATH, "./following-sibling::td").text.strip()
        except:
            halka = "None"

        try:
            halka_name_td =  driver.find_element(By.XPATH, "//td[contains(text(), 'Ward/patwari Halka Name')]")
            halka_name = halka_name_td.find_element(By.XPATH, "./following-sibling::td").text.strip()
        except:
            halka_name = "None"

        try:
            add_td =  driver.find_elements(By.XPATH, "//td[contains(text(), 'Address')]")
            padd = add_td[-1].find_element(By.XPATH, "./following-sibling::td").text.strip()  
        except:
            padd = "None"

        try:
            driver.find_element(By.XPATH, "//td[contains(text(), 'Khasra Details')]")
            property_rows =  driver.find_elements(By.XPATH, "//tr[td[@class='lastFormValue']]")
            property_details = []
            for row in property_rows:
                cells = row.find_elements(By.CLASS_NAME, "lastFormValue")
                if len(cells) >= 8:
                    details = [cell.text.strip() for cell in cells]
                    property_details.append(details)
            for details in property_details:
                khasra_number = details[0]
                north = details[4]
                south = details[5]
                east = details[6]
                west = details[7]
        except:
            try:
                plot_num = re.findall(r'\d+\.\d+|\d+', padd)
                khasra_number = plot_num[0]
            except:
                khasra_number = "None"
            north = "None"
            south = "None"
            east = "None"
            west = "None"

        row_details = {
            "Sr. No.": i,
            "Registration No.": reg,
            "Date of Reg.": date,
            "Buyer Name": bname,
            "Buyer's Address": badd,
            "Buyer's Number": bph,
            "Seller Name": snm,
            "Seller's Address": sadd,
            "Seller's Number": sph,
            "Ward/Patwari Halka": halka,
            "Ward/Patwari Halka Name": halka_name,
            "Property Address": padd,
            "Plot No.": khasra_number,
            "North": north,
            "South": south,
            "East": east,
            "West": west
        }
        return row_details

    # Automating Profile Randering
    c = 0
    wait = WebDriverWait(driver, 1800)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//th[contains(text(), "Date Of Registration")]')))
        time.sleep(5)
        # element.click()
    except:
        driver.exit()
    file_not_named = True
    while True:
        totalEntries = driver.find_element(By.CLASS_NAME, "pagebanner")
        notify = totalEntries.get_attribute("outerHTML")
        start_index = notify.find(">") + 1
        end_index = notify.find("</span>")
        desired_text = notify[start_index:end_index]
        with open(notification_path, 'w') as file:
            file.write(desired_text)
        try:
            elements = driver.find_elements(By.XPATH, "//td[@scope='request']")
            for i in range(len(elements)):
                try:
                    elements = driver.find_elements(By.XPATH, "//td[@scope='request']")
                    button = elements[i].find_element(By.NAME, 'radioButton1')
                    date_td = elements[i].find_elements(By.XPATH, "./following-sibling::td")
                    date = date_td[-1].text.strip()
                    button.click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//input[@value="Submit"]').click()
                    c += 1

                    driver.implicitly_wait(0)
                    wait = WebDriverWait(driver, 900)
                    try:
                        wait.until(EC.presence_of_element_located(By.XPATH, "//td[contains(text(), 'e Registration Number')]"))
                    except:
                        pass

                    if file_not_named == True:
                        try:
                            dist_td = driver.find_elements(By.XPATH, "//td[contains(text(), 'District')]")
                            dist = dist_td[-1].find_element(By.XPATH, "./following-sibling::td").text.strip()

                            tehsil_td = driver.find_element(By.XPATH, "//td[contains(text(), 'Tehsil')]")
                            tehsil = tehsil_td.find_element(By.XPATH, "./following-sibling::td").text.strip()

                            area_td = driver.find_element(By.XPATH, "//td[contains(text(), 'Type Of Area')]")
                            area = area_td.find_element(By.XPATH, "./following-sibling::td").text.strip()

                            sub_area_td = driver.find_element(By.XPATH, "//td[contains(text(), 'Sub Area Type')]")
                            sub_area = sub_area_td.find_element(By.XPATH, "./following-sibling::td").text.strip()

                            halka_td = driver.find_element(By.XPATH, "//td[contains(text(), 'Ward/Patwari Halka')]")
                            halka = halka_td.find_element(By.XPATH, "./following-sibling::td").text.strip()

                            halka_name_td = driver.find_element(By.XPATH, "//td[contains(text(), 'Ward/patwari Halka Name')]")
                            halka_name = halka_name_td.find_element(By.XPATH, "./following-sibling::td").text.strip()
                            
                            file_name = dist+", "+tehsil+", "+area+", "+sub_area+", "+halka+", "+halka_name
                            file_not_named = False
                            print(file_name)
                        except:
                            pass
                    try:
                        df.loc[c-1] = collection(c, date)
                    except:
                        print("Data Collection Faild")
                    driver.back()
                    wait = WebDriverWait(driver, 900)
                    wait.until(EC.presence_of_element_located((By.XPATH, '//th[contains(text(), "Date Of Registration")]')))
                except:
                    print("Stale element reference. Retrying...")
                    continue
            try:
                driver.find_element(By.LINK_TEXT, 'Next').click()
                time.sleep(5)
            except:
                break
        except:
            break
    print(c)
    
    characters_to_replace = r'\/:*?"<>|'
    for char in characters_to_replace:
        file_name = file_name.replace(char, ' ')

    sdate = df.loc[0, "Date of Reg."]
    edate= df.loc[0, "Date of Reg."]
    for i in reversed(range(len(df.index))):
        if df.loc[i, "Registration No."] != "None":
            edate = df.loc[i, "Date of Reg."]
            break

    date = "("+str(sdate)+"-"+str(edate)+")"
    date = date.replace("-", " ")
    date = date.replace("/", "-")

    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H-%M-%S")
    name = file_name+" "+date+'on'+current_date_time+".xlsx"
    file_path = os.path.join(settings.MEDIA_ROOT, name)
    df.to_excel(file_path, index=False)
    with open(file_path, 'rb') as excel_file:
        file_content = excel_file.read()
    
    response = FileResponse(file_content, as_attachment=True)
    response = HttpResponse(file_content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{file_name}.xlsx"'
    
    notify = "Search complete."
    with open(notification_path, 'w') as file:
        file.write(notify)
    return response

        

        
def save_captcha(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            captcha = form.cleaned_data['captcha']
            captcha_filename = f'captcha_{username}_value.txt'
            file_path = os.path.join(settings.MEDIA_ROOT, captcha_filename)

            with open(file_path, 'w') as file:
                file.write(captcha)

            response_data = {'message': 'Captcha saved successfully. Close this page and go back to previous page.'}
            return JsonResponse(response_data)
    else:
        form = CaptchaForm()

    response_data = {'message': 'Error saving captcha.'}
    return JsonResponse(response_data, status=400)

def save_captcha2(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            captcha = form.cleaned_data['captcha']
            captcha_filename2= f'captcha_{username}_value2.txt'
            file_path = os.path.join(settings.MEDIA_ROOT, captcha_filename2)

            with open(file_path, 'w') as file:
                file.write(captcha)

            response_data = {'message': 'Captcha saved successfully. Close this page and go back to previous page.'}
            return JsonResponse(response_data)
    else:
        form = CaptchaForm()
    response_data = {'message': 'Error saving captcha.'}
    return JsonResponse(response_data, status=400)

def get_districts(request):
    districts = District.objects.all()
    data = serialize("json", districts, fields=('id', 'name'))
    return HttpResponse(data, content_type="application/json")

def save_district(request, username, selectedDistrictId):
    username = username
    selectedDistrictId = selectedDistrictId
    district_filename = f'district_{username}_value2.txt'
    district_file_path = os.path.join(settings.MEDIA_ROOT, district_filename)
    district = District.objects.get(pk=selectedDistrictId)
    district_name = district.name
    with open(district_file_path, 'w') as file:
        file.write(district_name)
    return JsonResponse({'status': 'success'})

def get_tehsils(request, district_id):
    tehsils = Tehsil.objects.filter(state_id=district_id)
    data = serialize("json", tehsils, fields=('id', 'name'))
    return HttpResponse(data, content_type="application/json")

def save_tehsil(request, username, selectedTehsilId):
    username = username
    selectedTehsilId = selectedTehsilId
    tehsil_filename = f'tehsil_{username}_value2.txt'
    tehsil_file_path = os.path.join(settings.MEDIA_ROOT, tehsil_filename)
    tehsil = Tehsil.objects.get(pk=selectedTehsilId)
    tehsil_name = tehsil.name
    with open(tehsil_file_path, 'w') as file:
        file.write(tehsil_name)
    return JsonResponse({'status': 'success'})

def get_type_of_areas(request, tehsil_id):
    type_of_areas = TypeOfArea.objects.filter(tehsil=tehsil_id)
    data = serialize("json", type_of_areas, fields=('id', 'name'))
    return HttpResponse(data, content_type="application/json")

def save_type_of_area(request, username, selectedType_of_area_name):
    username = username
    type_of_area_name = selectedType_of_area_name
    print(type_of_area_name)
    type_of_area_filename = f'type_of_area_{username}_value2.txt'
    type_of_area_file_path = os.path.join(settings.MEDIA_ROOT, type_of_area_filename)
    with open(type_of_area_file_path, 'w') as file:
        file.write(type_of_area_name)
    return JsonResponse({'status': 'success'})

def get_sub_area_types(request, type_of_area_id, type_of_area_name):
    sub_area_types = SubArea.objects.filter(typeofarea=type_of_area_id)
    data = serialize("json", sub_area_types, fields=('id', 'name'))
    return HttpResponse(data, content_type="application/json")

def save_sub_area_type(request, username, selectedSub_area_typeId):
    username = username
    selectedSub_area_typeId  = selectedSub_area_typeId
    sub_area_type_filename = f'sub_area_type_{username}_value2.txt'
    sub_area_type_file_path = os.path.join(settings.MEDIA_ROOT, sub_area_type_filename)
    Sub_area_typeId = SubArea.objects.get(pk=selectedSub_area_typeId)
    Sub_area_typeId_name = Sub_area_typeId.name
    with open(sub_area_type_file_path, 'w') as file:
        file.write(Sub_area_typeId_name)
    return JsonResponse({'status': 'success'})

def get_ward_number_patwari_numbers(request, sub_area_type_id):
    ward_number_patwari_numbers = WardPatwariNumber.objects.filter(subarea=sub_area_type_id)
    data = serialize("json", ward_number_patwari_numbers, fields=('id', 'name'))
    return HttpResponse(data, content_type="application/json")

def save_ward_number_patwari_number(request, username, selectedWard_number_patwari_numberId):
    username = username
    selectedWard_number_patwari_numberId  = selectedWard_number_patwari_numberId
    ward_number_patwari_number_filename = f'ward_number_patwari_number_{username}_value2.txt'
    ward_number_patwari_number_file_path = os.path.join(settings.MEDIA_ROOT, ward_number_patwari_number_filename)
    Ward_number_patwari_numberId = WardPatwariNumber.objects.get(pk=selectedWard_number_patwari_numberId)
    Ward_number_patwari_numberId_name = Ward_number_patwari_numberId.name
    with open(ward_number_patwari_number_file_path, 'w') as file:
        file.write(Ward_number_patwari_numberId_name)
    return JsonResponse({'status': 'success'})

def get_mohalla_colony_name_society_roads(request, ward_number_patwari_number_id):
    mohalla_colony_name_society_roads = SocietyName.objects.filter(ward=ward_number_patwari_number_id)
    data = serialize("json", mohalla_colony_name_society_roads, fields=('id', 'name'))
    return HttpResponse(data, content_type="application/json")

def save_mohalla_colony_name_society_road(request, username, selectedMohalla_colony_name_society_roadId):
    username = username
    selectedMohalla_colony_name_society_roadId  = selectedMohalla_colony_name_society_roadId
    mohalla_colony_name_society_road_filename = f'mohalla_colony_name_society_road_{username}_value2.txt'
    mohalla_colony_name_society_road_file_path = os.path.join(settings.MEDIA_ROOT, mohalla_colony_name_society_road_filename)
    Mohalla_colony_name_society_roadId = SocietyName.objects.get(pk=selectedMohalla_colony_name_society_roadId)
    Mohalla_colony_name_society_roadId_name = Mohalla_colony_name_society_roadId.name
    with open(mohalla_colony_name_society_road_file_path, 'w') as file:
        file.write(Mohalla_colony_name_society_roadId_name)
    return JsonResponse({'status': 'success'})

def changedDropdownfun(request, username, changedDropdown):
    username = username
    changedDropdown  = changedDropdown
    changedDropdown_filename = f'changedDropdown_{username}.txt'
    changedDropdown_file_path = os.path.join(settings.MEDIA_ROOT, changedDropdown_filename)
    with open(changedDropdown_file_path, 'w') as file:
        file.write(changedDropdown)
    return JsonResponse({'status': 'success'})

def notification(request, username):
    notification_file = f'notification_{username}.txt'
    notification_path = os.path.join(settings.MEDIA_ROOT, notification_file)
    try:
        with open(notification_path, 'r') as file:
            notify = file.read()
    except:
        notify = "Starting"
    data = json.dumps({'message': notify})
    return HttpResponse(data, content_type="application/json")
