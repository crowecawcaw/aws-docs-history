# AWS managed policies for AWS IoT Wireless

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AWSIoTWirelessDataAccess

You can attach the `AWSIoTWirelessDataAccess` policy to your IAM identities.

This policy grants the associated identity permissions that allow access to send data
to LoRaWAN and Sidewalk devices using the `SendDataToWirelessDevice` API. To view
this policy in the AWS Management Console, see [AWSIoTWirelessDataAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessDataAccess$jsonEditor?section=permissions "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessDataAccess$jsonEditor?section=permissions").

**Permissions details**

This policy includes the following permissions.

- `iotwireless` – Retrieve AWS IoT Wireless data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotwireless:SendDataToWirelessDevice"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSIoTWirelessFullAccess

You can attach the `AWSIoTWirelessFullAccess` policy to your IAM identities.

This policy grants the associated identity permissions that allow full access to all
AWS IoT Wireless operations. To view this policy in the AWS Management Console, see [AWSIoTWirelessFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessFullAccess?section=permissions "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessFullAccess?section=permissions").

**Permissions details**

This policy includes the following permissions.

- `iotwireless` – Retrieve AWS IoT Wireless data and perform
  all AWS IoT Wireless operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotwireless:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSIoTWirelessFullPublishAccess

You can attach the `AWSIoTWirelessFullPublishAccess` policy to your IAM identities.

This policy grants the associated identity permissions that allow limited access to
publish to AWS IoT rules on your behalf. To view this policy in the
AWS Management Console, see [`AWSIoTWirelessFullPublishAccess`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessFullPublishAccess?section=permissions "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessFullPublishAccess?section=permissions").

**Permissions details**

This policy includes the following permissions.

- `iot` – Perform operations that gets the endpoint URL
  and publishes to AWS IoT rules engine.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:DescribeEndpoint",
 "iot:Publish"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSIoTWirelessLogging

You can attach the `AWSIoTWirelessLogging` policy to your IAM identities.

This policy grants the associated identity permissions that allow creation of Amazon CloudWatch Logs
log groups and stream logs to the groups. This policy is attached to your CloudWatch logging role.
To view this policy in the AWS Management Console, see [`AWSIoTWirelessLogging`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessLogging?section=permissions "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessLogging?section=permissions").

**Permissions details**

This policy includes the following permissions.

- `logs` – Retrieve CloudWatch logs. Also allows creation of CloudWatch Logs
  groups and stream logs to the groups.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/iotwireless*"
 }
 ]
}`

```

## AWS managed policy: AWSIoTWirelessReadOnlyAccess

You can attach the `AWSIoTLogging` policy to your IAM identities.

This policy grants the associated identity permissions that allow read-onlyaccess to
AWS IoT Wireless operations. To view this policy in the AWS Management Console, see [`AWSIoTWirelessReadOnlyAccess`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessReadOnlyAccess?section=permissions "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessReadOnlyAccess?section=permissions").

**Permissions details**

This policy includes the following permissions.

- `logs` – Perform AWS IoT Wireless `List` and `Get`
  API operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotwireless:List*",
 "iotwireless:Get*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSIoTWirelessGatewayCertManager

You can attach the `AWSIoTWirelessGatewayCertManager` policy to your IAM identities.

This policy grants the associated identity permissions that allow access to create,
list, and describe AWS IoT certificates. To view
this policy in the AWS Management Console, see [`AWSIoTWirelessGatewayCertManager`.](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessGatewayCertManager?section=permissions "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessGatewayCertManager?section=permissions")

**Permissions details**

This policy includes the following permissions.

- `iot` – Perform actions that create, describe, and list
  certificates.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IoTWirelessGatewayCertManager",
 "Effect": "Allow",
 "Action": [
 "iot:CreateKeysAndCertificate",
 "iot:DescribeCertificate",
 "iot:ListCertificates"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS IoT Wireless; updates to AWS managed

policies

View details about updates to AWS managed policies for AWS IoT Wireless since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed.

| Change                                    | Description                                                             | Date         |
| ----------------------------------------- | ----------------------------------------------------------------------- | ------------ |
| AWS IoT Wireless started tracking changes | AWS IoT Wireless started tracking changes for its AWS managed policies. | May 18, 2022 |
