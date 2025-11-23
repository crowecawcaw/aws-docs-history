# Customer managed policy examples

You can create your own custom IAM policies to allow permissions for
CodeCommit actions and resources. You can attach these custom policies to the
IAM users or groups that require those permissions. You can also create your own
custom IAM policies for integration between CodeCommit and other AWS services.

###### Topics

- [Customer managed identity
  policy examples](#customer-managed-policies-identity "#customer-managed-policies-identity")

## Customer managed identity

policy examples

The following example IAM policies grant permissions for various
CodeCommit actions. Use them to limit CodeCommit access for your IAM
users and roles. These policies control the ability to perform actions with the
CodeCommit console, API, AWS SDKs, or the AWS CLI.

###### Note

All examples use the US West (Oregon) Region (us-west-2) and contain fictitious
account IDs.

**Examples**

- [Example 1: Allow a user
  to perform CodeCommit operations in a single AWS Region](#identity-based-policies-example-1 "#identity-based-policies-example-1")
- [Example 2: Allow a user
  to use Git for a single repository](#identity-based-policies-example-2 "#identity-based-policies-example-2")
- [Example 3: Allow a user
  connecting from a specified IP address range access to a repository](#identity-based-policies-example-3 "#identity-based-policies-example-3")
- [Example 4: Deny or allow
  actions on branches](#identity-based-policies-example-4 "#identity-based-policies-example-4")
- [Example 5: Deny or allow
  actions on repositories with tags](#identity-based-policies-example-5 "#identity-based-policies-example-5")

### Example 1: Allow a user

to perform CodeCommit operations in a single AWS Region

The following permissions policy uses a wildcard character
(`"codecommit:*"`) to allow users to perform all CodeCommit
actions in the us-east-2 Region and not from other AWS Regions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codecommit:*",
 "Resource": "arn:aws:codecommit:us-east-2:111111111111:*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-east-2"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "codecommit:ListRepositories",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-east-2"
 }
 }
 }
 ]
}`

```

### Example 2: Allow a user

to use Git for a single repository

In CodeCommit, the `GitPull` IAM policy permissions apply to any
Git client command where data is retrieved from CodeCommit, including
**git fetch**, **git clone**, and so on.
Similarly, the `GitPush` IAM policy permissions apply to any
Git client command where data is sent to CodeCommit. For example, if the
`GitPush` IAM policy permission is set to
`Allow`, a user can push the deletion of a branch using the
Git protocol. That push is unaffected by any permissions applied to the
`DeleteBranch` operation for that IAM user. The
`DeleteBranch` permission applies to actions performed with
the console, the AWS CLI, the SDKs, and the API, but not the Git protocol.

The following example allows the specified user to pull from, and push to,
the CodeCommit repository named `MyDemoRepo`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "codecommit:GitPull",
 "codecommit:GitPush"
 ],
 "Resource" : "arn:aws:codecommit:us-east-2:`111122223333`:MyDemoRepo"
 }
 ]
}`

```

### Example 3: Allow a user

connecting from a specified IP address range access to a repository

You can create a policy that only allows users to connect to a CodeCommit
repository if their IP address is within a certain IP address range. There
are two equally valid approaches to this. You can create a `Deny`
policy that disallows CodeCommit operations if the IP address for the user is not
within a specific block, or you can create an `Allow` policy that
allows CodeCommit operations if the IP address for the user is within a specific
block.

You can create a `Deny` policy that denies access to all users
who are not within a certain IP range. For example, you could attach the
AWSCodeCommitPowerUser managed policy and a customer-managed policy to all users
who require access to your repository. The following example policy denies
all CodeCommit permissions to users whose IP addresses are not within the
specified IP address block of 203.0.113.0/16:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "codecommit:*"
 ],
 "Resource": "*",
 "Condition": {
 "NotIpAddress": {
 "aws:SourceIp": [
 "203.0.113.0/16"
 ]
 }
 }
 }
 ]
}`

```

The following example policy allows the specified user to access a CodeCommit
repository named MyDemoRepo with the equivalent permissions of the
AWSCodeCommitPowerUser managed policy only if their IP address is within the
specified address block of 203.0.113.0/16:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:BatchGetRepositories",
 "codecommit:CreateBranch",
 "codecommit:CreateRepository",
 "codecommit:Get*",
 "codecommit:GitPull",
 "codecommit:GitPush",
 "codecommit:List*",
 "codecommit:Put*",
 "codecommit:Post*",
 "codecommit:Merge*",
 "codecommit:TagResource",
 "codecommit:Test*",
 "codecommit:UntagResource",
 "codecommit:Update*"
 ],
 "Resource": "arn:aws:codecommit:us-east-2:`111122223333`:MyDemoRepo",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "203.0.113.0/16"
 ]
 }
 }
 }
 ]
}`

```

