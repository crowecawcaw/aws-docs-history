• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Cross-service

confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't
have permission to perform an action can coerce a more-privileged entity to
perform the action. In AWS, cross-service impersonation can result in the
confused deputy problem. Cross-service impersonation can occur when one service
(the _calling service_) calls another service (the
_called service_). The calling service can be manipulated
to use its permissions to act on another customer's resources in a way it should
not otherwise have permission to access. To prevent this, AWS provides tools
that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in
resource policies to limit the permissions that AWS Systems Manager gives another
service to the resource. If the `aws:SourceArn` value does not
contain the account ID, such as an Amazon Resource Name (ARN) for an S3 bucket,
you must use both global condition context keys to limit permissions. If you use
both global condition context keys and the `aws:SourceArn` value
contains the account ID, the `aws:SourceAccount` value and the
account in the `aws:SourceArn` value must use the same account ID
when used in the same policy statement. Use `aws:SourceArn` if you
want only one resource to be associated with the cross-service access. Use
`aws:SourceAccount` if you want to allow any resource in that
account to be associated with the cross-service use.

The following sections provide example policies for AWS Systems Manager
tools.

## Hybrid

activation policy example

For service roles used in a [hybrid
activation](activations.md "activations.md"), the value of `aws:SourceArn` must be the
ARN of the AWS account. Be sure to specify the AWS Region in the ARN
where you created your hybrid activation. If you don't know the full ARN of
the resource or if you're specifying multiple resources, use the
`aws:SourceArn` global context condition key with wildcards
(`*`) for the unknown portions of the ARN. For example,
`arn:aws:ssm:*:`region`:`123456789012`:*`.

The following example demonstrates using the `aws:SourceArn`
and `aws:SourceAccount` global condition context keys for
Automation to prevent the confused deputy problem in the
US East (Ohio) Region (us-east-2).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"",
 "Effect":"Allow",
 "Principal":{
 "Service":"ssm.amazonaws.com"
 },
 "Action":"sts:AssumeRole",
 "Condition":{
 "StringEquals":{
 "aws:SourceAccount":"`123456789012`"
 },
 "ArnEquals":{
 "aws:SourceArn":"arn:aws:ssm:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

## Resource data

sync policy example

Systems Manager Inventory, Explorer, and Compliance enable you to create a resource
data sync to centralize storage of your operations data (OpsData) in a
central Amazon Simple Storage Service bucket. If you want to encrypt a resource data sync by
using AWS Key Management Service (AWS KMS), then you must either create a new key that includes
the following policy, or you must update an existing key and add this policy
to it. The `aws:SourceArn` and `aws:SourceAccount`
condition keys in this policy prevent the confused deputy problem. Here is
an example policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "ssm-access-policy",
 "Statement": [
 {
 "Sid": "ssm-access-policy-statement",
 "Action": [
 "kms:GenerateDataKey"
 ],
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`KMS_key_id`",
 "Condition": {
 "StringLike": {
 "aws:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ssm:*:`123456789012`:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM"
 }
 }
 }
 ]
}`

```

###### Note

The ARN in the policy example enables the system to encrypt OpsData
from all sources except AWS Security Hub CSPM. If you need to encrypt Security Hub CSPM data,
for example if you use Explorer to collect Security Hub CSPM data, then you must
attach an additional policy that specifies the following ARN:

`"aws:SourceArn":
 "arn:aws:ssm:*:`account-id`:role/aws-service-role/opsdatasync.ssm.amazonaws.com/AWSServiceRoleForSystemsManagerOpsDataSync"`
