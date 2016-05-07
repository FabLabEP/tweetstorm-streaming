# tweetstorm-streaming
Turn a Raspberry Pi into a streaming tweet printer.

Must first install Python libraries required by the thermal printer library:

sudo apt-get install python-serial python-imaging python-unidecode

Replace your /boot/cmdline.txt and /etc/init/ files with the ones provided for software access to the serial port.

Setup thermal printer using Adafruit's python library (https://github.com/adafruit/Python-Thermal-Printer).

Reboot, then run this script in Python.  Will listen for tweets including your tracking strings and output the text on the thermal printer.
