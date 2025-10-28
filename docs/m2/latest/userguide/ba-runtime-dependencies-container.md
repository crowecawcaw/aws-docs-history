AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Set up licensed dependencies in AWS Blu Age Runtime on

container

This topic describes how to set up additional licensed dependencies that you can use with
AWS Blu Age Runtime on container.

###### Topics

- [Prerequisites](#ba-runtime-dependencies-prereq "#ba-runtime-dependencies-prereq")
- [Overview](#ba-runtime-dependencies-overview "#ba-runtime-dependencies-overview")

## Prerequisites

Before you begin, make sure you complete the following prerequisites.

- Complete [AWS Blu Age Runtime prerequisites](ba-runtime-setup-prereq.md "ba-runtime-setup-prereq.md") and [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") .
- Get the following dependencies from their source.

### Oracle database

Supply an [Oracle database
driver](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html " https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html"). For example, **ojdbc11-23.3.0.23.09.jar**.

### IBM MQ connection

Supply an [IBM MQ
client](https://www.ibm.com/support/pages/mqc91-ibm-mq-clients "https://www.ibm.com/support/pages/mqc91-ibm-mq-clients"). For example, **com.ibm.mq.jakarta.client-9.3.4.1.jar**.

With this dependency version, also supply the following transitive dependencies:

- bcprov-jdk15to18-1.76.jar
- bcpkix-jdk15to18-1.76.jar
- bcutil-jdk15to18-1.76.jar

### DDS Printer files

Supply the Jasper reports
library (https://community.jaspersoft.com/download-jaspersoft/community-edition). For example, **jasperreports-6.16.0.jar**, but a
more recent version might be compatible.

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

1. Copy any of the above dependencies as required to your Docker image build folder.
2. If your JICS database is hosted on Oracle, provide the Oracle database driver in
   ``your-tomcat-path`/extra`.
3. On your Dockerfile, copy these dependencies to
   ``your-tomcat-path`/extra`.
4. Build your Docker image, and then push it to Amazon ECR.
5. Stop and restart your Amazon ECS or Amazon EKS service.
6. Check the logs.
