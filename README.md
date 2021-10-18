<br />
<p align="center">
  <a href="https://github.com/nenad-zaric/reorg">
    <img src="images/logo.png" alt="Logo" width="256" height="128">
  </a>

  <h3 align="center">reorg</h3>

  <p align="center">
    Python script for organizing downloads directory
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

Reorg is a small python script that organizes your downloads directory by filetype. 

Tested on:
<br/>
Kubuntu 20.04.1 LTS
<br/>
Windows 10 Pro
<br/>
Windows 11 Pro


### Built With

* Python 3.8
    * Watchdog
    * python-magic



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
```sh
git clone https://github.com/nenad-zaric/ReORG
```
2. Install dependencies
```sh
python -m pip install watchdog
python -m pip install python-magic
```
If you get ```ImportError: failed to find libmagic. Check your installation ``` try:
```sh
python -m pip uninstall python-magic
python -m pip install python-magic-bin==0.4.14
```

<!-- CONTACT -->
## Contact

Nenad Zaric - nzaric31@gmail.com

Project Link: [https://github.com/nenad-zaric/ReORG](https://github.com/nenad-zaric/reorg)

