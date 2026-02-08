# Using

identity-based policies for AWS CodeBuild

This topic provides examples of identity-based policies that demonstrate how an
account administrator can attach permissions policies to IAM identities (that is,
users, groups, and roles) and thereby grant permissions to perform operations on
AWS CodeBuild resources.

###### Important

We recommend that you first review the introductory topics that explain the basic
concepts and options available to manage access to your CodeBuild resources. For more
information, see [Overview of
managing access permissions to your AWS CodeBuild resources](auth-and-access-control-iam-access-control-identity-based.md "auth-and-access-control-iam-access-control-identity-based.md").

###### Topics

- [Permissions required to use the AWS CodeBuild
  console](#console-permissions "#console-permissions")
- [Permissions required for AWS CodeBuild to connect to Amazon Elastic Container Registry](#ecr-policies "#ecr-policies")
- [Permissions required for the AWS CodeBuild console to
  connect to source providers](#console-policies "#console-policies")
- [AWS managed (predefined) policies for
  AWS CodeBuild](#managed-policies "#managed-policies")
- [CodeBuild managed policies and
  notifications](#notifications-permissions "#notifications-permissions")
- [CodeBuild updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")
- [Customer-managed policy examples](#customer-managed-policies "#customer-managed-policies")
  The following shows an example of a permissions policy that allows a user to get
  information about build projects only in the `us-east-2` region for account
  `123456789012` for any build project that starts with the name
  `my`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:BatchGetProjects",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/my*"
 }
 ]
}`

```

## Permissions required to use the AWS CodeBuild

console

A user who uses the AWS CodeBuild console must have a minimum set of permissions that
allows the user to describe other AWS resources for the AWS account. You must
have permissions from the following services:

- AWS CodeBuild
- Amazon CloudWatch
- CodeCommit (if you are storing your source code in an AWS CodeCommit
  repository)
- Amazon Elastic Container Registry (Amazon ECR) (if you are using a build environment that relies on a
  Docker image in an Amazon ECR repository)

###### Note

As of July 26, 2022, the default IAM policy has been updated. For more information, see [Permissions required for AWS CodeBuild to connect to Amazon Elastic Container Registry](#ecr-policies "#ecr-policies").

- Amazon Elastic Container Service (Amazon ECS) (if you are using a build environment that relies on a
  Docker image in an Amazon ECR repository)
- AWS Identity and Access Management (IAM)
- AWS Key Management Service (AWS KMS)
- Amazon Simple Storage Service (Amazon S3)

If you create an IAM policy that is more restrictive than the minimum required
permissions, the console won't function as intended.

## Permissions required for AWS CodeBuild to connect to Amazon Elastic Container Registry

As of July 26, 2022, AWS CodeBuild has updated its default IAM policy for Amazon ECR permission. The following permissions have been removed from the default policy:

```
"ecr:PutImage",
"ecr:InitiateLayerUpload",
"ecr:UploadLayerPart",
"ecr:CompleteLayerUpload"
```

For CodeBuild projects that were created before July 26, 2022, we recommend you update your policy with the following Amazon ECR policy:

```
"Action": [
    "ecr:BatchCheckLayerAvailability",
    "ecr:GetDownloadUrlForLayer",
    "ecr:BatchGetImage"
]
```

For more information on updating your policy, see [Allow users to interact with
CodeBuild](setting-up-service-permissions-group.md "setting-up-service-permissions-group.md").

## Permissions required for the AWS CodeBuild console to

connect to source providers

The AWS CodeBuild console uses the following API actions to connect to source
providers (for example, GitHub repositories).

- `codebuild:ListConnectedOAuthAccounts`
- `codebuild:ListRepositories`
- `codebuild:PersistOAuthToken`
- `codebuild:ImportSourceCredentials`

You can associate source providers (such as GitHub repositories) with your build
projects using the AWS CodeBuild console. To do this, you must first add the preceding API
actions to IAM access policies associated with the user you use to access
the AWS CodeBuild console.

The `ListConnectedOAuthAccounts`, `ListRepositories`, and
`PersistOAuthToken` API actions are not intended to be called by your
code. Therefore, these API actions are not included in the AWS CLI and AWS
SDKs.

## AWS managed (predefined) policies for

AWS CodeBuild

AWS addresses many common use cases by providing standalone IAM policies that are created and
administered by AWS. These AWS managed policies grant necessary permissions for common use cases so
you can avoid having to investigate what permissions are needed. The managed policies for CodeBuild also
provide permissions to perform operations in other services, such as IAM, AWS CodeCommit,Amazon EC2, Amazon ECR,
Amazon SNS, and Amazon CloudWatch Events, as required for the responsibilities for the users who have been granted the
policy in question. For example, the `AWSCodeBuildAdminAccess` policy is
an administrative-level user policy that allows users with this policy to create and manage CloudWatch
Events rules for project builds and Amazon SNS topics for notifications about project-related events
(topics whose names are prefixed with `arn:aws:codebuild:`), as well as administer projects
and report groups in CodeBuild. For more information, see [AWS Managed
Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your
account, are specific to AWS CodeBuild.

**AWSCodeBuildAdminAccess**

Provides full access to CodeBuild including permissions to administrate
CodeBuild build projects.

**AWSCodeBuildDeveloperAccess**

Provides access to CodeBuild but does not allow build project
administration.

**AWSCodeBuildReadOnlyAccess**

Provides read-only access to CodeBuild.

To access build output artifacts that CodeBuild creates, you must also attach the
AWS managed policy named `AmazonS3ReadOnlyAccess`.

To create and manage CodeBuild service roles, you must also attach the AWS managed
policy named `IAMFullAccess`.

You can also create your own custom IAM policies to allow permissions for CodeBuild
actions and resources. You can attach these custom policies to the users or
groups that require those permissions.

###### Topics

- [AWSCodeBuildAdminAccess](#admin-access-policy "#admin-access-policy")
- [AWSCodeBuildDeveloperAccess](#developer-access-policy "#developer-access-policy")
- [AWSCodeBuildReadOnlyAccess](#read-only-access-policy "#read-only-access-policy")

### AWSCodeBuildAdminAccess

The `AWSCodeBuildAdminAccess` policy provides full access to CodeBuild,
including permissions to administer CodeBuild build projects. Apply this policy only
to administrative-level users to grant them full control over CodeBuild projects,
report groups, and related resources in your AWS account, including the
ability to delete projects and report groups.

For the full managed policy, see
[AWSCodeBuildAdminAccess](../../../aws-managed-policy/latest/reference/AWSCodeBuildAdminAccess.md "../../../aws-managed-policy/latest/reference/AWSCodeBuildAdminAccess.md")
in the IAM managed policy reference.

### AWSCodeBuildDeveloperAccess

The `AWSCodeBuildDeveloperAccess` policy allows access to all of
the functionality of CodeBuild and project and report group-related resources. This
policy does not allow users to delete CodeBuild projects or report groups, or
related resources in other AWS services, such as CloudWatch Events. We recommend that you
apply this policy to most users.

For the full managed policy, see
[AWSCodeBuildDeveloperAccess](../../../aws-managed-policy/latest/reference/AWSCodeBuildDeveloperAccess.md "../../../aws-managed-policy/latest/reference/AWSCodeBuildDeveloperAccess.md")
in the IAM managed policy reference.

### AWSCodeBuildReadOnlyAccess

The `AWSCodeBuildReadOnlyAccess` policy grants read-only access to
CodeBuild and related resources in other AWS services. Apply this policy to users
who can view and run builds, view projects, and view report groups, but cannot
make any changes to them.

For the full managed policy, see
[AWSCodeBuildReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSCodeBuildReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSCodeBuildReadOnlyAccess.md")
in the IAM managed policy reference.

## CodeBuild managed policies and

notifications

CodeBuild supports notifications, which can notify users of important changes to
build projects.
Managed policies for CodeBuild include policy statements for notification
functionality. For more information, see [What are
notifications?](../../../codestar-notifications/latest/userguide/welcome.md "../../../codestar-notifications/latest/userguide/welcome.md").

### Permissions related to notifications in read-only managed

policies

The
`AWSCodeBuildReadOnlyAccess` managed policy includes the following
statements to allow read-only access to notifications. Users with this managed policy applied can view notifications for resources, but cannot create, manage, or
subscribe to them.

```
   {
        "Sid": "CodeStarNotificationsPowerUserAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:DescribeNotificationRule"
        ],
        "Resource": "*",
        "Condition" : {
            "ArnLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:codebuild:*:*:project/*"}
        }
    },
    {
        "Sid": "CodeStarNotificationsListAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:ListNotificationRules",
            "codestar-notifications:ListEventTypes",
            "codestar-notifications:ListTargets"
        ],
        "Resource": "*"
    }
```

### Permissions related to notifications in other managed

policies

The
`AWSCodeBuildDeveloperAccess` managed policy includes the following
statements to allow users to create, edit, and subscribe to notifications. Users cannot
delete notification rules or manage tags for resources.

```
    {
        "Sid": "CodeStarNotificationsReadWriteAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:CreateNotificationRule",
            "codestar-notifications:DescribeNotificationRule",
            "codestar-notifications:UpdateNotificationRule",
            "codestar-notifications:Subscribe",
            "codestar-notifications:Unsubscribe"
        ],
        "Resource": "*",
        "Condition" : {
            "ArnLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:codebuild:*:*:project/*"}
        }
    },
    {
        "Sid": "CodeStarNotificationsListAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:ListNotificationRules",
            "codestar-notifications:ListTargets",
            "codestar-notifications:ListTagsforResource",
            "codestar-notifications:ListEventTypes"
        ],
        "Resource": "*"
    },
    {
        "Sid": "SNSTopicListAccess",
        "Effect": "Allow",
        "Action": [
            "sns:ListTopics"
        ],
        "Resource": "*"
    },
    {
        "Sid": "CodeStarNotificationsChatbotAccess",
        "Effect": "Allow",
        "Action": [
            "chatbot:DescribeSlackChannelConfigurations",
            "chatbot:ListMicrosoftTeamsChannelConfigurations"
          ],
       "Resource": "*"
    }
```

For more information about IAM and notifications, see [Identity and Access Management for AWS CodeStar Notifications](../../../codestar-notifications/latest/userguide/security-iam.md "../../../codestar-notifications/latest/userguide/security-iam.md").

## CodeBuild updates to AWS managed

policies

View details about updates to AWS managed policies for CodeBuild since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on [AWS CodeBuild User Guide document history](history.md "history.md") .

| Change                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                     | Date              |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `AWSCodeBuildAdminAccess` and `AWSCodeBuildDeveloperAccess` –<br>Update to existing policies                                | CodeBuild added the `ssmmessages:OpenDataChannel` permission to these policies to support Session Manager interactive build debugging.<br>The `AWSCodeBuildAdminAccess` and `AWSCodeBuildDeveloperAccess` policies now include the `ssmmessages:OpenDataChannel` action for Session Manager session resources (`arn:aws:ssm:*:*:session/*`) to support SigV4 enforcement on this WebSocket API. | December 1, 2025  |
| `AWSCodeBuildAdminAccess`, `AWSCodeBuildDeveloperAccess`, and `AWSCodeBuildReadOnlyAccess` –<br>Update to existing policies | CodeBuild updated a resource to these policies.<br>The `AWSCodeBuildAdminAccess`, `AWSCodeBuildDeveloperAccess`, and `AWSCodeBuildReadOnlyAccess` policies have been changed to update an existing resource. The original resource<br>`arn:aws:codebuild:*` has been updated to `arn:aws:codebuild:*:*:project/*`.                                                                              | November 15, 2024 |
| `AWSCodeBuildAdminAccess`, `AWSCodeBuildDeveloperAccess`, and `AWSCodeBuildReadOnlyAccess` –<br>Update to existing policies | CodeBuild added a resource to these policies to support the AWS CodeConnections rebranding.<br>The `AWSCodeBuildAdminAccess`, `AWSCodeBuildDeveloperAccess`, and `AWSCodeBuildReadOnlyAccess` policies have been changed to add a resource, `arn:aws:codeconnections:*:*:*`.                                                                                                                    | April 18, 2024    |
| `AWSCodeBuildAdminAccess` and `AWSCodeBuildDeveloperAccess` –<br>Update to existing policies                                | CodeBuild added a permission to these policies to support an additional notification type using Amazon Q Developer in chat applications.<br>The `AWSCodeBuildAdminAccess` and `AWSCodeBuildDeveloperAccess` policies have been changed to add a permission, `chatbot:ListMicrosoftTeamsChannelConfigurations`.                                                                                  | May 16, 2023      |
| CodeBuild started tracking changes                                                                                          | CodeBuild started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                | May 16, 2021      |

## Customer-managed policy examples

In this section, you can find example user policies that grant permissions for
AWS CodeBuild actions. These policies work when you are using the CodeBuild API, AWS SDKs,
or AWS CLI. When you are using the console, you must grant additional,
console-specific permissions. For information, see [Permissions required to use the AWS CodeBuild
console](#console-permissions "#console-permissions").

You can use the following sample IAM policies to limit CodeBuild access for your
users and roles.

###### Topics

- [Allow a
  user to get information about build projects](#customer-managed-policies-example-batch-get-projects "#customer-managed-policies-example-batch-get-projects")
- [Allow
  a user to get information about fleets](#customer-managed-policies-get-information-about-fleets "#customer-managed-policies-get-information-about-fleets")
- [Allow a user to get information about report groups](#customer-managed-policies-get-information-about-report-group "#customer-managed-policies-get-information-about-report-group")
- [Allow
  a user to get information about reports](#customer-managed-policies-get-information-about-reports "#customer-managed-policies-get-information-about-reports")
- [Allow a user
  to create build projects](#customer-managed-policies-example-create-project "#customer-managed-policies-example-create-project")
- [Allow a
  user to create a fleet](#customer-managed-policies-example-create-fleet "#customer-managed-policies-example-create-fleet")
- [Allow a
  user to create a report group](#customer-managed-policies-example-create-report-group "#customer-managed-policies-example-create-report-group")
- [Allow a user
  to delete a fleet](#customer-managed-policies-example-delete-fleet "#customer-managed-policies-example-delete-fleet")
- [Allow a
  user to delete a report group](#customer-managed-policies-example-delete-report-group "#customer-managed-policies-example-delete-report-group")
- [Allow a user
  to delete a report](#customer-managed-policies-example-delete-report "#customer-managed-policies-example-delete-report")
- [Allow a user
  to delete build projects](#customer-managed-policies-example-delete-project "#customer-managed-policies-example-delete-project")
- [Allow a user
  to get a list of build project names](#customer-managed-policies-example-list-projects "#customer-managed-policies-example-list-projects")
- [Allow a user
  to change information about build projects](#customer-managed-policies-example-update-project "#customer-managed-policies-example-update-project")
- [Allow a
  user to change a fleet](#customer-managed-policies-example-change-fleet "#customer-managed-policies-example-change-fleet")
- [Allow a
  user to change a report group](#customer-managed-policies-example-change-report-group "#customer-managed-policies-example-change-report-group")
- [Allow a
  user to get information about builds](#customer-managed-policies-example-batch-get-builds "#customer-managed-policies-example-batch-get-builds")
- [Allow a user to get a list of build IDs for a build project](#customer-managed-policies-example-list-builds-for-project "#customer-managed-policies-example-list-builds-for-project")
- [Allow a user to
  get a list of build IDs](#customer-managed-policies-example-list-builds "#customer-managed-policies-example-list-builds")
- [Allow a user to get a list of fleets](#customer-managed-policies-example-get-list-of-fleets "#customer-managed-policies-example-get-list-of-fleets")
- [Allow a user to get a list of report groups](#customer-managed-policies-example-get-list-of-report-groups "#customer-managed-policies-example-get-list-of-report-groups")
- [Allow a
  user to get a list of reports](#customer-managed-policies-example-get-list-of-reports "#customer-managed-policies-example-get-list-of-reports")
- [Allow a user to get a list of reports for a report group](#customer-managed-policies-example-get-list-of-reports-for-report-group "#customer-managed-policies-example-get-list-of-reports-for-report-group")
- [Allow a user to get a list of test cases for a report](#customer-managed-policies-example-get-list-of-test-cases-for-report "#customer-managed-policies-example-get-list-of-test-cases-for-report")
- [Allow a user to
  start running builds](#customer-managed-policies-example-start-build "#customer-managed-policies-example-start-build")
- [Allow a user to
  attempt to stop builds](#customer-managed-policies-example-stop-build "#customer-managed-policies-example-stop-build")
- [Allow a user
  to attempt to delete builds](#customer-managed-policies-example-delete-builds "#customer-managed-policies-example-delete-builds")
- [Allow a user to get information about Docker images that are managed by
  CodeBuild](#customer-managed-policies-example-list-curated-environment-images "#customer-managed-policies-example-list-curated-environment-images")
- [Allow a user to add a permission policy for a fleet service role](#customer-managed-policies-example-permission-policy-fleet-service-role "#customer-managed-policies-example-permission-policy-fleet-service-role")
- [Allow CodeBuild access to AWS services required to create a VPC network
  interface](#customer-managed-policies-example-create-vpc-network-interface "#customer-managed-policies-example-create-vpc-network-interface")
- [Use a deny
  statement to prevent AWS CodeBuild from disconnecting from source providers](#customer-managed-policies-example-deny-disconnect "#customer-managed-policies-example-deny-disconnect")

### Allow a

user to get information about build projects

The following example policy statement allows a user to get information about
build projects in the `us-east-2` Region for account
`123456789012` for any build project that starts with the
name `my`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:BatchGetProjects",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/my*"
 }
 ]
}`

```

### Allow

a user to get information about fleets

The following example policy statement allows a user to get information about
fleets in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:BatchGetFleets",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:fleet/*"
 }
 ]
}`

```

### Allow a user to get information about report groups

The following example policy statement allows a user to get information about
report groups in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:BatchGetReportGroups",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:report-group/*"
 }
 ]
}`

```

### Allow

a user to get information about reports

The following example policy statement allows a user to get information about
reports in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:BatchGetReports",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:report-group/*"
 }
 ]
}`

```

### Allow a user

to create build projects

The following example policy statement allows a user to create build projects
with any name but only in the `us-east-2` Region for account
`123456789012` and only using the specified CodeBuild service
role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:CreateProject",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/CodeBuildServiceRole"
 }
 ]
}`

```

The following example policy statement allows a user to create build projects
with any name but only in the `us-east-2` Region for account
`123456789012` and only using the specified CodeBuild service role.
It also enforces that the user can only use the specified service role
with AWS CodeBuild and not any other AWS services.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:CreateProject",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/CodeBuildServiceRole",
 "Condition": {
 "StringEquals": {"iam:PassedToService": "codebuild.amazonaws.com"}
 }
 }
 ]
}`

```

### Allow a

user to create a fleet

The following example policy statement allows a user to create a fleet
in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:CreateFleet",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:fleet/*"
 }
 ]
}`

```

### Allow a

user to create a report group

The following example policy statement allows a user to create a report group
in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:CreateReportGroup",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:report-group/*"
 }
 ]
}`

```

### Allow a user

to delete a fleet

The following example policy statement allows a user to delete a fleet in the
`us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:DeleteFleet",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:fleet/*"
 }
 ]
}`

```

### Allow a

user to delete a report group

The following example policy statement allows a user to delete a report group
in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:DeleteReportGroup",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:report-group/*"
 }
 ]
}`

```

### Allow a user

to delete a report

The following example policy statement allows a user to delete a report in the
`us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:DeleteReport",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:report-group/*"
 }
 ]
}`

```

### Allow a user

to delete build projects

The following example policy statement allows a user to delete build projects
in the `us-east-2` Region for account
`123456789012` for any build project that starts with the
name `my`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:DeleteProject",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/my*"
 }
 ]
}`

```

### Allow a user

to get a list of build project names

The following example policy statement allows a user to get a list of build
project names for the same account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:ListProjects",
 "Resource": "*"
 }
 ]
}`

```

### Allow a user

to change information about build projects

The following example policy statement allows a user to change information
about build projects with any name but only in the `us-east-2` Region
for account `123456789012` and only using the specified
AWS CodeBuild service role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:UpdateProject",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/CodeBuildServiceRole"
 }
 ]
}`

```

### Allow a

user to change a fleet

The following example policy statement allows a user to change a fleet
in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:UpdateFleet",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:fleet/*"
 }
 ]
}`

```

### Allow a

user to change a report group

The following example policy statement allows a user to change a report group
in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:UpdateReportGroup",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:report-group/*"
 }
 ]
}`

```

