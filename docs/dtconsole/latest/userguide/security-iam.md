# Identity and access management for

AWS CodeStar Notifications and AWS CodeConnections

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use AWS CodeStar Notifications and AWS CodeConnections resources. IAM is an AWS service that you can
use with no additional charge.

###### Note

Actions for resources that are created under the new service prefix
`codeconnections` are available. Creating a resource under the new
service prefix will use `codeconnections` in the resource ARN. Actions and
resources for the `codestar-connections` service prefix remain available.
When specifying a resource in the IAM policy, the service prefix needs to match that of
the resource.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Managing access using policies](#security_iam_access-manage "#security_iam_access-manage")
- [How features in the developer tools
  console work with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [AWS CodeConnections permissions
  reference](#permissions-reference-connections "#permissions-reference-connections")
- [Identity-based policy
  examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [Using tags to control access to
  AWS CodeConnections resources](connections-tag-based-access-control.md "connections-tag-based-access-control.md")
- [Using notifications and
  connections in the console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Troubleshooting AWS CodeStar Notifications and AWS CodeConnections
  identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")
- [Using service-linked roles for
  AWS CodeStar Notifications](using-service-linked-roles.md "using-service-linked-roles.md")
- [Using service-linked roles for
  AWS CodeConnections](service-linked-role-connections.md "service-linked-role-connections.md")
- [AWS managed policies for AWS CodeConnections](security-iam-awsmanpol.md "security-iam-awsmanpol.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshooting AWS CodeStar Notifications and AWS CodeConnections
  identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How features in the developer tools
  console work with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md"))
- **IAM administrator** - write policies to manage
  access (see [Identity-based policy
  examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"))

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### IAM users and groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## Managing access using policies

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

### Identity-based

policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

## AWS CodeConnections permissions

reference

The following tables list each AWS CodeConnections API operation, the corresponding
actions for which you can grant permissions, and the format of the resource ARN to use
for granting permissions. The AWS CodeConnections APIs are grouped into tables based
on the scope of the actions allowed by that API. Refer to it when writing permissions
policies that you can attach to an IAM identity (identity-based policies).

When you create a permissions policy, you specify the actions in the policy's
`Action` field. You specify the resource value in the policy's
`Resource` field as an ARN, with or without a wildcard character (\*).

To express conditions in your connections policies, use the condition keys described
here and listed in [Condition keys](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys"). You
can also use AWS-wide condition keys. For a complete list of AWS-wide keys, see
[Available
keys](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

To specify an action, use the `codeconnections` prefix followed by the API
operation name (for example, `codeconnections:ListConnections` or
`codeconnections:CreateConnection`.

**Using wildcards**

To specify multiple actions or resources, use a wildcard character (\*) in your ARN.
For example, `codeconnections:*` specifies all AWS CodeConnections actions
and `codeconnections:Get*` specifies all AWS CodeConnections actions that
begin with the word `Get`. The following example grants access to all
resources with names that begin with `MyConnection`.

```
arn:aws:codeconnections:us-west-2:`account-ID`:connection/*
```

You can use wildcards only with the `connection` resources
listed in the following table. You can't use wildcards with
`region` or `account-id`
resources. For more information about wildcards, see [IAM identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md "../../../IAM/latest/UserGuide/reference_identifiers.md") in
_IAM User Guide_.

###### Topics

- [Permissions for
  managing connections](#permissions-reference-connections-managing "#permissions-reference-connections-managing")
- [Permissions for managing
  hosts](#permissions-reference-connections-hosts "#permissions-reference-connections-hosts")
- [Permissions for
  completing connections](#permissions-reference-connections-handshake "#permissions-reference-connections-handshake")
- [Permissions for
  setting up hosts](#connections-permissions-actions-host-registration "#connections-permissions-actions-host-registration")
- [Passing a
  connection to a service](#permissions-reference-connections-passconnection "#permissions-reference-connections-passconnection")
- [Using a connection](#permissions-reference-connections-use "#permissions-reference-connections-use")
- [Supported access types
  for ProviderAction](#permissions-reference-connections-access "#permissions-reference-connections-access")
- [Supported permissions
  for tagging connection resources](#permissions-reference-connections-tagging "#permissions-reference-connections-tagging")
- [Passing a
  connection to a repository link](#permissions-reference-connections-passrepository "#permissions-reference-connections-passrepository")
- [Supported condition key
  for repository links](#permissions-reference-connections-branch "#permissions-reference-connections-branch")
- [Supported permissions
  for connection sharing](#permissions-reference-connections-sharing "#permissions-reference-connections-sharing")

### Permissions for

managing connections

A role or user designated to use the AWS CLI or SDK to view, create, or delete
connections should have permissions limited to the following.

###### Note

You cannot complete or use a connection in the console with only the following
permissions. You need to add the permissions in [Permissions for
completing connections](#permissions-reference-connections-handshake "#permissions-reference-connections-handshake").

```
codeconnections:CreateConnection
codeconnections:DeleteConnection
codeconnections:GetConnection
codeconnections:ListConnections
```

Use the scroll bars to see the rest of the table.

| AWS CodeConnections required permissions for managing connections | AWS CodeConnections actions                                                                                        | Required permissions                                                     | Resources |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | --------- |
| CreateConnection                                                  | `codeconnections:CreateConnection`<br>Required to use the CLI or console to create a<br>connection.                | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| DeleteConnection                                                  | `codeconnections:DeleteConnection`<br>Required to use the CLI or console to delete a<br>connection.                | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| GetConnection                                                     | `codeconnections:GetConnection`<br>Required to use the CLI or console to view details about a<br>connection.       | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| ListConnections                                                   | `codeconnections:ListConnections`<br>Required to use the CLI or console to list all connections in<br>the account. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |

These operations support the following condition keys:

| Action                             | Condition keys                       |
| ---------------------------------- | ------------------------------------ |
| `codeconnections:CreateConnection` | `codeconnections:ProviderType`       |
| `codeconnections:DeleteConnection` | N/A                                  |
| `codeconnections:GetConnection`    | N/A                                  |
| `codeconnections:ListConnections`  | `codeconnections:ProviderTypeFilter` |

### Permissions for managing

hosts

A role or user designated to use the AWS CLI or SDK to view, create, or delete hosts
should have permissions limited to the following.

###### Note

You cannot complete or use a connection in the host with only the following
permissions. You need to add the permissions in [Permissions for
setting up hosts](#connections-permissions-actions-host-registration "#connections-permissions-actions-host-registration").

```
codeconnections:CreateHost
codeconnections:DeleteHost
codeconnections:GetHost
codeconnections:ListHosts
```

Use the scroll bars to see the rest of the table.

| AWS CodeConnections required permissions for managing hosts | AWS CodeConnections actions                                                                            | Required permissions                                         | Resources |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | --------- |
| CreateHost                                                  | `codeconnections:CreateHost`<br>Required to use the CLI or console to create a host.                   | arn:aws:codeconnections:`region`:`account-id`:host/`host-id` |
| DeleteHost                                                  | `codeconnections:DeleteHost`<br>Required to use the CLI or console to delete a host.                   | codeconnections:`region`:`account-id`:host/`host-id`         |
| GetHost                                                     | `codeconnections:GetHost`<br>Required to use the CLI or console to view details about a<br>host.       | arn:aws:codeconnections:`region`:`account-id`:host/`host-id` |
| ListHosts                                                   | `codeconnections:ListHosts`<br>Required to use the CLI or console to list all hosts in the<br>account. | arn:aws:codeconnections:`region`:`account-id`:host/`host-id` |

These operations support the following condition keys:

| Action                       | Condition keys                                            |
| ---------------------------- | --------------------------------------------------------- |
| `codeconnections:CreateHost` | `codeconnections:ProviderType`<br>`codeconnections:VpcId` |
| `codeconnections:DeleteHost` | N/A                                                       |
| `codeconnections:GetHost`    | N/A                                                       |
| `codeconnections:ListHosts`  | `codeconnections:ProviderTypeFilter`                      |

For an example policy that uses the **VpcId**
condition key, see [Example:
Limit host VPC permissions using the VpcId
context key](security_iam_id-based-policy-examples-connections.md#security_iam_id-based-policy-examples-connections-vpc "security_iam_id-based-policy-examples-connections.md#security_iam_id-based-policy-examples-connections-vpc") .

### Permissions for

completing connections

A role or user designated to manage connections in the console should have the
permissions required to complete a connection in the console and create an
installation, which includes authorizing the handshake to the provider and creating
installations for connections to use. Use the following permissions in addition to
the permissions above.

The following IAM operations are used by the console when performing a
browser-based handshake. The `ListInstallationTargets`,
`GetInstallationUrl`, `StartOAuthHandshake`,
`UpdateConnectionInstallation`, and
`GetIndividualAccessToken` are IAM policy permissions. They are not
API actions.

```
codeconnections:GetIndividualAccessToken
codeconnections:GetInstallationUrl
codeconnections:ListInstallationTargets
codeconnections:StartOAuthHandshake
codeconnections:UpdateConnectionInstallation

```

Based on this, the following permissions are needed to use, create, update, or
delete a connection in the console.

```
codeconnections:CreateConnection
codeconnections:DeleteConnection
codeconnections:GetConnection
codeconnections:ListConnections
codeconnections:UseConnection
codeconnections:ListInstallationTargets
codeconnections:GetInstallationUrl
codeconnections:StartOAuthHandshake
codeconnections:UpdateConnectionInstallation
codeconnections:GetIndividualAccessToken
```

Use the scroll bars to see the rest of the table.

| AWS CodeConnections required permissions for completing connections | AWS CodeConnections actions                                                                                                                                          | Required permissions                                                     | Resources |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------- |
| `GetIndividualAccessToken`                                          | `codeconnections:GetIndividualAccessToken`<br>Required to use the console to complete a connection. This is<br>an IAM policy permission only, not an API action.     | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `GetInstallationUrl`                                                | `codeconnections:GetInstallationUrl`<br>Required to use the console to complete a connection. This is<br>an IAM policy permission only, not an API action.           | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `ListInstallationTargets`                                           | `codeconnections:ListInstallationTargets`<br>Required to use the console to complete a connection. This is<br>an IAM policy permission only, not an API action.      | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `StartOAuthHandshake`                                               | `codeconnections:StartOAuthHandshake`<br>Required to use the console to complete a connection. This is<br>an IAM policy permission only, not an API action.          | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `UpdateConnectionInstallation`                                      | `codeconnections:UpdateConnectionInstallation`<br>Required to use the console to complete a connection. This is<br>an IAM policy permission only, not an API action. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |

These operations support the following condition keys.

| Action                                         | Condition keys                   |
| ---------------------------------------------- | -------------------------------- |
| `codeconnections:GetIndividualAccessToken`     | `codeconnections:ProviderType`   |
| `codeconnections:GetInstallationUrl`           | `codeconnections:ProviderType`   |
| `codeconnections:ListInstallationTargets`      | N/A                              |
| `codeconnections:StartOAuthHandshake`          | `codeconnections:ProviderType`   |
| `codeconnections:UpdateConnectionInstallation` | `codeconnections:InstallationId` |

### Permissions for

setting up hosts

A role or user designated to manage connections in the console should have the
permissions required to set up a host in the console, which includes authorizing the
handshake to the provider and installing the host app. Use the following permissions
in addition to the permissions for hosts above.

The following IAM operations are used by the console when performing a
browser-based host registration. `RegisterAppCode` and
`StartAppRegistrationHandshake` are IAM policy permissions. They
are not API actions.

```

codeconnections:RegisterAppCode
codeconnections:StartAppRegistrationHandshake

```

Based on this, the following permissions are needed to use, create, update, or
delete a connection in the console that requires a host (such as installed provider
types).

```
codeconnections:CreateConnection
codeconnections:DeleteConnection
codeconnections:GetConnection
codeconnections:ListConnections
codeconnections:UseConnection
codeconnections:ListInstallationTargets
codeconnections:GetInstallationUrl
codeconnections:StartOAuthHandshake
codeconnections:UpdateConnectionInstallation
codeconnections:GetIndividualAccessToken
codeconnections:RegisterAppCode
codeconnections:StartAppRegistrationHandshake

```

Use the scroll bars to see the rest of the table.

| AWS CodeConnections required permissions for completing host setup | Connections actions                                                                                                                                                 | Required permissions                                         | Resources |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------- |
| `RegisterAppCode`                                                  | `codeconnections:RegisterAppCode`<br>Required to use the console to complete host setup. This is an<br>IAM policy permission only, not an API action.               | arn:aws:codeconnections:`region`:`account-id`:host/`host-id` |
| `StartAppRegistrationHandshake`                                    | `codeconnections:StartAppRegistrationHandshake`<br>Required to use the console to complete host setup. This is an<br>IAM policy permission only, not an API action. | arn:aws:codeconnections:`region`:`account-id`:host/`host-id` |

These operations support the following condition keys.

### Passing a

connection to a service

When a connection is passed to a service (for example, when a connection ARN is
provided in a pipeline definition to create or update a pipeline) the user must have
the `codeconnections:PassConnection` permission.

Use the scroll bars to see the rest of the table.

| AWS CodeConnections required permissions for passing a connection | AWS CodeConnections actions                                                     | Required permissions                                                     | Resources |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------- |
| `PassConnection`                                                  | `codeconnections:PassConnection`<br>Required to pass a connection to a service. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |

This operation also supports the following condition key:

- `codeconnections:PassedToService`

| Supported values for condition keys | Key                                                                                 | Valid action providers |
| ----------------------------------- | ----------------------------------------------------------------------------------- | ---------------------- |
| `codeconnections:PassedToService`   | • `codeguru-reviewer`<br>• `codepipeline.amazonaws.com`<br>• `proton.amazonaws.com` |

### Using a connection

When a service like CodePipeline uses a connection, the service role must have the
`codeconnections:UseConnection` permission for a given
connection.

To manage connections in the console, the user policy must have the
`codeconnections:UseConnection` permission.

Use the scroll bars to see the rest of the table.

| AWS CodeConnections required action for using connections | AWS CodeConnections actions                                      | Required permissions                                                     | Resources |
| --------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------ | --------- |
| `UseConnection`                                           | `codeconnections:UseConnection`<br>Required to use a connection. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |

This operation also supports the following condition keys:

- `codeconnections:BranchName`
- `codeconnections:FullRepositoryId`
- `codeconnections:OwnerId`
- `codeconnections:ProviderAction`
- `codeconnections:ProviderPermissionsRequired`
- `codeconnections:RepositoryName`

| Supported values for condition keys           | Key                                                                                                                                                                                                                                                                                                                                                              | Valid action providers |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `codeconnections:FullRepositoryId`            | The user name and repository name of a repository, such as<br>`my-owner/my-repository`. Supported only when the<br>connection is being used to access a specific repository.                                                                                                                                                                                     |
| `codeconnections:ProviderPermissionsRequired` | read_only or read_write                                                                                                                                                                                                                                                                                                                                          |
| `codeconnections:ProviderAction`              | `GetBranch`, `ListRepositories`,<br>`ListOwners`, `ListBranches`,<br>`StartUploadArchiveToS3`, `GitPush`,<br>`GitPull`,<br>`GetUploadArchiveToS3Status`,<br>`CreatePullRequestDiffComment`,<br>`GetPullRequest`, `ListBranchCommits`,<br>`ListCommitFiles`,<br>`ListPullRequestComments`,<br>`ListPullRequestCommits`.<br>For information, see the next section. |

The required condition keys for some functionality might change over time. We
recommend that you use `codeconnections:UseConnection` to control access to
a connection unless your access control requirements require different
permissions.

### Supported access types

for `ProviderAction`

When a connection is used by an AWS service, it results in API calls being made
to your source code provider. For example, a service might list repositories for a
Bitbucket connection by calling the
`https://api.bitbucket.org/2.0/repositories/`username``
API.

The `ProviderAction` condition key allows you to restrict which APIs on
a provider can be called. Because the API path might be generated dynamically, and
the path varies from provider to provider, the `ProviderAction` value is
mapped to an abstract action name rather than the URL of the API. This allows you to
write policies that have the same effect regardless of the provider type for the
connection.

The following are the access types that are granted for each of the supported
`ProviderAction` values. The following are IAM policy permissions.
They are not API actions.

Use the scroll bars to see the rest of the table.

AWS CodeConnections supported access types for
`ProviderAction`| AWS CodeConnections permission | Required permissions | Resources |
| --- | --- | --- |
| `GetBranch` | `codeconnections:GetBranch`<br>Required to access information about a branch, such as the<br>latest commit for that branch. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `ListRepositories` | `codeconnections:ListRepositories`<br>Required to access a list of public and private repositories,<br>including details about those repositories, that belong to an<br>owner. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `ListOwners` | `codeconnections:ListOwners`<br>Required to access a list of owners that the connection has<br>access to. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `ListBranches` | `codeconnections:ListBranches`<br>Required to access the list of branches that exist on a given<br>repository. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `StartUploadArchiveToS3` | `codeconnections:StartUploadArchiveToS3`<br>Required to read source code and upload it to Amazon S3. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `GitPush` | `codeconnections:GitPush`<br>Required to write to a repository using Git. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `GitPull` | `codeconnections:GitPull`<br>Required to read from a repository using Git. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `GetUploadArchiveToS3Status` | `codeconnections:GetUploadArchiveToS3Status`<br>Required to access the status of an upload, including any<br>error messages, started by<br>`StartUploadArchiveToS3`. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `CreatePullRequestDiffComment` | `codeconnections:CreatePullRequestDiffComment`<br>Required to access comments on a pull request. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `GetPullRequest` | `codeconnections:GetPullRequest`<br>Required to view pull requests for a repository. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `ListBranchCommits` | `codeconnections:ListBranchCommits`<br>Required to view a list of commits for a repository<br>branch. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `ListCommitFiles` | `codeconnections:ListCommitFiles`<br>Required to view a list of files for a commit. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `ListPullRequestComments` | `codeconnections:ListPullRequestComments`<br>Required to view a list of comments for a pull request. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |
| `ListPullRequestCommits` | `codeconnections:ListPullRequestCommits`<br>Required to view a list of commits for a pull request. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |

### Supported permissions

for tagging connection resources

The following IAM operations are used when tagging connection resources.

```

codeconnections:ListTagsForResource
codeconnections:TagResource
codeconnections:UntagResource

```

Use the scroll bars to see the rest of the table.

AWS CodeConnections required actions for tagging connection
resources| AWS CodeConnections actions | Required permissions | Resources |
| --- | --- | --- |
| `ListTagsForResource` | `codeconnections:ListTagsForResource`<br>Required to view a list of tags associated with the connection<br>resource. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id`,arn:aws:codeconnections:`region`:`account-id`:host/`host-id` |
| `TagResource` | `codeconnections:TagResource`<br>Required to tag a connection resource. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id`,arn:aws:codeconnections:`region`:`account-id`:host/`host-id` |
| `UntagResource` | `codeconnections:UntagResource`<br>Required to remove tags from a connection resource. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id`,arn:aws:codeconnections:`region`:`account-id`:host/`host-id` |

### Passing a

connection to a repository link

When a repository-link is provided in a sync configuration, the user must have the
`codeconnections:PassRepository` permission for the repository-link
ARN/resource.

Use the scroll bars to see the rest of the table.

| AWS CodeConnections required permissions for passing a connection | AWS CodeConnections actions                                                                        | Required permissions                                                               | Resources |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------- |
| `PassRepository`                                                  | `codeconnections:PassRepository`<br>Required to pass a repository-link to a sync<br>configuration. | arn:aws:codeconnections:`region`:`account-id`:repository-link/`repository-link-id` |

This operation also supports the following condition key:

- `codeconnections:PassedToService`

| Supported values for condition keys | Key                                                   | Valid action providers |
| ----------------------------------- | ----------------------------------------------------- | ---------------------- |
| `codeconnections:PassedToService`   | • `cloudformation.sync.codeconnections.amazonaws.com` |

### Supported condition key

for repository links

Operations for repository links and sync configuration resources are supported by
the following condition key:

- `codeconnections:Branch`

Filters access by the branch name that is passed in the request.

| Supported actions for condition key | Key                                                                                                                                                | Valid values |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `codeconnections:Branch`            | The following actions are supported for this condition key:<br>• CreateSyncConfiguration<br>• UpdateSyncConfiguration<br>• GetRepositorySyncStatus |

### Supported permissions

for connection sharing

The following IAM operations are used when sharing connections.

```

codeconnections:GetResourcePolicy

```

Use the scroll bars to see the rest of the table.

| AWS CodeConnections required actions for sharing connections | AWS CodeConnections actions                                                                      | Required permissions                                                     | Resources |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | --------- |
| `GetResourcePolicy`                                          | `codeconnections:GetResourcePolicy`<br>Required to access information about the resource policy. | arn:aws:codeconnections:`region`:`account-id`:connection/`connection-id` |

For more information on connection sharing, see [Share connections with AWS accounts](connections-share.md "connections-share.md").

## Using notifications and

connections in the console

The notifications experience is built into the CodeBuild, CodeCommit, CodeDeploy, and CodePipeline
consoles, as well as in the Developer Tools console in the **Settings** navigation
bar itself. To access notifications in the consoles, you must either have one of the
managed policies for those services applied, or you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
AWS CodeStar Notifications and AWS CodeConnections resources in your AWS account. If you create an identity-based policy
that is more restrictive than the minimum required permissions, the console won't
function as intended for entities (IAM users or roles) with that policy. For more
information about granting access to AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline,
including access to those consoles, see the following topics:

- CodeBuild: [Using identity-based policies for CodeBuild](../../../codebuild/latest/userguide/security_iam_id-based-policy-examples.md#managed-policies "../../../codebuild/latest/userguide/security_iam_id-based-policy-examples.md#managed-policies")
- CodeCommit: [Using identity-based policies for CodeCommit](../../../codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md "../../../codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md")
- AWS CodeDeploy: [Identity and access
  management for AWS CodeDeploy](../../../codedeploy/latest/userguide/security-iam.md "../../../codedeploy/latest/userguide/security-iam.md")
- CodePipeline: [Access control with
  IAM policies](../../../codepipeline/latest/userguide/access-control.md "../../../codepipeline/latest/userguide/access-control.md")

AWS CodeStar Notifications does not have any AWS managed policies. To provide access to notification
functionality, you must either apply one of the managed policies for one of the services
listed previously, or you must create policies with the level of permission you want to
grant to users or entities, and then attach those policies to the users, groups, or
roles that require those permissions. For more information and examples, see the
following:

- [Example: An administrator-level policy for managing AWS CodeStar Notifications](security_iam_id-based-policy-examples-notifications.md#security_iam_id-based-policy-examples-notifications-full-access "security_iam_id-based-policy-examples-notifications.md#security_iam_id-based-policy-examples-notifications-full-access")
- [Example: A contributor-level policy for using AWS CodeStar Notifications](security_iam_id-based-policy-examples-notifications.md#security_iam_id-based-policy-examples-notifications-contributor "security_iam_id-based-policy-examples-notifications.md#security_iam_id-based-policy-examples-notifications-contributor")
- [Example: A read-only-level policy for using AWS CodeStar Notifications](security_iam_id-based-policy-examples-notifications.md#security_iam_id-based-policy-examples-notifications-read-only "security_iam_id-based-policy-examples-notifications.md#security_iam_id-based-policy-examples-notifications-read-only").

AWS CodeConnections does not have any AWS managed policies. You use the permissions and
combinations of permissions for access, such as the permissions detailed in [Permissions for
completing connections](#permissions-reference-connections-handshake "#permissions-reference-connections-handshake").

For more information, see the following:

- [Example: An administrator-level policy for managing AWS CodeConnections](security_iam_id-based-policy-examples-connections.md#security_iam_id-based-policy-examples-connections-fullaccess "security_iam_id-based-policy-examples-connections.md#security_iam_id-based-policy-examples-connections-fullaccess")
- [Example: A contributor-level policy for using AWS CodeConnections](security_iam_id-based-policy-examples-connections.md#security_iam_id-based-policy-examples-connections-contributor "security_iam_id-based-policy-examples-connections.md#security_iam_id-based-policy-examples-connections-contributor")
- [Example: A read-only-level policy for using AWS CodeConnections](security_iam_id-based-policy-examples-connections.md#security_iam_id-based-policy-examples-connections-readonly "security_iam_id-based-policy-examples-connections.md#security_iam_id-based-policy-examples-connections-readonly")

You don't need to allow console permissions for users that are making calls only to
the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API
operation that you're trying to perform.

## Allow users

to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```
