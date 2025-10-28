# Installing SAP BusinessObjects BI Platform for HA

## Creating a VPC

1. Create a VPC in one of the available AWS Regions by following the instructions in the [Amazon Virtual Private Cloud documentation](../../../AmazonVPC/latest/UserGuide/GetStarted.md "../../../AmazonVPC/latest/UserGuide/GetStarted.md").

###### Note

You can also use the [Amazon Virtual Private Cloud Quick Start](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/") to provision your VPC. 2. Specify a contiguous IP address range in CIDR block format (e.g., 192.168.0.0/16). You must choose a range that doesn’t overlap with an already existing range used internally on your corporate network. 3. Create six new subnets, associate each with the new VPC, and split them across two different Availability Zones. 4. To continue with the installation process, you’ll need access to the instances deployed into the VPC. You can use a [VPN connection](../../../AmazonVPC/latest/UserGuide/vpn-connections.md "../../../AmazonVPC/latest/UserGuide/vpn-connections.md") or [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/") to establish a dedicated network connection from your premises to AWS. In both cases, be sure to create appropriate route tables, associate them with the new subnets, and adjust the network ACLs with rules to meet internal security requirements.

###### Note

The procedure in this section is based on the large-scale distributed deployment example. You can revise the procedure to support your architecture. For example, you can use additional subnets combined with network ACLs to further isolate or restrict access to different tiers of the SAP BusinessObjects BI Platform environment, and you can create multiple public and private subnets for isolation. Any subnet that is associated with an internet gateway will become a public subnet.

## Building the Infrastructure

After you create the VPC, deploy supporting infrastructure instances that will provide key services used by the SAP environment from within the VPC. These services might include:

