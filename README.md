

![Contributors](https://img.shields.io/github/contributors/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV.svg)
![Forks](https://img.shields.io/github/forks/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV.svg)
![Stars](https://img.shields.io/github/stars/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV.svg)
![Issues](https://img.shields.io/github/issues/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV.svg)
![License](https://img.shields.io/github/license/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV.svg)



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h2 align="center">Document Text Detection</h2>

  <p align="center">
    An OpenCV and OCR project detecting text from photos taken from cameras.
    <br />
    <a href="https://github.com/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV"><strong>Explore the docs »</strong></a>
    <br />
    <br />
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
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project transforms images of documents into flat, readable views by detecting document boundaries using computer vision techniques, applying perspective warping, and extracting text via OCR.

- Resize images with aspect ratio preservation for faster processing.
- Detect document edges using Canny edge detection and Hough Line Transform.
- Calculate intersection points to identify document corners.
- Apply homography and perspective warping to obtain flat document views.
- OCR the warped images to extract textual content along with confidence scores.

### Built With


* [![](https://img.shields.io/badge/OpenCV-007ACC?style=for-the-badge&logo=opencv&logoColor=white)][Next-url]
* [![](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)][React-url]
* [![](https://img.shields.io/badge/PaddlePaddle-FF4088?style=for-the-badge&logo=pytorch&logoColor=white)][Vue-url]
* [![](https://img.shields.io/badge/PaddleOCR-33CCFF?style=for-the-badge&logo=github&logoColor=white)][Angular-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

1. Clone the repository:

```sh
    git clone https://github.com/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV.git
    cd your-project
```

2. Install the dependencies.
3. Configure your OCR language in `config/settings.py`
4. Place your input images in the img directory.

### Prerequisites

Install dependenices using pip:
* OpenCV
  ```sh
  npm install cv2
  ```
* NumPy
  ```sh
  npm install numpy
  ```
* PaddlePaddle
  ```sh
  npm install paddlepaddle
  ```
* PaddleOCR
  ```sh
  npm install paddleocr
  ```


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## OCR Engine

Implemented using [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR), a powerful OCR engine supporting multiple languages and scripts.

---

## Configuration

The language for OCR recognition is set in: English

Update the `LANG` variable to specify the desired OCR language(s).

---

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

<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Mishanil - mishanil@dockly.uk

Project Link: [https://github.com/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV](https://github.com/mishanilkazreen/Document-Photos-Recognistion-with-OpenCV#)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
