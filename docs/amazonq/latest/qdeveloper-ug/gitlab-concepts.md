# GitLab Duo concepts

Here are some concepts and terms to know when using
[GitLab Duo with Amazon Q](https://docs.gitlab.com/ee/user/duo_amazon_q/ "https://docs.gitlab.com/ee/user/duo_amazon_q/").

###### Topics

- [Setting up GitLab Duo with Amazon Q](#gitlab-concepts-set-up "#gitlab-concepts-set-up")
- [Onboarding with AWS resources and permission
  policies](#gitlab-concepts-onboarding "#gitlab-concepts-onboarding")
- [GitLab quick actions](#gitlab-concepts-quick-actions "#gitlab-concepts-quick-actions")

## Setting up GitLab Duo with Amazon Q

Before you can use Amazon Q artificial intelligence (AI) capabilities in GitLab Duo, you need
to complete the prerequisites and create AWS resources. For more information, see
[Set up GitLab Duo with
Amazon Q](https://docs.gitlab.com/ee/user/duo_amazon_q/setup.html "https://docs.gitlab.com/ee/user/duo_amazon_q/setup.html") in the _GitLab documentation_.

## Onboarding with AWS resources and permission

policies

As part of the GitLab Duo onboarding process, you need to create an Amazon Q Developer profile through the
[Amazon Q Developer console](https://console.aws.amazon.com/amazonq/developer/home "https://console.aws.amazon.com/amazonq/developer/home"). The
profile allows you to create customization and control settings for all or a subset of users in
your identity provider. After creating a profile,
you need an OpenID Connect (OIDC) identity provider (IdP), as well as an IAM service role, to establish
trust between GitLab Duo and your AWS account. To learn how to create the required resources and set up
GitLab Duo with Amazon Q, see [Set up
GitLab Duo with Amazon Q](https://docs.gitlab.com/ee/user/duo_amazon_q/setup.html "https://docs.gitlab.com/ee/user/duo_amazon_q/setup.html") in the _GitLab documentation_.

When the new IAM role is created, the required trust policy with the necessary permissions is
also created. A role trust policy is a required
[resource-based
policy](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based") that is attached to a role in IAM.

You need to add a permissions policy, which grants ability to connect with Amazon Q and
utilize the features in the GitLab Duo with Amazon Q integration. The policy must be added when creating
the IAM role. To learn more about the permissions provided by the
permissions policy, see [GitLabDuoWithAmazonQPermissionsPolicy](managed-policy.md#amazonq-policy-GitLabDuoWithAmazonQPermissionsPolicy "managed-policy.md#amazonq-policy-GitLabDuoWithAmazonQPermissionsPolicy").

Alternatively, you can create an inline policy and add the required permissions. You can choose
to create an inline policy if you want to custom access control. For more information, see
[Managed
policies and inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") and [Policies and permissions in AWS
Identity and Access Management](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

**Trust policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRoleWithWebIdentity",
 "Principal": {
 "Federated": "arn:aws:iam::`111122223333`:oidc-provider/auth.token.gitlab.com/cc/oidc/`instance-id`"
 },
 "Condition": {
 "StringEquals": {
 "auth.token.gitlab.com/cc/oidc/`instance-id`:aud": "gitlab-cc-`instance-id`"
 }
 }
 }
 ]
}`

```

**Permissions policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GitLabDuoUsagePermissions",
 "Effect": "Allow",
 "Action": [
 "q:SendEvent",
 "q:CreateAuthGrant",
 "q:UpdateAuthGrant",
 "q:GenerateCodeRecommendations",
 "q:SendMessage",
 "q:ListPlugins",
 "q:VerifyOAuthAppConnection"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GitLabDuoManagementPermissions",
 "Effect": "Allow",
 "Action": [
 "q:CreateOAuthAppConnection",
 "q:DeleteOAuthAppConnection"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GitLabDuoPluginPermissions",
 "Effect": "Allow",
 "Action": [
 "q:CreatePlugin",
 "q:DeletePlugin",
 "q:GetPlugin"
 ],
 "Resource": "arn:aws:qdeveloper:*:*:plugin/GitLabDuoWithAmazonQ/*"
 }
 ]
}`

```

Optionally, you can also use customer managed keys (CMK) to encrypt your resources
if you want full control over the lifecycle and usage of your key. The `kms:ViaService`
condition key to limit who can use CMK for encrypting and decrypting content. For more
information, see [Manage access to Amazon Q Developer for
third-party integration](security_iam_manage-access-with-kms-policies.md "security_iam_manage-access-with-kms-policies.md").

## GitLab quick actions

When invoked, quick actions perform tasks for you in GitLab issues and merge
requests. To learn how to invoke quick actions in GitLab, see the
[GitLab
documentation](https://docs.gitlab.com/ee/user/duo_amazon_q/index.html "https://docs.gitlab.com/ee/user/duo_amazon_q/index.html").

**Merge request generation and iteration**

- `/q dev` – Allows you to go from a high-level idea captured in a
  GitLab issue to having Amazon Q generate a ready-to-review merge request with the proposed code
  implementation. This helps streamline the process of turning concepts into working code. The
  merge request is created in a new branch and Amazon Q assigns the issue creator as a merge
  request reviewer. You're also provided a merge request summary. For more information, see
  [Turn
  an idea into a merge request](https://docs.gitlab.com/ee/user/duo_amazon_q/#turn-an-idea-into-a-merge-request "https://docs.gitlab.com/ee/user/duo_amazon_q/#turn-an-idea-into-a-merge-request").

**Code review**

- `/q review` – Allows you to initiate a merge request review in GitLab Duo
  with Amazon Q. An automatic code review is initiated for new merge requests. As a GitLab
  administrator, you can also configure Amazon Q to turn off automatic reviews. Automated code
  reviews identify and fix potential issues as Amazon Q generates and suggests code fixes to your
  merge request. They provide quality checks, analyzing for issues, logical errors, anti-patterns,
  code duplication, and more.

Amazon Q gives you code analysis with comments, with each comment providing a separate finding.
This quick action is available for all languages. Automatic code reviews are initiated when you open
new merge requests or reopen previously closed ones. However, automatic code reviews won't be
triggered by subsequent commits made within an existing merge request. You can manually trigger a
code review by using the `/q review` quick action.

You can configure code reviews to run automatically on every new merge request within your
GitLab instance or group. For more information, see
[Review a
merge request](https://docs.gitlab.com/ee/user/duo_amazon_q/#review-a-merge-request "https://docs.gitlab.com/ee/user/duo_amazon_q/#review-a-merge-request").

**Chat session in web UI and IDEs**

- GitLab Duo Chat and Code Suggestions works with Amazon Q to provide support for CI/CD
  configuration, error explanations, and addressing questions. You can use slash commands in a
  chat session to invoke the GitLab Duo with Amazon Q chat capabilities. For more information,
  see [Ask
  GitLab Duo Chat](https://docs.gitlab.com/user/gitlab_duo_chat/examples/ "https://docs.gitlab.com/user/gitlab_duo_chat/examples/").