### Allow a

user to get information about builds

The following example policy statement allows a user to get information about
builds in the `us-east-2` Region for account
`123456789012` for the build projects named
`my-build-project` and
`my-other-build-project`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:BatchGetBuilds",
 "Resource": [
 "arn:aws:codebuild:us-east-2:`111122223333`:project/my-build-project",
 "arn:aws:codebuild:us-east-2:`111122223333`:project/my-other-build-project"
 ]
 }
 ]
}`

```

### Allow a user to get a list of build IDs for a build project

The following example policy statement allows a user to get a list of build
IDs in the `us-east-2` Region for account
`123456789012` for the build projects named
`my-build-project` and
`my-other-build-project`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:ListBuildsForProject",
 "Resource": [
 "arn:aws:codebuild:us-east-2:`111122223333`:project/my-build-project",
 "arn:aws:codebuild:us-east-2:`111122223333`:project/my-other-build-project"
 ]
 }
 ]
}`

```

### Allow a user to

get a list of build IDs

The following example policy statement allows a user to get a list of all
build IDs for the same account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:ListBuilds",
 "Resource": "*"
 }
 ]
}`

```

### Allow a user to get a list of fleets

The following example policy statement allows a user to get a list of fleets
in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:ListFleets",
 "Resource": "*"
 }
 ]
}`

```

