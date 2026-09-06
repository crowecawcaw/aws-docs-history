

# Deploying a Node.js application with DynamoDB to Elastic Beanstalk
<a name="nodejs-dynamodb-tutorial"></a>

This tutorial and its example application [nodejs-example-dynamo.zip](samples/nodejs-example-dynamo.zip) walks you through the process of deploying a Node.js application that uses the AWS SDK for JavaScript in Node.js to interact with the Amazon DynamoDB service. You'll create a DynamoDB table that's in a database that's decoupled, or external, from the AWS Elastic Beanstalk environment. You'll also configure the application to use a decoupled database. In a production environment, it's best practice to use a database that's decoupled from the Elastic Beanstalk environment so that it's independent from the environment's life cycle. This practice also enables you to perform [blue/green deployments](using-features.CNAMESwap.md).

The example application illustrates the following:
+ A DynamoDB table that stores user-provided text data.
+ The [configuration files](ebextensions.md) to create the table.
+ An Amazon Simple Notification Service topic.
+  Use of a [package.json file](nodejs-platform-dependencies.md#nodejs-platform-packagejson) to install packages during deployment.

**Topics**
+ [Prerequisites](#nodejs-dynamodb-tutorial-prereqs)
+ [Create an Elastic Beanstalk environment](#nodejs-dynamodb-tutorial-launch)
+ [Add permissions to your environment's instances](#nodejs-dynamodb-tutorial-role)
+ [Deploy the example application](#nodejs-dynamodb-tutorial-deploy)
+ [Create a DynamoDB table](#nodejs-dynamodb-tutorial-database)
+ [Update the application's configuration files](#nodejs-dynamodb-tutorial-update)
+ [Configure your environment for high availability](#nodejs-dynamodb-tutorial-configure)
+ [Cleanup](#nodejs-dynamodb-tutorial-cleanup)
+ [Next steps](#nodejs-dynamodb-tutorial-nextsteps)

## Prerequisites
<a name="nodejs-dynamodb-tutorial-prereqs"></a>

This tutorial requires the following prerequisites:
+ The Node.js runtimes
+ The default Node.js package manager software, npm
+ The Express command line generator
+ The Elastic Beanstalk Command Line Interface (EB CLI)

For details about installing the first three listed components and setting up your local development environment, see [Setting up your Node.js development environment for Elastic Beanstalk](nodejs-devenv.md). For this tutorial, you don't need to install the AWS SDK for Node.js, which is also mentioned in the referenced topic.

For details about installing and configuring the EB CLI, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install) and [Configure the EB CLI](eb-cli3-configuration.md).

## Create an Elastic Beanstalk environment
<a name="nodejs-dynamodb-tutorial-launch"></a>

**Your application directory**  
This tutorial uses a directory called `nodejs-example-dynamo` for the application source bundle. Create the `nodejs-example-dynamo` directory for this tutorial.

```
~$ mkdir nodejs-example-dynamo
```

**Note**  
Each tutorial in this chapter uses it's own directory for the application source bundle. The directory name matches the name of the sample application used by the tutorial.

Change your current working directory to `nodejs-example-dynamo`.

```
~$ cd nodejs-example-dynamo
```

Now, let's set up an Elastic Beanstalk environment running the Node.js platform and the sample application. We'll use the Elastic Beanstalk command line interface (EB CLI).

**To configure an EB CLI repository for your application and create an Elastic Beanstalk environment running the Node.js platform**

1. Create a repository with the **[**eb init**](eb3-init.md)** command.

   ```
   ~/nodejs-example-dynamo$ eb init --platform {{node.js}} --region {{<region>}}
   ```

   This command creates a configuration file in a folder named `.elasticbeanstalk` that specifies settings for creating environments for your application, and creates an Elastic Beanstalk application named after the current folder.

1. Create an environment running a sample application with the **[**eb create**](eb3-create.md)** command.

   ```
   ~/nodejs-example-dynamo$ eb create --sample {{nodejs-example-dynamo}}
   ```

   This command creates a load-balanced environment with the default settings for the Node.js platform and the following resources:
   + **EC2 instance** – An Amazon Elastic Compute Cloud (Amazon EC2) virtual machine configured to run web apps on the platform that you choose.

     Each platform runs a specific set of software, configuration files, and scripts to support a specific language version, framework, web container, or combination of these. Most platforms use either Apache or NGINX as a reverse proxy that sits in front of your web app, forwards requests to it, serves static assets, and generates access and error logs.
   + **Instance security group** – An Amazon EC2 security group configured to allow inbound traffic on port 80. This resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic isn't allowed on other ports.
   + **Load balancer** – An Elastic Load Balancing load balancer configured to distribute requests to the instances running your application. A load balancer also eliminates the need to expose your instances directly to the internet.
   + **Load balancer security group** – An Amazon EC2 security group configured to allow inbound traffic on port 80. This resource lets HTTP traffic from the internet reach the load balancer. By default, traffic isn't allowed on other ports.
   + **Auto Scaling group** – An Auto Scaling group configured to replace an instance if it is terminated or becomes unavailable.
   + **Amazon S3 bucket** – A storage location for your source code, logs, and other artifacts that are created when you use Elastic Beanstalk.
   + **Amazon CloudWatch alarms** – Two CloudWatch alarms that monitor the load on the instances in your environment and that are triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
   + **CloudFormation stack** – Elastic Beanstalk uses CloudFormation to launch the resources in your environment and propagate configuration changes. The resources are defined in a template that you can view in the [CloudFormation console](https://console.aws.amazon.com/cloudformation).
   + **Domain name** – A domain name that routes to your web app in the form *{{subdomain}}.{{region}}.elasticbeanstalk.com*.
**Domain security**  
To augment the security of your Elastic Beanstalk applications, the *elasticbeanstalk.com* domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/).  
If you ever need to set sensitive cookies in the default domain name for your Elastic Beanstalk applications, we recommend that you use cookies with a `__Host-` prefix for increased security. This practice defends your domain against cross-site request forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes) page in the Mozilla Developer Network.

1. When environment creation completes, use the [**eb open**](eb3-open.md) command to open the environment's URL in the default browser.

   ```
   ~/nodejs-example-dynamo$ eb open
   ```

You have now created a Node.js Elastic Beanstalk environment with a sample application. You can update it with your own application. Next, we update the sample application to use the Express framework.

## Add permissions to your environment's instances
<a name="nodejs-dynamodb-tutorial-role"></a>

Your application runs on one or more EC2 instances behind a load balancer, serving HTTP requests from the Internet. When it receives a request that requires it to use AWS services, the application uses the permissions of the instance it runs on to access those services.

The sample application uses instance permissions to write data to a DynamoDB table, and to send notifications to an Amazon SNS topic with the SDK for JavaScript in Node.js. Add the following managed policies to the default [instance profile](concepts-roles-instance.md) to grant the EC2 instances in your environment permission to access DynamoDB and Amazon SNS:
+ **AmazonDynamoDBFullAccess**
+ **AmazonSNSFullAccess**

**To add policies to the default instance profile**

1. Open the [Roles page](https://console.aws.amazon.com/iam/home#roles) in the IAM console.

1. Choose **aws-elasticbeanstalk-ec2-role**.

1. On the **Permissions** tab, choose **Attach policies**.

1. Select the managed policy for the additional services that your application uses. For this tutorial, select `AmazonSNSFullAccess` and `AmazonDynamoDBFullAccess`.

1. Choose **Attach policy**.

See [Managing Elastic Beanstalk instance profiles](iam-instanceprofile.md) for more on managing instance profiles.

## Deploy the example application
<a name="nodejs-dynamodb-tutorial-deploy"></a>

Now your environment is ready for you to deploy and run the example application for this tutorial: [nodejs-example-dynamo.zip](samples/nodejs-example-dynamo.zip) .

**To deploy and run the tutorial example application**

1. Change your current working directory to the application directory `nodejs-example-dynamo`.

   ```
   ~$ cd nodejs-example-dynamo
   ```

1. Download and extract the contents of the example application source bundle [nodejs-example-dynamo.zip](samples/nodejs-example-dynamo.zip) to the application directory `nodejs-example-dynamo`.

1. Deploy the example application to your Elastic Beanstalk environment with the [**eb deploy**](eb3-deploy.md) command.

   ```
   ~/nodejs-example-dynamo$ eb deploy
   ```
**Note**  
By default, the `eb deploy` command creates a ZIP file of your project folder. You can configure the EB CLI to deploy an artifact from your build process instead of creating a ZIP file of your project folder. For more information, see [Deploying an artifact instead of the project folder](eb-cli3-configuration.md#eb-cli3-artifact).

1. When environment creation completes, use the [**eb open**](eb3-open.md) command to open the environment's URL in the default browser.

   ```
   ~/nodejs-example-dynamo$ eb open
   ```

The site collects user contact information and uses a DynamoDB table to store the data. To add an entry, choose **Sign up today**, enter a name and email address, and then choose **Sign Up\!**. The web app writes the form contents to the table and triggers an Amazon SNS email notification.

![Startup landing page with teaser message and sign-up button for upcoming product launch.](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/nodejs-dynamodb-tutorial-app.png)


Right now, the Amazon SNS topic is configured with a placeholder email for notifications. You will update the configuration soon, but in the meantime you can verify the DynamoDB table and Amazon SNS topic in the AWS Management Console.

**To view the table**

1. Open the [Tables page](https://console.aws.amazon.com/dynamodb/home?#tables:) in the DynamoDB console.

1. Find the table that the application created. The name starts with **awseb** and contains **StartupSignupsTable**.

1. Select the table, choose **Items**, and then choose **Start search** to view all items in the table.

The table contains an entry for every email address submitted on the signup site. In addition to writing to the table, the application sends a message to an Amazon SNS topic that has two subscriptions, one for email notifications to you, and another for an Amazon Simple Queue Service queue that a worker application can read from to process requests and send emails to interested customers.

**To view the topic**

1. Open the [Topics page](https://console.aws.amazon.com/sns/v2/home?#/topics) in the Amazon SNS console.

1. Find the topic that the application created. The name starts with **awseb** and contains **NewSignupTopic**.

1. Choose the topic to view its subscriptions.

The application (`[app.js](https://github.com/awslabs/eb-node-express-sample/blob/master/app.js)`) defines two routes. The root path (`/`) returns a webpage rendered from an Embedded JavaScript (EJS) template with a form that the user fills out to register their name and email address. Submitting the form sends a POST request with the form data to the `/signup` route, which writes an entry to the DynamoDB table and publishes a message to the Amazon SNS topic to notify the owner of the signup.

The sample application includes [configuration files](ebextensions.md) that create the DynamoDB table, Amazon SNS topic, and Amazon SQS queue used by the application. This lets you create a new environment and test the functionality immediately, but has the drawback of tying the DynamoDB table to the environment. For a production environment, you should create the DynamoDB table outside of your environment to avoid losing it when you terminate the environment or update its configuration.

## Create a DynamoDB table
<a name="nodejs-dynamodb-tutorial-database"></a>

To use an external DynamoDB table with an application running in Elastic Beanstalk, first create a table in DynamoDB. When you create a table outside of Elastic Beanstalk, it is completely independent of Elastic Beanstalk and your Elastic Beanstalk environments, and will not be terminated by Elastic Beanstalk.

Create a table with the following settings:
+ **Table name** – **nodejs-tutorial**
+ **Primary key** – **email**
+ Primary key type – **String**

**To create a DynamoDB table**

1. Open the [Tables page](https://console.aws.amazon.com/dynamodb/home?#tables:) in the DynamoDB management console.

1. Choose **Create table**.

1. Type a **Table name** and **Primary key**.

1. Choose the primary key type.

1. Choose **Create**.

## Update the application's configuration files
<a name="nodejs-dynamodb-tutorial-update"></a>

Update the [configuration files](ebextensions.md) in the application source to use the **nodejs-tutorial** table instead of creating a new one.

**To update the example application for production use**

1. Change your current working directory to the application directory `nodejs-example-dynamo`.

   ```
   ~$ cd nodejs-example-dynamo
   ```

1. Open `.ebextensions/options.config` and change the values of the following settings:
   + **NewSignupEmail** – Your email address.
   + **STARTUP\_SIGNUP\_TABLE** – **nodejs-tutorial**

     
**Example .ebextensions/options.config**  

   ```
   option_settings:
     aws:elasticbeanstalk:customoption:
       NewSignupEmail: {{you@example.com}}
     aws:elasticbeanstalk:application:environment:
       THEME: "flatly"
       AWS_REGION: '`{"Ref" : "AWS::Region"}`'
       STARTUP_SIGNUP_TABLE: {{nodejs-tutorial}}
       NEW_SIGNUP_TOPIC: '`{"Ref" : "NewSignupTopic"}`'
     aws:elasticbeanstalk:container:nodejs:
       ProxyServer: nginx
     aws:elasticbeanstalk:container:nodejs:staticfiles:
       /static: /static
     aws:autoscaling:asg:
       Cooldown: "120"
     aws:autoscaling:trigger:
       Unit: "Percent"
       Period: "1"
       BreachDuration: "2"
       UpperThreshold: "75"
       LowerThreshold: "30"
       MeasureName: "CPUUtilization"
   ```

   This applies the following configurations for the application:
   + The email address that the Amazon SNS topic uses for notifications is set to your address, or the one you enter in the `options.config` file.
   + The **nodejs-tutorial** table will be used instead of the one created by `.ebextensions/create-dynamodb-table.config`.

1. Remove `.ebextensions/create-dynamodb-table.config`.

   ```
   ~/nodejs-tutorial$ rm .ebextensions/create-dynamodb-table.config
   ```

   The next time you deploy the application, the table created by this configuration file will be deleted.

1. Deploy the updated application to your Elastic Beanstalk environment with the [**eb deploy**](eb3-deploy.md) command.

   ```
   ~/nodejs-example-dynamo$ eb deploy
   ```

1. When environment creation completes, use the [**eb open**](eb3-open.md) command to open the environment's URL in the default browser.

   ```
   ~/nodejs-example-dynamo$ eb open
   ```

When you deploy, Elastic Beanstalk updates the configuration of the Amazon SNS topic and deletes the DynamoDB table that it created when you deployed the first version of the application.

Now, when you terminate the environment, the **nodejs-tutorial** table will not be deleted. This lets you perform blue/green deployments, modify configuration files, or take down your website without risking data loss.

Open your site in a browser and verify that the form works as you expect. Create a few entries, and then check the DynamoDB console to verify the table.

**To view the table**

1. Open the [Tables page](https://console.aws.amazon.com/dynamodb/home?#tables:) in the DynamoDB console.

1. Find the **nodejs-tutorial** table.

1. Select the table, choose **Items**, and then choose **Start search** to view all items in the table.

You can also see that Elastic Beanstalk deleted the table that it created previously.

## Configure your environment for high availability
<a name="nodejs-dynamodb-tutorial-configure"></a>

Finally, configure your environment's Auto Scaling group with a higher minimum instance count. Run at least two instances at all times to prevent the web servers in your environment from being a single point of failure, and to allow you to deploy changes without taking your site out of service.

**To configure your environment's Auto Scaling group for high availability**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. In the navigation pane, choose **Configuration**.

1. In the **Capacity** configuration category, choose **Edit**.

1. In the **Auto Scaling group** section, set **Min instances** to **2**.

1. To save the changes choose **Apply** at the bottom of the page.

## Cleanup
<a name="nodejs-dynamodb-tutorial-cleanup"></a>

After you finish working with the demo code, you can terminate your environment. Elastic Beanstalk deletes all related AWS resources, such as [Amazon EC2 instances](using-features.managing.ec2.md), [database instances](using-features.managing.db.md), [load balancers](using-features.managing.elb.md), security groups, and [alarms](using-features.alarms.md#using-features.alarms.title). 

Removing resources does not delete the Elastic Beanstalk application, so you can create new environments for your application at any time.

**To terminate your Elastic Beanstalk environment from the console**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. Choose **Actions**, and then choose **Terminate environment**.

1. Use the on-screen dialog box to confirm environment termination.

You can also delete the external DynamoDB tables that you created.

**To delete a DynamoDB table**

1. Open the [Tables page](https://console.aws.amazon.com/dynamodb/home?#tables:) in the DynamoDB console.

1. Select a table.

1. Choose **Actions**, and then choose **Delete table**.

1. Choose **Delete**.

## Next steps
<a name="nodejs-dynamodb-tutorial-nextsteps"></a>

The example application uses configuration files to configure software settings and create AWS resources as part of your environment. See [Advanced environment customization with configuration files (`.ebextensions`)](ebextensions.md) for more information about configuration files and their use.

The example application for this tutorial uses the Express web framework for Node.js. For more information about Express, see the official documentation at [expressjs.com](https://expressjs.com).

Finally, if you plan on using your application in a production environment, [configure a custom domain name](customdomains.md) for your environment and [enable HTTPS](configuring-https.md) for secure connections.