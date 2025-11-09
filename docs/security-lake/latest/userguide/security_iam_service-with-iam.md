# How Security Lake works with IAM

Before you use IAM to manage access to Security Lake, learn what IAM features are
available to use with Security Lake.

| IAM features you can use with Amazon Security Lake                                                                                                       | IAM feature | Security Lake support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | Yes         |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Yes         |
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                        | No          |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                  | Yes         |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                              | Yes         |
| [Principal permissions](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                     | Yes         |
| [Service<br>roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                          | No          |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | Yes         |

To get a high-level view of how Security Lake and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based

policies for Security Lake

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

Security Lake supports identity-based policies. For more information, see [Identity-based policy examples for
Security Lake](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based

policies within Security Lake

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

The Security Lake service creates resource-based policies for the Amazon S3 buckets that store
your data. You don't attach these resource-based policies to your S3 buckets. Security Lake
automatically creates these policies on your behalf.

An example resource is an S3 bucket with an Amazon Resource Name (ARN) of
`arn:aws:s3:::aws-security-data-lake-{region}-{bucket-identifier}`. In
this example, `region` is a specific AWS Region where you've enabled
Security Lake, and `bucket-identifier` is a Regionally unique alphanumeric string
that Security Lake assigns to the bucket. Security Lake creates the S3 bucket to store data from
that Region. The resource policy defines which principals can perform actions on the
bucket. Here's a sample resource-based policy (bucket policy) that Security Lake attaches to
the bucket:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Principal": {
 "AWS": "*"
 },
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::aws-security-data-lake-{region}-{bucket-identifier}/*",
 "arn:aws:s3:::aws-security-data-lake-{region}-{bucket-identifier}"
 ],
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 },
 {
 "Sid": "PutSecurityLakeObject",
 "Effect": "Allow",
 "Principal": {
 "Service": "securitylake.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": [
 "arn:aws:s3:::aws-security-data-lake-{region}-{bucket-identifier}/*",
 "arn:aws:s3:::aws-security-data-lake-{region}-{bucket-identifier}"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{DA-AccountID}",
 "s3:x-amz-acl": "bucket-owner-full-control"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:securitylake:us-east-1:`111122223333`:*"
 }
 }
 }
 ]
}`

```

To learn more about resource-based policies, see [Identity-based
policies and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the
_IAM User Guide_.

## Policy actions

for Security Lake

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

For a list of Security Lake actions, see [Actions defined by Amazon Security Lake](../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in Security Lake use the following prefix before the action:

```
securitylake
```

For example, to grant a user permission to access information about a specific
subscriber, include the `securitylake:GetSubscriber` action in the policy
assigned to that user. Policy statements must include either an `Action` or
`NotAction` element. Security Lake defines its own set of actions that
describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "securitylake:`action1`",
      "securitylake:`action2`"
]
```

To view examples of Security Lake identity-based policies, see [Identity-based policy examples for
Security Lake](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy

resources for Security Lake

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Security Lake defines the following resource types: subscriber, and the data lake
configuration for an AWS account in a particular AWS Region. You can specify these
types of resources in policies by using ARNs.

For a list of Security Lake resource types and the ARN syntax for each one, see
[Resource types defined by Amazon Security Lake](../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-resources-for-iam-policies") in the _Service Authorization Reference_. To learn which
actions you can specify for each type of resource, see [Actions defined by Amazon Security Lake](../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-actions-as-permissions") in the
_Service Authorization Reference_.

To view examples of Security Lake identity-based policies, see [Identity-based policy examples for
Security Lake](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy

condition keys for Security Lake

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

For a list of Security Lake condition keys, see [Condition keys for Amazon Security Lake](../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-policy-keys "../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-policy-keys") in the
_Service Authorization Reference_. To learn which actions and resources you can
use a condition key with, see [Actions defined by Amazon Security Lake](../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-actions-as-permissions") in the
_Service Authorization Reference_. For examples of policies that use condition
keys, see [Identity-based policy examples for
Security Lake](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Access control lists (ACLs) in

Security Lake

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

Security Lake doesn't support ACLs, which means you can't attach an ACL to a Security Lake
resource.

## Attribute-based access control

(ABAC) with Security Lake

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

You can attach tags to Security Lake resources—subscribers, and the data lake
configuration for an AWS account in individual AWS Regions. You can also control
access to these types of resources by providing tag information in the
`Condition` element of a policy. For information about tagging Security Lake
resources, see [Tagging Security Lake resources](tagging-resources.md "tagging-resources.md").
For an example of an identity-based policy that controls access to a resource based on
the tags for that resource, see [Identity-based policy examples for
Security Lake](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Using temporary

credentials with Security Lake

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

Security Lake supports the use of temporary credentials.

## Forward access

sessions for Security Lake

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

Some Security Lake actions require permissions for additional, dependent actions in other
AWS services. For a list of these actions, see [Actions defined by Amazon Security Lake](../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonsecuritylake.md#amazonsecuritylake-actions-as-permissions") in the
_Service Authorization Reference_.

## Service roles for

Security Lake

**Supports service roles:**

No

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

Security Lake doesn't assume or use service roles. However, related services such as Amazon EventBridge, AWS Lambda, and Amazon S3 assume
service roles when you use Security Lake. To perform actions on your behalf,
Security Lake uses a service-linked role.

###### Warning

Changing the permissions for a service role may create operational issues with
your use of Security Lake. Edit service roles only when Security Lake provides guidance to do
so.

## Service-linked

roles for Security Lake

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

Security Lake uses an IAM service-linked role named
`AWSServiceRoleForAmazonSecurityLake`. The Security Lake service-linked role
grants permissions to operate a security data lake service on behalf of customers. This
service-linked role is an IAM role that's linked directly to Security Lake. It's
predefined by Security Lake, and it includes all the permissions that Security Lake requires to
call other AWS services on your behalf. Security Lake uses this service-linked role in all
the AWS Regions where Security Lake is available.

For details about creating or managing the Security Lake service-linked role, see [Using service-linked roles for
Security Lake](using-service-linked-roles.md "using-service-linked-roles.md").
