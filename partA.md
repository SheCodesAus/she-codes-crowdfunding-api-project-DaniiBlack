Select a prisoner, donate towards their bail. 

 A database schema.
 
**PLEDGE**
[x] total/ goal | integer
~~[ ] amount currently at | integer~~ (count all current pledges each time)
[x] project the pledge is for | ~~string~~ relationship. Foreign Key
[x] the supporter/ user who created the pledge | string
[x] annonymous or not | boolean

**PROJECT**
[ ] id | integer
[ ] title | string
[ ] owner | string
[ ] description | string
[ ] image | string
[ ] target amount | integer
[ ] creation date | date (?)
[ ] currently accepting new supporters | boolean

**USER**
[ ] id | integer (or would an id be a number, actually?)
[ ] username | string
[ ] email address | string
[ ] password | string
[ ] profile picture | string

User flows
- view website without an account
- create account (log in, log out)
- create project (view project, check progress, add target amount, add description, cannot edit target amount or description without admin permissions(?))
- submit pledge/s


