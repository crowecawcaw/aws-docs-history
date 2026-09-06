

# QuickStart: Deploy a Python application to Elastic Beanstalk
<a name="python-quickstart"></a>

This QuickStart tutorial walks you through the process of creating a Python application and deploying it to an AWS Elastic Beanstalk environment.

**Not for production use**  
Examples are intended for demonstration only. Do not use example applications in production.

**Topics**
+ [Your AWS account](#python-quickstart-aws-account)
+ [Prerequisites](#python-quickstart-prereq)
+ [Step 1: Create a Python application](#python-quickstart-create-app)
+ [Step 2: Run your application locally](#python-quickstart-run-local)
+ [Step 3: Deploy your Python application with the EB CLI](#python-quickstart-deploy)
+ [Step 4: Run your application on Elastic Beanstalk](#python-quickstart-run-eb-ap)
+ [Step 5: Clean up](#go-tutorial-cleanup)
+ [AWS resources for your application](#python-quickstart-eb-resources)
+ [Next steps](#python-quickstart-next-steps)
+ [Deploy with the Elastic Beanstalk console](#python-quickstart-console)

## Your AWS account
<a name="python-quickstart-aws-account"></a>

If you're not already an AWS customer, you need to create an AWS account. Signing up enables you to access Elastic Beanstalk and other AWS services that you need.

If you already have an AWS account, you can move on to [Prerequisites](#python-quickstart-prereq).

### Create an AWS account
<a name="python-quickstart-aws-account-procedure"></a>

#### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="python-quickstart-prereq"></a>

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in listings preceded by a prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ this is a command
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.

### EB CLI
<a name="python-quickstart-prereq.ebcli"></a>

This tutorial uses the Elastic Beanstalk Command Line Interface (EB CLI). For details on installing and configuring the EB CLI, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install) and [Configure the EB CLI](eb-cli3-configuration.md).

### Python and Flask framework
<a name="python-quickstart-prereq.runtime"></a>

Confirm that you have a working Python version with `pip` installed by running the following commands.

```
~$ python3 --version
Python 3.N.N
>~$ python3 -m pip --version
pip X.Y.Z from ... (python 3.N.N)
```

If any of the previous commands return “*Python was not found*", run the following commands that use `python` instead of `python3`. The setup of aliases and symbolic links can vary by operating system and individual customizations, so the `python3` command may not function on your machine.

```
~$ python --version
Python 3.N.N
>~$ python -m pip --version
pip X.Y.Z from ... (python 3.N.N)
```

If you don't have Python installed on your local machine, you can download it from the [Python downloads](https://www.python.org/downloads/) page on the Python website. For a list of Python language versions supported by Elastic Beanstalk, see [Supported Python platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.python) in the *AWS Elastic Beanstalk Platforms* guide. The Python downloads website provides a link to the *Python Developer's Guide*, where you'll find installation and setup instructions.

**Note**  
The Python `pip` package is included by default with Python 3.4 or later.

If your output indicates that you have a supported version of Python, but not `pip`, see the [Installation](https://pip.pypa.io/en/stable/installation/) page on the *pip.pypa.io* website. It provides guidance to install pip within a Python environment that doesn’t have it.



Confirm if Flask is installed by running the following command:

```
~$ pip list | grep Flask
```

If Flask is not installed, you can install it with the following command:

```
~$ pip install Flask
```

## Step 1: Create a Python application
<a name="python-quickstart-create-app"></a>

Create a project directory.

```
~$ mkdir eb-python
~$ cd eb-python
```

Create a sample "Hello Elastic Beanstalk\!" Python application that you'll deploy using Elastic Beanstalk.

Create a text file named `application.py` in the directory you just created with the following contents.

**Example `~/eb-python/application.py`**  

```
from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_elastic_beanstalk():
        return 'Hello Elastic Beanstalk!'
```

Create a text file named `requirements.txt` with the following line. This file contains the required `pip` packages for the application to run.

**Example `~/eb-python/requirements.txt`**  

```
Flask
```

## Step 2: Run your application locally
<a name="python-quickstart-run-local"></a>

Run the following command to run your application locally.

```
~/eb-python$ export FLASK_APP=application.py && flask run --port 5000
```

You should see output similar to the following

```
Serving Flask app 'application.py'
Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [01/Jan/1970 00:00:00] "GET / HTTP/1.1" 200 -
```

Navigate to `http://localhost:5000` in your web browser. The web browser should display “Hello Elastic Beanstalk\!”.

## Step 3: Deploy your Python application with the EB CLI
<a name="python-quickstart-deploy"></a>

Run the following commands to create an Elastic Beanstalk environment for this application.

 

**To create an environment and deploy your Python application**

1. Initialize your EB CLI repository with the **eb init** command.

   ```
   ~/eb-python$ eb init -p python-3.9 python-tutorial --region {{us-east-2}}
   ```

   This command creates an application named `python-tutorial` and configures your local repository to create environments with the provided Python platform version.

1. (Optional) Run **eb init** again to configure a default key pair so that you can use SSH to connect to the EC2 instance running your application.

   ```
   ~/eb-python$ eb init
   Do you want to set up SSH for your instances?
   (y/n): y
   Select a keypair.
   1) my-keypair
   2) [ Create new KeyPair ]
   ```

   Select a key pair if you have one already, or follow the prompts to create one. If you don't see the prompt or need to change your settings later, run **eb init -i**.

1. Create an environment and deploy your application to it with **eb create**. Elastic Beanstalk automatically builds a zip file for your application and starts it on port 5000.

   ```
   ~/eb-python$ eb create python-env
   ```

   It takes about five minutes for Elastic Beanstalk to create your environment.

## Step 4: Run your application on Elastic Beanstalk
<a name="python-quickstart-run-eb-ap"></a>

When the process to create your environment completes, open your website with **eb open**.

```
~/eb-python$ eb open
```

Congratulations\! You've deployed a Python application with Elastic Beanstalk\! This opens a browser window using the domain name created for your application.

## Step 5: Clean up
<a name="go-tutorial-cleanup"></a>

You can terminate your environment when you finish working with your application. Elastic Beanstalk terminates all AWS resources associated with your environment.

To terminate your Elastic Beanstalk environment with the EB CLI run the following command.

```
~/eb-python$ eb terminate
```

## AWS resources for your application
<a name="python-quickstart-eb-resources"></a>

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
<a name="python-quickstart-next-steps"></a>

After you have an environment running an application, you can deploy a new version of the application or a different application at any time. Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. You can also explore your new environment using the Elastic Beanstalk console. For detailed steps, see [Explore your environment](GettingStarted.md#GettingStarted.Explore) in the *Getting started* chapter of this guide.

**Try more tutorials**  
If you'd like to try other tutorials with different example applications, see the following tutorials:  
[Deploying a Flask application to Elastic Beanstalk](create-deploy-python-flask.md)
[Deploying a Django application to Elastic Beanstalk](create-deploy-python-django.md)

After you deploy a sample application or two and are ready to start developing and running Python applications locally, see [Setting up your Python development environment for Elastic Beanstalk](python-development-environment.md). 

## Deploy with the Elastic Beanstalk console
<a name="python-quickstart-console"></a>

You can also use the Elastic Beanstalk console to launch the sample application. For detailed steps, see [Create an example application](GettingStarted.md#GettingStarted.CreateApp) in the *Getting started* chapter of this guide.