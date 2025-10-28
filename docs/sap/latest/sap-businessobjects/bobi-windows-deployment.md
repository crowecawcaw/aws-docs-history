# Deployment

In this deployment, we will provision an Amazon EC2 instance for installing the SAP application servers and the CMS database (if you are using database on EC2). When using Amazon RDS for CMS database, follow [Step 7. (Only for CMS Database on EC2 Instance) Installing CMS Database](#bobi-windows-step-7-only-for-cms-database-on-ec2-instance-installing-cms-database "#bobi-windows-step-7-only-for-cms-database-on-ec2-instance-installing-cms-database").

In this deployment, we will provision an Amazon EC2 instance for installing a standalone Oracle database standard system.

###### Note

In this section, the syntax shown for the AWS CLI and Linux commands is specific to the scope of this document. Each command supports many additional options. For more information, use the AWS CLI `aws help` command or see the documentation.

## Step 1. Prepare Your AWS Account

In this example we step through setting up a sample environment for the installation which includes a public subnet for RDP and SSH access via the internet. In our scenario, we are using the AWS Launch Wizard for SAP in a single-AZ deployment to create the VPC, subnets, security groups, and IAM roles. This is just an example setup and customers should follow their own network layout and comply with their own security standards. This may include:

- using an AWS Launch Wizard for SAP for a multi-AZ deployment of SAP HANA
- using a landing zone solution like [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- work with their cloud team (for example a Cloud Center of Excellence or CCoE) to use existing standards
  1.  Check the region where you want to deploy your AWS resources:

  ###### Note

  You’ll have picked the region you want to deploy in during your planning phase. 2. Display the AWS CLI configuration data:

  ```
  $ aws configure list
  ```

In the command output, make sure that the default region that’s listed is the same as the target region where you want to deploy your AWS resources and install the SAP workload.

## Step 2. Create a JSON file for the Amazon EBS storage

Create a JSON file that contains the storage requirements for SAP BOBI Platform server volumes.

Below is an example JSON file with two EBS volumes for swap and SAP BOBI Platform installation directory. You can modify this file as per your requirements:

```
[
  {
    "DeviceName": "/dev/sdh",
    "Ebs": {
      "VolumeSize": 32,
      "VolumeType": "gp3",
      "DeleteOnTermination": true
    }
  },
  {
    "DeviceName": "/dev/sdg",
    "Ebs": {
      "VolumeSize": 50,
      "VolumeType": "gp3",
      "DeleteOnTermination": true
    }
  }
]
```

## Step 3. Launch the Amazon EC2 Instance

Launch the Amazon EC2 instance for the SAP BOBI Platform installation in your target region by using the information that you gathered in the preparation phase. You will also be creating the required storage volumes and attaching them to the Amazon EC2 instance for the SAP installation, based on the JSON file that you created in the previous step.

```
$ aws ec2 run-instances \
--image-id AMI-ID \
--count number-of-EC2-instances \
--instance-type instance-type \
--key-name=name-of-key-pair \
--security-group-ids security-group-ID \
--subnet-id subnet-ID \
--block-device-mappings file://C:\Users\<file>.json \
--region region-ID
```

The JSON file is the storage file that you created in [Step 2. Create a JSON file for the Amazon EBS storage](#bobi-windows-step-2-create-a-json-file-for-the-amazon-ebs-storage "#bobi-windows-step-2-create-a-json-file-for-the-amazon-ebs-storage").

When using the command, make sure to place the command and its parameters on a single line. For example:

```
aws ec2 run-instances --image-id <ami-xxxxxxxxxxxxxxx> --count 1 \
--instance-type m5.large --key-name=my_key --security-group-ids \
<sg-xxxxxxxx> --subnet-id <subnet-xxxxxx> \
--block-device-mappings file://C:\Users\<file>.json
```

You can also launch EC2 instances using the AWS Management Console. For detailed steps, see [Launch Windows EC2 Instances using AWS Management Console](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-launch-instance").

## Step 4. Prepare Each EC2 Instance for SAP Installation

1. Log into the newly-created RDP host in the public subnet. We will call this **jumpbox** for easy reference. Do this by either using the new [Session Manager feature for AWS Systems Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md") (for command line tasks), or by following these steps:
   1. In the AWS Management Console, select the EC2 instance **jumpbox** and choose **Connect**. Download the RDP file from the pop-up that appears.
   2. Choose **Get Password** and provide your private key to decrypt the password. This is the password for the local Administrator user on **jumpbox**.
   3. Open the RDP file in your preferred RDP program, and connect to **jumpbox**. Log in with user Administrator and the password you just retrieved in Step 2.
   4. Once logged in, return to the AWS Management Console and repeat steps 1 and 2, but this time for the EC2 instance where you will install SAP. Copy the downloaded RDP file to **jumpbox**.
   5. While logged into **jumpbox**, open the RDP file for the SAP instance in your preferred RDP program.

2. Log in as a user with administrator privileges but not an existing <SID>adm user (as per SAP’s requirements).
3. Install the AWS CLI tools or use the [AWS Tools for PowerShell](https://aws.amazon.com/powershell/ "https://aws.amazon.com/powershell/") provided with the Windows AMI.
4. Install the version of the Java JRE that is compatible with your desired SAP installation software.
5. Install the AWS Data Provider as per the instructions for Windows in the [AWS Data Provider for SAP Installation and Operations Guide](https://s3.amazonaws.com/aws-data-provider/aws-data-provider-ig.pdf "https://s3.amazonaws.com/aws-data-provider/aws-data-provider-ig.pdf").
6. Install and configure the AWS Systems Manager Agent (SSM Agent). For steps, see [Working with SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").

## Step 5. Create Amazon FSx Volumes

1. The global file share and transport directories need to be available across all your SAP system’s EC2 instances. For Windows we assume use of Amazon FSx for this purpose.
2. Be sure you’ve satisfied the prerequisites in the [Technical Requirements](bobi-windows-prerequisites.md#bobi-windows-technical-requirements "bobi-windows-prerequisites.md#bobi-windows-technical-requirements") section of this document. You will need to have already deployed your EC2 instances in each of the Availability Zones where you will create FSx filesystems.
3. Follow the step-by-step instructions in the [Getting Started with Amazon FSx](../../../fsx/latest/WindowsGuide/getting-started.md "../../../fsx/latest/WindowsGuide/getting-started.md") documentation.
4. For high availability deployments that require multi-AZ redundancy to tolerate temporary AZ unavailability , follow the instructions to [create multiple ﬁle systems in separate AZs](../../../fsx/latest/WindowsGuide/multi-az-deployments.md "../../../fsx/latest/WindowsGuide/multi-az-deployments.md") .

## Step 6. Prepare and Install the CMS Database (Only for RDS Database)

This option is applicable only when Amazon RDS MySQL is used for the CMS database. You can create a separate database for the auditing database if it’s required.

1. Create a DB subnet group for an RDS instance by following the instructions in [Create a DB Subnet Group](../../../AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.md#CHAP_Tutorials.WebServerDB.CreateVPC.DBSubnetGroup "../../../AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.md#CHAP_Tutorials.WebServerDB.CreateVPC.DBSubnetGroup").
2. In the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/"), launch an Amazon RDS MySQL DB instance by following the instructions in the [Creating a DB Instance Running the MySQL Database Engine](../../../AmazonRDS/latest/UserGuide/USER_CreateInstance.md "../../../AmazonRDS/latest/UserGuide/USER_CreateInstance.md").
3. Choose a supported DB version based on [SAP Note 1656099 - SAP on AWS: Supported SAP](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099"), and select the instance type and storage based on your sizing output.
4. On the **Specify DB details** page, in the **Instance specifications** section, choose **Create replica in different zone**.
5. The **Choose use case** page asks if you are planning to use the DB instance you are creating for production. If you choose **Production - MySQL**, the Multi-AZ failover option is preselected. You can deselect this option if you are not installing a highly available system.
6. On the **Configure advanced settings** page, provide information about the infrastructure you already provisioned, such as settings for the VPC, DB subnet group, and security group. In addition, you can provide custom options for encryption, backup retention period, maintenance window, and so on. You will also create a user to administer this database.
7. For the database name, you can provide the name you want to use for the CMS database. You can also change the database port from the default value to your choice of port.
8. Choose **Create database**, and then wait for the DB instance status to change to **available** in the Amazon RDS console.
9. Choose the **Instances** view and note the **Endpoint** name. In case of failover to another Availability Zone, this endpoint enables an application to reconnect to a new primary database instance without having to change anything.
10. (Optional) Create a CNAME in Amazon Route 53 or other DNS server for the database cluster endpoint. Use this CNAME during the installation of SAP BOBI Platform nodes.

## Step 7. Install CMS Database (Only for CMS Database on EC2 Instance)

Install the CMS database with an SAP supported database version of your choice. Refer to the database vendor specific documentation for instructions. You can also install Audit database if you plan to use auditing. The Auditing database can be installed at a later point in time as it is not required for SAP BOBI Platform functioning.

## Step 8. Install SAP BOBI Platform Nodes

1. Log in to each EC2 instance in the SAP BOBI Platform server and repeat the following step to install SAP BOBI platform on each instance.
2. See the [SAP BusinessObjects BI Platform installation guide](https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/ "https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/") and go to the SAP BOBI documentation specific to the version you want to install. Launch the installation as described:

**Custom / Expand** > **Expand an existing SAP BusinessObjects BI platform deployment** > **Instances** > **Servers** > **Platform Services** 3. For the first server installation, choose **Start a new SAP BusinessObjects BI platform deployment**. Follow the instructions and enter inputs as required for example database connection information. Figure 3 shows example of adding database connection information when using RDS MySQL. 4. (Optional) This step is only required for multi-node installation. For all additional server installations, choose **Expand an existing SAP BusinessObjects BI platform deployment**. Follow the instructions and enter inputs as required for example database connection information and first CMS server connection information.

This completes the installation of SAP BOBI Platform.

## Step 9. Configure End User Access for Multi-Node Deployment

To distribute the user load evenly across the web tier servers, you can use a load balancer between the web users and the web servers. In this guide, we’ll discuss the use of [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/ "https://aws.amazon.com/elasticloadbalancing/") for this purpose. You can also install other load balancers on EC2 instances for end user access, refer to vendor specific documentation for such installation. An Application Load Balancer automatically scales its request handling capacity in response to incoming application traffic. Follow these steps to configure an Application Load Balancer for SAP BOBI Platform:

1. In the [Amazon EC2 console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/"), [create an Application Load Balancer](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-load-balancer "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-load-balancer") in the VPC where SAP BOBI Platform is running. Specify the Availability Zones and subnets of all the web tier servers.

###### Note

Application Load Balancer cannot route fields with special characters (such as, underscore) to targets. Disable the `routing.http.drop_invalid_header_fields` attribute to enable routing of fields with special characters. 2. [Configure a security group](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-security-group "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-security-group") that allows users to connect to the Application Load Balancer on the SSL port. 3. [Create a target group](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-target-group "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-target-group") to register web servers as the targets to the load balancer. For **Target type**, choose **ip** and specify the IP address and SSL port of the web servers to register as targets. 4. [Enable sticky sessions](../../../elasticloadbalancing/latest/application/load-balancer-target-groups.md#sticky-sessions "../../../elasticloadbalancing/latest/application/load-balancer-target-groups.md#sticky-sessions"). 5. Create or upload an existing SSL certificate in AWS Certificate Manager (ACM). 6. Enable Secure Sockets Layer (SSL) communications for SAP BOBI Platform by following the instructions in the [Business Intelligence Platform Administrator Guide](https://help.sap.com/http.svc/rc/ec7df5236fdb101497906a7cb0e91070/4.2.6/en-US/sbo42sp6_bip_admin_en.pdf "https://help.sap.com/http.svc/rc/ec7df5236fdb101497906a7cb0e91070/4.2.6/en-US/sbo42sp6_bip_admin_en.pdf"). See also: [Enabling SSL in BI Platform 4.2 SP05](https://blogs.sap.com/2017/11/08/enabling-ssl-in-bi-platform-4.2-sp05/ "https://blogs.sap.com/2017/11/08/enabling-ssl-in-bi-platform-4.2-sp05/") on the SAP Blog. 7. (Optional) Create a CNAME in Amazon Route 53 for the Application Load Balancer DNS name. Use this CNAME to access SAP BOBI Platform.
