## Job Posting CRUD Platform 
### Python/Django - Html/TailwindCSS

A project that allows users to post and apply to jobs, edit jobs, and edit their company and user profiles.

This project was created over the course of one week. Development began with some whiteboarding on Figma - planning out the project was vital if I was going to complete it on time. 
!["Original Figma Brainstorm"](./static/images/1figma.png)
*As you can see, I was originally going to use React for the front end. I decided not to, to keep things simpler.*

Once I had the application planned out, I created the backend portion as specified.

After the backend was *mostly* done I began working on the front end. I decided to use Tailwind to style the UI to save time. 


!["Homepage"](./static/images/2homepage.png)
Here's the homepage. Fairly simple: Navbar, hero, search bar, and list of open positions.

!["Details"](./static/images/3jobdetails.png)
On the job details, you may read about the position and view the company that posted the job.

!["Applying"](./static/images/5apply.png)
At the bottom of the listing there are clickable tags to view other jobs with the same tag, and the *apply* button.

!["Applied"](./static/images/6apply.png)
Clicking the apply directs you to the success page after triggering the `send_mail()` function in the backend.

`send_mail()` Sends an alert email to the job poster, and a confirmation email to the applicant, shown below.

!["Employer email"](./static/images/email2.png)
Sent to employer/job poster...
!["Employee email"](./static/images/email1.png)
Sent to applicant.



!["Posting"](./static/images/7create.png)
Posting a job.


!["Employer Profile"](./static/images/8employerprofile.png)
The employer can view and edit their profile from this view. They may also view, edit, and delete their job postings.

!["Applicant Profile"](./static/images/employeeprofile.png)
The job applicant can view and edit their profile from this view. 

!["Search results"](./static/images/searchtags.png)
Here you can see the result of searching for "python".