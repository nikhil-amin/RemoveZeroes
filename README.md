# RemoveZeroes
A simple Python Script to remove 0 quantity row from a Product Database in CSV file.


Before starting, make sure you have **_Python_** installed in your system.

`RemoveZeroes.py` is the python script file which is placed at root path. (_User can place it anywhere as per their comfort_)

`Product_DB.csv` is a sample Database for testing the python script. It contains the following column headers.

------------------------------------------------------------------------------------------------
| P_ID | PRODUCT NAME | INCHARGE | BARCODE | STOCK | QUANTITY | UNITS | AREA | CATEGORY | RATIO |

------------------------------------------------------------------------------------------------

Kindly note that the column number of **QUANTITY** is 6.

Now open your terminal and go to the directory where your `RemoveZeroes.py` is placed. 
Run `python RemoveZeroes.py` and specify the path to the directory containing your `Product_DB.csv`.
Enter the CSV filename (_i.e `Product_DB`_) and Quantity Column Number followed by Output filename of your choice.

_Also note that you need not specify the extension (.csv) as an input_

>Here is the screenshot of my output terminal:
<img src="/.github/TerminalScreenshot.png" width="800" height="450" alt="TerminalScreenshot"/>
