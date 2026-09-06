

# QuickStart: Deploy a Node.js application to Elastic Beanstalk
<a name="nodejs-quickstart"></a>

This QuickStart tutorial walks you through the process of creating a Node.js application and deploying it to an AWS Elastic Beanstalk environment.

**Not for production use**  
Examples are intended for demonstration only. Do not use example applications in production.

**Topics**
+ [Your AWS account](#nodejs-quickstart-aws-account)
+ [Prerequisites](#nodejs-quickstart-prereq)
+ [Step 1: Create a Node.js application](#nodejs-quickstart-create-app)
+ [Step 2: Run your application locally](#nodejs-quickstart-run-local)
+ [Step 3: Deploy your Node.js application with the EB CLI](#nodejs-quickstart-deploy)
+ [Step 4: Run your application on Elastic Beanstalk](#nodejs-quickstart-run-eb-ap)
+ [Step 5: Clean up](#go-tutorial-cleanup)
+ [AWS resources for your application](#nodejs-quickstart-eb-resources)
+ [Next steps](#nodejs-quickstart-next-steps)
+ [Deploy with the Elastic Beanstalk console](#nodejs-quickstart-console)

## Your AWS account
<a name="nodejs-quickstart-aws-account"></a>

If you're not already an AWS customer, you need to create an AWS account. Signing up enables you to access Elastic Beanstalk and other AWS services that you need.

If you already have an AWS account, you can move on to [Prerequisites](#nodejs-quickstart-prereq).

### Create an AWS account
<a name="nodejs-quickstart-aws-account-procedure"></a>

#### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="nodejs-quickstart-prereq"></a>

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in listings preceded by a prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ this is a command
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.

### EB CLI
<a name="nodejs-quickstart-prereq.ebcli"></a>

This tutorial uses the Elastic Beanstalk Command Line Interface (EB CLI). For details on installing and configuring the EB CLI, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install) and [Configure the EB CLI](eb-cli3-configuration.md).

### Node.js
<a name="nodejs-quickstart-prereq.runtime"></a>

Install Node.js on your local machine by following [How to install Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs) on the Node.js website. 

Verify your Node.js installation by running the following command.

```
~$ node -v
```

## Step 1: Create a Node.js application
<a name="nodejs-quickstart-create-app"></a>

Create a project directory.

```
~$ mkdir eb-nodejs
~$ cd eb-nodejs
```

Next, create an application that you'll deploy using Elastic Beanstalk. We'll create a "Hello World" RESTful web service.

**Example `~/eb-nodejs/server.js`**  

```
const http = require('node:http');

const hostname = '127.0.0.1';
const port = 8080;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Elastic Beanstalk!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

This application opens a listener on port 8080. Elastic Beanstalk forwards requests to your application on port 8080 by default for Node.js.

## Step 2: Run your application locally
<a name="nodejs-quickstart-run-local"></a>

Run the following command to run your application locally.

```
~/eb-nodejs$ node server.js
```

You should see the following text.

```
Server running at http://127.0.0.1:8080/
```

Enter the URL address `http://127.0.0.1:8080/` in your web browser. The browser should display “Hello Elastic Beanstalk\!”.

## Step 3: Deploy your Node.js application with the EB CLI
<a name="nodejs-quickstart-deploy"></a>

Run the following commands to create an Elastic Beanstalk environment for this application.

**To create an environment and deploy your Node.js application**

1. Initialize your EB CLI repository with the **eb init** command.

   ```
   ~/eb-nodejs$ eb init -p node.js nodejs-tutorial --region us-east-2
   ```

   This command creates an application named `nodejs-tutorial` and configures your local repository to create environments with the latest Node.js platform version.

1. (Optional) Run **eb init** again to configure a default key pair so that you can use SSH to connect to the EC2 instance running your application.

   ```
   ~/eb-nodejs$ eb init
   Do you want to set up SSH for your instances?
   (y/n): y
   Select a keypair.
   1) my-keypair
   2) [ Create new KeyPair ]
   ```

   Select a key pair if you have one already, or follow the prompts to create one. If you don't see the prompt or need to change your settings later, run **eb init -i**.

1. Create an environment and deploy your application to it with **eb create**. Elastic Beanstalk automatically builds a zip file for your application and deploys it to an EC2 instance in the environment. After deploying your application, Elastic Beanstalk starts it on port 8080.

   ```
   ~/eb-nodejs$ eb create nodejs-env
   ```

   It takes about five minutes for Elastic Beanstalk to create your environment.

## Step 4: Run your application on Elastic Beanstalk
<a name="nodejs-quickstart-run-eb-ap"></a>

When the process to create your environment completes, open your website with **eb open**.

```
~/eb-nodejs$ eb open
```

Congratulations\! You've deployed a Node.js application with Elastic Beanstalk\! This opens a browser window using the domain name created for your application.

## Step 5: Clean up
<a name="go-tutorial-cleanup"></a>

You can terminate your environment when you finish working with your application. Elastic Beanstalk terminates all AWS resources associated with your environment.

To terminate your Elastic Beanstalk environment with the EB CLI run the following command.

```
~/eb-nodejs$ eb terminate
```

## AWS resources for your application
<a name="nodejs-quickstart-eb-resources"></a>

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
<a name="nodejs-quickstart-next-steps"></a>

After you have an environment running an application, you can deploy a new version of the application or a different application at any time. Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. You can also explore your new environment using the Elastic Beanstalk console. For detailed steps, see [Explore your environment](GettingStarted.md#GettingStarted.Explore) in the *Getting started* chapter of this guide.

**Try more tutorials**  
If you'd like to try other tutorials with different example applications, see [More Elastic Beanstalk example applications and tutorials for Node.js](nodejs-getstarted.md).

After you deploy a sample application or two and are ready to start developing and running Node.js applications locally, see [Setting up your Node.js development environment for Elastic Beanstalk](nodejs-devenv.md).

## Deploy with the Elastic Beanstalk console
<a name="nodejs-quickstart-console"></a>

You can also use the Elastic Beanstalk console to launch the sample application. For detailed steps, see [Create an example application](GettingStarted.md#GettingStarted.CreateApp) in the *Getting started* chapter of this guide.