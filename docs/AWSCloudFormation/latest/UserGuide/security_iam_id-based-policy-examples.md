# Example IAM identity-based
 policies for CloudFormation

By default, users and roles don't have permission to create or modify CloudFormation
 resources. They also can't perform tasks by using the AWS Management Console, AWS Command Line Interface (AWS CLI), or
 AWS API. To grant users permission to perform actions on the resources that they need, an
 IAM administrator can create IAM policies. The administrator can then add the IAM
 policies to roles, and users can assume the roles. For more information, see [Defining IAM identity-based policies for
 CloudFormation](control-access-with-iam.md#iam-id-based-policies "control-access-with-iam.md#iam-id-based-policies").

The following examples show policy statements that you could use to allow or deny
 permissions to use one or more CloudFormation actions. 

###### Topics

* [Require a specific template URL](#w71aac43c23c17b9 "#w71aac43c23c17b9")
* [Deny all CloudFormation import operations](#w71aac43c23c17c11 "#w71aac43c23c17c11")
* [Allow import operations for specific resource types](#w71aac43c23c17c13 "#w71aac43c23c17c13")
* [Deny IAM resources in stack templates](#w71aac43c23c17c15 "#w71aac43c23c17c15")
* [Allow stack creation with specific resource types](#w71aac43c23c17c17 "#w71aac43c23c17c17")
* [Control access based on resource-mutating API actions](#w71aac43c23c17c19 "#w71aac43c23c17c19")
* [Restrict stack
 set operations based on Region and resource types](#resource-level-permissions-service-managed-stack-set "#resource-level-permissions-service-managed-stack-set")
* [Allow all IaC generator
 operations](#iam-policy-example-for-iac-generator "#iam-policy-example-for-iac-generator")

## Require a specific template URL


The following policy grants permissions to use only the
 ``https://s3.amazonaws.com/amzn-s3-demo-bucket/test.template``
 template URL to create or update a stack.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:UpdateStack"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudformation:TemplateUrl": [
 "`https://s3.amazonaws.com/amzn-s3-demo-bucket/test.template`"
 ]
 }
 }
 }
 ]
}`

```





## Deny all CloudFormation import operations


The following policy grants permissions to complete all CloudFormation operations except
 import operations.



JSON





```
`{ 
 "Version":"2012-10-17", 
 "Statement": [ 
 { 
 "Sid": "AllowAllStackOperations",
 "Effect": "Allow", 
 "Action": "cloudformation:*", 
 "Resource": "*" 
 }, 
 { 
 "Sid": "DenyImport", 
 "Effect": "Deny", 
 "Action": "cloudformation:*", 
 "Resource": "*",
 "Condition": { 
 "ForAnyValue:StringLike": {
 "cloudformation:ImportResourceTypes": [ 
 "*" 
 ] 
 } 
 } 
 } 
 ] 
}`

```





## Allow import operations for specific resource types


The following policy grants permissions to all stack operations, in addition to
 import operations only on specified resources (in this example,
 `AWS::S3::Bucket`.



JSON





```
`{ 
 "Version":"2012-10-17", 
 "Statement": [ 
 { 
 "Sid": "AllowImport",
 "Effect": "Allow", 
 "Action": "cloudformation:*", 
 "Resource": "*",
 "Condition": { 
 "ForAllValues:StringEqualsIgnoreCase": {
 "cloudformation:ImportResourceTypes": [ 
 "AWS::S3::Bucket" 
 ] 
 } 
 } 
 } 
 ] 
}`

```





## Deny IAM resources in stack templates


The following policy grants permissions to create stacks but denies requests if the
 stack's template include any resource from the IAM service. The policy also requires
 users to specify the `ResourceTypes` parameter, which is available only for
 AWS CLI and API requests. This policy uses explicit deny statements so that if any other
 policy grants additional permissions, this policy always remain in effect (an explicit
 deny statement always overrides an explicit allow statement).



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":[
 {
 "Effect" : "Allow",
 "Action" : [ "cloudformation:CreateStack" ],
 "Resource" : "*"
 },
 {
 "Effect" : "Deny",
 "Action" : [ "cloudformation:CreateStack" ],
 "Resource" : "*",
 "Condition" : {
 "ForAnyValue:StringLikeIfExists" : {
 "cloudformation:ResourceTypes" : [ "AWS::IAM::*" ]
 }
 }
 },
 {
 "Effect": "Deny",
 "Action" : [ "cloudformation:CreateStack" ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "cloudformation:ResourceTypes": "true"
 }
 }
 }
 ]
}`

```





## Allow stack creation with specific resource types


The following policy is similar to the previous example. The policy grants
 permissions to create a stack unless the stack's template includes any resource from the
 IAM service. It also requires users to specify the `ResourceTypes`
 parameter, which is available only for AWS CLI and API requests. This policy is simpler,
 but it doesn't use explicit deny statements. Other policies, granting additional
 permissions, could override this policy.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":[
 {
 "Effect" : "Allow",
 "Action" : [ "cloudformation:CreateStack" ],
 "Resource" : "*",
 "Condition" : {
 "ForAllValues:StringNotLikeIfExists" : {
 "cloudformation:ResourceTypes" : [ "AWS::IAM::*" ]
 },
 "Null":{
 "cloudformation:ResourceTypes": "false"
 }
 }
 }
 ]
}`

```





