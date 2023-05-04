# Inspireboard
# About The Project

Inspireboard is a mood board creator web app. The app was built using Html, CSS, and Django. The user can log on to create their own mood boards by uploading images or can select from existing templates.The user can drag and drop images in any place. In the case of templates, the user can shuffle the order of images. Finally the created mood-board can be downloaded in a png format.

## App Preview
![s1](https://user-images.githubusercontent.com/83969235/236239230-93d1c2b6-9926-4f9e-b341-b038cadd0fd6.png)
![s2](https://user-images.githubusercontent.com/83969235/236239273-7803b765-70fe-4d52-b8fa-3d069659ea15.png)
![mood_board (1)](https://user-images.githubusercontent.com/83969235/236239338-4763dc13-4add-4cbd-9520-325924d03796.png)
![mood_board (2)](https://user-images.githubusercontent.com/83969235/236239375-962701bd-9f50-4e6f-878e-b19c56bd35db.png)

## Built With

* Django framework
* Html
* Css

<!-- GETTING STARTED -->
# Getting Started
## Dependencies

* Django==4.1.3
* pyscreenshot==3.1
* virtualenv==20.17.1
* virtualenvwrapper-win==1.2.7
* google-api-core==2.11.0
## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Sinta-Paul/Inspireboard
   ```
2.Create a virtual environment to install dependencies in and activate it:

  ```sh
  $ virtualenv2 --no-site-packages env
  $ source env/bin/activate
  ```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

<!-- USAGE EXAMPLES -->
# Usage
InspireBoard is a solution to bring your ideas together and visualise them. The predefined templates makes this job easier.

<!-- ROADMAP -->
# Roadmap

- Login 
- Choose from existing templates or create your own mood-board
- Add name,caption and images
- Export the mood-board

<!--FUTURE -->
# Future Scope
*  To be able to add more templates
*  To add options to change images and resize them,

<!-- CONTACT -->
# Project Link: 
[https://github.com/Sinta-Paul/Inspireboard]
