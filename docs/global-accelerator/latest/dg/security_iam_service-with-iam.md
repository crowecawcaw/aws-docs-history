

# How AWS Global Accelerator works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Global Accelerator, learn what IAM features are available to use with Global Accelerator.

To see tables showing a similar high-level view of how AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.






**IAM features you can use with AWS Global Accelerator**  

| IAM feature | Global Accelerator support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  Yes | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Partial | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes | 

## Identity-based policies for Global Accelerator
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

To view examples of Global Accelerator identity-based policies, see [Identity-based policy examples for AWS Global Accelerator](security_iam_id-based-policy-examples.md).

## Resource-based policies within Global Accelerator
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

## Policy actions for Global Accelerator
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Global Accelerator actions, see [Actions defined by AWS Global Accelerator](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglobalaccelerator.html#awsglobalaccelerator-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Global Accelerator use the following prefix before the action:

```
globalaccelerator
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "globalaccelerator:{{action1}}",
      "globalaccelerator:{{action2}}"
         ]
```





You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "globalaccelerator:Describe*"
```

To view examples of Global Accelerator identity-based policies, see [Identity-based policy examples for AWS Global Accelerator](security_iam_id-based-policy-examples.md).

## Policy resources for Global Accelerator
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

In the *Service Authorization Reference*, you can see the following information related to Global Accelerator:
+ To see a list of Global Accelerator resource types and their ARNs, see [Resources defined by AWS Global Accelerator](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglobalaccelerator.html#awsglobalaccelerator-resources-for-iam-policies).
+ To learn the actions that you can specify with the ARN of each resource, see [Actions defined by AWS Global Accelerator](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglobalaccelerator.html#awsglobalaccelerator-actions-as-permissions).

To view examples of Global Accelerator identity-based policies, see [Identity-based policy examples for AWS Global Accelerator](security_iam_id-based-policy-examples.md).

## Policy condition keys for Global Accelerator
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Global Accelerator condition keys, see [Condition keys for AWS Global Accelerator](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglobalaccelerator.html#awsglobalaccelerator-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions defined by AWS Global Accelerator](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglobalaccelerator.html#awsglobalaccelerator-actions-as-permissions).

To view examples of Global Accelerator identity-based policies, see [Identity-based policy examples for AWS Global Accelerator](security_iam_id-based-policy-examples.md).

## ACLs in Global Accelerator
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** Yes

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Global Accelerator
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Partial

Global Accelerator has *partial* support for tags in policies. It supports tagging for one resource, accelerators. For more information about using tags in policy statement conditions, and to view an example policy for limiting access to a resource based on tags on the resource, see [Using tag-based policies with AWS Global Accelerator](security_iam-tag-policies.md).

For more information about tagging Global Accelerator resources, see [Tagging in AWS Global Accelerator](tagging-in-global-accelerator.md).

To learn more about using tags in policies, review the following information.

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with Global Accelerator
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for Global Accelerator
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for Global Accelerator
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

## Service-linked role for Global Accelerator
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For more information about the service-linked role for Global Accelerator, see [Service-linked role for AWS Global Accelerator](using-service-linked-roles.md).

For details about creating or managing service-linked roles in general in AWS, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.