	district_filename = f'district_{username}_value2.txt'
    district_file_path = os.path.join(settings.MEDIA_ROOT, district_filename)
    if os.path.exists(district_file_path):
        os.remove(district_file_path)
    
    district_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "dsearchdto.distId"))
    )
    select_district = Select(district_dropdown)
    district_options = [option.text for option in select_district.options if option.text != 'Select']
    print(district_options)
    for district_name in district_options:
        districts = District.objects.get_or_create(name=district_name)
    time.sleep(2)
    while not os.path.exists(district_file_path):
        # Check if the maximum wait time has been exceeded
        if time.time() - start_time > max_wait_time:
            print("File not found within the specified time.")
            break

        # Wait for a short duration before checking again
        time.sleep(1)
    
    with open(district_file_path, 'r') as file:
        district_instance = file.read()
    
    
    
    select.select_by_visible_text(district_instance)
    
    tehsil_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "dsearchdto.tehisilId"))
    )
    
    select_tehsil = Select(tehsil_dropdown)
    tehsil_options = [option.text for option in select_tehsil.options if option.text != 'Select']
    print(tehsil_options)
    for tehsil_name in tehsil_options:
        tehsils = Tehsil.objects.get_or_create(name=tehsil_name, state=district_instance)
    time.sleep(2)
    
    if(tehsil):
        tehsil_dropdown = driver.find_element(By.NAME, "dsearchdto.tehisilId")
        select = Select(tehsil_dropdown)
        select.select_by_visible_text(tehsil_instance)
        time.sleep(2)
    
        
    if(type_of_area):
        area_dropdown = driver.find_element(By.NAME, "dsearchdto.areaTypeId")
        select = Select(area_dropdown)
        select.select_by_visible_text(type_of_area)
        time.sleep(2)

    if(sub_area_type):
        subArea_dropdown = driver.find_element(By.NAME, "dsearchdto.subAreaTypeId")
        select = Select(subArea_dropdown)
        select.select_by_visible_text(sub_area_type)
        time.sleep(2)
    
    if(ward_number_patwari_number):
        ward_dropdown = driver.find_element(By.NAME, "dsearchdto.subAreaWardMappingId")
        select = Select(ward_dropdown)
        select.select_by_visible_text(ward_number_patwari_number)
        time.sleep(2)
    
    if(mohalla_colony_name_society_road):
        mohalla_dropdown = driver.find_element(By.NAME, "dsearchdto.mohallaId")
        select = Select(mohalla_dropdown)
        select.select_by_visible_text(mohalla_colony_name_society_road)
        time.sleep(2)
        
    if(khasra_number):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.khasraNumber")
        khasra_input.send_keys(khasra_number)
        time.sleep(2)
        
    if(transacting_party_first_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyFirstName")
        khasra_input.send_keys(transacting_party_first_name)
        time.sleep(2)
        
    if(transacting_party_middle_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyMiddName")
        khasra_input.send_keys(transacting_party_middle_name)
        time.sleep(2)
        
    if(transacting_party_last_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyLastName")
        khasra_input.send_keys(transacting_party_last_name)
        time.sleep(2)
    
    if(transacting_party_mother_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyMotName")
        khasra_input.send_keys(transacting_party_mother_name)
        time.sleep(2)
        
    if(transacting_party_father_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.transPartyFatName")
        khasra_input.send_keys(transacting_party_father_name)
        time.sleep(2)
        
    if(organization_name):
        khasra_input = driver.find_element(By.NAME, "dsearchdto.orgName")
        khasra_input.send_keys(organization_name)
        time.sleep(2)