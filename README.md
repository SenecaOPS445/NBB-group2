# Fall 2024 Assignment 2

Original file line number	Diff line number	Diff line change

# Fall 2024 Assignment 2
**1. Description of the Project**

**Password Generator:** 
  The Password Generator is a Python-based application designed to create secure and customizable passwords or passphrases.  

  By accepting user input or random elements, it produces passwords that are both strong and memorable. This script ensures enhanced security by offering configuration options for complexity, length, and passphrase structure. 

  This tool is ideal for users seeking secure yet easy-to-remember credentials. 



**2. Installation Instructions** 

**Dependencies:**

  Python 3.7 or later 
  Required Python Libraries(utilizes Python buil-in library): random, string 



**Steps to Install and Run:**

  1. Clone the repository: 

    git clone https://github.com/SenecaOPS445/NBB-group2/password-generator.git

  2. Navigate to the project directory: 

    cd password-generator 

  3. Install any additional dependencies (if specified in requirements.txt): 

    pip install -r requirements.txt 

  4. Run the program: 

    python password_generator.py 



**3. Usage Instructions**

Suggested Modes of Operation: 



These modes are suggested config file configurations, **it is critical to configure the config file to your desired parameter before utilizing the Password Generator** to you or your organization's desired parameters. 

**User Input Mode:** Users provide keywords to influence the generated passphrase. For this to be activated, within the config file:
no_input = False

**Random Mode:** Generates a completely random passphrase or password based on a predefined word list. For this to be activated, within the config file:
no_input = True

**4. Steps to Use:**

1. Configure settings in config.txt as needed (e.g., minimum length, special character inclusion). 

2. Execute the program. 

3. Follow the prompts: 

  a. Enter desired password length. 

  b. Specify the inclusion of special characters or casing options. 

  c. Optionally, input keywords for passphrase generation. 

  d. Receive the generated password or passphrase displayed securely in the terminal. 

**5. Example Outputs**

  Password: 

  Your new password is: Th345StrongDogEatsTe@ 

  Passphrase: 

  Your new passphrase is: BraveElephant!Enjoys5Hiking 



**6.Code Structure**

**Core Functions:**

**load_config(filename="config.txt")**

Reads and loads the configuration file, applying default values if no custom settings are 		provided. 

**main()**

Main program flow, managing user input, random generation mode, and invoking other functions. 

**get_user_keywords()**

Prompts the user to input keywords or defaults to random word selection based on settings. 

**generate_passphrase(keywords)**

Generates a passphrase using provided keywords or random words from a predefined list. 

**add_special_characters(passphrase)**

Adds special characters to the passphrase for increased complexity. 

**randomize_cases(passphrase)**

Randomly adjusts the casing of words within the passphrase. 

**validate_passphrase(passphrase)**

Validates the generated passphrase against security criteria, such as length and character variety. 

**display_passphrase(passphrase)**

Formats and securely displays the passphrase to the user. 


**Features Overview**

**Passphrase Generation:** Combines user input or random words to create secure, memorable passphrases. 

**Customizable Validation:** Validates passphrase security (length, complexity) per user-defined configurations. 

**Configurable Settings:** Adjust password generation behavior via config.txt, including: 

  Minimum passphrase length. 

  Number of random words added. 

  Inclusion of special characters. 

  Casing variation. 

**Error Handling:** Ensures proper execution even with invalid or incomplete user input. 

**Example Configuration File (config.txt):**

  no_input = True 
  use_random_word = True 
  min_passphrase_length = 12 
  passphrase_word_count = 3 
  add_special_characters = True 
  randomize_cases = True 
  validate_passphrase = True 

This configuration file example generates passphrases with at least 12 characters, adds 3 random words, includes special characters, and randomizes the casing.