### Allow a user to get a list of report groups

The following example policy statement allows a user to get a list of report
groups in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:ListReportGroups",
 "Resource": "*"
 }
 ]
}`

```

### Allow a

user to get a list of reports

The following example policy statement allows a user to get a list of reports
in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:ListReports",
 "Resource": "*"
 }
 ]
}`

```

### Allow a user to get a list of reports for a report group

The following example policy statement allows a user to get a list of reports
for a report group in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:ListReportsForReportGroup",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:report-group/*"
 }
 ]
}`

```

### Allow a user to get a list of test cases for a report

The following example policy statement allows a user to get a list of test
cases for a report in the `us-east-2` Region for account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:DescribeTestCases",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:report-group/*"
 }
 ]
}`

```

### Allow a user to

start running builds

The following example policy statement allows a user to run builds in the
`us-east-2` Region for account `123456789012`
for a build project that starts with the name `my`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:StartBuild",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/my*"
 }
 ]
}`

```

### Allow a user to

attempt to stop builds

The following example policy statement allows a user to attempt to stop
running builds only in the `us-east-2` region for account
`123456789012` for any build project that starts with the
name `my`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:StopBuild",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/my*"
 }
 ]
}`

```

### Allow a user

to attempt to delete builds

The following example policy statement allows a user to attempt to delete
builds only in the `us-east-2` Region for account
`123456789012` for any build project that starts with the
name `my`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:BatchDeleteBuilds",
 "Resource": "arn:aws:codebuild:us-east-2:`111122223333`:project/my*"
 }
 ]
}`

```

