

# Identity and Access Management for Amazon OpenSearch Memory

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use OpenSearch Memory resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [Identity-based policies for OpenSearch Memory](#security-iam-memory-id-based-policies)
+ [Resource-based policies within OpenSearch Memory](#security-iam-memory-resource-based-policies)
+ [Policy actions for OpenSearch Memory](#security-iam-memory-id-based-policies-actions)
+ [Policy resources for OpenSearch Memory](#security-iam-memory-id-based-policies-resources)
+ [Policy condition keys for OpenSearch Memory](#security_iam_memory-conditionkeys)
+ [ABAC with OpenSearch Memory](#security_iam_memory-with-iam-tags)
+ [Authenticating to OpenSearch Memory with temporary credentials](#security_iam_memory-tempcreds)
+ [Service-linked roles for OpenSearch Memory](#security_iam_memory-slr)
+ [Identity-based policy examples for OpenSearch Memory](#security_iam_memory_id-based-policy-examples)
+ [Troubleshooting OpenSearch Memory identity and access](#security_iam_memory-troubleshoot)

## Identity-based policies for OpenSearch Memory
<a name="security-iam-memory-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for OpenSearch Memory
<a name="memory-security_iam_id-based-policy-examples"></a>

For examples of OpenSearch Memory identity-based policies, see [Identity-based policy examples for OpenSearch Memory](#security_iam_memory_id-based-policy-examples).

## Resource-based policies within OpenSearch Memory
<a name="security-iam-memory-resource-based-policies"></a>

**Supports resource-based policies:** No 

OpenSearch Memory doesn't support resource-based policies or service-linked roles. You control access to spaces and their data with identity-based policies attached to your users and roles. OpenSearch Memory doesn't assume a role in your account.

## Policy actions for OpenSearch Memory
<a name="security-iam-memory-id-based-policies-actions"></a>

**Supports policy actions:** Yes

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Policy actions usually have the same name as the associated AWS API operation. There are some exceptions, such as *permission-only actions* that don't have a matching API operation. There are also some operations that require multiple actions in a policy. These additional actions are called *dependent actions*.

Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in OpenSearch Memory use the prefix `osm`. Each API operation has an action of the same name, for example `osm:CreateSpace` and `osm:SearchMemories`. To grant several actions, list them or use a wildcard, such as `osm:Get*`.

Some operations require more than one action:
+ [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html) with tags also requires `osm:TagResource`.
+ Operations on a space with a customer managed key also require AWS KMS permissions. For more information, see [Permissions required for a customer managed key](memory-data-protection.md#memory-encryption-permissions).

## Policy resources for OpenSearch Memory
<a name="security-iam-memory-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

OpenSearch Memory has one resource type, the space, with the following ARN format:

```
arn:${Partition}:osm:${Region}:${Account}:space/${SpaceId}
```

Every operation on an existing space, including the event and memory operations, is authorized on the space's ARN. `CreateSpace` and [ListSpaces](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListSpaces.html) don't act on an existing space, so specify `"Resource": "*"` for them.

## Policy condition keys for OpenSearch Memory
<a name="security_iam_memory-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

OpenSearch Memory supports the following service-specific condition keys. Use them to limit a principal to the data of specific actors, sessions, or strategies within a space.

`osm:actorId`  
The actor IDs in the request. Operations: All event and memory operations.

`osm:sessionId`  
The session IDs in the request. Operations: `CreateEvent`, [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html), [BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html), [ListEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListEvents.html), [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html), [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html)

`osm:strategyName`  
The memory strategy names in the request. Operations: [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html), [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html), [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html), [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html), [UpdateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html), [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html)

These keys are multivalued. Use them with the `ForAllValues` or `ForAnyValue` set operators. When you use `osm:actorId`, `osm:sessionId`, or `osm:strategyName` in a policy, also add a `Null` condition that sets the key to `false`, for example `"Null": {"osm:actorId": "false"}`. Without it, requests that leave out the value get through. A `ForAllValues` condition on a missing key matches, so an `Allow` statement allows the request. A `ForAnyValue` condition on a missing key doesn't match, so a `Deny` statement doesn't deny it. For an example, see [Limiting a principal to one actor's memories](#security_iam_id-based-policy-examples-memory-actor).

For the operations that act on one event or memory by ID, the condition keys come from the optional `actorId`, `sessionId`, and `strategyName` request parameters. OpenSearch Memory also checks that the stored record matches the values in the request and returns `ResourceNotFoundException` if it doesn't. For more information, see [Checking an event's owner](memory-events.md#memory-events-owner).

OpenSearch Memory also supports the global condition keys `aws:ResourceTag/{{key}}`, `aws:RequestTag/{{key}}`, and `aws:TagKeys`. For more information, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

## ABAC with OpenSearch Memory
<a name="security_iam_memory-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

OpenSearch Memory supports `aws:ResourceTag/{{key}}` on the space resource, `aws:RequestTag/{{key}}` and `aws:TagKeys` on `CreateSpace` and [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_TagResource.html), and `aws:TagKeys` on [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UntagResource.html).

## Authenticating to OpenSearch Memory with temporary credentials
<a name="security_iam_memory-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Service-linked roles for OpenSearch Memory
<a name="security_iam_memory-slr"></a>

**Supports service-linked roles:** No 

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

OpenSearch Memory doesn't use service-linked roles.

## Identity-based policy examples for OpenSearch Memory
<a name="security_iam_memory_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify OpenSearch Memory resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

**Topics**
+ [Follow policy best practices](#security_iam_memory-policy-best-practices)
+ [Running the getting started tutorial](#security-iam-memory-policy-example-tutorial)
+ [Administering spaces](#security_iam_id-based-policy-examples-memory-space-admin)
+ [Reading and writing one space's data](#security-iam-memory-policy-example-data)
+ [Limiting a principal to one actor's memories](#security_iam_id-based-policy-examples-memory-actor)
+ [Requiring a tag when creating a space](#security_iam_id-based-policy-examples-memory-tag-on-create)

### Follow policy best practices
<a name="security_iam_memory-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete OpenSearch Memory resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

### Running the getting started tutorial
<a name="security-iam-memory-policy-example-tutorial"></a>

The following policy grants the permissions that [Getting started with Amazon OpenSearch Memory](memory-getting-started.md) uses. Replace `us-east-1` and `111122223333` with your Region and account ID.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [ "osm:CreateSpace", "osm:ListSpaces" ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [ "osm:GetSpace", "osm:DeleteSpace", "osm:CreateEvent", "osm:SearchMemories" ],
            "Resource": "arn:aws:osm:us-east-1:111122223333:space/*"
        }
    ]
}
```

### Administering spaces
<a name="security_iam_id-based-policy-examples-memory-space-admin"></a>

The following policy lets a user create, view, update, tag, and delete the spaces in one Region of your account. It doesn't grant access to the events and memories in the spaces.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [ "osm:CreateSpace", "osm:ListSpaces" ],
            "Resource": "*",
            "Condition": { "StringEquals": { "aws:RequestedRegion": "us-east-1" } }
        },
        {
            "Effect": "Allow",
            "Action": [
                "osm:GetSpace", "osm:UpdateSpace", "osm:DeleteSpace",
                "osm:TagResource", "osm:UntagResource", "osm:ListTagsForResource"
            ],
            "Resource": "arn:aws:osm:us-east-1:111122223333:space/*"
        }
    ]
}
```

### Reading and writing one space's data
<a name="security-iam-memory-policy-example-data"></a>

The following policy lets an application role send events and search memories in one space, but not change the space itself.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "osm:CreateEvent", "osm:GetEvent", "osm:BatchGetEvent", "osm:ListEvents", "osm:SearchEvents",
                "osm:CreateMemory", "osm:GetMemory", "osm:ListMemories", "osm:SearchMemories"
            ],
            "Resource": "arn:aws:osm:us-east-1:111122223333:space/sp-02864597b164"
        }
    ]
}
```

### Limiting a principal to one actor's memories
<a name="security_iam_id-based-policy-examples-memory-actor"></a>

The following policy lets a principal read only the memories of the actor `user-123` in one space. The `Null` condition makes the statement apply only to requests that specify an actor. Use this pattern when each end user of your application has their own credentials, for example through Amazon Cognito identity pools, with the actor ID taken from the user's identity.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [ "osm:GetMemory", "osm:ListMemories", "osm:SearchMemories" ],
            "Resource": "arn:aws:osm:us-east-1:111122223333:space/sp-02864597b164",
            "Condition": {
                "ForAllValues:StringEquals": { "osm:actorId": [ "user-123" ] },
                "Null": { "osm:actorId": "false" }
            }
        }
    ]
}
```

### Requiring a tag when creating a space
<a name="security_iam_id-based-policy-examples-memory-tag-on-create"></a>

The following policy lets a user create spaces only with the tag `team=search` and no other tags. Creating a space with tags requires both `osm:CreateSpace` and `osm:TagResource`.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "osm:CreateSpace",
            "Resource": "*",
            "Condition": {
                "StringEquals": { "aws:RequestTag/team": "search" },
                "ForAllValues:StringEquals": { "aws:TagKeys": [ "team" ] }
            }
        },
        {
            "Effect": "Allow",
            "Action": "osm:TagResource",
            "Resource": "arn:aws:osm:us-east-1:111122223333:space/*",
            "Condition": {
                "StringEquals": { "aws:RequestTag/team": "search" },
                "ForAllValues:StringEquals": { "aws:TagKeys": [ "team" ] }
            }
        }
    ]
}
```

## Troubleshooting OpenSearch Memory identity and access
<a name="security_iam_memory-troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with OpenSearch Memory and IAM.

**Topics**
+ [I am not authorized to perform an action in OpenSearch Memory](#security_iam_memory-troubleshoot-no-permissions)
+ [Requests fail for a space that uses a customer managed key](#security_iam_memory-troubleshoot-kms)
+ [I can't create a space with tags](#security_iam_memory-troubleshoot-tags)

### I am not authorized to perform an action in OpenSearch Memory
<a name="security_iam_memory-troubleshoot-no-permissions"></a>

If a request fails with `AccessDeniedException`, the message names the action and resource that were denied.

```
User: arn:aws:iam::111122223333:user/mateojackson is not authorized to perform: osm:GetSpace on resource:
arn:aws:osm:us-east-1:111122223333:space/sp-02864597b164
```

Add the action to a policy attached to the identity, scoped to the space's ARN. If you need help, contact your AWS administrator.

### Requests fail for a space that uses a customer managed key
<a name="security_iam_memory-troubleshoot-kms"></a>

If you can use other spaces but requests on one space fail with `AccessDeniedException`, your identity probably lacks permission to use that space's AWS KMS key. For the actions that each operation requires, see [Permissions required for a customer managed key](memory-data-protection.md#memory-encryption-permissions).

### I can't create a space with tags
<a name="security_iam_memory-troubleshoot-tags"></a>

Creating a space with tags requires both `osm:CreateSpace` and `osm:TagResource`. If your policy allows only `osm:CreateSpace`, add `osm:TagResource`.