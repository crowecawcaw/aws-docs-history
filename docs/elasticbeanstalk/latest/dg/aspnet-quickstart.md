# QuickStart: Deploy an ASP.NET application to Elastic Beanstalk

This QuickStart tutorial walks you through the process of creating a ASP.NET application and deploying it to an AWS Elastic Beanstalk environment.

###### Not for production use

Examples are intended for demonstration only. Do not use example applications in production.

###### Sections

- [Your AWS account](#aspnet-quickstart-aws-account "#aspnet-quickstart-aws-account")
- [Prerequisites](#aspnet-quickstart-prereq "#aspnet-quickstart-prereq")
- [Step 1: Create a ASP.NET application](#aspnet-quickstart-create-app "#aspnet-quickstart-create-app")
- [Step 2: Run your application locally](#aspnet-quickstart-run-local "#aspnet-quickstart-run-local")
- [Step 3: Deploy your ASP.NET application with the AWS Toolkit for Visual Studio](#aspnet-quickstart-deploy "#aspnet-quickstart-deploy")
- [Step 4: Run your application on Elastic Beanstalk](#aspnet-quickstart-run-eb-ap "#aspnet-quickstart-run-eb-ap")
- [Step 5: Clean up](#aspnet-quickstart-cleanup "#aspnet-quickstart-cleanup")
- [AWS resources for your application](#aspnet-quickstart-eb-resources "#aspnet-quickstart-eb-resources")
- [Next steps](#aspnet-quickstart-next-steps "#aspnet-quickstart-next-steps")
- [Deploy with the Elastic Beanstalk console](#aspnet-quickstart-console "#aspnet-quickstart-console")

## Your AWS account

If you're not already an AWS customer, you need to create an AWS account. Signing up enables you to access Elastic Beanstalk and other AWS services that you
need.

If you already have an AWS account, you can move on to [Prerequisites](#aspnet-quickstart-prereq "#aspnet-quickstart-prereq").

#### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

#### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Prerequisites

This QuickStart tutorial walks you through creating a "Hello World" application and deploying it to an Elastic Beanstalk environment with Visual Studio and the AWS Toolkit for Visual Studio.

### Visual Studio

To download and install Visual Studio follow the instructions on the Visual Studio [download page](https://visualstudio.microsoft.com/downloads/ "https://visualstudio.microsoft.com/downloads/").
This example uses Visual Studio 2022. During the Visual Studio installation select these specific items:

- On the **Workloads** tab — select **ASP.NET and web development**.
- On the **Individual components** tab — select **.NET Framework 4.8 development
  tools** and **.NET Framework project and item templates**.

### AWS Toolkit for Visual Studio

To download and set up AWS Toolkit for Visual Studio follow the instructions in the [Getting started](../../../toolkit-for-visual-studio/latest/user-guide/getting-set-up.md "../../../toolkit-for-visual-studio/latest/user-guide/getting-set-up.md") topic of the AWS Toolkit for Visual Studio User Guide.

## Step 1: Create a ASP.NET application

Next, create an application that you'll deploy to an Elastic Beanstalk environment. We'll create a "Hello World" ASP.NET web application.

###### To create an ASP.NET application

1. Launch Visual Studio. In the **File** menu, select **New**, then **Project**.
2. The **Create a new project** dialog box displays. Select **ASP.NET web application (.NET
   Framework)**, then select **Next**.
3. On the **Configure your new project** dialog, enter `eb-aspnet` for your **Project name**. From the **Framework** dropdown menu select **.NET Framework
   4.8**, then select **Create**.

Note the project directory. In this example, the project directory is
`C:\Users\Administrator\source\repos\eb-aspnet\eb-aspnet`. 4. The **Create a new ASP.NET Web Application** dialogue displays. Select the **Empty**
template. Next select **Create**.

At this point, you have created an empty ASP.NET web application project using Visual Studio. Next, we'll create a web form that will serve as the entry
point for the ASP.NET web application. 5. From the **Project** menu, select **Add New Item**. On the **Add New
Item** page, select **Web Form** and name it `Default.aspx`. Next select **Add**. 6. Add the following to `Default.aspx:`

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

In Visual Studio, from the **Debug** menu select **Start Debugging** to run your application locally.
The page should display "Hello Elastic Beanstalk! This is an ASP.NET on Windows Server application."

## Step 3: Deploy your ASP.NET application with the AWS Toolkit for Visual Studio

Follow these steps to create an Elastic Beanstalk environment and deploy your new application to it.

###### To create an environment and deploy your ASP.NET application

1. In **Solution Explorer**, right-click your application, then select **Publish to
   AWS Elastic Beanstalk**.
2. Choose a name for your new Elastic Beanstalk application and environment.
3. Beyond this point, you may proceed with the defaults provided by Elastic Beanstalk or modify any of the options and settings to your liking.
4. On the **Review** page, select **Deploy**. This will package your ASP.NET web
   application and deploy it to Elastic Beanstalk.

It takes about five minutes for Elastic Beanstalk to create your environment. The Elastic Beanstalk deployment feature will monitor your environment until it becomes
available with the newly deployed code. On the **Env:<`environment name`>** tab, you'll see
the status for your environment.

## Step 4: Run your application on Elastic Beanstalk

When the process to create your environment completes, the **Env:<`environment name`>** tab,
displays information about your environment and application, including the domain URL to launch your application. Select this URL on this tab or copy and
paste it into your web browser.

Congratulations! You've deployed a ASP.NET application with Elastic Beanstalk!

## Step 5: Clean up

When you finish working with your application, you can terminate your environment in the AWS Toolkit for Visual Studio.

###### To terminate your environment

1. Expand the Elastic Beanstalk node and the application node in **AWS Explorer**. Right-click your application environment and
   select **Terminate Environment**.
2. When prompted, select **Yes** to confirm that you want to terminate the environment. It will take a few minutes for
   Elastic Beanstalk to terminate the AWS resources running in the environment.

## AWS resources for your application

You just created a single instance application. It serves as a straightforward sample application with a single EC2 instance, so it doesn't require
load balancing or auto scaling. For single instance applications Elastic Beanstalk creates the following AWS resources:

- **EC2 instance** – An Amazon EC2 virtual machine configured to run web apps on the platform you choose.

Each platform runs a different set of software, configuration files, and scripts to support a specific language version, framework, web container, or
combination thereof. Most platforms use either Apache or nginx as a reverse proxy that processes web traffic in front of your web app, forwards requests
to it, serves static assets, and generates access and error logs.

- **Instance security group** – An Amazon EC2 security group configured to allow incoming traffic on port 80. This
  resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic is not allowed on other ports.
- **Amazon S3 bucket** – A storage location for your source
  code, logs, and other artifacts that are created when you use Elastic Beanstalk.
- **Amazon CloudWatch alarms** – Two CloudWatch alarms that monitor
  the load on the instances in your environment and are triggered if the load is too high or too
  low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
- **AWS CloudFormation stack** – Elastic Beanstalk uses AWS CloudFormation to launch the
  resources in your environment and propagate configuration changes. The resources are defined
  in a template that you can view in the [AWS CloudFormation
  console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
- **Domain name** – A domain name that routes to your
  web app in the form
  _`subdomain`.`region`.elasticbeanstalk.com_.

Elastic Beanstalk manages all of these resources. When you terminate your environment, Elastic Beanstalk terminates all the resources that it contains.

## Next steps

After you have an environment running an application, you can deploy a new version of the application or a different application at any time.
Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. You can also explore your new
environment using the Elastic Beanstalk console. For detailed steps, see [Explore your environment](GettingStarted.md#GettingStarted.Explore "GettingStarted.md#GettingStarted.Explore") in the
_Getting started_ chapter of this guide.

###### Try more tutorials

If you'd like to try other tutorials with different example applications, see [QuickStart for .NET Core on Windows](dotnet-quickstart.md "dotnet-quickstart.md").

After you deploy a sample application or two and are ready to start developing and running ASP.NET applications locally, see [Setting up your .NET development environment](dotnet-devenv.md "dotnet-devenv.md")

## Deploy with the Elastic Beanstalk console

You can also use the Elastic Beanstalk console to launch the sample application. For detailed steps, see [Create an
example application](GettingStarted.md#GettingStarted.CreateApp "GettingStarted.md#GettingStarted.CreateApp") in the _Getting started_ chapter of this guide.
