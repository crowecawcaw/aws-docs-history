# Controlling access with AWS IoT FleetWise

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

The following sections cover how to control access to and from your AWS IoT FleetWise resources.
The information they cover includes how to grant your application access so AWS IoT FleetWise can
transfer vehicle data during campaigns. They also describe how you can grant AWS IoT FleetWise access
to your Amazon S3 (S3) bucket or Amazon Timestream database and table to store data, or to MQTT messages
used to send data from vehicles.

The technology for managing all these forms of access is AWS Identity and Access Management (IAM). For more
information about IAM, see [What is
IAM?](../../../IAM/latest/UserGuide/IAM_Introduction.md "../../../IAM/latest/UserGuide/IAM_Introduction.md").

###### Contents

- [Grant AWS IoT FleetWise permission to send and receive data on
  an MQTT topic](#using-iam-mqtt "#using-iam-mqtt")
- [Grant AWS IoT FleetWise access to an Amazon S3 destination](#using-iam-s3 "#using-iam-s3")
- [Grant AWS IoT FleetWise access to an Amazon Timestream
  destination](#using-timestream "#using-timestream")
- [Grant AWS IoT Device Management permission to generate the
  payload for commands with AWS IoT FleetWise](#generate-command-payload "#generate-command-payload")

## Grant AWS IoT FleetWise permission to send and receive data on

an MQTT topic

When you use an [MQTT topic](../../../iot/latest/developerguide/topics.md "../../../iot/latest/developerguide/topics.md"), your vehicles send data using the AWS IoT
MQTT message broker. You must grant AWS IoT FleetWise permission to subscribe to the MQTT topic
you specify. If you also use AWS IoT Rules to take action, or route data to other
destinations, you must attach policies to an IAM role to allow AWS IoT FleetWise to forward
data to IoT Rules.

In addition, your other apps or devices can subscribe to the topic you specify to
receive vehicle data in near real-time, and these apps or devices must be granted
permissions and access as needed.

For more information about using MQTT and the roles and permissions required,
see:

- [Device communication protocols](../../../iot/latest/developerguide/protocols.md "../../../iot/latest/developerguide/protocols.md")
- [Rules for AWS IoT](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md")
- [Granting an AWS IoT rule
  the access it requires](../../../iot/latest/developerguide/iot-create-role.md "../../../iot/latest/developerguide/iot-create-role.md")
- [Pass role permissions](../../../iot/latest/developerguide/pass-role.md "../../../iot/latest/developerguide/pass-role.md")

Before you start, check the following:

###### Important

- You must use the same AWS Region when you create vehicle campaign
  resources for AWS IoT FleetWise. If you switch AWS Regions, you might have issues
  accessing the resources.
- AWS IoT FleetWise is available in US East (N. Virginia) and
  Europe (Frankfurt).

You can use the AWS CLI to create an IAM role with a trust policy for MQTT messaging.
To create an IAM role, run the following command.

###### To create an IAM role with a trust policy

- Replace `IotTopicExecutionRole` with the name of the
  role you're creating.
- Replace `trust-policy` with the JSON file that
  contains the trust policy.

```
aws iam create-role --role-name `IotTopicExecutionRole` --assume-role-policy-document file://`trust-policy`.json
```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "mqttTopicTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotfleetwise.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": [
 "arn:aws:iotfleetwise:`region:account-id`:campaign/`campaign-name`"
 ],
 "aws:SourceAccount": [
 "`account-id`"
 ]
 }
 }
 }
 ]
}`

```

Create a permissions policy to give AWS IoT FleetWise permissions to publish messages to the MQTT
topic you specified. To create a permissions policy, run the following command.

###### To create a permissions policy

- Replace
  `AWSIoTFleetwiseAccessIotTopicPermissionsPolicy`
  with the name of the policy you're creating.
- Replace `permissions-policy` with the name of the
  JSON file that contains the permissions policy.

```
aws iam create-policy --policy-name `AWSIoTFleetwiseAccessIotTopicPermissionsPolicy` --policy-document file://`permissions-policy`.json
```

###### To attach the permissions policy to your IAM role

1. From the output, copy the Amazon Resource Name (ARN) of the permissions
   policy.
2. To attach the IAM permissions policy to your IAM role, run the following
   command.
   - Replace `permissions-policy-arn` with the ARN
     that you copied in the previous step.
   - Replace `IotTopicExecutionRole` with the name
     of the IAM role that you created.

```
aws iam attach-role-policy --policy-arn `permissions-policy-arn` --role-name `IotTopicExecutionRole`
```