### Allow a user to get information about Docker images that are managed by

CodeBuild

The following example policy statement allows a user to get information about
all Docker images that are managed by CodeBuild:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:ListCuratedEnvironmentImages",
 "Resource": "*"
 }
 ]
}`

```

### Allow a user to add a permission policy for a fleet service role

The following example resource policy statement allows a user to add a VPC permission policy
for a fleet service role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeBuildFleetVpcCreateNI",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:`us-west-2`:`111122223333`:subnet/subnet-id-1",
 "arn:aws:ec2:`us-west-2`:`111122223333`:security-group/security-group-id-1",
 "arn:aws:ec2:`us-west-2`:`111122223333`:network-interface/*"
 ]
 },
 {
 "Sid": "CodeBuildFleetVpcPermission",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeBuildFleetVpcNIPermission",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterfacePermission"
 ],
 "Resource": "arn:aws:ec2:`us-west-2`:`111122223333`:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:Subnet": [
 "arn:aws:ec2:`us-west-2`:`111122223333`:subnet/subnet-id-1"
 ]
 }
 }
 }
 ]
}`

```

The following example resource policy statement allows a user to add a custom Amazon Managed Image (AMI) permission policy
for a fleet service role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:DescribeImages",
 "Resource": "*"
 }
 ]
}`

```

