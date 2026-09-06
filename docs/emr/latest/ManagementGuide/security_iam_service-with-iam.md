

# How Amazon EMR works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon EMR, learn what IAM features are available to use with Amazon EMR.


**IAM features you can use with Amazon EMR**  

| IAM feature | Amazon EMR support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  Yes | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) | Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) | No | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) | Yes | 

To get a high-level view of how Amazon EMR and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for Amazon EMR
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for Amazon EMR
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Amazon EMR identity-based policies, see [Amazon EMR identity-based policy examples](security_iam_id-based-policy-examples.md).

## Resource-based policies within Amazon EMR
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** Yes

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Amazon EMR
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.



To see a list of Amazon EMR actions, see [Actions, resources, and condition keys for Amazon EMR](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonemroneksemrcontainers.html) in the *Service Authorization Reference*.

Policy actions in Amazon EMR use the following prefix before the action:

```
EMR
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "EMR:{{action1}}",
      "EMR:{{action2}}"
         ]
```





To view examples of Amazon EMR identity-based policies, see [Amazon EMR identity-based policy examples](security_iam_id-based-policy-examples.md).

## Policy resources for Amazon EMR
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Amazon EMR resource types and their ARNs, see [Resources Defined by Amazon EMR](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticmapreduce.html#amazonelasticmapreduce-resources-for-iam-policies) in the *Service Authorization Reference*. To learn which actions you can specify the ARN of each resource, see [Actions, resources, and condition keys for Amazon EMR](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonemroneksemrcontainers.html).





To view examples of Amazon EMR identity-based policies, see [Amazon EMR identity-based policy examples](security_iam_id-based-policy-examples.md).

## Policy condition keys for Amazon EMR
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Amazon EMR condition keys and to learn which actions and resources you can use a condition key, see [Actions, resources, and condition keys for Amazon EMR](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonemroneksemrcontainers.html) in the *Service Authorization Reference*. 

To view examples of Amazon EMR identity-based policies, see [Amazon EMR identity-based policy examples](security_iam_id-based-policy-examples.md).

## Access control lists (ACLs) in Amazon EMR
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with Amazon EMR
<a name="security_iam_service-with-iam-tags"></a>


|  |  | 
| --- |--- |
| Supports ABAC (tags in policies) | Yes | 

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using Temporary credentials with Amazon EMR
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for Amazon EMR
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for Amazon EMR
<a name="security_iam_service-with-iam-roles-service"></a>


|  |  | 
| --- |--- |
| Supports service roles | No | 

## Service-linked roles for Amazon EMR
<a name="security_iam_service-with-iam-roles-service-linked"></a>


|  |  | 
| --- |--- |
| Supports service-linked roles | Yes | 

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.

## Use cluster and Notebook tags with IAM policies for access control
<a name="emr-tag-based-access"></a>

Permission for Amazon EMR actions associated with EMR Notebooks and EMR clusters can be fine-tuned using tag-based access control with identity-based IAM policies. You can use *condition keys* within a `Condition` element (also called a `Condition` block) to allow certain actions only when a notebook, cluster, or both has a certain tag key or key-value combination. You can also limit the `CreateEditor` action (which creates an EMR notebook) and the `RunJobFlow` action (which creates a cluster) so that a request for a tag must be submitted when the resource is created.

In Amazon EMR, the condition keys that can be used in a `Condition` element apply only to those Amazon EMR API actions where `ClusterID` or `NotebookID` is a required request parameter. For example, the [ModifyInstanceGroups](https://docs.aws.amazon.com/ElasticMapReduce/latest/API/API_ModifyInstanceGroups.html) action does not support context keys because `ClusterID` is an optional parameter.

When you create an EMR notebook, a default tag is applied with a key string of `creatorUserId` set to the value of the IAM user ID who created the notebook. This is useful for limiting allowed actions for the notebook only to the creator.

The following condition keys are available in Amazon EMR:
+ Use the `elasticmapreduce:ResourceTag/{{TagKeyString}}` condition context key to allow or deny user actions on clusters or notebooks with tags that have the `{{TagKeyString}}` that you specify. If an action passes both `ClusterID` and `NotebookID`, the condition applies to both the cluster and the notebook. This means that both resources must have the tag key string or key-value combination that you specify. You can use the `Resource` element to limit the statement so that it applies only to clusters or notebooks as required. For more information, see [Amazon EMR identity-based policy examples](security_iam_id-based-policy-examples.md).
+ Use the `elasticmapreduce:RequestTag/{{TagKeyString}}` condition context key to require a specific tag with actions/API calls. For example, you can use this condition context key along with the `CreateEditor` action to require that a key with `{{TagKeyString}}` is applied to a notebook when it is created.

## Examples
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To see a list of Amazon EMR actions, see [Actions Defined by Amazon EMR](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticmapreduce.html#amazonelasticmapreduce-actions-as-permissions) in the *IAM User Guide*.