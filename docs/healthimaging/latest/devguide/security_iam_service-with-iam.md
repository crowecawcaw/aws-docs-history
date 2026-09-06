

# How AWS HealthImaging works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to HealthImaging, learn what IAM features are available to use with HealthImaging.






**IAM features you can use with AWS HealthImaging**  

| IAM feature | HealthImaging support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Partial | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  Yes | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes | 

To get a high-level view of how HealthImaging and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for HealthImaging
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

HealthImaging supports condition statements that specify DICOM Study and Series UIDs, enabling access control scoped to one or more DICOM Study or Series.

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for HealthImaging
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of HealthImaging identity-based policies, see [Identity-based policy examples for AWS HealthImaging](security_iam_id-based-policy-examples.md).

## Resource-based policies within HealthImaging
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for HealthImaging
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.



To see a list of HealthImaging actions, see [ Actions defined by AWS HealthImaging](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html#awshealthimaging-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in HealthImaging use the following prefix before the action:

```
medical-imaging
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "medical-imaging:action1",
      "medical-imaging:action2"
         ]
```





To view examples of HealthImaging identity-based policies, see [Identity-based policy examples for AWS HealthImaging](security_iam_id-based-policy-examples.md).

## Policy resources for HealthImaging
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of HealthImaging resource types and their ARNs, see [ Resource types defined by AWS HealthImaging](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html#awshealthimaging-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions and resources you can use an ARN, see [ Actions defined by AWS HealthImaging](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html#awshealthimaging-actions-as-permissions).





To view examples of HealthImaging identity-based policies, see [Identity-based policy examples for AWS HealthImaging](security_iam_id-based-policy-examples.md).

## Policy condition keys for HealthImaging
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of HealthImaging condition keys, see [ Condition keys for AWS HealthImaging](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html#awshealthimaging-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [ Actions defined by AWS HealthImaging](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html#awshealthimaging-actions-as-permissions).

To view examples of HealthImaging identity-based policies, see [Identity-based policy examples for AWS HealthImaging](security_iam_id-based-policy-examples.md).

## ACLs in HealthImaging
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## RBAC with HealthImaging
<a name="security_iam_service-with-iam-tags-rbac"></a>


|  |  | 
| --- |--- |
| Supports RBAC | Yes | 

The traditional authorization model used in IAM is called role-based access control (RBAC). RBAC defines permissions based on a person's job function, known outside of AWS as a *role*. For more information, see [Comparing ABAC to the traditional RBAC model](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html#introduction_attribute-based-access-control_compare-rbac) in the *IAM User Guide*.

## ABAC with HealthImaging
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Partial

**Warning**  
ABAC is not enforced via the `SearchImageSets` API action. Anyone who has access to the `SearchImageSets` action can access all metadata for image sets in a data store.

**Note**  
Image sets are a child resource of data stores. To use ABAC, an image set must have the same tag as a data store. For more information, refer to [Tagging resources with AWS HealthImaging](tagging.md).

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with HealthImaging
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for HealthImaging
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

When you use an IAM user or role to perform actions in AWS, you are considered a principal. Policies grant permissions to a principal. When you use some services, you might perform an action that then triggers another action in a different service. In this case, you must have permissions to perform both actions. To see whether an action requires additional dependent actions in a policy, see [ Actions, resources, and condition keys for AWS HealthImaging](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html) in the *Service Authorization Reference*.

## Service roles for HealthImaging
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** Yes

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

**Warning**  
Changing the permissions for a service role might break HealthImaging functionality. Edit service roles only when HealthImaging provides guidance to do so.

## Service-linked roles for HealthImaging
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

HealthImaging uses service-linked roles to [publish CloudWatch metrics to your account](https://docs.aws.amazon.com/healthimaging/latest/devguide/monitoring-cloudwatch.html#setup-metrics). For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).