function showStep(stepId) {
    // Hide all steps
    document.getElementById("step1").style.display = "none";
    document.getElementById("step2").style.display = "none";
    document.getElementById("step3").style.display = "none";

    // Show the selected step
    document.getElementById(stepId).style.display = "block";
    localStorage.setItem("currentStep", stepId);
  }
  const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)[1];
  function addDelay() {
    const showCaptchaButton = document.getElementById("showCaptchaButton");

    // Disable the "Show Captcha" button initially
    showCaptchaButton.disabled = true;

    // After a delay of 6 seconds (4000 milliseconds), enable the button
    setTimeout(function () {
      showCaptchaButton.disabled = false;
      showCaptchaButton.click();
    }, 13000);
  }
  document
    .getElementById("loginButton")
    .addEventListener("click", addDelay);
  function addDelay2() {
    const buttonStep3 = document.getElementById("buttonStep3");

    // Disable the "Show Captcha" button initially
    buttonStep3.disabled = true;

    // After a delay of 6 seconds (4000 milliseconds), enable the button
    setTimeout(function () {
      buttonStep3.disabled = false;
      buttonStep3.click();
    }, 40000);
  }

  // Add an event listener to the "Login" button to call the addDelay function
  document
    .getElementById("submitStep2")
    .addEventListener("click", addDelay2);

  document
    .getElementById("showCaptchaButton")
    .addEventListener("click", function () {
      // Get the username entered by the user
      var username = document.getElementById("usernameInput").value;

      // Check if a username is entered
      if (username.trim() === "") {
        alert("Please enter a username.");
        return;
      }

      // Construct the URL for the captcha image based on the entered username
      var captchaImage = document.getElementById("captchaImage");
      captchaImage.src = `/media/captcha_${username}.png`;
      captchaImage.style.display = "block";
    });

  document
    .getElementById("showCaptchaButton2")
    .addEventListener("click", function () {
      // Get the username entered by the user
      var username2 = document.getElementById("usernameInput2").value;

      // Check if a username is entered
      if (username2.trim() === "") {
        alert("Please enter a username.");
        return;
      }

      // Construct the URL for the captcha image based on the entered username
      var captchaImage2 = document.getElementById("captchaImage2");
      captchaImage2.src = `/media/captcha_${username2}_form.png`;
      captchaImage2.style.display = "block";
    });

  // Get the input element for the username in Step 1
  const usernameStep2 = document.getElementById("username_input");

  // Get the input element for the username in Step 2
  const usernameStep2a = document.getElementById("usernameInput");
  const usernameStep2b = document.getElementById("usernameInputb");
  const usernameStep2c = document.getElementById("usernameInput2");
  const usernameStep2d = document.getElementById("usernameInput2b");

  // Listen for input changes in the username field in Step 2
  usernameStep2.addEventListener("input", function () {
    usernameStep2a.value = username_input.value;
    usernameStep2b.value = username_input.value;
    usernameStep2c.value = username_input.value;
    usernameStep2d.value = username_input.value;
  });
  usernameStep2a.addEventListener("input", function () {
    usernameStep2b.value = usernameInput.value;
    usernameStep2c.value = usernameInput.value;
    usernameStep2d.value = usernameInput.value;
  });
  usernameStep2b.addEventListener("input", function () {
    usernameStep2c.value = usernameInput2.value;
    usernameStep2d.value = usernameInput2.value;
  });
  const storedStep = localStorage.getItem("currentStep");
  if (storedStep) {
    showStep(storedStep);
  }
  
  function onSubmitHandler() {
    const username2b = document.getElementById("usernameInput2b").value;
    localStorage.setItem("usernameValue", username2b);
  
    // Reload the page after 10 seconds
    setTimeout(function () {
      window.location.reload();
  
      // Call fetchAndNotify after the reload
      setTimeout(function () {
        // Click on the "Show Captcha" button after the page reloads
        const showCaptchaButton2 = document.getElementById("showCaptchaButtonId"); // Replace with the actual ID of the button
        if (showCaptchaButton2) {
          showCaptchaButton2.click(); // Simulate a click on the button
        }
      }, 2000);
    }, 10000);
  
    // Return true to allow form submission
    return true;
  }
  

  // Check if there's a stored username value in localStorage
  const storedUsername = localStorage.getItem("usernameValue");

  // If a stored username exists, set it in the username input field
  if (storedUsername) {
    document.getElementById("usernameInput").value = storedUsername;
    document.getElementById("usernameInput2").value = storedUsername;
    document.getElementById("usernameInput2b").value = storedUsername;
  }

  const login_button = document.getElementById("submitStep2");

  login_button.addEventListener("click", function () {
    const url = `/get_districts/`;

    districtDropdown.innerHTML =
      '<option value="default">Select District</option>';

    setTimeout(function () {
      fetch(url)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log(data);

          if (!data || data.length === 0) {
            console.error("No districts found.");
            return;
          }

          // Populate district dropdown with fetched districts
          data.forEach((district) => {
            const option = document.createElement("option");
            option.value = district.pk;
            option.text = district.fields.name;
            districtDropdown.appendChild(option);
          });
        })
        .catch((error) => console.error("Error:", error));
    }, 25000);
  });

  const districtDropdown = document.getElementById("districtDrop");
  districtDropdown.addEventListener("change", function () {

    tehsilDropdown.innerHTML = '<option value="default">Select tehsil</option>';
    tehsilDropdown.disabled = false;
    type_of_areaDropdown.innerHTML = '<option value="default">Select type_of_area</option>';
    sub_area_typeDropdown.innerHTML = '<option value="default">Select Sub_area_type</option>';
    ward_number_patwari_numberDropdown.innerHTML = '<option value="default">Select Ward_number_patwari_number</option>';
    mohalla_colony_name_society_roadDropdown.innerHTML = '<option value="default">Select Mohalla_colony_name_society_road</option>';

    var username = document.getElementById("usernameInput").value;
    const selectedDistrictId = this.value;
    const district = 'district'
    const changed = `/changedDropdown/${username}/${district}/`;
    fetch(changed);
    const url = `/save_district/${username}/${selectedDistrictId}/`;
    fetch(url);
    districtDropdown.disabled = true;
    setTimeout(function () {
      const url2 = `/get_tehsils/${selectedDistrictId}/`;
      tehsilDropdown.innerHTML =
        '<option value="default">Select Tehsil</option>';
      fetch(url2)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log(data);

          if (!data || data.length === 0) {
            
            const defaultOption = document.createElement("option");
            defaultOption.value = "default";
            defaultOption.text = "No data found";
            tehsilDropdown.appendChild(defaultOption);
        } else {

          // Populate tehsil dropdown with fetched tehsils
          data.forEach((tehsil) => {
            const option = document.createElement("option");
            option.value = tehsil.pk;
            option.text = tehsil.fields.name;
            tehsilDropdown.appendChild(option);
            tehsilDropdown.style.display = 'block';
            districtDropdown.disabled = false;
          });
        }
        })
        .catch((error) => console.error("Error:", error));
    }, 5000);
  });

  const tehsilDropdown = document.getElementById("tehsilDrop");
  tehsilDropdown.addEventListener("change", function () {
    type_of_areaDropdown.innerHTML = '<option value="default">Select type_of_area</option>';
    type_of_areaDropdown.disabled = false;
    sub_area_typeDropdown.innerHTML = '<option value="default">Select Sub_area_type</option>';
    ward_number_patwari_numberDropdown.innerHTML = '<option value="default">Select Ward_number_patwari_number</option>';
    mohalla_colony_name_society_roadDropdown.innerHTML = '<option value="default">Select Mohalla_colony_name_society_road</option>';
    var username = document.getElementById("usernameInput").value;
    const selectedTehsilId = this.value;
    const tehsil = 'tehsil'
    const changed = `/changedDropdown/${username}/${tehsil}/`;
    fetch(changed);
    const url = `/save_tehsil/${username}/${selectedTehsilId}/`;
    fetch(url);
    tehsilDropdown.disabled = true;
    setTimeout(function () {
      const url2 = `/get_type_of_areas/${selectedTehsilId}/`;
      type_of_areaDropdown.innerHTML =
        '<option value="default">Select Type_of_area</option>';
      fetch(url2)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log(data);

          if (!data || data.length === 0) {
            
            const defaultOption = document.createElement("option");
            defaultOption.value = "default";
            defaultOption.text = "No data found";
            type_of_areaDropdown.appendChild(defaultOption);
        } else {

          // Populate type_of_area dropdown with fetched type_of_areas
          data.forEach((type_of_area) => {
            const option = document.createElement("option");
            option.value = type_of_area.pk;
            option.text = type_of_area.fields.name;
            type_of_areaDropdown.appendChild(option);
            type_of_areaDropdown.style.display = 'block';
            tehsilDropdown.disabled = false;
          });
        }
        })
        .catch((error) => console.error("Error:", error));
    }, 5000);
  });

  const type_of_areaDropdown = document.getElementById("type_of_areaDrop");
  type_of_areaDropdown.addEventListener("change", function () {
    sub_area_typeDropdown.innerHTML = '<option value="default">Select Sub_area_type</option>';
    sub_area_typeDropdown.disabled = false;
    ward_number_patwari_numberDropdown.innerHTML = '<option value="default">Select Ward_number_patwari_number</option>';
    mohalla_colony_name_society_roadDropdown.innerHTML = '<option value="default">Select Mohalla_colony_name_society_road</option>';
    var username = document.getElementById("usernameInput").value;
    const selectedType_of_areaName =
      type_of_areaDropdown.options[type_of_areaDropdown.selectedIndex].text;
    const selectedType_of_areaId = this.value;
    const area = 'area'
    const changed = `/changedDropdown/${username}/${area}/`;
    fetch(changed);
    const url = `/save_type_of_area/${username}/${selectedType_of_areaName}/`;
    fetch(url);
    type_of_areaDropdown.disabled = true;
    setTimeout(function () {
      const url2 = `/get_sub_area_types/${selectedType_of_areaId}/${selectedType_of_areaName}/`;
      sub_area_typeDropdown.innerHTML ='<option value="default">Select Sub_area_type</option>';
      fetch(url2)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log(data);

          if (!data || data.length === 0) {
            
            const defaultOption = document.createElement("option");
            defaultOption.value = "default";
            defaultOption.text = "No data found";
            sub_area_typeDropdown.appendChild(defaultOption);
            sub_area_typeDropdown.style.display = 'block';
        } else {

          // Populate sub_area_type dropdown with fetched sub_area_types
          data.forEach((sub_area_type) => {
            const option = document.createElement("option");
            option.value = sub_area_type.pk;
            option.text = sub_area_type.fields.name;
            sub_area_typeDropdown.appendChild(option);
            sub_area_typeDropdown.style.display = 'block';
            type_of_areaDropdown.disabled = false;
          });
        }
        })
        .catch((error) => console.error("Error:", error));
    }, 5000);
  });

  const sub_area_typeDropdown = document.getElementById("sub_area_typeDrop");
  sub_area_typeDropdown.addEventListener("change", function () {
    ward_number_patwari_numberDropdown.innerHTML = '<option value="default">Select Ward_number_patwari_number</option>';
    ward_number_patwari_numberDropdown.disabled = false;
    mohalla_colony_name_society_roadDropdown.innerHTML = '<option value="default">Select Mohalla_colony_name_society_road</option>';
    var username = document.getElementById("usernameInput").value;
    const selectedSub_area_typeId = this.value;
    const sub = 'sub'
    const changed = `/changedDropdown/${username}/${sub}/`;
    fetch(changed);
    const url = `/save_sub_area_type/${username}/${selectedSub_area_typeId}/`;
    fetch(url);
    sub_area_typeDropdown.disabled = true;

    setTimeout(function () {
      const url2 = `/get_ward_number_patwari_numbers/${selectedSub_area_typeId}/`;
      ward_number_patwari_numberDropdown.innerHTML = '<option value="default">Select Ward_number_patwari_number</option>';
      fetch(url2)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log(data);

          if (!data || data.length === 0) {
            
            const defaultOption = document.createElement("option");
            defaultOption.value = "default";
            defaultOption.text = "No data found";
            ward_number_patwari_numberDropdown.appendChild(defaultOption);
            ward_number_patwari_numberDropdown.style.display = 'block';
        } else {
          data.forEach((ward_number_patwari_number) => {
            const option = document.createElement("option");
            option.value = ward_number_patwari_number.pk;
            option.text = ward_number_patwari_number.fields.name;
            ward_number_patwari_numberDropdown.appendChild(option);
            ward_number_patwari_numberDropdown.style.display = 'block';
            sub_area_typeDropdown.disabled = false;
            
          });
        }
        })
        .catch((error) => console.error("Error:", error));
    }, 5000);
  });

  const ward_number_patwari_numberDropdown = document.getElementById("ward_number_patwari_numberDrop");
  ward_number_patwari_numberDropdown.addEventListener("change", function () {
    mohalla_colony_name_society_roadDropdown.innerHTML = '<option value="default">Select Mohalla_colony_name_society_road</option>';
    mohalla_colony_name_society_roadDropdown.disabled = false;
    var username = document.getElementById("usernameInput").value;
    const selectedWard_number_patwari_numberId = this.value;
    const ward = 'ward'
    const changed = `/changedDropdown/${username}/${ward}/`;
    fetch(changed);
    const url = `/save_ward_number_patwari_number/${username}/${selectedWard_number_patwari_numberId}/`;
    fetch(url)
    ward_number_patwari_numberDropdown.disabled = true;

    setTimeout(function () {
      const url2 = `/get_mohalla_colony_name_society_roads/${selectedWard_number_patwari_numberId}/`;
      mohalla_colony_name_society_roadDropdown.innerHTML = '<option value="default">Select Mohalla_colony_name_society_road</option>';
      fetch(url2)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log(data);

          if (!data || data.length === 0) {
            
            const defaultOption = document.createElement("option");
            defaultOption.value = "default";
            defaultOption.text = "No data found";
            mohalla_colony_name_society_roadDropdown.appendChild(defaultOption);
            mohalla_colony_name_society_roadDropdown.style.display = 'block';
        } else {
            // Populate mohalla_colony_name_society_road dropdown with fetched data
            data.forEach((mohalla_colony_name_society_road) => {
                const option = document.createElement("option");
                option.value = mohalla_colony_name_society_road.pk;
                option.text = mohalla_colony_name_society_road.fields.name;
                mohalla_colony_name_society_roadDropdown.appendChild(option);
                mohalla_colony_name_society_roadDropdown.style.display = 'block';
                ward_number_patwari_numberDropdown.disabled = false;

            });
        }
        })
        .catch((error) => console.error("Error:", error));
    }, 5000);
  });
  const mohalla_colony_name_society_roadDropdown = document.getElementById("mohalla_colony_name_society_roadDrop");
  mohalla_colony_name_society_roadDropdown.addEventListener("change", function () {
    var username = document.getElementById("usernameInput").value;
    const selectedMohalla_colony_name_society_roadId = this.value;
    const mohalla = 'mohalla'
    const changed = `/changedDropdown/${username}/${mohalla}/`;
    fetch(changed);
    const url = `/save_mohalla_colony_name_society_road/${username}/${selectedMohalla_colony_name_society_roadId}/`;
    fetch(url)
    mohalla_colony_name_society_roadDropdown.disabled = true;
    setTimeout(function () {
      mohalla_colony_name_society_roadDropdown.disabled = false;
    }, 5000); // Set the timeout for 5 seconds (adjust the time as needed)
  });
  const done = document.getElementById("done");
  done1 = 'done'
  done.addEventListener("click", function () {
    var username = document.getElementById("usernameInput").value;
    const changed = `/changedDropdown/${username}/${done1}/`;
    fetch(changed);
    setTimeout(function () {
      document.getElementById("showCaptchaButton2").click();
    }, 1000);
  });

  // Function to fetch the link and show notifications
  function fetchAndNotify() {
    var username = document.getElementById("usernameInput").value;
    const notifi = `/notification/${username}/`;
    fetch(notifi)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json(); // Parse the JSON response
        })
        .then(data => {
            // Display notifications as popups
            const popupContainer = document.getElementById('popupContainer');
            const popupContent = document.getElementById('popupContent');
            const message = data.message; // Assuming 'message' is a key in the fetched data
            
            // Store the initial message content
            const initialMessage = `<div>${message}</div>`;

            const matches = message.match(/(\d+) items found, displaying (\d+) to (\d+)/);

            if (matches && matches.length === 4) {
                const totalCount = parseInt(matches[1]);
                const displayingCountStart = parseInt(matches[2]);
                const displayingCountEnd = parseInt(matches[3]);
                const displayingCount = displayingCountStart + 1;

                // Calculate progress percentage
                const progressPercentage = (displayingCount / totalCount) * 100;
                const percentageText = `${progressPercentage.toFixed(2)}%`; // Round to two decimal places

                const progressBar = `
                  <div class="progress" style="width: 100px; border: 1px solid #ccc;">
                    <div class="progress-bar" role="progressbar" style="width: ${progressPercentage.toFixed(2)}%; background-color: green; height: 20px;" aria-valuenow="${progressPercentage.toFixed(2)}" aria-valuemin="0" aria-valuemax="100">
                      ${percentageText} <!-- Display the percentage next to the progress bar -->
                    </div>
                  </div>
                `;
                
            // Combine the initial message with the progress bar
            const contentWithProgressBar = initialMessage + progressBar;
            popupContent.innerHTML = contentWithProgressBar;
        } else {
            popupContent.innerHTML = initialMessage; // Show the message without the progress bar
        }

        popupContainer.style.display = 'block'; // Show the popup container

        // Automatically hide the popup after 5 seconds (adjust as needed)
        setTimeout(function () {
            popupContainer.style.display = 'none';
        }, 5000);
    })
    .catch(error => {
        console.error('There was a problem fetching the notification:', error);
    });
}


const notificationInit = document.getElementById("loginButton");
notificationInit.addEventListener("click", function () {
  fetchAndNotify(); 
  setInterval(fetchAndNotify, 8000);
});
const restartButton = document.getElementById("restart");

restartButton.addEventListener("click", function() {
fetchAndNotify();
setInterval(fetchAndNotify, 8000); 
});
