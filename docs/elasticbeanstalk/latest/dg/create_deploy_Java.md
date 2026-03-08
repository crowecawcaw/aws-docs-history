# Deploying Java applications with Elastic Beanstalk

This chapter provides instructions for configuring and deploying your Java applications to AWS Elastic Beanstalk. Elastic Beanstalk makes it easy to deploy, manage, and scale
your Java web applications using Amazon Web Services.

You can deploy your application in just a few minutes using the Elastic Beanstalk Command Line Interface (EB CLI) or by using the Elastic Beanstalk console. After you deploy
your Elastic Beanstalk application, you can continue to use the EB CLI to manage your application and environment, or you can use the Elastic Beanstalk console, AWS CLI, or the
APIs.

Follow the [QuickStart for Java](java-quickstart.md "java-quickstart.md") for step-by-step instructions to create and deploy a _Hello
World_ Java web application with the EB CLI. If you're interested in step-by-step instructions to create a simple _Hello
World_ Java JSP application to deploy with the EB CLI to our Tomcat based platform, try the [QuickStart for Java on Tomcat](tomcat-quickstart.md "tomcat-quickstart.md").

###### The Java platform branches

AWS Elastic Beanstalk supports two platforms for Java applications.

- Tomcat – A platform based on _Apache Tomcat_, an open source web container for applications
  that use Java servlets and JavaServer Pages (JSPs) to serve HTTP requests. Tomcat facilitates web application development by providing multithreading,
  declarative security configuration, and extensive customization. Elastic Beanstalk has platform branches for each of Tomcat's current major versions. For more
  information, see [The Tomcat platform](java-tomcat-platform.md "java-tomcat-platform.md").
- Java SE – A platform for applications that don't use a web container, or use one other than Tomcat, such as
  Jetty or GlassFish. You can include any library Java Archives (JARs) used by your application in the source bundle that you deploy to Elastic Beanstalk. For more
  information, see [The Java SE platform](java-se-platform.md "java-se-platform.md").
  Recent branches of both the Tomcat and Java SE platforms are based on Amazon Linux 2 and later, and use _Corretto_—the AWS Java SE
  distribution. The names of these platform branches include the word _Corretto_ instead of _Java_.

For a list of current platform versions, see [Tomcat](../platforms/platforms-supported.md#platforms-supported.java "../platforms/platforms-supported.md#platforms-supported.java") and [Java SE](../platforms/platforms-supported.md#platforms-supported.javase "../platforms/platforms-supported.md#platforms-supported.javase") in the _AWS Elastic Beanstalk Platforms_
guide.

###### AWS tools

AWS provides several tools for working with Java and Elastic Beanstalk. Regardless of the platform branch that you choose, you can use the [AWS SDK for Java](java-development-environment.md#java-development-environment-sdk "java-development-environment.md#java-development-environment-sdk") to use other AWS services from within your Java application. The AWS SDK for
Java is a set of libraries that allow you to use AWS APIs from your application code without writing the raw HTTP calls from scratch.

If you prefer to manage your applications from the command line, install the [Elastic Beanstalk Command Line Interface](eb-cli3.md "eb-cli3.md") (EB
CLI) and use it to create, monitor, and manage your Elastic Beanstalk environments. If you run multiple environments for your application, the EB CLI integrates with
Git to let you associate each of your environments with a different Git branch.

###### Topics

- [QuickStart: Deploy a Java application to Elastic Beanstalk](java-quickstart.md "java-quickstart.md")
- [QuickStart: Deploy a Java JSP web application for Tomcat to Elastic Beanstalk](tomcat-quickstart.md "tomcat-quickstart.md")
- [Setting up your Java development environment](java-development-environment.md "java-development-environment.md")
- [More Elastic Beanstalk example applications and tutorials for Java](java-getstarted.md "java-getstarted.md")
- [Using the Elastic Beanstalk Tomcat platform](java-tomcat-platform.md "java-tomcat-platform.md")
- [Using the Elastic Beanstalk Java SE platform](java-se-platform.md "java-se-platform.md")
- [Adding an Amazon RDS DB instance to your Java Elastic Beanstalk environment](java-rds.md "java-rds.md")
- [Java tools and resources](create_deploy_Java.md "create_deploy_Java.md")
