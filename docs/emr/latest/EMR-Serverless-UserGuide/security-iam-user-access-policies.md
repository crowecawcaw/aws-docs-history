# User access policy examples for

EMR Serverless

You can set up fine-grained policies for your users depending on the actions you want each
user to perform when interacting with EMR Serverless applications. The following policies are
examples that might help in setting up the appropriate permissions for your users. This section
focuses only on EMR Serverless policies. For samples of EMR Studio user policies, refer to
[Configure EMR Studio user permissions](../ManagementGuide/emr-studio-user-permissions.md#emr-studio-advanced-permissions-policy "../ManagementGuide/emr-studio-user-permissions.md#emr-studio-advanced-permissions-policy"). For information about how to attach
policies to IAM users (principals), refer to [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-using.md "../../../IAM/latest/UserGuide/access_policies_managed-using.md")
in the IAM User Guide.

## Power user policy

To grant all the required actions for EMR Serverless, create and attach a
`AmazonEMRServerlessFullAccess` policy to the required IAM user, role, or
group.

The following is a sample policy that allows power users to create and modify
EMR Serverless applications, as well as perform other actions like submitting and debugging
jobs. It reveals all the actions that EMR Serverless requires for other services.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EMRServerlessActions",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:CreateApplication",
 "emr-serverless:UpdateApplication",
 "emr-serverless:DeleteApplication",
 "emr-serverless:ListApplications",
 "emr-serverless:GetApplication",
 "emr-serverless:StartApplication",
 "emr-serverless:StopApplication",
 "emr-serverless:StartJobRun",
 "emr-serverless:CancelJobRun",
 "emr-serverless:ListJobRuns",
 "emr-serverless:GetJobRun"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

When you enable network connectivity to your VPC, EMR Serverless applications create
Amazon EC2 elastic network interfaces (ENIs) to communicate with VPC resources. The following
policy ensures that any new EC2 ENIs are only created in the context of EMR Serverless
applications.

###### Note

We strongly recommend setting this policy to ensure that users cannot create EC2 ENIs
except in the context of launching EMR Serverless applications.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEC2ENICreationWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "ops.emr-serverless.amazonaws.com"
 }
 }
 }
 ]
}`

```

If you want to restrict EMR Serverless access to certain subnets, you can tag each
subnet with a tag condition. This IAM policy ensures that EMR Serverless applications can
only create EC2 ENIs within allowed subnets.

```
{
    "Sid": "AllowEC2ENICreationInSubnetAndSecurityGroupWithEMRTags",
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterface"
    ],
    "Resource": [
        "arn:aws:ec2:*:*:subnet/*",
        "arn:aws:ec2:*:*:security-group/*"
    ],
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/`KEY`": "`VALUE`"
        }
    }
}
```

###### Important

If you’re an Administrator or power user creating your first application, you must
configure your permission policies to allow you to create a EMR Serverless service-linked
role. To learn more, refer to [Using service-linked roles for
EMR Serverless](using-service-linked-roles.md "using-service-linked-roles.md").

The following IAM policy permits you to create a EMR Serverless service-linked role
for your account.

```
{
   "Sid":"AllowEMRServerlessServiceLinkedRoleCreation",
   "Effect":"Allow",
   "Action":"iam:CreateServiceLinkedRole",
   "Resource":"arn:aws:iam::`account-id`:role/aws-service-role/ops.emr-serverless.amazonaws.com/AWSServiceRoleForAmazonEMRServerless"
}
```

## Data engineer

policy

This following is a sample policy that allows users read-only permissions on
EMR Serverless applications, as well as the ability to submit and debug jobs. Keep in
mind that because this policy does not explicitly deny actions, a different policy statement
may still be used to grant access to specified actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EMRServerlessActions",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:ListApplications",
 "emr-serverless:GetApplication",
 "emr-serverless:StartApplication",
 "emr-serverless:StartJobRun",
 "emr-serverless:CancelJobRun",
 "emr-serverless:ListJobRuns",
 "emr-serverless:GetJobRun"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Using tags for access

control

You can use tag conditions for fine-grained access control. For example, you can
restrict users from one team such that they’re only able to submit jobs to EMR Serverless
applications tagged with their team name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EMRServerlessActions",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:ListApplications",
 "emr-serverless:GetApplication",
 "emr-serverless:StartApplication",
 "emr-serverless:StartJobRun",
 "emr-serverless:CancelJobRun",
 "emr-serverless:ListJobRuns",
 "emr-serverless:GetJobRun"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
