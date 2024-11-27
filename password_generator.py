#!/usr/bin/env Python3

# This can be our default configuration settings that is already in dictionary format  
# Note: We may need to have a maximum passphrase, or change the default settings  

import os
import re
import random

DEFAULT_CONFIG = {  

    "no_input": False,  
    "use_random_word": True,  
    "min_passphrase_length": 12,  
    "passphrase_word_count": 2,  
    "add_special_characters": True,  
    "randomize_cases": True,  
    "validate_passphrase": True  
}  

'''  
The idea behind the config.txt file is to convert the text file into a dictionary.  
This was also what was recommended by the instructor in our meeting, instead of accepting user input to set these.   
The keys of the dictionary will be used by the main() function to activate, deactivate, and set values for our functions.  
The function write_default_config() will be used to create a default config file, but only if the config file is not found. 
''' 

def write_default_config(filename="CONFIG.TXT"):  

    ''' 
    Member - Zachary
    This function only writes the default config if the file doesn't exist.  
    This uses os module to check path for filename, which is defaulted as CONFIG.TXT  
    ''' 

    if not os.path.exists(filename):  
        with open(filename, "w") as file:  
            for key, value in DEFAULT_CONFIG.items():  
                file.write(f"{key} = {value}\n")  
            print(f"Default configuration written to {filename}")  

 
def load_config(filename="CONFIG.TXT"):  

    ''' 
    Member - Zachary
    This function first loads the defaults,  
    then it attempts to open the file,  
    then loads the default dictionary into memory,  
    then opens config.txt as "file," and for every line in "file,"  
    then it strips the left half into the key and the right half into the value,  
    ignores blankspace or comments,  
    then ensures all values are the appropriate data type,  
    and finally we have error print statements as the true error handling is that  
    even if incorrect values are provided, it will just keep the default config.  
    ''' 

    config = DEFAULT_CONFIG.copy()  # Copies our default dictionary defaults, mainly to ensure config[keys] are correct  
    try:  
        with open(filename, "r") as file:  
            for line in file:  
                # If not avoids stripping a blank line, or a comment starting with # 
                if not line.strip() or line.strip().startswith("#"):  
                    continue 
                #This strips line, and splits with = sign 
                key, value = line.strip().split("=")  
                key = key.strip() 
                #This will lower case to avoid any capitalization errors like TRUE 
                value = value.strip().lower()  

                # This will convert values into the appropriate type; Only accepts Boolean values of True and/or False or Int values  
                if value == "true":  
                    config[key] = True  
                elif value == "false":  
                    config[key] = False  
                elif value.isdigit():  
                    config[key] = int(value) 
                else:  
                    print(f"Warning: Invalid value {value} for {key}. Will now use default: {config[key]}")  

 

    except FileNotFoundError:  
        print(f"Configuration file {filename} not found. Using default settings.")  

    # This compares keys in DEFAULT_CONFIG with config dictionary, and provides an error if the dictionary key is not in default config. 
    for key in DEFAULT_CONFIG.keys():  
        if key not in config:  
            print(f"Warning: Missing key '{key}' in config file. Using default: {DEFAULT_CONFIG[key]}")  
    return config 
 
def main(): 

    ''' 
    Member - Zachary
    The main function is used to load/create default config file as a dictionary,  
    generates password from functions based on config dictionary settings, and  
    then run the validate and based on configuration 
    ''' 

    # We call the write default config file function so that the configuration file exists before moving onto next step,  
    # This won't overwrite config file, only if the config file is not found.  

    write_default_config() 

    # This will load the configuration settings from the config file, 
    # This is a dictionary with either default values or user-defined values 

    config = load_config() 

    # This will check the mode from config file to decide if using random words or user input 

    if config["use_random_word"] == True: 

        # This part will generate passphrase when random word mode is set to True; 
        # The keywords are chosen by either user input or defaults to random ones depending on config file settings 

        keywords = get_user_keywords() 
        passphrase = generate_passphrase(keywords)  # Uses the default keywords list to create the passphrase 

        # This ensures the passphrase meets the minimum length if it's not already long enough 
        while len(passphrase) < config["min_passphrase_length"]: 
            # This will add extra random words to meet the defined length requirement based on config file 
            extra_keywords = get_user_keywords()  # These keywords are chosen or defaulted to random 
            passphrase = generate_passphrase(keywords + extra_keywords)  # This will update passphrase to include extra words 

    else: 
        # This will generate passwords with user-provided keywords 
        # Works without requiring random words but still based on config 
        keywords = get_user_keywords() 
        passphrase = generate_passphrase(keywords)  # This uses keywords directly for password 

    # This will add complexity if settings in config are  
    if config["add_special_characters"] == True: 
        # Adds special characters to the passphrase for extra complexity 
        passphrase = add_special_characters(passphrase) 

    if config["randomize_cases"] == True: 
        # Thi randomizes the casing of words in passphrase for added variety if set to True
        passphrase = randomize_cases(passphrase) 

 

    # This validates the passphrase against security requirements from config 
    if config["validate_passphrase"] == True: 
        # This runs validation test based on config file settings and exits if passphrase fails security checks 
        if not validate_passphrase(passphrase): 
            print("The generated passphrase does not meet security requirements. Please try again.") 
            return  # The program stops and allows the user to retry generation 

    # This displays the final passphrase or password securely to the user 
    display_passphrase(passphrase)  # This is the last step, showing the result



