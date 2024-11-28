#!/usr/bin/env Python3
# This can be our default configuration settings that is already in dictionary format  
# Note: We may need to have a maximum passphrase, or change the default settings  

import os
import re
import random
#from PyDictionary() import PyDictionary()

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
PREDEFINED_DICTIONARY = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mountain", "river", "forest", "ocean", "desert",
    "tiger", "eagle", "shark", "whale", "panther",
    "bright", "dark", "shiny", "quick", "slow",
    "jump", "run", "fly", "swim", "climb",
    "stone", "metal", "wood", "glass", "plastic",
    "cloud", "storm", "rain", "snow", "wind",
    "happy", "sad", "angry", "calm", "brave",
    "earth", "fire", "water", "air", "light"
]
'''
For this project we cannot use third party modules, so the below is commented
but this this is an example of setting the PREDEFINED_DICTIONARY to a third party package
'''
#PREDEFINED_DICTIONARY = PyDictionary()



def write_default_config(filename="config.txt"):  

    ''' 
    Member - Zachary
    This function only writes the default config if the file doesn't exist.  
    This uses os module to check path for filename, which is defaulted as CONFIG.TXT  
    ''' 

    if not os.path.exists(filename):
        file = None  # This will initialize the file variable
        try:
            # Open the file for writing
            file = open(filename, "w")
            # Write each key-value pair from the default configuration
            for key, value in DEFAULT_CONFIG.items():
                file.write(f"{key} = {value}\n")
            print(f"The default configuration has been written to {filename}")
        except IOError as error:
            # This will handandle potential file operation errors
            print(f"Uh oh! An error occurred while writing the configuration: {error}")
        if file is not None:
            # Explicitly close the file if it was successfully opened
            file.close()

 
def load_config(filename="config.txt"):  

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
            print(f"Warning! There is a missing key '{key}' in config file. Please use the default: {DEFAULT_CONFIG[key]}")
 
    for key in config.keys():
        if key not in DEFAULT_CONFIG:
            print(f"Warning! There is an unknown key '{key}' in config file. This key will be ignored.")

    return config 

def get_user_keywords(config):
    """
    Member - Adetola
    Returns keywords based on config settings. 
    If no_input is True, skips user input and defaults to random words. 
    """
    if "no_input" in config and config["no_input"]:  # This checks config and skips user input if no_input is True
        print("No input mode enabled. Using random words.")
        word_count = config["passphrase_word_count"] if "passphrase_word_count" in config else 3
        return random.sample(PREDEFINED_DICTIONARY, word_count)

    # If no_input is False, then we ask the user for input
    keywords = input("Enter keywords (comma-separated) for passphrase generation: ").strip()
    if keywords: 
        return [word.strip() for word in keywords.split(",")]

    # If user provides no input, fall back to random words
    if "use_random_word" in config and config["use_random_word"]:
        word_count = config["passphrase_word_count"] if "passphrase_word_count" in config else 3
        print("Sorry. You have provided no keywords. Random words will now be used to generate a password.")
        return random.sample(PREDEFINED_DICTIONARY, word_count)

    print("Whoops. User Input and random words have been disabled in the config!")
    return []


def generate_passphrase(keywords, config): 
    """ 
    Member - Adetola
    Generates a passphrase using provided keywords or random words from a predefined list. 
    """ 
    
    try:
        word_count = config["passphrase_word_count"]
    except KeyError:
        word_count = 3  # Default value

    try:
        use_random_word = config["use_random_word"]
    except KeyError:
        use_random_word = True  # Default value

    
    if not keywords and use_random_word: 
        keywords = random.sample(PREDEFINED_DICTIONARY, word_count) 
    
    if len(keywords) < word_count: 
        additional_words = random.sample(PREDEFINED_DICTIONARY, word_count - len(keywords)) 
        keywords.extend(additional_words)
    
    return "".join(keywords) 


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

def randomize_cases(passphrase): 
    '''
    Member - Zhandong
    Randomizes the case of each character in the given passphrase, returning a new passphrase with randomized character cases. 
    '''
    # This will return passphrase if it is set to None or Blank
    if not passphrase:  
        return passphrase  

    return ''.join( 
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in passphrase 
    ) 


def validate_passphrase(passphrase, config): 

    """ 
    Member - Biswas
    Validates the generated passphrase against security criteria, such as length and character variety 
    """ 

    errors = []

    if "min_passphrase_length" in config:
        min_length = config["min_passphrase_length"]
    else:
        min_length = 12  # Uses the default value

    if "add_special_characters" in config:
        add_special_characters = config["add_special_characters"]
    else:
        add_special_characters = True  # Uses the default value

    # Check min length of the entered passphrase 
    if len(passphrase) < min_length: 
        errors.append(f"Passphrase must be at least {min_length} characters long.") 

    # Check for special characters if needed 
    if add_special_characters and not re.search(r"[!@#$%^&*()-_=+[]{}|;:',.<>?/`~]", passphrase): 
        errors.append("Passphrase needs to include at least one special character for example - (! @ # $ % ^ & * )") 

    # Check for mixed case - uppercase and lowercase 
    if not (any(c.islower() for c in passphrase) and any(c.isupper() for c in   passphrase)): 
        errors.append("Passphrase must include uppercase and lowercase letters") 

    # Check for numeric digits
    if not any(c.isdigit() for c in passphrase): 
        errors.append("Passphrase needs to include at least one digit") 

    # Return validation result
    return len(errors) == 0, errors

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

    if config["use_random_word"] or config["no_input"]: 
        # We are generating the passphrase using random words if `use_random_word` or `no_input` is enabled
        keywords = get_user_keywords(config)
        passphrase = generate_passphrase(keywords, config)

        # A while statement to verify the passphrase meets the minimum length
        while len(passphrase) < config["min_passphrase_length"]: 
            word_count = config["passphrase_word_count"] if "passphrase_word_count" in config else 1
            extra_keywords = random.sample(PREDEFINED_DICTIONARY, word_count)  # Add extra random words
            passphrase = generate_passphrase(keywords + extra_keywords, config)

    else: 
        # This will generate the passphrase based on user-inputted keywords
        keywords = get_user_keywords(config)
        passphrase = generate_passphrase(keywords, config)

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
        if not validate_passphrase(passphrase, config): 
            print("The generated passphrase does not meet security requirements. Please try again.") 
            return  # The program stops and allows the user to retry generation 

    # This displays the final passphrase or password securely to the user 
    display_passphrase(passphrase)  # This is the last step, showing the result


if __name__ == '__main__':
    main()
