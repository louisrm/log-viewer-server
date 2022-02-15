# PlotBot Server

This is a small flask server meant to parse .tlog files and provide flight data to the [PlotBot](https://github.com/louisrm/plot-bot-client) frontend. This process utilizes the [pymavlink](https://github.com/Parrot-Developers/mavlink/tree/master/pymavlink) toolbox to parse .tlog files and generate a JSON reply.

## Getting started

### Setup

1) `python3 -m venv venv`  
2) `.\venv\Scripts\activate`  
3) `pip install -r .\requirements.txt`

### Start server

`.\server.py`
