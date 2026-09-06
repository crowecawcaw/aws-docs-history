

# QuickStart: Deploy a PHP application to Elastic Beanstalk
<a name="php-quickstart"></a>

In the following tutorial, you'll learn how to create and deploy a sample PHP application to an AWS Elastic Beanstalk environment using the EB CLI.

**Not for production use**  
Examples are intended for demonstration only. Do not use example applications in production.

**Topics**
+ [Your AWS account](#php-quickstart-aws-account)
+ [Prerequisites](#php-quickstart-prereq)
+ [Step 1: Create a PHP application](#php-quickstart-create-app)
+ [Step 2: Run your application locally](#php-quickstart-run-local)
+ [Step 3: Initialize and deploy your PHP application](#php-quickstart-deploy)
+ [Step 4: Browse your cloud application](#php-quickstart-run-eb-ap)
+ [Step 5: Update and redeploy your application](#php-quickstart-run-eb-ap)
+ [Clean up](#php-quickstart-cleanup)
+ [Next steps](#php-quickstart-next-steps)

## Your AWS account
<a name="php-quickstart-aws-account"></a>

If you're not already an AWS customer, you need to create an AWS account to use Elastic Beanstalk.

### Create an AWS account
<a name="php-quickstart-aws-account-procedure"></a>

#### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="php-quickstart-prereq"></a>
+ Elastic Beanstalk Command Line Interface - For installation, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install).
+ PHP - Install PHP on your local machine by following [Installation and Configuration](https://www.php.net/manual/en/install.php) instructions on the PHP website.

## Step 1: Create a PHP application
<a name="php-quickstart-create-app"></a>

For this quick start, you will create a *Hello World* PHP application.

Create a project directory.

```
~$ mkdir eb-php
~$ cd eb-php
```

Next, create an `index.php` file in the project directory and add the following code.

**Example `index.php`**  

```
<?php
  echo "Hello from a PHP application running in Elastic Beanstalk!";
?>
```

## Step 2: Run your application locally
<a name="php-quickstart-run-local"></a>

Use the following command to run your application locally.

```
~$ php -S localhost:5000
```

Open a browser to [`http://localhost:5000`](http://localhost:5000).

You should see your hello message in the browser and log messages in your terminal.

Stop the local server by entering `Control+c`, so you can deploy the Elastic Beanstalk.

## Step 3: Initialize and deploy your PHP application
<a name="php-quickstart-deploy"></a>

Next, you will deploy your application to an *environment* using the Elastic Beanstalk console or the EB CLI. For this tutorial, you'll use the EB CLI with the interactive option to initialize an environment. 

**To initialize your environment and create an environment**

1. Run the following **init** command.

   ```
   ~$ eb init -i
   ```

   The init command creates an application interactively. The application name will default to the local folder which is `eb-php`.

   For all prompts, except SSH access, accept the defaults to create an environment with the latest PHP platform version. For troubleshooting instances, you can set up SSH access by re-running the `eb init -i`command at a later time, or connect using Amazon EC2 Instance Connect or Session Manager.

1. Create an environment and deploy your application

   Run the following command to create an environment named `blue-env`.

   ```
   ~$ eb create blue-env
   ```

   When you run the **eb create** command for the first time, Elastic Beanstalk automatically builds a zip file of your application, called a *source bundle*. Next, Elastic Beanstalk creates an environment with one or more Amazon EC2 instances, and then deploys the application into the environment.

   Deploying your application to Elastic Beanstalk might take up to five minutes.

## Step 4: Browse your cloud application
<a name="php-quickstart-run-eb-ap"></a>

When the process to create your environment completes, your application should be running and listening for requests on port 5000. Connect to your application with the following command:

```
~$ eb open
```

The `eb open` command opens a browser tab to a custom subdomain created for your application.

## Step 5: Update and redeploy your application
<a name="php-quickstart-run-eb-ap"></a>

After you have created an application and deployed to an environment, you can deploy a new version of the application or a different application at any time. Deploying a new application version is faster because it doesn't require provisioning or restarting Amazon EC2 instances.

Update your PHP code to include the REQUEST\_TIME value from the server environment:

```
<?php
  echo "Hello from a PHP application running in Elastic Beanstalk!";
  
  $timestamp = $_SERVER['REQUEST_TIME'];
  echo '<br/>Request time: ' . date('Y/m/d H:i:s', $timestamp);
?>
```

Redeploy your PHP code to Elastic Beanstalk with the following command:

```
~$ eb deploy
```

When you run **eb deploy**, the EB CLI bundles up the contents of your project directory and deploys it to your environment.

After the deploy finishes, refresh the page or reconnect to your application with `eb open`. You should see your updates. If not, troubleshoot by running your local server again to verify your changes.

****Congratulations\!****  
You've created, deployed, and updated a PHP application with Elastic Beanstalk\!

## Clean up
<a name="php-quickstart-cleanup"></a>

After you finish working with the demo code, you can terminate your environment. Elastic Beanstalk deletes all related AWS resources, such as [Amazon EC2 instances](using-features.managing.ec2.md), [database instances](using-features.managing.db.md), [load balancers](using-features.managing.elb.md), security groups, and [alarms](using-features.alarms.md#using-features.alarms.title). 

Removing resources does not delete the Elastic Beanstalk application, so you can create new environments for your application at any time.

**To terminate your Elastic Beanstalk environment from the console**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. Choose **Actions**, and then choose **Terminate environment**.

1. Use the on-screen dialog box to confirm environment termination.

Alternatively, you can terminate your environment with the EB CLI with the following command:

```
~$ eb terminate
```

## Next steps
<a name="php-quickstart-next-steps"></a>

You can explore your application environment using the Elastic Beanstalk console. For more info, see [Explore your environment](GettingStarted.md#GettingStarted.Explore).

For advanced examples using PHP, see [Advanced examples for PHP in Elastic Beanstalk](php-samples.md).