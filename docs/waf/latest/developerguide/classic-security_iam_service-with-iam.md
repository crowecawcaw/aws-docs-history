**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How AWS WAF Classic works with IAM

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

Before you use IAM to manage access to AWS WAF Classic, learn what IAM features are
available to use with AWS WAF Classic.

| IAM features you can use with AWS WAF Classic                                                                                                                                               | IAM feature | AWS WAF Classic support |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------- |
| [Identity-based policies](#classic-security_iam_service-with-iam-id-based-policies "#classic-security_iam_service-with-iam-id-based-policies")                                              | Yes         |
| [Resource-based policies](#classic-security_iam_service-with-iam-resource-based-policies "#classic-security_iam_service-with-iam-resource-based-policies")                                  | No          |
| [Policy actions](#classic-security_iam_service-with-iam-id-based-policies-actions "#classic-security_iam_service-with-iam-id-based-policies-actions")                                       | Yes         |
| [Policy resources](#classic-security_iam_service-with-iam-id-based-policies-resources "#classic-security_iam_service-with-iam-id-based-policies-resources")                                 | Yes         |
| [Policy condition keys (service-specific)](#classic-security_iam_service-with-iam-id-based-policies-conditionkeys "#classic-security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [ACLs](#classic-security_iam_service-with-iam-acls "#classic-security_iam_service-with-iam-acls")                                                                                           | No          |
| [ABAC (tags in<br>policies)](#classic-security_iam_service-with-iam-tags "#classic-security_iam_service-with-iam-tags")                                                                     | Partial     |
| [Temporary<br>credentials](#classic-security_iam_service-with-iam-roles-tempcreds "#classic-security_iam_service-with-iam-roles-tempcreds")                                                 | Yes         |
| [Forward access sessions (FAS)](#classic-security_iam_service-with-iam-principal-permissions "#classic-security_iam_service-with-iam-principal-permissions")                                | Yes         |
| [Service<br>roles](#classic-security_iam_service-with-iam-roles-service "#classic-security_iam_service-with-iam-roles-service")                                                             | Yes         |
| [Service-linked roles](#classic-security_iam_service-with-iam-roles-service-linked "#classic-security_iam_service-with-iam-roles-service-linked")                                           | Yes         |

To get a high-level view of how AWS WAF Classic and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based

policies for AWS WAF Classic

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

To view examples of AWS WAF Classic identity-based policies, see [Identity-based policy examples for
AWS WAF Classic](classic-security_iam_id-based-policy-examples.md "classic-security_iam_id-based-policy-examples.md").

## Resource-based

policies within AWS WAF Classic

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

## Policy actions

for AWS WAF Classic

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of AWS WAF Classic actions, see [Actions defined by AWS WAF](../../../service-authorization/latest/reference/list_awswaf.md#awswaf-actions-as-permissions "../../../service-authorization/latest/reference/list_awswaf.md#awswaf-actions-as-permissions") and [Actions defined by AWS WAF Regional](../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-actions-as-permissions "../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in AWS WAF Classic use the following prefix before the action:

```
waf
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "waf:`action1`",
      "waf:`action2`"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions in AWS WAF Classic that begin with `List`, include the following
action:

```
"Action": "waf:List*"
```

To view examples of AWS WAF Classic identity-based policies, see [Identity-based policy examples for
AWS WAF Classic](classic-security_iam_id-based-policy-examples.md "classic-security_iam_id-based-policy-examples.md").

## Policy

resources for AWS WAF Classic

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see the list of AWS WAF Classic resource types and their ARNs, see
[Resources defined by AWS WAF](../../../service-authorization/latest/reference/list_awswaf.md#awswaf-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awswaf.md#awswaf-resources-for-iam-policies") and [Resources defined by AWS WAF Regional](../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-resources-for-iam-policies") in the _Service Authorization Reference_. To learn with
which actions you can specify the ARN of each resource, see [Actions defined by AWS WAF](../../../service-authorization/latest/reference/list_awswaf.md#awswaf-actions-as-permissions "../../../service-authorization/latest/reference/list_awswaf.md#awswaf-actions-as-permissions") and [Actions defined by AWS WAF Regional](../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-actions-as-permissions "../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-actions-as-permissions"). To
allow or deny access to a subset of AWS WAF Classic resources, include the ARN of the
resource in the `resource` element of your policy.

In AWS WAF Classic, the resources are _web ACLs_ and
_rules_. AWS WAF Classic also supports conditions such as _byte
match_, _IP match_, and _size constraint_.

These resources and conditions have unique Amazon Resource Names (ARNs) associated with
them, as shown in the following table.

| Name in AWS WAF Console              | Name in AWS WAF SDK/CLI | ARN Format                                        |
| ------------------------------------ | ----------------------- | ------------------------------------------------- | --- |
| Web ACL                              | `WebACL`                | `arn:aws:waf::`account`:`webacl`/`ID``            |
| Rule                                 | `Rule`                  | `arn:aws:waf::`account`:`rule`/`ID``              |
| String match condition               | `ByteMatchSet`          | `arn:aws:waf::`account`:`bytematchset`/`ID``      |
| SQL injection match condition        | `SqlInjectionMatchSet`  | `arn:aws:waf::`account`:`sqlinjectionset`/`ID``   |
| Size constraint condition            | `SizeConstraintSet`     | `arn:aws:waf::`account`:`sizeconstraintset`/`ID`` |
| IP match condition                   | `IPSet`                 | `arn:aws:waf::`account`:`ipset`/`ID``             |
| Cross-site scripting match condition | `XssMatchSet`           | `arn:aws:waf::`account`:`xssmatchset`/`ID``       |     |

To allow or deny access to a subset of AWS WAF Classic resources, include the ARN of the resource
in the `resource` element of your policy. The ARNs for AWS WAF Classic have the following
format:

```
arn:aws:waf::`account`:`resource`/`ID`
```

Replace the `account`, `resource`, and
`ID` variables with valid values. Valid values can be the
following:

- `account`: The ID of your AWS account. You must specify a
  value.
- `resource`: The type of AWS WAF Classic resource.
- `ID`: The ID of the AWS WAF Classic resource, or a wildcard
  (`*`) to indicate all resources of the specified type that are associated
  with the specified AWS account.

For example, the following ARN specifies all web ACLs for the account
`111122223333`:

```
arn:aws:waf::111122223333:webacl/*
```

## Policy

condition keys for AWS WAF Classic

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of AWS WAF Classic condition keys, see [Condition keys for AWS WAF](../../../service-authorization/latest/reference/list_awswaf.md#awswaf-policy-keys "../../../service-authorization/latest/reference/list_awswaf.md#awswaf-policy-keys") and [Resources defined by AWS WAF Regional](../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-resources-for-iam-policies") in the
_Service Authorization Reference_. To learn with which actions and resources you
can use a condition key, see [Actions defined by AWS WAF](../../../service-authorization/latest/reference/list_awswaf.md#awswaf-actions-as-permissions "../../../service-authorization/latest/reference/list_awswaf.md#awswaf-actions-as-permissions") and [Actions defined by AWS WAF Regional](../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-actions-as-permissions "../../../service-authorization/latest/reference/list_awswafregional.md#awswafregional-actions-as-permissions").

To view examples of AWS WAF Classic identity-based policies, see [Identity-based policy examples for
AWS WAF Classic](classic-security_iam_id-based-policy-examples.md "classic-security_iam_id-based-policy-examples.md").

## ACLs in AWS WAF Classic

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with AWS WAF Classic

**Supports ABAC (tags in policies):**

Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using temporary

credentials with AWS WAF Classic

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Forward access sessions for AWS WAF Classic

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for

AWS WAF Classic

**Supports service roles:**

Yes

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break AWS WAF Classic functionality.
Edit service roles only when AWS WAF Classic provides guidance to do so.

## Service-linked

roles for AWS WAF Classic

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing AWS WAF Classic service-linked roles, see [Using service-linked roles for AWS WAF Classic](classic-using-service-linked-roles.md "classic-using-service-linked-roles.md").