def get_user_keywords(): 
    """ 
    Member - Adetola
    Prompts the user to input keywords or defaults to random words. 
    """ 
    keywords = input("Enter keywords (comma-separated) for passphrase generation: ").strip()
    if keywords: 
        return [word.strip() for word in keywords.split(",")] 
    return [] 

 

def generate_passphrase(keywords, config): 
    """ 
    Member - Adetola
    Generates a passphrase using provided keywords or random words from a predefined list. 
    """ 
    
    word_count = config.get("passphrase_word_count", 3) 
    use_random_word = config.get("use_random_word", True) 
    
    if not keywords and use_random_word: 
        keywords = random.sample(PREDEFINED_WORDS, word_count) 
    
    if len(keywords) < word_count: 
        additional_words = random.sample(PREDEFINED_WORDS, word_count - len(keywords)) 
        keywords.extend(additional_words) 
    
    return " ".join(keywords) 


def add_special_characters(passphrase): 

    """ 
    Member - Yeshi
    Inserts a single special character at a randomly chosen position within the provided passphrase. 
    """ 

    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" 
    special_char = random.choice(special_characters)  # Pick one random special character 
    position = random.randint(0, len(passphrase))  # Random position in the passphrase 

    return passphrase[:position] + special_char + passphrase[position:]  # Insert the character 


def display_passphrase(passphrase): 

    """ 
    Member - Yeshi
    Shows the generated passphrase in a clear and user-friendly way, making sure it is displayed securely. 
    """ 

    print("\n" + "=" * 30) 
    print("Generated Passphrase:") 
    print(passphrase) 
    print("=" * 30 + "\n") 

import random 

  

def randomize_cases(passphrase): 
    '''
    Member - Zhandong
    Randomizes the case of each character in the given passphrase, returning a new passphrase with randomized character cases. 
    '''
    return ''.join( 
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in passphrase 
    ) 

def validate_passphrase(passphrase, config): 
    '''
    Member - Zhandong
    Validates the given passphrase against security criteria based on the provided configuration, returning a boolean indicating validity and a list of validation errors if invalid. 
    '''
    errors = [] 
    min_length = config.get("min_passphrase_length", 12) 
    add_special_characters = config.get("add_special_characters", True) 

    # Check minimum length 
    if len(passphrase) < min_length: 
        errors.append(f"Passphrase must be at least {min_length} characters long.") 

    # Check for special characters if required 
    if add_special_characters and not re.search(r"[!@#$%^&*]", passphrase): 
        errors.append("Passphrase must include at least one special character (!@#$%^&*).") 

    # Check for mixed case 
    if not (any(c.islower() for c in passphrase) and any(c.isupper() for c in passphrase)): 
        errors.append("Passphrase must include both uppercase and lowercase letters.") 

    # Check for digits 
    if not any(c.isdigit() for c in passphrase): 
        errors.append("Passphrase must include at least one digit.") 

    # Return validation result 
    return len(errors) == 0, errors

def validate_passphrase(passphrase, config): 

    """ 
    Member - Biswas
    Validates the generated passphrase against security criteria, such as length and character variety 
    """ 

    errors = [] 

    # Retrieve config 
    min_length = config.get("min_passphrase_length", 12) 
    add_special_characters = config.get("add_special_characters", True) 

    # Check min length of the entered passphrase 
    if len(passphrase) < min_length: 

    errors.append(f"Passphrase must be at least {min_length} characters long.") 

    # Check for special characters if needed 
    if add_special_characters and not re.search(r"[!@#$%^&*]", passphrase): 

    errors.append("Passphrase needs to include at least one special character for example - (! @ # $ % ^ & * )") 

    # Check for mixed case - uppercase and lowercase 
    if not (any(c.islower() for c in passphrase) and any(c.isupper() for c in   passphrase)): 

    errors.append("Passphrase must include uppercase and lowercase letters") 

    # Check for numeric digits 
    if not any(c.isdigit() for c in passphrase): 
    errors.append("Passphrase needs to include at least one digit") 

    # Return validation result 
    return len(errors) == 0, errors 

if __name__ == '__main__':
    main()
