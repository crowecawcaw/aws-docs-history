# Prerequisites for syncing stacks to a Git repository using
 Git sync

Before you sync a CloudFormation stack to your Git repository, verify that the following
 requirements are met.

###### Topics

* [Git repository](#git-sync-prereq-repo "#git-sync-prereq-repo")
* [CloudFormation template](#git-sync-prereq-template "#git-sync-prereq-template")
* [Git sync service role](#git-sync-prereq-iam "#git-sync-prereq-iam")
* [IAM permissions for console
 users](#git-sync-prereq-user-permissions "#git-sync-prereq-user-permissions")

## Git repository


You must have a Git repository hosted on one of the following platforms.



* [GitHub](https://github.com/ "https://github.com/")
* [GitHub Enterprise](https://github.com/enterprise "https://github.com/enterprise")
* [GitLab](https://about.gitlab.com/ "https://about.gitlab.com/")
* [Bitbucket](https://bitbucket.org "https://bitbucket.org")
* [GitLab
 self-managed](https://docs.gitlab.com/subscriptions/self_managed/ "https://docs.gitlab.com/subscriptions/self_managed/")

The repository can be either public or private. You will need to connect this Git
 repository to CloudFormation though the [Connections console](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections").


## CloudFormation template


Your Git repository must contain a [CloudFormation template file](git-sync-concepts-terms.md#git-sync-concepts-terms-template-file "git-sync-concepts-terms.md#git-sync-concepts-terms-template-file")
 checked into the branch you intend to connect with Git sync. This template will be
 referenced by the [stack
 deployment file](git-sync-concepts-terms.md#git-sync-concepts-terms-depoyment-file "git-sync-concepts-terms.md#git-sync-concepts-terms-depoyment-file").


## Git sync service role


Git sync requires an IAM role. You can choose to have an IAM role created for
 your stack when you configure Git sync, or you can use an existing role.


###### Note

An automatically generated IAM role only applies permissions to the stack for
 which the role is generated. To reuse an automatically generated IAM role, you
 must edit the role for the new stack.


### Required permissions for Git sync
 service role


The IAM role that you provide for Git sync requires the following
 permissions.



* `cloudformation:CreateChangeSet`
* `cloudformation:DeleteChangeSet`
* `cloudformation:DescribeChangeSet`
* `cloudformation:DescribeStackEvents`
* `cloudformation:DescribeStacks`
* `cloudformation:ExecuteChangeSet`
* `cloudformation:ListChangeSets`
* `cloudformation:ValidateTemplate`
* `events:PutRule`
* `events:PutTargets`

###### Note

The preceding required permissions are automatically added to IAM roles that
 Git sync generates.


The following example IAM role includes the prerequisite permissions for
 Git sync.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "SyncToCloudFormation",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateChangeSet",
 "cloudformation:DeleteChangeSet",
 "cloudformation:DescribeChangeSet",
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeStacks",
 "cloudformation:ExecuteChangeSet",
 "cloudformation:GetTemplate",
 "cloudformation:ListChangeSets",
 "cloudformation:ListStacks",
 "cloudformation:ValidateTemplate"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PolicyForManagedRules",
 "Effect": "Allow",
 "Action": [
 "events:PutRule",
 "events:PutTargets"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "events:ManagedBy": ["cloudformation.sync.codeconnections.amazonaws.com"]
 }
 }
 },
 {
 "Sid": "PolicyForDescribingRule",
 "Effect": "Allow",
 "Action": "events:DescribeRule",
 "Resource": "*"
 }
 ]
}`

```





#### Trust policy


You must provide the following trust policy when you create the role to define
 the trust relationship.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "CfnGitSyncTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudformation.sync.codeconnections.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```





We recommend that you use the `aws:SourceArn` and
 `aws:SourceAccount` condition keys to protect yourself against the
 confused deputy problem. The source account is your account ID and the source ARN is the
 ARN of the connection in the [CodeConnections](https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html") service that
 allows CloudFormation to connect to your Git repository.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "CfnGitSyncTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudformation.sync.codeconnections.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "`arn:aws:codeconnections:us-east-1:123456789012:connection/EXAMPLE64-8aad-4d5d-8878-dfcab0bc441f`"
 }
 }
 }
 ]
}`

```





For more information about the confused deputy problem, see [Cross-service confused deputy
 prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").


## IAM permissions for console
 users


To successfully set up Git sync through the CloudFormation console, end users must also
 be granted permissions through IAM.


The following `codeconnections` permissions are required to create and
 manage the connection to your Git repository.



* `codeconnections:CreateRepositoryLink`
* `codeconnections:CreateSyncConfiguration`
* `codeconnections:DeleteRepositoryLink`
* `codeconnections:DeleteSyncConfiguration`
* `codeconnections:GetRepositoryLink`
* `codeconnections:GetSyncConfiguration`
* `codeconnections:ListRepositoryLinks`
* `codeconnections:ListSyncConfigurations`
* `codeconnections:ListTagsForResource`
* `codeconnections:TagResource`
* `codeconnections:UntagResource`
* `codeconnections:UpdateRepositoryLink`
* `codeconnections:UpdateSyncBlocker`
* `codeconnections:UpdateSyncConfiguration`
* `codeconnections:UseConnection`

Console users must also have the following `cloudformation` permissions to
 view and manage stacks during the Git sync setup process.



* `cloudformation:CreateChangeSet`
* `cloudformation:DeleteChangeSet`
* `cloudformation:DescribeChangeSet`
* `cloudformation:DescribeStackEvents`
* `cloudformation:DescribeStacks`
* `cloudformation:ExecuteChangeSet`
* `cloudformation:GetTemplate`
* `cloudformation:ListChangeSets`
* `cloudformation:ListStacks`
* `cloudformation:ValidateTemplate`

###### Note

While change set permissions (`cloudformation:CreateChangeSet`,
 `cloudformation:DeleteChangeSet`,
 `cloudformation:DescribeChangeSet`,
 `cloudformation:ExecuteChangeSet`) might not be strictly required for
 console-only usage, they're recommended to enable full stack inspection and
 management capabilities.


The following example IAM policy includes the user permissions needed to set up
 Git sync through the console.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "CodeConnectionsPermissions",
 "Effect": "Allow",
 "Action": [
 "codeconnections:CreateRepositoryLink",
 "codeconnections:CreateSyncConfiguration",
 "codeconnections:DeleteRepositoryLink",
 "codeconnections:DeleteSyncConfiguration",
 "codeconnections:GetRepositoryLink",
 "codeconnections:GetSyncConfiguration",
 "codeconnections:ListRepositoryLinks",
 "codeconnections:ListSyncConfigurations",
 "codeconnections:ListTagsForResource",
 "codeconnections:TagResource",
 "codeconnections:UntagResource",
 "codeconnections:UpdateRepositoryLink",
 "codeconnections:UpdateSyncBlocker",
 "codeconnections:UpdateSyncConfiguration",
 "codeconnections:UseConnection",
 "codeconnections:CreateForcedTargetSync",
 "codeconnections:CreatePullRequestForResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudFormationConsolePermissions",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateChangeSet",
 "cloudformation:DeleteChangeSet",
 "cloudformation:DescribeChangeSet",
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeStacks",
 "cloudformation:ExecuteChangeSet",
 "cloudformation:GetTemplate",
 "cloudformation:ListChangeSets",
 "cloudformation:ListStacks",
 "cloudformation:ValidateTemplate"
 ],
 "Resource": "*"
 }
 ]
}`

```





###### Note

When creating an IAM policy that includes the permissions
 `codeconnections:CreateForcedTargetSync` and
 `codeconnections:CreatePullRequestForResource`, you might see a
 warning in the IAM console stating that these actions do not exist. This warning
 can be ignored, and the policy will still be created successfully. These
 permissions are required for certain Git sync operations despite not being
 recognized by the IAM console.
