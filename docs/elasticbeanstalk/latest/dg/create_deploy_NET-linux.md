# Managing your Elastic Beanstalk application environments

This section describes the specific service settings you can edit in the AWS
Toolkit for Visual Studio as part of your application environment configuration. With the AWS Toolkit for Visual Studio and the AWS Management Console, you can change the provisioning and configuration of the AWS resources used by
your application environments. For information on how to manage your application environments using the AWS Management Console, see [Creating environments in Elastic Beanstalk](using-features.md "using-features.md").

## Changing environment configurations settings

When you deploy your application, Elastic Beanstalk configures several connected AWS cloud computing services. You can control how these individual services are
configured by using the AWS Toolkit for Visual Studio.

###### To edit an application's environment settings

1. In Visual Studio, on the **File** menu, choose **AWS Explorer**.
2. Expand the Elastic Beanstalk node and your application node. Open the context (right-click) menu for your application environment and select **View
   Status**.

You can now configure settings for the following:

    * AWS X-Ray
    * Server
    * Load Balancer (only applies to multiple-instance environments)
    * Auto Scaling (only applies to multiple-instance environments)
    * Notifications
    * Container
    * Advanced Configuration Options
