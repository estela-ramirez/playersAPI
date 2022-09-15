# List of Players

**URL** : `/api/players/`

**Method** : `GET`

**Auth required** : NO

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "aardsda01": {
    "bats": "R", 
    "bbrefID": "aardsda01", 
    "birthCity": "Denver", 
    "birthCountry": "USA", 
    "birthDay": 27, 
    "birthMonth": 12, 
    "birthState": "CO", 
    "birthYear": 1981, 
    "deathCity": "", 
    "deathCountry": "", 
    "deathDay": "", 
    "deathMonth": "", 
    "deathState": "", 
    "deathYear": "", 
    "debut": "2004-04-06", 
    "finalGame": "2015-08-23", 
    "height": 75, 
    "nameFirst": "David", 
    "nameGiven": "David Allan", 
    "nameLast": "Aardsma", 
    "playerID": "aardsda01", 
    "retroID": "aardd001", 
    "throws": "R", 
    "weight": 215
  }
}
```

## Notes

if the playerID does not exist, returns an empty dictionary

```json
{}
````