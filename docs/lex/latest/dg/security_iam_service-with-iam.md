End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# How Amazon Lex works with IAM

Before you use IAM to manage access to Amazon Lex, learn what IAM features are
available to use with Amazon Lex.

| IAM features you can use with Amazon Lex                                                                                                                                    | IAM feature | Amazon Lex support |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------ |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                                              | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")                                  | No          |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                                       | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")                                 | Yes         |
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                                           | No          |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                                     | Partial     |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                                                 | Yes         |
| [Principal permissions](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                                        | Yes         |
| [Service<br>roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                                             | Yes         |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                                           | Yes         |

To get a high-level view of how Amazon Lex and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based

policies for Amazon Lex

**Supports identity-based policies:**

Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

###

Identity-based policy examples for Amazon Lex

To view examples of Amazon Lex identity-based policies, see [Identity-based policy
examples for Amazon Lex](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based

policies within Amazon Lex

**Supports resource-based policies:**

No

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are
IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service
administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions
a specified principal can perform on that resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals
can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities
in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
_IAM User Guide_.

## Policy actions

for Amazon Lex

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Amazon Lex actions, see [Actions defined by Amazon Lex](../../../service-authorization/latest/reference/list_amazonlex.md#your_service-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonlex.md#your_service-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in Amazon Lex use the following prefix before the action:

```
lex
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "lex:`action1`",
      "lex:`action2`"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
"Action": "lex:Describe*"
```

## Policy

resources for Amazon Lex

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

An Amazon Lex bot resource ARN has the following format.

```
arn:aws:lex:${Region}:${Account}:bot:${Bot-Name}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service
Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `OrderFlowers` bot in
your statement, use the following ARN.

```
"Resource": "arn:aws:lex:us-east-2:123456789012:bot:OrderFlowers"
```

To specify all bots that belong to a specific account, use the
wildcard (\*).

```
"Resource": "arn:aws:lex:us-east-2:123456789012:bot:*"
```

Some Amazon Lex actions, such as those for creating
resources, can't be performed on a specific resource. In those
cases, you must use the wildcard, (\*).

```
"Resource": "*"
```

To see a list of Amazon Lex resource types and their ARNs, see
[Resources defined by Amazon Lex](../../../service-authorization/latest/reference/list_amazonlex.md#your_service-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonlex.md#your_service-resources-for-iam-policies") in the _Service Authorization Reference_. To learn with
which actions you can specify the ARN of each resource, see
[Actions defined by Amazon Lex](../../../service-authorization/latest/reference/list_amazonlex.md#your_service-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonlex.md#your_service-actions-as-permissions").

## Policy

condition keys for Amazon Lex

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Amazon Lex condition keys, see [Condition keys for Amazon Lex](../../../service-authorization/latest/reference/list_amazonlex.md#your_service-policy-keys "../../../service-authorization/latest/reference/list_amazonlex.md#your_service-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and resources you
can use a condition key, see [Actions defined by Amazon Lex](../../../service-authorization/latest/reference/list_amazonlex.md#your_service-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonlex.md#your_service-actions-as-permissions").

The following table lists the Amazon Lex condition keys
that apply to Amazon Lex resources. You can include these
keys in `Condition` elements in an IAM permissions
policy.

| Amazon Lex Condition Key  | Description                                                                                                   | Value Type       | Permission                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------- |
| `lex:associatedIntents`   | Scopes the set of intents that can be used when<br>creating or modifying the definition of a<br>bot.          | Array of strings | `lex:PutBot`                                                                                             |
| `lex:associatedSlotTypes` | Scopes the set of slot types that can be used<br>when creating or modifying the definition of a<br>slot type. | Array of strings | `lex:PutIntent`                                                                                          |
| `lex:ChannelType`         | Scopes the type of bot channel association that<br>a user can create, get, or delete.                         | String           | `lex:CreateBotChannelAssociation`<br>`lex:DeleteBotChannelAssociation`<br>`lex:GetBotChannelAssociation` |

## ACLs in Amazon Lex

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Amazon Lex

**Supports ABAC (tags in policies):**

Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

You can associate tags with certain types of Amazon Lex
resources for authorization. To control access based on tags,
provide tag information in the condition element of a policy by
using the `lex:ResourceTag/${TagKey}`,
`aws:RequestTag/${TagKey}`, or
`aws:TagKeys` condition keys.

For more information about tagging Amazon Lex
resources, see [Tagging Your Amazon Lex Resources](how-it-works-tags.md "how-it-works-tags.md").

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [Use a Tag to Access a Resource](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tag "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tag").

The following table lists the actions and corresponding resource
types for tag-based access control. Each action is authorized based
on the tags associated with the corresponding resource type.

| Action                                                                                                 | Resource type          | Condition keys                                    | Notes                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ---------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CreateBotVersion](API_CreateBotVersion.md "API_CreateBotVersion.md")                                  | bot                    | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [DeleteBot](API_DeleteBot.md "API_DeleteBot.md")                                                       | bot                    | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [DeleteBotAlias](API_DeleteBotAlias.md "API_DeleteBotAlias.md")                                        | alias                  | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [DeleteBotChannelAssociation](API_DeleteBotChannelAssociation.md "API_DeleteBotChannelAssociation.md") | channel                | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [DeleteBotVersion](API_DeleteBotVersion.md "API_DeleteBotVersion.md")                                  | bot                    | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [DeleteSession](API_runtime_DeleteSession.md "API_runtime_DeleteSession.md")                           | bot or alias           | `lex:ResourceTag`                                 | Uses tags associated with the bot when alias is set<br>to `$LATEST`. Uses tags associated with the<br>specified alias when used with other aliases.                              |
| [DeleteUtterances](API_DeleteUtterances.md "API_DeleteUtterances.md")                                  | bot                    | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [GetBot](API_GetBot.md "API_GetBot.md")                                                                | bot or alias           | `lex:ResourceTag`                                 | Uses tags associated with the bot when<br>`versionOrAlias` is set to<br>`$LATEST` or numeric version. Uses tags<br>associated with the specified alias when used with<br>aliases |
| [GetBotAlias](API_GetBotAlias.md "API_GetBotAlias.md")                                                 | alias                  | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [GetBotChannelAssociation](API_GetBotChannelAssociation.md "API_GetBotChannelAssociation.md")          | chanel                 | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [GetBotChannelAssociations](API_GetBotChannelAssociations.md "API_GetBotChannelAssociations.md")       | chanel                 | `lex:ResourceTag`                                 | Uses tags associated with the bot when alias is set<br>to "-". Uses tags associated with the specified alias<br>when a bot alias is specified                                    |
| [GetBotVersions](API_GetBotVersions.md "API_GetBotVersions.md")                                        | bot                    | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [GetExport](API_GetExport.md "API_GetExport.md")                                                       | bot                    | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [GetSession](API_runtime_GetSession.md "API_runtime_GetSession.md")                                    | bot or alias           | `lex:ResourceTag`                                 | Uses tags associated with the bot when alias is set<br>to `$LATEST`. Uses tags associated with the<br>specified alias when used with other aliases.                              |
| [GetUtterancesView](API_GetUtterancesView.md "API_GetUtterancesView.md")                               | bot                    | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [ListTagsForResource](API_ListTagsForResource.md "API_ListTagsForResource.md")                         | bot, alias, or channel | `lex:ResourceTag`                                 |                                                                                                                                                                                  |
| [PostContent](API_runtime_PostContent.md "API_runtime_PostContent.md")                                 | bot or alias           | `lex:ResourceTag`                                 | Uses tags associated with the bot when alias is set<br>to `$LATEST`. Uses tags associated with the<br>specified alias when used with other aliases.                              |
| [PostText](API_runtime_PostText.md "API_runtime_PostText.md")                                          | bot or alias           | `lex:ResourceTag`                                 | Uses tags associated with the bot when alias is set<br>to `$LATEST`. Uses tags associated with the<br>specified alias when used with other aliases.                              |
| [PutBot](API_PutBot.md "API_PutBot.md")                                                                | bot                    | `lex:ResourceTag, aws:RequestTag,<br>aws:TagKeys` |                                                                                                                                                                                  |
| [PutBotAlias](API_PutBotAlias.md "API_PutBotAlias.md")                                                 | alias                  | `lex:ResourceTag, aws:RequestTag,<br>aws:TagKeys` |                                                                                                                                                                                  |
| [PutSession](API_runtime_PutSession.md "API_runtime_PutSession.md")                                    | bot or alias           | `lex:ResourceTag`                                 | Uses tags associated with the bot when alias is set<br>to `$LATEST`. Uses tags associated with the<br>specified alias when used with other aliases.                              |
| [StartImport](API_StartImport.md "API_StartImport.md")                                                 | bot                    | `lex:ResourceTag`                                 | Relies on access policy for the `PutBot`<br>operation. Tags and permissions specific to the<br>`StartImport` operation are<br>ignored.                                           |
| [TagResource](API_TagResource.md "API_TagResource.md")                                                 | bot, alias, or channel | `lex:ResourceTag, aws:RequestTag,<br>aws:TagKeys` |                                                                                                                                                                                  |
| [UntagResource](API_UntagResource.md "API_UntagResource.md")                                           | bot, alias, or channel | `lex:ResourceTag, aws:RequestTag,<br>aws:TagKeys` |                                                                                                                                                                                  |

## Using temporary

credentials with Amazon Lex

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

You can use temporary credentials to sign in with federation,
assume an IAM role, or to assume a cross-account role. You
obtain temporary security credentials by calling AWS STS API
operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

## Cross-service

principal permissions for Amazon Lex

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for

Amazon Lex

**Supports service roles:**

Yes

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break Amazon Lex functionality.
Edit service roles only when Amazon Lex provides guidance to do so.

### Choosing an IAM role

in Amazon Lex

Amazon Lex uses service-linked roles to call Amazon Comprehend and Amazon Polly. It
uses resource-level permissions on your AWS Lambda functions to
invoke them.

You must provide an IAM role to enable conversation tagging.
For more information, see [Creating an IAM Role and
Policies for Conversation Logs](conversation-logs-policies.md#conversation-logs-role-and-policy "conversation-logs-policies.md#conversation-logs-role-and-policy").

## Service-linked

roles for Amazon Lex

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing Amazon Lex service-linked roles, see [Using Service-Linked Roles for
Amazon Lex](using-service-linked-roles.md "using-service-linked-roles.md").