- Active Directory services (see [Quick Start](https://aws.amazon.com/quickstart/architecture/active-directory-ds/ "https://aws.amazon.com/quickstart/architecture/active-directory-ds/"))
- DNS
- Network address translation (NAT) services
- Remote Desktop gateways (see [Quick Start](https://aws.amazon.com/quickstart/architecture/rd-gateway/ "https://aws.amazon.com/quickstart/architecture/rd-gateway/"))
- Bastion hosts (see [Quick Start](https://aws.amazon.com/quickstart/architecture/linux-bastion/ "https://aws.amazon.com/quickstart/architecture/linux-bastion/"))

When supporting infrastructure services are in place, you can continue with the next section to start deploying SAP components into the VPC.

## Preparing and Installing the CMS Database

This guide uses Amazon RDS MySQL for the CMS database. You can create a separate database for the auditing database if it’s required. HA isn’t a requirement for the auditing database, so this guide doesn’t cover the steps for provisioning it.

1. Create a DB subnet group for an RDS instance by following the instructions in the [Amazon RDS documentation](../../../AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.md#CHAP_Tutorials.WebServerDB.CreateVPC.DBSubnetGroup "../../../AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.md#CHAP_Tutorials.WebServerDB.CreateVPC.DBSubnetGroup"). Use two of the subnets you created earlier to create a DB subnet group.
2. In the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/"), launch an Amazon RDS MySQL DB instance by following the instructions in the [Amazon RDS documentation](../../../AmazonRDS/latest/UserGuide/USER_CreateInstance.md "../../../AmazonRDS/latest/UserGuide/USER_CreateInstance.md").
   - Choose a supported DB version based on the [Product Availability Matrix](https://support.sap.com/pam "https://support.sap.com/pam") on the SAP website, and select the instance type and storage based on your sizing output.
   - On the **Specify DB details** page, in the **Instance specifications** section, choose **Create replica in different zone**.
   - The **Choose use case** page asks if you are planning to use the DB instance you are creating for production. If you choose **Production - MySQL**, the Multi-AZ failover option is pre-selected.
   - On the **Configure advanced settings** page, provide information about the infrastructure you already provisioned, such as settings for the VPC, DB subnet group, and security group. In addition, you can provide custom options for encryption, backup retention period, maintenance window, and so on. You will also create a user to administer this database.
   - For the database name, you can provide the name you want to use for the CMS database. You can also change the database port from the default value of 3306 to your choice of port.
   - Choose **Create database**, and then wait for the DB instance status to change to **available** in the Amazon RDS console.
   - Choose the **Instances** view and note the **Endpoint** name. In case of failover to another Availability Zone, this endpoint enables an application to reconnect to a new primary database instance without having to change anything.
   - (Optional) Create a CNAME in Amazon Route 53 for the database cluster endpoint. Use this CNAME during the installation of SAP BusinessObjects BI Platform nodes.

If you’re planning a different database than Amazon RDS MySQL, use the database failover solution appropriate for your use case. Some solutions provide automatic failover on AWS in the event of primary database failure, including the failover of the virtual IP address used for database access. This method provides seamless failover for your applications.

## Preparing the OS

Follow these steps to build and configure EC2 instances before installing SAP BusinessObjects BI Platform:

1. Launch a new Amazon Elastic Compute Cloud Linux instance in Availability Zone 1. Prepare the server for the installation of SAP BusinessObjects BI Platform by following the instructions in the [SAP BusinessObjects BI Platform](https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/ "https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/") installation guide.
2. Create an EBS volume and attach it to the EC2 Linux instance. For instructions, see the [Amazon EBS user guide](../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md "../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md").
3. Create and mount a file system by following the instructions in the [Amazon EBS user guide](../../../AWSEC2/latest/UserGuide/ebs-using-volumes.md "../../../AWSEC2/latest/UserGuide/ebs-using-volumes.md"). Instructions include enabling automatic mounting each time you reboot the Linux instance.
4. Optionally, you can create an AMI of the instance, as described in the [AWS Toolkit for Visual Studio user guide](../../../toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.md "../../../toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.md"), and launch all other SAP BusinessObjects BI Platform nodes by using this AMI.
5. Launch other EC2 instances according to your design, using one of these methods:
   - Manually perform steps 1-3 for all EC2 instances required by your architecture.
   - Create an AWS CloudFormation template, using the AMI you created in step 4 as a resource. Use this template to launch all additional instances in their respective Availability Zones. This option saves time and helps prevent manual errors during instance provisioning.

## Installing CMS Nodes

1. Log in to each CMS server in the SAP BusinessObjects BI Platform node.
2. Launch the installation as described in the [SAP BusinessObjects BI Platform installation guide](https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/ "https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/") and choose:

**Custom / Expand** > **Expand an existing SAP BusinessObjects BI platform deployment** > **Instances** > **Servers** > **Platform Services** 3. For the first CMS server installation, choose **Start a new SAP BusinessObjects BI platform deployment**. 4. For all additional CMS server installations, choose **Expand an existing SAP BusinessObjects BI platform deployment**. 5. Enter the details of the first CMS server when prompted. This will cluster the additional CMS servers with the first one.

###### Note

You can also perform a silent installation by using a response file and the procedure described in the SAP installation guide. This method enables you to quickly rerun the installation again on the same server or on another server, as required. You can further automate the installation by using an AWS CloudFormation template. The template will enable you to provision EC2 instances and install the BusinessObjects BI Platform application in just a few clicks.

## Installing the Processing Tier

1. Log in to the processing tier server in the SAP BusinessObjects BI Platform node.
2. Launch the installation as described in the [SAP BusinessObjects BI Platform installation guide](https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/ "https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/") and choose:

**Custom / Expand** > **Expand an existing SAP BusinessObjects BI platform deployment** > **Instances** > **Servers** 3. Choose the servers and other features that you want to install on the processing tier node, and run the installation. 4. Repeat these steps for all your processing tier servers.

## Installing the Web Tier

1. Log in to each web tier server in the SAP BusinessObjects BI Platform node.
2. Launch the installation as described in the [SAP BusinessObjects BI Platform installation guide](https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/ "https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/") and choose:

**Custom / Expand** > **Expand an existing SAP BusinessObjects BI platform deployment** > **Instances** > **WebTier** 3. Create a response file for silent installation by choosing **Custom / Expand** > **Web Tier**. You can install an integrated Tomcat web server by using the SAP installer, or you can use another supported web server and install applications by using the SAP installer.

## Post-Installation Configuration for HA

When you have installed the SAP BusinessObjects BI Platform on all servers, you must configure the cluster name, Amazon EFS, and the load balancer to complete the HA configuration.

### Configuring the SAP BusinessObjects BI Platform Cluster Name

Set up a cluster name by following the instructions in the [SAP BusinessObjects BI Platform Administrator Guide](https://help.sap.com/http.svc/rc/ec7df5236fdb101497906a7cb0e91070/4.2.6/en-US/sbo42sp6_bip_admin_en.pdf "https://help.sap.com/http.svc/rc/ec7df5236fdb101497906a7cb0e91070/4.2.6/en-US/sbo42sp6_bip_admin_en.pdf"). Use this cluster name in the properties files of all web applications and client tools.

### Configuring Amazon EFS for Input and Output Filestores

###### Note

Amazon EFS isn’t available yet in all AWS Regions; see a [list of available regions](../../../general/latest/gr/rande.md#elasticfilesystem-region "../../../general/latest/gr/rande.md#elasticfilesystem-region"). If you’re planning to use a region that doesn’t support Amazon EFS, you can choose a partner NFS solution from AWS Marketplace (such as Cloud Volumes ONTAP or SoftNAS) or you can deploy your own solution.

By default, the [File Repository Server (FRS)](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=322437724 "https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=322437724") filestore for SAP BusinessObjects BI Platform is located in the local installation directory. You can set up the filestore on a shared storage system like Amazon EFS, and then mount the Amazon EFS file system on all servers that are configured to run storage tier servers:

1. Create an Amazon EFS file system in the VPC where you installed SAP BusinessObjects BI Platform, and create mount targets in the subnets that run storage tier servers.
2. Configure Amazon EFS for automatic mounting on FRS servers by following the instructions in the [Amazon EFS documentation](../../../efs/latest/ug/mount-fs-auto-mount-onreboot.md "../../../efs/latest/ug/mount-fs-auto-mount-onreboot.md"), and run the command **mount –a** to mount the file system.
3. Follow the instructions in the [SAP Community Wiki](https://wiki.scn.sap.com/wiki/display/BOBJ/File+Repository+Server "https://wiki.scn.sap.com/wiki/display/BOBJ/File+Repository+Server") to change the FRS path to Amazon EFS.

### Configuring the Load Balancer for Web Server Access

To distribute the user load evenly across the web tier servers, you can use a load balancer between the web users and the web servers. In this guide, we’ll discuss the use of [Elastic Load Balancing (Elastic Load Balancing)](https://aws.amazon.com/elasticloadbalancing/ "https://aws.amazon.com/elasticloadbalancing/") for this purpose. An Application Load Balancer automatically scales its request handling capacity in response to incoming application traffic. Follow these steps to configure an Application Load Balancer for SAP BusinessObjects BI Platform:

1. Enable Secure Sockets Layer (SSL) communications for SAP BusinessObjects BI Platform by following the instructions in the [administrator guide](https://help.sap.com/http.svc/rc/ec7df5236fdb101497906a7cb0e91070/4.2.6/en-US/sbo42sp6_bip_admin_en.pdf "https://help.sap.com/http.svc/rc/ec7df5236fdb101497906a7cb0e91070/4.2.6/en-US/sbo42sp6_bip_admin_en.pdf"). See also: [Enabling SSL in BI Platform 4.2 SP05](https://blogs.sap.com/2017/11/08/enabling-ssl-in-bi-platform-4.2-sp05/ "https://blogs.sap.com/2017/11/08/enabling-ssl-in-bi-platform-4.2-sp05/") on the SAP blog.
2. In the [Amazon EC2 console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/"), [create an Application Load Balancer](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-load-balancer "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-load-balancer") in the VPC where SAP BusinessObjects BI Platform is running. Specify the Availability Zones and subnets of all the web tier servers.
3. [Configure a security group](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-security-group "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-security-group") that allows users to connect to the Application Load Balancer on the SSL port.
4. [Create a target group](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-target-group "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md#configure-target-group") to register web servers as the targets to the load balancer. For **Target type**, choose **ip** and specify the IP address and SSL port of the web servers to register as targets.
5. [Enable sticky sessions](../../../elasticloadbalancing/latest/application/load-balancer-target-groups.md#sticky-sessions "../../../elasticloadbalancing/latest/application/load-balancer-target-groups.md#sticky-sessions").
6. (Optional) Create a CNAME in Route 53 for the Application Load Balancer DNS name. Use this CNAME to access SAP BusinessObjects BI Platform.
