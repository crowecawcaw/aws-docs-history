Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Monitoring the scheduled

query

For the Amazon SNS topic that you specify to send email notifications, create the Amazon SNS
topic using the query editor v2 by navigating to the **SNS notifications**
section, **Turn on** monitoring, and create the topic with
**Create SNS topic**. The query editor v2 creates the Amazon SNS topic and adds a
service principal to the access policy for Amazon EventBridge.

The following is an example **Access policy** that is created in the
Amazon SNS topic. In the example, the AWS Region `us-west-2`,
AWS account `123456789012`, and Amazon SNS topic
`select-version-pdx-testunload` are used.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "__default_policy_ID",
 "Statement": [
 {
 "Sid": "Allow_Publish_Events",
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "sns:Publish",
 "Resource": "arn:aws:sns:`us-west-2`:`123456789012`:`select-version-pdx-testunload`"
 }
 ]
}`

```

When the scheduled query runs, Amazon SNS sends AWS notification emails. The following
example shows an email sent to `myemail@example.com` for
scheduled query `QS2-may25a` that ran on AWS Region
`eu-north-1` in AWS account
`123456789012` using Amazon SNS notification topic
`may25a-SNS`.

```
{"version":"0","id":"8e4323ec-5258-7138-181b-91290e30ff9b","detail-type":"Scheduled Event","source":"aws.events","account":"`123456789012`","time":"2023-05-25T15:22:00Z",
                    "region":"`eu-north-1`","resources":["arn:aws:events:`eu-north-1`:`123456789012`:rule/`QS2-may25a`"],"detail":{}}

--
If you wish to stop receiving notifications from this topic, please click or visit the link below to unsubscribe:
https://sns.`eu-north-1`.amazonaws.com/unsubscribe.html?SubscriptionArn=arn:aws:sns:`eu-north-1`:`123456789012`:`may25a-SNS`:0c1a3d05-39c2-4507-bc3d-47250513d7b0&Endpoint=`myemail@example.com`

Please do not reply directly to this email. If you have any questions or comments regarding this email, please contact us at https://aws.amazon.com/support

```
