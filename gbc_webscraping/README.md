Documentation for "Program Finder"

The "Program Finder" script is designed to scrape program information from the George Brown College website for computer-related programs, transform it into a structured format, and save it to a CSV file for further analysis.

Data Extraction

The extract function sends an HTTP GET request to the George Brown College website, with a specified year to filter programs by, and returns the HTML content of the page as a Beautiful Soup object.

Data Transformation

The transform function extracts program information from the HTML content of the page, such as program title, program summary, and program duration. It creates a dictionary object for each program and adds it to a list of programs.

Data Loading

The for loop calls the extract and transform functions for each year in the range 2020 to 2022. The program information is stored in a list of dictionaries called programs, which is then converted into a Pandas data frame. Finally, the program data is saved to a CSV file called programs.csv.
