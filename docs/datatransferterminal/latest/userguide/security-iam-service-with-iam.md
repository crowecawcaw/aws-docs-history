

# How Data Transfer Terminal works with IAM
<a name="security-iam-service-with-iam"></a>

Before you use IAM to manage access to Data Transfer Terminal, learn what IAM features are available to use with Data Transfer Terminal.


| IAM feature | Data Transfer Terminal support | 
| --- | --- | 
|  [Identity-based policies](#security-iam-service-with-iam-id-based-policies)  | Yes | 
|  [Resource-based policies](#security-iam-service-with-iam-resource-based-policies)  | No | 
|  [Policy actions](#security-iam-service-with-iam-id-based-policies-actions)  | Yes | 
|  [Policy resources](#security-iam-service-with-iam-id-based-policies-resources)  | Yes | 
|  [Policy condition keys](#security-iam-service-with-iam-id-based-policies-conditionkeys)  | Yes | 
|  [ACLs](#security-iam-service-with-iam-acls)  | No | 
|  [ABAC (tags in policies)](#security-iam-service-with-iam-tags)  | No | 
|  [Temporary credentials](#security-iam-service-with-iam-roles-tempcreds)  | Yes | 
|  [Principal permissions](#security-iam-service-with-iam-principal-permissions)  | No | 
|  [Service roles](#security-iam-service-with-iam-roles-service)  | No | 
|  [Service-linked roles](#security-iam-service-with-iam-roles-service-linked)  | No | 

To get a high-level view of how Data Transfer Terminal and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for Data Transfer Terminal
<a name="security-iam-service-with-iam-id-based-policies"></a>

 **Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. You can’t specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for Data Transfer Terminal
<a name="security-iam-service-with-iam-id-based-policies-examples"></a>

To view examples of Data Transfer Terminal identity-based policies, see [Identity-based policy examples for AWS Data Transfer Terminal](security-iam-id-based-policy-examples.md).

## Resource-based policies within Data Transfer Terminal
<a name="security-iam-service-with-iam-resource-based-policies"></a>

 **Supports resource-based policies:** No

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. Adding a cross-account principal to a resource-based policy is only half of establishing the trust relationship. When the principal and the resource are in different AWS accounts, an IAM administrator in the trusted account must also grant the principal entity (user or role) permission to access the resource. They grant permission by attaching an identity-based policy to the entity. However, if a resource-based policy grants access to a principal in the same account, no additional identity-based policy is required. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Data Transfer Terminal
<a name="security-iam-service-with-iam-id-based-policies-actions"></a>

 **Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Policy actions usually have the same name as the associated AWS API operation. There are some exceptions, such as *permission-only actions* that don’t have a matching API operation. There are also some operations that require multiple actions in a policy. These additional actions are called *dependent actions*.

Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Data Transfer Terminal actions, see [Actions Defined by AWS Data Transfer Terminal](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_your_service.html#your_service-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Data Transfer Terminal use the following prefix before the action:

```
datatransferterminal
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "datatransferterminal:action1",
      "datatransferterminal:action2"
         ]
```

To view examples of Data Transfer Terminal identity-based policies, see [Identity-based policy examples for AWS Data Transfer Terminal](security-iam-id-based-policy-examples.md).

## Policy resources for Data Transfer Terminal
<a name="security-iam-service-with-iam-id-based-policies-resources"></a>

 **Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. Statements must include either a `Resource` or a `NotResource` element. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). You can do this for actions that support a specific resource type, known as *resource-level permissions*.

For actions that don’t support resource-level permissions, such as listing operations, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Data Transfer Terminal resource types and their ARNs, see [Resources Defined by AWS Data Transfer Terminal](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_your_service.html#your_service-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by AWS Data Transfer Terminal](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_your_service.html#your_service-actions-as-permissions).

To view examples of Data Transfer Terminal identity-based policies, see [Identity-based policy examples for AWS Data Transfer Terminal](security-iam-id-based-policy-examples.md).

## Policy condition keys for Data Transfer Terminal
<a name="security-iam-service-with-iam-id-based-policies-conditionkeys"></a>

 **Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element (or `Condition`block) lets you specify conditions in which a statement is in effect. The `Condition` element is optional. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys in a single `Condition` element, AWS evaluates them using a logical `AND` operation. If you specify multiple values for a single condition key, AWS evaluates the condition using a logical `OR` operation. All of the conditions must be met before the statement’s permissions are granted.

You can also use placeholder variables when you specify conditions. For example, you can grant an IAM user permission to access a resource only if it is tagged with their IAM user name. For more information, see [IAM policy elements: variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) in the *IAM User Guide*.

 AWS supports global condition keys and service-specific condition keys. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Data Transfer Terminal condition keys, see [Condition Keys for AWS Data Transfer Terminal](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_your_service.html#your_service-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions Defined by AWS Data Transfer Terminal](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_your_service.html#your_service-actions-as-permissions).

To view examples of Data Transfer Terminal identity-based policies, see [Identity-based policy examples for AWS Data Transfer Terminal](security-iam-id-based-policy-examples.md).

## ACLs in Data Transfer Terminal
<a name="security-iam-service-with-iam-acls"></a>

 **Supports ACLs:** No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Data Transfer Terminal
<a name="security-iam-service-with-iam-tags"></a>

 **Supports ABAC (tags in policies):** No

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes. In AWS, these attributes are called *tags*. You can attach tags to IAM entities (users or roles) and to many AWS resources. Tagging entities and resources is the first step of ABAC. Then you design ABAC policies to allow operations when the principal’s tag matches the tag on the resource that they are trying to access.

ABAC is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/[replaceable]`key-name` `, , or aws:TagKeys condition keys.` If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**. For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*. 

### Using temporary credentials with Data Transfer Terminal
<a name="security-iam-service-with-iam-roles-tempcreds"></a>

 **Supports temporary credentials:** Yes

Some AWS services don’t work when you sign in using temporary credentials. For additional information, including which AWS services work with temporary credentials, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

You are using temporary credentials if you sign in to the AWS Management Console using any method except a user name and password. For example, when you access AWS using your company’s single sign-on (SSO) link, that process automatically creates temporary credentials. You also automatically create temporary credentials when you sign in to the console as a user and then switch roles. For more information about switching roles, see [Switch from a user to an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) in the *IAM User Guide*.

You can manually create temporary credentials using the AWS CLI or AWS API. You can then use those temporary credentials to access AWS. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html).

### Cross-service principal permissions for Data Transfer Terminal
<a name="security-iam-service-with-iam-principal-permissions"></a>

 **Supports forward access sessions (FAS):** No

When you use an IAM user or role to perform actions in AWS, you are considered a principal. When you use some services, you might perform an action that then initiates another action in a different service. FAS uses the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. FAS requests are only made when a service receives a request that requires interactions with other AWS services or resources to complete. In this case, you must have permissions to perform both actions. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html).

### Service roles for Data Transfer Terminal
<a name="security-iam-service-with-iam-roles-service"></a>

 **Supports service roles:** No

A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

**Warning**  
Changing the permissions for a service role might break Data Transfer Terminal functionality. Edit service roles only when Data Transfer Terminal provides guidance to do so.

### Service-linked roles for Data Transfer Terminal
<a name="security-iam-service-with-iam-roles-service-linked"></a>

 **Supports service-linked roles:** No

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles.

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.