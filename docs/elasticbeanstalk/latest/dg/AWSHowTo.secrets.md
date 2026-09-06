

# Using Elastic Beanstalk with AWS Secrets Manager and AWS Systems Manager Parameter Store
<a name="AWSHowTo.secrets"></a>

This topic explains how you can use AWS Secrets Manager and AWS Systems Manager Parameter Store with your Elastic Beanstalk environment to securely store and retrieve sensitive information, such as credentials and API keys. Your application can retrieve stored secrets and parameters directly from these stores, using the APIs or command line tools of these services. 

Elastic Beanstalk also offers the ability to reference Secrets Manager and Systems Manager Parameter Store data in environment variables. This is a secure option for your application to natively access secrets and parameters stored by these services without having to manage API calls to them.

**Topics**
+ [Fetching secrets and parameters to Elastic Beanstalk environment variables](AWSHowTo.secrets.env-vars.md)
+ [Required IAM permissions for Elastic Beanstalk to access secrets and parameters](AWSHowTo.secrets.IAM-permissions.md)
+ [Using AWS Secrets Manager and AWS Systems Manager Parameter Store](AWSHowTo.secrets.Secrets-Manager-and-Parameter-Store.md)
+ [Troubleshooting secrets integration with Elastic Beanstalk environment variables](AWSHowTo.secrets.troubleshoot.md)