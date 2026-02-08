# Using tags to control access to Elastic Beanstalk resources

This topic explains how tag-based access control can help you create and manage IAM policies.

We can use conditions in IAM user policy statements to configure permissions for Elastic Beanstalk's access to resources. To learn more about policy statement
conditions, see [Resources and conditions for Elastic Beanstalk actions](AWSHowTo.iam.policies.md "AWSHowTo.iam.policies.md"). Using tags in conditions is one way to
control access to resources and requests. For information about tagging Elastic Beanstalk resources, see [Tagging Elastic Beanstalk application resources](applications-tagging-resources.md "applications-tagging-resources.md").

When you design IAM policies, you might be setting granular permissions by granting access to specific resources. As the number of resources that you
manage grows, this task becomes more difficult. Tagging resources and using tags in policy statement conditions can make this task easier. You grant access
in bulk to any resource with a certain tag. Then you repeatedly apply this tag to relevant resources, during creation or later.

Tags can be attached to the resource or passed in the request to services that support tagging. In Elastic Beanstalk, resources can have tags, and some actions can
include tags. When you create an IAM policy, you can use tag condition keys to control the following conditions:

- Which users can perform actions on an environment, based on tags that it already has.
- What tags can be passed in an action's request.
- Whether specific tag keys can be used in a request.
  For the complete syntax and semantics of tag condition keys, see [Controlling Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in
  the _IAM User Guide_.

## Examples of tag conditions in policies

The following examples demonstrate how to specify tag conditions in policies for Elastic Beanstalk users.

###### Example 1: Limit actions based on tags in the request

The Elastic Beanstalk **AdministratorAccess-AWSElasticBeanstalk** managed user policy gives users unlimited permission to perform any Elastic Beanstalk
action on any Elastic Beanstalk-managed resource.

The following policy limits this power and denies unauthorized users permission to create Elastic Beanstalk production environments. To do that, it denies the
`CreateEnvironment` action if the request specifies a tag named `stage` with one of the values `gamma` or
`prod`. In addition, the policy prevents these unauthorized users from tampering with the stage of production environments by not allowing
tag modification actions to include these same tag values or to completely remove the `stage` tag. A customer's administrator must attach this
IAM policy to unauthorized IAM users, in addition to the managed user policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "elasticbeanstalk:CreateEnvironment",
 "elasticbeanstalk:AddTags"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/stage": ["gamma", "prod"]
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "elasticbeanstalk:RemoveTags"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": ["stage"]
 }
 }
 }
 ]
}`

```

###### Example 2: Limit actions based on resource tags

The Elastic Beanstalk **AdministratorAccess-AWSElasticBeanstalk** managed user policy gives users unlimited permission to perform any Elastic Beanstalk
action on any Elastic Beanstalk-managed resource.

The following policy limits this power and denies unauthorized users permission to perform actions on Elastic Beanstalk production environments. To do that, it
denies specific actions if the environment has a tag named `stage` with one of the values `gamma` or `prod`. A customer's
administrator must attach this IAM policy to unauthorized IAM users, in addition to the managed user policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "elasticbeanstalk:AddTags",
 "elasticbeanstalk:RemoveTags",
 "elasticbeanstalk:DescribeEnvironments",
 "elasticbeanstalk:TerminateEnvironment",
 "elasticbeanstalk:UpdateEnvironment",
 "elasticbeanstalk:ListTagsForResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/stage": ["gamma", "prod"]
 }
 }
 }
 ]
}`

```

###### Example 3: Allow actions based on tags in the request

The following policy grants users permission to create Elastic Beanstalk development applications.

To do that, it allows the `CreateApplication`and `AddTags` actions if the request specifies a tag named `stage` with
the value `development`. The `aws:TagKeys` condition ensures that the user can't add other tag keys. In particular, it ensures case
sensitivity of the `stage` tag key. Notice that this policy is useful for IAM
users that don't have the Elastic Beanstalk **AdministratorAccess-AWSElasticBeanstalk** managed user policy attached. The managed policy gives
users unlimited permission to perform any Elastic Beanstalk action on any Elastic Beanstalk-managed resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticbeanstalk:CreateApplication",
 "elasticbeanstalk:AddTags"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/stage": "development"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": ["stage"]
 }
 }
 }
 ]
}`

```

###### Example 4: Allow actions based on resource tags

The following policy grants users permission to perform actions on, and get information about, Elastic Beanstalk development applications.

To do that, it allows specific actions if the application has a tag named `stage` with the value `development`. The
`aws:TagKeys` condition ensures that the user can't add other tag keys. In particular, it ensures case
sensitivity of the `stage` tag key. Notice that this policy is useful for IAM users that don't have the Elastic Beanstalk
**AdministratorAccess-AWSElasticBeanstalk** managed user policy attached. The managed policy gives users unlimited permission to
perform any Elastic Beanstalk action on any Elastic Beanstalk-managed resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticbeanstalk:UpdateApplication",
 "elasticbeanstalk:DeleteApplication",
 "elasticbeanstalk:DescribeApplications"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/stage": "development"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": ["stage"]
 }
 }
 }
 ]
}`

```
