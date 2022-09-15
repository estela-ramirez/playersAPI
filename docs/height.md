# Increment Height by 1

**URL** : `/api/players/<playerID>/height`

**Method** : `PUT`

**Auth required** : NO

## Success Response

**Code** : `200 OK`

**Content example**

For a player with playerID aardsda01 who started off with height 75 gets updated to 

```json
{
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
  "height": 76, 
  "nameFirst": "David", 
  "nameGiven": "David Allan", 
  "nameLast": "Aardsma", 
  "playerID": "aardsda01", 
  "retroID": "aardd001", 
  "throws": "R", 
  "weight": 215
}
```
## Error Response

**Condition** : playerID does not exist in DB

**Code** : `404`

**Content** : `{}`