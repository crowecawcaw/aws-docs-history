# Receive alerts for interface endpoint

events

You can create a notification to receive alerts for specific events related to your
interface endpoint. For example, you can receive an email when a connection request is
accepted or rejected.

###### Tasks

- [Create an SNS notification](#create-sns-notification "#create-sns-notification")
- [Add an access policy](#add-access-policy "#add-access-policy")
- [Add a key policy](#add-key-policy "#add-key-policy")

## Create an SNS notification

Use the following procedure to create an Amazon SNS topic for the notifications and subscribe
to the topic.

###### To create a notification for an interface endpoint using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Select the interface endpoint.
4. From the **Notifications** tab, choose **Create
   notification**.
5. For **Notification ARN**, choose the [Amazon Resource Name](../../../glossary/latest/reference/glos-chap.md#ARN "../../../glossary/latest/reference/glos-chap.md#ARN") (ARN) for the SNS topic that
   you created.
6. To subscribe to an event, select it from **Events**.
   - **Connect** – The service consumer created the interface
     endpoint. This sends a connection request to the service provider.
   - **Accept** – The service provider accepted the connection
     request.
   - **Reject** – The service provider rejected the connection
     request.
   - **Delete** – The service consumer deleted the interface
     endpoint.

7. Choose **Create notification**.

###### To create a notification for an interface endpoint using the command line

- [create-vpc-endpoint-connection-notification](../../../cli/latest/reference/ec2/create-vpc-endpoint-connection-notification.md "../../../cli/latest/reference/ec2/create-vpc-endpoint-connection-notification.md") (AWS CLI)
- [New-EC2VpcEndpointConnectionNotification](../../../powershell/latest/reference/items/New-EC2VpcEndpointConnectionNotification.md "../../../powershell/latest/reference/items/New-EC2VpcEndpointConnectionNotification.md") (Tools for Windows PowerShell)

## Add an access policy

Add an access policy to the Amazon SNS topic that allows AWS PrivateLink to publish
notifications on your behalf, such as the following. For more information, see [How do I edit my Amazon SNS
topic's access policy?](https://repost.aws/knowledge-center/sns-edit-topic-access-policy "https://repost.aws/knowledge-center/sns-edit-topic-access-policy") Use the `aws:SourceArn` and
`aws:SourceAccount` global condition keys to protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "vpce.amazonaws.com"
 },
 "Action": "SNS:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`111111111111`:`topic-name`",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ec2:`us-east-1`:`111111111111`:vpc-endpoint/`endpoint-id`"
 },
 "StringEquals": {
 "aws:SourceAccount": "`111111111111`"
 }
 }
 }
 ]
}`

```

## Add a key policy

If you're using encrypted SNS topics, the resource policy for the KMS key must trust
AWS PrivateLink to call AWS KMS API operations. The following is an example key policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "vpce.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111111111111`:key/`key-id`",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ec2:`us-east-1`:`111111111111`:vpc-endpoint/`endpoint-id`"
 },
 "StringEquals": {
 "aws:SourceAccount": "`111111111111`"
 }
 }
 }
 ]
}`

```
