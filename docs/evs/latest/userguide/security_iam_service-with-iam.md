# How Amazon EVS works with IAM

Before you use IAM to manage access to Amazon EVS, learn what IAM features are available to use with Amazon EVS.

| IAM feature                                                                                                                                                             | Amazon EVS support |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [Identity-based policies for Amazon EVS](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes                |
| [Resource-based policies within Amazon EVS](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")            | No                 |
| [Policy actions for Amazon EVS](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes                |
| [Policy resources for Amazon EVS](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Partial            |
| [Policy condition keys for Amazon EVS](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes                |
| [Access control lists (ACLs) in Amazon EVS](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                  | No                 |
| [Attribute-based access control (ABAC) with Amazon EVS](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                      | Yes                |
| [Using temporary credentials with Amazon EVS](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                          | Yes                |
| [Forward access sessions for Amazon EVS](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                   | Yes                |
| [Service roles for Amazon EVS](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                             | No                 |
| [Service-linked roles for Amazon EVS](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | Yes                |

To get a high-level view of how Amazon EVS and other AWS services work with IAM, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Identity-based policies for Amazon EVS

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions.
To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. You can’t specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Identity-based policy examples for Amazon EVS

To view examples of Amazon EVS identity-based policies, see [Amazon EVS identity-based policy examples](security-iam-id-based-policy-examples.md "security-iam-id-based-policy-examples.md").

### Resource-based policies within Amazon EVS

**Supports resource-based policies:** No

Resource-based policies are JSON policy documents that you attach to a resource.
Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies.
In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions.
You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy.
Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy.
Adding a cross-account principal to a resource-based policy is only half of establishing the trust relationship.
When the principal and the resource are in different AWS accounts, an IAM administrator in the trusted account must also grant the principal entity (user or role) permission to access the resource.
They grant permission by attaching an identity-based policy to the entity.
However, if a resource-based policy grants access to a principal in the same account, no additional identity-based policy is required.
For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the IAM User Guide.

### Policy actions for Amazon EVS

**Supports actions** Yes

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of an IAM identity-based policy describes the specific action or actions that will be allowed or denied by the policy.
Policy actions usually have the same name as the associated AWS API operation.
The action is used in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon EVS use the following prefix before the action: `evs:`.
For example, to grant someone permission to create an environment with the Amazon EVS `CreateEnvironment` API operation, you include the `evs:CreateEnvironment` action in their policy.
Policy statements must include either an `Action` or `NotAction` element.
Amazon EVS defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "evs:action1",
      "evs:action2"
```

You can specify multiple actions using wildcards (\*).
For example, to specify all actions that begin with the word `List`, include the following action:

```
"Action": "evs:List*"
```

To see a list of Amazon EVS actions, see [Actions Defined by Amazon EVS](../../../IAM/latest/UserGuide/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-actions-as-permissions") in the _Service Authorization Reference_.

### Policy resources for Amazon EVS

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

To see a list of Amazon EVS resource types and their ARNs, see [Resources defined by Amazon Elastic VMware Service](../../../service-authorization/latest/reference/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-resources-for-iam-policies") in the _Service Authorization Reference_.
To learn with which actions you can specify the ARN of each resource, see [Actions defined by Amazon Elastic VMware Service](../../../service-authorization/latest/reference/list_amazonelasticvwareservice.md#amazonelasticvmwareservice-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonelasticvwareservice.md#amazonelasticvmwareservice-actions-as-permissions").

Some Amazon EVS API actions support multiple resources.
For example, multiple environments can be referenced when calling the `ListEnvironments` API action.
To specify multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "EXAMPLE-RESOURCE-1",
      "EXAMPLE-RESOURCE-2"
```

For example, the Amazon EVS environment resource has the following ARN:

```
arn:${Partition}:evs:${Region}:${Account}:environment/${EnvironmentId}
```

To specify the environments `my-environment-1` and `my-environment-2` in your statement, use the following example ARNs:

```
"Resource": [
         "arn:aws:evs:us-east-1:123456789012:environment/my-environment-1",
         "arn:aws:evs:us-east-1:123456789012:environment/my-environment-2"
```

To specify all environments that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:evs:us-east-1:123456789012:environment/*"
```

### Policy condition keys for Amazon EVS

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element (or `Condition` block) lets you specify conditions in which a statement is in effect. The `Condition` element is optional. You can create conditional expressions that use [condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys in a single `Condition` element, AWS evaluates them using a logical `AND` operation. If you specify multiple values for a single condition key, AWS evaluates the condition using a logical `OR` operation. All of the conditions must be met before the statement’s permissions are granted.

You can also use placeholder variables when you specify conditions. For example, you can grant an IAM user permission to access a resource only if it is tagged with their IAM user name. For more information, see [IAM policy elements: variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

Amazon EVS defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

All Amazon EC2 actions support the `aws:RequestedRegion` and `ec2:Region` condition keys. For more information, see [Example: Restricting access to a specific region](../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region "../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region").

To see a list of Amazon EVS condition keys, see [Condition Keys for Amazon EVS](../../../IAM/latest/UserGuide/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-policy-keys "../../../IAM/latest/UserGuide/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-policy-keys") in the _Service Authorization Reference_. To learn with which actions and resources you can use a condition key, see [Actions defined by Amazon EVS](../../../IAM/latest/UserGuide/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-actions-as-permissions").

## Access control lists (ACLs) in Amazon EVS

**Supports ACLs:** No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource.
ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with Amazon EVS

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes.
In AWS, these attributes are called tags.
You can attach tags to IAM entities (users or roles) and to many AWS resources.
Tagging entities and resources is the first step of ABAC.
Then you design ABAC policies to allow operations when the principal’s tag matches the tag on the resource that they are trying to access.

ABAC is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome.

You can attach tags to Amazon EVS resources or pass tags in a request to Amazon EVS.
To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/<key-name>`, `aws:RequestTag/<key-name>`, or `aws:TagKeys` condition keys.
For more information about which actions that you can use tags in condition keys with, see [Actions defined by Amazon EVS](../../../IAM/latest/UserGuide/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonelasticvmwareservice.md#amazonelasticvmwareservice-actions-as-permissions") in the _Service Authorization Reference_.

## Using temporary credentials with Amazon EVS

**Supports temporary credentials:** Yes

Some AWS services don’t work when you sign in using temporary credentials.
For additional information, including which AWS services work with temporary credentials, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

You are using temporary credentials if you sign in to the AWS Management Console using any method except a user name and password.
For example, when you access AWS using your company’s single sign-on (SSO) link, that process automatically creates temporary credentials.
You also automatically create temporary credentials when you sign in to the console as a user and then switch roles.
For more information about switching roles, see [Switch from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") in the _IAM User Guide_.

You can manually create temporary credentials using the AWS CLI or AWS API.
You can then use those temporary credentials to access AWS.
AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys.
For more information, see [Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md").

## Forward access sessions for Amazon EVS

**Supports forward access sessions (FAS):** Yes

When you use an IAM user or role to perform actions in AWS, you are considered a principal.
When you use some services, you might perform an action that then initiates another action in a different service.
FAS uses the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services.
FAS requests are only made when a service receives a request that requires interactions with other AWS services or resources to complete.
In this case, you must have permissions to perform both actions.
For policy details when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for Amazon EVS

**Supports service roles:** No

A service role is an IAM role that a service assumes to perform actions on your behalf.
An IAM administrator can create, modify, and delete a service role from within IAM.
For more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

## Service-linked roles for Amazon EVS

**Supports service-linked roles:** Yes

A service-linked role is a type of service role that is linked to an AWS service.
The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service.
An IAM administrator can view, but not edit the permissions for service-linked roles.

For details about creating or managing Amazon EVS service-linked roles, see [Using service-linked roles for Amazon EVS](using-service-linked-roles.md "using-service-linked-roles.md").
