# addresses-backend

Multi tenant web application that combines both backend and frontend.

On the backend part uses the django_tenants package to support multi-tenancy. The apps in this project are as follows:
* addresses: Manages the templates of the project, the general settings and the url routing.
* addresses_tenant: Manages the information exclusive to each tenant, not the information shared by all.
* client: Manages the clients for each of the tenants/schemas.

On the front end part, uses templates to manage the views. Also uses Google Maps.

# CI/CD

CD is not complete, I could only configure the deployment up to uploading to ECR.

The rest was uploaded manually.

# Possible improvements

The Templates can be improved further, the same as the workflow. For example, the workflow is using secrets when environment variables could have been used. They are also incomplete, so that is an obvious improvement. And there are security vulnerabilities that haven't been addressed for a fast development.

I'm also not very familiarized with django, so I'm pretty sure there are a lot of different ways the code can improve that I'm not aware of.

However, one error I know I made for sure was putting the DB connection details inside the settings.py. I didn't have the time to fix it as I wanted to as I couldn't get to finish the CI/CD for the project.

Another evident improvement is separating the frontend and the backend. It would allow us to use the best tool for the job, instead of trying to solve everything with django. It would also enhance the escalability of the app, because the backend and the frontend could scale independently based on each's needs.

# How to Run

Simply build and run the Dockerfile exposing the port 8000, it can be done the following way:

docker build -t addresses-web-app .
docker run --name demo-run -p 8000:8000 addresses-web-app