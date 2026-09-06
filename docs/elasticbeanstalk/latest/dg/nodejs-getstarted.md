

# More Elastic Beanstalk example applications and tutorials for Node.js
<a name="nodejs-getstarted"></a>

This section provides additional applications and tutorials. The [QuickStart for Node.js](nodejs-quickstart.md) topic located previously in this topic walks you through launching the sample Node.js application with the EB CLI.

 To get started with Node.js applications on AWS Elastic Beanstalk, all you need is an application [source bundle](applications-sourcebundle.md) to upload as your first application version and to deploy to an environment. 

## Launching an environment with a sample Node.js application
<a name="nodejs-getstarted-samples"></a>

Elastic Beanstalk provides single page sample applications for each platform as well as more complex examples that show the use of additional AWS resources such as Amazon RDS and language or platform-specific features and APIs.

**Note**  
Follow the steps in the source bundle `README.md` file to deploy it. 


**Samples**  

|  Environment type  |  Source bundle  |  Description  | 
| --- | --- | --- | 
| Web Server |  [nodejs.zip](samples/nodejs.zip)  | Single page application.<br />To launch the sample application with the EB CLI, see [QuickStart for Node.js](nodejs-quickstart.md).<br />You can also use the Elastic Beanstalk console to launch the sample application. For detailed steps, see [Create an example application](GettingStarted.md#GettingStarted.CreateApp) in the *Getting started* chapter of this guide. | 
| Web Server with Amazon RDS | [nodejs-example-express-rds.zip](samples/nodejs-example-express-rds.zip) | Hiking log application that uses the Express framework and an Amazon Relational Database Service (RDS).<br />[Tutorial](create_deploy_nodejs_express.md) | 
| Web Server with Amazon ElastiCache | [nodejs-example-express-elasticache.zip](samples/nodejs-example-express-elasticache.zip) | Express web application that uses Amazon ElastiCache for clustering. Clustering enhances your web application's high availability, performance, and security.<br />[Tutorial](nodejs-express-clustering.md) | 
| Web Server with DynamoDB, Amazon SNS and Amazon SQS | [nodejs-example-dynamo.zip](samples/nodejs-example-dynamo.zip) | Express web site that collects user contact information for a new company's marketing campaign. Uses the AWS SDK for JavaScript in Node.js to write entries to a DynamoDB table, and Elastic Beanstalk configuration files to create resources in DynamoDB, Amazon SNS and Amazon SQS.<br />[Tutorial](nodejs-dynamodb-tutorial.md) | 

## Next steps
<a name="nodejs-getstarted-next"></a>

After you have an environment running an application, you can deploy a new version of the application or a completely different application at any time. Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. For details about application deployment, see [Deploy a New Version of Your Application](GettingStarted.md#GettingStarted.DeployApp).

After you've deployed a sample application or two and are ready to start developing and running Node.js applications locally, see [Setting up your Node.js development environment for Elastic Beanstalk](nodejs-devenv.md) to set up a Node.js development environment with all of the tools that you will need.