# Getting started with App Runner

AWS App Runner is an AWS service that provides a fast, simple, and cost-effective way to turn an existing container image or source code directly into a
running web service in the AWS Cloud.

This tutorial covers how you can use AWS App Runner to deploy your application to an App Runner service. It walks through configuring the source code and
deployment, the service build, and the service runtime. It also shows how to deploy a code version, make a configuration change, and view logs. Last, the
tutorial shows how to clean up the resources that you created while following the tutorial's procedures.

###### Topics

- [Prerequisites](#getting-started.prereq "#getting-started.prereq")
- [Step 1: Create an App Runner service](#getting-started.create "#getting-started.create")
- [Step 2: Change your service code](#getting-started.deploy "#getting-started.deploy")
- [Step 3: Make a configuration change](#getting-started.config "#getting-started.config")
- [Step 4: View logs for your service](#getting-started.logs "#getting-started.logs")
- [Step 5: Clean up](#getting-started.cleanup "#getting-started.cleanup")
- [What's next](#getting-started.next "#getting-started.next")

## Prerequisites

Before you start the tutorial, be sure to take the following actions:

1. Complete the setup steps in [Setting up for App Runner](setting-up.md "setting-up.md").
2. Decide if you'd like to work with either a GitHub repository or a Bitbucket repository.
   - To work with a Bitbucket, first create a [Bitbucket](https://bitbucket.org/ "https://bitbucket.org/") account, if you don't already have one. If you're new
     to Bitbucket, see [Getting started with
     Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/ "https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/") in the _Bitbucket Cloud Documentation_.
   - To work with GitHub, create a [GitHub](https://github.com/ "https://github.com/") account, if you don't already have one. If you're new to GitHub, see
     [Getting started with GitHub](https://docs.github.com/en/github/getting-started-with-github "https://docs.github.com/en/github/getting-started-with-github") in the _GitHub
     Docs_.

   ###### Note

   You can create connections to multiple repository providers from your account. So if you'd like to walk through deploying from both a GitHub
   and a Bitbucket repository, you can repeat this procedure. The next time through create a new App Runner service and create a new account connection
   for the other repository provider.

3. Create a repository in your repository provider account. This tutorial uses the repository name `python-hello`. Create files in
   the root directory of the repository, with the names and content specified in the following examples.

###### Example requirements.txt

```
pyramid==2.0
```

###### Example server.py

```
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
```

## Step 1: Create an App Runner service

In this step, you create an App Runner service based on the example source code repository that you created on GitHub or Bitbucket as part of [Prerequisites](#getting-started.prereq "#getting-started.prereq"). The example contains a simple Python website. These are the main steps you take to create a service:

1. Configure your source code.
2. Configure source deployment.
3. Configure application build.
4. Configure your service.
5. Review and confirm.

The following diagram outlines the steps for creating an App Runner service:

![App Runner service creation workflow diagram](images/getting-started-create-service-workflow.png)

###### To create an App Runner service based on a source code repository

1.  Configure your source code.
    1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
    2. If the AWS account doesn't have any App Runner services yet, the console home page is displayed. Choose **Create an App Runner service**.

    ![App Runner console home page showing the create service button](images/getting-started-home.png)

    If the AWS account has existing services, the **Services** page with a list of your services is displayed. Choose **Create
    service**.

    ![App Runner console services page](images/getting-started-services.png) 3. On the **Source and deployment** page, in the **Source** section, for **Repository type**,
    choose **Source code repository**. 4. Select a **Provider Type**. Choose either **GitHub** or **Bitbucket**. 5. Next choose **Add new**. If prompted, provide your GitHub or Bitbucket credentials. 6. Choose the next set of steps based on the **Provider type** you previously selected.

    ###### Note

    The following steps to install the AWS connector for GitHub to your GitHub account are one-time steps. You can reuse the connection for
    creating multiple App Runner services based on repositories in this account. When you have an existing connection, choose it and skip to
    repository selection.

    The same applies to the AWS connector for your Bitbucket account. If you're using both GitHub and Bitbucket as source code repositories for
    your App Runner services, you'll need to install one AWS Connector for each provider. You can then reuse each connector for creating more App Runner
    services.

        * For **GitHub**, follow these steps.


        	1. On the next screen, enter a **Connection Name**.
        	2. If this your first time using GitHub with App Runner, select **Install another**.
        	3. In the **AWS Connector for GitHub** dialog box, if prompted, choose your GitHub account name.
        	4. If prompted to authorize the AWS Connector for GitHub, choose **Authorize AWS Connections**.
        	5. In the **Install AWS Connector for GitHub** dialog box,Choose **Install**.


        	Your account name appears as the selected **GitHub account/organization**. You can now choose a repository in your
        	 account.
        	6. For **Repository**, choose the example repository you created, `python-hello`. For
        	 **Branch**, choose the default branch name of your repository (for example, **main**).
        	7. Leave **Source directory** with the default value. The directory defaults to the repository root. You stored your
        	 source code in the repository root directory in the previous *Prerequisites* steps.
        * For **Bitbucket**, follow these steps.


        	1. On the next screen, enter a **Connection Name**.
        	2. If this your first time using Bitbucket with App Runner, select **Install another**.
        	3. In the **AWS CodeStar requests access** dialog box, you can select your workspace and grant access to AWS CodeStar for
        	 Bitbucket integration. Select your workspace, then select **Grant access**.
        	4. Next you'll be redirected to the AWS console. Verify that the Bitbucket application is set to the correct Bitbucket workspace and
        	 select **Next**.
        	5. For **Repository**, choose the example repository you created, `python-hello`. For
        	 **Branch**, choose the default branch name of your repository (for example, **main**).
        	6. Leave **Source directory** with the default value. The directory defaults to the repository root. You stored your
        	 source code in the repository root directory in the previous *Prerequisites* steps.

2.  Configure your deployments: In the **Deployment settings** section, choose **Automatic**, and then choose
    **Next**.

###### Note

With automatic deployment, each new commit to your repository source directory automatically deploys a new version of your service.

![Source and deployment settings while creating an App Runner service](images/getting-started-create-source-depl.png) 3. Configure application build.

    1. On the **Configure build** page, for **Configuration file**, choose **Configure all settings
     here**.
    2. Provide the following build settings:




    	* **Runtime** – Choose **Python 3**.
    	* **Build command** – Enter `pip install -r requirements.txt`.
    	* **Start command** – Enter `python server.py`.
    	* **Port** – Enter `8080`.
    3. Choose **Next**.###### Note

The Python 3 runtime builds a Docker image using a base Python 3 image and your example Python code. It then launches a service that runs a
container instance of this image.

![Build settings while creating an App Runner service](images/getting-started-create-build.png) 4. Configure your service.

    1. On the **Configure service** page, in the **Service settings** section, enter a service name.
    2. Under **Environment variables**, select **Add environment variable**. Provide the following
     values for the environment variable.




    	* **Source** – Choose **Plain text**
    	* **Environment variable name** – `NAME`
    	* **Environment variable value** – any name (for example, your first name).
    ###### Note

    The example application reads the name you set in this environment variable and displays the name on its webpage.
    3. Choose **Next**.

![Service settings while creating an App Runner service](images/getting-started-create-service.png) 5. On the **Review and create** page, verify all the details you've entered, and then choose **Create and
deploy**.

If the service is successfully created, the console shows the service dashboard, with a **Service overview** of the new
service.

![App Runner service dashboard page](images/getting-started-create-dashboard.png) 6. Verify that your service is running.

    1. On the service dashboard page, wait until the service **Status** is **Running**.
    2. Choose the **Default domain** value—it's the URL to the website of your service.


    ###### Note

    To augment the security of your App Runner applications, the *\*.awsapprunner.com* domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further security, we recommend that you use cookies with a `__Host-`
     prefix if you ever need to set sensitive cookies in the default domain name for your App Runner applications.
     This practice will help to defend your domain against cross-site request
     forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.


    A webpage displays: **Hello, `your name`!**

![The application web page of an App Runner service](images/getting-started-create-webpage.png)

## Step 2: Change your service code

In this step, you make a change to your code in the repository source directory. The App Runner CI/CD capability automatically builds and deploys the change to your
service.

###### To make a change to your service code

1. Navigate to your example repository.
2. Edit the file named `server.py`.
3. In the expression assigned to the variable `message`, change the text `Hello` to `Good morning`.
4. Save and commit your changes to the repository.
5. The following steps illustrate changing the service code in a GitHub repository.
   1. Navigate to your example GitHub repository.
   2. Choose the file name `server.py` to navigate to that file.
   3. Choose **Edit this file** (the pencil icon).
   4. In the expression assigned to the variable `message`, change the text `Hello` to `Good morning`.

   ![GitHub file page with edit icon and message highlighted](images/getting-started-deploy-edit.png) 5. Choose **Commit changes**.

6. The new commit starts to deploy for your App Runner service. On the service dashboard page, the service **Status** changes to
   **Operation in progress**.

Wait for the deployment to end. On the service dashboard page, the service **Status** should change back to
**Running**. 7. Verify that the deployment is successful: refresh the browser tab where the webpage of your service is displayed.

The page now displays the modified message: **Good morning, `your name`!**

## Step 3: Make a configuration change

In this step, you make a change to the `NAME` environment variable value, to demonstrate a service configuration change.

###### To change an environment variable value

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Services**, and then choose your App Runner service.

The console displays the service dashboard with a **Service overview**.

![App Runner service dashboard page showing Activity list](images/console-dashboard.png) 3. On the service dashboard page, choose the **Configuration** tab.

The console displays your service configuration settings in several sections. 4. In the **Configure service** section, choose **Edit**.

![The Service configuration section of the Configuration tab on the App Runner service dashboard page](images/service-dashboad-config-service.png) 5. For the environment variable with the key `NAME`, change the value to a different name. 6. Choose **Apply changes**.

App Runner starts the update process. On the service dashboard page, the service **Status** changes to **Operation in
progress**. 7. Wait for the update to end. On the service dashboard page, the service **Status** should change back to
**Running**. 8. Verify that the update is successful: refresh the browser tab where the webpage of your service is displayed.

The page now displays the modified name: **Good morning, `new name`!**

## Step 4: View logs for your service

In this step, you use the App Runner console to view logs for your App Runner service. App Runner streams logs to Amazon CloudWatch Logs (CloudWatch Logs) and displays them on your service's
dashboard. For information about App Runner logs, see [Viewing App Runner logs streamed to CloudWatch Logs](monitor-cwl.md "monitor-cwl.md").

###### To view logs for your service

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Services**, and then choose your App Runner service.

The console displays the service dashboard with a **Service overview**.

![App Runner service dashboard page showing Activity list](images/console-dashboard.png) 3. On the service dashboard page, choose the **Logs** tab.

The console displays a few types of logs in several sections:

    * Event log – Activity in the lifecycle of your App Runner service. The console displays the latest events.
    * Deployment logs – Source repository deployments to your App Runner service. The console displays a separate log
     stream for each deployment.
    * Application logs – The output of the web application that's deployed to your App Runner service. The console
     combines the output from all running instances into a single log stream.

![The Logs tab on the App Runner service dashboard page](images/service-dashboad-logs.png) 4. To find specific deployments, scope down the deployment log list by entering a search term. You can search for any value that appears in the
table. 5. To view a log's content, choose **View full log** (event log) or the log stream name (deployment and application logs). 6. Choose **Download** to download a log. For a deployment log stream, select a log stream first. 7. Choose **View in CloudWatch** to open the CloudWatch console and use its full capabilities to explore your App Runner service logs. For a deployment
log stream, select a log stream first.

###### Note

The CloudWatch console is particularly useful if you want to view application logs of specific instances instead of the combined application log.

## Step 5: Clean up

You've now learned how to create an App Runner service, view logs, and make some changes. In this step, you delete the service to remove resources that you
don't need anymore.

###### To delete your service

1. On the service dashboard page, choose **Actions**, and then choose **Delete service**.
2. In the confirmation dialog, enter the requested text, and then choose **Delete**.

Result: The console navigates to the **Services** page. The service that you just deleted shows a status of
**DELETING**. A short time later it disappears from the list.

Consider also deleting the GitHub and Bitbucket connections that you created as part of this tutorial. For more information, see [Managing App Runner connections](manage-connections.md "manage-connections.md").

## What's next

Now that you've deployed your first App Runner service, learn more in the following topics:

- [App Runner architecture and concepts](architecture.md "architecture.md") – The architecture, main concepts, and AWS resources related to App Runner.
- [Image-based service](service-source-image.md "service-source-image.md") and [Code-based service](service-source-code.md "service-source-code.md") – The two types of application source that App Runner can deploy.
- [Developing application code for App Runner](develop.md "develop.md") – Things you should know when developing or migrating application code for deployment to App Runner.
- [Using the App Runner console](console.md "console.md") – Manage and monitor your service using the App Runner console.
- [Managing your App Runner service](manage.md "manage.md") – Manage the lifecycle of your App Runner service.
- [Observability for your App Runner service](monitor.md "monitor.md") – Get visibility into your App Runner service operations by monitoring metrics, reading logs, handling events, tracking
  service action calls, and tracing application events like HTTP calls.
- [App Runner configuration file](config-file.md "config-file.md") – A configuration-based way to specify options for the build and runtime
  behavior of your App Runner service.
- [The App Runner API](api.md "api.md") – Use the App Runner application programming interface (API) to create, read, update, and delete App Runner resources.
- [Security in App Runner](security.md "security.md") – The different ways that AWS and you ensure cloud security while you use App Runner and other services.
