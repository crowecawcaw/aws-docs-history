AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Upgrade the AWS Blu Age Runtime on Amazon EC2

This guide describes how to upgrade the AWS Blu Age Runtime on Amazon EC2.

###### Topics

- [Prerequisites](#ba-runtime-maint-prereq "#ba-runtime-maint-prereq")
- [Upgrade the AWS Blu Age Runtime in the Amazon EC2
  instance](#ba-runtime-maint-copy-files "#ba-runtime-maint-copy-files")
- [Upgrade the AWS Blu Age Runtime in a
  container](#ba-runtime-maint-copy-files "#ba-runtime-maint-copy-files")

## Prerequisites

Before you begin, make sure you meet the following prerequisites.

- To check if there are specific instructions for your version, see [Upgrading instructions for AWS Blu Age](ba-migration-notes.md "ba-migration-notes.md").
- Complete [AWS Blu Age Runtime prerequisites](ba-runtime-setup-prereq.md "ba-runtime-setup-prereq.md") and [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") .
- Ensure that you have an Amazon EC2 instance that contains the latest AWS Blu Age Runtime. For more
  information, see [Get started with Amazon EC2 Linux instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md").
- Make sure you can connect to the Amazon EC2 instance successfully, for example, by using
  SSM.
- Download the version of the AWS Blu Age Runtime that you want to upgrade to. For more information, see
  [Set up AWS Blu Age Runtime](ba-runtime-setup.md "ba-runtime-setup.md") The framework consists of two binary files:
  `aws-bluage-runtime-x.y.z.zip` and
  `aws-bluage-webapps-x.y.z.zip`.

## Upgrade the AWS Blu Age Runtime in the Amazon EC2

instance

Complete the following steps to upgrade the AWS Blu Age Runtime.

1. Connect to your Amazon EC2 instance and change the user to **su**
   by running the following command.

```
`sudo su`
```

You need superuser privilege to run commands in this tutorial. 2. Create two folders, one for each binary file. 3. Name each folder with the same name as the binary file. 4. Copy each binary file to the corresponding folder.

###### Warning

Extracting each binary produces a folder with the same name. Therefore, if you extract
both binary files at the same location one after another, you will overwrite the
content. 5. To extract the binaries, use the following commands. Run the commands in each
folder.

```
unzip aws-bluage-runtime-x.y.z.zip
unzip aws-bluage-webapps-x.y.z.zip
```

6. Stop the Apache Tomcat services by using the following commands.

```
systemctl stop tomcat.service
systemctl stop tomcat-webapps.service
```

7. Replace the content of `<your-tomcat-path>/shared/` with the content
   of `aws-bluage-runtime-x.y.z/shared/`.
8. Replace `<your-tomcat-path>/webapps/gapwalk-application.war` with
   `aws-bluage-runtime-x.y.z/webapps/gapwalk-application.war`.
9. Replace the war files in `<your-tomcat-path>/webapps/`, namely
   `bac.war` and `jac.war`, with the same files from
   `aws-bluage-webapps-x.y.z/velocity/webapps/`.
10. Start the Apache Tomcat services by running the following commands.

```
systemctl start tomcat.service
systemctl start tomcat-webapps.service
```

11. Check the logs.

To check the status of the deployed application, run the following commands.

```
curl http://localhost:8080/gapwalk-application/
```

The following message should appear.

```
Jics application is running
```

```
curl http://localhost:8181/jac/api/services/rest/jicsservice/
```

The following message should appear.

```
Jics application is running
```

```
curl http://localhost:8181/bac/api/services/rest/bluesamserver/serverIsUp
```

The response should be empty.

The AWS Blu Age runtime is successfully upgraded.

## Upgrade the AWS Blu Age Runtime in a

container

Complete the following steps to upgrade the AWS Blu Age Runtime.

1. Rebuild your Docker image with the desired AWS Blu Age Runtime version. For instructions, see [Set up AWS Blu Age Runtime on Amazon EC2](ba-runtime-deploy-ec2.md "ba-runtime-deploy-ec2.md").
2. Push your Docker image to your Amazon ECR repository.
3. Stop and restart your Amazon ECS or Amazon EKS service.
4. Check the logs.

The AWS Blu Age Runtime is successfully upgraded.
