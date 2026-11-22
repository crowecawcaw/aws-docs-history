

AWS Well-Architected Agent is in preview release and is subject to change.

# How AWS Well-Architected works with IAM

Before you use IAM to manage access to AWS Well-Architected, learn what IAM features are available to use with AWS Well-Architected.


**IAM features you can use with AWS Well-Architected**  

| IAM feature | AWS Well-Architected Tool | AWS Well-Architected Agent | 
| --- | --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  |  Yes | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes |  Yes | 
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes |  No  | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Yes |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes |  No  | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  |  Yes | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes |  Yes | 

To get a high-level view of how AWS Well-Architected and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## AWS Well-Architected identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

## Resource-based policies within AWS Well-Architected
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

The AWS Well-Architected Tool does not support resource-based policies. AWS Well-Architected Agent supports resource-based policies attached to two resource types:
+ **Agent profile** – Use the `PutAgentProfilePolicy`, `GetAgentProfilePolicy`, and `DeleteAgentProfilePolicy` operations to manage the policy attached to an agent profile. The profile policy controls cross-account access to the profile and its child resources, such as recommendations, goals, and contexts. Only the profile owner can call these operations. The policy must be valid IAM JSON with `Allow`-only statements and no negation condition operators.
+ **Agent recommendation** – Use the `PutAgentRecommendationPolicy`, `GetAgentRecommendationPolicy`, and `DeleteAgentRecommendationPolicy` operations to manage the policy attached to an agent recommendation.

For details about these operations, see the *Service Authorization Reference*.

## Policy actions for AWS Well-Architected
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Well-Architected use the following prefix before the action: `wellarchitected:`. For example, in the AWS Well-Architected Tool, to allow an entity to define a workload, an administrator must attach a policy that allows `wellarchitected:CreateWorkload` actions. Similarly, to prevent an entity from deleting workloads, an administrator can attach a policy that denies `wellarchitected:DeleteWorkload` actions. Policy statements must include either an `Action` or `NotAction` element. AWS Well-Architected defines its own set of actions that describe tasks that you can perform with this service.

To see a list of AWS Well-Architected actions, see [Actions Defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-actions-as-permissions) in the *Service Authorization Reference*.

## Policy resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of AWS Well-Architected resource types and their ARNs, see [Resources defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-actions-as-permissions).

The AWS WA Tool workload resource has the following ARN:

```
arn:${Partition}:wellarchitected:${Region}:${Account}:workload/${ResourceId} 
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

The ARN can be found on the **Workload properties** page for a workload. For example, to specify a specific workload:

```
"Resource": "arn:aws:wellarchitected:{{us-west-2}}:{{123456789012}}:workload/{{11112222333344445555666677778888}}" 
```

To specify all workloads that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:wellarchitected:{{us-west-2}}:{{123456789012}}:workload/*" 
```

AWS Well-Architected Agent defines two additional resource types, the agent profile and the agent recommendation. These resources have the following ARN formats:

```
arn:${Partition}:wellarchitected:${Region}:${Account}:agent-profile/${ProfileName} 
```

```
arn:${Partition}:wellarchitected:${Region}:${Account}:agent-recommendation/${ResourceId} 
```

Some AWS Well-Architected actions, such as those for creating and listing workloads, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

To see a list of AWS Well-Architected resource types and their ARNs, see [Resources Defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-actions-as-permissions).

## Policy condition keys for AWS Well-Architected
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

`wellarchitected:JiraProjectKey` is the only service-specific condition key in AWS Well-Architected. It applies to the AWS Well-Architected Tool, which uses it for the AWS Well-Architected Tool Connector for Jira. AWS Well-Architected Agent defines no service-specific condition keys. Both services support using some global condition keys. To see all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *Service Authorization Reference*.

## ACLs in AWS Well-Architected
<a name="security_iam_service-with-iam-acls"></a>

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Authorization based on AWS Well-Architected tags
<a name="security_iam_service-with-iam-tags"></a>

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with AWS Well-Architected
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for AWS Well-Architected
<a name="security_iam_service-with-iam-principal-permissions"></a>

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

AWS Well-Architected Agent does not use forward access sessions. During resource discovery and recommendation generation, it makes downstream calls under IAM roles rather than a forwarded customer session: where you supply an execution role, AWS WA Agent assumes that execution role and then a per-account access role from it; for an organizational profile with no execution role, it assumes the `` service-linked role in the member account. The downstream calls carry the permissions of those roles. For the full role model, see [AWS Well-Architected Agent access model](security-iam-agent.md).

## Service roles for AWS Well-Architected
<a name="security_iam_service-with-iam-roles-service"></a>

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

The AWS Well-Architected Tool does not use service roles. AWS Well-Architected Agent uses a customer-managed execution role that you pass to the service when you create an agent profile. AWS WA Agent assumes this execution role to orchestrate cross-account resource discovery, and a pass-role check during profile creation validates that the caller has permission to pass the role to the service. For details about the execution role, the pass-role model, and the cross-account role chain, see [AWS Well-Architected Agent access model](security-iam-agent.md).

## Service-linked roles for AWS Well-Architected
<a name="security_iam_service-with-iam-roles-service-linked"></a>

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

AWS Well-Architected uses service-linked roles for both services under the brand. The AWS Well-Architected Tool uses the `AWSServiceRoleForWellArchitected` service-linked role for organization sharing, and AWS Well-Architected Agent uses two service-linked roles: the `` role for resource scanning and the `` role for AWS Organizations access. For details about creating or managing these service-linked roles, see [Using service-linked roles for AWS Well-Architected](using-service-linked-roles.md).