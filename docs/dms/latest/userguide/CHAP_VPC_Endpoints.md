

# Configuring VPC endpoints for AWS DMS
<a name="CHAP_VPC_Endpoints"></a>

AWS DMS supports Amazon virtual private cloud (VPC) endpoints as sources and targets. AWS DMS can connect to any AWS source or target database with Amazon VPC endpoints as long as explicitly defined routes to these source and target databases are defined in their AWS DMS VPC.

By supporting Amazon VPC endpoints, AWS DMS makes it easier to maintain end-to-end network security for all replication tasks without additional networking configuration and setup. Using VPC endpoints for all source and target endpoints ensures that all your traffic remains within your VPC and under your control.

For AWS DMS replication instance created in private subnet or AWS DMS serverless replication, to connect to AWS managed databases, it is necessary to set up an Amazon VPC endpoint:
+ Amazon S3
+ Amazon DynamoDB
+ Amazon Kinesis
+ Amazon Redshift
+ Amazon OpenSearch Service

If you are using AWS Secrets Manager to store connection credentials for DMS to use, you also need to set up a VPC endpoint.

Starting with AWS DMS version 3.4.7, VPC endpoints are required to establish connection between DMS replication instance or Serverless replication and the above Amazon services, when private network is used.

## Common AWS DMS prerequisites
<a name="CHAP_VPC_Endpoints.prereq"></a>

