# TCG-Scanner API

## How to run

After going through the setup, in a terminal,
navigate to this folder. Activate the virtual environment with the same steps
in the `Set virtual environment & install packages` section's activation instructions.
Then run with

```
python3 src/main.py
```

<br>

##### Optionally
For a better development experience, download [NodeJS](https://nodejs.org/en/download/). Then in the terminal instead of the command above, run

```
npx nodemon src/main.py
```

This will automatically reload the code whenever the file is saved

## Set Up

### 1. Download Tesseract

#### `Windows`

https://github.com/UB-Mannheim/tesseract/wiki
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

 <br>

### 2. Set virtual environment & install packages

With your terminal, `cd` into this project folder if on UNIX.\

Windows CMD example:\
`cd C:\Users\name\Documents\projects\api`

Use `venv` to create a virtual environment
`python3 -m venv venv`\
If python3 does not exist in your PATH, try `python` instead.

#### Activate the virtual environment

##### Windows CMD

> `venv\Scripts\activate.bat`

##### Windows Powershell

> `venv\Scripts\activate.ps1`

##### UNIX

> `source venv/bin/activate`

#### Install Packages

`python3 -m pip install -r requirements.txt`

## .env variables

`TESSERACT_PATH` - The path to tesseract's executable
