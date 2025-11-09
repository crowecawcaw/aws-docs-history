AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Set up licensed dependencies in AWS Blu Age Runtime on

Amazon EC2

This guide describes how to set up additional licensed dependencies that you can use with
AWS Blu Age Runtime on Amazon EC2.

###### Topics

- [Prerequisites](#ba-runtime-dependencies-prereq "#ba-runtime-dependencies-prereq")
- [Overview](#ba-runtime-dependencies-overview "#ba-runtime-dependencies-overview")
- [Set up the dependencies for JAC and BAC
  webapps](#ba-runtime-dependencies-webapps "#ba-runtime-dependencies-webapps")

## Prerequisites

Before you begin, make sure you complete the following prerequisites.

- Complete [AWS Blu Age Runtime prerequisites](ba-runtime-setup-prereq.md "ba-runtime-setup-prereq.md") and [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") .
- Make sure that you have an Amazon EC2 instance containing the latest AWS Blu Age Runtime (on Amazon EC2). For more
  information, see [Get started with Amazon EC2 Linux instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md").
- Make sure you can connect to the Amazon EC2 instance successfully, for example, by using
  SSM.
- Get the following dependencies from their sources.

### Oracle database

Supply an [Oracle database
driver](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html "https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html"). We tested the AWS Blu Age Runtime (on Amazon EC2) functionality with version **ojdbc11-23.3.0.23.09.jar**, but a more recent version might be compatible.

### IBM MQ connection

Supply an [IBM MQ
client](https://www.ibm.com/support/pages/mqc91-ibm-mq-clients "https://www.ibm.com/support/pages/mqc91-ibm-mq-clients"). We tested the AWS Blu Age Runtime (on Amazon EC2) functionality with version **com.ibm.mq.jakarta.client-9.3.4.1.jar**, but a more recent version might be
compatible.

With this dependency version, also supply the following transitive dependencies:

- bcprov-jdk15to18-1.76.jar
- bcpkix-jdk15to18-1.76.jar
- bcutil-jdk15to18-1.76.jar

### DDS Printer files

Supply the Jasper reports library
(https://community.jaspersoft.com/download-jaspersoft/community-edition). We tested the AWS Blu Age Runtime (on Amazon EC2)
functionality with **jasperreports-6.16.0.jar**, but a more recent
version might be compatible.

With this dependency version, also supply the following transitive dependencies:

- castor-core-1.4.1.jar
- castor-xml-1.4.1.jar
- commons-digester-2.1.jar
- ecj-3.21.0.jar
- itext-2.1.7.js8.jar
- javax.inject-1.jar
- jcommon-1.0.23.jar
- jfreechart-1.0.19.jar
- commons-beanutils-1.9.4.jar
- commons-collections-3.2.2.jar

## Overview

To install the dependencies, complete the following steps.

1. Connect to your Amazon EC2 instance and change the user to **su**
   by running the following command.

```
sudo su
```

You need Superuser privilege to run commands in this tutorial. 2. Navigate to the `<your-tomcat-path>/extra/` folder.

```
cd <your-tomcat-path>/extra/
```

3. Copy any of the above dependencies as required at this folder.
4. Stop and start the tomcat.service by running the following commands.

```
systemctl stop tomcat.service
```

```
systemctl start tomcat.service
```

5. Check the status of the service to make sure it is running.

```
systemctl status tomcat.service
```

6. Verify the logs.

## Set up the dependencies for JAC and BAC

webapps

1. If your JICS database is hosted on Oracle, then you need to provide the Oracle database
   driver in `<your-tomcat-path>/extra`.
2. Create the folder if it is not present already.
3. Stop and restart your Apache Tomcat server.
4. Verify the logs.
