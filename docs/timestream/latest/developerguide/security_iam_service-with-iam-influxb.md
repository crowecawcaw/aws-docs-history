For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# How Amazon Timestream for InfluxDB works with IAM

| IAM features you can use with Amazon Timestream for InfluxDB                                                                                                                                   | IAM feature | Timestream for InfluxDB support |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------- |
| [Identity-based policies](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies") | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies-influxb "#security_iam_service-with-iam-resource-based-policies-influxb")                                     | No          |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions-influxb "#security_iam_service-with-iam-id-based-policies-actions-influxb")                                          | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources-influxb "#security_iam_service-with-iam-id-based-policies-resources-influxb")                                    | Yes         |
| [Policy condition<br>keys](#security_iam_service-with-iam-id-based-policies-conditionkeys-influxb "#security_iam_service-with-iam-id-based-policies-conditionkeys-influxb")                    | No          |
| [ACLs](#security_iam_service-with-iam-acls-influxb "#security_iam_service-with-iam-acls-influxb")                                                                                              | No          |
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags-influxb "#security_iam_service-with-iam-tags-influxb")                                                                           | Yes         |
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds-influxb "#security_iam_service-with-iam-roles-tempcreds-influxb")                                                       | Yes         |
| [Principal permissions](#security_iam_service-with-iam-principal-permissions-influxb "#security_iam_service-with-iam-principal-permissions-influxb")                                           | Yes         |
| [Service roles](#security_iam_service-with-iam-roles-service-influxb "#security_iam_service-with-iam-roles-service-influxb")                                                                   | No          |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked-influxb "#security_iam_service-with-iam-roles-service-linked-influxb")                                              | Yes         |

To get a high-level view of how Timestream for InfluxDB and other AWS services work with most IAM features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based policies for Timestream for InfluxDB

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

### Identity-based policy examples for

Timestream for InfluxDB

To view examples of Timestream for InfluxDB identity-based policies, see [Identity-based policy examples for Amazon Timestream for InfluxDB](security_iam_id-based-policy-examples-influxb.md "security_iam_id-based-policy-examples-influxb.md").

## Resource-based policies within

Timestream for InfluxDB

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

## Policy actions for Timestream for InfluxDB

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Timestream for InfluxDB actions, see [Actions,
resources and condition keys for Amazon Timestream for InfluxDB](../../../service-authorization/latest/reference/list_amazontimestreaminfluxdb.md "../../../service-authorization/latest/reference/list_amazontimestreaminfluxdb.md") in the
_Service Authorization Reference_.

Policy actions in Timestream for InfluxDB use the following prefix before the action:

```
timestream-influxdb
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "timestream-influxdb:`action1`",
      "timestream-influxdb:`action2`"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the
word `Describe`, include the following action:

```
"Action": "timestream-influxdb:Describe*"
```

## Policy resources for Timestream for InfluxDB

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Timestream for InfluxDB resource types and their ARNs, see [Resource
types defined by Amazon Timestream for InfluxDB](../../../service-authorization/latest/reference/list_amazontimestreaminfluxdb.md#amazontimestreaminfluxdb-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazontimestreaminfluxdb.md#amazontimestreaminfluxdb-resources-for-iam-policies") in the
_Service Authorization Reference_. To learn with which actions you can specify the ARN of each resource, see
[Actions,
resources and condition keys for Amazon Timestream for InfluxDB](../../../service-authorization/latest/reference/list_amazontimestreaminfluxdb.md "../../../service-authorization/latest/reference/list_amazontimestreaminfluxdb.md").

## Policy condition keys for

Timestream for InfluxDB

**Supports service-specific policy condition keys:**

No

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

## Access control lists (ACLs) in Timestream for InfluxDB

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with Timestream for InfluxDB

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using Temporary credentials with Timestream for InfluxDB

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Cross-service principal permissions for

Timestream for InfluxDB

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for Timestream for InfluxDB

**Supports service roles:**

No

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break Timestream for InfluxDB functionality. Edit service roles only when
Timestream for InfluxDB provides guidance to do so.

## Service-linked roles for Timestream for InfluxDB

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find
a service in the table that includes a `Yes` in the **Service-linked role** column.
Choose the **Yes** link to view the service-linked role documentation for that service.
