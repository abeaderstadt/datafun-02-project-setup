"""
Module: beaderstadt_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Alissa Beaderstadt

"""

#####################################
# Import Modules at the Top
#####################################

# Import modules from standand library

import time
import pathlib



# Import local modules

import utils_beaderstadt

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int, exclude_years: list =[]) -> None:
    '''
    Create folders for a given range of years, with an option to exclude specific years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    exclude_years -- A list of years to exclude when folders are created.
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year}, end_year={end_year}, exclude_years={exclude_years}")
   
    for year in range(start_year, end_year + 1):
        if year in exclude_years:
            print(f"Skipping folder creation for {year} (excluded year).")
            continue 
        # Create a folder path for the year
        folder_path = project_path.joinpath(str(year))

         # Create a new folder at the path
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")
        
        
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a given list of names in all lowercase and spaces removed.

    Arguments:
    folder_list -- A list of folder names to create.
    to_lowercase -- If true, change all folder names to lowercase.
    remove_spaces -- If true, remove spaces from folder names.
    '''
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, "
          f"to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")

    for name in folder_list:
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(" ", "")
        # Create a folder path for the name
        name_path = project_path.joinpath(name)

        # Create a new folder at the path
        name_path.mkdir(exist_ok=True)
        print(f"Created folder: {name_path}")
        
  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders from a given list of names with prefixes.

    Arguments:
    folder_list -- A list of folder names to create.
    prefix -- A prefix to add to the beginning of the folder names.
    '''
    # Log the function call and its arguments

    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix='{prefix}'")
    
    for folder_name in folder_list:
        # Create a path for the folder
        folder_path = project_path.joinpath(f"{prefix}{folder_name}")

        # Create a new folder at the path
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")


#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically waiting a specified amount of time between each folder creation.

    Arguments:
    duration_seconds -- The wait time between folder creations in seconds.
    '''
    # Log the function call and its arguments

    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")

    for i in range(5):  
        # Create a folder name
        folder_name = f"folder{i+1}"

        # Create the path for the folder
        folder_path = project_path.joinpath(folder_name)

        # Create a new folder at the path
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")
        time.sleep(duration_seconds)

  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_beaderstadt.get_byline()}")

    # Call function 1 to create folders for a range with exclusion
    create_folders_for_range(start_year=2020, end_year=2023, exclude_years=[2022])

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
   
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()


