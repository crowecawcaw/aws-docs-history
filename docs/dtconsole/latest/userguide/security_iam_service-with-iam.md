# How features in the developer tools

console work with IAM

Before you use IAM to manage access to features in the Developer Tools console, you should
understand which IAM features are available to use with it. To get a high-level view
of how notifications and other AWS services work with IAM, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Identity-based
  policies in the developer tools console](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [AWS CodeStar Notifications and AWS CodeConnections resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Identity-based

policies in the developer tools console

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
AWS CodeStar Notifications and AWS CodeConnections support specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions for notifications in the Developer Tools console use the following prefixes
before the action: `codestar-notifications and codeconnections`. For example, to grant
someone permission to view all notification rules in their account, you include
the `codestar-notifications:ListNotificationRules` action in their
policy. Policy statements must include either an `Action` or
`NotAction` element. AWS CodeStar Notifications and AWS CodeConnections defines its own set of
actions that describe tasks that you can perform with this service.

To specify multiple AWS CodeStar Notifications actions in a single statement, separate them with
commas as follows.

```
"Action": [
      "codestar-notifications:*action1*",
      "codestar-notifications:*action2*"
```

To specify multiple AWS CodeConnections actions in a single statement, separate them
with commas as follows.

```
"Action": [
      "codeconnections:*action1*",
      "codeconnections:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `List`, include the following
action.

```
`"Action": "codestar-notifications:List*"`
```

AWS CodeStar Notifications API actions include:

- `CreateNotificationRule`
- `DeleteNotificationRule`
- `DeleteTarget`
- `DescribeNotificationRule`
- `ListEventTypes`
- `ListNotificationRules`
- `ListTagsForResource`
- `ListTargets`
- `Subscribe`
- `TagResource`
- `Unsubscribe`
- `UntagResource`
- `UpdateNotificationRule`

AWS CodeConnections API actions include the following:

- `CreateConnection`
- `DeleteConnection`
- `GetConnection`
- `ListConnections`
- `ListTagsForResource`
- `TagResource`
- `UntagResource`

The following permissions-only actions are required in AWS CodeConnections to complete
the auth handshake:

- `GetIndividualAccessToken`
- `GetInstallationUrl`
- `ListInstallationTargets`
- `StartOAuthHandshake`
- `UpdateConnectionInstallation`

The following permissions-only action is required in AWS CodeConnections to use a
connection:

- `UseConnection`

The following permissions-only action is required in AWS CodeConnections to pass a
connection to a service:

- `PassConnection`

To see a list of AWS CodeStar Notifications and AWS CodeConnections actions, see [Actions Defined by AWS CodeStar Notifications](../../../IAM/latest/UserGuide/list_codestarnotifications.md#codestarnotifications-actions-as-permissions "../../../IAM/latest/UserGuide/list_codestarnotifications.md#codestarnotifications-actions-as-permissions") and [Actions Defined by AWS CodeConnections](../../../IAM/latest/UserGuide/list_codestarconnections.md#codestarconnections-actions-as-permissions "../../../IAM/latest/UserGuide/list_codestarconnections.md#codestarconnections-actions-as-permissions") in the
_IAM User Guide_.

### Resources

AWS CodeStar Notifications and AWS CodeConnections do not support specifying resource ARNs in a policy.

### Condition keys

AWS CodeStar Notifications and AWS CodeConnections define their own sets of condition keys and also support
using some global condition keys. To see all AWS global condition keys, see
[AWS
global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

All AWS CodeStar Notifications actions support the
`codestar-notifications:NotificationsForResource` condition key.
For more information, see [Identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

AWS CodeConnections define the following condition keys
that can be used in the `Condition` element of an IAM policy. You can
use these keys to further refine the conditions under which the policy statement
applies. For more information, see [AWS CodeConnections permissions
reference](security-iam.md#permissions-reference-connections "security-iam.md#permissions-reference-connections").

| Condition keys                                | Description                                                                                                                                                                                                       |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `codeconnections:BranchName`                  | Filters access by the third-party repository branch name                                                                                                                                                          |
| `codeconnections:FullRepositoryId`            | Filters access by the repository that is passed in the request. Applies only to `UseConnection` requests for access to a specific repository                                                                      |
| `codeconnections:InstallationId`              | Filters access by the third-party ID (such as the Bitbucket app installation ID) that is used to update a connection. Allows you to restrict which third-party app installations can be used to make a connection |
| `codeconnections:OwnerId`                     | Filters access by the owner or account ID of the third-party provider                                                                                                                                             |
| `codeconnections:PassedToService`             | Filters access by the service to which the principal is allowed to pass a connection                                                                                                                              |
| `codeconnections:ProviderAction`              | Filters access by the provider action in a `UseConnection` request such as `ListRepositories`.                                                                                                                    |
| `codeconnections:ProviderPermissionsRequired` | Filters access by the type of third-party provider permissions                                                                                                                                                    |
| `codeconnections:ProviderType`                | Filters access by the type of third-party provider passed in the request                                                                                                                                          |
| `codeconnections:ProviderTypeFilter`          | Filters access by the type of third-party provider used to filter results                                                                                                                                         |
| `codeconnections:RepositoryName`              | Filters access by the third-party repository name                                                                                                                                                                 | ### Examples To view examples of AWS CodeStar Notifications and AWS CodeConnections identity-based policies, see [Identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). ## AWS CodeStar Notifications and AWS CodeConnections resource-based policies AWS CodeStar Notifications and AWS CodeConnections do not support resource-based policies. ## Authorization based on tags You can attach tags to AWS CodeStar Notifications and AWS CodeConnections resources or pass tags in a request. To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `codestar-notifications and codeconnections:ResourceTag/`key-name``, `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys. For more information about tagging strategies, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md"). For more information about tagging AWS CodeStar Notifications and AWS CodeConnections resources, see [Tag connections resources](connections-tag.md "connections-tag.md"). To view example identity-based policies for limiting access to a resource based on the tags on that resource, see [Using tags to control access to AWS CodeConnections resources](connections-tag-based-access-control.md "connections-tag-based-access-control.md"). ## IAM roles An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your AWS account that has specific permissions. ### Using temporary credentials You can use temporary credentials to sign in with federation, and assume an IAM role or a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md"). AWS CodeStar Notifications and AWS CodeConnections supports the use of temporary credentials. ### Service-linked roles [Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An IAM administrator can view but not edit the permissions for service-linked roles. AWS CodeStar Notifications supports service-linked roles. For details about creating or managing AWS CodeStar Notifications and AWS CodeConnections service-linked roles, see [Using service-linked roles for AWS CodeStar Notifications](using-service-linked-roles.md "using-service-linked-roles.md"). CodeConnections does not support service-linked roles. |
