# KeyWizard
Python script that makes a sound whenever you hit a key. 

<details>
<summary>F.A.Q.</summary>
  
Q: It's kinda annoying... why did you do this...

A: As a vector for making a automatic package installer.

</details>

# Python Package Installer
This Python script simplifies the process of checking for and installing required Python packages in your project. It provides a convenient way to ensure that all necessary dependencies are available for your project to run smoothly.

# Prerequisites
Before using the script, ensure you have the following prerequisites:

Open your IDE of choice and navigate to the directory containing the script you wish to have the requirerd packages installed for.

The script will automatically check if the required packages are installed. If any are missing, it will prompt you to install them.

Usage

Checking and Installing Packages
The script includes a check_and_install_packages function that can be easily integrated into other Python projects. This function automates the process of verifying the presence of required packages and installing any that are missing.

1. Import the check_and_install_packages function:
```
from package_installer import check_and_install_packages
```

2. Define a list of required packages:
```
required_packages = [
    "package0",
    "package1",
    "package2",
]
```
Replace "package0", "package1", "package2", and so on with the names of the packages your project depends on.

3. Call the check_and_install_packages function:
```
if __name__ == "__main__":
    check_and_install_packages(required_packages)
```
By running this code snippet, the script will automatically check for the specified packages and install any that are missing.

## Example Usage:
An example of how to use the check_and_install_packages function is provided in the header of the package_installer.py script itself. You can uncomment the relevant lines and customize the list of required packages to match your project's dependencies.
