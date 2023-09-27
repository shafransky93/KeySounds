import subprocess
import sys


#(Uncomment and use synax in other program)

#from package_installer import check_and_install_packages

# List of required packages 
#required_packages = [
#    "package0",
#    "package1",
#    "package2",
#]

#if __name__ == "__main__":
#    check_and_install_packages(required_packages)

def check_and_install_packages(packages):
    missing_packages = []
    
    for package in packages:
        try:
            # Check if the package is installed
            subprocess.check_call([sys.executable, "-m", "pip", "show", package])
        except subprocess.CalledProcessError:
            # Package is not installed
            missing_packages.append(package)

    if missing_packages:
        print("The following packages are missing and will be installed:")
        for package in missing_packages:
            print(package)

        try:
            # Install missing packages using pip
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
            print("Packages installed successfully.")
        except subprocess.CalledProcessError:
            print("Error installing packages. Please install them manually.")
    else:
        print("All required packages are already installed.")

if __name__ == "__main__":
    check_and_install_packages(required_packages)
