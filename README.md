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