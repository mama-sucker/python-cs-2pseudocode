
# Python script to turn code into pseudocode 
# more specifically c# code

import os
import sys
import re
from time import sleep

def convert_csharp_to_pseudocode(csharp_code):
    # Remove single-line comments
    csharp_code = re.sub(r'//.*', '', csharp_code)
    
    # Convert common C# constructs to pseudocode
    pseudocode = csharp_code.replace('for', 'loop')
    pseudocode = pseudocode.replace('if', 'conditional')
    pseudocode = pseudocode.replace('else', 'else')
    pseudocode = pseudocode.replace('Console.WriteLine(', 'Output: ')
    # Add more conversions as needed
    
    return pseudocode

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    real_cs_path = os.path.join(script_directory, "real.cs")

    try:
        with open(real_cs_path, "r") as file:
            csharp_code = file.read()
            
        pseudocode = convert_csharp_to_pseudocode(csharp_code)

        # Save pseudocode to a .txt file
        converted_pseudocode_path = os.path.join(script_directory, "converted_pseudocode.txt")
        with open(converted_pseudocode_path, "w") as file:
            file.write(pseudocode)

        print("Pseudocode saved as 'converted_pseudocode.txt'")

    except FileNotFoundError:
        print("'real.cs' file not found in the working directory.")



sleep(10)
exit()

