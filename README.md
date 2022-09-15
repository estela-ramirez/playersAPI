<!-- Table of Contents -->
# Table of Contents
- [About the Project](#star2-about-the-project)
  * [Postman Testing](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Methods](#chart_with_upwards_trend-analytics)
  * [Run Locally](#running-run-locally)
  * [Run Unit Tests](#running-tests)
- [Acknowledgements](#raised_hands-acknowledgements)


<!-- About the Project -->
## :star2: About the Project
<p>This REST API allows access to the data in the players.csv file. </p>

* [Dataset](https://www.kaggle.com/datasets/haydenvenable/zillow-observed-rent-index-jan-2014-june-2021)

<!-- Postman Testing -->
### :camera: Screenshots


<!-- TechStack -->
### :space_invader: Tech Stack

<details>
   <summary>Web Server</summary>
     <li><a href="https://flask.palletsprojects.com/en/2.2.x/">Flask</a></li>
</details>

<details>
 <summary>DevOps</summary>
   <ul>
     <li><a href="https://www.docker.com/">Docker</a></li>
   </ul>
</details>

<!-- Methods -->
   
open endpoints require no Authentication.

* [get dictionary of players](players.md) : `GET /api/players/`
* [get player json object](playerID.md) : `GET /api/players/<playerID>`
* [increment player weight by 1](weight.md) : `PUT /api/players/<playerID>/weight`
* [increment player height by 1](height.md) : `PUT /api/players/<playerID>/height`

<!-- Run Locally -->
### :running: Run Locally
Clone the project

```bash
  git clone https://github.com/estela-ramirez/microservice.git
```

<!-- Run Unit Tests -->
### :running: Run Unit Tests 

<!-- Acknowledgments -->
## :raised_hands: Acknowledgements
 - [Flask API + Postman Tutorial](https://www.youtube.com/watch?v=fJz3JTEtJJA)
 
