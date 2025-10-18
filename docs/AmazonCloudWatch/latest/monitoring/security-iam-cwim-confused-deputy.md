# Cross-service confused deputy prevention

A confused deputy is an entity (a service or an account) that is coerced by a different entity
 to perform an action. This type of impersonation can happen cross-account and cross-service.

To prevent confused deputies, AWS provides tools that help you protect your data for all 
 services using service principals that have been given access to resources in your AWS account.
 This section focuses on cross-service confused deputy prevention specific to Internet Monitor; however, you
 can learn more about this topic in the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html") section of the 
 *IAM User Guide*.

To limit the permissions that IAM gives to Internet Monitor to access your
 resources, we recommend using the global condition context keys [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn") and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount") in your resource policies. 

If you use both of these global condition context keys, and the `aws:SourceArn`
 value contains the AWS account ID, the `aws:SourceAccount` value 
 and the AWS account in `aws:SourceArn` must use the same 
 AWS account ID when used in the same policy statement.

For Internet Monitor, you specify your account ID for `aws:SourceAccount`
 and your monitor ARN for `aws:SourceArn`. For cross-service access, 
 you also use your monitor ARN for `aws:SourceArn`.

###### Note

The most effective way to protect against the confused deputy problem is to use the
 `aws:SourceArn` global condition context key with the **full ARN** of
 the resource. If you don’t know the full ARN, or if you're specifying multiple resources, use the
 `aws:SourceArn` global context condition key with wildcards (`*`) for the 
 unknown portions of the ARN. For example,
 `arn:aws:internetmonitor:us-east-1:`111122223333`:*`.

The following is an example of an assume role policy that shows how you can prevent 
 a confused deputy issue. 


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "internetmonitor.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:internetmonitor:us-east-1:`111122223333`:monitor/confused-deputy-monitor"
 },
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 }
 }
 }
}`

```
