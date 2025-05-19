# Example file for Advanced Python by Joe Marini
# Using special module names
import collections

# __name__ is the name of the module
print("Modul name:", __name__)

# __file__ contains the path to the file from which the module was loaded
print("Modul name:", __file__)

# __package__ indicates the package that the module belongs to.
print("Modul name:", __package__)
print(collections.__package__)

if __name__ == "__main__":
    print("Denna kod körs")