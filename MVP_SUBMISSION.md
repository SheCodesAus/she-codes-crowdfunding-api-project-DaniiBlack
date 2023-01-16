### MVP Plan Submission
> Please submit the following:
- [x] The title of your website.
  - Jolt
- [x] A paragraph detailing the purpose and target audience for your website.
  - Support local and international initiatives run by activists. A lot of people aren't able to make it to a riot or through med school to join doctors without borders, and we all know the housing market is fvcked meaning we aren't easily able to take those in need into our homes. Through Jolt, you are able to contribute, with full transparency of where every dollar goes. You can support activist magasines, buy gear for rioters or donate money to verified charities, activist groups and social organisations.
- [x] The features your MVP will include.
  1. Title
  2. Owner (a user)
  3. Supporter (user)
  4. Description
  5. Image
  6. Target amount to fundraise
  7. Whether it is currently open to accepting new supporters or not
  8. When the project was created
  9. Ability to “pledge” to a project
     1. An amount
     2. The project the pledge is for
     3. The supporter/user (i.e. who created the pledge)
     4. Whether the pledge is anonymous or not
     5. A comment to go along with the pledge
  10. flexible update/delete functionality
  11. we take care of all permissions
  12. return the relevant status codes for both successful and unsuccessful requests to the API
  13. helpful error messaging
  14. token Authentication
  15. responsive design
- [x] At least 3 additional features you would like to include if you reach your MVP
1. ability to opt for purchasing an item/items, or for donation of money towards a project
2. ability to search by category
3. a blog page for users who own projects and are actively fundraising for their cause, to also post content if they are artists/ writers/ journalists etc 
4. *tentive feature: live(ish) exchange rates for donating to international projects such as doctors without borders
- [x] An API specification.
  - **PLEDGE**
    - POST: /pledge, create pledge
    - PUT: ?
    - DELETE: pledge/pledgeid, delete a pledge (admin only)
    - GET: pledge/pledges, view all pledges. Can use media queries here also? Can a user view all pledges made through the site or only their own? Probably all, automatically set to annonymous. 
  - **PROJECT**
    - POST: /project/pledge, to pledge to project
    - PUT: project/projectid, edit project and place project on hold status (not currently acception new supporters)
    - DELETE: project/projectid, delete a project
    - GET: project/projects, view all (potentially could use a query param here project/projects?queryParamGoesHere for viewing all by category)
  - **USER**
    - POST: create user
    - PUT: user/userid(pk), edit user
    - DELETE: delete user
    - GET: return user's information (id, email address, name etc)
- [x] A database schema.
  - **PLEDGE**
    - total/ goal
    - amount currently at
    - project the pledge is for
    - the supporter/ user who created the pledge
    - annonymous or not
  - **PROJECT**
    - id
    - title
    - owner
    - description
    - image
    - target amount
    - creation date
    - currently accepting new supporters (y/n boolean, probably)
  - **USER**
    - id
    - username
    - email address
    - password
    - profile picture
- [] Wireframes.
- [x] Colour Scheme. Black, white. Maybe accents of colour tbd.
- [x] Heading and body font(s). Helvetica

**TODO:** 
1. What fields per route for the API?
   - for example; POST: user fields = username, password, email address etc 
 - Wireframes, add images to an image file or sketch them up on excalidraw/ miro etc. 