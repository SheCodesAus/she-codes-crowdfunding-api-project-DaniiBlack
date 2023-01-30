Please submit the following: 
[x] A link to the Github repo containing the code for your project
    - https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-DaniiBlack
[x] A link to the deployed project
    - Admin: https://lively-dew-2150.fly.dev/admin/login/?next=/admin/
    - 
[x] A screenshot of insomnia, demonstrating a successful GET method for any endpoint
    - see images folder
[x] A screenshot of insomnia, demonstrating a successful POST method for any endpoint
    - see images folder
[x] A screenshot of insomnia, demonstrating a token being returned
[ ] Step by step instructions for how to register a new user and create a new project (ie. endpoints and body data)
[x] Your refined API specification and Database schema
#### Refined database schema
  **PLEDGE**
        - total/ goal | integer
        - project the pledge is for | relationship. Foreign Key
        - the supporter/ user who created the pledge | string
        - annonymous or not | boolean
    
  **PROJECT**
        - id | integer
        - title | string
        - owner | string
        - description | string
        - image | string
        - target amount | integer
        - creation date | date 
        - currently accepting new supporters | boolean

  **USER**
        - id | number
        - username | string
        - email address | string
        - password | string
        - profile picture | string

#### API specification

  **PLEDGE**
    - POST: </pledge>, create pledge
    - PUT: ?
    - DELETE: <pledge/pledgeid>, delete a pledge (admin only)
    - GET: <pledge/pledges>, view all pledges. Can use media queries here also? Can a user view all pledges made through the site or only their own? Probably all, automatically set to annonymous. 
  **PROJECT**
    - POST: </project/pledge>, to pledge to project
    - PUT: <project/projectid>, edit project and place project on hold status (not currently acception new supporters)
    - DELETE: <project/projectid>, delete a project
    - GET: <project/projects>, view all (potentially could use a query param here project/projects?queryParamGoesHere for viewing all by category)
  **USER**
    - POST: create user
    - PUT: <user/userid(pk)>, edit user
    - DELETE: delete user
    - GET: return user's information (id, email address, name etc)