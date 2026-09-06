

# How Amazon RDS works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon RDS, you should understand what IAM features are available to use with Amazon RDS.

The following table lists IAM features you can use with Amazon RDS:


| IAM feature | Amazon RDS support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) | Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) | No | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) | Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) | Yes | 
| [Policy condition keys (service-specific)](#UsingWithRDS.IAM.Conditions) | Yes | 
| [ACLs](#security_iam_service-with-iam-acls) | No | 
| [Attribute-based access control (ABAC) (tags in policies)](#security_iam_service-with-iam-tags) | Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) | Yes | 
| [Forward access sessions](#security_iam_service-with-iam-principal-permissions) | Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) | Yes | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) | Yes | 

To get a high-level view of how Amazon RDS and other AWS services work with IAM, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Amazon RDS identity-based policies](#security_iam_service-with-iam-id-based-policies)
+ [Resource-based policies within Amazon RDS](#security_iam_service-with-iam-resource-based-policies)
+ [Policy actions for Amazon RDS](#security_iam_service-with-iam-id-based-policies-actions)
+ [Policy resources for Amazon RDS](#security_iam_service-with-iam-id-based-policies-resources)
+ [Policy condition keys for Amazon RDS](#UsingWithRDS.IAM.Conditions)
+ [Access control lists (ACLs) in Amazon RDS](#security_iam_service-with-iam-acls)
+ [Attribute-based access control (ABAC) in policies with Amazon RDS tags](#security_iam_service-with-iam-tags)
+ [Using temporary credentials with Amazon RDS](#security_iam_service-with-iam-roles-tempcreds)
+ [Forward access sessions for Amazon RDS](#security_iam_service-with-iam-principal-permissions)
+ [Service roles for Amazon RDS](#security_iam_service-with-iam-roles-service)
+ [Service-linked roles for Amazon RDS](#security_iam_service-with-iam-roles-service-linked)

## Amazon RDS identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes.

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for Amazon RDS
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To view examples of Amazon RDS identity-based policies, see [Identity-based policy examples for Amazon RDS](security_iam_id-based-policy-examples.md).

## Resource-based policies within Amazon RDS
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No.

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Amazon RDS
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes.

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon RDS use the following prefix before the action: `rds:`. For example, to grant someone permission to describe DB instances with the Amazon RDS `DescribeDBInstances` API operation, you include the `rds:DescribeDBInstances` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Amazon RDS defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows.

```
"Action": [
      "rds:action1",
      "rds:action2"
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action.

```
"Action": "rds:Describe*"
```



To see a list of Amazon RDS actions, see [Actions Defined by Amazon RDS](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html#amazonrds-actions-as-permissions) in the *Service Authorization Reference*.

## Policy resources for Amazon RDS
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes.

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The DB instance resource has the following Amazon Resource Name (ARN).

```
arn:${Partition}:rds:${Region}:${Account}:{ResourceType}/${Resource}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS service namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify the `dbtest` DB instance in your statement, use the following ARN.

```
"Resource": "arn:aws:rds:us-west-2:123456789012:db:dbtest"
```

To specify all DB instances that belong to a specific account, use the wildcard (\*).

```
"Resource": "arn:aws:rds:us-east-1:123456789012:db:*"
```

Some RDS API operations, such as those for creating resources, can't be performed on a specific resource. In those cases, use the wildcard (\*).

```
"Resource": "*"
```

Many Amazon RDS API operations involve multiple resources. For example, `CreateDBInstance` creates a DB instance. You can specify that an user must use a specific security group and parameter group when creating a DB instance. To specify multiple resources in a single statement, separate the ARNs with commas. 

```
"Resource": [
      "resource1",
      "resource2"
```

To see a list of Amazon RDS resource types and their ARNs, see [Resources Defined by Amazon RDS](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html#amazonrds-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by Amazon RDS](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html#amazonrds-actions-as-permissions).

## Policy condition keys for Amazon RDS
<a name="UsingWithRDS.IAM.Conditions"></a>

**Supports service-specific policy condition keys:** Yes.

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Amazon RDS defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.



 All RDS API operations support the `aws:RequestedRegion` condition key. 

To see a list of Amazon RDS condition keys, see [Condition Keys for Amazon RDS](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html#amazonrds-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions Defined by Amazon RDS](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html#amazonrds-actions-as-permissions).

## Access control lists (ACLs) in Amazon RDS
<a name="security_iam_service-with-iam-acls"></a>

**Supports access control lists (ACLs):** No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) in policies with Amazon RDS tags
<a name="security_iam_service-with-iam-tags"></a>

**Supports attribute-based access control (ABAC) tags in policies:** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

For more information about tagging Amazon RDS resources, see [Specifying conditions: Using custom tags](UsingWithRDS.IAM.SpecifyingCustomTags.md). To view an example identity-based policy for limiting access to a resource based on the tags on that resource, see [Grant permission for actions on a resource with a specific tag with two different values](security_iam_id-based-policy-examples-create-and-modify-examples.md#security_iam_id-based-policy-examples-grant-permissions-tags).

## Using temporary credentials with Amazon RDS
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes.

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Forward access sessions for Amazon RDS
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions:** Yes.

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for Amazon RDS
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** Yes.

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

**Warning**  
Changing the permissions for a service role might break Amazon RDS functionality. Edit service roles only when Amazon RDS provides guidance to do so.

## Service-linked roles for Amazon RDS
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes.

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about using Amazon RDS service-linked roles, see [Using service-linked roles for Amazon RDS](UsingWithRDS.IAM.ServiceLinkedRoles.md).