For more information, see [Access management for
AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the _IAM User Guide_.

## Grant AWS IoT FleetWise access to an Amazon S3 destination

When you use an Amazon S3 destination, AWS IoT FleetWise delivers vehicle data to your S3 bucket and
can optionally use an AWS KMS key that you own for data encryption. If error logging is
enabled, AWS IoT FleetWise also sends data delivery errors to your CloudWatch log group and streams.
You're required to have an IAM role when creating a delivery stream.

AWS IoT FleetWise uses a bucket policy with the service principal for the S3 destination. For
more information about adding bucket policies, see [Adding a bucket policy by
using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon Simple Storage Service User
Guide_.

Use the following access policy to enable AWS IoT FleetWise to access your S3 bucket. If you
don't own the S3 bucket, add `s3:PutObjectAcl` to the list of Amazon S3 actions.
This grants the bucket owner full access to the objects delivered by AWS IoT FleetWise. For more
information about how you can secure access to objects in your buckets, see [Bucket policy examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md") in the _Amazon Simple Storage Service User
Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "iotfleetwise.amazonaws.com"
 ]
 },
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::`bucket-name`"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "iotfleetwise.amazonaws.com"
 ]
 },
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`bucket-name`/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "`campaign-arn`",
 "aws:SourceAccount": "`account-id`"
 }
 }
 }
 ]
}`

```

The following bucket policy is for all campaigns in an account in an AWS
Region.

If you have a KMS key attached to your S3 bucket, the key will need the following
policy. For information about key management, see [Protecting data using
server-side encryption with AWS Key Management Service keys (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") in the
_Amazon Simple Storage Service User Guide_.

```
{
  "Version": "2012-10-17",
  "Effect": "Allow",
  "Principal": {
    "Service": "iotfleetwise.amazonaws.com"
  },
  "Action": [
    "kms:GenerateDataKey",
    "kms:Decrypt"
   ],
  "Resource": "`key-arn`"
}
```

###### Important

When you create a bucket, S3 creates a default access control lists (ACL) that
grants the resource owner full control over the resource. If AWS IoT FleetWise can't deliver
data to S3, make sure you disable the ACL on the S3 bucket. For more information,
see [Disabling ACLs for
all new buckets and enforcing Object Ownership](../../../AmazonS3/latest/userguide/ensure-object-ownership.md "../../../AmazonS3/latest/userguide/ensure-object-ownership.md") in the _Amazon Simple Storage Service
User Guide_.

## Grant AWS IoT FleetWise access to an Amazon Timestream

destination

When you use a Timestream destination, AWS IoT FleetWise delivers vehicle data to a Timestream table.
You must attach the policies to the IAM role to allow AWS IoT FleetWise to send data to
Timestream.

If you use the console to [create a
campaign](create-campaign.md#create-campaign-console "create-campaign.md#create-campaign-console"), AWS IoT FleetWise automatically attaches the required policy to the
role.

###### Note

Amazon Timestream is not available in the Asia Pacific (Mumbai) Region.

Before you start, check the following:

###### Important

- You must use the same AWS Region when you create Timestream resources for
  AWS IoT FleetWise. If you switch AWS Regions, you might have issues accessing the
  Timestream resources.
- AWS IoT FleetWise is available in US East (N. Virginia), Europe (Frankfurt), and
  Asia Pacific (Mumbai).
- For the list of supported Regions, see [Timestream endpoints and
  quotas](../../../general/latest/gr/timestream.md "../../../general/latest/gr/timestream.md") in the _AWS General Reference_.

- You must have a Timestream database. For a tutorial, see [Create a database](../../../timestream/latest/developerguide/console_timestream.md#console_timestream.db.using-console "../../../timestream/latest/developerguide/console_timestream.md#console_timestream.db.using-console") in the _Amazon Timestream Developer
  Guide_.
- You must have a table created in the specified Timestream database. For a
  tutorial, see [Create a table](../../../timestream/latest/developerguide/console_timestream.md#console_timestream.table.using-console "../../../timestream/latest/developerguide/console_timestream.md#console_timestream.table.using-console") in the _Amazon Timestream Developer
  Guide_.

You can use the AWS CLI to create an IAM role with a trust policy for Timestream. To
create an IAM role, run the following command.

###### To create an IAM role with a trust policy

- Replace `TimestreamExecutionRole` with the name of
  the role you're creating.
- Replace `trust-policy` with the .json file that contains
  the trust policy.

```
aws iam create-role --role-name `TimestreamExecutionRole` --assume-role-policy-document file://`trust-policy`.json
```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "timestreamTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotfleetwise.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": [
 "arn:aws:iotfleetwise:`region`:`account-id`:campaign/`campaign-name`"
 ],
 "aws:SourceAccount": [
 "`account-id`"
 ]
 }
 }
 }
 ]
}`

```

