# Setting up your environment for Amazon RDS Custom for Oracle

Before you create an Amazon RDS Custom for Oracle DB instance, perform the following tasks.

###### Topics

- [Step 1: Create or reuse a symmetric encryption
  AWS KMS key](#custom-setup-orcl.cmk "#custom-setup-orcl.cmk")
- [Step 2: Download and install the AWS CLI](#custom-setup-orcl.cli "#custom-setup-orcl.cli")
- [Step 3: Extract the CloudFormation
  templates for RDS Custom for Oracle](#custom-setup-orcl.cf.downloading "#custom-setup-orcl.cf.downloading")
- [Step 4: Configure IAM for
  RDS Custom for Oracle](#custom-setup-orcl.iam-vpc "#custom-setup-orcl.iam-vpc")
- [Step 5: Grant required permissions to your
  IAM user or role](#custom-setup-orcl.iam-user "#custom-setup-orcl.iam-user")
- [Step 6: Configure your VPC for
  RDS Custom for Oracle](#custom-setup-orc.vpc-config "#custom-setup-orc.vpc-config")

## Step 1: Create or reuse a symmetric encryption

AWS KMS key

_Customer managed keys_ are AWS KMS keys in your AWS account
that you create, own, and manage. A customer managed symmetric encryption KMS key is
required for RDS Custom. When you create an RDS Custom for Oracle DB instance, you supply the KMS key
identifier. For more information, see [Configuring a DB instance for Amazon RDS Custom for Oracle](custom-creating.md "custom-creating.md").

You have the following options:

- If you have an existing customer managed KMS key in your AWS account, you can
  use it with RDS Custom. No further action is necessary.
- If you already created a customer managed symmetric encryption KMS key for a
  different RDS Custom engine, you can reuse the same KMS key. No further action is
  necessary.
- If you don't have an existing customer managed symmetric encryption KMS key in
  your account, create a KMS key by following the instructions in [Creating
  keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.
- If you're creating a CEV or RDS Custom DB instance, and your KMS key is in a
  different AWS account, make sure to use the AWS CLI. You can't use the AWS console
  with cross-account KMS keys.

###### Important

RDS Custom doesn't support AWS managed KMS keys.

Make sure that your symmetric encryption key grants access to the `kms:Decrypt`
and `kms:GenerateDataKey` operations to the AWS Identity and Access Management (IAM) role in your IAM
instance profile. If you have a new symmetric encryption key in your account, no changes are
required. Otherwise, make sure that your symmetric encryption key's policy grants access to
these operations.

For more information, see [Step 4: Configure IAM for
RDS Custom for Oracle](#custom-setup-orcl.iam-vpc "#custom-setup-orcl.iam-vpc").

For more information about configuring IAM for RDS Custom for Oracle, see [Step 4: Configure IAM for
RDS Custom for Oracle](#custom-setup-orcl.iam-vpc "#custom-setup-orcl.iam-vpc").

## Step 2: Download and install the AWS CLI

AWS provides you with a command-line interface to use RDS Custom features. You can use either version 1 or version 2 of the
AWS CLI.

For information about downloading and installing the AWS CLI, see [Installing or updating the latest version of the
AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

Skip this step if either of the following is true:

- You plan to access RDS Custom only from the AWS Management Console.
- You have already downloaded the AWS CLI for Amazon RDS or a different RDS Custom
  DB engine.

## Step 3: Extract the CloudFormation

templates for RDS Custom for Oracle

To simplify setup, we strongly recommend that you use CloudFormation templates to create
CloudFormation stacks. If you plan to configure IAM and your VPC manually, skip this
step.

###### Topics

- [Step 3a: Download the CloudFormation
  template files](#custom-setup-orcl.cf.dl-templates "#custom-setup-orcl.cf.dl-templates")
- [Step 3b: Extract
  custom-oracle-iam.json](#custom-setup-orcl.cf.downloading.ca-role "#custom-setup-orcl.cf.downloading.ca-role")
- [Step 3c: Extract
  custom-vpc.json](#custom-setup-orcl.cf.downloading.ca-pn "#custom-setup-orcl.cf.downloading.ca-pn")

### Step 3a: Download the CloudFormation

template files

A _CloudFormation template_ is a declaration of the AWS
resources that make up a stack. The template is stored as a JSON file.

###### To download the CloudFormation template files

1. Open the context (right-click) menu for the link [custom-oracle-iam.zip](samples/custom-oracle-iam.md "samples/custom-oracle-iam.md") and
   choose **Save Link As**.
2. Save the file to your computer.
3. Repeat the previous steps for the link [custom-vpc.zip](samples/custom-vpc.md "samples/custom-vpc.md").

If you already configured your VPC for RDS Custom, skip this step.

### Step 3b: Extract

custom-oracle-iam.json

Open the `custom-oracle-iam.zip` file that you downloaded, and
then extract the file `custom-oracle-iam.json`. The beginning of
the file looks like the following.

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "EncryptionKey": {
      "Type": "String",
      "Default": "*",
      "Description": "KMS Key ARN for encryption of data managed by RDS Custom and by DB Instances."
    }
  },
  "Resources": {
    "RDSCustomInstanceServiceRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "RoleName": { "Fn::Sub": "AWSRDSCustomInstanceRole-${AWS::Region}" },
        "AssumeRolePolicyDocument": {
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
        },...
```

### Step 3c: Extract

custom-vpc.json

###### Note

If you already configured an existing VPC for RDS Custom for Oracle, skip this step. For
more information, see [Configure your VPC manually for
RDS Custom for Oracle](#custom-setup-orcl.vpc "#custom-setup-orcl.vpc").

Open the `custom-vpc.zip` ﬁle that you downloaded, and then extract the
ﬁle `custom-vpc.json`. The beginning of the file looks like the
following.

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "PrivateVpc": {
      "Type": "AWS::EC2::VPC::Id",
      "Description": "Private VPC Id to use for RDS Custom DB Instances"
    },
    "PrivateSubnets": {
      "Type": "List<AWS::EC2::Subnet::Id>",
      "Description": "Private Subnets to use for RDS Custom DB Instances"
    },
    "RouteTable": {
      "Type": "String",
      "Description": "Route Table that must be associated with the PrivateSubnets and used by S3 VPC Endpoint",
      "AllowedPattern": "rtb-[0-9a-z]+"
    }
  },
  "Resources": {
    "DBSubnetGroup": {
      "Type": "AWS::RDS::DBSubnetGroup",
      "Properties": {
        "DBSubnetGroupName": "rds-custom-private",
        "DBSubnetGroupDescription": "RDS Custom Private Network",
        "SubnetIds": {
          "Ref": "PrivateSubnets"
        }
      }
    },...
```

## Step 4: Configure IAM for

RDS Custom for Oracle

You use an IAM role or IAM user (known as an _IAM entity_) to
create an RDS Custom DB instance using the console or AWS CLI. This IAM entity must have the
necessary permissions for instance creation.

You can configure IAM using either CloudFormation or manual steps.

###### Important

We strongly recommend that you configure your RDS Custom for Oracle environment using CloudFormation.
This technique is the easiest and least error-prone.

###### Topics

- [Configure IAM using
  CloudFormation](#custom-setup-orcl.cf.config-iam "#custom-setup-orcl.cf.config-iam")
- [Create your IAM role and instance profile
  manually](#custom-setup-orcl.iam "#custom-setup-orcl.iam")

### Configure IAM using

CloudFormation

When you use the CloudFormation template for IAM, it creates the following required
resources:

- An instance profile named
  `AWSRDSCustomInstanceProfile-`region``
- A service role named
  `AWSRDSCustomInstanceRole-`region``
- An access policy named `AWSRDSCustomIamRolePolicy` that is
  attached to the service role

###### To configure IAM using CloudFormation

1.  Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2.  Start the Create Stack wizard, and choose **Create
    Stack**.
3.  On the **Create stack** page, do the following:
    1. For **Prepare template**, choose
       **Template is ready**.
    2. For **Template source**, choose **Upload
       a template file**.
    3. For **Choose file**, navigate to, then choose
       **custom-oracle-iam.json**.
    4. Choose **Next**.

4.  On the **Specify stack details** page, do the
    following:
    1. For **Stack name**, enter
       `custom-oracle-iam`.
    2. Choose **Next**.

5.  On the **Configure stack options page**, choose
    **Next**.
6.  On the **Review custom-oracle-iam** page, do the
    following:
    1. Select the \***\*I acknowledge that
       CloudFormation might create IAM resources with custom
       names\*\*** check box.
    2. Choose **Submit**.CloudFormation creates the IAM roles that RDS Custom for Oracle requires. In the left
       panel, when **custom-oracle-iam** shows
       **CREATE_COMPLETE**, proceed to the next step.

7.  In the left panel, choose **custom-oracle-iam**. In the
    right panel, do the following:
    1.  Choose **Stack info**. Your stack has an ID in
        the format
        **arn:aws:cloudformation:`region`:`account-no`:stack/custom-oracle-iam/`identifier`**.
    2.  Choose **Resources**. You should see the
        following:

            * An instance profile named
             **AWSRDSCustomInstanceProfile-`region`**
            * A service role named
             **AWSRDSCustomInstanceRole-`region`**

        When you create your RDS Custom DB instance, you need to supply the instance
        profile ID.

### Create your IAM role and instance profile

manually

Configuration is easiest when you use CloudFormation. However, you can also configure
IAM manually. For manual setup, do the following:

- [Step 1: Create the IAM
  role AWSRDSCustomInstanceRoleForRdsCustomInstance](#custom-setup-orcl.iam.create-role "#custom-setup-orcl.iam.create-role").
- [Step 2: Add an access policy
  to AWSRDSCustomInstanceRoleForRdsCustomInstance](#custom-setup-orcl.iam.add-policy "#custom-setup-orcl.iam.add-policy").
- [Step 2: Add an access policy
  to AWSRDSCustomInstanceRoleForRdsCustomInstance](#custom-setup-orcl.iam.create-profile "#custom-setup-orcl.iam.create-profile").
- [Step 4: Add
  AWSRDSCustomInstanceRoleForRdsCustomInstance to
  AWSRDSCustomInstanceProfile](#custom-setup-orcl.iam.add-profile "#custom-setup-orcl.iam.add-profile").

#### Step 1: Create the IAM

role AWSRDSCustomInstanceRoleForRdsCustomInstance

In this step, you create the role using the naming format
`AWSRDSCustomInstanceRole-`region``.
 Using the trust policy, Amazon EC2 can assume the role. The following example assumes
 that you have set the environment variable `$REGION` to the
AWS Region in which you want to create your DB instance.

```
aws iam create-role \
  --role-name AWSRDSCustomInstanceRole-$REGION \
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

#### Step 2: Add an access policy

to AWSRDSCustomInstanceRoleForRdsCustomInstance

When you embed an inline policy in an IAM role, the inline policy is used as
part of the role's access (permissions) policy. You create the
`AWSRDSCustomIamRolePolicy` policy that permits Amazon EC2 to send and
receive messages and perform various actions.

The following example creates the access policy named
`AWSRDSCustomIamRolePolicy`, and adds it to the IAM role
`AWSRDSCustomInstanceRole-`region``.
This example assumes that you have set the following environment
variables:

`$REGION`

Set this variable to the AWS Region in which you plan to create
your DB instance.

`$ACCOUNT_ID`

Set this variable to your AWS account number.

`$KMS_KEY`

Set this variable to the Amazon Resource Name (ARN) of the
AWS KMS key that you want to use for your RDS Custom DB instances. To
specify more than one KMS key, add it to the
`Resources` section of statement ID (Sid) 11.

```
aws iam put-role-policy \
  --role-name AWSRDSCustomInstanceRole-$REGION \
  --policy-name AWSRDSCustomIamRolePolicy \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "1",
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeAssociation",
                "ssm:GetDeployablePatchSnapshotForInstance",
                "ssm:GetDocument",
                "ssm:DescribeDocument",
                "ssm:GetManifest",
                "ssm:GetParameter",
                "ssm:GetParameters",
                "ssm:ListAssociations",
                "ssm:ListInstanceAssociations",
                "ssm:PutInventory",
                "ssm:PutComplianceItems",
                "ssm:PutConfigurePackageResult",
                "ssm:UpdateAssociationStatus",
                "ssm:UpdateInstanceAssociationStatus",
                "ssm:UpdateInstanceInformation",
                "ssm:GetConnectionStatus",
                "ssm:DescribeInstanceInformation",
                "ssmmessages:CreateControlChannel",
                "ssmmessages:CreateDataChannel",
                "ssmmessages:OpenControlChannel",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "2",
            "Effect": "Allow",
            "Action": [
                "ec2messages:AcknowledgeMessage",
                "ec2messages:DeleteMessage",
                "ec2messages:FailMessage",
                "ec2messages:GetEndpoint",
                "ec2messages:GetMessages",
                "ec2messages:SendReply"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "3",
            "Effect": "Allow",
            "Action": [
                "logs:PutRetentionPolicy",
                "logs:PutLogEvents",
                "logs:DescribeLogStreams",
                "logs:DescribeLogGroups",
                "logs:CreateLogStream",
                "logs:CreateLogGroup"
            ],
            "Resource": [
                "arn:aws:logs:'$REGION':'$ACCOUNT_ID':log-group:rds-custom-instance*"
            ]
        },
        {
            "Sid": "4",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::do-not-delete-rds-custom-*/*"
            ]
        },
        {
            "Sid": "5",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": [
                        "RDSCustomForOracle/Agent"
                    ]
                }
            }
        },
        {
            "Sid": "6",
            "Effect": "Allow",
            "Action": [
                "events:PutEvents"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "7",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret"
            ],
            "Resource": [
                "arn:aws:secretsmanager:'$REGION':'$ACCOUNT_ID':secret:do-not-delete-rds-custom-*",
                "arn:aws:secretsmanager:'$REGION':'$ACCOUNT_ID':secret:rds-custom!oracle-do-not-delete-*"
            ]
        },
        {
           "Sid": "8",
           "Effect": "Allow",
           "Action": [
             "s3:ListBucketVersions"
           ],
           "Resource": [
             "arn:aws:s3:::do-not-delete-rds-custom-*"
           ]
         },
         {
            "Sid": "9",
            "Effect": "Allow",
            "Action": "ec2:CreateSnapshots",
            "Resource": [
                "arn:aws:ec2:*:*:instance/*",
                "arn:aws:ec2:*:*:volume/*"
            ],
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/AWSRDSCustom": "custom-oracle"
                }
            }
          },
          {
            "Sid": "10",
            "Effect": "Allow",
            "Action": "ec2:CreateSnapshots",
            "Resource": [
                "arn:aws:ec2:*::snapshot/*"
            ]
          },
          {
            "Sid": "11",
            "Effect": "Allow",
            "Action": [
              "kms:Decrypt",
              "kms:GenerateDataKey"
            ],
            "Resource": [
              "arn:aws:kms:'$REGION':'$ACCOUNT_ID':key/'$KMS_KEY'"
            ]
          },
          {
            "Sid": "12",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "ec2:CreateAction": [
                        "CreateSnapshots"
                    ]
                }
            }
        },
        {
            "Sid": "13",
            "Effect": "Allow",
            "Action": [
                "sqs:SendMessage",
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl"
            ],
            "Resource": "arn:aws:sqs:'$REGION':'$ACCOUNT_Id':do-not-delete-rds-custom-*",
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSRDSCustom": "custom-oracle"
                }
            }
        }
    ]
}'
```

#### Step 3: Create the RDS Custom

instance profile AWSRDSCustomInstanceProfile

An instance profile is a container that includes a single IAM role. RDS Custom
uses the instance profile to pass the role to the instance.

If you use the CLI to create a role, you create the role and instance profile
as separate actions, with potentially different names. Create your IAM
instance profile as follows, naming it using the format
`AWSRDSCustomInstanceProfile-`region``.
 The following example assumes that you have set the environment variable
 `$REGION` to the AWS Region in which you want to create your
DB instance.

```
aws iam create-instance-profile \
    --instance-profile-name AWSRDSCustomInstanceProfile-$REGION
```

#### Step 4: Add

AWSRDSCustomInstanceRoleForRdsCustomInstance to
AWSRDSCustomInstanceProfile

Add your IAM role to the instance profile that you previously created. The
following example assumes that you have set the environment variable
`$REGION` to the AWS Region in which you want to create your
DB instance.

```
aws iam add-role-to-instance-profile \
    --instance-profile-name AWSRDSCustomInstanceProfile-$REGION \
    --role-name AWSRDSCustomInstanceRole-$REGION
```

## Step 5: Grant required permissions to your

IAM user or role

Make sure that the IAM principal (user or role) that creates the CEV or RDS Custom DB instance
has either of the following policies:

- The `AdministratorAccess` policy
- The `AmazonRDSFullAccess` policy with required permissions for Amazon S3
  and AWS KMS, CEV creation, and DB instance creation

###### Topics

- [IAM permissions required for Amazon S3 and
  AWS KMS](#custom-setup-orcl.s3-kms "#custom-setup-orcl.s3-kms")
- [IAM permissions required for creating a
  CEV](#custom-setup-orcl.cev "#custom-setup-orcl.cev")
- [IAM permissions required for creating a DB instance
  from a CEV](#custom-setup-orcl.db "#custom-setup-orcl.db")

### IAM permissions required for Amazon S3 and

AWS KMS

To create CEVs or RDS Custom for Oracle DB instances, your IAM principal needs to access Amazon S3 and
AWS KMS. The following sample JSON policy grants the required permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
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
}`

```

For more information about the `kms:CreateGrant` permission, see [AWS KMS key management](Overview.Encryption.md "Overview.Encryption.md").

### IAM permissions required for creating a

CEV

To create a CEV, your IAM principal needs the following additional
permissions:

```
s3:GetObjectAcl
s3:GetObject
s3:GetObjectTagging
s3:ListBucket
mediaimport:CreateDatabaseBinarySnapshot
```

The following sample JSON policy grants the additional permissions necessary to
access bucket `my-custom-installation-files` and its
contents.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessToS3MediaBucket",
 "Effect": "Allow",
 "Action": [
 "s3:GetObjectAcl",
 "s3:GetObject",
 "s3:GetObjectTagging",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`my-custom-installation-files`",
 "arn:aws:s3:::`my-custom-installation-files`/*"
 ]
 },
 {
 "Sid": "PermissionForByom",
 "Effect": "Allow",
 "Action": [
 "mediaimport:CreateDatabaseBinarySnapshot"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can grant similar permissions for Amazon S3 to caller accounts using an S3 bucket
policy.

### IAM permissions required for creating a DB instance

from a CEV

To create an RDS Custom for Oracle DB instance from an existing CEV, the IAM principal needs the
following additional permissions.

```
iam:SimulatePrincipalPolicy
cloudtrail:CreateTrail
cloudtrail:StartLogging
```

The following sample JSON policy grants the permissions necessary to validate an
IAM role and log information to an AWS CloudTrail.

JSON

```
`{
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
 }
 ]
}`

```

## Step 6: Configure your VPC for

RDS Custom for Oracle

Your RDS Custom DB instance is in a virtual private cloud (VPC) based on the Amazon VPC service, just
like an Amazon EC2 instance or Amazon RDS instance. You provide and configure your own VPC. Unlike
RDS Custom for SQL Server, RDS Custom for Oracle doesn't create an access control list or security groups. You must
attach you own security group, subnets, and route tables.

You can configure your virtual private cloud (VPC) using either CloudFormation or a manual
process.

###### Important

We strongly recommend that you configure your RDS Custom for Oracle environment using CloudFormation.
This technique is the easiest and least error-prone.

###### Topics

- [Configure your VPC using
  CloudFormation (recommended)](#custom-setup-orcl.cf.config-vpc "#custom-setup-orcl.cf.config-vpc")
- [Configure your VPC manually for
  RDS Custom for Oracle](#custom-setup-orcl.vpc "#custom-setup-orcl.vpc")

### Configure your VPC using

CloudFormation (recommended)

If you've already configured your VPC for a different RDS Custom engine, and want to
reuse the existing VPC, skip this step. This section assumes the following:

- You've already used CloudFormation to create your IAM instance profile and
  role.
- You know your route table ID.

For a DB instance to be private, it must be in a private subnet. For a subnet to be
private, it must not be associated with a route table that has a default internet
gateway. For more information, see [Configure route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md")
in the _Amazon VPC User Guide_.

When you use the CloudFormation template for your VPC, it creates the following
resources:

- A private VPC
- A subnet group named `rds-custom-private`
- The following VPC endpoints, which your DB instance uses to communicate with dependent
  AWS services:

      + `com.amazonaws.`region`.ec2messages`
      + `com.amazonaws.`region`.events`
      + `com.amazonaws.`region`.logs`
      + `com.amazonaws.`region`.monitoring`
      + `com.amazonaws.`region`.s3`
      + `com.amazonaws.`region`.secretsmanager`
      + `com.amazonaws.`region`.ssm`
      + `com.amazonaws.`region`.ssmmessages`

  If you're creating a Multi-AZ deployment:

      + `com.amazonaws.`region`.sqs`

###### Note

For a complex networking setup with existing accounts, we recommend that you
configure access to dependent services manually if access doesn't already exist.
For more information, see [Make sure your VPC can access
dependent AWS services](#custom-setup-orcl.vpc.endpoints "#custom-setup-orcl.vpc.endpoints").

###### To configure your VPC using CloudFormation

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. Start the Create Stack wizard, and choose **Create Stack** and
   then **With new resources (standard)**.
3. On the **Create stack** page, do the following:
   1. For **Prepare template**, choose **Template is
      ready**.
   2. For **Template source**, choose **Upload a
      template file**.
   3. For **Choose file**, navigate to, then choose
      `custom-vpc.json`.
   4. Choose **Next**.

4. On the **Specify stack details** page, do the
   following:
   1. For **Stack name**, enter `custom-vpc`.
   2. For **Parameters**, choose the private subnets to use for RDS Custom DB instances.
   3. Choose the private VPC ID to use for RDS Custom DB instances.
   4. Enter the route table associated with the private subnets.
   5. Choose **Next**.

5. On the **Configure stack options page**, choose **Next**.
6. On the **Review custom-vpc** page, choose
   **Submit**.

CloudFormation configures your private VPC. In the left panel, when
**custom-vpc** shows **CREATE_COMPLETE**,
proceed to the next step. 7. (Optional) Review the details of your VPC. In the **Stacks**
pane, choose **custom-vpc**. In the right pane, do the
following:

    1. Choose **Stack info**. Your stack has an ID in the format
     **arn:aws:cloudformation:`region`:`account-no`:stack/custom-vpc/`identifier`**.
    2. Choose **Resources**. You should see a subnet group named
     **rds-custom-private** and several VPC endpoints that
     use the naming format
     **vpce-`string`**. Each
     endpoint corresponds to an AWS service that RDS Custom needs to communicate
     with. For more information, see [Make sure your VPC can access
     dependent AWS services](#custom-setup-orcl.vpc.endpoints "#custom-setup-orcl.vpc.endpoints").
    3. Choose **Parameters**. You should see the private
     subnets, private VPC, and the route table that you specified when you
     created the stack. When you create a DB instance, you need to supply the VPC ID
     and subnet group.

### Configure your VPC manually for

RDS Custom for Oracle

As an alternative to automating VPC creation with CloudFormation, you can configure your
VPC manually. This option might be best when you have a complex networking setup
that uses existing resources.

###### Topics

- [Make sure your VPC can access
  dependent AWS services](#custom-setup-orcl.vpc.endpoints "#custom-setup-orcl.vpc.endpoints")
- [Configure the instance metadata
  service](#custom-setup-orcl.vpc.imds "#custom-setup-orcl.vpc.imds")

#### Make sure your VPC can access

dependent AWS services

RDS Custom sends communication from your DB instance to other AWS services. Make sure the
following services are accessible from the subnet in which you create your RDS Custom
DB instances:

- Amazon CloudWatch
  (`com.amazonaws.`region`.monitoring`)
- Amazon CloudWatch Logs
  (`com.amazonaws.`region`.logs`)
- Amazon CloudWatch Events
  (`com.amazonaws.`region`.events`)
- Amazon EC2 (`com.amazonaws.`region`.ec2` and
  `com.amazonaws.`region`.ec2messages`)
- Amazon S3 (`com.amazonaws.`region`.s3`)
- AWS Secrets Manager
  (`com.amazonaws.`region`.secretsmanager`)
- AWS Systems Manager (`com.amazonaws.`region`.ssm` and
  `com.amazonaws.`region`.ssmmessages`)

If creating Multi-AZ deployments

- Amazon Simple Queue Service (`com.amazonaws.`region`.sqs`)

If RDS Custom can't communicate with the necessary services, it publishes the following
events:

```
Database instance in incompatible-network. SSM Agent connection not available. Amazon RDS can't connect to the dependent AWS services.
```

```
Database instance in incompatible-network. Amazon RDS can't connect to dependent AWS services. Make sure port 443 (HTTPS) allows outbound connections, and try again. "Failed to connect to the following services: s3 events"
```

To avoid `incompatible-network` errors, make sure that VPC components involved
in communication between your RDS Custom DB instance and AWS services satisfy the following
requirements:

- The DB instance can make outbound connections on port 443 to other
  AWS services.
- The VPC allows incoming responses to requests originating from your RDS Custom
  DB instance.
- RDS Custom can correctly resolve the domain names of endpoints for each
  AWS service.

If you already configured a VPC for a different RDS Custom DB engine, you can reuse that VPC and
skip this process.

#### Configure the instance metadata

service

Make sure that your instance can do the following:

- Access the instance metadata service using Instance Metadata Service
  Version 2 (IMDSv2).
- Allow outbound communications through port 80 (HTTP) to the IMDS link IP address.
- Request instance metadata from `http://169.254.169.254`, the IMDSv2 link.

For more information, see [Use IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") in the _Amazon EC2 User Guide_.

RDS Custom for Oracle automation uses IMDSv2 by default, by setting
`HttpTokens=enabled` on the underlying Amazon EC2 instance. However,
you can use IMDSv1 if you want. For more information, see [Configure the instance metadata options](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md") in the
_Amazon EC2 User Guide_.
