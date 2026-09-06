

# How Image Builder works with IAM policies and roles
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Image Builder, learn what IAM features are available to use with Image Builder.

To get a high-level view of how Image Builder and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for Image Builder
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for Image Builder
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Image Builder identity-based policies, see [Image Builder identity-based policies](#security_iam_id-based-policy-examples).

## Resource-based policies within Image Builder
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** Yes

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Image Builder
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.



To see a list of Image Builder actions, see [Actions defined by EC2 Image Builder](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2imagebuilder.html#amazonec2imagebuilder-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Image Builder use the following prefix before the action:

```
imagebuilder
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
	"imagebuilder:{{action1}}",
	"imagebuilder:{{action2}}"
	]
```





To view examples of Image Builder identity-based policies, see [Image Builder identity-based policies](#security_iam_id-based-policy-examples).

## Policy resources for Image Builder
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Image Builder resource types and their ARNs, see [Resources defined by EC2 Image Builder](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2imagebuilder.html#amazonec2imagebuilder-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by EC2 Image Builder](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2imagebuilder.html#amazonec2imagebuilder-actions-as-permissions).

To view examples of Image Builder identity-based policies, see [Image Builder identity-based policies](#security_iam_id-based-policy-examples).

## Policy condition keys for Image Builder
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Image Builder condition keys, see [Condition keys for EC2 Image Builder](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2imagebuilder.html#amazonec2imagebuilder-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions defined by EC2 Image Builder](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2imagebuilder.html#amazonec2imagebuilder-actions-as-permissions).

To view examples of Image Builder identity-based policies, see [Image Builder identity-based policies](#security_iam_id-based-policy-examples).

## ACLs in Image Builder
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Image Builder
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with Image Builder
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for Image Builder
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for Image Builder
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** Yes

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

**Warning**  
Changing the permissions for a service role might break Image Builder functionality. Edit service roles only when Image Builder provides guidance to do so.

## Service-linked roles for Image Builder
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about the Image Builder service-linked role, see [Use IAM service-linked roles for Image Builder](image-builder-service-linked-role.md).

## Image Builder identity-based policies
<a name="security_iam_id-based-policy-examples"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources, and also the conditions under which actions are allowed or denied. Image Builder supports specific actions, resources, and condition keys. For information about all of the elements that you use in a JSON policy, see [Actions, Resources, and Condition Keys for Amazon EC2 Image Builder](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonec2imagebuilder.html) in the *IAM User Guide*.

### Actions
<a name="sec-iam-ib-id-based-policies-actions"></a>

Policy actions in Image Builder use the following prefix before the action: `imagebuilder:`. Policy statements must include either an `Action` or `NotAction` element. Image Builder defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
	"imagebuilder:action1",
	"imagebuilder:action2"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `List`, include the following action:

```
"Action": "imagebuilder:List*"
```

To see a list of Image Builder actions, see [Actions, Resources, and Condition Keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) in the *IAM User Guide*.

### Managing access using policies
<a name="security-iam-manage-access"></a>

For detailed information about how to manage access in AWS by creating policies and attaching them to IAM identities or AWS resources, see [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*. 

The IAM role that you associate with your instance profile must have permissions to run the build and test components included in your image. The following IAM role policies must be attached to the IAM role that is associated with the instance profile:
+ EC2InstanceProfileForImageBuilder
+ EC2InstanceProfileForImageBuilderECRContainerBuilds
+ AmazonSSMManagedInstanceCore

### Resources
<a name="sec-iam-ib-id-based-policies-resources"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The ARN is made up of multiple nodes that help identify the resource and ensure that the name is unique. The last nodes in the name include several variations in formatting for the resource type, name, and ID. When Image Builder creates a resource it uses the following format:

`arn:aws:imagebuilder:{{region}}:{{owner}}:{{resource-type/resource-name/version/build-version}}`

**Note**  
The build version is not always included in the resource ARN. However, some API operations, such as [GetComponent](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetComponent.html), need the build version to uniquely identify a resource to retrieve.

For the resources that Image Builder uses in its recipes, such as the base image or components, the owner node can be one of the following:
+ The account number of the resource owner
+ For Amazon managed resources: `aws`
+ For AWS Marketplace resources: `aws-marketplace`

The following example shows the ARN for a managed component to install the Amazon CloudWatch agent on Linux:

```
arn:aws:imagebuilder:{{us-east-1}}:aws:component/{{amazon-cloudwatch-agent-linux/1.0.1/1}}
```

This example shows the ARN for a fictitious managed component from the AWS Marketplace:

```
arn:aws:imagebuilder:{{us-east-1}}:aws-marketplace:component/{{example-linux-software-component/1.0.1}}
```

For more information about getting a list of components, including the use of an ownership filter, see [List Image Builder components](component-details.md#list-components).

**Example ARNs**  
The following are some examples of resource ARNs that you might specify in an IAM policy:
+ Instance ARN

  ```
  "Resource": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:instance/{{i-1234567890abcdef0}}"
  ```
+ Wildcard (\*) example to specify all instances for a given account

  ```
  "Resource": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:instance/*"
  ```
+ Wildcard (\*) example to specify all versions of a managed image workflow

  ```
  "Resource": "arn:aws:imagebuilder:{{us-east-1}}:aws:workflow/build/build-image/*"
  ```
+ Managed image ARN

  ```
  "Resource": "arn:aws:imagebuilder:{{us-east-1}}:aws:image/{{amazon-linux-2-arm64/2024.12.17/1}}"
  ```
+ Wildcard (\*) example to specify all versions of a managed image

  ```
  "Resource": "arn:aws:imagebuilder:{{us-east-1}}:aws:image/{{amazon-linux-2-arm64/x.x.x}}"
  ```

Many EC2 Image Builder API actions involve multiple resources. To specify multiple resources in a single statement, separate the ARNs with commas. 

```
"Resource": [
	  "{{resource1}}",
	  "{{resource2}}"
]
```

### Condition keys
<a name="sec-iam-ib-id-based-policies-conditionkeys"></a>

Image Builder provides service-specific condition keys and supports using some global condition keys. To see all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*. The following service-specific condition keys are provided.

#### imagebuilder:CreatedResourceTagKeys
<a name="image-builder-security-createdresourcetagkeys"></a>

Works with [string operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String).

Use this key to filter access by the presence of tag keys in the request. This allows you to manage the resources that Image Builder creates.

**Availability** – This key is available to only the `CreateInfrastrucutreConfiguration` and `UpdateInfrastructureConfiguration` APIs.

#### imagebuilder:CreatedResourceTag/<key>
<a name="image-builder-security-createdresourcetag"></a>

Works with [string operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String).

Use this key to filter access by the tag key-value pairs that are attached to the resource that Image Builder created. This allows you to manage Image Builder resources through defined tags.

**Availability** – This key is available to only the `CreateInfrastrucutreConfiguration` and `UpdateInfrastructureConfiguration` APIs.

#### imagebuilder:LifecyclePolicyResourceType
<a name="image-builder-security-lifecyclepolicyresourcetype"></a>

Works with [string operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String).

Use this key to filter access by the Lifecycle resource type specified in the request.

The value for this key can be either `AMI_IMAGE` or `CONTAINER_IMAGE`.

**Availability** – This key is available to only the `CreateLifecyclePolicy` and `UpdateLifecyclePolicy` APIs.

#### imagebuilder:Ec2MetadataHttpTokens
<a name="image-builder-security-ec2metadatatokens"></a>

Works with [string operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String).

Use this key to filter access by the EC2 Instance Metadata HTTP Token Requirement specified in the request.

This value for this key can be either `optional` or `required`.

**Availability** – This key is available to only the `CreateInfrastrucutreConfiguration` and `UpdateInfrastructureConfiguration` APIs.

#### imagebuilder:StatusTopicArn
<a name="image-builder-security-statustopicarn"></a>

Works with [string operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String).

Use this key to filter access by the SNS Topic ARN in the request to which terminal state notifications will be published.

**Availability** – This key is available to only the `CreateInfrastrucutreConfiguration` and `UpdateInfrastructureConfiguration` APIs.

### Examples
<a name="sec-iam-ib-id-based-policies-examples"></a>



To view examples of Image Builder identity-based policies, see [Image Builder identity-based policies](security-iam-identity-based-policies.md).

## Image Builder resource-based policies
<a name="security-iam-service-with-ib-resource-based-policies"></a>

Resource-based policies specify what actions a specified principal can perform on the Image Builder resource and under what conditions. Image Builder supports resource-based permissions policies for components, images, and image recipes. Resource-based policies let you grant usage permission to other accounts on a per-resource basis. You can also use a resource-based policy to allow an AWS service to access your components, images, and image recipes.

For information about how to attach a resource-based policy to a component, image, or image recipe, see [Share Image Builder resources with AWS RAM](manage-shared-resources.md).

**Note**  
When you update a resource policy using Image Builder, the update will appear in the RAM console.

## Authorization based on Image Builder tags
<a name="security-iam-service-with-ib-tags"></a>

You can attach tags to Image Builder resources or pass tags in a request to Image Builder. To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `imagebuilder:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys. For more information about tagging Image Builder resources, see [Tag a resource from the AWS CLI](tag-resources.md#cli-tag-resource).

## Image Builder IAM roles
<a name="security-iam-service-with-ib-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using temporary credentials with Image Builder
<a name="security-iam-service-with-ib-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html). 

### Service-linked roles
<a name="sec-iam-ib-service-linked-roles"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. A user with administrative access can view but not edit the permissions for service-linked roles.

Image Builder supports service-linked roles. For information about creating or managing Image Builder service-linked roles, see [Use IAM service-linked roles for Image Builder](image-builder-service-linked-role.md).

### Service roles
<a name="sec-iam-ib-service-roles"></a>

This feature allows a service to assume a [service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) on your behalf. This role allows the service to access resources in other services to complete an action on your behalf. Service roles appear in your IAM account and are owned by the account. This means that an user with administrative access can change the permissions for this role. However, doing so might break the functionality of the service.