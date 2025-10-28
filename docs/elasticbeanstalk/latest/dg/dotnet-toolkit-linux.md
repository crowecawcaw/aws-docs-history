# The AWS Toolkit for Visual Studio - Working with .Net Core on Elastic Beanstalk

This topic shows how you can do the following tasks using the AWS Toolkit for Visual Studio:

- Create an ASP.NET Core web application using a Visual Studio template.
- Create an Elastic Beanstalk Amazon Linux environment.
- Deploy the ASP.NET Core web application to the new Amazon Linux environment.
  This topic also explores how you can use the AWS Toolkit for Visual Studio to manage your Elastic Beanstalk application environments and monitor your application's health.

The AWS Toolkit for Visual Studio is a plugin to the Visual Studio IDE. With the toolkit you can deploy and manage applications in Elastic Beanstalk while you are working in your Visual Studio
environment.

###### Sections

- [Prerequisites](#dotnet-toolkit-linux-core-tutorial-prereqs "#dotnet-toolkit-linux-core-tutorial-prereqs")
- [Create a new application project](#dotnet-toolkit-linux-core-tutorial-create-project "#dotnet-toolkit-linux-core-tutorial-create-project")
- [Create an Elastic Beanstalk environment and deploy your application](#dotnet-toolkit-linux-core-tutorial-create-env-and-deploy "#dotnet-toolkit-linux-core-tutorial-create-env-and-deploy")
- [Terminating an environment](#dotnet-toolkit-linux-core-tutorial-terminate-env "#dotnet-toolkit-linux-core-tutorial-terminate-env")
- [Managing your Elastic Beanstalk application environments](create_deploy_NET-linux.md "create_deploy_NET-linux.md")
- [Monitoring application health](create_deploy_NET-linux.md "create_deploy_NET-linux.md")

## Prerequisites

Before you begin this tutorial, you need to install the AWS Toolkit for Visual Studio. For instructions, see [Setting up the AWS Toolkit for Visual Studio](../../../toolkit-for-visual-studio/latest/user-guide/getting-set-up.md "../../../toolkit-for-visual-studio/latest/user-guide/getting-set-up.md").

If you have never used the toolkit before, the first thing you'll need to do after installing the toolkit is to register your AWS credentials with
the toolkit. For more information about this, see [Providing
AWS Credentials](../../../toolkit-for-visual-studio/latest/user-guide/credentials.md "../../../toolkit-for-visual-studio/latest/user-guide/credentials.md").

## Create a new application project

If you don't have a .NET Core application project in Visual Studio, you can easily create one using one of the Visual Studio project templates.

###### To create a new ASP.NET Core web application project

1. In Visual Studio, on the **File** menu, choose **New** and then choose **Project**.
2. In the **Create a new project** dialog box, select **C#**, select **Linux**, and then select
   **Cloud**.
3. From the list of project templates that displays select **ASP.NET Core Web Application**, and then select
   **Next**.

###### Note

If you don't see **ASP.NET Core Web Application** listed in the project templates, you can install it in Visual Studio.

    1. Scroll to the bottom of the template list and select the **Install more tools and features** link that is located under the
     template list.
    2. If you are prompted to allow the Visual Studio application to make changes to your device, select **Yes**.
    3. Choose the **Workloads** tab, then select **ASP.NET and web development.**
    4. Select the **Modify** button. The **Visual Studio Installer** installs the project template.
    5. After the installer completes, exit the panel to return to where you left off in Visual Studio .

4. In the **Configure your new project** dialog box, enter a **Project name**. The **Solution
   name** defaults to your project name. Next, choose **Create**.
5. In the **Create a new ASP.NET Core web application** dialog box, select **.NET Core**, and then select
   **ASP.NET Core 3.1**. From the list of application types that are displayed, select **Web Application**, then
   select the **Create** button.

Visual Studio displays the **Creating Project** dialog box when it creates your application. After Visual Studio completes generating your
application, a panel with your application name is displayed.

## Create an Elastic Beanstalk environment and deploy your application

This section describes how to create an Elastic Beanstalk environment for your application and deploy your application to that environment.

###### To create a new environment and deploy your application

1. In Visual Studio select **View**, then **Solution Explorer**.
2. In **Solution Explorer**, open the context (right-click) menu for your application, and then select **Publish to
   AWS Elastic Beanstalk**.
3. In the **Publish to AWS Elastic Beanstalk** wizard, enter your account information.
   1. For **Account profile to use**, select your **default** account or choose the **Add another
      account** icon to enter new account information.
   2. For **Region**, select the Region where you want to deploy your application. For information about available AWS Regions,
      see [AWS Elastic Beanstalk Endpoints and Quotas](../../../general/latest/gr/elasticbeanstalk.md "../../../general/latest/gr/elasticbeanstalk.md") in the _AWS General Reference_. If you
      select a Region that is not supported by Elastic Beanstalk, then the option to deploy to Elastic Beanstalk is unavailable.
   3. Select **Create a new application environment**, then choose **Next**.

4. On the **Application Environment** dialog box, enter the details for your new application environment.
5. On the next **AWS** options dialog box, set Amazon EC2 options and other AWS related options for your deployed
   application.
   1. For **Container type** select **64bit Amazon Linux 2 v`<n.n.n>` running .NET
      Core.**

   ###### Note

   We recommend you select the current platform version of Linux. This version contains the most recent security and bug fixes that are
   included in our latest Amazon Machine Image (AMI). 2. For **Instance Type**, select **t2.micro**. (Choosing a micro instance type minimizes the cost associated
   with running the instance.) 3. For **Key pair**, select **Create new key pair**. Enter a name for the new key pair, and then choose
   **OK**. (In this example, we use `myuseastkeypair`.) A key pair enables remote-desktop access to your
   Amazon EC2 instances. For more information about Amazon EC2 key pairs, see [Using
   Credentials](../../../AWSEC2/latest/UserGuide/using-credentials.md "../../../AWSEC2/latest/UserGuide/using-credentials.md") in the _Amazon Elastic Compute Cloud User Guide_. 4. For a simple, low traffic application, select **Single instance environment**. For more information, see [Environment types](using-features-managing-env-types.md "using-features-managing-env-types.md") 5. Select **Next**. For more information about the AWS options that are not used in this example consider the following pages:
   - For **Use custom AMI**, see [Using a custom Amazon machine image (AMI) in your Elastic Beanstalk environment](using-features.md "using-features.md").
   - If you don't select **Single instance environment**, you need to choose a **Load balance type**. See [Load balancer for your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md") for more information.
   - Elastic Beanstalk uses the default [Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") (Amazon Virtual Private Cloud) configuration if you didn't choose **Use
     non-default VPC**. For more information see [Using Elastic Beanstalk with Amazon VPC](vpc.md "vpc.md").
   - Choosing the **Enable Rolling Deployments** option splits a deployment into batches to avoid potential downtime during
     deployments. For more information, see [Deploying applications to Elastic Beanstalk environments](using-features.md "using-features.md").
   - Choosing the **Relational Database Access** option connects your Elastic Beanstalk environment to a previously created Amazon RDS
     database with _Amazon RDS DB Security Groups_. For more information, see [Controlling Access with Security Groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") in the
     _Amazon RDS User Guide_.

6. Select **Next** on the **Permissions** dialog box.
7. Select **Next** on the **Applications Options** dialog box.
8. Review your deployment options. After you've verified your settings are correct, select **Deploy**.

Your ASP.NET Core web application is exported as a web deploy file. This file is then uploaded to Amazon S3 and registered as a new application version
with Elastic Beanstalk. The Elastic Beanstalk deployment feature monitors your environment until it is available with the newly deployed code. The **Status** for
your environment is displayed on the Env:<environment name> tab. After the status updates to **Environment is healthy**, you can
select the URL address to launch the web application.

## Terminating an environment

To avoid incurring charges for unused AWS resources, you can use the AWS Toolkit for Visual Studio to terminate a running environment.

###### Note

You can always launch a new environment using the same version later.

###### To terminate an environment

1. Expand the Elastic Beanstalk node and the application node. In **AWS Explorer** open the context (right-click) menu for your application
   environment and select **Terminate Environment**.
2. When prompted, select **Yes** to confirm that you want to terminate the environment. It takes a few minutes for Elastic Beanstalk to
   terminate the AWS resources running in the environment.

The **Status** for your environment on the Env:<environment name> tab changes to **Terminating** and is
eventually **Terminated**.

###### Note

When you terminate your environment, the CNAME associated with the terminated environment becomes available for anyone to use.
