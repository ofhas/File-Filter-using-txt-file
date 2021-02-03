# File-Filter-using-txt-file

Just a simple GUI app that move/copies files out of a given txt file that contains all the desired file names, also you need to choose soruce folder that contains the files and destination folder.\
Every file name should have the type of file after it's name, for example: example.jpg.
You could use the file lister repo locate here: https://github.com/ofhas/GUI-txt-file-from-folder/blob/master/src/listTXTFile.py to generate a txt file list of files you wish to move or copy to a destination folder.\

If you wish to convert the script into a exe file you could use the pyinstaller module, you should do the followiing:\
pip install pyinstaller.\
Open the files_filter_v3.py file folder.\
Right click you mouse and open powershell window.\
Write the command pyinstaller -w files_filter_v3.py.\
This will create a dist folder inside it you'll find a folder with the .py file name which has the exe file.




