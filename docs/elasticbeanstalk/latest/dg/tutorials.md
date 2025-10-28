# Tutorials and samples

Language and framework specific tutorials are spread throughout the AWS Elastic Beanstalk Developer Guide. New and updated tutorials are added to this list as they
are published. The most recent updates are shown first.

These tutorials are targeted at intermediate users and may not contain instructions for basic steps such as signing up for AWS. If this is your first
time using AWS or Elastic Beanstalk, check out the [Getting Started walkthrough](GettingStarted.md "GettingStarted.md") to get your first Elastic Beanstalk environment up and
running.

- **Ruby on Rails** - [Deploying a rails application to Elastic Beanstalk](ruby-rails-tutorial.md "ruby-rails-tutorial.md")
- **Ruby and Sinatra** - [Deploying a sinatra application to Elastic Beanstalk](ruby-sinatra-tutorial.md "ruby-sinatra-tutorial.md")
- **PHP and MySQL HA Configuration** - [Deploying a high-availability PHP application with an external Amazon RDS database to Elastic Beanstalk](php-ha-tutorial.md "php-ha-tutorial.md")
- **PHP and Laravel** - [Deploying a Laravel application to Elastic Beanstalk](php-laravel-tutorial.md "php-laravel-tutorial.md")
- **PHP and CakePHP** - [Deploying a CakePHP application to Elastic Beanstalk](php-cakephp-tutorial.md "php-cakephp-tutorial.md")
- **PHP and Drupal HA Configuration** - [Deploying a high-availability Drupal website with an external Amazon RDS database to Elastic Beanstalk](php-hadrupal-tutorial.md "php-hadrupal-tutorial.md")
- **PHP and WordPress HA Configuration** - [Deploying a high-availability WordPress website with an external Amazon RDS database to Elastic Beanstalk](php-hawordpress-tutorial.md "php-hawordpress-tutorial.md")
- **Node.js with DynamoDB HA Configuration** - [Deploying a Node.js application with DynamoDB to Elastic Beanstalk](nodejs-dynamodb-tutorial.md "nodejs-dynamodb-tutorial.md")
- **ASP.NET Core** - [QuickStart: Deploy an ASP.NET application to Elastic Beanstalk](aspnet-quickstart.md "aspnet-quickstart.md")
- **Python and Flask** - [Deploying a Flask application to Elastic Beanstalk](create-deploy-python-flask.md "create-deploy-python-flask.md")
- **Python and Django** - [Deploying a Django application to Elastic Beanstalk](create-deploy-python-django.md "create-deploy-python-django.md")
- **Node.js and Express** - [Deploying a Node.js Express application to Elastic Beanstalk](create_deploy_nodejs_express.md "create_deploy_nodejs_express.md")
- **Docker, PHP and nginx** - [Creating an ECS managed Docker environment with the Elastic Beanstalk console](create_deploy_docker_ecstutorial.md "create_deploy_docker_ecstutorial.md")
  You can download the sample applications used by Elastic Beanstalk when you create an environment without providing a source bundle with the following links:

- **Docker** – [docker.zip](samples/docker.md "samples/docker.md")
- **Multicontainer Docker** – [docker-multicontainer-v2.zip](samples/docker-multicontainer-v2.md "samples/docker-multicontainer-v2.md")
- **Preconfigured Docker (Glassfish)** – [docker-glassfish-v1.zip](samples/docker-glassfish-v1.md "samples/docker-glassfish-v1.md")
- **Go** – [go.zip](samples/go.md "samples/go.md")
- **Corretto** – [corretto.zip](samples/corretto.md "samples/corretto.md")
- **Tomcat** – [tomcat.zip](samples/tomcat.md "samples/tomcat.md")
- **.NET Core on Linux** – [dotnet-core-linux.zip](samples/dotnet-core-linux.md "samples/dotnet-core-linux.md")
- **.NET Core** – [dotnet-asp-windows.zip](samples/dotnet-asp-windows.md "samples/dotnet-asp-windows.md")
- **Node.js** – [nodejs.zip](samples/nodejs.md "samples/nodejs.md")
- **PHP** – [php.zip](samples/php.md "samples/php.md")
- **Python** – [python.zip](samples/python.md "samples/python.md")
- **Ruby** – [ruby.zip](samples/ruby.md "samples/ruby.md")
  More involved sample applications that show the use of additional web frameworks, libraries and tools are available as open source projects on
  GitHub:

- **[Load-balanced WordPress](https://github.com/awslabs/eb-php-wordpress "https://github.com/awslabs/eb-php-wordpress")** ([tutorial](php-hawordpress-tutorial.md "php-hawordpress-tutorial.md")) – Configuration files for installing WordPress securely and running it in a load-balanced
  Elastic Beanstalk environment.
- **[Load-balanced Drupal](https://github.com/awslabs/eb-php-drupal "https://github.com/awslabs/eb-php-drupal")** ([tutorial](php-hadrupal-tutorial.md "php-hadrupal-tutorial.md")) – Configuration files and instructions for installing Drupal securely and running it in a
  load-balanced Elastic Beanstalk environment.
- **[Scorekeep](https://github.com/awslabs/eb-java-scorekeep "https://github.com/awslabs/eb-java-scorekeep")** - RESTful web API that uses the Spring
  framework and the AWS SDK for Java to provide an interface for creating and managing users, sessions, and games. The API is bundled with an Angular 1.5 web
  app that consumes the API over HTTP. Includes branches that show integration with Amazon Cognito, AWS X-Ray, and Amazon Relational Database Service.

The application uses features of the Java SE platform to download dependencies and build on-instance, minimizing the size of the souce bundle. The
application also includes nginx configuration files that override the default configuration to serve the frontend web app statically on port 80 through
the proxy, and route requests to paths under `/api` to the API running on `localhost:5000`.

- **[Does it Have Snakes?](https://github.com/awslabs/eb-tomcat-snakes "https://github.com/awslabs/eb-tomcat-snakes")** - Tomcat application that
  shows the use of RDS in a Java EE web application in Elastic Beanstalk. The project shows the use of Servlets, JSPs, Simple Tag Support, Tag Files,
  JDBC, SQL, Log4J, Bootstrap, Jackson, and Elastic Beanstalk configuration files.
- **[Locust Load Generator](https://github.com/awslabs/eb-locustio-sample "https://github.com/awslabs/eb-locustio-sample")** - This project shows the
  use of Java SE platform features to install and run [Locust](http://locust.io/ "http://locust.io/"), a load generating tool written in Python. The project
  includes configuration files that install and configure Locust, a build script that configures a DynamoDB table, and a Procfile that runs Locust.
- **[Share Your Thoughts](https://github.com/awslabs/eb-demo-php-simple-app "https://github.com/awslabs/eb-demo-php-simple-app")** ([tutorial](php-ha-tutorial.md "php-ha-tutorial.md")) - PHP application that shows the use of MySQL on Amazon RDS, Composer, and configuration files.
- **[A New Startup](https://github.com/awslabs/eb-node-express-sample "https://github.com/awslabs/eb-node-express-sample")** ([tutorial](nodejs-dynamodb-tutorial.md "nodejs-dynamodb-tutorial.md")) - Node.js sample application that shows the use of DynamoDB, the AWS SDK for JavaScript in Node.js, npm package management,
  and configuration files.
