# QuickStart: Deploy a PHP application to

Elastic Beanstalk

In the following tutorial, you'll learn how to create and deploy a sample PHP application to an AWS Elastic Beanstalk environment using the EB CLI.

###### Not for production use

Examples are intended for demonstration only. Do not use example applications in production.

###### Sections

- [Your AWS account](#php-quickstart-aws-account "#php-quickstart-aws-account")
- [Prerequisites](#php-quickstart-prereq "#php-quickstart-prereq")
- [Step 1: Create a PHP
  application](#php-quickstart-create-app "#php-quickstart-create-app")
- [Step 2: Run your application locally](#php-quickstart-run-local "#php-quickstart-run-local")
- [Step 3: Initialize and deploy your PHP application](#php-quickstart-deploy "#php-quickstart-deploy")
- [Step 4: Browse your cloud application](#php-quickstart-run-eb-ap "#php-quickstart-run-eb-ap")
- [Step 5: Update and redeploy your application](#php-quickstart-run-eb-ap "#php-quickstart-run-eb-ap")
- [Clean up](#php-quickstart-cleanup "#php-quickstart-cleanup")
- [Next steps](#php-quickstart-next-steps "#php-quickstart-next-steps")

## Your AWS account

If you're not already an AWS customer, you need to create an AWS account to use Elastic Beanstalk.

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

- Elastic Beanstalk Command Line Interface - For installation, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install "eb-cli3.md#eb-cli3-install").
- PHP - Install PHP on your local machine by following [Installation and Configuration](https://www.php.net/manual/en/install.php "https://www.php.net/manual/en/install.php") instructions on
  the PHP website.

## Step 1: Create a PHP

application

For this quick start, you will create a _Hello World_ PHP
application.

Create a project directory.

```
`~$` `mkdir eb-php`
`~$` `cd eb-php`
```

Next, create an `index.php` file in the project directory and add the following code.

###### Example `index.php`

```
<?php
  echo "Hello from a PHP application running in Elastic Beanstalk!";
?>

```

## Step 2: Run your application locally

Use the following command to run your application locally.

```
`~$` `php -S localhost:5000`
```

Open a browser to [`http://localhost:5000`](http://localhost:5000 "http://localhost:5000").

You should see your hello message in the browser and log messages in your terminal.

Stop the local server by entering `Control+c`, so you can deploy the Elastic Beanstalk.

## Step 3: Initialize and deploy your PHP application

Next, you will deploy your application to an _environment_ using the Elastic Beanstalk console or the EB CLI. For this tutorial, you'll use the EB CLI with the interactive option to initialize an environment.

###### To initialize your environment and create an environment

1. Run the following **init** command.

```
`~$` `eb init -i`
```

The init command creates an application interactively. The application name will default to the local folder which is `eb-php`.

For all prompts, except SSH access, accept the defaults to create an environment with the latest PHP platform version. For troubleshooting instances, you can set up SSH access by re-running the `eb init -i`command at a later time, or connect using Amazon EC2 Instance Connect or Session Manager. 2. Create an environment and deploy your application

Run the following command to create an environment named `blue-env`.

```
`~$` `eb create blue-env`
```

When you run the **eb create** command for the first time, Elastic Beanstalk automatically builds a zip file of your application, called a _source bundle_. Next, Elastic Beanstalk creates an environment with one or more Amazon EC2 instances, and then deploys the application into the environment.

Deploying your application to Elastic Beanstalk might take up to five minutes.

## Step 4: Browse your cloud application

When the process to create your environment completes, your application should be running and listening for requests on port 5000. Connect to your application with the following command:

```
`~$` `eb open`
```

The `eb open` command opens a browser tab to a custom subdomain created for your application.

## Step 5: Update and redeploy your application

After you have created an application and deployed to an environment, you can deploy a new version of the
application or a different application at any time. Deploying a new application version is
faster because it doesn't require provisioning or restarting Amazon EC2 instances.

Update your PHP code to include the REQUEST_TIME value from the server environment:

```
<?php
  echo "Hello from a PHP application running in Elastic Beanstalk!";

  $timestamp = $_SERVER['REQUEST_TIME'];
  echo '<br/>Request time: ' . date('Y/m/d H:i:s', $timestamp);
?>
```

Redeploy your PHP code to Elastic Beanstalk with the following command:

```
`~$` `eb deploy`
```

When you run **eb deploy**, the EB CLI bundles up the contents of your project directory and deploys it to your environment.

After the deploy finishes, refresh the page or reconnect to your application with `eb open`. You should see your updates. If not, troubleshoot by running your local server again to verify your changes.

###### Congratulations!

You've created, deployed, and updated a PHP application with Elastic Beanstalk!

## Clean up

After you finish working with the demo code, you can terminate your environment.
Elastic Beanstalk deletes all related AWS resources, such as
[Amazon EC2 instances](using-features.managing.md "using-features.managing.md"),
[database instances](using-features.managing.md "using-features.managing.md"),
[load balancers](using-features.managing.md "using-features.managing.md"),
security groups,
and [alarms](using-features.md#using-features.alarms.title "using-features.md#using-features.alarms.title").

Removing resources does not delete the Elastic Beanstalk application, so you can create new environments for your application at any time.

###### To terminate your Elastic Beanstalk environment from the console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. Choose **Actions**, and then choose **Terminate
   environment**.
4. Use the on-screen dialog box to confirm environment termination.

Alternatively, you can terminate your environment with the EB CLI with the following command:

```
`~$` `eb terminate`
```

## Next steps

You can explore your application environment using the Elastic Beanstalk console. For more info, see [Explore your environment](GettingStarted.md#GettingStarted.Explore "GettingStarted.md#GettingStarted.Explore").

For advanced examples using PHP, see [Advanced examples for PHP in Elastic Beanstalk](php-samples.md "php-samples.md").