Before you configure a VPC endpoint, you must meet the following prerequisites:
+ Locate or create the VPC to use with AWS DMS replication instance or AWS DMS serverless replication. If you do not provide this information, DMS attempts to use the default VPC in the region, where it is setup.
+ Ensure you have IAM permissions to create VPC endpoint. To connect to Amazon S3 and Amazon DynamoDB, you can create Gateway VPC endpoints that provide reliable connectivity without requiring an internet gateway or a NAT device for your VPC. Gateway endpoints do not use AWS PrivateLink, unlike other types of VPC endpoints. For more information, see [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) in the *AWS PrivateLink guide*.
+ Configure IAM permissions to use DMS:
  + Configure the `dms-vpc-role` role. For more information, see [AWS managed policy: AmazonDMSVPCManagementRole](https://docs.aws.amazon.com/dms/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonDMSVPCManagementRole).
  + Configure the `dms-cloudwatch-logs-role` role. For more information, see [AWS managed policy: AmazonDMSCloudWatchLogsRole](https://docs.aws.amazon.com/dms/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonDMSCloudWatchLogsRole).
  + AWS DMS Serverless requires a service linked role (SLR) to exist in your account. AWS DMS manages the creation and usage of this role. For more information about making sure that you have the necessary SLR, see [Service-linked role for AWS DMS Serverless](https://docs.aws.amazon.com/dms/latest/userguide/slr-services-sl.html). When you create a replication, AWS DMS Serverless programmatically creates a Serverless service linked role. You can view this role in the IAM console.

## Set up an Amazon VPC endpoint with AWS Secrets Manager
<a name="CHAP_VPC_Endpoints.vpcforsecrets"></a>

You can set up an Amazon VPC endpoint for AWS Secrets Manager to work with AWS DMS. By creating this endpoint, you enable AWS DMS replication instances or serverless replication configurations in private subnets to securely access database credentials stored in Secrets Manager without requiring public internet access.

**Prerequisites**

Before you configure a VPC endpoint with AWS Secrets Manager in AWS DMS, you must meet the following prerequisites:
+ Ensure you configure all the [Common AWS DMS prerequisites](#CHAP_VPC_Endpoints.prereq).
+ Create and configure [source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html) or [target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html) database that you want to connect with.
+ Create secret in AWS Secrets manager with credentials to access source and target databases. Secret must be located in the same region as AWS DMS replication instance or AWS DMS serverless replication. Depending on the database type, the schema of the secret can vary. For more information, see [Working with AWS DMS endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html).
**Important**  
AWS DMS replication instance and AWS DMS serverless replication do not work with secrets, managed by Amazon RDS. These credentials do not include host and port information, that is required by AWS DMS to establish connections.
+ Configuring IAM permissions to manage DMS endpoint is required for some databases: Amazon S3, Amazon Kinesis, Amazon DynamoDB, Amazon Redshift, Amazon OpenSearch Service, Amazon Neptune, and Amazon Timestream. For more information see [Working with AWS DMS endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html).

**Create VPC endpoint for AWS Secrets Manager**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the VPC console menu bar, choose the same AWS Region as your AWS DMS replication instance.

1. In the VPC navigation pane, choose **Endpoints**.

1. In **Endpoints**, choose **Create endpoint**.

1. Configure the VPC endpoint as follows:

   1. Select **Type** as **AWS Services**.

   1. In the **Service Name** textbox, search for **secretsmanager** and select **com.amazonaws.[region].secretsmanager**. Ensure that the **Type** for your selected service is **Interface**.

   1. Under **Network settings** select the VPC that is running in the same region as your DMS replication instance or where you created Serverless replication.

   1. In the **Subnets** section, select your desired subnets where you want DMS to operate. Ensure you only select private subnets. You can identify a private subnet with the subnet ID. For example: `vpc-xxxxxx-subnet-private1-us-west-2a`.

      If your DMS replication instance is created without public access, you must choose the route tables associated with the private subnets where your replication instance resides.
**Note**  
Ensure you note the private subnets as you are required to provide them when creating DMS replication subnet group. To connect DMS with the AWS Secrets manager using the VPC endpoints, the subnets specified for VPC endpoint must be the same as the subnets in DMS replication subnet group.

   1. Select your desired **Security groups**. The security group rules control the traffic to the endpoint network interface from the resources in your VPC. If you do not specify a security group, the default security group is selected.

1. Select **Full access** under **Policy**. If you want to use custom policy to specify your own access control select **Custom**. You can use a trust policy that conforms with the JSON policy document, `dms-vpc-role`. For more information, see [Creating the IAM roles to use with AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/security-iam.html#CHAP_Security.APIRole).

1. Select **Create endpoint**.

   You must wait until the status becomes `Available`. Your VPC endpoint now has an ID starting with `vpce-xxxx`.

You have now successfully created a VPC endpoint. You must configure AWS DMS Endpoints, DMS subnet groups. Depending on migration option you choose, configure DMS replication instance or Serverless replication.

## Set up an Amazon VPC endpoint with Amazon S3
<a name="CHAP_VPC_Endpoints.vpcfors3"></a>

You can set up an Amazon VPC endpoint for Amazon S3 to work with AWS DMS. By creating this endpoint, you enable AWS DMS replication instances or serverless replication configurations in private subnets to securely access database credentials stored in S3 buckets without requiring public internet access.

**Prerequisites**

Before you configure a VPC endpoint with Amazon S3 in AWS DMS, you must meet the following prerequisites:
+ Ensure you configure all the [Common AWS DMS prerequisites](#CHAP_VPC_Endpoints.prereq).
+ Create an Amazon S3 bucket to use as [source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html) or [target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html) databases with AWS DMS. Do not enable versioning for S3. If you need S3 versioning, use lifecycle policies to actively delete old versions. Otherwise, you can encounter endpoint test connection failures because of an S3 list-object call timeout.
+ Configure IAM permissions to manage DMS Amazon S3 endpoint. If you are using AWS DMS Console, the IAM role with the necessary permissions can be created if you have permissions to create IAM roles.

**Create a VPC endpoint for Amazon S3**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the VPC console menu bar, choose the same AWS Region as your AWS DMS replication instance.

1. In the VPC navigation pane, choose **Endpoints**.

1. In **Endpoints**, choose **Create endpoint**.

1. Configure the VPC endpoint as follows:

   1. Select **Type** as **AWS Services**.

   1. In the **Service Name** textbox, search for **s3** and select **com.amazonaws.[region].s3**. Ensure that the **Type** for your selected service is **Gateway**. You can create a Gateway VPC endpoint when connecting to Amazon S3 and DynamoDB. Gateway endpoints do not use AWS PrivateLink, unlike other types of VPC endpoints.

   1. Under **Network settings** select the VPC that is running in the same region as your DMS replication instance or where you created Serverless replication.

   1. In the **Subnets** section, select your desired subnets where you want DMS to operate. Ensure you only select private subnets. You can identify a private subnet with the subnet ID. For example: `vpc-xxxxxx-subnet-private1-us-west-2a`.
**Note**  
If you have created your DMS replication instance without public access, you must choose the route tables associated with private subnets that are in the same region as your DMS instance. Ensure you note the private subnets as you are required to provide them when creating DMS replication subnet group. To connect DMS with Amazon S3 using the VPC endpoints, the subnets specified for VPC endpoint must be the same as the subnets in DMS replication subnet group.

1. Select **Full access** under **Policy**. If you want to use custom policy to specify your own access control select **Custom**. You can use a trust policy that conforms with the JSON policy document, `dms-vpc-role`. For more information, see [Creating the IAM roles to use with AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/security-iam.html#CHAP_Security.APIRole).

1. Select **Create endpoint**.

   You must wait until the status becomes `Available`. Your VPC endpoint now has an ID starting with `vpce-xxxx`.

You have now successfully created a VPC endpoint. You must configure AWS DMS Endpoints, DMS subnet groups. Depending on migration option you choose, configure DMS replication instance or Serverless replication.

## Setup an Amazon VPC endpoint for Amazon DynamoDB
<a name="CHAP_VPC_Endpoints.vpcfordynamoDB"></a>

When using AWS DMS replication instances in private subnets or AWS DMS serverless replication, you must create a VPC endpoint to establish secure connectivity with Amazon DynamoDB. Without a VPC endpoint configuration, AWS DMS faces connection errors.

When creating the VPC endpoint, you must select **Endpoint type** as **Gateway** or **Interface** in the DMS Console. For more information, see:
+ [Common AWS DMS prerequisites](#CHAP_VPC_Endpoints.prereq)
+ [Gateway endpoints for Amazon DynamoDB](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html)
+ [How do I troubleshoot connectivity issues with my gateway Amazon VPC endpoints?](https://repost.aws/knowledge-center/connect-s3-vpc-endpoint)

## Setup an Amazon VPC endpoint for Amazon Kinesis
<a name="CHAP_VPC_Endpoints.vpcforkinesis"></a>

When using AWS DMS replication instances in private subnets or AWS DMS serverless replication, you must create a VPC endpoint to establish secure connectivity with Amazon Kinesis. Without a VPC endpoint configuration, AWS DMS faces connection errors. For more information, see:
+ [Common AWS DMS prerequisites](#CHAP_VPC_Endpoints.prereq)
+ [Using Amazon Kinesis Data Streams as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html)

## Setup an Amazon VPC endpoint for Amazon Redshift
<a name="CHAP_VPC_Endpoints.vpcforredshift"></a>

When using AWS DMS replication instances in private subnets or AWS DMS serverless replication, you must create a VPC endpoint to establish secure connectivity with Amazon Redshift. Without a VPC endpoint configuration, AWS DMS faces connection errors. For more information, see:
+ [Common AWS DMS prerequisites](#CHAP_VPC_Endpoints.prereq)
+ [Redshift-managed VPC endpoints](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-cross-vpc.html)

## Setup an Amazon VPC endpoint for Amazon OpenSearch Service
<a name="CHAP_VPC_Endpoints.vpcforos"></a>

When using AWS DMS replication instances in private subnets or AWS DMS serverless replication, you must create a VPC endpoint to establish secure connectivity with Amazon OpenSearch Service. Without a VPC endpoint configuration, AWS DMS faces connection errors. For more information, see:
+ [Common AWS DMS prerequisites](#CHAP_VPC_Endpoints.prereq)
+ [Configuring VPC access for Amazon OpenSearch Ingestion pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security.html)

## Setup replication instances, DMS subnet groups, and DMS Endpoints
<a name="CHAP_VPC_Endpoints.option.123"></a>

You must configure AWS DMS replication resources after creating VPC endpoints. You can set up replication subnet groups for network isolation, replication instances or serverless replications for processing, and endpoints for connecting to source and target databases to enable secure database migration within your VPC.

### Setup an AWS DMS replication instance
<a name="CHAP_VPC_Endpoints.option.123.provisioned"></a>

To configure an AWS DMS provisioned replication instance you must setup DMS replication subnets groups.

**Create DMS replication subnet groups**

1. Sign in to the AWS Management Console and open the DMS console.

1. From the left navigation pane, open to **Subnet groups** and select **Create subnet group**.

1. Enter **Name** and **Description**.

1. From the **VPC** dropdown menu, select the VPC that is running in the same region where you want to create your DMS replication instance.

1. From the **Add subnets** dropdown menu, add the private subnets that you have specified when creating your VPC endpoint. You can identify a private subnet with the subnet ID. For example: `vpc-xxxxxx-subnet-private1-us-west-2a`.

1. Click **Create subnet group**.

**Create DMS replication instance (provisioned)**

1. Navigate to the AWS Management Console to create a replication instance. For more information, see [Creating a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Creating.html). To understand more choosing, sizing, and configuring replication instances, see [Working with an AWS DMS replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html).

1. In the **Connectivity and security** section, select the VPC from the **Virtual private cloud (VPC) for IPv4** or **Dual-stack mode** where you want to create the AWS DMS replication instance. For more information, see [Setting up a network for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html).

1. From the **Replication subnet group** dropdown menu, choose the subnet group that you created for your replication instance.
**Note**  
Ensure the subnets specified for the VPC endpoint are identical to the subnets in the DMS replication instance subnet group. You must remove any subnets from your subnet group that are not associated with VPC endpoint.

1. Uncheck the **Public accessible** checkbox to disable public access.

1. In **Advanced settings** section, from the **VPC security groups** dropdown menu, select all the VPC subnet groups associated with your replication instance. These groups must include the subnet group that includes subnets you specified when creating the VPC endpoint.

   If you do not specify the subnet groups, DMS chooses the default **Replication subnet group** or creates it if it does not exist. For more information, see [Security group configuration for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Advanced.Endpoints.securitygroup.html).

1. Complete the replication instance configuration and select **Create replication instance**.

   You must wait until the status becomes `Available`.

**Create AWS DMS source and target Endpoints**

1. Sign in to the DMS console.

1. Navigate to the **AWS DMS endpoints** and select **Create endpoint**.

1. Create and configure [source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html) and [target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.html) endpoints.

1. In the DMS console, you can choose an existing IAM role or create a new IAM role to access your stored database credentials in the AWS Secrets manager.

1. Click **Run test** to test the endpoint connection in your DMS replication instance. Your replication instance should have `Available` status to run the test with it.

1. Select **Create endpoint**.

### Setup an AWS DMS serverless replication
<a name="CHAP_VPC_Endpoints.option.123.serverless"></a>

To configure an AWS DMS serverless replication you must setup DMS replication subnets groups.

**Create AWS DMS source and target Endpoints**

1. Sign in to the DMS console.

1. Navigate to the **AWS DMS endpoints** and select **Create endpoint**.

1. Create and configure [source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html) and [target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.html) endpoints.

1. In the DMS console, you can choose an existing IAM role or create a new IAM role to access your stored database credentials in the AWS Secrets manager.
**Note**  
For AWS DMS serverless replication, you cannot test the connection for the DMS endpoint or use the `TestConnection` API. The connection test is performed during serverless replication launch between DMS instance and your source/target databases. For more information, see [AWS DMS Serverless components](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.Components.html).

1. Select **Create endpoint**.

**Create DMS replication subnet groups**

1. Sign in to the AWS Management Console and open the DMS console.

1. From the left navigation pane, open to **Subnet groups** and select **Create subnet group**.

1. Enter **Name** and **Description**.

1. From the **VPC** dropdown menu, select the VPC that is running in the same region as your DMS serverless instance.

1. From the **Add subnets** dropdown menu, add the private subnets that you have specified when creating your VPC endpoint. You can identify a private subnet with the subnet ID. For example: `vpc-xxxxxx-subnet-private1-us-west-2a`.

1. Click **Create subnet group**.

**Create DMS serverless replication**

1. Navigate to the DMS console to create a serverless instance. For more information, see [Creating a serverless replication](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.Components.html#CHAP_Serverless.create). To understand more choosing, sizing, and configuring serverless instances, see [Working with AWS DMS serverless](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.html).

1. In the **Connectivity and security** section, select the VPC from the **Virtual private cloud (VPC)** dropdown menu where you want to create the AWS DMS serverless instance . For more information, see [Setting up a network for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html).

1. From the **Subnet group** dropdown menu, choose the subnet group that you created for your serverless instance.
**Note**  
Ensure the subnets specified for the VPC endpoint are identical to the subnets in the DMS serverless instance subnet group. You must remove any subnets from your subnet group that are not associated with your serverless instance.

1. Select **Availability zone**.

1. From the **Maximum DMS capacity units (DCU)** dropdown menu, select the desired DCU capacity.

1. Select **Create task**. This creates a DMS serverless replication configuration that appears in the task list with the status `Start required`.

1. To start serverless replication, choose your task and select **Start** from the **Actions** menu.

## Who is impacted when migrating to AWS DMS versions 3.4.7 and higher?
<a name="CHAP_VPC_Endpoints.Users_Impacted"></a>

You are impacted if you are using one or more of the previously listed AWS DMS endpoints, and these endpoints are not publicly routable or they don’t have VPC endpoints already associated with them.

## Who is not impacted when migrating to AWS DMS versions 3.4.7 and higher?
<a name="CHAP_VPC_Endpoints.Users_Not_Impacted"></a>

You are not impacted if:
+ You aren't using one or more of the previously listed AWS DMS endpoints.
+ You are using any of the previously listed endpoints and they are publicly routable.
+ You are using any of the previously listed endpoints and they have VPC endpoints associated with them.

## Preparing a migration to AWS DMS versions 3.4.7 and higher
<a name="CHAP_VPC_Endpoints.User_Mitigation"></a>

To prevent AWS DMS task failures when you are using any of the endpoints described previously, take one of the steps following prior to upgrading AWS DMS to version 3.4.7 or higher:
+ Make the impacted AWS DMS endpoints publicly routable. For example, add an Internet Gateway (IGW) route to any VPC already used by your AWS DMS replication instance to make all its source and target endpoints publicly routable.
+ Create VPC endpoints to access all source and target endpoints used by AWS DMS as described following.

For any existing VPC endpoints that you use for your AWS DMS source and target endpoints, ensure that they use a trust policy that conforms with the XML policy document, `dms-vpc-role`. For more information on this XML policy document, see [Creating the IAM roles to use with AWS DMS](security-iam.md#CHAP_Security.APIRole).

Otherwise, configure your replication instances as VPC endpoints by adding a VPC endpoint to the VPC containing them. If you configured your replication instances without public endpoints, adding a publicly-accessible VPC endpoint to the VPC that contains your replication instances makes them publicly accessible. You don't need to do anything further to specifically associate your replication instances with the VPC endpoint.

**Note**  
Different services might have unique VPC endpoint configurations. For instance, when using AWS Secrets Manager, you typically don't need to adjust the routing table. Always check the specific requirements for each service.

For more information on configuring VPC endpoints for an AWS DMS replication instance, see [Network configurations for database migration](CHAP_ReplicationInstance.VPC.md#CHAP_ReplicationInstance.VPC.Configurations). For more information on creating interface VPC endpoints for accessing AWS services generally, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*. For information on AWS DMS regional availability for VPC endpoints, see the [AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).