The following example trust policy statement allows a user to add a permission policy
for a fleet service role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeBuildFleetVPCTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "codebuild.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

### Allow CodeBuild access to AWS services required to create a VPC network

interface

The following example policy statement grants AWS CodeBuild permission to create a
network interface in a VPC with two subnets:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterfacePermission"
 ],
 "Resource": "arn:aws:ec2:`us-west-2`:`111122223333`:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:AuthorizedService": "codebuild.amazonaws.com"
 },
 "ArnEquals": {
 "ec2:Subnet": [
 "arn:aws:ec2:`us-west-2`:`111122223333`:subnet/subnet-id-1",
 "arn:aws:ec2:`us-west-2`:`111122223333`:subnet/subnet-id-2"
 ]
 }
 }
 }
 ]
}`

```

### Use a deny

statement to prevent AWS CodeBuild from disconnecting from source providers

The following example policy statement uses a deny statement to prevent
AWS CodeBuild from disconnecting from source providers. It uses
`codebuild:DeleteOAuthToken`, which is the inverse of
`codebuild:PersistOAuthToken` and
`codebuild:ImportSourceCredentials`, to connect with source
providers. For more information, see [Permissions required for the AWS CodeBuild console to
connect to source providers](#console-policies "#console-policies").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "codebuild:DeleteOAuthToken",
 "Resource": "*"
 }
 ]
}`

```
