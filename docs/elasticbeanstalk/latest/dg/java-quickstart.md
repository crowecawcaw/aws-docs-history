

# QuickStart: Deploy a Java application to Elastic Beanstalk
<a name="java-quickstart"></a>

This QuickStart tutorial walks you through the process of creating a Java application and deploying it to an AWS Elastic Beanstalk environment.

**Not for production use**  
Examples are intended for demonstration only. Do not use example applications in production.

**Topics**
+ [Your AWS account](#java-quickstart-aws-account)
+ [Prerequisites](#java-quickstart-prereq)
+ [Step 1: Create a Java application](#java-quickstart-create-app)
+ [Step 2: Run your application locally](#java-quickstart-run-local)
+ [Step 3: Deploy your Java application with the EB CLI](#java-quickstart-deploy)
+ [Step 4: Run your application on Elastic Beanstalk](#java-quickstart-run-eb-ap)
+ [Step 5: Clean up](#java-tutorial-cleanup)
+ [AWS resources for your application](#java-quickstart-eb-resources)
+ [Next steps](#java-quickstart-next-steps)
+ [Deploy with the Elastic Beanstalk console](#java-quickstart-console)

## Your AWS account
<a name="java-quickstart-aws-account"></a>

If you're not already an AWS customer, you need to create an AWS account. Signing up enables you to access Elastic Beanstalk and other AWS services that you need.

If you already have an AWS account, you can move on to [Prerequisites](#java-quickstart-prereq).

### Create an AWS account
<a name="java-quickstart-aws-account-procedure"></a>

#### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="java-quickstart-prereq"></a>

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in listings preceded by a prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ this is a command
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.

### EB CLI
<a name="java-quickstart-prereq.ebcli"></a>

This tutorial uses the Elastic Beanstalk Command Line Interface (EB CLI). For details on installing and configuring the EB CLI, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install)and [Configure the EB CLI](eb-cli3-configuration.md).

### Java and Maven
<a name="java-quickstart-prereq.runtime"></a>

If you don't have Amazon Corretto installed on your local machine, you can install it by following the [ installation instructions](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/amazon-linux-install.html) in the *Amazon Corretto User Guide*.

Verify your Java installation by running the following command.

```
~$ java -version 
```

This tutorial uses Maven. Follow the [download](https://maven.apache.org/download.cgi) and [installation](https://maven.apache.org/install.html) instructions on the Apache Maven Project website. For more information about Maven see the [Maven Users Centre](https://maven.apache.org/users/index.html) on the Apache Maven Project website.

Verify your Maven installation by running the following command.

```
~$ mvn -v
```

## Step 1: Create a Java application
<a name="java-quickstart-create-app"></a>

Create a project directory.

```
~$ mkdir eb-java
~$ cd eb-java
```

Next, create an application that you'll deploy using Elastic Beanstalk. We'll create a "Hello World" RESTful web service.

This example uses the [Spring Boot](https://spring.io/projects/spring-boot) framework. This application opens a listener on port 5000. Elastic Beanstalk forward requests to your application on port 5000 by default.

Create the following files:

This file creates a simple Spring Boot application.

**Example `~/eb-java/src/main/java/com/example/Application.java`**  

```
package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

This file creates a mapping that returns a String that we define here.

**Example `~/eb-java/src/main/java/com/example/Controller.java`**  

```
package com.example;
    
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
    
@RestController
public class Controller {
    
    @GetMapping("/")
    public String index() {
       return "Hello Elastic Beanstalk!";
    }
}
```

This file defines the Maven project configuration.

**Example `~/eb-java/pom.xml`**  

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.3</version>
  </parent>

  <groupId>com.example</groupId>
  <artifactId>BeanstalkJavaExample</artifactId>
  <version>1.0-SNAPSHOT</version>

  <properties>
    <java.version>21</java.version>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
      </plugin>
    </plugins>
  </build>

</project>
```

This properties file overrides the default port to be 5000. This is the default port that Elastic Beanstalk sends traffic to for Java applications.

**Example `~/eb-java/application.properties`**  

```
server.port=5000
```

## Step 2: Run your application locally
<a name="java-quickstart-run-local"></a>

Package your application with the following command:

```
~/eb-java$ mvn clean package
```

Run your application locally with the following command:

```
~/eb-java$ java -jar target/BeanstalkJavaExample-1.0-SNAPSHOT.jar
```

While the application is running, navigate to `http://127.0.0.1:5000/` in your browser. You should see the text “Hello Elastic Beanstalk\!”.

## Step 3: Deploy your Java application with the EB CLI
<a name="java-quickstart-deploy"></a>

Before deploying your Java application to Elastic Beanstalk, let’s clean the build application from your directory and create a [Buildfile](java-se-buildfile.md) and a [Procfile](java-se-procfile.md) to control how the application is built and run on your Elastic Beanstalk environment.

**To prepare and configure for application deployment**

1. Clean the built application.

   ```
   ~/eb-java$ mvn clean
   ```

1. Create your `Buildfile`.  
**Example `~/eb-java/Buildfile`**  

   ```
   build: mvn clean package
   ```

   This `Buildfile` specifies the command used to build your application. If you don’t include a `Buildfile` for a Java application, Elastic Beanstalk doesn't attempt to build your application.

1. Create your `Procfile`.  
**Example `~/eb-java/Procfile`**  

   ```
   web: java -jar target/BeanstalkJavaExample-1.0-SNAPSHOT.jar
   ```

   This `Procfile` specifies the command used to run your application. If you don’t include a `Procfile` for a Java application, Elastic Beanstalk assumes there is one JAR file in the root of your source bundle and tries to run it with the `java -jar` command.

 Now that you have set up the configuration files to build and start your application, you're ready to deploy it. 

**To create an environment and deploy your Java application**

1. Initialize your EB CLI repository with the **eb init** command. 

   ```
   ~/eb-java eb init -p corretto java-tutorial --region {{us-east-2}}
           
   Application java-tutorial has been created.
   ```

   This command creates an application named `java-tutorial` and configures your local repository to create environments with the latest Java platform version.

1. (Optional) Run **eb init** again to configure a default key pair so that you can use SSH to connect to the EC2 instance running your application.

   ```
   ~/eb-java$ eb init
   Do you want to set up SSH for your instances?
   (y/n): y
   Select a keypair.
   1) my-keypair
   2) [ Create new KeyPair ]
   ```

   Select a key pair if you have one already, or follow the prompts to create one. If you don't see the prompt or need to change your settings later, run **eb init -i**.

1. Create an environment and deploy your application to it with **eb create**. Elastic Beanstalk automatically builds a zip file for your application and starts it on port 5000.

   ```
   ~/eb-java$ eb create java-env
   ```

   It takes about five minutes for Elastic Beanstalk to create your environment.

## Step 4: Run your application on Elastic Beanstalk
<a name="java-quickstart-run-eb-ap"></a>

When the process to create your environment completes, open your website with **eb open**.

```
~/eb-java eb open
```

Congratulations\! You've deployed a Java application with Elastic Beanstalk\! This opens a browser window using the domain name created for your application.

## Step 5: Clean up
<a name="java-tutorial-cleanup"></a>

You can terminate your environment when you finish working with your application. Elastic Beanstalk terminates all AWS resources associated with your environment.

To terminate your Elastic Beanstalk environment with the EB CLI run the following command.

```
~/eb-java$ eb terminate
```

## AWS resources for your application
<a name="java-quickstart-eb-resources"></a>

You just created a single instance application. It serves as a straightforward sample application with a single EC2 instance, so it doesn't require load balancing or auto scaling. For single instance applications Elastic Beanstalk creates the following AWS resources:
+ **EC2 instance** – An Amazon EC2 virtual machine configured to run web apps on the platform you choose.

  Each platform runs a different set of software, configuration files, and scripts to support a specific language version, framework, web container, or combination thereof. Most platforms use either Apache or nginx as a reverse proxy that processes web traffic in front of your web app, forwards requests to it, serves static assets, and generates access and error logs.
+ **Instance security group** – An Amazon EC2 security group configured to allow incoming traffic on port 80. This resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic is not allowed on other ports.
+ **Amazon S3 bucket** – A storage location for your source code, logs, and other artifacts that are created when you use Elastic Beanstalk.
+ **Amazon CloudWatch alarms** – Two CloudWatch alarms that monitor the load on the instances in your environment and are triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
+ **CloudFormation stack** – Elastic Beanstalk uses CloudFormation to launch the resources in your environment and propagate configuration changes. The resources are defined in a template that you can view in the [CloudFormation console](https://console.aws.amazon.com/cloudformation).
+  **Domain name** – A domain name that routes to your web app in the form *{{subdomain}}.{{region}}.elasticbeanstalk.com*. 

Elastic Beanstalk manages all of these resources. When you terminate your environment, Elastic Beanstalk terminates all the resources that it contains.

## Next steps
<a name="java-quickstart-next-steps"></a>

After you have an environment running an application, you can deploy a new version of the application or a different application at any time. Deploying a new application version is very quick because it doesn't require provisioning or restarting EC2 instances. You can also explore your new environment using the Elastic Beanstalk console. For detailed steps, see [Explore your environment](GettingStarted.md#GettingStarted.Explore) in the *Getting started* chapter of this guide.

**Try more tutorials**  
If you'd like to try other tutorials with different example applications, see [Sample applications and tutorials](java-getstarted.md).

After you deploy a sample application or two and are ready to start developing and running Java applications locally, see [Setting up your Java development environment](java-development-environment.md). 

## Deploy with the Elastic Beanstalk console
<a name="java-quickstart-console"></a>

You can also use the Elastic Beanstalk console to launch the sample application. For detailed steps, see [Create an example application](GettingStarted.md#GettingStarted.CreateApp) in the *Getting started* chapter of this guide.