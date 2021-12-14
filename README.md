<div align="center">

# [PewPewPew](http://pewpewpew-fe.herokuapp.com/)
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![Stargazers][stars-shield]][stars-url]
[![Forks][forks-shield]][forks-url]
![Build Badge][build-badge]

<br>

  PewPewPew is a simple grid-based puzzle game designed to give you a few minutes cool-down between activities. Try to top our leaderboard!

  This repository is for the API that stores our game data and manages our leaderboard.

---

## Contributors

|Jacq Whitmer|Dane Brophy|Kevin Mugele|Joshua Horner|Logan Vincent
|--- |--- |--- |--- |--- |
|[<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=flaste&logo=github&logoColor=white" />](https://github.com/jrwhitmer)|[<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=flaste&logo=github&logoColor=white" />](https://github.com/danembb)|[<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=flaste&logo=github&logoColor=white" />](https://github.com/kevinmugele)|[<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=flaste&logo=github&logoColor=white" />](https://github.com/jphorner)|[<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=flaste&logo=github&logoColor=white" />](https://github.com/logandv3)
|[<img src= "https://img.shields.io/badge/in-LinkedIn-blue" />](https://www.linkedin.com/in/jacqwhitmer/)|[<img src= "https://img.shields.io/badge/in-LinkedIn-blue" />](https://www.linkedin.com/in/dane-brophy/)|[<img src= "https://img.shields.io/badge/in-LinkedIn-blue" />](https://www.linkedin.com/in/kevinmugele/)|[<img src= "https://img.shields.io/badge/in-LinkedIn-blue" />](http://www.linkedin.com/in/logan-vincent/)|[<img src= "https://img.shields.io/badge/in-LinkedIn-blue" />](https://www.linkedin.com/in/joshuapaulhorner/)


## Table of Contents
|Links
|--- |
[Tools Used](#tools-used)
[Setup](#setup)
[Learning Goals](#learning-goals)
[Database Schema](#database-schema)
[API Endpoints](#api-endpoints)


## Tools Used

|Development|Development|Testing|Deployment
|--- |--- |--- |--- |
|[<img src="https://img.shields.io/badge/-python3-red" />](https://www.python.org/downloads/)|[<img src="https://img.shields.io/badge/Git-F05032.svg?&style=flaste&logo=git&logoColor=white" />](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)|[<img src="https://img.shields.io/badge/-pytest-orange" />](https://docs.pytest.org/en/6.2.x/)|[<img src="https://img.shields.io/badge/Heroku-430098.svg?&style=flaste&logo=heroku&logoColor=white" />](http://virtual-watch-party.herokuapp.com)|
|[<img src="https://img.shields.io/badge/-flask-yellow" />](https://flask.palletsprojects.com/en/2.0.x/)|[<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=flaste&logo=github&logoColor=white" />](https://desktop.github.com/)|[<img src="https://img.shields.io/badge/sql-alchemy-yellowgreen" />](https://www.sqlalchemy.org/)|[<img src="https://img.shields.io/badge/circle-CI-blue" />](https://circleci.com/)|
|[<img src="https://img.shields.io/badge/flask-seeder-yellow" />](https://pypi.org/project/Flask-Seeder/)|[<img src="https://img.shields.io/badge/flask-migrate-yellowgreen" />](https://flask-migrate.readthedocs.io/en/latest/)|[<img src="https://img.shields.io/badge/-SQLite3-blue" />](https://www.sqlite.org/index.html)|[<img src="https://img.shields.io/badge/Postman-FF6E4F.svg?&style=flat&logo=postman&logoColor=white" />](https://www.postman.com/product/rest-client/)|

</div>

<div align="center">

## Setup

</div>


  This project requires Python3

  * Fork this repository
  * From the command line, install dependencies and set up your DB:
      * `python3 -m venv venv`
      * `source venv/bin/activate`
      * `pip3 install flask`
      * `pip3 install flask-sqlalchemy`
      * `pip3 install flask-migrate`
      * `pip3 install pytest`
      * `pip3 install pytest-flask`
      * `pip3 install pytest-cov`
      * `pip3 install jsonify`
      * `pip3 install flask-seeder`
      * `export FLASK_APP=pewpewpew.py`
      * `python3 -m flask db migrate -m "games table"`
      * `python3 -m flask db upgrade`
      * `flask seed`
  * Run the test suite with `pytest`
  * Run your development server with `flask run` to see the app in action.

  * [Heroku Deployment](https://pewpewpew-be.herokuapp.com/), for production


<div align="center">

## Learning Goals

</div>


&nbsp; &nbsp; ⭐ &nbsp; &nbsp; Demonstrate knowledge you’ve gained throughout Turing<br>
&nbsp; &nbsp; ⭐ &nbsp; &nbsp; Use an agile process to turn well defined requirements into deployed and production ready software<br>
&nbsp; &nbsp; ⭐ &nbsp; &nbsp;Gain experience dividing applications into components and domains of responsibilities to facilitate multi-developer teams. Service oriented architecture concepts and patterns are highly encouraged.<br>
&nbsp; &nbsp; ⭐ &nbsp; &nbsp; Explore and implement new concepts, patterns, or libraries that have not been explicitly taught while at Turing<br>
&nbsp; &nbsp; ⭐ &nbsp; &nbsp; Practice an advanced, professional git workflow using Git Rebase<br>
&nbsp; &nbsp; ⭐ &nbsp; &nbsp; Gain experience using continuous integration tools to build and automate the deployment of features<br>
&nbsp; &nbsp; ⭐ &nbsp; &nbsp; Build applications that execute in development, test, CI, and production environments<br>
&nbsp; &nbsp; ⭐ &nbsp; &nbsp; Focus on communication between front-end and back-end teams in order to complete and deploy features that have been outlined by the project spec<br>

<div align="center">

## Database Schema

<img src="https://user-images.githubusercontent.com/78382113/145473210-db903941-447e-4136-a2c9-626d2c93ed0f.png">

</div>


## API Endpoints

<div align="left">

* POST to `/api/v1/games`
  - accepts the following body:
  ```
  "body": {
    {
      "player_name": "name",
      "time_lapsed": "time",
      "moves_taken": "num of moves",
      "hidden_items_found": "num of items"
    }
  }
  ```
  - returns the following body:
  ```
  {
    "player_name": "name",
    "score": "score"
  }
  ```
* GET to `/api/v1/leaderboard`
 - returns the following body:
 ```
   {
    "games": [
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      },
      {
        "player_name": "name",
        "score": "score"
      }
    ]
  }
 ```
 </div>

## Acknowledgements

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/pewpewpewturing/back-end.svg?style=flat-square
[contributors-url]: https://github.com/pewpewpewturing/back-end/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/pewpewpewturing/back-end.svg?style=flat-square
[forks-url]: https://github.com/pewpewpewturing/back-end/network/members
[stars-shield]: https://img.shields.io/github/stars/pewpewpewturing/back-end.svg?style=flat-square
[stars-url]: https://github.com/pewpewpewturing/back-end/stargazers
[issues-shield]: https://img.shields.io/github/issues/pewpewpewturing/back-end.svg?style=flat-square
[issues-url]: https://github.com/pewpewpewturing/back-end/issues
[build-badge]: https://img.shields.io/circleci/build/gh/pewpewpewturing/back-end?style=flat-square
