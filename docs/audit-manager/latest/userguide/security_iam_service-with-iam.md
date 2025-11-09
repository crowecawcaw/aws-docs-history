# How AWS Audit Manager works with IAM

Before you use IAM to manage access to Audit Manager, learn what IAM features are
available to use with Audit Manager.

| IAM features you can use with AWS Audit Manager                                                                                                          | IAM feature | Audit Manager support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | No          |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Yes         |
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Partial     |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                        | No          |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                  | Yes         |
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                                 | Yes         |
| [Forward access sessions (FAS)](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")             | Yes         |
| [Service roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                             | No          |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | Yes         |

To get a high-level view of how AWS Audit Manager and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based

policies for AWS Audit Manager

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

AWS Audit Manager creates a managed policy named
`AWSAuditManagerAdministratorAccess` for Audit Manager administrators.
This policy grants full administration access in Audit Manager. Administrators can attach
this policy to any existing role or user, or create a new role with this
policy.

###

Recommended policies for user personas in AWS Audit Manager

AWS Audit Manager enables you to maintain the segregation of duties among different
users and for different audits by using different IAM policies. The two personas
in Audit Manager and their recommended policies are defined as follows.

| Persona         | Description and recommended policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Audit owner** | • This persona must have the necessary permissions<br>to manage assessments in AWS Audit Manager.<br>• The recommended policy to use for this persona is<br>the managed policy named [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md"). You<br>can use this policy as a starting point, and scope<br>down these permissions as needed to fit your<br>requirements.                                                                        |
| **Delegate**    | • This persona can access the delegated control sets<br>in an assessment. They can update the control<br>status, add comments, submit a control set for<br>review, and add evidence to the assessment<br>report.<br>• The recommended policy to use for this persona is<br>the following example policy: [Allow users management access to<br>AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access"). You can use<br>this policy as a starting point, and make changes as<br>necessary to fit your requirements. |

###

Identity-based policy examples for AWS Audit Manager

To view examples of Audit Manager identity-based policies, see [Identity-based policy examples
for AWS Audit Manager](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based policies within AWS Audit Manager

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

Although AWS Audit Manager does not allow you to manage resource-based
policies through IAM, the service internally implements and manages resource-based
policies for the following two scenarios:

- When audit owners are assigned to an assessment, a resource-based policy
  is attached to the assessment with the principal as the audit owner. For
  more information, see [Step 3: Specify audit owners](create-assessments.md#choose-audit-owners "create-assessments.md#choose-audit-owners") and [Step 3: Edit audit owners](edit-assessment.md#edit-choose-audit-owners "edit-assessment.md#edit-choose-audit-owners").
- When a control set of an assessment is delegated, a resource-based policy
  is attached to the control set with the principal as the delegate. For more
  information, see [Delegating a control
  set for review in AWS Audit Manager](delegation-for-audit-owners-delegating-a-control-set.md "delegation-for-audit-owners-delegating-a-control-set.md").

## Policy

actions for AWS Audit Manager

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of AWS Audit Manager actions, see [Actions defined by AWS Audit Manager](../../../service-authorization/latest/reference/list_awsauditmanager.md#awsauditmanager-actions-as-permissions "../../../service-authorization/latest/reference/list_awsauditmanager.md#awsauditmanager-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in AWS Audit Manager use the following prefix before the action.

```
auditmanager
```

To specify multiple actions in a single statement, separate them with
commas.

```
"Action": [
      "auditmanager:`GetEvidenceDetails`",
      "auditmanager:`GetEvidenceEventDetails`"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Get`, include the following
action.

```
"Action": "auditmanager:Get*"
```

To view examples of Audit Manager identity-based policies, see [Identity-based policy examples
for AWS Audit Manager](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy

resources for AWS Audit Manager

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of AWS Audit Manager resource types and their ARNs, see
[Resources defined by AWS Audit Manager](../../../service-authorization/latest/reference/list_awsauditmanager.md#awsauditmanager-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awsauditmanager.md#awsauditmanager-resources-for-iam-policies") in the _Service Authorization Reference_. To learn about
actions with which you can specify the ARN of each resource, see
[Actions defined by AWS Audit Manager](../../../service-authorization/latest/reference/list_awsauditmanager.md#awsauditmanager-actions-as-permissions "../../../service-authorization/latest/reference/list_awsauditmanager.md#awsauditmanager-actions-as-permissions").

An Audit Manager assessment has the following Amazon Resource Name (ARN) format:

```
arn:${Partition}:auditmanager:${Region}:${Account}:assessment/${assessmentId}
```

An Audit Manager control set has the following ARN format:

```
arn:${Partition}:auditmanager:${Region}:${Account}:assessment/${assessmentId}controlSet/${controlSetId}
```

An Audit Manager control has the following ARN format:

```
arn:${Partition}:auditmanager:${Region}:${Account}:control/${controlId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `i-1234567890abcdef0` assessment in your
statement, use the following ARN.

```
"Resource": "arn:aws:auditmanager:us-east-1:123456789012:assessment/i-1234567890abcdef0"
```

To specify all instances that belong to a specific account, use the wildcard
(\*).

```
"Resource": "arn:aws:auditmanager:us-east-1:123456789012:assessment/*"
```

Some Audit Manager actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

Many Audit Manager API actions involve multiple resources. For example,
`ListAssessments` returns a list of assessment metadata that's
accessible by the currently logged in AWS account. Therefore, a user must have
permissions to view the assessments. To specify multiple resources in a single
statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of Audit Manager resource types and their ARNs, see
[Resources Defined by AWS Audit Manager](../../../IAM/latest/UserGuide/list_awskeymanagementservice.md#awskeymanagementservice-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awskeymanagementservice.md#awskeymanagementservice-resources-for-iam-policies") in the _IAM User Guide_. To learn
about actions with which you can specify the ARN of each resource, see
[Actions Defined by AWS Audit Manager](../../../IAM/latest/UserGuide/list_awskeymanagementservice.md#awskeymanagementservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_awskeymanagementservice.md#awskeymanagementservice-actions-as-permissions").

Some Audit Manager API actions support multiple resources. For example,
`GetChangeLogs` accesses an `assessmentID`,
`controlID`, and `controlSetId`, so a principal must have
permissions to access each of these resources. To specify multiple resources in a
single statement, separate the ARNs with commas.

```
"Resource": [
      "*assessmentId*",
      "*controlId*",
      "*controlSetId*"
```

## Policy condition keys for AWS Audit Manager

**Supports service-specific policy condition keys:**

Partial

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element (or `Condition`
_block_) lets you specify conditions in which a
statement is in effect. The `Condition` element is optional. You can
create conditional expressions that use [condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the
condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or
multiple keys in a single `Condition` element, AWS evaluates them using
a logical `AND` operation. If you specify multiple values for a single
condition key, AWS evaluates the condition using a logical `OR`
operation. All of the conditions must be met before the statement's permissions
are granted.

When the principal in a policy statement is an [AWS service principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), we strongly recommend that
you use the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") or [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition
keys in the policy. You can use these global condition context keys to help prevent
the [confused deputy scenario](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md"). The following documented policies show how
you can use the `aws:SourceArn` and `aws:SourceAccount` global
condition context keys in Audit Manager to prevent the confused deputy problem.

- [Example policy for an SNS topic that's used for Audit Manager
  notifications](security_iam_id-based-policy-examples.md#sns-topic-permissions "security_iam_id-based-policy-examples.md#sns-topic-permissions")
- [Example policy for a KMS key that's used with an SNS
  topic](security_iam_id-based-policy-examples.md#sns-key-permissions "security_iam_id-based-policy-examples.md#sns-key-permissions")

You can also use placeholder variables when you specify conditions. For example,
you can grant a user permission to access a resource only if it is tagged with their
user name. For more information, see [IAM policy elements:
variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

Audit Manager does not provide any service-specific condition keys, but it does
support using some global condition keys. To see all AWS global condition keys,
see [AWS global
condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

## Access control lists (ACLs) in

AWS Audit Manager

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control

(ABAC) with AWS Audit Manager

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

For more information about tagging AWS Audit Manager resources, see [Tagging AWS Audit Manager resources](tagging.md "tagging.md").

## Using temporary

credentials with AWS Audit Manager

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Forward access

sessions for AWS Audit Manager

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for

AWS Audit Manager

**Supports service roles:**

No

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break AWS Audit Manager
functionality. Edit service roles only when Audit Manager provides guidance to do
so.

## Service-linked

roles for AWS Audit Manager

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about service-linked roles for AWS Audit Manager, see [Using service-linked roles for AWS Audit Manager](using-service-linked-roles.md "using-service-linked-roles.md").
