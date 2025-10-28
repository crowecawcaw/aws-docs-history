# AMS AMI notifications with SNS

AMS provides an AMI notification service. You can use it to subscribe to an Amazon Simple Notification Service
(SNS) topic that notifies you when AMS AMI updates have been released. You can choose to receive notifications for only
the AMS AMIs you use, or you can sign up to receive update notifications for all AMS AMIs. For more information on SNS
topics, see [What is Amazon Simple Notification Service?](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md")

Whenever AMIs are released, we send notifications to the subscribers of the corresponding topic; this section describes how to subscribe
to the AMS AMI notifications.

**Sample message**

```
{
  "Type" : "Notification",
  "MessageId" : "example messageId",
  "TopicArn" : "arn:aws:sns:us-east-1:591688410472:customer-ams-windows2019",
  "Subject" : "New AMS AMIs are Now Available",
  "Message" : "{"v1": {"Message": "A new version of the AMS Amazon Machine Images has been released. You are now able to launch new EC2 stacks from these AMIs.
  Please use this time to update any dependencies such as CloudFormation or Autoscaling groups. Release Notes Windows - Contains latest Windows Patches:
  Microsoft Windows Server 2008 R2 Datacenter - (KB2819745, KB3018238, KB4507004, KB4507437) Microsoft Windows Server 2016 Datacenter Security Enhancedn - (KB4509091, KB4507459)
  Microsoft Windows Server 2016 Datacentern - (KB4509091, KB4507459) Microsoft Windows Server 2012 R2 Security Enhancedn - (KB3191564, KB3003057, KB3013172, KB3185319, KB4504418,
  KB4506996, KB4507463) Microsoft Windows Server 2012 R2 Standardn - (KB3003057, KB3013172, KB3185319, KB4504418, KB4506996, KB4507463) Linux - Contains latest Linux patches -
  All AMIs now force domainjoin-cli leave before domainjoin-cli join for better stability in the domain join process.", "images":
  {"images": {"image_name": "customer-ams-windows2019-2021.08-1", "image_id": "ami-05dfa45396fddaa5e"}}, "region": "us-east-1"}}",
  "Timestamp" : "2021-09-03T19:05:57.882Z",
  "SignatureVersion" : "1",
  "Signature" : "example sig",
  "SigningCertURL" : "example url",
  "UnsubscribeURL" : "example url"
}
```

Possible AMS AMI topics to subscribe to:

- **ALL**: Use `customer-ams-all-amis`. This topic subscription
  notifies you when any of the AMS AMIs are updated.
- **AMS AWS Linux AMIs**: For Amazon Linux, use
  `customer-ams-amazon1` and
  `customer-ams-amazon1-security-enhanced`. For Amazon Linux 2, use
  `customer-ams-amazon2` and
  `customer-ams-amazon2-security-enhanced`.
- **AMS SUSE Linux AMIs**: Use `customer-ams-sles12` or `customer-ams-sles15`.
- **AMS AWS RedHat AMIs**: Use `customer-ams-rhel8`, `customer-ams-rhel8-security-enhanced`,
  `customer-ams-rhel7`, `customer-ams-rhel7-security-enhanced`.
- **AMS AWS CentOs AMIs**: Use `customer-ams-centos7`, `customer-ams-centos7-security-enhanced`.
- **AMS Ubuntu AMIs**: Use `customer-ams-ubuntu18`.
- **AMS AWS Windows AMIs**: Use `customer-ams-windows2019`, `customer-ams-windows2019-security-enhanced`,
  `customer-ams-windows2016`, `customer-ams-windows2016-security-enhanced`, `customer-ams-windows2012`,
  `customer-ams-windows2012r2`, `customer-ams-windows2012r2-security-enhanced`, `customer-ams-windows2022`.
  To subscribe to AMS new AMI notifications by using the Amazon SNS console:

1. Open the Amazon SNS console to the [Dashboard](https://console.aws.amazon.com/sns/v2/home "https://console.aws.amazon.com/sns/v2/home").
2. In the upper-right corner, change to the AWS Region for the AMIs that you are subscribing to.
3. In the left-navigation pane, choose **Subscriptions**, and then choose **Create subscription**.
4. Provide the following information:
   1. **Topic ARN**: `arn:aws:sns:{`REGION`}:287847593866:{`AMS_AMI_NAME`}`
      where REGION is the selected AWS Region (where the SNS notification was created) and AMS_AMI_NAME is the AMI that you want notifications about. Examples:
      - To subscribe to notifications of new AMS Amazon Linux AMIs in AWS Region us-east-1, use this
        **Topic ARN** = `arn:aws:sns:us-east-1:287847593866:customer-ams-amazon1`.
      - To subscribe to notifications of new AMS Window Server 2016 AMIs in AWS Region us-west-2, use this
        **Topic ARN** = `arn:aws:sns:us-west-2:287847593866:customer-ams-windows2016`

   2. For **Protocol**, choose **Email**.
   3. For **Endpoint**, enter an email address that you can use to receive the
      notifications. We recommend a distribution list rather than an individual's email.

5. Choose **Create subscription**.
6. When you receive a confirmation email with the subject line "AWS Notification - Subscription
   Confirmation," open the email and choose **Confirm subscription** to complete your subscription.

###### Note

You are not limited to email for the **Protocol**. For information on other acceptable protocols and how to use them, see
[subscribe](../../../cli/latest/reference/sns/subscribe.md "../../../cli/latest/reference/sns/subscribe.md").

To unsubscribe from AMS new AMI notifications by using the AWS SNS console:

1. Open the Amazon SNS console to the [Dashboard](https://console.aws.amazon.com/sns/v2/home "https://console.aws.amazon.com/sns/v2/home").
2. In the navigation bar, change to the AWS Region of your choice. You must use the AWS Region in which you want to receive notifications for the corresponding AMIs.
3. In the navigation pane, choose **Subscriptions**, select the subscription, and then choose **Actions** -> **Delete subscriptions**.
4. When prompted for confirmation, choose **Delete**.
   To subscribe to AMS New AMI notifications using the
   Deployment | Ingestion | Stack from CloudFormation Template | Create (ct-36cn2avfrrj9v):

5. To subscribe to the AmazonLinuxSubscription, create and save an execution parameters JSON
   file; this example names it CreateSubscribeAmiParams.json:

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "AmazonLinuxSubscription":{
              "Type" : "AWS::SNS::Subscription",
              "Properties": {
                "TopicArn": "arn:aws:sns:{`REGION`}:287847593866:{`AMS_AMI_NAME`}",
                "Protocol": "email",
                "Endpoint": "`username@yourdomain.com`"
            }
        }
      }
}

```

2. Create and save the RFC parameters JSON file with the following content; this example names it CreateSubscribeAmiRfc.json file:

```
{
   "ChangeTypeId": "ct-36cn2avfrrj9v",
   "ChangeTypeVersion": "1.0",
   "Title": "`cfn-ingest-subscribe-ami`"
}
```

3. Create the RFC, specifying the CreateSubscribeAmiRfc file and the CreateSubscribeAmiParams file:

```
aws amscm create-rfc --cli-input-json file://CreateSubscribeAmiRfc.json  --execution-parameters file://CreateSubscribeAmiParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
For examples of creating AMIs, see
[Create AMI](../ctref/ex-ami-create-col.md "../ctref/ex-ami-create-col.md").

For information on consuming AMIs programmatically, see
[EC2 stack: creating](../ctref/ex-ec2-create-col.md "../ctref/ex-ec2-create-col.md").
