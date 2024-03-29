[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MQMerlin/MQMerlin/">
    <img src="mqmerlin-logo.png" alt="Logo" width="300">
  </a>

  <h3 align="center">MQMerlin</h3>

  <p align="center">
    MQMerlin is a user-friendly tool aimed at simplifying the understanding and monitoring of MQ systems.
    <br />
    <br />
    <a href="https://github.com/MQMerlin/MQMerlin/issues">Bug Report</a>
    ·
  
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Usage-Prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#MQMerlin-Team">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
     <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

MQMerlin is designed to aid users in early issue identification and resolution by displaying crucial system information in an easily comprehensible manner. A standout feature is its specialized AI chatbot that addresses user queries regarding IBM MQ and offers troubleshooting advice for identified issues. Based on modern language learning models, this chatbot has shown promise for future enhancements through rigorous testing.



<!-- GETTING STARTED -->
## Getting Started

### Usage Prerequisites
- A compatible computer OS (Mac, Windows, Linux).
- Installed Python 3.
- Installed Java.

### Downloading the Application
1. Go to the MQMerlin GitHub repository at github xxx.
2. Download the entire repository to your local machine.
3. Extract the downloaded files to a preferred location on your machine.

### Frontend Setup (Unity)
1. Navigate to the folder containing the built Unity app within the downloaded repository.
2. Run the version of the app corresponding to your OS (e.g., Windows, MacOS, Linux).

### Backend Setup
1. Navigate to the backend folder within the downloaded repository.
2. Confirm the installation of Python 3 and Java on your machine by running `python3 --version` and `java -version` in the terminal.
3. Install the necessary Python packages using pip.

### Running the Backend
1. Inside the backend folder, start the Flask server using the specified command.
2. The Flask server will start and listen on port 5000 by default.
3. Navigate to the ChatBot module folder within the backend folder and replace the APIKEY field with your own OpenAI API key.

### Running MQMerlin
1. With the backend running, launch the Unity app.
2. The frontend will automatically connect to the backend via port 5000.
3. Now, you can interact with the MQMerlin application through the Unity interface.

>Note: The default port 5000 can be changed if desired, both in the Flask server configuration and in the Unity app settings.



<!-- USAGE -->
## Usage

For a more detailed understanding and operation of the MQMerlin application, refer to the provided System Manual in the GitHub repository.



<!-- CONTRIBUTING -->
## Contributing

Contribute to MQMerlin by following the setup instructions under "Getting Started" for development purposes. For more information, check the Waffle board or contact the MQMerlin community.



<!-- CONTACT -->
## MQMerlin Team

- [Zaid Samedi](https://github.com/ZaidSamedi)
- [Fergus Cassidy](https://github.com/FergusCassidy)
- [Hugo Giddins](https://github.com/HugoGiddins)

We express our deepest gratitude towards the IBM supervisors: John McNamara, Yuzi Nakamura, and Richard Coppen for their invaluable guidance and support throughout this project. Further acknowledgements and appreciations are extended to the entire MQMerlin community for their collaborative efforts.

MQMerlin project link: [https://github.com/MQMerlin/](https://github.com/MQMerlin/)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

- IBM Supervisors: John McNamara, Yuzi Nakamura, and Richard Coppen.
- The MQMerlin community for their contributions and support.



<!-- LICENSE -->
## License

Distributed under the Standard GitHub License. See `LICENSE` for more information.



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MQMerlin/mqmerlin.svg?style=for-the-badge
[contributors-url]: https://github.com/MQMerlin/MQMerlin/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MQMerlin/mqmerlin.svg?style=for-the-badge
[forks-url]: https://github.com/MQMerlin/MQMerlin/network/members
[stars-shield]: https://img.shields.io/github/stars/MQMerlin/mqmerlin.svg?style=for-the-badge
[stars-url]: https://github.com/MQMerlin/MQMerlin/stargazers
[issues-shield]: https://img.shields.io/github/issues/MQMerlin/mqmerlin.svg?style=for-the-badge
[issues-url]: https://github.com/MQMerlin/MQMerlin/issues
[license-shield]: https://img.shields.io/github/license/MQMerlin/mqmerlin.svg?style=for-the-badge
[license-url]: https://github.com/MQMerlin/MQMerlin/blob/master/LICENSE.txt
