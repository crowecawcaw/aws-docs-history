# Getting started by using the AWS CLI and SDK for Java

With Amazon S3 on Outposts, you can create S3 buckets on your AWS Outposts and easily store and
retrieve objects on premises for applications that require local data access, local data
processing, and data residency. S3 on Outposts provides a new storage class, S3 Outposts
(`OUTPOSTS`), which uses the Amazon S3 APIs, and is designed to store
data durably and redundantly across multiple devices and servers on your AWS Outposts. You communicate with your Outpost bucket
by using an access point
and endpoint connection over a virtual private cloud (VPC). You can use the same APIs and
features on Outpost buckets as you do on Amazon S3 buckets, including access policies, encryption, and tagging.
You can use S3 on Outposts through the AWS Management Console, AWS Command Line Interface (AWS CLI), AWS SDKs, or REST API. For more information, see [What is Amazon S3 on Outposts?](S3onOutposts.md "S3onOutposts.md")

To get started with S3 on Outposts, you must create a bucket, an access point, and an endpoint. Then,
you can upload objects to your bucket. The following examples show you how to get started
with S3 on Outposts by using the AWS CLI and SDK for Java. To get started by using the console, see
[Getting started by using the AWS Management Console](S3OutpostsGSConsole.md "S3OutpostsGSConsole.md").

###### Topics

- [Step 1: Create a bucket](#S3OutpostsGSCreateBucket "#S3OutpostsGSCreateBucket")
- [Step 2: Create an access point](#S3OutpostsGSCreateAccessPoint "#S3OutpostsGSCreateAccessPoint")
- [Step 3: Create an endpoint](#S3OutpostsGSCreateEndpoint "#S3OutpostsGSCreateEndpoint")
- [Step 4: Upload an object to an S3 on Outposts
  bucket](#S3OutpostsGSUploadObject "#S3OutpostsGSUploadObject")

## Step 1: Create a bucket

The following AWS CLI and SDK for Java examples show you how to create an S3 on Outposts
bucket.

AWS CLI
The following example creates an S3 on Outposts bucket (`s3-outposts:CreateBucket`)
by using the AWS CLI. To run this command, replace the `user input
 placeholders` with your own information.

```
aws s3control create-bucket --bucket `example-outposts-bucket` --outpost-id `op-01ac5d28a6a232904`
```

SDK for Java
For examples of how to create an S3 Outposts bucket with the AWS SDK for Java, see [CreateOutpostsBucket.java](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/CreateOutpostsBucket.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/CreateOutpostsBucket.java") in the _AWS SDK for Java 2.x Code Examples_.

## Step 2: Create an access point

To access your Amazon S3 on Outposts bucket, you must create and configure an access point. These
examples how you how to create an access point by using the AWS CLI and the SDK for Java.

Access points simplify managing data access at
scale for shared datasets in Amazon S3. Access points are named network endpoints that are
attached to buckets that you can use to perform Amazon S3 object operations, such as
`GetObject` and `PutObject`. With S3 on Outposts, you must use access points to access any object in an Outposts bucket. Access
points support only virtual-host-style addressing.

AWS CLI
The following AWS CLI example creates an access point for an Outposts bucket. To run this command,
replace the `user input placeholders` with your own
information.

```
aws s3control create-access-point --account-id `123456789012` --name `example-outposts-access-point` --bucket "arn:aws:s3-outposts:``region``:`123456789012`:outpost/`op-01ac5d28a6a232904`/bucket/`example-outposts-bucket`" --vpc-configuration VpcId=`example-vpc-12345`
```

SDK for Java
For examples of how to create an access point for an S3 Outposts bucket with the AWS SDK for Java, see [CreateOutpostsAccessPoint.java](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/CreateOutpostsAccessPoint.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/CreateOutpostsAccessPoint.java") in the _AWS SDK for Java 2.x Code Examples_.

## Step 3: Create an endpoint

To route requests to an Amazon S3 on Outposts access point, you must create and configure an
S3 on Outposts endpoint. In order to create an endpoint, you will need an active connection with your service link to your Outposts home region. Each virtual private cloud (VPC) on your Outpost can have one associated endpoint. For more information about endpoint quotas, see [S3 on Outposts network
requirements](S3OnOutpostsRestrictionsLimitations.md#S3OnOutpostsConnectivityRestrictions "S3OnOutpostsRestrictionsLimitations.md#S3OnOutpostsConnectivityRestrictions"). You must create an endpoint to be able to
access your Outposts buckets and perform object operations. For more information, see [Endpoints](S3OutpostsWorkingBuckets.md#S3OutpostsEP "S3OutpostsWorkingBuckets.md#S3OutpostsEP").

These examples show you how to create an endpoint by using the AWS CLI and the SDK for Java.
For more information about the permissions required to create and manage endpoints, see
[Permissions for S3 on Outposts
endpoints](S3OutpostsIAM.md#S3OutpostsEndpointPermissions "S3OutpostsIAM.md#S3OutpostsEndpointPermissions").

AWS CLI
The following AWS CLI example creates an endpoint for an Outpost by using the VPC resource
access type. The VPC is derived from the subnet. To run this command, replace the
`user input placeholders` with your own
information.

```
aws s3outposts create-endpoint --outpost-id `op-01ac5d28a6a232904` --subnet-id subnet-`8c7a57c5` --security-group-id `sg-ab19e0d1`
```

The following AWS CLI example creates an endpoint for an Outpost by using the customer-owned IP
address pool (CoIP pool) access type. To run this command, replace the
`user input placeholders` with your own
information.

```
aws s3outposts create-endpoint --outpost-id `op-01ac5d28a6a232904` --subnet-id subnet-`8c7a57c5` --security-group-id `sg-ab19e0d1` --access-type CustomerOwnedIp --customer-owned-ipv4-pool `ipv4pool-coip-12345678901234567`
```

SDK for Java
For examples of how to create an endpoint for an S3 Outpost with the AWS SDK for Java, see [CreateOutpostsEndPoint.java](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/CreateOutpostsEndPoint.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/CreateOutpostsEndPoint.java") in the _AWS SDK for Java 2.x Code Examples_.

## Step 4: Upload an object to an S3 on Outposts

bucket

To upload an object, see [Upload an object to an S3 on Outposts
bucket](S3OutpostsUploadObjects.md "S3OutpostsUploadObjects.md").