### Example 4: Deny or allow

actions on branches

You can create a policy that denies users permissions to actions you
specify on one or more branches. Alternatively, you can create a policy that
allows actions on one or more branches that they might not otherwise have in
other branches of a repository. You can use these policies with the
appropriate managed (predefined) policies. For more information, see [Limit pushes and merges to branches in AWS CodeCommit](how-to-conditional-branch.md "how-to-conditional-branch.md").

For example, you can create a `Deny` policy that denies users
the ability to make changes to a branch named main, including deleting that
branch, in a repository named
`MyDemoRepo`. You can use this policy
with the **AWSCodeCommitPowerUser** managed policy. Users with
these two policies applied would be able to create and delete branches,
create pull requests, and all other actions as allowed by
**AWSCodeCommitPowerUser**, but they would not be able to
push changes to the branch named _main_,
add or edit a file in the _main_ branch in
the CodeCommit console, or merge branches or a pull request into the _main_ branch. Because `Deny` is
applied to `GitPush`, you must include a `Null`
statement in the policy, to allow initial `GitPush` calls to be
analyzed for validity when users make pushes from their local repos.

###### Tip

If you want to create a policy that applies to all branches named
_main_ in all repositories in your
Amazon Web Services account, for `Resource`, specify an asterisk (
`*` ) instead of a repository ARN.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "codecommit:GitPush",
 "codecommit:DeleteBranch",
 "codecommit:PutFile",
 "codecommit:Merge*"
 ],
 "Resource": "arn:aws:codecommit:us-east-2:111111111111:MyDemoRepo",
 "Condition": {
 "StringEqualsIfExists": {
 "codecommit:References": [
 "refs/heads/main"
 ]
 },
 "Null": {
 "codecommit:References": "false"
 }
 }
 }
 ]
}`

```

The following example policy allows a user to make changes to a branch
named main in all repositories in an Amazon Web Services account. It does not allow
changes to any other branches. You might use this policy with the
AWSCodeCommitReadOnly managed policy to allow automated pushes to the
repository in the main branch. Because the Effect is `Allow`,
this example policy would not work with managed policies such as
AWSCodeCommitPowerUser.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:GitPush",
 "codecommit:Merge*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEqualsIfExists": {
 "codecommit:References": [
 "refs/heads/main"
 ]
 }
 }
 }
 ]
}`

```

### Example 5: Deny or allow

actions on repositories with tags

You can create a policy that allows or denies actions on repositories
based on the AWS tags associated with those repositories, and then apply
those policies to the IAM groups you configure for managing IAM users.
For example, you can create a policy that denies all CodeCommit actions on any
repositories with the AWS tag key _Status_ and the key value of _Secret_, and then apply that policy to the IAM group you
created for general developers (`Developers`). You
then need to make sure that the developers working on those tagged
repositories are not members of that general
`Developers` group, but belong instead to a
different IAM group that does not have the restrictive policy applied
(_SecretDevelopers_).

