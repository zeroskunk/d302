># d302
d302 serial rfid reader #python3#

python with qtpython for reading and writing RFID Tags with a D302 reader
I is a lot of work to do so this is my starting point

enjoy


# Debian install python deps

## python3
```
bash:~/ apt-get install python3-serial
bash:~/ apt-get install python3-pyqt5
```

## pyinstaller
```
bash:~/ apt-get install python3-pip
bash:~/ pip3 install pyinstaller
```

## make executable
```
bash:/foldername/ pyinstaller d302.py --onefile --windowed
```
### on windows 32Bit Python QT installation
```
c:\folderpath_to_script\>pyinstaller --onefile --noconsole --win-private-assemblies --win-no-prefer-redirects --name d302w32 --specpath pyinstaller d302.py
```

# TODO
It's quit a lot of work left -> Design and functionality
