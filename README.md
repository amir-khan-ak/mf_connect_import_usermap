# Micro Focus Connect - Importing Usermaps from Excel File
# mf_connect_import_usermap
This python script allows to import usermap into MF Connect from an excel file

# Pre-requisites
- Download & Install Python 3.8 or higher: https://www.python.org/downloads/
- Install pandas library - https://pypi.org/project/pandas/
- Install requests library - https://pypi.org/project/requests/2.7.0/
- Install xlrd library - https://pypi.org/project/xlrd/

# Usage
Using commandline run:
cd "directory where importUserMaps.py is located"
python importUserMaps.py <url> <credentials> <path_to_excel_file_with_users.xls>

# Parameters
- <url> Micro Focus Connect URL in the exact format as follow: 'http://serverhost:port'.
- <credentials> Credentials for MF Connect in the following format: '<user>:<password>:<authenticator>' 
- <path_to_excel_file_with_users.xls> the full path to the upload excel containing the users.

# Example: 
cd C:\importUsermaps
C:\importUsermaps>python importUserMaps.py "http://localhost:8081" "Administrator:Administrator:Micro Focus Connect" "C:\Users\khanamir\Documents\import_usermaps.xlsx"

# Short Demo Video:
https://youtu.be/nY6ZmSBcmCs
