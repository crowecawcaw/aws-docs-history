

# QuickStart: Deploy an ASP.NET application to Elastic Beanstalk
<a name="aspnet-quickstart"></a>

This QuickStart tutorial walks you through the process of creating a ASP.NET application and deploying it to an AWS Elastic Beanstalk environment.

**Not for production use**  
Examples are intended for demonstration only. Do not use example applications in production.

**Topics**
+ [Your AWS account](#aspnet-quickstart-aws-account)
+ [Prerequisites](#aspnet-quickstart-prereq)
+ [Step 1: Create a ASP.NET application](#aspnet-quickstart-create-app)
+ [Step 2: Run your application locally](#aspnet-quickstart-run-local)
+ [Step 3: Deploy your ASP.NET application with the AWS Toolkit for Visual Studio](#aspnet-quickstart-deploy)
+ [Step 4: Run your application on Elastic Beanstalk](#aspnet-quickstart-run-eb-ap)
+ [Step 5: Clean up](#aspnet-quickstart-cleanup)
+ [AWS resources for your application](#aspnet-quickstart-eb-resources)
+ [Next steps](#aspnet-quickstart-next-steps)
+ [Deploy with the Elastic Beanstalk console](#aspnet-quickstart-console)

## Your AWS account
<a name="aspnet-quickstart-aws-account"></a>

If you're not already an AWS customer, you need to create an AWS account. Signing up enables you to access Elastic Beanstalk and other AWS services that you need.

If you already have an AWS account, you can move on to [Prerequisites](#aspnet-quickstart-prereq).

### Create an AWS account
<a name="aspnet-quickstart-aws-account-procedure"></a>

#### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="aspnet-quickstart-prereq"></a>

This QuickStart tutorial walks you through creating a "Hello World" application and deploying it to an Elastic Beanstalk environment with Visual Studio and the AWS Toolkit for Visual Studio.

### Visual Studio
<a name="aspnet-quickstart-prereq.vs"></a>

To download and install Visual Studio follow the instructions on the Visual Studio [download page](https://visualstudio.microsoft.com/downloads/). This example uses Visual Studio 2022. During the Visual Studio installation select these specific items:
+ On the **Workloads** tab — select **ASP.NET and web development**.
+ On the **Individual components** tab — select **.NET Framework 4.8 development tools** and **.NET Framework project and item templates**.

### AWS Toolkit for Visual Studio
<a name="aspnet-quickstart-prereq.aws-vs-tk"></a>

To download and set up AWS Toolkit for Visual Studio follow the instructions in the [Getting started](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/getting-set-up.html) topic of the AWS Toolkit for Visual Studio User Guide. 

## Step 1: Create a ASP.NET application
<a name="aspnet-quickstart-create-app"></a>

Next, create an application that you'll deploy to an Elastic Beanstalk environment. We'll create a "Hello World" ASP.NET web application.

**To create an ASP.NET application**

1. Launch Visual Studio. In the **File** menu, select **New**, then **Project**.

1. The **Create a new project** dialog box displays. Select **ASP.NET web application (.NET Framework)**, then select **Next**.

1. On the **Configure your new project** dialog, enter `eb-aspnet` for your **Project name**. From the **Framework** dropdown menu select **.NET Framework 4.8**, then select **Create**.

   Note the project directory. In this example, the project directory is `C:\Users\Administrator\source\repos\eb-aspnet\eb-aspnet`.

1. The **Create a new ASP.NET Web Application** dialogue displays. Select the **Empty** template. Next select **Create**.

   At this point, you have created an empty ASP.NET web application project using Visual Studio. Next, we'll create a web form that will serve as the entry point for the ASP.NET web application.

1. From the **Project** menu, select **Add New Item**. On the **Add New Item** page, select **Web Form** and name it `Default.aspx`. Next select **Add**.

1. Add the following to `Default.aspx:`

   ```
   <%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="eb_aspnet.Default" %>
   
   <!DOCTYPE html>
   
   <html xmlns="https://www.w3.org/1999/xhtml">
   <head runat="server">
       <title>Hello Elastic Beanstalk!</title>
   </head>
   <body>
       <form id="body" runat="server">
           <div>
               Hello Elastic Beanstalk! This is an ASP.NET on Windows Server application.
           </div>
       </form>
   </body>
   </html>
   ```

## Step 2: Run your application locally
<a name="aspnet-quickstart-run-local"></a>

In Visual Studio, from the **Debug** menu select **Start Debugging** to run your application locally. The page should display "Hello Elastic Beanstalk\! This is an ASP.NET on Windows Server application."

## Step 3: Deploy your ASP.NET application with the AWS Toolkit for Visual Studio
<a name="aspnet-quickstart-deploy"></a>

Follow these steps to create an Elastic Beanstalk environment and deploy your new application to it.

**To create an environment and deploy your ASP.NET application**

1. In **Solution Explorer**, right-click your application, then select **Publish to AWS Elastic Beanstalk**.

1. Choose a name for your new Elastic Beanstalk application and environment.

1. Beyond this point, you may proceed with the defaults provided by Elastic Beanstalk or modify any of the options and settings to your liking.

1. On the **Review** page, select **Deploy**. This will package your ASP.NET web application and deploy it to Elastic Beanstalk.

   It takes about five minutes for Elastic Beanstalk to create your environment. The Elastic Beanstalk deployment feature will monitor your environment until it becomes available with the newly deployed code. On the **Env:<**environment name**>** tab, you'll see the status for your environment.

## Step 4: Run your application on Elastic Beanstalk
<a name="aspnet-quickstart-run-eb-ap"></a>

When the process to create your environment completes, the **Env:<**environment name**>** tab, displays information about your environment and application, including the domain URL to launch your application. Select this URL on this tab or copy and paste it into your web browser.

Congratulations\! You've deployed a ASP.NET application with Elastic Beanstalk\!

## Step 5: Clean up
<a name="aspnet-quickstart-cleanup"></a>

When you finish working with your application, you can terminate your environment in the AWS Toolkit for Visual Studio.

**To terminate your environment**

1. Expand the Elastic Beanstalk node and the application node in **AWS Explorer**. Right-click your application environment and select **Terminate Environment**.

1. When prompted, select **Yes** to confirm that you want to terminate the environment. It will take a few minutes for Elastic Beanstalk to terminate the AWS resources running in the environment.

## AWS resources for your application
<a name="aspnet-quickstart-eb-resources"></a>

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
<a name="aspnet-quickstart-next-steps"></a>

After you have an environment running an application, you can deploy a new version of the application or a different application at any time. Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. You can also explore your new environment using the Elastic Beanstalk console. For detailed steps, see [Explore your environment](GettingStarted.md#GettingStarted.Explore) in the *Getting started* chapter of this guide.

**Try more tutorials**  
If you'd like to try other tutorials with different example applications, see [QuickStart for .NET Core on Windows](dotnet-quickstart.md).

After you deploy a sample application or two and are ready to start developing and running ASP.NET applications locally, see [Setting up your .NET development environment](dotnet-devenv.md) 

## Deploy with the Elastic Beanstalk console
<a name="aspnet-quickstart-console"></a>

You can also use the Elastic Beanstalk console to launch the sample application. For detailed steps, see [Create an example application](GettingStarted.md#GettingStarted.CreateApp) in the *Getting started* chapter of this guide.