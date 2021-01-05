[![licence](http://img.shields.io/badge/licence-MIT-blue.svg?style=flat)](https://github.com/aigora-de/rwriWhatsapp/blob/master/LICENCE)
# RWRI WhatsApp Profiler #
This repo is the beginnings of a "profiler" to allow us to analyse our RWRI WhatsApp chat.

It has been started using Python 3.7.

## Installation ##
I use Pycharm with a virtual Python 3.7 environment.

Start by cloning this repo:

    git clone https://github.com/aigora-de/rwriWhatsapp.git

You should also download a copy of the RWRI WhatsApp chat export and place it in a direct called 'data' under the project root directory.

    cd rwriWhatsapp
    mkdir data
    cp <from your source> ./data
    
### Virtual Python Environment ###
You use whatever Python environment suits you, but I use a virtual environment with Python 3.7:

    cd rwriWhatsapp # The project root folder
    pip install virtualenv
    virtualenv --python=/usr/bin/python3 venv # Or whatever you prefer to call your virtual python environment
    cd venv/bin
    .activate
    cd ../.. # back to the root directory
    <venv>pip3 install -r requirements.txt
    
### Third Party Libraries ###
If you followed the instructions above, you should have installed dependency libraries into your Python3 virtual environment:

- numpy==1.19.4
- pandas==1.2.0
- python-dateutil==2.8.1
- pytz==2020.5
- six==1.15.0

This embryonic profiler also uses two third party libraries not installed as above:

- [whatsapp-chat-parser](https://github.com/mazen160/whatsapp-chat-parser "whatsapp-chat-parser")
- [word_cloud](https://github.com/amueller/word_cloud "word_cloud")

One way to get these is to clone the git repositories into a directory under your root directory:

    cd rwriWhatsapp
    mkdir site_libraries
    git clone https://github.com/mazen160/whatsapp-chat-parser.git
    cd whatsapp-chat-parser
    python3 setup.py install
    
    cd ..
    git clone https://github.com/amueller/word_cloud.git
    cd word_cloud
    pip3 install .
    
# Contributing #
Contributions from RWRI alumni are encouraged. Please submit your ideas or better still a Pull Requests :)

# Licensing #
This code is currently MIT licensed [![licence](http://img.shields.io/badge/licence-MIT-blue.svg?style=flat)](https://github.com/aigora-de/rwriWhatsapp/blob/master/LICENCE)
