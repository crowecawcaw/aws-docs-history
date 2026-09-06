

# How Amazon AppFlow works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon AppFlow, learn what IAM features are available to use with Amazon AppFlow.






**IAM features you can use with Amazon AppFlow**  

| IAM feature | Amazon AppFlow support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Partial | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  No  | 

To get a high-level view of how Amazon AppFlow and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for Amazon AppFlow
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Other required permissions in identity-based policies for Amazon AppFlow
<a name="other-permissions"></a>

Because Amazon AppFlow always encrypts data at rest and in motion, ensure that the user that is creating and running a flow has the following AWS KMS permissions in your identity-based policies.


| Required AWS KMS permission | Description | 
| --- | --- | 
| kms:ListKeys  | Controls permission to view the key ID and Amazon Resource Name (ARN) of all customer master keys (CMKs) in the account. | 
| kms:DescribeKey | Controls permission to view detailed information about a CMK. | 
| kms:ListAliases | Controls permission to view the aliases that are defined in the account. Aliases are optional friendly names that you can associate with CMKs. | 
| kms:CreateGrant  | Controls permission to add a grant to a CMK. You can use grants to add permissions without changing the key policy or IAM policy. | 
|  kms:ListGrants | Controls permission to view all grants for a CMK. | 

For more information about AWS Key Management Service (AWS KMS), see [What is AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) in the *AWS Key Management Service Developer Guide*.

For the complete list of AWS services that are integrated with AWS KMS, see [AWS Service Integration](https://aws.amazon.com/kms/features/#AWS_Service_Integration).

### Identity-based policy examples for Amazon AppFlow
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Amazon AppFlow identity-based policies, see [Identity-based policy examples for Amazon AppFlow](security_iam_id-based-policy-examples.md).

## Resource-based policies within Amazon AppFlow
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Amazon AppFlow
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.



To see a list of Amazon AppFlow actions, see [Actions defined by Amazon AppFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html#amazonappflow-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Amazon AppFlow use the following prefix before the action.

```
appflow
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "appflow:{{CreateConnectorProfile}}",
      "appflow:{{CreateFlow}}"
         ]
```



You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action.

```
"Action": "appflow:Describe*"
```

To view examples of Amazon AppFlow identity-based policies, see [Identity-based policy examples for Amazon AppFlow](security_iam_id-based-policy-examples.md).

## Policy resources for Amazon AppFlow
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Amazon AppFlow resource types and their ARNs, see [Resources defined by Amazon AppFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html#amazonappflow-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by Amazon AppFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html#amazonappflow-actions-as-permissions).





An Amazon AppFlow connector profile has the following Amazon Resource Name (ARN) format.

```
arn:${Partition}:appflow:${Region}:${Account}:connectorprofile/${connector-profile-name}
```

An Amazon AppFlow flow has the following ARN format.

```
arn:${Partition}:appflow:${Region}:${Account}:flow/${flow-name}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify the `test-flow` flow in your statement, use the following ARN.

```
"Resource": "arn:aws:appflow:us-east-1:123456789012:flow/test-flow"
```

To specify all flows that belong to a specific account, use the wildcard (\*).

```
"Resource": "arn:aws:appflow:us-east-1:123456789012:flow/*"
```

Some Amazon AppFlow actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Many Amazon AppFlow API actions involve multiple resources. For example, `DescribeConnectorProfiles` returns a list of details for specified connector profiles that are accessible by the currently logged in AWS account. So an user must have permissions to view those connector profiles. To specify multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "resource1",
      "resource2"
```

To see a list of Amazon AppFlow resource types and their ARNs, see [Resources defined by Amazon AppFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html#amazonappflow-resources-for-iam-policies) in the *IAM User Guide*. To learn about actions with which you can specify the ARN of each resource, see [Actions defined by Amazon AppFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html#amazonappflow-actions-as-permissions).

## Policy condition keys for Amazon AppFlow
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Partial

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element (or `Condition` *block*) lets you specify conditions in which a statement is in effect. The `Condition` element is optional. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys in a single `Condition` element, AWS evaluates them using a logical `AND` operation. If you specify multiple values for a single condition key, AWS evaluates the condition using a logical `OR` operation. All of the conditions must be met before the statement's permissions are granted.

 You can also use placeholder variables when you specify conditions. For example, you can grant a user permission to access a resource only if it is tagged with their user name. For more information, see [IAM policy elements: variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) in the *IAM User Guide*.

Amazon AppFlow does not provide any service-specific condition keys, but it does support using some [global condition keys](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html#amazonappflow-policy-keys). To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

## Access control lists (ACLs) in Amazon AppFlow
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with Amazon AppFlow
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with Amazon AppFlow
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for Amazon AppFlow
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for Amazon AppFlow
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

## Service-linked roles for Amazon AppFlow
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** No 

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 