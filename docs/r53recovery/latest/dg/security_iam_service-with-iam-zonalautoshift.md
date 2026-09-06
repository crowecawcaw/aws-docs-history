

# How zonal autoshift in ARC works with IAM
<a name="security_iam_service-with-iam-zonalautoshift"></a>

Before you use IAM to manage access to zonal autoshift in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with zonal autoshift.


**IAM features that you can use with zonal autoshift in ARC**  

| IAM feature | Zonal autoshift support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-zonalautoshift-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-zonalautoshift-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-zonalautoshift-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-zonalautoshift-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-zonalautoshift-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-zonalautoshift-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-zonalautoshift-tags) |  Partial | 
| [Temporary credentials](#security_iam_service-with-iam-zonalautoshift-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-zonalautoshift-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-zonalautoshift-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-zonalautoshift-roles-service-linked) |  Yes | 

To get a high-level, overall view of how AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for ARC
<a name="security_iam_service-with-iam-zonalautoshift-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

To view examples of ARC identity-based policies, see [Identity-based policy examples in Amazon Application Recovery Controller (ARC)](security_iam_id-based-policy-examples.md).

## Resource-based policies within ARC
<a name="security_iam_service-with-iam-zonalautoshift-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

## Policy actions for ARC
<a name="security_iam_service-with-iam-zonalautoshift-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of ARC actions for zonal autoshift, see [ Actions defined by Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in ARC for zonal autoshift use the following prefixes before the action:

```
arc-zonal-shift
```

To specify multiple actions in a single statement, separate them with commas. For example, the following:

```
"Action": [
      "arc-zonal-shift:{{action1}}",
      "arc-zonal-shift:{{action2}}"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "arc-zonal-shift:Describe*"
```

To view examples of ARC identity-based policies for zonal autoshift, see [Identity-based policy examples for zonal autoshift in ARC](security_iam_id-based-policy-examples-zonalautoshift.md).

## Policy resources for zonal autoshift in ARC
<a name="security_iam_service-with-iam-zonalautoshift-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of resource types and their ARNs, and the actions that you can specify with the ARN of each resource, see the following topic in the *Service Authorization Reference*:
+ [ Actions defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions)

To see the actions and resources that you can use with a condition key, see the following topic in the *Service Authorization Reference*:
+ [ Condition keys defined by Amazon Route 53 - Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html#amazonroute53applicationrecoverycontroller-zonalshift-policy-keys)

To view examples of ARC identity-based policies for zonal autoshift, see [Identity-based policy examples for zonal autoshift in ARC](security_iam_id-based-policy-examples-zonalautoshift.md).

## Policy condition keys for zonal autoshift in ARC
<a name="security_iam_service-with-iam-zonalautoshift-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of ARC condition keys for zonal autoshift, see the following topics in the *Service Authorization Reference*:
+ [ Condition keys for Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html#amazonroute53applicationrecoverycontroller-zonalshift-policy-keys)

To see the actions and resources that you can use with a condition key, see the following topics in the *Service Authorization Reference*:
+ [ Actions defined by Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html#amazonroute53applicationrecoverycontroller-zonalshift-actions-as-permissions)

To view examples of ARC identity-based policies for zonal autoshift, see [Identity-based policy examples for zonal autoshift in ARC](security_iam_id-based-policy-examples-zonalautoshift.md).

## Access control lists (ACLs) in ARC
<a name="security_iam_service-with-iam-zonalautoshift-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with ARC
<a name="security_iam_service-with-iam-zonalautoshift-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

Zonal autoshift in ARC includes the following partial support for ABAC: 
+ Zonal autoshift supports ABAC for managed resources that are registered in ARC for zonal shift. For more information about ABAC for Network Load Balancer and Application Load Balancer managed resources, see [ ABAC with Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags) in the Elastic Load Balancing User Guide.

## Using temporary credentials with ARC
<a name="security_iam_service-with-iam-zonalautoshift-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for ARC
<a name="security_iam_service-with-iam-zonalautoshift-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

When you use an IAM entity (user or role) to perform actions in AWS, you are considered a principal. Policies grant permissions to a principal. When you use some services, you might perform an action that then triggers another action in a different service. In this case, you must have permissions to perform both actions.

To see whether an action requires additional dependent actions in a policy, see the following topic in the *Service Authorization Reference*:
+ [ Amazon Route 53 Zonal Shift](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html)

## Service roles for ARC
<a name="security_iam_service-with-iam-zonalautoshift-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

## Service-linked roles for ARC
<a name="security_iam_service-with-iam-zonalautoshift-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing ARC service-linked roles, see [Using the service-linked role for zonal autoshift in ARC](using-service-linked-roles-zonal-autoshift.md).

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.