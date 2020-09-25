<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="256" height="128">
  </a>

  <h3 align="center">reorg</h3>

  <p align="center">
    Python script for organizing downloads directory
    <br />
    IMPORTANT: For now works only with chrome
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

Reorg is a small python script that organizes your downloads directory by filetype. Feel free to contribute if you want.

Tested on:
Kubuntu 20.04.1 LTS
Windows 10 Pro


### Built With

* Python 3.8
* Python modules:
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

Nenad Zaric - [@AnunnakiNenad](https://twitter.com/AnunnakiNenad) - nzaric31@gmail.com

Project Link: [https://github.com/nenad-zaric/ReORG](https://github.com/nenad-zaric/reorg)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=flat-square
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=flat-square
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=flat-square
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=flat-square
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=flat-square
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
[product-screenshot]: images/screenshot.png
