AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Set up AWS Blu Age Runtime (non-managed) on Amazon EC2

This topic explains how to set up and deploy the PlanetsDemo sample application using AWS Blu Age Runtime (non-managed)
on Amazon EC2.

###### Topics

- [Prerequisites](#ba-runtime-deploy-prereq "#ba-runtime-deploy-prereq")
- [Setting up](#ba-runtime-deploy-setup "#ba-runtime-deploy-setup")
- [Test the deployed application](#ba-runtime-deploy-test "#ba-runtime-deploy-test")

## Prerequisites

Before you begin, make sure you complete the following prerequisites.

- Configure the AWS CLI by following the steps in [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
- Complete [AWS Blu Age Runtime prerequisites](ba-runtime-setup-prereq.md "ba-runtime-setup-prereq.md") and [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") .
- Create an Amazon EC2 instance using one of the supported instance types. For more information, see [Get started with Amazon
  EC2 Linux instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md").
- Make sure you can connect to the Amazon EC2 instance successfully, for example by using
  SSM.

###### Note

Throughout this guide, the Tomcat installation path is assumed to be
`/m2-anywhere/tomcat-gapwalk/velocity`. Ensure you use this path when following the
instructions below or adapt the following instruction to the path of your choice.

- Download and extract AWS Blu Age Runtime (on Amazon EC2). Copy the contents of the velocity directory to
  `/m2-anywhere/tomcat-gapwalk/velocity`. Make sure to place the
  `bluage.bin` file exactly in the location specified by CATALINA_HOME environment
  variable described under [CATALINA_HOME and CATALINA_BASE](https://tomcat.apache.org/tomcat-8.5-doc/introduction.html#CATALINA_HOME_and_CATALINA_BASE "https://tomcat.apache.org/tomcat-8.5-doc/introduction.html#CATALINA_HOME_and_CATALINA_BASE") in the Apache Tomcat documentation. For
  instructions on how to retrieve the AWS Blu Age Runtime artifacts, including information
  about storage, access, and content, see [AWS Blu Age Runtime artifacts](ba-runtime-artifacts.md "ba-runtime-artifacts.md").
- Download the [PlanetsDemo
  application archive](https://d3lkpej5ajcpac.cloudfront.net/demo/bluage/PlanetsDemo-v1.zip "https://d3lkpej5ajcpac.cloudfront.net/demo/bluage/PlanetsDemo-v1.zip").
- Unzip the archive and upload the application to an Amazon S3 bucket of your choice.
- Create an Amazon Aurora PostgreSQL database for JICS. The AWS Blu Age Runtime will automatically execute the
  `PlanetsDemo-v1/jics/sql/initJics.sql` script during the first
  startup. For information about how to create an Amazon Aurora PostgreSQL database, see [Creating and connecting to an Aurora PostgreSQL DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster").

## Setting up

To set up the PlanetsDemo sample application, complete the following steps.

1. Connect to your Amazon EC2 instance and go to the `conf` folder under your Apache
   Tomcat 10 installation folder. Open the `catalina.properties`
   file for editing and replace the line that starts with `common.loader`
   with the following line.

```
common.loader="${catalina.base}/lib","${catalina.base}/lib/*.jar","${catalina.home}/lib","${catalina.home}/lib/*.jar","${catalina.home}/shared","${catalina.home}/shared/*.jar","${catalina.home}/extra","${catalina.home}/extra/*.jar"
```

2. Navigate to the `/m2-anywhere/tomcat-gapwalk/velocity /webapps/webapps`
   folder.
3. Copy the PlanetsDemo binaries available at `PlanetsDemo-v1/webapps/` folder from the Amazon S3
   bucket using the following command.

```
`aws s3 cp s3://`path-to-demo-app-webapps`/ . --recursive`
```

###### Note

Replace `path-to-demo-app-webapps` with the correct Amazon S3 URI for the bucket
where you previously unzipped the PlanetsDemo archive. 4. Copy the content of `PlanetsDemo-v1/config/` folder to
`/m2-anywhere/tomcat-gapwalk/velocity /config/`. 5. Provide the connection information for the database that you created as part of the
prerequisites in the following snippet in the `application-main.yml` file.
For more information see, [Creating and connecting to an Aurora PostgreSQL DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster").

```
datasource:
   jicsDs:
     driver-class-name :
     url:
     username:
     password:
     type :
```

6. Start your Apache Tomcat server and verify the logs.

```
/m2-anywhere/tomcat-gapwalk/velocity/startup.sh

tail -f /m2-anywhere/tomcat-gapwalk/velocity/logs/catalina.log
```

If you find error codes that start with a C followed by a number, such as CXXXX, note the
error messages. For example, error code C5102 is a common error indicating an incorrect
infrastructure configuration.

## Test the deployed application

For an example of how to test the PlanetsDemo application, see [Test the PlanetsDemo application](ba-runtime-test-planetsdemo.md "ba-runtime-test-planetsdemo.md").
