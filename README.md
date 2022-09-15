<!-- Table of Contents -->
# Table of Contents
- [About the Project](about-the-project)
  * [Tech Stack](#space_invader-tech-stack)
  * [Methods](#star2-methods)
  * [Run Locally](#running-run-locally)
  * [Run Unit Tests](#running_woman-tests)
- [Acknowledgements](#raised_hands-acknowledgements)


<!-- About the Project -->
## :star2: About the Project
<p>This REST API allows access to the data in the players.csv file. </p>

<!-- TechStack -->
### :space_invader: Tech Stack

<h4>Web Server</h4>
- <a href="https://flask.palletsprojects.com/en/2.2.x/">Flask</a>

  <h4>DevOps<h4>
- <a href="https://www.docker.com/">Docker</a>

<!-- Methods -->
### :star2: Methods


* [get list of players](/docs/players.md) : `GET /api/players/`
* [get player info](/docs/playerID.md) : `GET /api/players/<playerID>`
* [increment player weight by 1](/docs/weight.md) : `PUT /api/players/<playerID>/weight`
* [increment player height by 1](/docs/height.md) : `PUT /api/players/<playerID>/height`

<!-- Run Locally -->
### :running: Run Locally
Clone the project

```bash
  git clone https://github.com/estela-ramirez/microservice.git
```

<!-- Run Unit Tests -->
### :running_woman: Run Unit Tests 

Start API 
```bash
  python main.py
```
Run Unit Tests
```bash
  cd tests/
  python unit_test.py
```

<!-- Acknowledgments -->
## :raised_hands: Acknowledgements
 - [Flask API + Postman Tutorial](https://www.youtube.com/watch?v=fJz3JTEtJJA)
 
