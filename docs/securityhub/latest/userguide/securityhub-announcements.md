

# Subscribing to Security Hub CSPM announcements with Amazon SNS
<a name="securityhub-announcements"></a>

This section provides information about subscribing to AWS Security Hub CSPM announcements with Amazon Simple Notification Service (Amazon SNS) to receive notifications about Security Hub CSPM. 

After subscribing, you will receive notifications about the following events (note the corresponding `AnnouncementType` for each event):
+ `NEW_STANDARDS_CONTROLS` – New Security Hub CSPM controls or standards have been added.
+ `RETIRED_STANDARDS_CONTROLS` – Existing Security Hub CSPM controls or standards have been retired.

Notifications are available in all formats that Amazon SNS supports. You can subscribe to Security Hub CSPM announcements in all [AWS Regions that Security Hub CSPM is available in](https://docs.aws.amazon.com/general/latest/gr/sechub.html).

A user must have `Subscribe` permissions to subscribe to an Amazon SNS topic. You can achieve this with Amazon SNS policies, IAM policies, or both. For more information, see [IAM and Amazon SNS policies together](https://docs.aws.amazon.com/sns/latest/dg/sns-using-identity-based-policies.html#iam-and-sns-policies) in the *Amazon Simple Notification Service Developer Guide*.

**Note**  
Security Hub CSPM sends Amazon SNS announcements about updates to the Security Hub CSPM service to any subscribed AWS account. To receive notifications about Security Hub CSPM findings, see [Reviewing finding details and history in Security Hub CSPM](securityhub-findings-viewing.md).

You can subscribe to an Amazon Simple Queue Service (Amazon SQS) queue for an Amazon SNS topic, but you must use an Amazon SNS topic Amazon Resource Name (ARN) that is in the same Region. For more information, see [Subscribing a queue to an Amazon SNS topic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-subscribe-queue-sns-topic.html) in the *Amazon Simple Queue Service Developer Guide*.

You can also use an AWS Lambda function to invoke events when you receive notifications. For more information, including sample function code, see [Tutorial: Using AWS Lambda with Amazon Simple Notification Service](https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html) in the *AWS Lambda Developer Guide*.

The Amazon SNS topic ARNs for each Region are as follows.


| AWS Region | Amazon SNS topic ARN | 
| --- | --- | 
| US East (Ohio) | arn:aws:sns:us-east-2:291342846459:SecurityHubAnnouncements | 
| US East (N. Virginia) | arn:aws:sns:us-east-1:088139225913:SecurityHubAnnouncements | 
| US West (N. California) | arn:aws:sns:us-west-1:137690824926:SecurityHubAnnouncements | 
| US West (Oregon) | arn:aws:sns:us-west-2:393883065485:SecurityHubAnnouncements | 
| Africa (Cape Town) | arn:aws:sns:af-south-1:463142546776:SecurityHubAnnouncements | 
| Asia Pacific (Hong Kong) | arn:aws:sns:ap-east-1:464812404305:SecurityHubAnnouncements | 
| Asia Pacific (Hyderabad) | arn:aws:sns:ap-south-2:849907286123:SecurityHubAnnouncements | 
| Asia Pacific (Jakarta) | arn:aws:sns:ap-southeast-3:627843640627:SecurityHubAnnouncements | 
| Asia Pacific (Mumbai) | arn:aws:sns:ap-south-1:707356269775:SecurityHubAnnouncements | 
| Asia Pacific (Osaka) | arn:aws:sns:ap-northeast-3:633550238216:SecurityHubAnnouncements | 
| Asia Pacific (Seoul) | arn:aws:sns:ap-northeast-2:374299265323:SecurityHubAnnouncements | 
| Asia Pacific (Singapore) | arn:aws:sns:ap-southeast-1:512267288502:SecurityHubAnnouncements | 
| Asia Pacific (Sydney) | arn:aws:sns:ap-southeast-2:475730049140:SecurityHubAnnouncements | 
| Asia Pacific (Tokyo) | arn:aws:sns:ap-northeast-1:592469075483:SecurityHubAnnouncements | 
| Canada (Central) | arn:aws:sns:ca-central-1:137749997395:SecurityHubAnnouncements | 
| China (Beijing) | arn:aws-cn:sns:cn-north-1:672341567257:SecurityHubAnnouncements | 
| China (Ningxia) | arn:aws-cn:sns:cn-northwest-1:672534482217:SecurityHubAnnouncements | 
| Europe (Frankfurt) | arn:aws:sns:eu-central-1:871975303681:SecurityHubAnnouncements | 
| Europe (Ireland) | arn:aws:sns:eu-west-1:705756202095:SecurityHubAnnouncements | 
| Europe (London) | arn:aws:sns:eu-west-2:883600840440:SecurityHubAnnouncements | 
| Europe (Milan) | arn:aws:sns:eu-south-1:151363035580:SecurityHubAnnouncements | 
| Europe (Paris) | arn:aws:sns:eu-west-3:313420042571:SecurityHubAnnouncements | 
| Europe (Spain) | arn:aws:sns:eu-south-2:777487947751:SecurityHubAnnouncements | 
| Europe (Stockholm) | arn:aws:sns:eu-north-1:191971010772:SecurityHubAnnouncements | 
| Europe (Zurich) | arn:aws:sns:eu-central-2:704347005078:SecurityHubAnnouncements | 
| Israel (Tel Aviv) | arn:aws:sns:il-central-1:726652212146:SecurityHubAnnouncements | 
| Middle East (Bahrain) | arn:aws:sns:me-south-1:585146626860:SecurityHubAnnouncements | 
| Middle East (UAE) | arn:aws:sns:me-central-1:431548502100:SecurityHubAnnouncements | 
| South America (São Paulo) | arn:aws:sns:sa-east-1:359811883282:SecurityHubAnnouncements | 
| AWS GovCloud (US-East) | arn:aws-us-gov:sns:us-gov-east-1:239368469855:SecurityHubAnnouncements | 
| AWS GovCloud (US-West) | arn:aws-us-gov:sns:us-gov-west-1:239334163374:SecurityHubAnnouncements | 

Messages are typically the same across Regions within a [partition](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html), so you can subscribe to one Region in each partition to receive announcements that affect all Regions in that partition. Announcements associated with member accounts are not replicated in the administrator account. As a result, each account, including the administrator account, will only have one copy of each announcement. You can decide which account you want to use to subscribe to Security Hub CSPM announcements.

For information about the cost of subscribing to Security Hub CSPM announcements, see [Amazon SNS pricing](https://aws.amazon.com/sns/pricing/).

**Subscribing to Security Hub CSPM announcements (console)**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the Region list, choose the Region in which you want to subscribe to Security Hub CSPM announcements. This example uses the `us-west-2` Region.

1. In the navigation pane, choose **Subscriptions**, and then choose **Create subscription**.

1. Enter the topic ARN into the **Topic ARN** box. For example, `arn:aws:sns:us-west-2:393883065485:SecurityHubAnnouncements`.

1. For **Protocol**, choose how you want to receive Security Hub CSPM announcements. If you choose **Email**, for **Endpoint**, enter the email address that you want to use to receive announcements.

1. Choose **Create subscription**.

1. Confirm the subscription. For example, if you chose email protocol, Amazon SNS will send a subscription confirmation message to the email you provided.

**Subscribing to Security Hub CSPM announcements (AWS CLI)**

1. Run the following command:

   ```
    aws  sns --region {{us-west-2}} subscribe --topic-arn {{arn:aws:sns:us-west-2:393883065485:SecurityHubAnnouncements}} --protocol {{email}} --notification-endpoint {{your_email@your_domain.com}}
   ```

1. Confirm the subscription. For example, if you chose email protocol, Amazon SNS will send a subscription confirmation message to the email you provided.

## Amazon SNS message format
<a name="securityhub-announcements-example"></a>

The following examples show Security Hub CSPM announcements from Amazon SNS about the introduction of new security controls. Message content varies based on announcement type, but the format is the same for all announcement types. Optionally, a `Link` field that provides details about the announcement may be included.

**Example: Security Hub CSPM announcement for new controls (email protocol)**

```
{
"AnnouncementType":"NEW_STANDARDS_CONTROLS",
"Title":"[New Controls] 36 new Security Hub CSPM controls added to the AWS Foundational Security Best Practices standard",
"Description":"We have added 36 new controls to the AWS Foundational Security Best Practices standard. These include controls for Amazon Auto Scaling (AutoScaling.3, AutoScaling.4, AutoScaling.6), CloudFormation (CloudFormation.1), Amazon CloudFront (CloudFront.10), Amazon Elastic Compute Cloud (Amazon EC2) (EC2.23, EC2.24, EC2.27), Amazon Elastic Container Registry (Amazon ECR) (ECR.1, ECR.2), Amazon Elastic Container Service (Amazon ECS) (ECS.3, ECS.4, ECS.5, ECS.8, ECS.10, ECS.12), Amazon Elastic File System (Amazon EFS) (EFS.3, EFS.4), Amazon Elastic Kubernetes Service (Amazon EKS) (EKS.2), Elastic Load Balancing (ELB.12, ELB.13, ELB.14), Amazon Kinesis (Kinesis.1), AWS Network Firewall (NetworkFirewall.3, NetworkFirewall.4, NetworkFirewall.5), Amazon OpenSearch Service (OpenSearch.7), Amazon Redshift (Redshift.9),
Amazon Simple Storage Service (Amazon S3) (S3.13), Amazon Simple Notification Service (SNS.2), AWS WAF (WAF.2, WAF.3, WAF.4, WAF.6, WAF.7, WAF.8). If you enabled the AWS Foundational Security Best Practices standard in an account and configured Security Hub CSPM to automatically enable new controls, these controls are enabled by default. Availability of controls can vary by Region. "
}
```

**Example: Security Hub CSPM announcement for new controls (email-JSON protocol)**

```
{
  "Type" : "Notification",
  "MessageId" : "d124c9cf-326a-5931-9263-92a92e7af49f",
  "TopicArn" : "arn:aws:sns:us-west-2:393883065485:SecurityHubAnnouncements",
  "Message" : "{\"AnnouncementType\":\"NEW_STANDARDS_CONTROLS\",\"Title\":\"[New Controls] 36 new Security Hub CSPM controls added to the AWS Foundational Security Best Practices standard\",\"Description\":\"We have added 36 new controls to the AWS Foundational Security Best Practices standard. These include controls for Amazon Auto Scaling (AutoScaling.3, AutoScaling.4, AutoScaling.6), CloudFormation (CloudFormation.1), Amazon CloudFront (CloudFront.10), Amazon Elastic Compute Cloud (Amazon EC2) (EC2.23, EC2.24, EC2.27), Amazon Elastic Container Registry (Amazon ECR) (ECR.1, ECR.2), Amazon Elastic Container Service (Amazon ECS) (ECS.3, ECS.4, ECS.5, ECS.8, ECS.10, ECS.12), Amazon Elastic File System (Amazon EFS) (EFS.3, EFS.4), Amazon Elastic Kubernetes Service (Amazon EKS) (EKS.2), Elastic Load Balancing (ELB.12, ELB.13, ELB.14), Amazon Kinesis (Kinesis.1), AWS Network Firewall (NetworkFirewall.3, NetworkFirewall.4, NetworkFirewall.5), Amazon OpenSearch Service (OpenSearch.7), Amazon Redshift (Redshift.9),
Amazon Simple Storage Service (Amazon S3) (S3.13), Amazon Simple Notification Service (SNS.2), AWS WAF (WAF.2, WAF.3, WAF.4, WAF.6, WAF.7, WAF.8). If you enabled the AWS Foundational Security Best Practices standard in an account and configured Security Hub CSPM to automatically enable new controls, these controls are enabled by default. Availability of controls can vary by Region. \"}",
  "Timestamp" : "2022-08-04T19:11:12.652Z",
  "SignatureVersion" : "1",
  "Signature" : "HTHgNFRYMetCvisulgLM4CVySvK9qCXFPHQDxYl9tuCFQuIrd7YO4m4YFR28XKMgzqrF20YP+EilipUm2SOTpEEtOTekU5bn74+YmNZfwr4aPFx0vUuQCVOshmHl37hjkiLjhCg/t53QQiLfP7MH+MTXIUPR37k5SuFCXvjpRQ8ynV532AH3Wpv0HmojDLMg+eg51V1fUsOG8yiJVCBEJhJ1yS+gkwJdhRk2UQab9RcAmE6COK3hRWcjDwqTXz5nR6Ywv1ZqZfLIl7gYKslt+jsyd/k+7kOqGmOJRDr7qhE7H+7vaGRLOptsQnbW8VmeYnDbahEO8FV+Mp1rpV+7Qg==",
  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
  "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:393883065485:SecurityHubAnnouncements:9d0230d7-d582-451d-9f15-0c32818bf61f"
}
```