# rinex-summary

This python code reads your RINEX File and then converts the ECEF position to WGS84 format.
It also extracts the GNSS Receiver details including Brand and Model Name.
The baseline.py code computes the distance between positions of two RINEX files

<br> Do not forget to install required packages
<br> ``` pip install -r requirements.txt ```

How to use readrin.py:
1. Place this python file in the directory where the RINEX file is
2. Run "python readrin.py" in the terminal
3. Enter the RINEX filename when prompted

How to use baseline.py
1. Place this python file in the directory where the RINEX file is
2. Run "python baseline.py" in the terminal
3. Enter the RINEX filenames of both the base and rover when prompted

The outputs will be printed in the terminal
