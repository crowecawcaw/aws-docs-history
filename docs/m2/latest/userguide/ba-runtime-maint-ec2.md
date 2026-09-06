

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Upgrade the AWS Transform for mainframe Runtime on Amazon EC2
<a name="ba-runtime-maint-ec2"></a>

This guide describes how to upgrade the AWS Transform for mainframe Runtime on Amazon EC2.

**Topics**
+ [Prerequisites](#ba-runtime-maint-prereq)
+ [Upgrade the AWS Transform for mainframe Runtime in the Amazon EC2 instance](#ba-runtime-maint-copy-files)
+ [Upgrade the AWS Transform for mainframe Runtime in a container](#ba-runtime-maint-copy-files)

## Prerequisites
<a name="ba-runtime-maint-prereq"></a>

Before you begin, make sure you meet the following prerequisites.
+ To check if there are specific instructions for your version, see [Upgrading instructions for AWS Transform for mainframe](ba-migration-notes.md).
+ Complete [AWS Transform for mainframe Runtime prerequisites](ba-runtime-setup-prereq.md) and [Onboarding AWS Transform for mainframe Runtime](ba-runtime-setup-onboard.md).
+ Ensure that you have an Amazon EC2 instance with an existing AWS Transform for mainframe Runtime installation. For more information, see [Get started with Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).
+ Make sure you can connect to the Amazon EC2 instance successfully, for example, by using SSM.
+ Download the AWS Transform for mainframe Runtime version you want to upgrade to. The framework consists of two archive files : `gapwalk-x.y.z.zip` and `aws-bluage-webapps-x.y.z.zip`. For more information, see [AWS Transform for mainframe Runtime artifacts](ba-runtime-artifacts.md).

## Upgrade the AWS Transform for mainframe Runtime in the Amazon EC2 instance
<a name="ba-runtime-maint-copy-files"></a>

Complete the following steps to upgrade the AWS Transform for mainframe Runtime.

1. Connect to your Amazon EC2 instance and change the user to **su** by running the following command.

   ```
   sudo su
   ```

   You need superuser privilege to run commands in this tutorial.

1. To extract the binaries, use the following commands. Run the commands in each folder.

   ```
   unzip gapwalk-x.y.z.zip
   unzip aws-bluage-webapps-x.y.z.zip
   ```

1. Stop the Apache Tomcat services by using the following commands.

   ```
   systemctl stop tomcat.service
   systemctl stop tomcat-webapps.service
   ```

1. Replace the content of `<your-tomcat-path>/shared/` with the content of `gapwalk-x.y.z/shared/`.

1. Replace `<your-tomcat-path>/webapps/gapwalk-application.war` with `gapwalk-x.y.z/webapps/gapwalk-application.war`.

1. Replace the war files in `<your-tomcat-path>/webapps/`, namely `bac.war` and `jac.war`, with the same files from `aws-bluage-webapps-x.y.z/velocity/webapps/`.

1. Start the Apache Tomcat services by running the following commands.

   ```
   systemctl start tomcat.service
   systemctl start tomcat-webapps.service
   ```

1. Check the logs.

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

The AWS Transform for mainframe runtime is successfully upgraded.

## Upgrade the AWS Transform for mainframe Runtime in a container
<a name="ba-runtime-maint-copy-files"></a>

Complete the following steps to upgrade the AWS Transform for mainframe Runtime.

1. Rebuild your Docker image with the desired AWS Transform for mainframe Runtime version. For instructions, see [Set up AWS Transform for mainframe Runtime on Amazon EC2](ba-runtime-deploy-ec2.md).

1. Push your Docker image to your Amazon ECR repository.

1. Stop and restart your Amazon ECS or Amazon EKS service.

1. Check the logs.

The AWS Transform for mainframe Runtime is successfully upgraded.