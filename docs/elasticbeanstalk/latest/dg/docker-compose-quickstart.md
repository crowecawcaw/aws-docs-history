

# QuickStart: Deploy a Docker Compose application to Elastic Beanstalk
<a name="docker-compose-quickstart"></a>

This QuickStart tutorial walks you through the process of creating a multi-container Docker Compose application and deploying it to an AWS Elastic Beanstalk environment. You'll create a Flask web application with an nginx reverse proxy to demonstrate how Docker Compose simplifies orchestrating multiple containers.

**Not for production use**  
Examples are intended for demonstration only. Do not use example applications in production.

**Topics**
+ [Your AWS account](#docker-compose-quickstart-aws-account)
+ [Prerequisites](#docker-compose-quickstart-prereq)
+ [Step 1: Create a Docker Compose application](#docker-compose-quickstart-create-app)
+ [Step 2: Run your application locally](#docker-compose-quickstart-run-local)
+ [Step 3: Deploy your Docker Compose application with the EB CLI](#docker-compose-quickstart-deploy)
+ [Step 4: Test your application on Elastic Beanstalk](#docker-compose-quickstart-run-eb-ap)
+ [Step 5: Clean up](#docker-compose-quickstart-cleanup)
+ [AWS resources for your application](#docker-compose-quickstart-eb-resources)
+ [Next steps](#docker-compose-quickstart-next-steps)
+ [Deploy with the Elastic Beanstalk console](#docker-compose-quickstart-console)

## Your AWS account
<a name="docker-compose-quickstart-aws-account"></a>

If you're not already an AWS customer, you need to create an AWS account. Signing up enables you to access Elastic Beanstalk and other AWS services that you need.

If you already have an AWS account, you can move on to [Prerequisites](#docker-compose-quickstart-prereq).

### Create an AWS account
<a name="docker-compose-quickstart-aws-account-procedure"></a>

#### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="docker-compose-quickstart-prereq"></a>

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in listings preceded by a prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ this is a command
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.

### EB CLI
<a name="docker-compose-quickstart-prereq.ebcli"></a>

This tutorial uses the Elastic Beanstalk Command Line Interface (EB CLI). For details on installing and configuring the EB CLI, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install) and [Configure the EB CLI](eb-cli3-configuration.md).

### Docker and Docker Compose
<a name="docker-compose-quickstart-prereq.runtime"></a>

To follow this tutorial, you'll need a working local installation of Docker and Docker Compose. For more information, see [Get Docker](https://docs.docker.com/get-docker/) and [Install Docker Compose](https://docs.docker.com/compose/install/) on the Docker documentation website.

Verify that Docker and Docker Compose are installed and running by running the following commands.

```
~$ docker info
~$ docker compose version
```

## Step 1: Create a Docker Compose application
<a name="docker-compose-quickstart-create-app"></a>

For this example, we create a multi-container application using Docker Compose that consists of a Flask web application and an nginx reverse proxy. This demonstrates how Docker Compose simplifies orchestrating multiple containers that work together.

The application includes health monitoring configuration that allows Elastic Beanstalk to collect detailed application metrics from your nginx proxy.

The application consists of the following structure:

```
~/eb-docker-compose-flask/
|-- docker-compose.yml
|-- web/
|   |-- Dockerfile
|   |-- app.py
|   `-- requirements.txt
|-- proxy/
|   |-- Dockerfile
|   `-- nginx.conf
`-- .platform/
    `-- hooks/
        `-- postdeploy/
            `-- 01_setup_healthd_permissions.sh
```

Create the directory structure and add the following files:

First, create the main `docker-compose.yml` file that defines the services and their relationships.

**Example `~/eb-docker-compose-flask/docker-compose.yml`**  

```
services:
  web:
    build: ./web
    expose:
      - "5000"

  nginx-proxy:
    build: ./proxy
    ports:
      - "80:80"
    volumes:
      - "/var/log/nginx:/var/log/nginx"
    depends_on:
      - web
```

Create the Flask web application in the `web` directory. Add the following contents to your `app.py` file.

**Example `~/eb-docker-compose-flask/web/app.py`**  

```
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello Elastic Beanstalk! This is a Docker Compose application'
```

Add the following contents to your web service `Dockerfile`.

**Example `~/eb-docker-compose-flask/web/Dockerfile`**  

```
FROM public.ecr.aws/docker/library/python:3.12
COPY . /app
WORKDIR /app
RUN pip install Flask==3.1.1
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

Create the nginx reverse proxy in the `proxy` directory. Add the following contents to your `nginx.conf` file.

This configuration includes health monitoring setup that allows Elastic Beanstalk to collect detailed application metrics. For more information about customizing health monitoring log formats, see [Enhanced health log format](health-enhanced-serverlogs.md).

**Example `~/eb-docker-compose-flask/proxy/nginx.conf`**  

```
events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    map $http_upgrade $connection_upgrade {
        default       "upgrade";
    }

    # Health monitoring log format for Elastic Beanstalk
    log_format healthd '$msec"$uri"$status"$request_time"$upstream_response_time"$http_x_forwarded_for';
    
    upstream flask_app {
        server web:5000;
    }

    server {
        listen 80 default_server;
        root /usr/share/nginx/html;

        # Standard access log
        access_log /var/log/nginx/access.log;
        
        # Health monitoring log for Elastic Beanstalk
        if ($time_iso8601 ~ "^(\d{4})-(\d{2})-(\d{2})T(\d{2})") {
            set $year $1;
            set $month $2;
            set $day $3;
            set $hour $4;
        }
        access_log /var/log/nginx/healthd/application.log.$year-$month-$day-$hour healthd;
        
        location / {
            proxy_pass http://flask_app;
            proxy_http_version    1.1;

            proxy_set_header    Connection             $connection_upgrade;
            proxy_set_header    Upgrade                $http_upgrade;
            proxy_set_header    Host                   $host;
            proxy_set_header    X-Real-IP              $remote_addr;
            proxy_set_header    X-Forwarded-For        $proxy_add_x_forwarded_for;
        }
    }
}
```

Add the following contents to your proxy service `Dockerfile`.

**Example `~/eb-docker-compose-flask/proxy/Dockerfile`**  

```
FROM public.ecr.aws/nginx/nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
```

Finally, create a platform hook script to set up the necessary log directories and permissions for health monitoring. Platform hooks allow you to run custom scripts during the deployment process. For more information about platform hooks, see [Platform hooks](platforms-linux-extend.hooks.md).

**Example `~/eb-docker-compose-flask/.platform/hooks/postdeploy/01_setup_healthd_permissions.sh`**  

```
#!/bin/bash
set -ex

NGINX_CONTAINER=$(docker ps --filter "name=nginx-proxy" -q)

if [ -z "$NGINX_CONTAINER" ]; then
    echo "Error: No nginx-proxy container found running"
    exit 1
fi

NGINX_UID=$(docker exec ${NGINX_CONTAINER} id -u nginx)
NGINX_GID=$(docker exec ${NGINX_CONTAINER} id -g nginx)

mkdir -p /var/log/nginx/healthd
chown -R ${NGINX_UID}:${NGINX_GID} /var/log/nginx
```

## Step 2: Run your application locally
<a name="docker-compose-quickstart-run-local"></a>

Use the [docker compose up](https://docs.docker.com/compose/reference/up/) command to build and run your multi-container application locally. Docker Compose will build both container images and start the services defined in your `docker-compose.yml` file.

```
~/eb-docker-compose-flask$ docker compose up --build
```

The **--build** option ensures that Docker Compose builds the container images before starting the services. You should see output showing both the web service and nginx-proxy service starting up.

Navigate to `http://localhost` in your browser. You should see the text "Hello Elastic Beanstalk\! This is a Docker Compose application". The nginx proxy receives your request on port 80 and forwards it to the Flask application running on port 5000.

When you're finished testing, stop the application by pressing **Ctrl\+C** in the terminal, or run the following command in a separate terminal:

```
~/eb-docker-compose-flask$ docker compose down
```

## Step 3: Deploy your Docker Compose application with the EB CLI
<a name="docker-compose-quickstart-deploy"></a>

Run the following commands to create an Elastic Beanstalk environment for this application.

 

**To create an environment and deploy your Docker Compose application**

1. Initialize your EB CLI repository with the **eb init** command.

   ```
   ~/eb-docker-compose-flask$ eb init -p docker docker-compose-tutorial --region {{us-east-2}}
   Application docker-compose-tutorial has been created.
   ```

   This command creates an application named `docker-compose-tutorial` and configures your local repository to create environments with the latest Docker platform version.

1. (Optional) Run **eb init** again to configure a default key pair so that you can use SSH to connect to the EC2 instance running your application.

   ```
   ~/eb-docker-compose-flask$ eb init
   Do you want to set up SSH for your instances?
   (y/n): y
   Select a keypair.
   1) my-keypair
   2) [ Create new KeyPair ]
   ```

   Select a key pair if you have one already, or follow the prompts to create one. If you don't see the prompt or need to change your settings later, run **eb init -i**.

1. Create an environment and deploy your application to it with **eb create**. Elastic Beanstalk automatically detects your `docker-compose.yml` file and deploys your multi-container application.

   ```
   ~/eb-docker-compose-flask$ eb create docker-compose-tutorial
   ```

   It takes about five minutes for Elastic Beanstalk to create your environment and deploy your multi-container application.

## Step 4: Test your application on Elastic Beanstalk
<a name="docker-compose-quickstart-run-eb-ap"></a>

When the process to create your environment completes, open your website with **eb open**.

```
~/eb-docker-compose-flask$ eb open
```

Great\! You've deployed a multi-container Docker Compose application with Elastic Beanstalk\! This opens a browser window using the domain name created for your application. You should see the message from your Flask application, served through the nginx reverse proxy.

## Step 5: Clean up
<a name="docker-compose-quickstart-cleanup"></a>

You can terminate your environment when you finish working with your application. Elastic Beanstalk terminates all AWS resources associated with your environment.

To terminate your Elastic Beanstalk environment with the EB CLI run the following command.

```
~/eb-docker-compose-flask$ eb terminate
```

## AWS resources for your application
<a name="docker-compose-quickstart-eb-resources"></a>

You just created a single instance application running multiple containers. It serves as a straightforward sample application with a single EC2 instance, so it doesn't require load balancing or auto scaling. For single instance applications Elastic Beanstalk creates the following AWS resources:
+ **EC2 instance** – An Amazon EC2 virtual machine configured to run web apps on the platform you choose.

  Each platform runs a different set of software, configuration files, and scripts to support a specific language version, framework, web container, or combination thereof. Most platforms use either Apache or nginx as a reverse proxy that processes web traffic in front of your web app, forwards requests to it, serves static assets, and generates access and error logs.
+ **Instance security group** – An Amazon EC2 security group configured to allow incoming traffic on port 80. This resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic is not allowed on other ports.
+ **Amazon S3 bucket** – A storage location for your source code, logs, and other artifacts that are created when you use Elastic Beanstalk.
+ **Amazon CloudWatch alarms** – Two CloudWatch alarms that monitor the load on the instances in your environment and are triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
+ **CloudFormation stack** – Elastic Beanstalk uses CloudFormation to launch the resources in your environment and propagate configuration changes. The resources are defined in a template that you can view in the [CloudFormation console](https://console.aws.amazon.com/cloudformation).
+  **Domain name** – A domain name that routes to your web app in the form *{{subdomain}}.{{region}}.elasticbeanstalk.com*. 

Elastic Beanstalk manages all of these resources. When you terminate your environment, Elastic Beanstalk terminates all the resources that it contains. Your Docker Compose application runs multiple containers on the single EC2 instance, with Elastic Beanstalk handling the orchestration automatically.

## Next steps
<a name="docker-compose-quickstart-next-steps"></a>

After you have an environment running an application, you can deploy a new version of the application or a different application at any time. Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. You can also explore your new environment using the Elastic Beanstalk console. For detailed steps, see [Explore your environment](GettingStarted.md#GettingStarted.Explore) in the *Getting started* chapter of this guide.

After you deploy a sample application or two and are ready to start developing and running Docker Compose applications locally, see [Preparing your Docker image for deployment to Elastic Beanstalk](single-container-docker-configuration.md). 

## Deploy with the Elastic Beanstalk console
<a name="docker-compose-quickstart-console"></a>

You can also use the Elastic Beanstalk console to launch a Docker Compose application. Create a ZIP file containing your `docker-compose.yml` file and all associated directories and files, then upload it when creating a new application. For detailed steps, see [Create an example application](GettingStarted.md#GettingStarted.CreateApp) in the *Getting started* chapter of this guide.