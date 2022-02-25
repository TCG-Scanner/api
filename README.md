# TCG-Scanner API

## Set Up

### 1. Download Tesseract

#### `Windows`

https://github.com/UB-Mannheim/tesseract/wiki\
If you don't know whether to use 64 or 32 bit, most likely you will be using 64 bit.\
Download the tesseract-ocr-w{BIT}-setup-{VERSION}.exe file if running on 64 bit.\

`BIT` - 64 or 32\
`VERSION` - Version number of tesseract

Add tesseract to your `PATH`\
or\
set `TESSERACT_PATH` to be
`"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"` or wherever you installed tesseract,
in your `.env` file. If you don't have a `.env` file yet copy or rename `.env.example`
to be `.env`, then uncomment `TESSERACT_PATH` and set it's value.

##### Please note to use 2 backslashes in your path when setting the value in the `.env` file.

#### `MacOS`

Using [brew](https://brew.sh/), run `brew install tesseract`\
You do not need to set the `TESSERACT_PATH` envrionment variable.
If you run into any trouble with tesseract, make sure that environment variable
is not set.

#### `Linux`

Please refer to https://tesseract-ocr.github.io/tessdoc/Installation.html\
if your distrobution is not listed below.

##### Debian

`sudo apt install tesseract-ocr`

##### Arch

`sudo pacman -S tesseract`

## .env variables

`TESSERACT_PATH` - The path to tesseract's executable
