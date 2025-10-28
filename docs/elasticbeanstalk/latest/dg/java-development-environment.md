# Setting up your Java development environment

This topic provides instructions to set up a Java development environment to test your application locally prior to deploying it to AWS Elastic Beanstalk.
It also references websites that provide installation instructions for useful tools.

###### Sections

- [Installing the Java development kit](#java-development-environment-jdk "#java-development-environment-jdk")
- [Installing a web container](#java-development-environment-tomcat "#java-development-environment-tomcat")
- [Downloading libraries](#java-development-environment-libraries "#java-development-environment-libraries")
- [Installing the AWS SDK for Java](#java-development-environment-sdk "#java-development-environment-sdk")
- [Installing an IDE or text editor](#java-development-environment-ide "#java-development-environment-ide")

## Installing the Java development kit

Install the Java Development Kit (JDK). If you don't have a preference, get the latest version. Download the JDK at [oracle.com](http://www.oracle.com/technetwork/java/javase/downloads/index.html "http://www.oracle.com/technetwork/java/javase/downloads/index.html")

The JDK includes the Java compiler, which you can use to build your source files into class files that can be executed on an Elastic Beanstalk web server.

## Installing a web container

If you don't already have another web container or framework, install a version of Tomcat that Elastic Beanstalk supports for your Amazon Linux operating system. For a
list of the current versions of Apache Tomcat that Elastic Beanstalk supports, see [Tomcat](../platforms/platforms-supported.md#platforms-supported.java "../platforms/platforms-supported.md#platforms-supported.java") in the _AWS Elastic Beanstalk Platforms_ document. Download the Tomcat version that applies to your environment from the [Apache Tomcat](http://tomcat.apache.org "http://tomcat.apache.org") website.

## Downloading libraries

Elastic Beanstalk platforms include few libraries by default. Download libraries that your application will use and save them in your project folder to deploy in
your application source bundle.

If you've installed Tomcat locally, you can copy the servlet API and JavaServer Pages (JSP) API libraries from the installation folder. If you deploy
to a Tomcat platform version, you don't need to include these files in your source bundle, but you do need to have them in your `classpath` to
compile any classes that use them.

JUnit, Google Guava, and Apache Commons provide several useful libraries. Visit their home pages to learn more:

- [Download JUnit](https://github.com/junit-team/junit/wiki/Download-and-Install "https://github.com/junit-team/junit/wiki/Download-and-Install")
- [Download Google Guava](https://code.google.com/p/guava-libraries/ "https://code.google.com/p/guava-libraries/")
- [Download Apache Commons](http://commons.apache.org/downloads/ "http://commons.apache.org/downloads/")

## Installing the AWS SDK for Java

If you need to manage AWS resources from within your application, install the AWS SDK for Java. For example, with the AWS SDK for Java, you can use
Amazon DynamoDB (DynamoDB) to share session states of Apache Tomcat applications across multiple web servers. For more information, see [Manage Tomcat Session State with Amazon DynamoDB](../../../AWSSdkDocsJava/latest/DeveloperGuide/java-dg-tomcat-session-manager.md "../../../AWSSdkDocsJava/latest/DeveloperGuide/java-dg-tomcat-session-manager.md")
in the AWS SDK for Java documentation.

Visit the [AWS SDK for Java home page](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/") for more information and installation instructions.

## Installing an IDE or text editor

Integrated development environments (IDEs) provide a wide range of features that facilitate application development. If you haven't used an IDE for
Java development, try Eclipse and IntelliJ and see which works best for you.

- [Install Eclipse IDE for Java EE Developers](https://www.eclipse.org/downloads/ "https://www.eclipse.org/downloads/")
- [Install IntelliJ](https://www.jetbrains.com/idea/ "https://www.jetbrains.com/idea/")

An IDE might add files to your project folder that you might not want to commit to source control. To prevent committing these files to source
control, use `.gitignore` or your source control tool's equivalent.

If you just want to begin coding and don't need all of the features of an IDE, consider [installing Sublime
Text](http://www.sublimetext.com/ "http://www.sublimetext.com/").

###### Note

On May 31, 2023, the [AWS Toolkit for Eclipse](../../../toolkit-for-eclipse/v1/user-guide/welcome.md "../../../toolkit-for-eclipse/v1/user-guide/welcome.md") reached end of life and is
no longer supported by AWS. For additional details regarding the end of life cycle for the AWS Toolkit for Eclipse, see the [README.md](https://github.com/aws/aws-toolkit-eclipse "https://github.com/aws/aws-toolkit-eclipse") file on the AWS Toolkit for Eclipse GitHub repository.