The following example denies all CodeCommit actions on repositories tagged with
the key _Status_ and the key value of
_Secret_:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "codecommit:Associate*",
 "codecommit:Batch*",
 "codecommit:CancelUploadArchive",
 "codecommit:CreateBranch",
 "codecommit:CreateCommit",
 "codecommit:CreatePullRequest*",
 "codecommit:CreateRepository",
 "codecommit:CreateUnreferencedMergeCommit",
 "codecommit:DeleteBranch",
 "codecommit:DeleteCommentContent",
 "codecommit:DeleteFile",
 "codecommit:DeletePullRequest*",
 "codecommit:DeleteRepository",
 "codecommit:Describe*",
 "codecommit:DisassociateApprovalRuleTemplateFromRepository",
 "codecommit:EvaluatePullRequestApprovalRules",
 "codecommit:GetBlob",
 "codecommit:GetBranch",
 "codecommit:GetComment*",
 "codecommit:GetCommit",
 "codecommit:GetDifferences*",
 "codecommit:GetFile",
 "codecommit:GetFolder",
 "codecommit:GetMerge*",
 "codecommit:GetObjectIdentifier",
 "codecommit:GetPullRequest*",
 "codecommit:GetReferences",
 "codecommit:GetRepository*",
 "codecommit:GetTree",
 "codecommit:GetUploadArchiveStatus",
 "codecommit:Git*",
 "codecommit:ListAssociatedApprovalRuleTemplatesForRepository",
 "codecommit:ListBranches",
 "codecommit:ListPullRequests",
 "codecommit:ListTagsForResource",
 "codecommit:Merge*",
 "codecommit:OverridePullRequestApprovalRules",
 "codecommit:Post*",
 "codecommit:Put*",
 "codecommit:TagResource",
 "codecommit:TestRepositoryTriggers",
 "codecommit:UntagResource",
 "codecommit:UpdateComment",
 "codecommit:UpdateDefaultBranch",
 "codecommit:UpdatePullRequest*",
 "codecommit:UpdateRepository*",
 "codecommit:UploadArchive"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Status": "Secret"
 }
 }
 }
 ]
}`

```

You can further refine this strategy by specifying specific repositories,
rather than all repositories, as resources. You can also create policies
that allow CodeCommit actions on all repositories that are not tagged with
specific tags. For example, the following policy allows the equivalent of
**AWSCodeCommitPowerUser**
permissions
for CodeCommit actions, except that it
only
allows CodeCommit actions on repositories not tagged with the
specified tags:

###### Note

This policy example only includes actions for CodeCommit. It does not
include actions for other AWS services that are included in the
**AWSCodeCommitPowerUser** managed policy.
For more information, see .[AWS managed policy: AWSCodeCommitPowerUser](security-iam-awsmanpol.md#managed-policies-poweruser "security-iam-awsmanpol.md#managed-policies-poweruser").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:Associate*",
 "codecommit:Batch*",
 "codecommit:CancelUploadArchive",
 "codecommit:CreateBranch",
 "codecommit:CreateCommit",
 "codecommit:CreatePullRequest*",
 "codecommit:CreateRepository",
 "codecommit:CreateUnreferencedMergeCommit",
 "codecommit:DeleteBranch",
 "codecommit:DeleteCommentContent",
 "codecommit:DeleteFile",
 "codecommit:DeletePullRequest*",
 "codecommit:Describe*",
 "codecommit:DisassociateApprovalRuleTemplateFromRepository",
 "codecommit:EvaluatePullRequestApprovalRules",
 "codecommit:GetBlob",
 "codecommit:GetBranch",
 "codecommit:GetComment*",
 "codecommit:GetCommit",
 "codecommit:GetDifferences*",
 "codecommit:GetFile",
 "codecommit:GetFolder",
 "codecommit:GetMerge*",
 "codecommit:GetObjectIdentifier",
 "codecommit:GetPullRequest*",
 "codecommit:GetReferences",
 "codecommit:GetRepository*",
 "codecommit:GetTree",
 "codecommit:GetUploadArchiveStatus",
 "codecommit:Git*",
 "codecommit:ListAssociatedApprovalRuleTemplatesForRepository",
 "codecommit:ListBranches",
 "codecommit:ListPullRequests",
 "codecommit:ListTagsForResource",
 "codecommit:Merge*",
 "codecommit:OverridePullRequestApprovalRules",
 "codecommit:Post*",
 "codecommit:Put*",
 "codecommit:TagResource",
 "codecommit:TestRepositoryTriggers",
 "codecommit:UntagResource",
 "codecommit:UpdateComment",
 "codecommit:UpdateDefaultBranch",
 "codecommit:UpdatePullRequest*",
 "codecommit:UpdateRepository*",
 "codecommit:UploadArchive"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:ResourceTag/Status": "Secret",
 "aws:ResourceTag/Team": "Saanvi"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:CreateApprovalRuleTemplate",
 "codecommit:GetApprovalRuleTemplate",
 "codecommit:ListApprovalRuleTemplates",
 "codecommit:ListRepositories",
 "codecommit:ListRepositoriesForApprovalRuleTemplate",
 "codecommit:UpdateApprovalRuleTemplateContent",
 "codecommit:UpdateApprovalRuleTemplateDescription",
 "codecommit:UpdateApprovalRuleTemplateName"
 ],
 "Resource": "*"
 }
 ]
}`

```