## Control access based on resource-mutating API actions


The following policy grants permissions to filter access by the name of a
 resource-mutating API action. This is used to control which APIs IAM users can use to
 add or remove tags on a stack or stack set. The operation that is used to add or remove
 tags should be added as value for the condition key. The following policy grants
 `TagResource` and `UntagResource` permissions to mutating
 operation `CreateStack`.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [{
 "Sid": "CreateActionConditionPolicyForTagUntagResources",
 "Effect": "Allow",
 "Action": [
 "cloudformation:TagResource",
 "cloudformation:UntagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudformation:CreateAction": [
 "CreateStack"
 ]
 }
 }
 }]
}`

```





## Restrict stack
 set operations based on Region and resource types


The following policy grants service-managed stack set permissions. A user with this
 policy can only perform operations on stack sets with templates containing Amazon S3 resource
 types (`AWS::S3::*`) or the `AWS::SES::ConfigurationSet` resource
 type. If signed in to the organization management account with ID
 `123456789012`, the user can also only perform operations on stack sets
 that target the OU with ID ``ou-1fsfsrsdsfrewr``,
 and can only perform operations on the stack set with ID `stack-set-id` that
 targets the AWS account with ID
 ``987654321012``.


Stack set operations fail if the stack set template contains resource types other
 than those specified in the policy, or if the deployment targets are OU or account IDs
 other than those specified in the policy for the corresponding management accounts and
 stack sets.


These policy restrictions only apply when stack set operations target the
 `us-east-1`, `us-west-2`, or `eu-west-2`
 AWS Regions.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:*"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:*:stackset/*",
 "arn:aws:cloudformation:*:*:type/resource/`AWS-S3`-*",
 "arn:aws:cloudformation:us-west-2:`111122223333`:type/resource/`AWS-SES-ConfigurationSet`",
 "arn:aws:cloudformation:*:`111122223333`:stackset-target/*/`ou-1fsfsrsdsfrewr`",
 "arn:aws:cloudformation:*:`111122223333`:stackset-target/`stack-set-id`/`444455556666`"
 ],
 "Condition": {
 "ForAllValues:StringEqualsIgnoreCase": {
 "cloudformation:TargetRegion": [
 "`us-east-1`",
 "`us-west-2`",
 "`eu-west-1`"
 ]
 }
 }
 }
 ]
}`

```





## Allow all IaC generator
 operations


The following policy allows access to CloudFormation actions related to IaC generator
 resource scanning and template management. The first statement grants permissions to
 describe, list, and start resource scans. It also allows access to additional required
 permissions (`cloudformation:GetResource`,
 `cloudformation:ListResources`, and `cloudformation:ListTypes`)
 that enable the IaC generator to retrieve information about resources and available
 resource types. The second statement grants full permissions to create, delete,
 describe, list, and update generated templates.


You must also grant read permissions for the target AWS services to anyone who will
 scan resources with IaC generator. For more information, see [IAM permissions required for scanning
 resources](generate-IaC.md#iac-generator-permissions "generate-IaC.md#iac-generator-permissions").



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":[
 {
 "Sid":"ResourceScanningOperations",
 "Effect":"Allow",
 "Action":[
 "cloudformation:DescribeResourceScan",
 "cloudformation:GetResource",
 "cloudformation:ListResources",
 "cloudformation:ListResourceScanRelatedResources",
 "cloudformation:ListResourceScanResources",
 "cloudformation:ListResourceScans",
 "cloudformation:ListTypes",
 "cloudformation:StartResourceScan"
 ],
 "Resource":"*"
 },
 {
 "Sid":"TemplateGeneration",
 "Effect":"Allow",
 "Action":[
 "cloudformation:CreateGeneratedTemplate",
 "cloudformation:DeleteGeneratedTemplate",
 "cloudformation:DescribeGeneratedTemplate",
 "cloudformation:GetResource",
 "cloudformation:GetGeneratedTemplate",
 "cloudformation:ListGeneratedTemplates",
 "cloudformation:UpdateGeneratedTemplate"
 ],
 "Resource":"*"
 }
 ]
}`

```
