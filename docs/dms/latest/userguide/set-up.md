# Complete prerequisites for working with DMS Schema Conversion

To set up DMS Schema Conversion, complete the following tasks. Then you can set up an instance
profile, add data providers, and create a migration project.

###### Topics

- [Create a VPC based on Amazon VPC](#set-up-vpc "#set-up-vpc")
- [Create an Amazon S3 bucket](#set-up-s3-bucket "#set-up-s3-bucket")
- [Store database credentials in AWS Secrets Manager](#set-up-secrets "#set-up-secrets")
- [Create IAM policies](#set-up-iam-policies "#set-up-iam-policies")
- [Create IAM roles](#set-up-iam-roles "#set-up-iam-roles")

## Create a VPC based on Amazon VPC

In this step, you create a virtual private cloud (VPC) in your AWS account. This
VPC is based on the Amazon Virtual Private Cloud (Amazon VPC) service and contains your AWS
resources.

###### To create a VPC for DMS Schema Conversion

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Choose **Create VPC**.
3. On the **Create VPC** page, enter the following
   settings:
   - **Resources to create** – **VPC
     and more**
   - **Name tag auto-generation** – Choose
     **Auto-generate** and enter a globally unique
     name. For example, enter `sc-vpc`.
   - **IPv4 CIDR block** –
     `10.0.1.0/24`
   - **NAT gateways** – **In 1
     AZ**
   - **VPC endpoints** –
     **None**

4. Keep the rest of the settings as they are, and then choose
   **Create VPC**.
5. Choose **Subnets**, and take a note of your public and
   private subnet IDs.

To connect to your Amazon RDS databases, create a subnet group that includes
public subnets.

To connect to your on-premises databases, create a subnet group that
includes private subnets. For more information, see [Create an instance profile for
DMS Schema Conversion](getting-started-instance.md "getting-started-instance.md"). 6. Choose **NAT gateways**. Choose your **NAT
gateway** and take a note of your **Elastic IP
address**.

Configure your network to make sure that AWS DMS can access your source
on-premises database from this NAT gateway's public IP address. For more
information, see [Using an internet connection to a VPC](instance-profiles-network.md#instance-profiles-network-internet "instance-profiles-network.md#instance-profiles-network-internet").

Use this VPC when you create your instance profile and target databases on
Amazon RDS.

## Create an Amazon S3 bucket

To store information from your migration project, create an Amazon S3 bucket. DMS Schema Conversion
uses this Amazon S3 bucket to save items such as assessment reports, converted SQL code,
information about database schema objects, and so on.

###### To create an Amazon S3 bucket for DMS Schema Conversion

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. On the **Create bucket** page, select a globally unique
   name for your S3 bucket. For example, enter
   `sc-s3-bucket`.
4. For **AWS Region**, choose your Region.
5. For **Bucket Versioning**, choose
   **Enable**.
6. Keep the rest of the settings as they are, and then choose
   **Create bucket**.

###### Note

DMS Schema Conversion (SC) works only with S3 buckets that use Server-Side
Encryption with Amazon S3-Managed Keys (SSE-S3). Other encryption
configurations, including Server-Side Encryption with AWS KMS (SSE-KMS),
Customer-Provided Keys (SSE-C), or Client-Side Encryption, are not currently
supported by SC and prevents it from accessing the S3 bucket. If using a
different encryption method, you must create a separate S3 bucket with SSE-S3
for use with DMS Schema Conversion.

## Store database credentials in AWS Secrets Manager

Store your source and target database credentials in AWS Secrets Manager. Make sure that you
replicate these secrets to your AWS Region. DMS Schema Conversion uses these secrets to connect
to your databases in the migration project.

###### To store your database credentials in AWS Secrets Manager

1. Sign in to the AWS Management Console and open the AWS Secrets Manager console at
   [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. The **Choose secret type** page opens. For
   **Secret type**, choose the type of database
   credentials to store:
   - **Credentials for Amazon RDS database** – Choose this
     option to store credentials for your Amazon RDS database. For
     **Credentials**, enter the credentials for your
     database. For **Database**, choose your
     database.
   - **Credentials for other database** – Choose this
     option to store credentials for your source Oracle or SQL Server
     databases. For **Credentials**, enter the
     credentials for your database.
   - **Other type of secret** – Choose this option to
     store only the user name and password to connect to your database.
     Choose **Add row** to add two key-value pairs. Make
     sure that you use `username` and
     `password` for key names. For values
     related to these keys, enter the credentials for your
     database.

4. For **Encryption key**, choose the AWS KMS key that Secrets Manager
   uses to encrypt the secret value. Choose **Next**.
5. On the **Configure secret** page, enter a descriptive
   **Secret name**. For example, enter
   `sc-source-secret` or
   `sc-target-secret`.
6. Choose **Replicate secret** and then for
   **AWS Region** choose your Region. Choose
   **Next**.
7. On the **Configure rotation** page, choose
   **Next**.
8. On the **Review** page, review your secret details, and
   then choose **Store**.

To store credentials for your source and target databases, repeat these
steps.

## Create IAM policies

###### To create an IAM policy for DMS Schema Conversion to access Amazon S3

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. On the **Select service** page, choose
   **Amazon S3** from the list.
5. In the **Actions allowed**, choose
   `PutObject`, `GetObject`,
   `GetObjectVersion`, `GetBucketVersioning`,
   `GetBucketLocation`, `ListBucket`.
6. In the **Resources** specify the ARN of the bucket that
   you created in the previous section. Choose
   **Next**.
7. On the **Review and create** page, enter a descriptive
   name. For example: `sc-s3-policy`. Then, choose **Create
   policy**.

###### To create an IAM policy for DMS Schema Conversionto access AWS Secrets Manager

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. On the **Select service** page, choose
   **Secrets Manager** from the list.
5. Choose **Next**. The **Add permissions**
   page opens.
6. In the **Actions allowed**, choose:
   `GetSecretValue` and `DescribeSecret`.
7. On the **Review and create** page, enter a descriptive
   name. For example: `sc-secrets-manager-policy`. Then, choose
   **Create policy**.

## Create IAM roles

Create AWS Identity and Access Management (IAM) roles to use in your migration project. DMS Schema Conversion uses
these IAM roles to access your Amazon S3 bucket and database credentials stored in
AWS Secrets Manager.

###### To create an IAM role that provides access to your Amazon S3 bucket

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. On the **Select trusted entity** page, choose
   **AWS service**. Choose
   **DMS**.
5. Choose **Next**. The **Add permissions**
   page opens.
6. For **Filter policies**, enter `S3`.
   Choose the **sc-s3-policy** policy that you created in the
   previous section.
7. Choose **Next**. The **Name, review, and
   create** page opens.
8. For **Role name**, enter a descriptive name. For example,
   enter `sc-s3-role`. Choose **Create
   role**.
9. On the **Roles** page, enter
   `sc-s3-role` for **Role name**.
   Choose **sc-s3-role**.
10. On the **sc-s3-role page**, choose the **Trust
    relationships** tab. Choose **Edit trust
    policy**.
11. Thes AWS DMS regional service principal has the following format:

```
dms.region-name.amazonaws.com
```

Replace `region-name` with the name of your Region, such as
`us-east-1`: The following code example shows the principal
for the `us-east-1` Region:

```
dms.us-east-1.amazonaws.com
```

The following code example shows a trust policy for accessing AWS DMS schema
conversion:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.us-east-1.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

###### To create an IAM role that provides access to AWS Secrets Manager

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. On the **Select trusted entity** page, choose
   **AWS service**. Choose
   **DMS**.
5. Choose **Next**. The **Add permissions**
   page opens.
6. For **Filter policies**, enter `s3`. Choose
   the **sc-secrets-manager-policy** that you created in the
   previous section.
7. Choose **Next**. The **Name, review, and
   create** page opens.
8. For **Role name**, enter a descriptive name. For example,
   enter `sc-secrets-manager-role`. Choose
   **Create role**.
9. On the **Roles** page, enter
   `sc-secrets-manager-role` for **Role
   name**. Choose
   **sc-secrets-manager-role**.
10. On the **sc-secrets-manager-role** page, choose the
    **Trust relationships tab**. Choose **Edit
    trust policy**.
11. On the **Edit trust policy** page, edit the trust
    relationships for the role to use
    `schema-conversion.dms.amazonaws.com` and your AWS DMS regional
    service principal as the trusted entities. This AWS DMS regional service
    principal has the following format:

```
dms.region-name.amazonaws.com
```

Replace `region-name` with the name of your Region, such as
`us-east-1`: The following code example shows the principal
for the `us-east-1` Region:

```
dms.us-east-1.amazonaws.com
```

The following code example shows a trust policy for accessing AWS DMS schema
conversion:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.us-east-1.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

###### To create the `dms-vpc-role` IAM role for use with the AWS CLI

or AWS DMS API

1. Create a JSON file with the following IAM policy. Name the JSON file
   `dmsAssumeRolePolicyDocument.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Then, create the role using the AWS CLI using the following
command:

```
aws iam create-role --role-name dms-vpc-role --assume-role-policy-document file://dmsAssumeRolePolicyDocument.json

```

2. Attach the `AmazonDMSVPCManagementRole` policy to
   `dms-vpc-role` using the following command:

```
aws iam attach-role-policy --role-name dms-vpc-role --policy-arn arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole
```

###### To create the `dms-cloudwatch-logs-role` IAM role for use with the AWS CLI

or AWS DMS API

1. Create a JSON file with the following IAM policy. Name the JSON file
   `dmsAssumeRolePolicyDocument2.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Then, create the role using the AWS CLI using the following
command:

```
aws iam create-role --role-name dms-cloudwatch-logs-role --assume-role-policy-document file://dmsAssumeRolePolicyDocument2.json
```

2. Attach the `AmazonDMSCloudWatchLogsRole` policy to
   `dms-cloudwatch-logs-role` using the following command:

```
aws iam attach-role-policy --role-name dms-cloudwatch-logs-role --policy-arn arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole
```
