# Python-eel react app template

## Get Started

- Clone the repository onto your system
- Open a terminal and run `npm install` in the project directory to download the node modules

- If you do not have python installed, install python
    - The installation varies based on the system you are on
- If python is installed run `pip install eel` or `pip3 install eel` based on which version of python and pip you have
    - In the examples I am using `python3`. Remove the `3` if it is uneeded for your system
    - You can check pyhton verion by running `python -V` or `python3 -V`
    - You can check pip version by running `pip -V` or `pip3 -V`

## For Development

- Open a terminal and run `npm start`
    - This starts a development server running your code
- Open a second terminal and run `python3 index.py -dev`
    - This opens a python-eel window for you to develop in

## Building a production version

- Open a terminal and run `npm run build`
    - This will create a `/build` folder with the production code inside
- To view the built project run `python3 index.py`
    - This will open a python-eel window allowing you to view and test your program

## Convert the project to an executable

- Open a terminal and run `python3 -m eel index.py build`
    - This will take your production code inside of the build folder and convert it to a standalone executable file
- The executable will be in `/dist/index`
    - Run the executable to view your program
