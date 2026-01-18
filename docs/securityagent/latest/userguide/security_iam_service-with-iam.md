# How AWS Security Agent works with IAM

Before you use IAM to manage access to AWS Security Agent, learn what IAM features are available to use with AWS Security Agent.

| IAM feature                                                                                                                                                                     | AWS Security Agent support |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [Identity-based policies for AWS Security Agent](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes                        |
| [Resource-based policies within AWS Security Agent](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")            | No                         |
| [Policy actions for AWS Security Agent](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes                        |
| [Policy resources for AWS Security Agent](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Partial                    |
| [Policy condition keys for AWS Security Agent](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes                        |
| [Access control lists (ACLs) in AWS Security Agent](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                  | No                         |
| [Attribute-based access control (ABAC) with AWS Security Agent](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                      | No                         |
| [Using temporary credentials with AWS Security Agent](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                          | Yes                        |
| [Forward access sessions for AWS Security Agent](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                   | Yes                        |
| [Service roles for AWS Security Agent](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                             | No                         |
| [Service-linked roles for AWS Security Agent](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | Yes                        |

To get a high-level view of how AWS Security Agent and other AWS services work with IAM, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Identity-based policies for AWS Security Agent

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions.
To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. You can’t specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Identity-based policy examples for AWS Security Agent

To view examples of AWS Security Agent identity-based policies, see [AWS Security Agent identity-based policy examples](security-iam-id-based-policy-examples.md "security-iam-id-based-policy-examples.md").

### Resource-based policies within AWS Security Agent

**Supports resource-based policies:** No

Resource-based policies are JSON policy documents that you attach to a resource.
Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies.
In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions.
You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy.
Principals can include accounts, users, roles, federated users, or AWS Services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy.
Adding a cross-account principal to a resource-based policy is only half of establishing the trust relationship.
When the principal and the resource are in different AWS Accounts, an IAM administrator in the trusted account must also grant the principal entity (user or role) permission to access the resource.
They grant permission by attaching an identity-based policy to the entity.
However, if a resource-based policy grants access to a principal in the same account, no additional identity-based policy is required.
For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the IAM User Guide.

### Policy actions for AWS Security Agent

**Supports actions** Yes

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of an IAM identity-based policy describes the specific action or actions that will be allowed or denied by the policy.
Policy actions usually have the same name as the associated AWS API operation.
The action is used in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Security Agent use the following prefix before the action: `securityagent:`.
For example, to grant someone permission to create an environment with the AWS Security Agent `CreateEnvironment` API operation, you include the `securityagent:CreateEnvironment` action in their policy.
Policy statements must include either an `Action` or `NotAction` element.
AWS Security Agent defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "securityagent:action1",
      "securityagent:action2"
```

You can specify multiple actions using wildcards (\*).
For example, to specify all actions that begin with the word `List`, include the following action:

```
"Action": "securityagent:List*"
```

### Policy resources for AWS Security Agent

**Supports policy resources:** Partial

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies.
Statements must include either a `Resource` or a `NotResource` element.
As a best practice, specify a resource using its Amazon Resource Name (ARN).
You can do this for actions that support a specific resource type, known as _resource-level permissions_.

For actions that don’t support resource-level permissions, such as listing operations, use a wildcard (\*) to indicate that the statement applies to all resources.

```
 "Resource": "*"
```

Some AWS Security Agent API actions support multiple resources.
For example, multiple environments can be referenced when calling the `ListEnvironments` API action.
To specify multiple resources in a single statement, separate the ARNs with commas.

```
 "Resource": [
      "EXAMPLE-RESOURCE-1",
      "EXAMPLE-RESOURCE-2"
```

For example, the AWS Security Agent environment resource has the following ARN:

```
arn:${Partition}:securityagent:${Region}:${Account}:environment/${EnvironmentId}
```

To specify the environments `my-environment-1` and `my-environment-2` in your statement, use the following example ARNs:

```
 "Resource": [
         "arn:aws:securityagent:us-east-1:123456789012:environment/my-environment-1",
         "arn:aws:securityagent:us-east-1:123456789012:environment/my-environment-2"
```

To specify all environments that belong to a specific account, use the wildcard (\*):

```
 "Resource": "arn:aws:securityagent:us-east-1:123456789012:environment/*"
```

### Policy condition keys for AWS Security Agent

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element (or `Condition` block) lets you specify conditions in which a statement is in effect. The `Condition` element is optional. You can create conditional expressions that use [condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys in a single `Condition` element, AWS evaluates them using a logical `AND` operation. If you specify multiple values for a single condition key, AWS evaluates the condition using a logical `OR` operation. All of the conditions must be met before the statement’s permissions are granted.

You can also use placeholder variables when you specify conditions. For example, you can grant an IAM user permission to access a resource only if it is tagged with their IAM user name. For more information, see [IAM policy elements: variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

AWS Security Agent defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

## Access control lists (ACLs) in AWS Security Agent

**Supports ACLs:** No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource.
ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with AWS Security Agent

**Supports ABAC (tags in policies):** No

## Using temporary credentials with AWS Security Agent

**Supports temporary credentials:** Yes

Some AWS Services don’t work when you sign in using temporary credentials.
For additional information, including which AWS Services work with temporary credentials, see [AWS Services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

You are using temporary credentials if you sign in to the AWS Management Console using any method except a user name and password.
For example, when you access AWS using your company’s single sign-on (SSO) link, that process automatically creates temporary credentials.
You also automatically create temporary credentials when you sign in to the console as a user and then switch roles.
For more information about switching roles, see [Switch from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") in the _IAM User Guide_.

You can manually create temporary credentials using the AWS CLI or AWS API.
You can then use those temporary credentials to access AWS.
AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys.
For more information, see [Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md").

## Forward access sessions for AWS Security Agent

**Supports forward access sessions (FAS):** Yes

When you use an IAM user or role to perform actions in AWS, you are considered a principal.
When you use some services, you might perform an action that then initiates another action in a different service.
FAS uses the permissions of the principal calling an AWS Service, combined with the requesting AWS Service to make requests to downstream services.
FAS requests are only made when a service receives a request that requires interactions with other AWS Services or resources to complete.
In this case, you must have permissions to perform both actions.
For policy details when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for AWS Security Agent

**Supports service roles:** No

A service role is an IAM role that a service assumes to perform actions on your behalf.
An IAM administrator can create, modify, and delete a service role from within IAM.
For more information, see [Create a role to delegate permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

## Service-linked roles for AWS Security Agent

**Supports service-linked roles:** Yes

A service-linked role is a type of service role that is linked to an AWS Service.
The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS Account and are owned by the service.
An IAM administrator can view, but not edit the permissions for service-linked roles.
