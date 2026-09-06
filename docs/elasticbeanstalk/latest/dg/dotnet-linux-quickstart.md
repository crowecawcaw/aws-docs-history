

# QuickStart: Deploy a .NET Core on Linux application to Elastic Beanstalk
<a name="dotnet-linux-quickstart"></a>

This QuickStart tutorial walks you through the process of creating a .NET Core on Linux application and deploying it to an AWS Elastic Beanstalk environment.

**Not for production use**  
Examples are intended for demonstration only. Do not use example applications in production.

**Topics**
+ [Your AWS account](#dotnet-linux-quickstart-aws-account)
+ [Prerequisites](#dotnet-linux-quickstart-prereq)
+ [Step 1: Create a .NET Core on Linux application](#dotnet-linux-quickstart-create-app)
+ [Step 2: Run your application locally](#dotnet-linux-quickstart-run-local)
+ [Step 3: Deploy your .NET Core on Linux application with the EB CLI](#dotnet-linux-quickstart-deploy)
+ [Step 4: Run your application on Elastic Beanstalk](#dotnet-linux-quickstart-run-eb-ap)
+ [Step 5: Clean up](#go-tutorial-cleanup)
+ [AWS resources for your application](#dotnet-linux-quickstart-eb-resources)
+ [Next steps](#dotnet-linux-quickstart-next-steps)
+ [Deploy with the Elastic Beanstalk console](#dotnet-linux-quickstart-console)

## Your AWS account
<a name="dotnet-linux-quickstart-aws-account"></a>

If you're not already an AWS customer, you need to create an AWS account. Signing up enables you to access Elastic Beanstalk and other AWS services that you need.

If you already have an AWS account, you can move on to [Prerequisites](#dotnet-linux-quickstart-prereq).

### Create an AWS account
<a name="dotnet-linux-quickstart-aws-account-procedure"></a>

#### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="dotnet-linux-quickstart-prereq"></a>

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in listings preceded by a prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ this is a command
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.

### EB CLI
<a name="dotnet-linux-quickstart-prereq.ebcli"></a>

This tutorial uses the Elastic Beanstalk Command Line Interface (EB CLI). For details on installing and configuring the EB CLI, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install) and [Configure the EB CLI](eb-cli3-configuration.md).

### .NET Core on Linux
<a name="dotnet-linux-quickstart-prereq.runtime"></a>

If you don't have the .NET SDK installed on your local machine, you can install it by following the [Download .NET](https://dotnet.microsoft.com/en-us/download) link on the [.NET documentation](https://learn.microsoft.com/en-us/dotnet/) website.

Verify your .NET SDK installation by running the following command.

```
~$ dotnet --info
```

## Step 1: Create a .NET Core on Linux application
<a name="dotnet-linux-quickstart-create-app"></a>

Create a project directory.

```
~$ mkdir eb-dotnetcore
~$ cd eb-dotnetcore
```

Next, create a sample Hello World application by running the following commands.

```
~/eb-dotnetcore$ dotnet new web --name HelloElasticBeanstalk
~/eb-dotnetcore$ cd HelloElasticBeanstalk
```

## Step 2: Run your application locally
<a name="dotnet-linux-quickstart-run-local"></a>

Run the following command to run your application locally.

```
~/eb-dotnetcore/HelloElasticBeasntalk$ dotnet run
```

The output should look something like the following text.

```
Building...
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: https://localhost:7294
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5052
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
```

**Note**  
The `dotnet` command selects a port at random when running the application locally. In this example the port is 5052. When you deploy the application to your Elastic Beanstalk environment, the application will run on port 5000.

Enter the URL address `http://localhost:{{port}}` in your web browser. For this specific example, the command is `http://localhost:5052`. The web browser should display “Hello World\!”.

## Step 3: Deploy your .NET Core on Linux application with the EB CLI
<a name="dotnet-linux-quickstart-deploy"></a>

Run the following commands to create an Elastic Beanstalk environment for this application.

 

**To create an environment and deploy your .NET Core on Linux application**

1. Compile and publish your application to a folder for deployment to the Elastic Beanstalk environment you're about to create.

   ```
   ~$ cd eb-dotnetcore/HelloElasticBeanstalk
   ~/eb-dotnetcore/HelloElasticBeanstalk$ dotnet publish -o site
   ```

1. Navigate to the site directory where you just published your app.

   ```
   ~/eb-dotnetcore/HelloElasticBeanstalk$ cd site
   ```

1. Initialize your EB CLI repository with the **eb init** command.

   Be aware of the following details regarding the platform branch version that you specify in the command:
   + Replace `{{x.y.z}}` in the following command with the latest version of the platform branch *.NET 6 on AL2023*.
   + To locate the latest platform branch version see [.NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.dotnetlinux) *Supported platforms* in the *AWS Elastic Beanstalk Platforms* guide.
   + An example of a solution stack name that includes the version number is `64bit-amazon-linux-2023-v3.1.1-running-.net-6`. In this example the branch version is *3.1.1*.

   ```
   ~eb-dotnetcore/HelloElasticBeanstalk/site$ eb init -p 64bit-amazon-linux-2023-v{{x.y.z}}-running-.net-6 dotnetcore-tutorial --region us-east-2
   Application dotnetcore-tutorial has been created.
   ```

   This command creates an application named `dotnetcore-tutorial` and configures your local repository to create environments with the .NET Core on Linux platform version specified in the command.

1. (Optional) Run **eb init** again to configure a default key pair so that you can use SSH to connect to the EC2 instance running your application.

   ```
   ~eb-dotnetcore/HelloElasticBeanstalk/site$ eb init
   Do you want to set up SSH for your instances?
   (y/n): y
   Select a keypair.
   1) my-keypair
   2) [ Create new KeyPair ]
   ```

   Select a key pair if you have one already, or follow the prompts to create one. If you don't see the prompt or need to change your settings later, run **eb init -i**.

1. Create an environment and deploy your application to it with **eb create**. Elastic Beanstalk automatically builds a zip file for your application and starts it on port 5000.

   to 

   ```
   ~eb-dotnetcore/HelloElasticBeanstalk/site$ eb create dotnet-tutorial
   ```

   It takes about five minutes for Elastic Beanstalk to create your environment.

## Step 4: Run your application on Elastic Beanstalk
<a name="dotnet-linux-quickstart-run-eb-ap"></a>

When the process to create your environment completes, open your website with **eb open**.

```
~eb-dotnetcore/HelloElasticBeanstalk/site$ eb open
```

Congratulations\! You've deployed a .NET Core on Linux application with Elastic Beanstalk\! This opens a browser window using the domain name created for your application.

## Step 5: Clean up
<a name="go-tutorial-cleanup"></a>

You can terminate your environment when you finish working with your application. Elastic Beanstalk terminates all AWS resources associated with your environment.

To terminate your Elastic Beanstalk environment with the EB CLI run the following command.

```
~eb-dotnetcore/HelloElasticBeanstalk/site$ eb terminate
```

## AWS resources for your application
<a name="dotnet-linux-quickstart-eb-resources"></a>

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
<a name="dotnet-linux-quickstart-next-steps"></a>

After you have an environment running an application, you can deploy a new version of the application or a different application at any time. Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. You can also explore your new environment using the Elastic Beanstalk console. For detailed steps, see [Explore your environment](GettingStarted.md#GettingStarted.Explore) in the *Getting started* chapter of this guide.

After you deploy a sample application or two and are ready to start developing and running .NET Core on Linux applications locally, see [Setting up your .NET core on Linux development environment for Elastic Beanstalk](dotnet-linux-devenv.md). 

## Deploy with the Elastic Beanstalk console
<a name="dotnet-linux-quickstart-console"></a>

You can also use the Elastic Beanstalk console to launch the sample application. For detailed steps, see [Create an example application](GettingStarted.md#GettingStarted.CreateApp) in the *Getting started* chapter of this guide.