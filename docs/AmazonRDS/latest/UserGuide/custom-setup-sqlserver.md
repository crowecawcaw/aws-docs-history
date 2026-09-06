

# Setting up your environment for Amazon RDS Custom for SQL Server
<a name="custom-setup-sqlserver"></a>

Before you create and manage a DB instance for Amazon RDS Custom for SQL Server DB instance, make sure to perform the following tasks.

**Contents**
+ [Prerequisites for setting up RDS Custom for SQL Server](#custom-setup-sqlserver.review)
  + [Automated instance profile creation using the AWS Management Console](#custom-setup-sqlserver.instanceProfileCreation)
+ [Step 1: Grant required permissions to your IAM principal](#custom-setup-sqlserver.iam-user)
+ [Step 2: Configure networking, instance profile, and encryption](#custom-setup-sqlserver.iam-vpc)
  + [Configuring with CloudFormation](#custom-setup-sqlserver.cf)
    + [Parameters required by CloudFormation](#custom-setup-sqlserver.cf.params)
    + [Download CloudFormation template file](#custom-setup-sqlserver.cf.download)
    + [Configuring resources using CloudFormation](#custom-setup-sqlserver.cf.config)
  + [Configuring manually](#custom-setup-sqlserver.manual)
    + [Make sure that you have a symmetric encryption AWS KMS key](#custom-setup-sqlserver.cmk)
    + [Creating your IAM role and instance profile manually](#custom-setup-sqlserver.iam)
      + [Create the AWSRDSCustomSQLServerInstanceRole IAM role](#custom-setup-sqlserver.iam.create-role)
      + [Add an access policy to AWSRDSCustomSQLServerInstanceRole](#custom-setup-sqlserver.iam.add-policy)
      + [Create your RDS Custom for SQL Server instance profile](#custom-setup-sqlserver.iam.create-profile)
      + [Add AWSRDSCustomSQLServerInstanceRole to your RDS Custom for SQL Server instance profile](#custom-setup-sqlserver.iam.add-profile)
    + [Configuring your VPC manually](#custom-setup-sqlserver.vpc)
      + [Configure your VPC security group](#custom-setup-sqlserver.vpc.sg)
      + [Configure endpoints for dependent AWS services](#custom-setup-sqlserver.vpc.endpoints)
      + [Configure the instance metadata service](#custom-setup-sqlserver.vpc.imds)
+ [Cross-instance restriction](#custom-setup-sqlserver.cross-instance-restriction)

**Note**  
For a step-by-step tutorial on how to set up prerequisites and launch Amazon RDS Custom for SQL Server, see [Get started with Amazon RDS Custom for SQL Server using an CloudFormation template (Network setup)](https://aws.amazon.com/blogs/database/get-started-with-amazon-rds-custom-for-sql-server-using-an-aws-cloudformation-template-network-setup/) and [ Explore the prerequisites required to create an Amazon RDS Custom for SQL Server instance](https://aws.amazon.com/blogs/database/explore-the-prerequisites-required-to-create-an-amazon-rds-custom-for-sql-server-instance/).

## Prerequisites for setting up RDS Custom for SQL Server
<a name="custom-setup-sqlserver.review"></a>

Before creating an RDS Custom for SQL Server DB instance, make sure that your environment meets the requirements described in this topic. You can also use the CloudFormation template to set up the prerequisites within your AWS account. For more information, see [Configuring with CloudFormation](#custom-setup-sqlserver.cf)

RDS Custom for SQL Server requires that you configure the following prerequisites:
+ Configure the AWS Identity and Access Management (IAM) permissions required for instance creation. This is the AWS Identity and Access Management (IAM) user or role needed to make a `create-db-instance` request to RDS.
+ Configure prerequisite resources required by RDS Custom for SQL Server DB instance:
  + Configure the AWS KMS key required for encryption of RDS Custom instance. RDS Custom requires a customer managed key at the time of instance creation for encryption. The KMS key ARN, ID, alias ARN, or alias name is passed as `kms-key-id` parameter in the request to create the RDS Custom DB instance.
  + Configure the permissions required inside RDS Custom for SQL Server DB instance. RDS Custom attaches an instance profile to DB instance at creation and uses it for automation within the DB instance. The instance profile name is set to `custom-iam-instance-profile` in the RDS Custom create request. You can create an instance profile from the AWS Management Console or manually create your instance profile. For more information, see [Automated instance profile creation using the AWS Management Console](#custom-setup-sqlserver.instanceProfileCreation) and [Creating your IAM role and instance profile manually](#custom-setup-sqlserver.iam).
  + Configure the networking setup as per the requirements of RDS Custom for SQL Server. RDS Custom instances reside in the subnets (configured with DB subnet group) that you provide at instance creation. These subnets must allow RDS Custom instances to communicate with services required for RDS automation.

**Note**  
For the requirements mentioned above, make sure there aren't any service control policies (SCPs) restricting account level permissions.  
If the account that you're using is part of an AWS Organization, it might have service control policies (SCPs) restricting account level permissions. Make sure that the SCPs don't restrict the permissions on users and roles that you create using the following procedures.  
For more information about SCPs, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*. Use the [describe-organization](https://docs.aws.amazon.com/cli/latest/reference/organizations/describe-organization.html) AWS CLI command to check whether your account is part of an AWS Organization.  
For more information about AWS Organizations, see [What is AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) in the *AWS Organizations User Guide*.

For general requirements that apply to RDS Custom for SQL Server, see [General requirements for RDS Custom for SQL Server](custom-reqs-limits-MS.md#custom-reqs-limits.reqsMS).

### Automated instance profile creation using the AWS Management Console
<a name="custom-setup-sqlserver.instanceProfileCreation"></a>

RDS Custom requires you to create and configure an instance profile to launch any RDS Custom for SQL Server DB instance. Use the AWS Management Console to create and attach a new instance profile in a single step. This option is available under RDS Custom security section in the **Create database**, **Restore snapshot**, and **Restore to point in time** console pages. Choose **Create a new instance profile** to provide an instance profile name suffix. The AWS Management Console creates a new instance profile that has the permissions required for RDS Custom automation tasks. To automatically create new instance profiles, your logged-in AWS Management Console user must have `iam:CreateInstanceProfile`, `iam:AddRoleToInstanceProfile`, `iam:CreateRole`, and `iam:AttachRolePolicy` permissions.

**Note**  
This option is only available in the AWS Management Console. If you are using the CLI or SDK, use the RDS Custom provided CloudFormation template or manually create an instance profile. For more information, see [Creating your IAM role and instance profile manually](#custom-setup-sqlserver.iam).

## Step 1: Grant required permissions to your IAM principal
<a name="custom-setup-sqlserver.iam-user"></a>

Make sure that you have sufficient access to create an RDS Custom instance. The IAM role or IAM user (referred to as the *IAM principal*) for creating an RDS Custom for SQL Server DB instance using the console or CLI must have either of the following policies for successful DB instance creation:
+ The `AdministratorAccess` policy
+ The `AmazonRDSFullAccess` policy with the following additional permissions:

  ```
  iam:SimulatePrincipalPolicy
  cloudtrail:CreateTrail
  cloudtrail:StartLogging
  s3:CreateBucket
  s3:PutBucketPolicy
  s3:PutBucketObjectLockConfiguration
  s3:PutBucketVersioning 
  kms:CreateGrant
  kms:DescribeKey
  kms:Decrypt
  kms:ReEncryptFrom
  kms:ReEncryptTo
  kms:GenerateDataKeyWithoutPlaintext
  kms:GenerateDataKey
  ec2:DescribeImages
  ec2:RunInstances
  ec2:CreateTags
  ```

  RDS Custom uses these permissions during instance creation. These permissions configure resources in your account that are required for RDS Custom operations.

  For more information about the `kms:CreateGrant` permission, see [AWS KMS key management](Overview.Encryption.Keys.md).

The following sample JSON policy grants the required permissions.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ValidateIamRole",
            "Effect": "Allow",
            "Action": "iam:SimulatePrincipalPolicy",
            "Resource": "*"
        },
        {
            "Sid": "CreateCloudTrail",
            "Effect": "Allow",
            "Action": [
                "cloudtrail:CreateTrail",
                "cloudtrail:StartLogging"
            ],
            "Resource": "arn:aws:cloudtrail:*:*:trail/do-not-delete-rds-custom-*"
        },
        {
            "Sid": "CreateS3Bucket",
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:PutBucketPolicy",
                "s3:PutBucketObjectLockConfiguration",
                "s3:PutBucketVersioning"
            ],
            "Resource": "arn:aws:s3:::do-not-delete-rds-custom-*"
        },
        {
            "Sid": "CreateKmsGrant",
            "Effect": "Allow",
            "Action": [
                "kms:CreateGrant",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The IAM principal requires the following additional permissions to work with custom engine versions (CEVs):

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ConfigureKmsKeyEncryptionPermission",
            "Effect": "Allow",
            "Action": [
                "kms:CreateGrant",
                "kms:DescribeKey",
                "kms:Decrypt",
                "kms:ReEncryptFrom",
                "kms:ReEncryptTo",
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key_id}}"
        },
        {
            "Sid": "CreateEc2Instance",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeImages",
                "ec2:RunInstances",
                "ec2:CreateTags"
            ],
            "Resource": "*"
        }
    ]
}
```

------

Replace {{111122223333}} with the ID of the account that you are using to create your instance. Replace {{us-east-1}} with the AWS Region you are using to create your instance. Replace {{key\_id}} with your customer managed key ID. You can add multiple keys as required. 

For more information about the resource-level permissions that are required to launch an EC2 instance, see [Launch instances (RunInstances)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html#iam-example-runinstances). 

Also, the IAM principal requires the `iam:PassRole` permission on the IAM role. That must be attached to the instance profile passed in the `custom-iam-instance-profile` parameter in the request to create the RDS Custom DB instance. The instance profile and its attached role are created later in [Step 2: Configure networking, instance profile, and encryption](#custom-setup-sqlserver.iam-vpc).

**Note**  
Make sure that the previously listed permissions aren't restricted by service control policies (SCPs), permission boundaries, or session policies associated with the IAM principal.

## Step 2: Configure networking, instance profile, and encryption
<a name="custom-setup-sqlserver.iam-vpc"></a>

You can configure your IAM instance profile role, virtual private cloud (VPC), and AWS KMS symmetric encryption key by using either of the following processes:
+ [Configuring with CloudFormation](#custom-setup-sqlserver.cf) (recommended)
+ [Configuring manually](#custom-setup-sqlserver.manual)

**Note**  
If your account is part of any AWS Organizations, make sure that the permissions required by the instance profile role aren't restricted by service control policies (SCPs).  
The networking configurations in this topic work best with DB instances that aren't publicly accessible. You can't connect directly to such DB instances from outside the VPC.

### Configuring with CloudFormation
<a name="custom-setup-sqlserver.cf"></a>

To simplify setup, you can use an CloudFormation template file to create a CloudFormation stack. A CloudFormation template creates all the networking, instance profiles, and encryption resources according the requirements of RDS Custom.

To learn how to create stacks, see [Creating a stack on the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the *CloudFormation User Guide*.

For a tutorial on how to launch Amazon RDS Custom for SQL Server using an CloudFormation template, see [Get started with Amazon RDS Custom for SQL Server using an CloudFormation template](https://aws.amazon.com/blogs/database/get-started-with-amazon-rds-custom-for-sql-server-using-an-aws-cloudformation-template-network-setup/) in the *AWS Database Blog *.

**Topics**
+ [Parameters required by CloudFormation](#custom-setup-sqlserver.cf.params)
+ [Download CloudFormation template file](#custom-setup-sqlserver.cf.download)
+ [Configuring resources using CloudFormation](#custom-setup-sqlserver.cf.config)

#### Parameters required by CloudFormation
<a name="custom-setup-sqlserver.cf.params"></a>

The following parameters are required to configure RDS Custom prerequisite resources with CloudFormation:



- **Availability Configuration**
  - **Parameter name:** Select an availability configuration for prerequisites setup
  - **Default Value:** Multi-AZ
  - **Description:** Specify whether to setup prerequisites in Single-AZ or Multi-AZ configuration for RDS Custom instances. You should use Multi-AZ configuration if you require at least one Multi-AZ DB instance in this configuration

- **Network Configuration**
  - **Parameter name:** IPv4 CIDR block for VPC / **Default Value:** 10.0.0.0/16 / **Description:** Specify an IPv4 CIDR block (or IP address range) for your VPC. This VPC is configured to create and work with RDS Custom DB instance.
  - **Parameter name:** IPv4 CIDR block for 1 of 2 private subnets / **Default Value:** 10.0.128.0/20 / **Description:** Specify an IPv4 CIDR block (or IP address range) for your first private subnet. This is one of the two subnets in which the RDS Custom DB instance can be created. This is a private subnet with no access to internet.
  - **Parameter name:** IPv4 CIDR block for 2 of 2 private subnets / **Default Value:** 10.0.144.0/20 / **Description:** Specify an IPv4 CIDR block (or IP address range) for your second private subnet. This is one of the two subnets in which the RDS Custom DB instance can be created. This is a private subnet with no access to internet.
  - **Parameter name:** IPv4 CIDR block for public subnet / **Default Value:** 10.0.0.0/20 / **Description:** Specify an IPv4 CIDR block (or IP address range) for your public subnet. This is one of the subnet in which the EC2 instance can connect with RDS Custom DB instance can be created. This is a public subnet with access to internet.

- **RDP Access Configuration**
  - **Parameter name:** IPv4 CIDR block of your source / **Default Value:** ‐ / **Description:** Specify an IPv4 CIDR block (or IP address range) of your source. This is the IP range from where you make RDP connection to EC2 instance in the public subnet. If not set, RDP connection to EC2 instance is not configured.
  - **Parameter name:** Setup RDP access to RDS Custom for SQL Server instance  / **Default Value:** No / **Description:** Specify whether to enable the RDP connection from the EC2 instance to the RDS Custom for SQL Server instance. By default, RDP connection from the EC2 instance to the DB instance is not configured.



#### Resources created by CloudFormation
<a name="custom-setup-sqlserver.cf.list"></a>

Successfully creating the CloudFormation stack using default settings creates the following resources in your AWS account:
+ Symmetric encryption KMS key for encryption of data managed by RDS Custom.
+ The instance profile is is associated to an IAM role with `AmazonRDSCustomInstanceProfileRolePolicy` to provide permissions required by RDS Custom. For more information, see [AmazonRDSCustomServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSCustomServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.
+ VPC with the CIDR range specified as the CloudFormation parameter. The default value is `10.0.0.0/16`.
+ Two private subnets with the CIDR range specified in the parameters, and two different Availability Zones in the AWS Region. The default values for the subnet CIDRs are `10.0.128.0/20` and `10.0.144.0/20`.
+ One public subnet with the CIDR range specified in the parameters. The default value for the subnet CIDR is 10.0.0.0/20. The EC2 instance resides in this subnet and can be used to connect to the RDS Custom instance. 
+ DHCP option set for the VPC with domain name resolution to an Amazon Domain Name System (DNS) server.
+ Route table to associate with two private subnets and no access to the internet.
+ Route table to associate with public subnet and has access to the internet.
+ Internet gateway associated with the VPC to allow internet access to public subnet.
+ Network access control list (ACL) to associate with two private subnets and access restricted to HTTPS and DB port within VPC.
+ VPC security group to be associated with the RDS Custom instance. Access is restricted for outbound HTTPS to AWS service endpoints that are required by RDS Custom and inbound DB port from EC2 instance security group.
+ VPC security group to be associated with the EC2 instance in public subnet. Access is restricted for outbound DB port to RDS Custom instance security group.
+ VPC security group to be associated with VPC endpoints that are created for AWS service endpoints that are required by RDS Custom.
+ DB subnet group in which RDS Custom instances are created. Two private subnets created by this template are added to the DB subnet group.
+ VPC endpoints for each of the AWS service endpoints that are required by RDS Custom.

Setting availability configuration to multi-az will create following resources in addition to above list:
+ Network ACL rules allowing communication between private subnets.
+ Inbound and outbound access to Multi-AZ port within VPC security group associated with the RDS Custom instance.
+ VPC endpoints to AWS service endpoint(s) that are required for Multi-AZ communication.

In addition, setting RDP access configuration creates the following resources:
+ Configuring RDP access to public subnet from your source IP address:
  + Network ACL rules that allow RDP connection from your source IP to public subnet.
  + Ingress access to RDP port from your source IP to VPC security group associated with the EC2 instance.
+ Configuring RDP access from EC2 instance in public subnet to RDS Custom Instance in private subnets:
  + Network ACL rules allowing RDP connection from public subnet to private subnets.
  + Inbound access to RDP port from VPC security group associated with the EC2 instance to VPC security group associated with the RDS Custom Instance.

Use the following procedures to create the CloudFormation stack for RDS Custom for SQL Server.

#### Download CloudFormation template file
<a name="custom-setup-sqlserver.cf.download"></a>

**To download the template file**

1. Open the context (right-click) menu for the link [ custom-sqlserver-onboard.zip](samples/custom-sqlserver-onboard.zip) and choose **Save Link As**.

1. Save and extract the file to your computer.

#### Configuring resources using CloudFormation
<a name="custom-setup-sqlserver.cf.config"></a>

**To configure resources using CloudFormation**

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. To start the Create Stack wizard, choose **Create Stack**.

   The **Create stack** page appears.

1. For **Prerequisite - Prepare template**, choose **Template is ready**.

1. For **Specify template**, do the following:

   1. For **Template source**, choose **Upload a template file**.

   1. For **Choose file**, navigate to and then choose the correct file.

1. Choose **Next**.

   The **Specify stack details** page appears.

1. For **Stack name**, enter **rds-custom-sqlserver**.

1. For **Parameters**, do the following:

   1. To keep the default options, choose **Next**.

   1. To change options, choose the appropriate availability configuration, networking configuration, and RDP access configuration, and then choose **Next**.

      Read the description of each parameter carefully before changing parameters.
**Note**  
If you choose to create at least one Multi-AZ instance in this CloudFormation stack, make sure that the CloudFormation stack parameter **Select an availability configuration for prerequisites setup** is set to `Multi-AZ`. If you create the CloudFormation stack as Single-AZ, update the CloudFormation stack to Multi-AZ configuration before creating the first Multi-AZ instance.

1. On the **Configure stack options page**, choose **Next.**

1. On the **Review rds-custom-sqlserver** page, do the following:

   1. For **Capabilities**, select the ****I acknowledge that CloudFormation might create IAM resources with custom names**** check box.

   1. Choose **Create stack**.

**Note**  
Do not update the resources created from this CloudFormation stack directly from the resource pages. This prevents you from applying future updates to these resources by using a CloudFormation template.

CloudFormation creates the resources that RDS Custom for SQL Server requires. If the stack creation fails, read through the **Events** tab to see which resource creation failed and its status reason.

The **Outputs** tab for this CloudFormation stack in the console should have information about all resources to be passed as parameters for creating an RDS Custom for SQL Server DB instance. Make sure to use the VPC security group and DB subnet group created by CloudFormation for RDS Custom DB instances. By default, RDS tries to attach the default VPC security group, which might not have the access that you need.

If you used CloudFormation to create resources, you can skip [Configuring manually](#custom-setup-sqlserver.manual).

#### Updating the CloudFormation stack
<a name="custom-setup-sqlserver.cf.update"></a>

You can also update some of the configuration on the CloudFormation stack after creation. The configurations that can be updated are:
+ Availability Configuration for RDS Custom for SQL Server
  + **Select an availability configuration for prerequisites setup**: Update this parameter to switch between Single-AZ and Multi-AZ configuration. If you are using this CloudFormation stack for at least one Multi-AZ instance, you must update the stack to choose Multi-AZ configuration.
+ RDP Access Configuration for RDS Custom for SQL Server
  + IPv4 CIDR block of your source: You can update the IPv4 CIDR block (or IP address range) of your source by updating this parameter. Setting this parameter to blank removes RDP access configuration from your source CIDR block to public subnet. 
  + Setup RDP access to RDS Custom for SQL Server: Enable or disable the RDP connection from the EC2 instance to the RDS Custom for SQL Server instance.

#### Deleting the CloudFormation stack
<a name="custom-setup-sqlserver.cf.delete"></a>

You can delete the CloudFormation stack after deleting all the RDS Custom instances that uses resources from the stack. RDS Custom doesn’t keep track of the CloudFormation stack, hence it doesn't block deletion of the stack when there are DB instances that uses stack resources. Make sure that there are no RDS Custom DB instances that uses the stack resources when deleting the stack.

**Note**  
When you delete a CloudFormation stack, all of the resources created by the stack are deleted except the KMS key. The KMS key goes into a pending-deletion state and is deleted after 30 days. To keep the KMS key, perform a [CancelKeyDeletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_CancelKeyDeletion.html) operation during the 30-day grace period.

### Configuring manually
<a name="custom-setup-sqlserver.manual"></a>

If you choose to configure resources manually, perform the following tasks.

**Note**  
To simplify setup, you can use the CloudFormation template file to create a CloudFormation stack rather than a manual configuration. For more information, see [Configuring with CloudFormation](#custom-setup-sqlserver.cf).  
You can also use the AWS CLI to complete this section. If so, download and install the latest CLI.

**Topics**
+ [Make sure that you have a symmetric encryption AWS KMS key](#custom-setup-sqlserver.cmk)
+ [Creating your IAM role and instance profile manually](#custom-setup-sqlserver.iam)
+ [Configuring your VPC manually](#custom-setup-sqlserver.vpc)

#### Make sure that you have a symmetric encryption AWS KMS key
<a name="custom-setup-sqlserver.cmk"></a>

A symmetric encryption AWS KMS key is required for RDS Custom. When you create an RDS Custom for SQL Server DB instance, make sure to supply the KMS key identifier as parameter `kms-key-id`. For more information, see [Creating and connecting to a DB instance for Amazon RDS Custom for SQL Server](custom-creating-sqlserver.md).

You have the following options:
+ If you have an existing customer managed KMS key in your AWS account, you can use it with RDS Custom. No further action is necessary.
+ If you already created a customer managed symmetric encryption KMS key for a different RDS Custom engine, you can reuse the same KMS key. No further action is necessary.
+ If you don't have an existing customer managed symmetric encryption KMS key in your account, create a KMS key by following the instructions in [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*.
+ If you're creating a CEV or RDS Custom DB instance, and your KMS key is in a different AWS account, make sure to use the AWS CLI. You can't use the AWS console with cross-account KMS keys.

**Important**  
RDS Custom doesn't support AWS managed KMS keys.

Make sure that your symmetric encryption key grants access to the `kms:Decrypt` and `kms:GenerateDataKey` operations to the AWS Identity and Access Management (IAM) role in your IAM instance profile. If you have a new symmetric encryption key in your account, no changes are required. Otherwise, make sure that your symmetric encryption key's policy grants access to these operations.

For more information, see [Step 4: Configure IAM for RDS Custom for Oracle](custom-setup-orcl.md#custom-setup-orcl.iam-vpc).

#### Creating your IAM role and instance profile manually
<a name="custom-setup-sqlserver.iam"></a>

You can manually create an instance profile and use it to launch RDS Custom instances. If you plan to create the instance in the AWS Management Console, skip this section. The AWS Management Console allows you to create and attach an instance profile to your RDS Custom DB instances. For more information, see [Automated instance profile creation using the AWS Management Console](#custom-setup-sqlserver.instanceProfileCreation). 

When you manually create an instance profile, pass the instance profile name as the `custom-iam-instance-profile` parameter to your `create-db-instance` CLI command. RDS Custom uses the role associated with this instance profile to run automation to manage the instance.

**To create the IAM instance profile and IAM roles for RDS Custom for SQL Server**

1. Create the IAM role named `AWSRDSCustomSQLServerInstanceRole` with a trust policy that lets Amazon EC2 assume this role.

1. Add the AWS Managed Policy `AmazonRDSCustomInstanceProfileRolePolicy` to `AWSRDSCustomSQLServerInstanceRole`.

1. Create an IAM instance profile for RDS Custom for SQL Server that is named `AWSRDSCustomSQLServerInstanceProfile`.

1. Add `AWSRDSCustomSQLServerInstanceRole` to the instance profile.

##### Create the AWSRDSCustomSQLServerInstanceRole IAM role
<a name="custom-setup-sqlserver.iam.create-role"></a>

The following example creates the `AWSRDSCustomSQLServerInstanceRole` role. The trust policy lets Amazon EC2 assume the role.

```
aws iam create-role \
    --role-name AWSRDSCustomSQLServerInstanceRole \
    --assume-role-policy-document '{
        "Version": "2012-10-17",		 	 	 
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Effect": "Allow",
              "Principal": {
                  "Service": "ec2.amazonaws.com"
              }
            }
          ]
        }'
```

##### Add an access policy to AWSRDSCustomSQLServerInstanceRole
<a name="custom-setup-sqlserver.iam.add-policy"></a>

To provide the required permissions, attach the AWS managed policy `AmazonRDSCustomInstanceProfileRolePolicy` to `AWSRDSCustomSQLServerInstanceRole`. `AmazonRDSCustomInstanceProfileRolePolicy` allows RDS Custom instances to send and receive messages, and perform various automation actions.

**Note**  
Make sure that the permissions in the access policy aren't restricted by SCPs or permission boundaries associated with the instance profile role.

The following example attaches AWS managed policy `AmazonRDSCustomInstanceProfileRolePolicy` to the `AWSRDSCustomSQLServerInstanceRole` role.

```
aws iam attach-role-policy \
    --role-name AWSRDSCustomSQLServerInstanceRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonRDSCustomInstanceProfileRolePolicy
```

##### Create your RDS Custom for SQL Server instance profile
<a name="custom-setup-sqlserver.iam.create-profile"></a>

An instance profile is a container that includes a single IAM role. RDS Custom uses the instance profile to pass the role to the instance.

If you use the AWS Management Console to create a role for Amazon EC2, the console automatically creates an instance profile and gives it the same name as the role when the role is created. Create your instance profile as follows, naming it `AWSRDSCustomSQLServerInstanceProfile`.

```
aws iam create-instance-profile \
    --instance-profile-name AWSRDSCustomSQLServerInstanceProfile
```

##### Add AWSRDSCustomSQLServerInstanceRole to your RDS Custom for SQL Server instance profile
<a name="custom-setup-sqlserver.iam.add-profile"></a>

Add the `AWSRDSCustomInstanceRoleForRdsCustomInstance` role to the previously created `AWSRDSCustomSQLServerInstanceProfile` profile.

```
aws iam add-role-to-instance-profile \
    --instance-profile-name AWSRDSCustomSQLServerInstanceProfile \
    --role-name AWSRDSCustomSQLServerInstanceRole
```

#### Configuring your VPC manually
<a name="custom-setup-sqlserver.vpc"></a>

Your RDS Custom DB instance is in a virtual private cloud (VPC) based on the Amazon VPC service, just like an Amazon EC2 instance or Amazon RDS instance. You provide and configure your own VPC. Thus, you have full control over your instance networking setup.

RDS Custom sends communication from your DB instance to other AWS services. Make sure the following services are accessible from the subnet in which you create your RDS Custom DB instances:
+ Amazon CloudWatch (`com.amazonaws.{{region}}.monitoring`)
+ Amazon CloudWatch Logs (`com.amazonaws.{{region}}.logs`)
+ Amazon CloudWatch Events (`com.amazonaws.{{region}}.events`)
+ Amazon EC2 (`com.amazonaws.{{region}}.ec2` and `com.amazonaws.{{region}}.ec2messages`)
+ Amazon S3 (`com.amazonaws.{{region}}.s3`)
+ AWS Secrets Manager (`com.amazonaws.{{region}}.secretsmanager`)
+ AWS Systems Manager (`com.amazonaws.{{region}}.ssm` and `com.amazonaws.{{region}}.ssmmessages`)

If creating Multi-AZ deployments
+ Amazon Simple Queue Service (`com.amazonaws.{{region}}.sqs`)

If RDS Custom can't communicate with the necessary services, it publishes the following events:

```
Database instance in incompatible-network. SSM Agent connection not available. Amazon RDS can't connect to the dependent AWS services.
```

```
Database instance in incompatible-network. Amazon RDS can't connect to dependent AWS services. Make sure port 443 (HTTPS) allows outbound connections, and try again. "Failed to connect to the following services: s3 events"
```

To avoid `incompatible-network` errors, make sure that VPC components involved in communication between your RDS Custom DB instance and AWS services satisfy the following requirements:
+ The DB instance can make outbound connections on port 443 to other AWS services.
+ The VPC allows incoming responses to requests originating from your RDS Custom DB instance.
+ RDS Custom can correctly resolve the domain names of endpoints for each AWS service.

If you already configured a VPC for a different RDS Custom DB engine, you can reuse that VPC and skip this process.

**Topics**
+ [Configure your VPC security group](#custom-setup-sqlserver.vpc.sg)
+ [Configure endpoints for dependent AWS services](#custom-setup-sqlserver.vpc.endpoints)
+ [Configure the instance metadata service](#custom-setup-sqlserver.vpc.imds)

##### Configure your VPC security group
<a name="custom-setup-sqlserver.vpc.sg"></a>

A *security group* acts as a virtual firewall for a VPC instance, controlling both inbound and outbound traffic. An RDS Custom DB instance has a security group attached to its network interface that protects the instance. Make sure that your security group permits traffic between RDS Custom and other AWS services through HTTPS. You pass this security group as the `vpc-security-group-ids` parameter in the instance creation request.

**To configure your security group for RDS Custom**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com/vpc). 

1. Allow RDS Custom to use the default security group, or create your own security group.

   For detailed instructions, see [Provide access to your DB instance in your VPC by creating a security group](CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup).

1. Make sure that your security group permits outbound connections on port 443. RDS Custom needs this port to communicate with dependent AWS services.

1. If you have a private VPC and use VPC endpoints, make sure that the security group associated with the DB instance allows outbound connections on port 443 to VPC endpoints. Also make sure that the security group associated with the VPC endpoint allows inbound connections on port 443 from the DB instance.

   If incoming connections aren't allowed, the RDS Custom instance can't connect to the AWS Systems Manager and Amazon EC2 endpoints. For more information, see [Create a Virtual Private Cloud endpoint](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html) in the *AWS Systems Manager User Guide*.

1. For RDS Custom for SQL Server Multi-AZ instances, make sure that the security group associated with the DB instance allows inbound and outbound connections on port 1120 to this security group itself. This is required for peer host connection on a Multi-AZ RDS Custom for SQL Server DB instance. 

For more information about security groups, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC Developer Guide*.

##### Configure endpoints for dependent AWS services
<a name="custom-setup-sqlserver.vpc.endpoints"></a>

We recommend that you add endpoints for every service to your VPC using the following instructions. However, you can use any solution that lets your VPC communicate with AWS service endpoints. For example, you can use Network Address Translation (NAT) or AWS Direct Connect.

**To configure endpoints for AWS services with which RDS Custom works**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation bar, use the Region selector to choose the AWS Region.

1. In the navigation pane, choose **Endpoints**. In the main pane, choose **Create Endpoint**.

1. For **Service category**, choose **AWS services**.

1. For **Service Name**, choose the endpoint shown in the table.

1. For **VPC**, choose your VPC.

1. For **Subnets**, choose a subnet from each Availability Zone to include.

   The VPC endpoint can span multiple Availability Zones. AWS creates an elastic network interface for the VPC endpoint in each subnet that you choose. Each network interface has a Domain Name System (DNS) host name and a private IP address.

1. For **Security group**, choose or create a security group.

   You can use security groups to control access to your endpoint, much as you use a firewall. Make sure that the security group allows inbound connections on port 443 from the DB instances. For more information about security groups, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*. 

1. Optionally, you can attach a policy to the VPC endpoint. Endpoint policies can control access to the AWS service to which you are connecting. The default policy allows all requests to pass through the endpoint. If you're using a custom policy, make sure that requests from the DB instance are allowed in the policy.

1. Choose **Create endpoint**.

The following table explains how to find the list of endpoints that your VPC needs for outbound communications.


| Service | Endpoint format | Notes and links | 
| --- | --- | --- | 
| AWS Systems Manager | Use the following endpoint formats:+  `ssm.{{region}}.amazonaws.com` <br />+  `ssmmessages.{{region}}.amazonaws.com`  | For the list of endpoints in each Region, see [AWS Systems Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html) in the *Amazon Web Services General Reference*. | 
| AWS Secrets Manager | Use the endpoint format `secretsmanager.{{region}}.amazonaws.com`. | For the list of endpoints in each Region, see [AWS Secrets Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/asm.html) in the *Amazon Web Services General Reference*. | 
| Amazon CloudWatch | Use the following endpoint formats:+  For CloudWatch metrics, use `monitoring.{{region}}.amazonaws.com` <br />+  For CloudWatch Events, use `events.{{region}}.amazonaws.com` <br />+  For CloudWatch Logs, use `logs.{{region}}.amazonaws.com`  | For the list of endpoints in every Region, see: +  [Amazon CloudWatch endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cw_region.html) in the *Amazon Web Services General Reference* <br />+  [Amazon CloudWatch Logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html) in the *Amazon Web Services General Reference* <br />+  [Amazon CloudWatch Events endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwe_region.html) in the *Amazon Web Services General Reference*  | 
| Amazon EC2 | Use the following endpoint formats:+  `ec2.{{region}}.amazonaws.com` <br />+  `ec2messages.{{region}}.amazonaws.com`  | For the list of endpoints in each Region, see [Amazon Elastic Compute Cloud endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ec2-service.html) in the *Amazon Web Services General Reference*. | 
| Amazon S3 | Use the endpoint format `s3.{{region}}.amazonaws.com`. | For the list of endpoints in each Region, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the *Amazon Web Services General Reference*. <br />To learn more about gateway endpoints for Amazon S3, see [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) in the *Amazon VPC Developer Guide*. <br />To learn how to create an access point, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/access-points-create-ap.html) in the *Amazon VPC Developer Guide*.<br />To learn how to create a gateway endpoints for Amazon S3, see [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html). | 
| Amazon Simple Queue Service | Use the endpoint format sqs.{{region}}.amazonaws.com | For the list of endpoints in each Region, see [Amazon Simple Queue Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html). | 

##### Configure the instance metadata service
<a name="custom-setup-sqlserver.vpc.imds"></a>

Make sure that your instance can do the following:
+ Access the instance metadata service using Instance Metadata Service Version 2 (IMDSv2).
+ Allow outbound communications through port 80 (HTTP) to the IMDS link IP address.
+ Request instance metadata from `http://169.254.169.254`, the IMDSv2 link.

For more information, see [Use IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.

## Cross-instance restriction
<a name="custom-setup-sqlserver.cross-instance-restriction"></a>

When you create an instance profile by following the steps above, it uses the AWS managed policy `AmazonRDSCustomInstanceProfileRolePolicy` to provide the required permissions to RDS Custom which allows instance management and monitoring automation. The managed policy ensures that the permissions allow access to only those resources which RDS Custom requires to run automation. We recommend using the managed policy to support new features and address security requirements which are automatically applied to existing instance profiles without manual intervention. For more information, see [AWS managed policy: AmazonRDSCustomInstanceProfileRolePolicy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-security-iam-awsmanpol.html#rds-security-iam-awsmanpol-AmazonRDSCustomInstanceProfileRolePolicy).

The `AmazonRDSCustomInstanceProfileRolePolicy` managed policy restricts the instance profile to have cross-account access but it might allow access to some RDS Custom managed resources across RDS Custom instances within the same account. Based on your requirement, you can use permission boundaries to further restrict cross-instance access. Permission boundaries define the maximum permissions that the identity-based policies can grant to an entity, but doesn't grant permissions by themselves. For more information, see [ Evaluating effective permissions with boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html#access_policies_boundaries-eval-logic).

For example, the following boundary policy restricts instance profile role to access a specific AWS KMS key and limits access to RDS Custom managed resources across instances which are using different AWS KMS keys.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DenyOtherKmsKeyAccess",
            "Effect": "Deny",
            "Action": "kms:*",
            "NotResource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{KMS_key_ID}}"
        }
    ]
}
```

------

**Note**  
Make sure the permissions boundary does not block any permissions that `AmazonRDSCustomInstanceProfileRolePolicy` grants to RDS Custom.