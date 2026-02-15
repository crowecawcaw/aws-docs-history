# Deploying a Symfony application to Elastic Beanstalk

[Symfony](http://symfony.com/ "http://symfony.com/") is an open-source framework for developing dynamic PHP web applications. This tutorial walks you
through the process of generating a Symfony application and deploying it to an AWS Elastic Beanstalk environment.

###### Sections

- [Prerequisites](#php-symfony-tutorial-prereqs "#php-symfony-tutorial-prereqs")
- [Launch an Elastic Beanstalk environment](#php-symfony-tutorial-launch "#php-symfony-tutorial-launch")
- [Install Symfony and generate a website](#php-symfony-tutorial-generate "#php-symfony-tutorial-generate")
- [Deploy your application](#php-symfony-tutorial-deploy "#php-symfony-tutorial-deploy")
- [Configure Composer settings](#php-symfony-tutorial-configure "#php-symfony-tutorial-configure")
- [Cleanup](#php-symfony-tutorial-cleanup "#php-symfony-tutorial-cleanup")
- [Next steps](#php-symfony-tutorial-nextsteps "#php-symfony-tutorial-nextsteps")

## Prerequisites

This tutorial assumes you have knowledge of the basic Elastic Beanstalk operations and the Elastic Beanstalk console. If you haven't already, follow the instructions in [Learn how to get started with Elastic Beanstalk](GettingStarted.md "GettingStarted.md") to launch your first Elastic Beanstalk environment.

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in
listings preceded by a
prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ `this is a command`
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10 "https://docs.microsoft.com/en-us/windows/wsl/install-win10") to get a Windows-integrated version of
Ubuntu and Bash.

Symfony 4.4.9 requires PHP 7.1.3 or later. It also requires the PHP extensions listed in the [technical requirements](https://symfony.com/doc/4.4/setup.html "https://symfony.com/doc/4.4/setup.html ") topic in the official Symfony installation documentation. In this tutorial, we use PHP 7.2 and the corresponding Elastic Beanstalk
[platform version](../platforms/platforms-supported.md#platforms-supported.PHP "../platforms/platforms-supported.md#platforms-supported.PHP"). Before you proceed, you must install both PHP and Composer.

For Symfony support and maintenance information, see the [symfony releases](https://symfony.com/releases "https://symfony.com/releases") topic on the Symfony
website. For more information about updates related to PHP version support for Symfony 4.4.9, see the [Symfony 4.4.9 release notes](https://symfony.com/blog/symfony-4-4-9-released "https://symfony.com/blog/symfony-4-4-9-released") topic on the Symfony website.

## Launch an Elastic Beanstalk environment

Use the Elastic Beanstalk console to create an Elastic Beanstalk environment. Choose the **PHP** platform and accept the default settings and sample
code.

###### To launch an environment (console)

1. Open the Elastic Beanstalk console using this preconfigured link: [console.aws.amazon.com/elasticbeanstalk/home#/newApplication?applicationName=tutorials&environmentType=LoadBalanced](https://console.aws.amazon.com/elasticbeanstalk/home#/newApplication?applicationName=tutorials&environmentType=LoadBalanced "https://console.aws.amazon.com/elasticbeanstalk/home#/newApplication?applicationName=tutorials&environmentType=LoadBalanced")
2. For **Platform**, select the platform and platform branch that match the language used by your application.
3. For **Application code**, choose **Sample application**.
4. Choose **Review and launch**.
5. Review the available options. Choose the available option you want to use, and when you're ready, choose **Create app**.

Environment creation takes about 5 minutes and creates the following resources:

- **EC2 instance** – An Amazon Elastic Compute Cloud (Amazon EC2) virtual
  machine configured to run web apps on the platform that you choose.

Each platform runs a specific set of software, configuration files, and scripts to support a specific language version, framework, web container, or
combination of these. Most platforms use either Apache or NGINX as a reverse proxy that sits in front of your web app, forwards requests to it, serves
static assets, and generates access and error logs.

- **Instance security group** – An Amazon EC2 security group configured to allow inbound traffic on port 80. This
  resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic isn't allowed on other ports.
- **Load balancer** – An Elastic Load Balancing load balancer configured to distribute requests to the instances running your
  application. A load balancer also eliminates the need to expose your instances directly to the internet.
- **Load balancer security group** – An Amazon EC2 security group configured to allow inbound traffic on port 80. This
  resource lets HTTP traffic from the internet reach the load balancer. By default, traffic isn't allowed on other ports.
- **Auto Scaling group** – An Auto Scaling group configured to replace
  an instance if it is terminated or becomes unavailable.
- **Amazon S3 bucket** – A storage location for your source
  code, logs, and other artifacts that are created when you use Elastic Beanstalk.
- **Amazon CloudWatch alarms** – Two CloudWatch alarms that monitor the load on the instances in your environment and that are
  triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
- **CloudFormation stack** – Elastic Beanstalk uses CloudFormation to launch the
  resources in your environment and propagate configuration changes. The resources are defined
  in a template that you can view in the [CloudFormation
  console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
- **Domain name** – A domain name that routes to your
  web app in the form
  _`subdomain`.`region`.elasticbeanstalk.com_.

###### Domain security

To augment the security of your Elastic Beanstalk applications, the _elasticbeanstalk.com_ domain is registered in the
[Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/").

If you ever need to set sensitive cookies in the default domain name for your Elastic Beanstalk applications, we recommend that you use cookies with a
`__Host-` prefix for increased security. This practice defends your domain against cross-site request forgery attempts (CSRF). For more
information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla
Developer Network.

All of these resources are managed by Elastic Beanstalk. When you terminate your environment, Elastic Beanstalk terminates all the resources that it contains.

###### Note

The Amazon S3 bucket that Elastic Beanstalk creates is shared between environments and is not deleted during environment termination. For more information, see [Using Elastic Beanstalk with Amazon S3](AWSHowTo.md "AWSHowTo.md").

## Install Symfony and generate a website

Composer can install Symfony and create a working project with one command:

```
~$ `composer create-project symfony/website-skeleton eb-symfony`
```

Composer installs Symfony and its dependencies, and generates a default project.

If you run into any issues installing Symfony, go to the [installation](https://symfony.com/doc/4.4/setup.html "https://symfony.com/doc/4.4/setup.html") topic in the
official Symfony documentation.

## Deploy your application

Go to the project directory.

```
~$ `cd eb-symfony`
```

Create a [source bundle](applications-sourcebundle.md "applications-sourcebundle.md") containing the files created by Composer. The following command creates a
source bundle named `symfony-default.zip`. It excludes files in the `vendor` folder, which take up a lot of space
and are not necessary for deploying your application to Elastic Beanstalk.

```
eb-symfony$ `zip ../symfony-default.zip -r * .[^.]* -x "vendor/*"`
```

Upload the source bundle to Elastic Beanstalk to deploy Symfony to your environment.

###### To deploy a source bundle

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. On the environment overview page, choose **Upload and deploy**.
4. Use the on-screen dialog box to upload the source bundle.
5. Choose **Deploy**.
6. When the deployment completes, you can choose the site URL to open your website in a new tab.

###### Note

To optimize the source bundle further, initialize a Git repository and use the [git
archive command](applications-sourcebundle.md#using-features.deployment.source.git "applications-sourcebundle.md#using-features.deployment.source.git") to create the source bundle. The default Symfony project includes a `.gitignore` file that tells
Git to exclude the `vendor` folder and other files that are not required for deployment.

## Configure Composer settings

When the deployment completes, click the URL to open your Symfony application in the browser.

What's this? By default, Elastic Beanstalk serves the root of your project at the root path of the web site. In this case, though, the default page
(`app.php`) is one level down in the `web` folder. You can verify this by adding `/public` to
the URL. For example,
`http://`symfony`.`us-east-2`.elasticbeanstalk.com/public`.

To serve the Symfony application at the root path, use the Elastic Beanstalk console to configure the _document root_ for the web site.

###### To configure your web site's document root

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.
5. For **Document root**, enter `/public`.
6. To save the changes choose **Apply** at the bottom of the page.
7. When the update is complete, click the URL to reopen your site in the browser.

## Cleanup

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

## Next steps

For more information about Symfony, see [What is Symfony?](https://symfony.com/what-is-symfony "https://symfony.com/what-is-symfony") at symfony.com.

As you continue to develop your application, you'll probably want a way to manage environments and deploy your application without manually creating a
.zip file and uploading it to the Elastic Beanstalk console. The [Elastic Beanstalk Command Line Interface](eb-cli3.md "eb-cli3.md") (EB CLI) provides easy-to-use commands
for creating, configuring, and deploying applications to Elastic Beanstalk environments from the command line.

In this tutorial, you used the Elastic Beanstalk console to configure composer options. To make this configuration part of your application source, you can use a
configuration file like the following.

###### Example.ebextensions/composer.config

```
option_settings:
  aws:elasticbeanstalk:container:php:phpini:
    document_root: /public
```

For more information, see [Advanced environment customization with configuration files (.ebextensions)](ebextensions.md "ebextensions.md").

Symfony uses its own configuration files to configure database connections. For instructions on connecting to a database with Symfony, see [Connecting to a database with Symfony](create_deploy_PHP.md#php-rds-symfony "create_deploy_PHP.md#php-rds-symfony").

Finally, if you plan on using your application in a production environment, you will want to [configure a custom domain
name](customdomains.md "customdomains.md") for your environment and [enable HTTPS](configuring-https.md "configuring-https.md") for secure connections.
