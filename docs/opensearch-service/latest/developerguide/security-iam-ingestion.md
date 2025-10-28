# Identity and Access Management for

Amazon OpenSearch Ingestion

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use OpenSearch Ingestion resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Identity-based policies for
  OpenSearch Ingestion](#security-iam-ingestion-id-based-policies "#security-iam-ingestion-id-based-policies")
- [Policy actions for
  OpenSearch Ingestion](#security-iam-ingestion-id-based-policies-actions "#security-iam-ingestion-id-based-policies-actions")
- [Policy resources
  for OpenSearch Ingestion](#security-iam-ingestion-id-based-policies-resources "#security-iam-ingestion-id-based-policies-resources")
- [Policy condition keys for
  Amazon OpenSearch Ingestion](#security_iam_ingestion-conditionkeys "#security_iam_ingestion-conditionkeys")
- [ABAC with OpenSearch Ingestion](#security_iam_ingestion-with-iam-tags "#security_iam_ingestion-with-iam-tags")
- [Using temporary credentials with
  OpenSearch Ingestion](#security_iam_ingestion-tempcreds "#security_iam_ingestion-tempcreds")
- [Service-linked roles for
  OpenSearch Ingestion](#security_iam_ingestion-slr "#security_iam_ingestion-slr")
- [Identity-based policy
  examples for OpenSearch Ingestion](#security_iam_ingestion_id-based-policy-examples "#security_iam_ingestion_id-based-policy-examples")

## Identity-based policies for

OpenSearch Ingestion

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

### Identity-based policy

examples for OpenSearch Ingestion

To view examples of OpenSearch Ingestion identity-based policies, see [Identity-based policy
examples for OpenSearch Ingestion](#security_iam_ingestion_id-based-policy-examples "#security_iam_ingestion_id-based-policy-examples").

## Policy actions for

OpenSearch Ingestion

**Supports policy actions:**

Yes

The `Action` element of a JSON policy describes the actions that you can
use to allow or deny access in a policy. Policy actions usually have the same name as
the associated AWS API operation. There are some exceptions, such as
_permission-only actions_ that don't have a matching API
operation. There are also some operations that require multiple actions in a policy.
These additional actions are called _dependent actions_.

Include actions in a policy to grant permissions to perform the associated
operation.

Policy actions in OpenSearch Ingestion use the following prefix before the action:

```
osis
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "osis:`action1`",
      "osis:`action2`"
         ]
```

You can specify multiple actions using wildcard characters (\*). For example, to
specify all actions that begin with the word `List`, include the following
action:

```
"Action": "osis:List*"
```

To view examples of OpenSearch Ingestion identity-based policies, see [Identity-based policy
examples for OpenSearch Serverless](security-iam-serverless.md#security_iam_id-based-policy-examples "security-iam-serverless.md#security_iam_id-based-policy-examples").

## Policy resources

for OpenSearch Ingestion

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

## Policy condition keys for

Amazon OpenSearch Ingestion

**Supports service-specific policy condition keys:**

No

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of OpenSearch Ingestion condition keys, see [Condition keys for Amazon OpenSearch Ingestion](../../../service-authorization/latest/reference/list_amazonopensearchingestion.md#amazonopensearchingestion-policy-keys "../../../service-authorization/latest/reference/list_amazonopensearchingestion.md#amazonopensearchingestion-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and resources you
can use a condition key, see [Actions defined by Amazon OpenSearch Ingestion](../../../service-authorization/latest/reference/list_amazonopensearchingestion.md#amazonopensearchingestion-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonopensearchingestion.md#amazonopensearchingestion-actions-as-permissions").

## ABAC with OpenSearch Ingestion

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

For more information about tagging OpenSearch Ingestion resources, see [Tagging Amazon OpenSearch Ingestion pipelines](tag-pipeline.md "tag-pipeline.md").

## Using temporary credentials with

OpenSearch Ingestion

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Service-linked roles for

OpenSearch Ingestion

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

OpenSearch Ingestion uses a service-linked role called
`AWSServiceRoleForAmazonOpenSearchIngestionService`. The service-linked
role named `AWSServiceRoleForOpensearchIngestionSelfManagedVpce` is also
available for pipelines with self-managed VPC endpoints. For details about creating and
managing OpenSearch Ingestion service-linked roles, see [Using service-linked roles to create OpenSearch Ingestion
pipelines](slr-osis.md "slr-osis.md").

## Identity-based policy

examples for OpenSearch Ingestion

By default, users and roles don't have permission to create or modify OpenSearch Ingestion
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon OpenSearch Ingestion, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon OpenSearch Ingestion](../../../service-authorization/latest/reference/list_amazonopensearchingestion.md "../../../service-authorization/latest/reference/list_amazonopensearchingestion.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_ingestion-policy-best-practices "#security_iam_ingestion-policy-best-practices")
- [Using
  OpenSearch Ingestion in the console](#security_iam_ingestion_id-based-policy-examples-console "#security_iam_ingestion_id-based-policy-examples-console")
- [Administering
  OpenSearch Ingestion pipelines](#security_iam_id-based-policy-examples-pipeline-admin "#security_iam_id-based-policy-examples-pipeline-admin")
- [Ingesting data
  into an OpenSearch Ingestion pipeline](#security_iam_id-based-policy-examples-ingest-data "#security_iam_id-based-policy-examples-ingest-data")

### Policy best

practices

Identity-based policies are very powerful. They determine whether someone can
create, access, or delete OpenSearch Ingestion resources in your account. These actions
can incur costs for your AWS account. When you create or edit identity-based
policies, follow these guidelines and recommendations:

Identity-based policies determine whether someone can create, access, or delete OpenSearch Ingestion resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

### Using

OpenSearch Ingestion in the console

To access OpenSearch Ingestion within the OpenSearch Service console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
OpenSearch Ingestion resources in your AWS account. If you create an identity-based
policy that is more restrictive than the minimum required permissions, the console
won't function as intended for entities (such as IAM roles) with that
policy.

You don't need to allow minimum console permissions for users that are making
calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions
that match the API operation that you're trying to perform.

The following policy allows a user to access OpenSearch Ingestion within the OpenSearch Service
console:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Resource": "*",
 "Effect": "Allow",
 "Action": [
 "osis:ListPipelines",
 "osis:GetPipeline",
 "osis:ListPipelineBlueprints",
 "osis:GetPipelineBlueprint",
 "osis:GetPipelineChangeProgress"
 ]
 }
 ]
}`

```

Alternately, you can use the [AmazonOpenSearchIngestionReadOnlyAccess](ac-managed.md#AmazonOpenSearchIngestionReadOnlyAccess "ac-managed.md#AmazonOpenSearchIngestionReadOnlyAccess") AWS managed policy,
which grants read-only access to all OpenSearch Ingestion resources for an
AWS account.

### Administering

OpenSearch Ingestion pipelines

This policy is an example of a "pipeline admin" policy that allows a user to
manage and administer Amazon OpenSearch Ingestion pipelines. The user can create, view, and
delete pipelines.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Resource": "arn:aws:osis:`us-east-1`:`111122223333`:pipeline/*",
 "Action": [
 "osis:CreatePipeline",
 "osis:DeletePipeline",
 "osis:UpdatePipeline",
 "osis:ValidatePipeline",
 "osis:StartPipeline",
 "osis:StopPipeline"
 ],
 "Effect": "Allow"
 },
 {
 "Resource": "*",
 "Action": [
 "osis:ListPipelines",
 "osis:GetPipeline",
 "osis:ListPipelineBlueprints",
 "osis:GetPipelineBlueprint",
 "osis:GetPipelineChangeProgress"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

### Ingesting data

into an OpenSearch Ingestion pipeline

This example policy allows a user or other entity to ingest data into an
Amazon OpenSearch Ingestion pipeline in their account. The user can't modify the
pipelines.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Resource": "arn:aws:osis:`us-east-1`:`123456789012`:pipeline/*",
 "Action": [
 "osis:Ingest"
 ],
 "Effect": "Allow"
 }
 ]
}`

```
