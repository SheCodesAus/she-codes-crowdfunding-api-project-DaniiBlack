SHE{CODES}Plus
Danielle's crowdfunding project


## Project: Crowdfunding
### Project Description
> Kickstarter,GoFundMe,Kiva,Change.org,Patreon... All of these different websites have something in common: they provide a platform for people to fund projects thattheybelievein,buttheyallhaveaslightlydifferent approach. You are going to create your own crowdfunding website, and put your own spin on it!

### Project Requirements
Your crowdfunding project must:
- Be separated into two distinct projects: an API built using the Django Rest Framework and a website built using React.
- Have a cool name, bonus points if it includes a pun and/or missing vowels. Seehttps://namelix.com/1 for inspiration.
- Have a clear target audience.
- Have user accounts. A user should have at least the following attributes:
  - Username
  - Email address
  - Password
- Ability to create a “project” to be crowdfunded which will include at least the following attributes:
  - Title
  - Owner (a user)
  - Description
  - Image
  - Target amount to fundraise
  - Whether it is currently open to accepting new supporters or not
  - When the project was created
- Ability to “pledge” to a project. A pledge should include at least the following attributes:
  - An amount
  - The project the pledge is for
  - The supporter/user (i.e. who created the pledge)
  - Whether the pledge is anonymous or not
  - A comment to go along with the pledge
- Implement suitable update/delete functionality, e.g.should a project owner be allowed to update a project description?
- Implement suitable permissions, e.g. who is allowed to delete a pledge?
- Return the relevant status codes for both successful and unsuccessful requests to the API
- Handle failed requests gracefully (e.g.you should have a custom 404 page rather than the default error page).
- Use Token Authentication.
- Implement responsive design.
  
**Additional Notes**
No additional libraries or frameworks, other than what we use in class,are allowed unless approved by the Lead Mentor. 
  1. Bonus points are meaningless.

*Note that while this is a crowdfunding website, actual money transactions are out of scope for this project.*

### MVP Plan Submission
Please submit the following:▢The title of your website.▢A paragraph detailing the purpose and target audience for your website.▢The features your MVP will include.▢At least 3 additional features you would like to include if you reach your MVP.▢An API specification.▢A database schema.▢Wireframes.▢Colour Scheme.▢Heading and body font(s).Part A SubmissionPlease submit the following:▢A link to the GitHub repository containing the code for your project.▢A link to the deployed project.▢A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.▢A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.▢A screenshot of Insomnia, demonstrating a token being returned.▢Stepbystepinstructionsforhowtoregisteranewuserandcreateanewproject(i.e.endpointsandbody data).▢Your refined API specification and Database Schema.Part B SubmissionPlease submit the following:▢A link to the GitHub repository containing the code for your project.▢A link to the deployed project.▢A screenshot of the home page.▢A screenshot of the project creation form.▢A screenshot of a project with pledges.▢A screenshot of the resulting page when an unauthorized user attempts to edit a project.