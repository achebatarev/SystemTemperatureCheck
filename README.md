# SystemTemperatureCheck
This is a python script that allows to check GPU and CPU temperatures of the system
This script prints a temperature of all CPU cores and the GPU in the console every minute. 
If temperature gets above certain threshold this script sends a notification.
If temperature gets above 98 then it plays text to voice message along with a notification

## Install Requirements
- Open your terminal in this folder and run the following command:
`pip install -r requirements.txt`

## Running the App
- Open your terminal in this folder and run the following command:
`python app.py`

## Disclaimer
This script was created for and tested only on the Ubuntu 18.04
This script automatically assumes that user uses a NVIDIA GPU
