# How AWS Database Migration Service works with

IAM

Before you use IAM to manage access to AWS DMS, you should understand what
IAM features are available to use with AWS DMS. To get a high-level view of how
AWS DMS and other AWS services work with IAM, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [AWS DMS
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [AWS DMS
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  AWS DMS tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [IAM roles for AWS DMS](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")
- [Identity and access management for DMS Fleet Advisor](#fa-security-iam "#fa-security-iam")

## AWS DMS

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources, and also the conditions under which actions are allowed or denied.
AWS DMS supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in AWS DMS use the following prefix before the action:
`dms:`. For example, to grant someone permission to
create a replication task with the AWS DMS `CreateReplicationTask` API
operation, you include the `dms:CreateReplicationTask` action in their
policy. Policy statements must include either an `Action` or
`NotAction` element. AWS DMS defines its own set of actions
that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows.

```
"Action": [
      "dms:*action1*",
      "dms:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action.

```
`"Action": "dms:Describe*"`
```

To see a list of AWS DMS actions, see [Actions Defined by AWS Database Migration Service](../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

AWS DMS works with the following resources:

- Certificates
- Endpoints
- Event subscriptions
- Replication instances
- Replication subnet (security) groups
- Replication tasks

The resource or resources that AWS DMS requires depends on the action or actions
that you invoke. You need a policy that permits these actions on the associated
resource or resources specified by the resource ARNs.

For example, an AWS DMS endpoint resource has the following ARN:

```
arn:${Partition}:dms:${Region}:${Account}:endpoint/${InstanceId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS service namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `1A2B3C4D5E6F7G8H9I0J1K2L3M` endpoint
instance for the `us-east-2` region in your statement, use the following
ARN.

```
"Resource": "arn:aws:dms:us-east-2:987654321098:endpoint/1A2B3C4D5E6F7G8H9I0J1K2L3M"
```

To specify all endpoints that belong to a specific account, use the wildcard
(\*).

```
"Resource": "arn:aws:dms:us-east-2:987654321098:endpoint/*"
```

Some AWS DMS actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

Some AWS DMS API actions involve multiple resources. For example,
`StartReplicationTask` starts and connects a replication task to two
database endpoint resources, a source and a target, so an IAM user must have
permissions to read the source endpoint and to write to the target endpoint. To
specify multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*" ]
```

For more information on controlling access to AWS DMS resources using policies, see
[Using resource names
to control access](CHAP_Security.md#CHAP_Security.FineGrainedAccess.ResourceName "CHAP_Security.md#CHAP_Security.FineGrainedAccess.ResourceName"). To see a list of
AWS DMS resource types and their ARNs, see [Resources Defined by AWS Database Migration Service](../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-resources-for-iam-policies") in the
_IAM User Guide_. To learn with which actions you can specify
the ARN of each resource, see [Actions Defined by AWS Database Migration Service](../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

AWS DMS defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS global condition
context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

AWS DMS defines a set of standard tags that you can use in its condition keys and
also allows you defined your own custom tags. For more information, see [Using tags to control
access](CHAP_Security.md#CHAP_Security.FineGrainedAccess.Tags "CHAP_Security.md#CHAP_Security.FineGrainedAccess.Tags").

To see a list of AWS DMS condition keys, see [Condition Keys for AWS Database Migration Service](../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-policy-keys "../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-policy-keys")
in the _IAM User Guide_. To learn with which actions and
resources you can use a condition key, see [Actions Defined by AWS Database Migration Service](../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-actions-as-permissions") and
[Resources Defined by AWS Database Migration Service](../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsdatabasemigrationservice.md#awsdatabasemigrationservice-resources-for-iam-policies").

### Examples

To view examples of AWS DMS identity-based policies, see [AWS Database Migration Service identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## AWS DMS

resource-based policies

Resource-based policies are JSON policy documents that specify what actions a
specified principal can perform on a given AWS DMS resource and under what
conditions. AWS DMS supports resource-based permissions policies for AWS KMS encryption keys
that you create to encrypt data migrated to supported target endpoints. The supported
target endpoints include Amazon Redshift and Amazon S3. By using resource-based policies, you can grant
the permission for using these encryption keys to other accounts for each target
endpoint.

To enable cross-account access, you can specify an entire account or IAM entities
in another account as the [principal in a
resource-based policy](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md"). Adding a cross-account principal to a resource-based
policy is only half of establishing the trust relationship. When the principal and the
resource are in different AWS accounts, you must also grant the principal entity
permission to access the resource. Grant permission by attaching an identity-based
policy to the entity. However, if a resource-based policy grants access to a principal
in the same account, no additional identity-based policy is required. For more
information, see [How
IAM roles differ from resource-based policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the
_IAM User Guide_.

The AWS DMS service supports only one type of resource-based policy called a _key policy_, which is attached to an AWS KMS encryption key.
This policy defines which principal entities (accounts, users, roles, and federated
users) can encrypt migrated data on the supported target endpoint.

To learn how to attach a resource-based policy to an encryption key that you create
for the supported target endpoints, see [Creating and using AWS KMS keys to
encrypt Amazon Redshift target data](CHAP_Target.md#CHAP_Target.Redshift.KMSKeys "CHAP_Target.md#CHAP_Target.Redshift.KMSKeys") and [Creating AWS KMS keys to encrypt Amazon S3 target
objects](CHAP_Target.md#CHAP_Target.S3.KMSKeys "CHAP_Target.md#CHAP_Target.S3.KMSKeys").

### Examples

For examples of AWS DMS resource-based policies, see [Resource-based policy
examples for AWS KMS](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").

## Authorization based on

AWS DMS tags

You can attach tags to AWS DMS resources or pass tags in a request to
AWS DMS. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`dms:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition key. AWS DMS defines a set of standard tags that you
can use in its condition keys and also enables you to define your own custom tags. For
more information, see [Using tags to control
access](CHAP_Security.md#CHAP_Security.FineGrainedAccess.Tags "CHAP_Security.md#CHAP_Security.FineGrainedAccess.Tags").

For an example identity-based policy that limits access to a resource based on tags,
see [Accessing
AWS DMS resources based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-resources-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-resources-tags").

## IAM roles for AWS DMS

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with AWS DMS

You can use temporary credentials to sign in with federation, assume an IAM
role, or assume a cross-account role. You get temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

AWS DMS supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

For details about creating or managing AWS DMS service-linked roles, see
[Using service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md").

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

AWS DMS supports two types of service roles that you must create to use
certain source or target endpoints:

- Roles with permissions to allow AWS DMS access to the following source
  and target endpoints (or their resources):

      + Amazon DynamoDB as a target – For more information see [Prerequisites for using
       DynamoDB as a target for AWS Database Migration Service](CHAP_Target.md#CHAP_Target.DynamoDB.Prerequisites "CHAP_Target.md#CHAP_Target.DynamoDB.Prerequisites").
      + OpenSearch as a target – For more information see [Prerequisites for using
       Amazon OpenSearch Service as a target for AWS Database Migration Service](CHAP_Target.md#CHAP_Target.Elasticsearch.Prerequisites "CHAP_Target.md#CHAP_Target.Elasticsearch.Prerequisites").
      + Amazon Kinesis as a target – For more information see [Prerequisites for using a Kinesis
       data stream as a target for AWS Database Migration Service](CHAP_Target.md#CHAP_Target.Kinesis.Prerequisites "CHAP_Target.md#CHAP_Target.Kinesis.Prerequisites").
      + Amazon Redshift as a target – You need to create the specified role only
       for creating a custom KMS encryption key to encrypt the target data or
       for specifying a custom S3 bucket to hold intermediate task storage. For
       more information, see [Creating and using AWS KMS keys to
       encrypt Amazon Redshift target data](CHAP_Target.md#CHAP_Target.Redshift.KMSKeys "CHAP_Target.md#CHAP_Target.Redshift.KMSKeys") or [Amazon S3 bucket
       settings](CHAP_Target.md#CHAP_Target.Redshift.EndpointSettings.S3Buckets "CHAP_Target.md#CHAP_Target.Redshift.EndpointSettings.S3Buckets").
      + Amazon S3 as a source or as a target – For more information, see
       [Prerequisites when using Amazon S3 as a
       source for AWS DMS](CHAP_Source.md#CHAP_Source.S3.Prerequisites "CHAP_Source.md#CHAP_Source.S3.Prerequisites") or [Prerequisites for using Amazon S3 as a
       target](CHAP_Target.md#CHAP_Target.S3.Prerequisites "CHAP_Target.md#CHAP_Target.S3.Prerequisites").

  For example, to read data from an S3 source endpoint or to push data to an
  S3 target endpoint, you must create a service role as a prerequisite to
  accessing S3 for each of these endpoint operations.

- Roles with permissions required to use the AWS DMS console, the AWS CLI and AWS DMS API –
  Two IAM roles that you need to create are `dms-vpc-role` and
  `dms-cloudwatch-logs-role`. If you use Amazon Redshift as a target database,
  you must also create and add the IAM role
  `dms-access-for-endpoint` to your AWS account. For more
  information, see [Creating the IAM roles to use with AWS DMS](security-iam.md#CHAP_Security.APIRole "security-iam.md#CHAP_Security.APIRole").

### Choosing an IAM role

in AWS DMS

If you use the AWS DMS console, the AWS CLI or the AWS DMS API for your database migration, you must
add certain IAM roles to your AWS account before you can use the features of
AWS DMS. Two of these are `dms-vpc-role` and
`dms-cloudwatch-logs-role`. If you use Amazon Redshift as a target database, you
must also add the IAM role `dms-access-for-endpoint` to your AWS account.
For more information, see [Creating the IAM roles to use with AWS DMS](security-iam.md#CHAP_Security.APIRole "security-iam.md#CHAP_Security.APIRole").

## Identity and access management for DMS Fleet Advisor

With IAM identity-based policies, you can specify allowed or denied actions and
resources, and also the conditions under which actions are allowed or denied.
DMS Fleet Advisor supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

DMS Fleet Advisor uses IAM roles to access Amazon Simple Storage Service. An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your AWS account that has specific permissions.
For more information, see [Create IAM resources](fa-resources.md#fa-resources-iam "fa-resources.md#fa-resources-iam").
