# How EMR Serverless works with IAM

Before you use IAM to manage access to Amazon EMR Serverless, learn what IAM features are
available to use with Amazon EMR Serverless.

| IAM features use with EMR Serverless                                                                                      | IAM feature | Amazon EMR Serverless support |
| ------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------- |
| [Identity-based<br>policies](#security-iam-id-based-policies "#security-iam-id-based-policies")                           | Yes         |
| [Resource-based<br>policies](#security-iam-resource-based-policies "#security-iam-resource-based-policies")               | No          |
| [Policy<br>actions](#security-iam-id-based-policies-actions "#security-iam-id-based-policies-actions")                    | Yes         |
| [Policy<br>resources](#security-iam-id-based-policies-resources "#security-iam-id-based-policies-resources")              | Yes         |
| [Policy condition<br>keys](#security-iam-id-based-policies-conditionkeys "#security-iam-id-based-policies-conditionkeys") | No          |
| [ACLs](#security-iam-acls "#security-iam-acls")                                                                           | No          |
| [ABAC (tags in policies)](#security-iam-tags "#security-iam-tags")                                                        | Yes         |
| [Temporary credentials](#security-iam-roles-tempcreds "#security-iam-roles-tempcreds")                                    | Yes         |
| [Principal<br>permissions](#security-iam-principal-permissions "#security-iam-principal-permissions")                     | Yes         |
| [Service roles](#security-iam-roles-service "#security-iam-roles-service")                                                | No          |
| [Service-linked<br>roles](#security-iam-roles-service-linked "#security-iam-roles-service-linked")                        | Yes         |

To get a high-level view of how EMR Serverless and other AWS services work with most
IAM features, refer to [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based policies for

EMR Serverless

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

### Sample identity-based policies for

EMR Serverless

To access examples of Amazon EMR Serverless identity-based policies, refer to [Identity-based policy examples for
EMR Serverless](security-iam-id-based-policy-examples.md "security-iam-id-based-policy-examples.md").

## Resource-based policies within

EMR Serverless

**Supports resource-based policies:**

No

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are
IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service
administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions
a specified principal can perform on that resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals
can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities
in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
_IAM User Guide_.

## Policy actions for

EMR Serverless

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To refer to a list of EMR Serverless actions, refer to [Actions,
resources, and condition keys for Amazon EMR Serverless](../../../service-authorization/latest/reference/list_amazonemrserverless.md "../../../service-authorization/latest/reference/list_amazonemrserverless.md") in the
_Service Authorization Reference_.

Policy actions in EMR Serverless use the following prefix before the action.

```
emr-serverless
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "emr-serverless:`action1`",
      "emr-serverless:`action2`"
         ]
```

To access examples of Amazon EMR Serverless identity-based policies, refer to [Identity-based policy examples for
EMR Serverless](security-iam-id-based-policy-examples.md "security-iam-id-based-policy-examples.md").

## Policy resources for

EMR Serverless

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To refer to a list of Amazon EMR Serverless resource types and their ARNs, see [Resources defined by Amazon EMR Serverless](../../../service-authorization/latest/reference/list_amazonelasticmapreduce.md#amazonelasticmapreduce-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonelasticmapreduce.md#amazonelasticmapreduce-resources-for-iam-policies") in
the _Service Authorization Reference_. To learn which actions specify the ARN of
each resource, refer to [Actions,
resources, and condition keys for Amazon EMR Serverless](../../../service-authorization/latest/reference/list_amazonemrserverless.md "../../../service-authorization/latest/reference/list_amazonemrserverless.md").

To access examples of Amazon EMR Serverless identity-based policies, refer to [Identity-based policy examples for
EMR Serverless](security-iam-id-based-policy-examples.md "security-iam-id-based-policy-examples.md").

## Policy condition keys for

EMR Serverless

Policy condition keys support| Supports service-specific policy condition keys | No |

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To refer to a list of Amazon EMR Serverless condition keys and to learn which actions and resources you
can use a condition key, refer to [Actions,
resources, and condition keys for Amazon EMR Serverless](../../../service-authorization/latest/reference/list_amazonemrserverless.md "../../../service-authorization/latest/reference/list_amazonemrserverless.md") in the
_Service Authorization Reference_.

All Amazon EC2 actions support the `aws:RequestedRegion` and
`ec2:Region` condition keys. For more information, refer to [Example: Restricting
access to a specific region](../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region "../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region").

## Access control lists (ACLs) in EMR Serverless

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with

EMR Serverless

Attribute-based access control (ABAC) support| Supports ABAC (tags in policies) | Yes |

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using Temporary credentials with

EMR Serverless

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Cross-service principal permissions for

EMR Serverless

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for EMR Serverless

|                        |     |
| ---------------------- | --- |
| Supports service roles | No  |

## Service-linked roles for

EMR Serverless

|                               |     |
| ----------------------------- | --- |
| Supports service-linked roles | Yes |

For details about creating or managing service-linked roles, refer to [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find a service in the table that includes a `Yes` in
the **Service-linked role** column. Choose the **Yes**
link to access the service-linked role documentation for that service.
