# Using current IAM user permissions

Use this method if you want to use your current IAM user permissions to
create and run an assessment. You can attach the
`AWSResilienceHubAsssessmentExecutionPolicy` managed policy to
your IAM user or a Role associated with your user.

## Single account setup

Using the managed policy mentioned above is enough to run an assessment on
an application which is managed in the same account as the IAM
user.

## Scheduled assessment setup

You must create a new role
`AwsResilienceHubPeriodicAssessmentRole` to enable AWS Resilience Hub
to perform scheduled assessment related tasks.

###### Note

- While using the role-based access (with the invoker role
  mentioned above) this step is not required.
- The role name must be
  `AwsResilienceHubPeriodicAssessmentRole`.

###### To enable AWS Resilience Hub to perform scheduled assessment related

tasks

1. Attach the `AWSResilienceHubAsssessmentExecutionPolicy`
   managed policy to the role.
2. Add the following policy, where `primary_account_id` is
   the AWS account where the application is defined and will run the
   assessment. In addition, you must add the associated trust policy
   for the scheduled assessment's role,
   (`AwsResilienceHubPeriodicAssessmentRole`), which
   gives permissions for the AWS Resilience Hub service to assume the scheduled
   assessment's role.

**Trust policy for the scheduled assessment's
role
(`AwsResilienceHubPeriodicAssessmentRole`)**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "resiliencehub.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Cross-account setup

The following IAM permissions policies are required if you're using AWS
Resilience Hub with multiple accounts. Each AWS account might need
different permissions depending on your use case. While setting up AWS Resilience Hub
for cross-account access, the following accounts and roles are considered:

- **Primary account** – AWS
  account in which you want to create the application and run
  assessments.
- **Secondary/Resource account(s)**
  – AWS account(s) where the resources are located.

###### Note

- While using the role-based access (with the invoker role
  mentioned above) this step is not required.
- For more information about configuring permissions to access
  Amazon Elastic Kubernetes Service, see [Enabling AWS Resilience Hub access to your Amazon Elastic Kubernetes Service
  cluster](enabling-eks-in-arh.md "enabling-eks-in-arh.md").

### Primary account setup

You must create a new role
`AwsResilienceHubAdminAccountRole` in the primary account
and enable AWS Resilience Hub access to assume it. This role will be used to
access another role in your AWS account that contains your resources.
It should not have permissions to read resources.

###### Note

- The role name must be
  `AwsResilienceHubAdminAccountRole`.
- It must be created in the primary account.
- Your current IAM user/role must have the
  `iam:assumeRole` permission to assume this
  role.
- Replace `secondary_account_id_1/2/...` with the
  relevant secondary account identifiers.

The following policy provides executor permissions to your role for
accessing resources in another role in your AWS account:

The trust policy for the admin role
(`AwsResilienceHubAdminAccountRole`) is as
follows:

### Secondary/Resource account(s) setup

In each of your secondary accounts, you must create a new
`AwsResilienceHubExecutorAccountRole` and enable the
admin role created above to assume this role. Since this role will be
used by AWS Resilience Hub to scan and assess your application resources, it will
also require the appropriate permissions.

However, you must attach the
`AWSResilienceHubAsssessmentExecutionPolicy` managed
policy to the role and attach the executor role policy.

The executor role trust policy is as follows:
