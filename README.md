# hrm-to-tcx
Simple wrapper for JWHGT to process all HRM files in one directory. Config your input and output path in the script or use it as template for your own use case.

## Usage

The script has no arguments. It converts all HRM files from /home/chris/Downloads/in to /home/chris/Downloads/out. To make it work, config your path' in the variables:

    IN = "<path-for-your-in-directory>"
    OUT = "<path-for-your-out-directory>"
    JWHGT = "<jwhgt-installation-path>/JWHGT"

Then copy all HRM files into the `in` directory and call:

    $ python3 <hrm-to-tcx-installation-path>/convert.py 

Example output: 

    $ python3 convert.py 
    OK  14012301.hrm --> 14012301.tcx
    OK  14013101.hrm --> 14013101.tcx
    OK  14013102.hrm --> 14013102.tcx
    OK  14022301.hrm --> 14022301.tcx

## Credits

Many thanks to **Jochen-Matthias Wienke** for sharing JWHGT with us, see http://jwhgt.worldwidehome.de/ !!!
