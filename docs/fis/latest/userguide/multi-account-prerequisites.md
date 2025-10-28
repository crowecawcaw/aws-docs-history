# Prerequisites for multi-account experiments

To use stop conditions for a multi-account experiment, you must first configure cross-account alarms.
IAM roles are defined when you create a multi-account experiment template. You can create the necessary IAM roles before you create the template.

###### Content

- [Permissions for multi-account experiments](#permissions "#permissions")
- [Stop conditions for multi-account experiments (optional)](#alarms-and-monitoring "#alarms-and-monitoring")
- [Safety levers for multi-account experiments (optional)](#safety-levers-for-multi-accounts "#safety-levers-for-multi-accounts")

## Permissions for multi-account experiments

Multi-account experiments use IAM _role chaining_ to grant permissions to
AWS FIS to take actions on resources in target accounts. For multi-account experiments, you set up
IAM roles in each target account and the orchestrator account. These IAM roles
require a trust relationship between the target accounts and the orchestrator
account, and between the orchestrator account and AWS FIS.

The IAM roles for the target accounts contain the permissions required to
take action on resources and are created for an experiment template by
adding target account configurations. You will create an IAM role for
the orchestrator account with permission to assume the roles of target accounts
and establish a trust relationship with AWS FIS. This IAM role is used as the `roleArn`
for the experiment template.

To learn more about role chaining, see [Roles Terms and concepts.](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") in IAM's User Guide

In the following example, you will set up permissions for an orchestrator account A to run an experiment with `aws:ebs:pause-volume-io`
in target account B.

1. In account B, create an IAM role with the permissions required to run the action.
   For permissions required for each action, see [AWS FIS Actions reference](fis-actions-reference.md "fis-actions-reference.md").
   The following example shows the permissions a target account grants to run the EBS Pause Volume IO action [aws:ebs:pause-volume-io](fis-actions-reference.md#pause-volume-io "fis-actions-reference.md#pause-volume-io").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVolumes"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:PauseVolumeIO"
 ],
 "Resource": "arn:aws:ec2:us-east-1:123456789012:volume/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "tag:GetResources"
 ],
 "Resource": "*"
 }
 ]
}`

```

2. Next, add a trust policy in account B that creates a trust relationship with account A.
   Choose a name for the IAM role for account A, which you will create in step 3.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "`AccountIdA`"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringLike": {
 "sts:ExternalId": "arn:aws:fis:`region`:`accountIdA`:experiment/*"
 },
 "ArnEquals": {
 "aws:PrincipalArn": "arn:aws:iam::`111122223333`:role/`role_name`"
 }
 }
 }
 ]
}`

```

3. In account A, create an IAM role. This role name must match the role you specified in the trust policy in step 2.
   To target multiple accounts, you grant the orchestrator permissions to assume each role. The following example shows the
   permissions for account A to assume account B. If you have additional target accounts, you will add additional role ARNs to this policy.
   You can only have one role ARN per target account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`role_name`"
 ]
 }
 ]
}`

```

4. This IAM role for account A is used as the `roleArn` for the experiment template.
   The following example shows the trust policy required in the IAM role that grants AWS FIS permissions
   to assume account A, the orchestrator account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "fis.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

You can also use Stacksets to provision multiple IAM roles at one time.
To use CloudFormation StackSets, you will need to set up the necessary StackSet permissions in your AWS accounts.
To learn more, see [Working with AWS CloudFormation StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md").

## Stop conditions for multi-account experiments (optional)

A _stop condition_ is a mechanism to stop an experiment if it reaches a threshold that you define as an alarm. To set up a stop condition
for your multi-account experiment, you can use cross-account alarms. You must enable sharing in each target account to make the alarm
available to the orchestrator account using read-only permissions. Once shared, you can combine metrics from different target accounts using Metric Math.
Then, you can add this alarm as a stop condition for the experiment.

To learn more about cross-account dashboards, see [Enabling cross-account functionality in CloudWatch.](../../../AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.md "../../../AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.md")

## Safety levers for multi-account experiments (optional)

Safety levers are used to stop all running experiments and prevent new experiments from starting.
You may want to use the safety lever to prevent FIS experiments during certain time periods or in response to application health alarms.
Every AWS account has a safety lever per AWS Region. When a safety lever is engaged, it impacts all experiments running in the same account and
region as the safety lever. To stop and prevent multi-account experiments, the safety lever must be engaged in the same account and region where the experiments are running.
