# MACHINE READER

#### Video Demo: <https://youtu.be/MaT6rv0LNd8>

#### Description:

My final project is a desktop application coded in python. For GUI Custom Tkinter library was used. Application is split in two sections. First part of the appliaction allows the user to read multiple pdf files and save the read data in a SQLite database. Second part of the application is used to perfomr search operations and export it to excel worksheets.

## Read section

### Input setup

First the user chooses input folder where the pdf's are stored. The application displays how many files are in the folder a shows a folder path.

### Output setup

User then chooses where to output the read data, first option is to use existing database. This database has to have a table called "pdf_data" and two columns called "pdf_name" and "pdf_text". Second option is to create a new database called "output.db".
By clicking on "Select db or folder" user selects path to either an existing database or to folder where new database will be created.
Then user can choose if he wants to update the data in the existing database or to not update.
Lastly there is an option to use OCR engine to allow the application read image-like pdf's too.

### Read process

After the _"Read"_ button is clicked the application will start a separate thread in which the files in input folder are opened and processed with PYPDF library. If the text extract was not successful and the OCR checkbox is crossed, application then processes the pdf with OCRmyPDF engine to extract the text data.
All extracted data is then stored in SQLite database.

## Analyze section

### Input setup

First the user chooses a path to a database then will be analyzed. This database has to have a table called "pdf_data" and two columns called "pdf_name" and "pdf_text".

### Search criteria

There are two options for search criteria, keyword search or search between two keywords. Criteria can be a single word, multiple words or a fraction of a word. Type your keyword(s) to input field(s) and click Add to list. If you want to remove criteria from the list, select it by clicking on it and click _"Remove from list"_.

### Output setup

Click on _"Select output folder"_ button and choose location where output exel file will be stored.

### Analyze

After clicking on _"Analyse"_ button application will go through all data in the db applying the search criteria using the regular expressions library.
Results of search are stored in output.xlsx file. One column for each search criteria.
