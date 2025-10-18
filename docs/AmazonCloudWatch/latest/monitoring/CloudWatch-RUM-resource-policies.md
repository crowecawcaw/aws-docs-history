# Using resource-based policies with CloudWatch RUM

You can attach a resource policy to a CloudWatch RUM app monitor. By default, app monitors do not have a resource policy attached to them. CloudWatch RUM resource based policies do not support cross-account access.

To learn more about AWS resource policies, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html").

To learn more about how resource policies and identity policies are evaluated, see 
 [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html").

To learn more about IAM policy grammar, see [IAM JSON policy element reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html").


## Supported actions


Resource-based policies on app monitors support the `rum:PutRumEvents` action.


## Sample policies to use with CloudWatch RUM


The following example allows anyone to write data to your app monitor, including those without SigV4 credentials.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "rum:PutRumEvents",
 "Resource": "arn:aws:rum:`us-east-1`:`123456789012`:appmonitor/`app monitor name`",
 "Principal": "*"
 }
 ]
}`

```





You can modify the policy to block specified source IP addresses by using the `aws:SourceIp` condition key. With this example, 
 Using this policy, PutRumEvents from the IP address listed will be rejected. All other requests from other IP addresses will be accepted. For 
 more information about this condition key, see [Properties of the network](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-network-properties "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-network-properties")
 in the IAM User Guide.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "rum:PutRumEvents",
 "Resource": "arn:aws:rum:`us-east-1`:`123456789012`:appmonitor/`AppMonitorName`",
 "Principal": "*"
 },
 {
 "Effect": "Deny",
 "Action": "rum:PutRumEvents",
 "Resource": "arn:aws:rum:`us-east-1`:`123456789012`:appmonitor/`AppMonitorName`",
 "Principal": "*",
 "Condition": {
 "NotIpAddress": {
 "aws:SourceIp": "`198.51.100.252`"
 }
 }
 }
 ]
}`

```





Additionally, you can also choose to only accept [PutRumEvents](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumevents.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumevents.html")
 requests that are signed with a certain alias using the `rum:alias` service context key.
 In the following example, `PutRumEvents` will have to set the optional `Alias` request parameter to either `alias1` or `alias2`
 for the event to be accepted. To configure your web client to send `Alias` you must use version 1.20 or later of the CloudWatch RUM web client, as described in 
 
 [Application-specific Configurations](https://github.com/aws-observability/aws-rum-web/blob/main/docs/configuration.md "https://github.com/aws-observability/aws-rum-web/blob/main/docs/configuration.md") on GitHub.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "AllowRUMPutEvents",
 "Effect": "Allow",
 "Action": "rum:PutRumEvents",
 "Resource": "arn:aws:rum:`us-east-1`:`123456789012`:appmonitor/`MyApplication`",
 "Principal": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:rum:`us-east-1`:`123456789012`:appmonitor/`MyApplication`"
 }
 }
 }
 ]
}`

```
