# Subscribing to Amazon SNS GuardDuty announcements

This section provides information about subscribing to Amazon SNS (Simple Notification Service)
for GuardDuty announcements to receive notifications about newly released finding types, updates
to the existing finding types, and other functionality changes. Notifications are available
in all formats that Amazon SNS supports.

The GuardDuty SNS sends announcement about updates to the GuardDuty service across AWS to any
subscribed account. To receive notifications about findings within your account, see [Processing GuardDuty findings with
Amazon EventBridge](guardduty_findings_eventbridge.md "guardduty_findings_eventbridge.md").

###### Note

Your IAM user must have `sns::subscribe` permissions to subscribe to an
SNS.

You can subscribe an Amazon SQS queue to this notification topic, but you must use a topic
ARN that is in the same Region. For more information, see [Tutorial: Subscribing an Amazon SQS queue to an Amazon SNS topic](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.md") in the
_Amazon Simple Queue Service developer guide_.

You can also use an AWS Lambda function to trigger events when notifications are received.
For more information, see [Invoking Lambda functions using Amazon
SNS notifications](../../../sns/latest/dg/sns-lambda-as-subscriber.md "../../../sns/latest/dg/sns-lambda-as-subscriber.md") in the _Amazon Simple Queue Service developer
guide_.

The Amazon SNS topic ARNs for each Region are shown below.

| AWS Region                                     | Amazon SNS topic ARN                                                   |
| ---------------------------------------------- | ---------------------------------------------------------------------- |
| US East (N. Virginia)<br>• `us-east-1`         | `arn:aws:sns:us-east-1:242987662583:GuardDutyAnnouncements`            |
| US East (Ohio)<br>• `us-east-2`                | `arn:aws:sns:us-east-2:118283430703:GuardDutyAnnouncements`            |
| US West (N. California)<br>• `us-west-1`       | `arn:aws:sns:us-west-1:144182107116:GuardDutyAnnouncements`            |
| US West (Oregon)<br>• `us-west-2`              | `arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements`            |
| Canada (Central)<br>• `ca-central-1`           | `arn:aws:sns:ca-central-1:107430051933:GuardDutyAnnouncements`         |
| Canada West (Calgary)<br>• `ca-west-1`         | `arn:aws:sns:ca-west-1:440427180217:GuardDutyAnnouncements`            |
| Europe (Stockholm)<br>• `eu-north-1`           | `arn:aws:sns:eu-north-1:973841112453:GuardDutyAnnouncements`           |
| Europe (Ireland)<br>• `eu-west-1`              | `arn:aws:sns:eu-west-1:965013871422:GuardDutyAnnouncements`            |
| Europe (London)<br>• `eu-west-2`               | `arn:aws:sns:eu-west-2:506403581195:GuardDutyAnnouncements`            |
| Europe (Paris)<br>• `eu-west-3`                | `arn:aws:sns:eu-west-3:436163563069:GuardDutyAnnouncements`            |
| Europe (Frankfurt)<br>• `eu-central-1`         | `arn:aws:sns:eu-central-1:378365507264:GuardDutyAnnouncements`         |
| Europe (Zurich)<br>• `eu-central-2`            | `arn:aws:sns:eu-central-2:383009515534:GuardDutyAnnouncements`         |
| Asia Pacific (Hong Kong)<br>• `ap-east-1`      | `arn:aws:sns:ap-east-1:646602203151:GuardDutyAnnouncements`            |
| Asia Pacific (Tokyo)<br>• `ap-northeast-1`     | `arn:aws:sns:ap-northeast-1:741172661024:GuardDutyAnnouncements`       |
| Asia Pacific (Seoul)<br>• `ap-northeast-2`     | `arn:aws:sns:ap-northeast-2:464168911255:GuardDutyAnnouncements`       |
| Asia Pacific (Singapore)<br>• `ap-southeast-1` | `arn:aws:sns:ap-southeast-1:476419727788:GuardDutyAnnouncements`       |
| Asia Pacific (Sydney)<br>• `ap-southeast-2`    | `arn:aws:sns:ap-southeast-2:457615622431:GuardDutyAnnouncements`       |
| Asia Pacific (Mumbai)<br>• `ap-south-1`        | `arn:aws:sns:ap-south-1:926826061926:GuardDutyAnnouncements`           |
| South America (São Paulo)<br>• `sa-east-1`     | `arn:aws:sns:sa-east-1:955633302743:GuardDutyAnnouncements`            |
| AWS GovCloud (US-West)<br>• `us-gov-west-1`    | `arn:aws-us-gov:sns:us-gov-west-1:430639793359:GuardDutyAnnouncements` |
| China (Beijing)<br>• `cn-north-1`              | `arn:aws-cn:sns:cn-north-1:002991280229:GuardDutyAnnouncements`        |
| China (Ningxia)<br>• `cn-northwest-1`          | `arn:aws-cn:sns:cn-northwest-1:003033775354:GuardDutyAnnouncements`    |
| Middle East (Bahrain)<br>• `me-south-1`        | `arn:aws:sns:me-south-1:552740612889:GuardDutyAnnouncements`           |
| Middle East (UAE)<br>• `me-central-1`          | `arn:aws:sns:me-central-1:030935290150:GuardDutyAnnouncements`         |
| Europe (Milan)<br>• `eu-south-1`               | `arn:aws:sns:eu-south-1:188461706213:GuardDutyAnnouncements`           |
| Europe (Spain)<br>• `eu-south-2`               | `arn:aws:sns:eu-south-2:445632894446:GuardDutyAnnouncements`           |
| AWS GovCloud (US-East)<br>• `us-gov-east-1`    | `arn:aws:sns:us-gov-east-1:143972945659:GuardDutyAnnouncements`        |
| Asia Pacific (Osaka)<br>• `ap-northeast-3`     | `arn:aws:sns:ap-northeast-3:129086577509:GuardDutyAnnouncements`       |
| Asia Pacific (Jakarta)<br>• `ap-southeast-3`   | `arn:aws:sns:ap-southeast-3:225965583551:GuardDutyAnnouncements`       |
| Asia Pacific (Hyderabad)<br>• `ap-south-2`     | `arn:aws:sns:ap-south-2:595653072700:GuardDutyAnnouncements`           |
| Asia Pacific (Melbourne)<br>• `ap-southeast-4` | `arn:aws:sns:ap-southeast-4:529900636122:GuardDutyAnnouncements`       |
| Asia Pacific (Malaysia)<br>• `ap-southeast-5`  | `arn:aws:sns:ap-southeast-5:343218181797:GuardDutyAnnouncements`       |
| Israel (Tel Aviv)<br>• `il-central-1`          | `arn:aws:sns:il-central-1:847886274986:GuardDutyAnnouncements`         |
| Asia Pacific (Thailand)<br>• `ap-southeast-7`  | `arn:aws:sns:ap-southeast-7:863518448376:GuardDutyAnnouncements`       |
| Mexico (Central)<br>• `mx-central-1`           | `arn:aws:sns:mx-central-1:060795916546:GuardDutyAnnouncements`         |
| Asia Pacific (Taipei)<br>• `ap-east-2`         | `arn:aws:sns:ap-east-2:604225987917:GuardDutyAnnouncements`            |

###### To subscribe to the GuardDuty update notification email in the AWS Management Console

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the Region list, choose the same Region as the topic ARN to which to subscribe.
   This example uses the `us-west-2` Region.
3. In the left navigation pane, choose **Subscriptions**,
   **Create subscription**.
4. In the **Create Subscription** dialog box, for **Topic
   ARN**, paste the topic ARN:
   `arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements`.
5. For **Protocol**, choose **Email**. For
   **Endpoint**, type an email address that you can use to receive
   the notification.
6. Choose **Create subscription**.
7. In your email application, open the message from AWS Notifications and open the
   link to confirm your subscription.

Your web browser displays a confirmation response from Amazon SNS.

###### To subscribe to the GuardDuty update notification email with the AWS CLI

1. Run the following command with the AWS CLI:

```
 aws  sns --region `us-west-2` subscribe --topic-arn arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements --protocol `email` --notification-endpoint `your_email@your_domain.com`
```

2. In your email application, open the message from AWS Notifications and open the
   link to confirm your subscription.

Your web browser displays a confirmation response from Amazon SNS.

## Amazon SNS message format

An example GuardDuty general notification message:

```
{
    "Type" : "Notification",
    "MessageId" : "9101dc6b-726f-4df0-8646-ec2f94e674bc",
    "TopicArn" : "arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements",
    "Message" : "{\"version\":\"1\",\"type\":\"GENERAL\",\"message\":[{\"title\":\"Updated AmazonGuardDutyFullAccess_v2 policy\",\"body\":\"Added permission that allows you to pass an IAM role to GuardDuty when you enable Malware Protection for S3.\",\"links\":[\"https://docs.aws.amazon.com//guardduty/latest/ug/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2\"]}]}",
    "Timestamp" : "2018-03-09T00:25:43.483Z",
    "SignatureVersion" : "1",
    "Signature" : "XWox8GDGLRiCgDOXlo/fG9Lu/88P8S0FL6M6oQYOmUFzkucuhoblsdea3BjqdCHcWR7qdhMPQnLpN7y9iBrWVUqdAGJrukAI8athvAS+4AQD/V/QjrhsEnlj+GaiW+ozAu006X6GopOzFGnCtPMROjCMrMonjz7Hpv/8KRuMZR3pyQYm5d4wWB7xBPYhUMuLoZ1V8YFs55FMtgQV/YLhSYuEu0BP1GMtLQauxDkscOtPP/vjhGQLFx1Q9LTadcQiRHtNIBxWL87PSI+BVvkin6AL7PhksvdQ7FAgHfXsit+6p8GyOvKCqaeBG7HZhR1AbpyVka7JSNRO/6ssyrlj1g==",
    "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem",
    "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements:9225ed2b-7228-4665-8a01-c8a5db6859f4"
}
```

The parsed Message value (with escaped quotes removed) is shown below:

```
{
        "version": "1",
        "type": "GENERAL",
        "message": [
            {
                "title": "Updated AmazonGuardDutyFullAccess policy",
                "body": "Added permission that allows you to pass an IAM role to GuardDuty when you enable Malware Protection for S3.",
                "links": [
                    "https://docs.aws.amazon.com//guardduty/latest/ug/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2"
                ]
             }
        ]
}
```

An example GuardDuty update notification message about new findings is shown below:

```
{
    "Type" : "Notification",
    "MessageId" : "9101dc6b-726f-4df0-8646-ec2f94e674bc",
    "TopicArn" : "arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements",
    "Message" : "{\"version\":\"1\",\"type\":\"NEW_FINDINGS\",\"findingDetails\":[{\"link\":\"https://docs.aws.amazon.com//guardduty/latest/ug/guardduty_unauthorized.html\",\"findingType\":\"UnauthorizedAccess:EC2/TorClient\",\"findingDescription\":\"This finding informs you that an EC2 instance in your AWS environment is making connections to a Tor Guard or an Authority node. Tor is software for enabling anonymous communication. Tor Guards and Authority nodes act as initial gateways into a Tor network. This traffic can indicate that this EC2 instance is acting as a client on a Tor network. A common use for a Tor client is to circumvent network monitoring and filter for access to unauthorized or illicit content. Tor clients can also generate nefarious Internet traffic, including attacking SSH servers. This activity can indicate that your EC2 instance is compromised.\"}]}",
    "Timestamp" : "2018-03-09T00:25:43.483Z",
    "SignatureVersion" : "1",
    "Signature" : "XWox8GDGLRiCgDOXlo/fG9Lu/88P8S0FL6M6oQYOmUFzkucuhoblsdea3BjqdCHcWR7qdhMPQnLpN7y9iBrWVUqdAGJrukAI8athvAS+4AQD/V/QjrhsEnlj+GaiW+ozAu006X6GopOzFGnCtPMROjCMrMonjz7Hpv/8KRuMZR3pyQYm5d4wWB7xBPYhUMuLoZ1V8YFs55FMtgQV/YLhSYuEu0BP1GMtLQauxDkscOtPP/vjhGQLFx1Q9LTadcQiRHtNIBxWL87PSI+BVvkin6AL7PhksvdQ7FAgHfXsit+6p8GyOvKCqaeBG7HZhR1AbpyVka7JSNRO/6ssyrlj1g==",
    "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem",
    "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements:9225ed2b-7228-4665-8a01-c8a5db6859f4"
}
```

The parsed Message value (with escaped quotes removed) is shown below:

```
{
    "version": "1",
    "type": "NEW_FINDINGS",
    "findingDetails": [{
        "link": "https://docs.aws.amazon.com//guardduty/latest/ug/guardduty_unauthorized.html",
        "findingType": "UnauthorizedAccess:EC2/TorClient",
        "findingDescription": "This finding informs you that an EC2 instance in your AWS environment is making connections to a Tor Guard or an Authority node. Tor is software for enabling anonymous communication. Tor Guards and Authority nodes act as initial gateways into a Tor network. This traffic can indicate that this EC2 instance is acting as a client on a Tor network. A common use for a Tor client is to circumvent network monitoring and filter for access to unauthorized or illicit content. Tor clients can also generate nefarious Internet traffic, including attacking SSH servers. This activity can indicate that your EC2 instance is compromised."
    }]
}
```

An example GuardDuty update notification message about GuardDuty functionality updates is
shown below:

```
{
    "Type" : "Notification",
    "MessageId" : "9101dc6b-726f-4df0-8646-ec2f94e674bc",
    "TopicArn" : "arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements",
    "Message" : "{\"version\":\"1\",\"type\":\"NEW_FEATURES\",\"featureDetails\":[{\"featureDescription\":\"Customers with high-volumes of global CloudTrail events should see a net positive impact on their GuardDuty costs.\",\"featureLink\":\"https://docs.aws.amazon.com//guardduty/latest/ug/guardduty_data-sources.html#guardduty_controlplane\"}]}",
    "Timestamp" : "2018-03-09T00:25:43.483Z",
    "SignatureVersion" : "1",
    "Signature" : "XWox8GDGLRiCgDOXlo/fG9Lu/88P8S0FL6M6oQYOmUFzkucuhoblsdea3BjqdCHcWR7qdhMPQnLpN7y9iBrWVUqdAGJrukAI8athvAS+4AQD/V/QjrhsEnlj+GaiW+ozAu006X6GopOzFGnCtPMROjCMrMonjz7Hpv/8KRuMZR3pyQYm5d4wWB7xBPYhUMuLoZ1V8YFs55FMtgQV/YLhSYuEu0BP1GMtLQauxDkscOtPP/vjhGQLFx1Q9LTadcQiRHtNIBxWL87PSI+BVvkin6AL7PhksvdQ7FAgHfXsit+6p8GyOvKCqaeBG7HZhR1AbpyVka7JSNRO/6ssyrlj1g==",
    "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem",
    "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements:9225ed2b-7228-4665-8a01-c8a5db6859f4"
}
```

The parsed Message value (with escaped quotes removed) is shown below:

```
{
    "version": "1",
    "type": "NEW_FEATURES",
    "featureDetails": [{
        "featureDescription": "Customers with high-volumes of global CloudTrail events should see a net positive impact on their GuardDuty costs.",
        "featureLink": "https://docs.aws.amazon.com//guardduty/latest/ug/guardduty_data-sources.html#guardduty_controlplane"
    }]
}
```

An example GuardDuty update notification message about updated findings is shown
below:

```
{
    "Type": "Notification",
    "MessageId": "9101dc6b-726f-4df0-8646-ec2f94e674bc",
    "TopicArn": "arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements",
    "Message": "{\"version\":\"1\",\"type\":\"UPDATED_FINDINGS\",\"findingDetails\":[{\"link\":\"https://docs.aws.amazon.com//guardduty/latest/ug/guardduty_unauthorized.html\",\"findingType\":\"UnauthorizedAccess:EC2/TorClient\",\"description\":\"Increased severity value from 5 to 8.\"}]}",
    "Timestamp": "2018-03-09T00:25:43.483Z",
    "SignatureVersion": "1",
    "Signature": "XWox8GDGLRiCgDOXlo/fG9Lu/88P8S0FL6M6oQYOmUFzkucuhoblsdea3BjqdCHcWR7qdhMPQnLpN7y9iBrWVUqdAGJrukAI8athvAS+4AQD/V/QjrhsEnlj+GaiW+ozAu006X6GopOzFGnCtPMROjCMrMonjz7Hpv/8KRuMZR3pyQYm5d4wWB7xBPYhUMuLoZ1V8YFs55FMtgQV/YLhSYuEu0BP1GMtLQauxDkscOtPP/vjhGQLFx1Q9LTadcQiRHtNIBxWL87PSI+BVvkin6AL7PhksvdQ7FAgHfXsit+6p8GyOvKCqaeBG7HZhR1AbpyVka7JSNRO/6ssyrlj1g==",
    "SigningCertURL": "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem",
    "UnsubscribeURL": "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:934957504740:GuardDutyAnnouncements:9225ed2b-7228-4665-8a01-c8a5db6859f4"
}
```

The parsed Message value (with escaped quotes removed) is shown below:

```
{
    "version": "1",
    "type": "UPDATED_FINDINGS",
    "findingDetails": [{
        "link": "https://docs.aws.amazon.com//guardduty/latest/ug/guardduty_unauthorized.html",
        "findingType": "UnauthorizedAccess:EC2/TorClient",
        "description": "Increased severity value from 5 to 8."
    }]
}
```