Create a permissions policy to give AWS IoT FleetWise permissions to write data into Timestream. To
create a permissions policy, run the following command.

###### To create a permissions policy

- Replace
  `AWSIoTFleetwiseAccessTimestreamPermissionsPolicy`
  with the name of the policy you're creating.
- Replace `permissions-policy` with the name of the
  JSON file that contains the permissions policy.

```
aws iam create-policy --policy-name `AWSIoTFleetwiseAccessTimestreamPermissionsPolicy` --policy-document file://`permissions-policy`.json
```

###### To attach the permissions policy to your IAM role

1. From the output, copy the Amazon Resource Name (ARN) of the permissions
   policy.
2. To attach the IAM permissions policy to your IAM role, run the following
   command.
   - Replace `permissions-policy-arn` with the ARN
     that you copied in the previous step.
   - Replace `TimestreamExecutionRole` with the
     name of the IAM role that you created.

```
aws iam attach-role-policy --policy-arn `permissions-policy-arn` --role-name `TimestreamExecutionRole`
```

For more information, see [Access management for
AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the _IAM User Guide_.

## Grant AWS IoT Device Management permission to generate the

payload for commands with AWS IoT FleetWise

When you use the commands feature to start a command execution, AWS IoT Device Management will
fetch the command and command parameters from the incoming request. It then requires
permissions to access AWS IoT FleetWise resources to validate the request and generate the payload.
The payload is then sent to the vehicle by AWS IoT Device Management over MQTT to the command request topic
that your vehicle has subscribed to.

You must first create an IAM role that grants AWS IoT Device Management the required permissions for
generating the payload. Then, provide the ARN of this role to the [`CreateCommand`](../../../iot/latest/apireference/API_CreateCommand.md "../../../iot/latest/apireference/API_CreateCommand.md") API
using the `roleArn` field. The following shows some policy examples.

###### Important

For the IAM role, you must use the same AWS Region as the one where
you created the vehicle and command resources. If you switch AWS Region,
you might have issues accessing the resources.

The IAM role need to have the following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RemoteCommandsTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "iot.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The following example shows how to grant permissions to generate the payload
for all vehicles registered as AWS IoT things.

###### Note

- This policy can be overly permissive. Use the principle of least
  privilege to make sure that you grant only the necessary
  permissions.
- To deny permissions instead, change `"Effect": "Allow"`
  to `"Effect": "Deny"` in the IAM policy.
  In this example, replace:

- `region` with your AWS Region
  where you are using the AWS IoT FleetWise resources.
- `111122223333` with your AWS account
  number.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iotfleetwise:GenerateCommandPayload",
 "Resource": "*"
 }
 ]
}`

```

The following example shows how to grant permissions to generate the payload
for a specific vehicle registered as an AWS IoT thing.

In this example, replace:

- `region` with your AWS Region
  where you are using the AWS IoT FleetWise resources.
- `111122223333` with your AWS account
  number.
- `<VEHICLE_NAME>` with the IoT thing
  name for your vehicle .
  The following example shows how to grant permissions to generate the payload
  for the actuator for a specific vehicle.

In this example, replace:

- `region` with your AWS Region
  where you are using the AWS IoT FleetWise resources.
- `111122223333` with your AWS account
  number.
- `<VEHICLE_NAME>` with the IoT thing
  name for your vehicle.
- `<SIGNAL_FQN>` with the name of
  the signal, such as `<Vehicle.actuator2>`.
  The following example shows how to grant permissions to generate the payload
  for a specific vehicle and state template.

In this example, replace:

- `region` is your AWS Region
  where you are using the AWS IoT FleetWise resources.
- `111122223333` is your AWS account
  number.
- `<VEHICLE_NAME>` is the IoT thing
  name for your vehicle.
- `<STATE_TEMPLATE_ID>` with the identifier of
  your state template.
  If you've enabled customer managed KMS keys for AWS IoT FleetWise, then
  the following example shows how to grant permissions to generate the payload.

In this example, replace:

- `region` with your AWS Region
  where you are using the AWS IoT FleetWise resources.
- `111122223333` with your AWS account
  number.
- `<KMS_KEY_ID>` with the ID of your
  KMS key.
