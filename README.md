# myblog

This is a dockerised Django blog application, it features a content management system using django markdown which can be managed using the django admin interface.

It uses the following Docker images:

* Python Alpine
* Nginx-proxy server
* letsencrypt-nginx-proxy-companian 
* PostgreSQL (for development only, the production docker-compose.prod.yml assumes a system install of PostgreSQL)

To run the containers you will need to set up a .env.dev file in the project root, you can then use `docker-compose -f docker-compose.yml up --build -d`

Note - this is no longer use as my [current blog](https:joekbullard.xyz), django is great for many things, but after deploying this on my raspberry pi, I soon learnt there are much better (simpler) ways of building a blog than Django.

## Todo

TBC
