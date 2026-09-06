

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# How AWS Audit Manager works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Audit Manager, learn what IAM features are available to use with Audit Manager.






**IAM features you can use with AWS Audit Manager**  

| IAM feature | Audit Manager support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Partial | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Forward access sessions (FAS)](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes | 

To get a high-level view of how AWS Audit Manager and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for AWS Audit Manager
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

 AWS Audit Manager creates a managed policy named `AWSAuditManagerAdministratorAccess` for Audit Manager administrators. This policy grants full administration access in Audit Manager. Administrators can attach this policy to any existing role or user, or create a new role with this policy.

### Recommended policies for user personas in AWS Audit Manager
<a name="security_iam_service-with-iam-id-based-policies-personas"></a>

AWS Audit Manager enables you to maintain the segregation of duties among different users and for different audits by using different IAM policies. The two personas in Audit Manager and their recommended policies are defined as follows.


| Persona | Description and recommended policy | 
| --- | --- | 
| **Audit owner** |  +  This persona must have the necessary permissions to manage assessments in AWS Audit Manager.  <br />+  The recommended policy to use for this persona is the managed policy named [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html). You can use this policy as a starting point, and scope down these permissions as needed to fit your requirements.   | 
| **Delegate** |  +  This persona can access the delegated control sets in an assessment. They can update the control status, add comments, submit a control set for review, and add evidence to the assessment report. <br />+  The recommended policy to use for this persona is the following example policy: [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access). You can use this policy as a starting point, and make changes as necessary to fit your requirements.   | 

### Identity-based policy examples for AWS Audit Manager
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Audit Manager identity-based policies, see [Identity-based policy examples for AWS Audit Manager](security_iam_id-based-policy-examples.md).

## Resource-based policies within AWS Audit Manager
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

Although AWS Audit Manager does not allow you to manage resource-based policies through IAM, the service internally implements and manages resource-based policies for the following two scenarios:
+ When audit owners are assigned to an assessment, a resource-based policy is attached to the assessment with the principal as the audit owner. For more information, see [Step 3: Specify audit owners](create-assessments.md#choose-audit-owners) and [Step 3: Edit audit owners](edit-assessment.md#edit-choose-audit-owners).
+ When a control set of an assessment is delegated, a resource-based policy is attached to the control set with the principal as the delegate. For more information, see [Delegating a control set for review in AWS Audit Manager](delegation-for-audit-owners-delegating-a-control-set.md).

## Policy actions for AWS Audit Manager
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.



To see a list of AWS Audit Manager actions, see [Actions defined by AWS Audit Manager](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsauditmanager.html#awsauditmanager-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in AWS Audit Manager use the following prefix before the action.

```
auditmanager
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "auditmanager:{{GetEvidenceDetails}}",
      "auditmanager:{{GetEvidenceEventDetails}}"
         ]
```



You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Get`, include the following action.

```
"Action": "auditmanager:Get*"
```

To view examples of Audit Manager identity-based policies, see [Identity-based policy examples for AWS Audit Manager](security_iam_id-based-policy-examples.md).

## Policy resources for AWS Audit Manager
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of AWS Audit Manager resource types and their ARNs, see [Resources defined by AWS Audit Manager](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsauditmanager.html#awsauditmanager-resources-for-iam-policies) in the *Service Authorization Reference*. To learn about actions with which you can specify the ARN of each resource, see [Actions defined by AWS Audit Manager](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsauditmanager.html#awsauditmanager-actions-as-permissions).





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

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify the `i-1234567890abcdef0` assessment in your statement, use the following ARN.

```
"Resource": "arn:aws:auditmanager:us-east-1:123456789012:assessment/i-1234567890abcdef0"
```

To specify all instances that belong to a specific account, use the wildcard (\*).

```
"Resource": "arn:aws:auditmanager:us-east-1:123456789012:assessment/*"
```

Some Audit Manager actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Many Audit Manager API actions involve multiple resources. For example, `ListAssessments` returns a list of assessment metadata that's accessible by the currently logged in AWS account. Therefore, a user must have permissions to view the assessments. To specify multiple resources in a single statement, separate the ARNs with commas. 

```
"Resource": [
      "resource1",
      "resource2"
```

To see a list of Audit Manager resource types and their ARNs, see [Resources Defined by AWS Audit Manager](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awskeymanagementservice.html#awskeymanagementservice-resources-for-iam-policies) in the *IAM User Guide*. To learn about actions with which you can specify the ARN of each resource, see [Actions Defined by AWS Audit Manager](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awskeymanagementservice.html#awskeymanagementservice-actions-as-permissions).

Some Audit Manager API actions support multiple resources. For example, `GetChangeLogs` accesses an `assessmentID`, `controlID`, and `controlSetId`, so a principal must have permissions to access each of these resources. To specify multiple resources in a single statement, separate the ARNs with commas. 

```
"Resource": [
      "assessmentId",
      "controlId",
      "controlSetId"
```

## Policy condition keys for AWS Audit Manager
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Partial

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element (or `Condition` *block*) lets you specify conditions in which a statement is in effect. The `Condition` element is optional. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. 

If you specify multiple `Condition` elements in a statement, or multiple keys in a single `Condition` element, AWS evaluates them using a logical `AND` operation. If you specify multiple values for a single condition key, AWS evaluates the condition using a logical `OR` operation. All of the conditions must be met before the statement's permissions are granted.

When the principal in a policy statement is an [AWS service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services), we strongly recommend that you use the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) or [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition keys in the policy. You can use these global condition context keys to help prevent the [confused deputy scenario](https://docs.aws.amazon.com/audit-manager/latest/userguide/cross-service-confused-deputy-prevention.html). The following documented policies show how you can use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in Audit Manager to prevent the confused deputy problem.
+ [Example policy for an SNS topic that's used for Audit Manager notifications](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#sns-topic-permissions)
+ [Example policy for a KMS key that's used with an SNS topic](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#sns-key-permissions)

You can also use placeholder variables when you specify conditions. For example, you can grant a user permission to access a resource only if it is tagged with their user name. For more information, see [IAM policy elements: variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) in the *IAM User Guide*. 

Audit Manager does not provide any service-specific condition keys, but it does support using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

## Access control lists (ACLs) in AWS Audit Manager
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with AWS Audit Manager
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

For more information about tagging AWS Audit Manager resources, see [Tagging AWS Audit Manager resources](tagging.md).

## Using temporary credentials with AWS Audit Manager
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Forward access sessions for AWS Audit Manager
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for AWS Audit Manager
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

**Warning**  
Changing the permissions for a service role might break AWS Audit Manager functionality. Edit service roles only when Audit Manager provides guidance to do so.

## Service-linked roles for AWS Audit Manager
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about service-linked roles for AWS Audit Manager, see [Using service-linked roles for AWS Audit Manager](using-service-linked-roles.md).