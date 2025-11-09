AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Set up AWS Blu Age Runtime on container

This topic explains how to set up and deploy the PlanetsDemo sample application using AWS Blu Age Runtime
on a docker container.

AWS Blu Age Runtime on container is available for Amazon ECS managed by Amazon EC2, Amazon ECS managed by AWS Fargate,
and Amazon EKS managed by Amazon EC2. It isn't compatible with Amazon EKS managed by AWS Fargate.

###### Topics

- [Prerequisites](#ba-runtime-deploy-prereq "#ba-runtime-deploy-prereq")
- [Setting up](#ba-runtime-deploy-setup "#ba-runtime-deploy-setup")
- [Test the deployed application](#ba-runtime-deploy-test "#ba-runtime-deploy-test")

## Prerequisites

Before you begin, make sure you complete the following prerequisites.

- Configure the AWS CLI by following the steps in [Configuring the AWS
  CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
- Complete [AWS Blu Age Runtime prerequisites](ba-runtime-setup-prereq.md "ba-runtime-setup-prereq.md") and [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") .
- Download the AWS Blu Age Runtime binaries. For instructions, see
  [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") .
- Download the Apache Tomcat 10 binaries.
- Download the [PlanetsDemo
  application archive](https://d3lkpej5ajcpac.cloudfront.net/demo/bluage/PlanetsDemo-v1.zip "https://d3lkpej5ajcpac.cloudfront.net/demo/bluage/PlanetsDemo-v1.zip").
- Create an Amazon Aurora PostgreSQL database for JICS, and run the
  `PlanetsDemo-v1/jics/sql/initJics.sql` query on it. For information
  about how to create an Amazon Aurora PostgreSQL database see, [Creating and connecting to an Aurora PostgreSQL DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster").

## Setting up

To set up the PlanetsDemo sample application, complete the following steps.

1. After downloading the Apache Tomcat binaries, extract the contents, and go to the
   `conf` folder. Open the
   `catalina.properties` file for editing and replace the
   line that starts with `common.loader` with the following
   line.

```
common.loader="${catalina.base}/lib","${catalina.base}/lib/*.jar","${catalina.home}/lib","${catalina.home}/lib/*.jar","${catalina.home}/shared","${catalina.home}/shared/*.jar","${catalina.home}/extra","${catalina.home}/extra/*.jar"
```

2. Compress the Apache Tomcat folder by using the tar command to build a `tar.gz`
   archive.
3. Prepare a [Dockerfile](https://docs.docker.com/engine/reference/builder/ "https://docs.docker.com/engine/reference/builder/") to build your custom image based on the provided runtime binaries
   and Apache Tomcat server binaries. See the following example Dockerfile. The goal is to
   install Apache Tomcat 10, followed by AWS Blu Age Runtime (for Amazon ECS managed by
   AWS Fargate) extracted at the root of Apache Tomcat 10 installation directory, and then
   to install the sample modernized application named PlanetsDemo.

###### Note

The contents of install-gapwalk.sh and install-app.sh scripts, which are used in
this example Dockerfile, are listed after the Dockerfile.

```
FROM --platform=linux/x86_64 amazonlinux:2

RUN mkdir -p /workdir/apps
WORKDIR /workdir
COPY install-gapwalk.sh .
COPY install-app.sh .
RUN chmod +x install-gapwalk.sh
RUN chmod +x install-app.sh

# Install Java and AWS CLI v2-y
RUN yum install sudo java-17-amazon-corretto unzip tar -y
RUN sudo yum remove awscli -y
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN sudo unzip awscliv2.zip
RUN sudo ./aws/install

# Installation dir
RUN mkdir -p /usr/local/velocity/installation/gapwalk
# Copy PlanetsDemo archive to a dedicated apps dir
COPY PlanetsDemo-v1.zip /workdir/apps/

# Copy resources (tomcat, blu age runtime) to installation dir
COPY tomcat.tar.gz /usr/local/velocity/installation/tomcat.tar.gz
COPY aws-bluage-runtime-4.x.x.tar.gz /usr/local/velocity/installation/gapwalk/gapwalk.tar.gz

# run relevant installation scripts
RUN ./install-gapwalk.sh
RUN ./install-app.sh

EXPOSE 8080
EXPOSE 8081
# ...

WORKDIR /bluage/tomcat.gapwalk/velocity
# Run Command to start Tomcat server
CMD ["sh", "-c", "sudo bin/catalina.sh run"]
```

The following are the contents of `install-gapwalk.sh.`

```

# Vars
TEMP_DIR=/bluage-on-fargate/tomcat.gapwalk/temp

# Install
echo "Installing Gapwalk and Tomcat"
sudo rm -rf /bluage-on-fargate
mkdir -p ${TEMP_DIR}
# Copy Blu Age runtime and tomcat archives to temporary extraction dir
sudo cp /usr/local/velocity/installation/gapwalk/gapwalk.tar.gz ${TEMP_DIR}
sudo cp /usr/local/velocity/installation/tomcat.tar.gz ${TEMP_DIR}
# Create velocity dir
mkdir -p /bluage/tomcat.gapwalk/velocity
# Extract tomcat files
tar -xvf ${TEMP_DIR}/tomcat.tar.gz -C ${TEMP_DIR}
# Copy all tomcat files to velocity dir
cp -fr ${TEMP_DIR}/apache-tomcat-10.x.x/* /bluage/tomcat.gapwalk/velocity
# Remove default webapps of Tomcat
rm -f /bluage-on-fargate/tomcat.gapwalk/velocity/webapps/*
# Extract Blu Age runtime at velocity dir
tar -xvf ${TEMP_DIR}/gapwalk.tar.gz -C /bluage/tomcat.gapwalk
# Remove temporary extraction dir
sudo rm -rf ${TEMP_DIR}
```

The following are the contents of `install-app.sh`.

```
#!/bin/sh

APP_DIR=/workdir/apps
TOMCAT_GAPWALK_DIR=/bluage-on-fargate/tomcat.gapwalk

unzip ${APP_DIR}/PlanetsDemo-v1.zip -d ${APP_DIR}
cp -r ${APP_DIR}/webapps/* ${TOMCAT_GAPWALK_DIR}/velocity/webapps/
cp -r ${APP_DIR}/config/* ${TOMCAT_GAPWALK_DIR}/velocity/config/
```

4. Provide the connection information for the database that you created as part of the
   prerequisites in the following snippet in the `application-main.yml`
   file, which is located in the `{TOMCAT_GAPWALK_DIR}/config` folder. For
   more information see, [Creating and connecting to an Aurora PostgreSQL DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster").

```
datasource:
   jicsDs:
     driver-class-name :
     url:
     username:
     password:
     type :
```

5. Build and push the image to your Amazon ECR repository. For instructions, see [Pushing a Docker image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md") in the
   Amazon Elastic Container Registry User Guide. Then, depending on your situation, either create an Amazon EKS pod or an
   Amazon ECS task definition using your Amazon ECR image, and deploy it to your cluster. For example
   on creating these, see [Creating a task definition using the console](../../../AmazonECS/latest/developerguide/create-task-definition.md "../../../AmazonECS/latest/developerguide/create-task-definition.md") in the _Amazon Elastic Container Service (Amazon ECS) Developer Guide_ and [Deploy a
   sample application](../../../eks/latest/userguide/sample-deployment.md "../../../eks/latest/userguide/sample-deployment.md") in the _Amazon EKS User
   Guide_.
6. Specifically, for **Amazon ECS managed by AWS Fargate** case,
   when creating the Task definition, use the IAM role
   you created as part of the initial Infrastructure setup. Then, while creating the
   service, expand the **Networking** section,
   and configure the VPC, subnets, and security group that you created as part of the
   initial Infrastructure setup. See, [Infrastructure setup requirements for AWS Blu Age Runtime
   (non-managed)](ba-infrastructure-setup.md "ba-infrastructure-setup.md").

## Test the deployed application

For an example of how to test the PlanetsDemo application, see [Test the PlanetsDemo application](ba-runtime-test-planetsdemo.md "ba-runtime-test-planetsdemo.md").
