<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JonaRichter/email_bot">
    <img src="images/logo.webp" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">E-Mail Bot</h3>

  <p align="center">
    This Python script automates the process of sending personalized emails to Spotify playlist managers. It reads contact information from a CSV file, constructs customized email messages introducing the sender (a music producer) and their latest song release, and sends the emails via SMTP with SSL authentication to the GMX mail server. The goal is to streamline outreach efforts and increase the likelihood of the song being considered for playlist inclusion.
    <br />
    <a href="https://github.com/JonaRichter/email_bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JonaRichter/email_bot">View Demo</a>
    ·
    <a href="https://github.com/JonaRichter/email_bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/JonaRichter/email_bot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<!--
[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `JonaRichter`, `jonarichter_bot`, `twitter_handle`, `Jona Richter`, `gmx`, `jonarichter`, `E-Mail Bot`, `project_description`
-->
<p align="right">(<a href="#readme-top">back to top</a>)</p>




### Built With

* [![Python][Python.js]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* **Install Python on your machine**
  * For Windows, download and install Python from [python.org](https://www.python.org/downloads/windows/).
  * For macOS, download and install Python from [python.org](https://www.python.org/downloads/macos/).
  * For Linux, use your package manager to install Python. For example, on Ubuntu, you can run:
    ```sh
    sudo apt-get update
    sudo apt-get install python3
    ```

* **Verify the installation by checking the Python version:**
  ```sh
  python --version

### Installation

To set up and run this script, follow the steps below:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/JonaRichter/email_bot.git
    cd email_bot
    ```

2. **Create and activate a Python virtual environment:**
    * For Windows:
      ```bash
      python -m venv .venv
      .venv\Scripts\activate
      ```
    * For macOS and Linux:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the `config.env` file:**  
    Populate the `config.env` file with your configuration details:
    ```bash
    SENDER_EMAIL=your_email@example.com
    SENDER_EMAIL_PASSWORD=your_password
    SENDER_NAME=Your Name
    SONG_TITLE=Your Song Title
    SONG_LINK=Your Song Link
    ```
    Replace the placeholder data with your actual data.

5. **Set up the `contacts_file.csv`:**  
    Populate the `contacts_file.csv` with your actual data.

6. **Adjust your E-Mail content**  
    Adjust the content you want to include to your E-Mail to your preferences in `main.py`


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

After filling the data, just run the `main.py`and enjoy!  
An example E-Mail could look like this:

![Example Mail](images/example_email.png)

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/JonaRichter/jonarichter_bot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - jonatrichter@gmail.com

Project Link: [https://github.com/JonaRichter/email_bot](https://github.com/JonaRichter/email_bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JonaRichter/email_bot.svg?style=for-the-badge
[contributors-url]: https://github.com/JonaRichter/email_bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JonaRichter/email_bot.svg?style=for-the-badge
[forks-url]: https://github.com/JonaRichter/email_bot/network/members
[stars-shield]: https://img.shields.io/github/stars/JonaRichter/email_bot.svg?style=for-the-badge
[stars-url]: https://github.com/JonaRichter/email_bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/JonaRichter/email_bot.svg?style=for-the-badge
[issues-url]: https://github.com/JonaRichter/email_bot/issues
[license-shield]: https://img.shields.io/github/license/JonaRichter/email_bot.svg?style=for-the-badge
[license-url]: https://github.com/JonaRichter/email_bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jona-richter-b373ab2b9/
[product-screenshot]: images/screenshot.png

[Python.js]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
