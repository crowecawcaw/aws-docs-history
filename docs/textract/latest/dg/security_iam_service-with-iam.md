

# How Amazon Textract works with IAM

Before you use IAM to manage access to Amazon Textract Core, you should understand what IAM features are available to use with Amazon Textract Core. To get a high-level view of how Amazon Textract Core and other AWS services work with IAM, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Amazon Textract identity-based policies](#security_iam_service-with-iam-id-based-policies)
+ [Amazon Textract resource-based policies](#security_iam_service-with-iam-resource-based-policies)
+ [Authorization based on Amazon Textract tags](#security_iam_service-with-iam-tags)
+ [Amazon Textract IAM roles](#security_iam_service-with-iam-roles)

## Amazon Textract identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources and the conditions under which actions are allowed or denied. Amazon Textract Core supports specific actions, resources, and condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Asynchronous actions in Amazon Textract Core require two action permissions to be given, one for Start actions and one for Get actions. Additionally, if you are using an Amazon S3 bucket to pass documents, you will need to grant your account read access.

For example, an Amazon Textract Insights job needs `textract:StartDocumentInsights` and `textract:GetDocumentInsights`, plus `s3:GetObject` on the input location. Amazon Textract Insights also needs `s3:PutObject` on the output location, and AWS KMS permissions when you use a customer managed key.

In Amazon Textract Core, all policy actions start with: `textract:`. For example, to grant someone permission to run the Amazon Textract Core `AnalyzeDocument` operation, you include the `textract:AnalyzeDocument` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Amazon Textract Core defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "textract:action1",
      "textract:action2"
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "textract:Describe*"
```



Amazon Textract Insights adds actions for projects, such as `textract:CreateProject`, for blueprints, such as `textract:CreateBlueprint`, and for jobs: `textract:StartDocumentInsights` and `textract:GetDocumentInsights`. It uses the same tagging actions as adapters. For the full list of Amazon Textract Insights actions and a policy that covers the whole workflow, see [Prerequisites and setup](insights-prerequisites.md).

For a list of Amazon Textract Core actions, see [Actions Defined by Amazon Textract](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazontextract.html#amazontextract-actions-as-permissions) in the *IAM User Guide*.

### Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

For actions that support resource-level permissions, such as the [AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/APIReference/API_AnalyzeDocument.html) and [GetAdapter](https://docs.aws.amazon.com/textract/latest/APIReference/API_GetAdapter.html) operations, use the ARN to indicate the resources:

```
"Resource": [
  # Adapter ARN
  "arn:aws:textract:<region>:<account-id>:/adapters/<adapter-id>",
  # Adapter version ARN
  "arn:aws:textract:<region>:<account-id>:/adapters/<adapter-id>/versions/<version>",
  # Use wildcard to indicate all versions under an adapter
  "arn:aws:textract:<region>:<account-id>:/adapters/<adapter-id>/versions/*"
]
```

Amazon Textract Insights resources are projects, blueprints, and jobs, and each has its own ARN. Public blueprints are owned by AWS, so their ARNs use `aws` in place of an account ID. For the ARN formats, see [Tagging Amazon Textract Insights resources](insights-tagging.md).

Amazon Textract Insights actions support resource-level permissions. The following table lists the resource ARNs that Amazon Textract Insights checks for each action. A request succeeds only if your policy allows the action on every ARN listed for it.


**Resource ARNs checked for each Amazon Textract Insights action**  

| **Action** | **Resource ARNs checked** | 
| --- | --- | 
| `CreateProject` | `project/*` in your account, plus each blueprint ARN in `CustomConfiguration`, including fallback blueprints | 
| `UpdateProject` | The project ARN, plus each blueprint ARN in `CustomConfiguration`, including fallback blueprints | 
| `GetProject`, `DeleteProject` | The project ARN | 
| `ListProjects` | `project/*` in your account, plus the blueprint ARN in `BlueprintFilter`, if you specify one | 
| `CreateBlueprint` | `blueprint/*` in your account | 
| `GetBlueprint`, `UpdateBlueprint`, `DeleteBlueprint`, `CreateBlueprintVersion` | The blueprint ARN | 
| `ListBlueprints` | `blueprint/*` in your account, or `aws:blueprint/*` when `ResourceOwner` is `SERVICE`. Also checks the project ARN in `ProjectFilter`. When you list the versions of one blueprint, only that blueprint ARN is checked. | 
| `StartDocumentInsights` | The project ARN, or each inline blueprint ARN, plus `job/*` in your account | 
| `GetDocumentInsights` | The job ARN | 
| `TagResource`, `UntagResource`, `ListTagsForResource` | The resource ARN in the request | 

**Note**  
An action that creates a resource is checked against a wildcard ARN in your account, such as `project/*`, because the new resource doesn't have an ARN yet. If you pass `Tags` to a create call, `textract:TagResource` is also checked against that wildcard ARN.  
Public blueprints are owned by AWS, so their ARNs use `aws` in place of an account ID, for example `arn:aws:textract:us-east-1:aws:blueprint/public-w2-form`. To use public blueprints, allow `arn:aws:textract:<region>:aws:blueprint/*`. A policy that allows only ARNs in your own account blocks them.  
Amazon Textract Insights rejects ARNs from another account or another AWS Region. Public blueprints are exempt only from the account check.

### Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Amazon Textract Core does not provide any service-specific condition keys, but it does support using some global condition keys. For a list of all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

For adapters and for Amazon Textract Insights projects, blueprints, and jobs, you can use the `aws:ResourceTag/${TagKey}`, `aws:RequestTag/${TagKey}`, and `aws:TagKeys` condition keys.

In AWS KMS key policies, you can match the encryption context that Amazon Textract Insights attaches to each request, such as context keys that start with `aws:textract:`. See [Data protection and encryption](insights-data-protection.md).

### Examples
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Amazon Textract Core identity-based policies, see [Amazon Textract identity-based policy examples](security_iam_id-based-policy-examples.md).

## Amazon Textract resource-based policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Amazon Textract Core does not support resource-based policies.

## Authorization based on Amazon Textract tags
<a name="security_iam_service-with-iam-tags"></a>



You can attach tags to adapters and to Amazon Textract Insights projects, blueprints, and jobs, and control access based on those tags. Use the [TagResource](https://docs.aws.amazon.com/STS/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/STS/latest/APIReference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/STS/latest/APIReference/API_ListTagsForResource.html) operations to manage tags. For adapters, see [Tagging resources](tagging-adapters.md). For the Amazon Textract Insights resources you can tag and the condition keys, see [Tagging Amazon Textract Insights resources](insights-tagging.md).

For access control based on tags, you can refer to [AccessTags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html). 

## Amazon Textract IAM roles
<a name="security_iam_service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using temporary credentials with Amazon Textract
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html). 

Amazon Textract Core supports using temporary credentials. 

### Service-linked roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An IAM administrator can view but not edit the permissions for service-linked roles.

Amazon Textract Core does not support service-linked roles.

**Note**  
Because Amazon Textract Core does not support service-linked roles, it does not support AWS service principals. For more information about service principals, see [AWS service principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) in the *IAM User Guide*.

### Service roles
<a name="security_iam_service-with-iam-roles-service"></a>

This feature allows a service to assume a [service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) on your behalf. This role allows the service to access resources in other services to complete an action on your behalf. Service roles appear in your IAM account and are owned by the account. This means that an IAM administrator can change the permissions for this role. However, doing so might break the functionality of the service.

Amazon Textract Core supports service roles. 

Amazon Textract Insights doesn't use a service role. It accesses your Amazon S3 locations and KMS keys with the caller's permissions.

If you are using a service role, you should ensure that your account is secure by limiting the scope of Amazon Textract Core access to only the resources that you're using. To do this, attach a trust policy to your IAM service role. For more information, see [Cross-service confused deputy prevention](https://docs.aws.amazon.com/textract/latest/dg/cross-service-confused-deputy-prevention.html).