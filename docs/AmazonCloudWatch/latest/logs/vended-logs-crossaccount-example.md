# Cross-account delivery

example

In this example, two accounts are involved. The account with the log-generating
resource is Account A, ID: `123456789012`, and the
account with the log-consuming resource is Account B, ID:
`111122223333`.

Account A wants to deliver logs from the Amazon Bedrock knowledge base in
their account with the ARN
arn:aws:bedrock:`us-east-1`:`123456789012`:knowledge-base/`kb-12345678`.

For this example, account A needs the following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowVendedLogDeliveryForKnowledgeBase",
 "Effect": "Allow",
 "Action": [
 "bedrock:AllowVendedLogDeliveryForResource"
 ],
 "Resource": "arn:aws:bedrock:`us-east-1`:`123456789012`:knowledge-base/`XXXXXXXXXX`"
 },
 {
 "Sid": "CreateLogDeliveryPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:PutDeliverySource",
 "logs:CreateDelivery"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:delivery-source:*",
 "arn:aws:logs:`us-east-1`:`123456789012`:delivery:*",
 "arn:aws:logs:`us-east-1`:`444455556666`:delivery-destination:*"
 ]
 }
 ]
}`

```

## Create delivery source

To begin, account A creates a delivery source with their bedrock knowledge
base:

```
aws logs put-delivery-source --name my-delivery-source --log-type APPLICATION_LOGS --resource-arn arn:aws:bedrock:`region`:`AAAAAAAAAAAA`:knowledge-base/`XXXXXXXXXX`
```

Next, account B must create the delivery destination using one of the flows
below:

- [Configure delivery to an Amazon S3
  bucket](#crossaccount-example-delivery-S3 "#crossaccount-example-delivery-S3")
- [Configure delivery to a
  Firehose stream](#crossaccount-example-delivery-Firehose "#crossaccount-example-delivery-Firehose")

## Configure delivery to an Amazon S3

bucket

Account B wants to receive the logs into their S3 bucket with the ARN
arn:aws:s3:::amzn-s3-demo-bucket For this example, account B will need the following
permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PutLogDestinationPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:PutDeliveryDestination",
 "logs:PutDeliveryDestinationPolicy"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:delivery-destination:*"
 }
 ]
}`

```

The bucket will need the following permissions in its bucket policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSLogsDeliveryWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/AWSLogs/`123456789012`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": [
 "`123456789012`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`123456789012`:delivery-source:my-delivery-source"
 ]
 }
 }
 }
 ]
}`

```

If the bucket is encrypted with SSE-KMS, ensure the AWS KMS key policy has the
appropriate permissions. For example, if the KMS key is
`arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab``,
use the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowLogsGenerateDataKey",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`123456789012`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`123456789012`:delivery-source:my-delivery-source"
 ]
 }
 }
 }
 ]
}`

```

Account B can then create a delivery destination with the S3 bucket as the
destination resource:

```
aws logs put-delivery-destination --name my-s3-delivery-destination --delivery-destination-configuration "destinationResourceArn=arn:aws:s3:::amzn-s3-demo-bucket"
```

Next, Account B creates a delivery destination policy on their newly created
delivery destination, which will give permission for Account A to create a log
delivery. The policy that will be added to the newly created delivery destination is
the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateDelivery",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`123456789012`"
 },
 "Action": [
 "logs:CreateDelivery"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:delivery-destination:`amzn-s3-demo-bucket`"
 }
 ]
}`

```

This policy will be saved in Account B’s computer as
`destination-policy-s3.json` To attach this resource, Account
B will run the following command:

```
aws logs put-delivery-destination-policy --delivery-destination-name my-s3-delivery-destination --delivery-destination-policy file://destination-policy-s3.json
```

Lastly, Account A creates the delivery, which links the delivery source in Account
A to the delivery destination in Account B.

```
aws logs create-delivery --delivery-source-name my-delivery-source --delivery-destination-arn arn:aws:logs:`region`:`BBBBBBBBBBBB`:delivery-destination:my-s3-delivery-destination
```

## Configure delivery to a

Firehose stream

In this example, Account B wants to receive logs into their Firehose stream. The
Firehose stream has the following ARN and is configured to use the DirectPut delivery
stream type:

`arn:aws:firehose:`us-east-1`:`111122223333`:deliverystream/`log-delivery-stream``

For this example, Account B needs the following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowFirehoseCreateSLR",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/delivery.logs.amazonaws.com/AWSServiceRoleForLogDelivery"
 },
 {
 "Sid": "AllowFirehoseTagging",
 "Effect": "Allow",
 "Action": [
 "firehose:TagDeliveryStream"
 ],
 "Resource": "arn:aws:firehose:`us-east-1`:`111122223333`:deliverystream/`X`"
 },
 {
 "Sid": "AllowFirehoseDeliveryDestination",
 "Effect": "Allow",
 "Action": [
 "logs:PutDeliveryDestination",
 "logs:PutDeliveryDestinationPolicy"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:delivery-destination:*"
 }
 ]
}`

```

The Firehose stream must have the tag `LogDeliveryEnabled` set to
`true`.

Account B will then create a delivery destination with the Firehose stream as the
destination resource:

```
aws logs put-delivery-destination --name my-fh-delivery-destination --delivery-destination-configuration "destinationResourceArn=arn:aws:firehose:`region`:`BBBBBBBBBBBB`:deliverystream/`X`"
```

Next, Account B creates a delivery destination policy on their newly created
delivery destination, which will give permission for Account A to create a log
delivery. The policy to be added to the newly created delivery destination is the
following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateDelivery",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`123456789012`"
 },
 "Action": [
 "logs:CreateDelivery"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:delivery-destination:`amzn-s3-demo-bucket`"
 }
 ]
}`

```

This policy will be saved in Account B’s computer as
`destination-policy-fh.json` To attach this resource, Account
B runs the following command:

```
aws logs put-delivery-destination-policy --delivery-destination-name my-fh-delivery-destination --delivery-destination-policy file://destination-policy-fh.json
```

Lastly, Account A creates the delivery, which links the delivery source in Account
A to the delivery destination in Account B.

```
aws logs create-delivery --delivery-source-name my-delivery-source --delivery-destination-arn arn:aws:logs:`region`:`BBBBBBBBBBBB`:delivery-destination:my-fh-delivery-destination
```
