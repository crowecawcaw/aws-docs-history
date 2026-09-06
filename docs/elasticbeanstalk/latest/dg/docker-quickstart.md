

# QuickStart: Deploy a Docker application to Elastic Beanstalk
<a name="docker-quickstart"></a>

This QuickStart tutorial walks you through the process of creating a Docker application and deploying it to an AWS Elastic Beanstalk environment.

**Not for production use**  
Examples are intended for demonstration only. Do not use example applications in production.

**Topics**
+ [Your AWS account](#docker-quickstart-aws-account)
+ [Prerequisites](#docker-quickstart-prereq)
+ [Step 1: Create a Docker application and container](#docker-quickstart-create-app)
+ [Step 2: Run your application locally](#docker-quickstart-run-local)
+ [Step 3: Deploy your Docker application with the EB CLI](#docker-quickstart-deploy)
+ [Step 4: Run your application on Elastic Beanstalk](#docker-quickstart-run-eb-ap)
+ [Step 5: Clean up](#go-tutorial-cleanup)
+ [AWS resources for your application](#docker-quickstart-eb-resources)
+ [Next steps](#docker-quickstart-next-steps)
+ [Deploy with the Elastic Beanstalk console](#docker-quickstart-console)

## Your AWS account
<a name="docker-quickstart-aws-account"></a>

If you're not already an AWS customer, you need to create an AWS account. Signing up enables you to access Elastic Beanstalk and other AWS services that you need.

If you already have an AWS account, you can move on to [Prerequisites](#docker-quickstart-prereq).

### Create an AWS account
<a name="docker-quickstart-aws-account-procedure"></a>

#### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="docker-quickstart-prereq"></a>

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in listings preceded by a prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ this is a command
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.

### EB CLI
<a name="docker-quickstart-prereq.ebcli"></a>

This tutorial uses the Elastic Beanstalk Command Line Interface (EB CLI). For details on installing and configuring the EB CLI, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install) and [Configure the EB CLI](eb-cli3-configuration.md).

### Docker
<a name="docker-quickstart-prereq.runtime"></a>

To follow this tutorial, you'll need a working local installation of Docker. For more information, see [Get Docker](https://docs.docker.com/get-docker/) on the Docker documentation website.

Verify the Docker daemon is up an running by running the following command.

```
~$ docker info
```

## Step 1: Create a Docker application and container
<a name="docker-quickstart-create-app"></a>

For this example, we create a Docker image of the sample Flask application that's also referenced in [Deploying a Flask application to Elastic Beanstalk](create-deploy-python-flask.md).

The application consists of two files:
+ `app.py`— the Python file that contains the code that will execute in the container.
+ `Dockerfile`— the Dockerfile to build your image.

Place both files at the root of a directory.

```
~/eb-docker-flask/
|-- Dockerfile
|-- app.py
```

Add the following contents to your `Dockerfile`.

**Example `~/eb-docker-flask/Dockerfile`**  

```
FROM public.ecr.aws/docker/library/python:3.12
COPY . /app
WORKDIR /app
RUN pip install Flask==3.1.1
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

Add the following contents to your `app.py` file.

**Example `~/eb-docker-flask/app.py`**  

```
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello Elastic Beanstalk! This is a Docker application'
```

Use the [docker build](https://docs.docker.com/reference/cli/docker/image/build/) command to build your container image locally, tagging the image with `eb-docker-flask`. The period (`.`) at the end of the command specificies that path is a local directory.

```
~/eb-docker-flask$ docker build -t eb-docker-flask .
```

## Step 2: Run your application locally
<a name="docker-quickstart-run-local"></a>

Run your container with the [docker run](https://docs.docker.com/reference/cli/docker/container/run/) command. The command will print the ID of the running container. The **-d** option runs docker in background mode. The **-p** option exposes your application at port 5000. Elastic Beanstalk serves traffic to port 5000 on the Docker platform by default.

```
~/eb-docker-flask$ docker run -dp 127.0.0.1:5000:5000 eb-docker-flask
```

Navigate to `http://127.0.0.1:5000/ `in your browser. You should see the text "Hello Elastic Beanstalk\! This is a Docker application".

Run the [docker kill](https://docs.docker.com/reference/cli/docker/container/kill/) command to terminate the container.

```
~/eb-docker-flask$ docker kill {{container-id}}
```

## Step 3: Deploy your Docker application with the EB CLI
<a name="docker-quickstart-deploy"></a>

Run the following commands to create an Elastic Beanstalk environment for this application.

 

**To create an environment and deploy your Docker application**

1. Initialize your EB CLI repository with the **eb init** command.

   ```
   ~/eb-docker-flask$ eb init -p docker docker-tutorial --region {{us-east-2}}
   Application docker-tutorial has been created.
   ```

   This command creates an application named `docker-tutorial` and configures your local repository to create environments with the latest Docker platform version.

1. (Optional) Run **eb init** again to configure a default key pair so that you can use SSH to connect to the EC2 instance running your application.

   ```
   ~/eb-docker-flask$ eb init
   Do you want to set up SSH for your instances?
   (y/n): y
   Select a keypair.
   1) my-keypair
   2) [ Create new KeyPair ]
   ```

   Select a key pair if you have one already, or follow the prompts to create one. If you don't see the prompt or need to change your settings later, run **eb init -i**.

1. Create an environment and deploy your application to it with **eb create**. Elastic Beanstalk automatically builds a zip file for your application and starts it on port 5000.

   ```
   ~/eb-docker-flask$ eb create docker-tutorial
   ```

   It takes about five minutes for Elastic Beanstalk to create your environment.

## Step 4: Run your application on Elastic Beanstalk
<a name="docker-quickstart-run-eb-ap"></a>

When the process to create your environment completes, open your website with **eb open**.

```
~/eb-docker-flask$ eb open
```

Congratulations\! You've deployed a Docker application with Elastic Beanstalk\! This opens a browser window using the domain name created for your application.

## Step 5: Clean up
<a name="go-tutorial-cleanup"></a>

You can terminate your environment when you finish working with your application. Elastic Beanstalk terminates all AWS resources associated with your environment.

To terminate your Elastic Beanstalk environment with the EB CLI run the following command.

```
~/eb-docker-flask$ eb terminate
```

## AWS resources for your application
<a name="docker-quickstart-eb-resources"></a>

You just created a single instance application. It serves as a straightforward sample application with a single EC2 instance, so it doesn't require load balancing or auto scaling. For single instance applications Elastic Beanstalk creates the following AWS resources:
+ **EC2 instance** – An Amazon EC2 virtual machine configured to run web apps on the platform you choose.

  Each platform runs a different set of software, configuration files, and scripts to support a specific language version, framework, web container, or combination thereof. Most platforms use either Apache or nginx as a reverse proxy that processes web traffic in front of your web app, forwards requests to it, serves static assets, and generates access and error logs.
+ **Instance security group** – An Amazon EC2 security group configured to allow incoming traffic on port 80. This resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic is not allowed on other ports.
+ **Amazon S3 bucket** – A storage location for your source code, logs, and other artifacts that are created when you use Elastic Beanstalk.
+ **Amazon CloudWatch alarms** – Two CloudWatch alarms that monitor the load on the instances in your environment and are triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
+ **CloudFormation stack** – Elastic Beanstalk uses CloudFormation to launch the resources in your environment and propagate configuration changes. The resources are defined in a template that you can view in the [CloudFormation console](https://console.aws.amazon.com/cloudformation).
+  **Domain name** – A domain name that routes to your web app in the form *{{subdomain}}.{{region}}.elasticbeanstalk.com*. 

Elastic Beanstalk manages all of these resources. When you terminate your environment, Elastic Beanstalk terminates all the resources that it contains.

## Next steps
<a name="docker-quickstart-next-steps"></a>

After you have an environment running an application, you can deploy a new version of the application or a different application at any time. Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. You can also explore your new environment using the Elastic Beanstalk console. For detailed steps, see [Explore your environment](GettingStarted.md#GettingStarted.Explore) in the *Getting started* chapter of this guide.

After you deploy a sample application or two and are ready to start developing and running Docker applications locally, see [Preparing your Docker image for deployment to Elastic Beanstalk](single-container-docker-configuration.md). 

## Deploy with the Elastic Beanstalk console
<a name="docker-quickstart-console"></a>

You can also use the Elastic Beanstalk console to launch the sample application. For detailed steps, see [Create an example application](GettingStarted.md#GettingStarted.CreateApp) in the *Getting started* chapter of this guide.