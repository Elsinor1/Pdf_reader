# MACHINE READER

#### Video Demo: <URL HERE>

#### Description:

My final project is a desktop application coded in python. For GUI Custom Tkinter library was used. Application is split in two sections. First part of the appliaction allows the user to read multiple pdf files and save the read data in a SQLite database. Second part of the application is used to perfomr search operations and export it to excel worksheets.

Read section
Input and Output setup
First the user chooses input folder where the pdf's are stored. The application displays how many files are in the folder a shows a folder path.
User then chooses where to output the read data, first option is to use existing database. This database has to have a table called "pdf_data" and two columns called "pdf_name" and "pdf_text". Second option is to create a new database called "output.db".
By clicking on Select db or folder user selects path to either an existing database or to folder where new database will be created.
Then user can choose if he wants to update the data in the existing database or to not update.
Lastly there is an option to use OCR engine to allow the application read image-like pdf's too.

Read process
After the "Read" button is clicked the application will start a separate thread in which the files in input folder are opened and processed with PYPDF library. If the text extract was not successful and the OCR checkbox is crossed, application then processes the pdf with OCRmyPDF engine to extract the text data.
All extracted data is then stored in SQLite database.

Analyze section
First the user chooses a path to a database then will be analyzed. This database has to have a table called "pdf_data" and two columns called "pdf_name" and "pdf_text".
