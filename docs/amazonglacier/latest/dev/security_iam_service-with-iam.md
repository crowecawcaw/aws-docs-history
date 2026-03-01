**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# How Amazon Glacier works with IAM

Before you use IAM to manage access to Amazon Glacier, learn what IAM features are
available to use with Amazon Glacier.

| IAM features you can use with Amazon Glacier                                                                                                                                | IAM feature | Amazon Glacier support |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                                              | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")                                  | Yes         |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                                       | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")                                 | Yes         |
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                                           | No          |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                                     | No          |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                                                 | Yes         |
| [Principal permissions](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                                        | No          |
| [Service<br>roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                                             | No          |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                                           | No          |

To get a high-level view of how Amazon Glacier and other AWS services work with most IAM features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Identity-based policies for Amazon Glacier

**Supports identity-based policies:**

Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

### Identity-based policy examples for Amazon Glacier

To view examples of Amazon Glacier identity-based policies, see [Identity-based policy examples for Amazon Glacier](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based policies within Amazon Glacier

**Supports resource-based policies:**

Yes

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are
IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service
administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions
a specified principal can perform on that resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals
can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities
in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
_IAM User Guide_.

The Amazon Glacier service supports only one type of resource-based policy called a _vault policy_, which is attached
to a vault. This policy defines which principals can perform actions on the
vault.

Amazon Glacier vault policies manage permissions in the following ways:

- Manage user permissions in an account using a single vault policy, instead of more than one individual user policies.
- Manage cross-account permissions as an alternative to using IAM roles.

### Resource-based policy examples within Amazon Glacier

To view examples of Amazon Glacier resource-based policies, see [Resource-based policy examples for Amazon Glacier](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").

## Policy actions for Amazon Glacier

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Amazon Glacier actions, see [Actions defined by Amazon Glacier](../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-actions-as-permissions "../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-actions-as-permissions") in the _Service Authorization Reference_.

Policy actions in Amazon Glacier use the following prefix before the action:

```
glacier
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
            "glacier:CreateVault",
            "glacier:DescribeVault",
            "glacier:ListVaults"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "glacier:GetVault*"
```

To view examples of Amazon Glacier identity-based policies, see [Identity-based policy examples for Amazon Glacier](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy resources for Amazon Glacier

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Amazon Glacier resource types and their ARNs, see
[Resources defined by Amazon Glacier](../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-resources-for-iam-policies") in the _Service Authorization Reference_. To learn which actions you can specify the ARN of each resource, see
[Actions defined by Amazon Glacier](../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-actions-as-permissions "../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-actions-as-permissions").

In Amazon Glacier, the primary resource is a _vault_. Amazon Glacier supports policies only at the vault level.
That is, in an IAM policy, the `Resource` value that you
specify can be a specific vault or a set of vaults in a specific AWS Region.
Amazon Glacier doesn't support archive-level permissions.

For all Amazon Glacier actions, `Resource` specifies the vault on which you want to grant the permissions. These resources have unique Amazon Resource Names (ARNs) associated with them as shown in the following table, and you can use a wildcard character (\*) in the ARN to match vault names that start with the same prefix.

| Resource Type                             | ARN Format                                                  |
| ----------------------------------------- | ----------------------------------------------------------- |
| Vaults                                    | `arn:aws:glacier:`region`:`account-id`:vaults/`vault-name`` |
| Vaults with names starting with "example" | `arn:aws:glacier:`region`:`account-id`:vaults/example*`     |

Amazon Glacier provides a set of operations to work with the Amazon Glacier resources. For information on the available operations, see [API Reference for Amazon Glacier](amazon-glacier-api.md "amazon-glacier-api.md").

Some Amazon Glacier API actions support multiple resources. For example, `glacier:AddTagsToVault` accesses examplevault1 and examplevault2, so a principal must have permissions to access both resources. To specify multiple resources in a single statement, separate the ARNs with commas.

```

            "Resource": [
            "*"arn:aws:glacier:us-west-2:123456789012:vaults/examplevault1",*",
            "*"arn:aws:glacier:us-west-2:123456789012:vaults/examplevault2",*"
            ]

```

## Policy condition keys for Amazon Glacier

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Amazon Glacier condition keys, see [Condition keys for Amazon Glacier](../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-policy-keys "../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and resources you
can use a condition key, see [Actions defined by Amazon Glacier](../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-actions-as-permissions "../../../service-authorization/latest/reference/list_amazons3glacier.md#amazons3glacier-actions-as-permissions").

For examples of using the glacier–specific condition keys, see [Vault Lock Policies](vault-lock-policy.md "vault-lock-policy.md").

## ACLs in Amazon Glacier

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Amazon Glacier

**Supports ABAC (tags in policies):**

No

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using temporary credentials with Amazon Glacier

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Cross-service principal permissions for Amazon Glacier

**Supports forward access sessions (FAS):**

No

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for Amazon Glacier

**Supports service roles:**

No

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break Amazon Glacier functionality.
Edit service roles only when Amazon Glacier provides guidance to do so.

## Service-linked roles for Amazon Glacier

**Supports service-linked roles:**

No

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find a service in the table that includes a
`Yes` in the **Service-linked role** column. Choose the
**Yes** link to view the service-linked role documentation for that
service.
