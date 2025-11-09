AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# How AWS Mainframe Modernization works with

IAM

Before you use IAM to manage access to AWS Mainframe Modernization, learn what IAM features are
available to use with AWS Mainframe Modernization.

| IAM features you can use with AWS Mainframe Modernization                                                                                                | IAM feature | AWS Mainframe Modernization support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------------- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | No          |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Yes         |
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                        | No          |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                  | Yes         |
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                                 | Yes         |
| [Forward access sessions (FAS)](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")             | Yes         |
| [Service roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                             | Yes         |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | Yes         |

To get a high-level view of how AWS Mainframe Modernization and other AWS services work with most
IAM features, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Identity-based

policies for AWS Mainframe Modernization

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

###

Identity-based policy examples for AWS Mainframe Modernization

To view examples of AWS Mainframe Modernization identity-based policies, see [Identity-based policy examples
for AWS Mainframe Modernization](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based policies within AWS Mainframe Modernization

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

## Policy

actions for AWS Mainframe Modernization

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of AWS Mainframe Modernization actions, see [Actions Defined by AWS Mainframe Modernization](../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in AWS Mainframe Modernization use the following prefix before the action:

```
m2
```

To specify multiple actions in a single statement, separate them with
commas.

```
"Action": [
      "m2:`StartApplication`",
      "m2:`StopApplication`"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `List`, include the following
action:

```
"Action": "m2:List*"
```

To view examples of AWS Mainframe Modernization identity-based policies, see [Identity-based policy examples
for AWS Mainframe Modernization](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy

resources for AWS Mainframe Modernization

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

You can restrict access to specific AWS Mainframe Modernization resources by using their ARNs to
identify the resource that the IAM policy applies to. For more information about
the format of ARNs, see [Amazon Resource Names
(ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _AWS General Reference_.

For example, an AWS Mainframe Modernization environment has the following ARN.

```
"Resource": "arn:aws:m2:`regionId`:`accountId`:env/`service-generated-unique-identifier`"
```

An AWS Mainframe Modernization application has the following ARN.

```
"Resource": "arn:aws:m2:`regionId`:`accountId`:app/`service-generated-unique-identifier`"
```

Not all AWS Mainframe Modernization actions support resource-level permissions. For actions that
don't support resource-level permissions, you must use the wildcard (\*).

The following AWS Mainframe Modernization actions do not support resource-level permissions.

```
ListApplications
            ListApplicationVersions
            ListBatchJobDefinitions
            ListBatchJobExecutions
            ListDataSetImportHistory
            ListDataSets
            ListDeployments
            ListEngineVersions
            ListEnvironments
            ListTagsForResource
```

To see a list of AWS Mainframe Modernization resource types and their ARNs, see
[Resources Defined by AWS Mainframe Modernization](../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-resources-for-iam-policies") in the _Service Authorization Reference_. To learn with
which actions you can specify the ARN of each resource, see
[Actions Defined by AWS Mainframe Modernization](../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-actions-as-permissions").

To view examples of AWS Mainframe Modernization identity-based policies, see [Identity-based policy examples
for AWS Mainframe Modernization](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy condition keys for AWS Mainframe Modernization

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

The following condition keys are specific to AWS Mainframe Modernization

```
m2:EngineType
            m2:InstanceType
```

To see a list of AWS Mainframe Modernization condition keys, see [Condition Keys for AWS Mainframe Modernization](../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-policy-keys "../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and resources
you can use a condition key, see [Actions Defined by AWS Mainframe Modernization](../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsmainframemodernizationservice.md#awsmainframemodernizationservice-actions-as-permissions").

To view examples of AWS Mainframe Modernization identity-based policies, see [Identity-based policy examples
for AWS Mainframe Modernization](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Access control lists (ACLs) in

AWS Mainframe Modernization

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control

(ABAC) with AWS Mainframe Modernization

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using Temporary

credentials with AWS Mainframe Modernization

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Forward access sessions for AWS Mainframe Modernization

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

###### Important

These tokens give AWS Mainframe Modernization access to customer data without your explicit
agreement; for example, AWS Mainframe Modernization deploys application artifacts with associated
business data from an Amazon S3 bucket without obtaining explicit permission from the
customer. You might need to update any compliance documentation
accordingly.

## Service roles for

AWS Mainframe Modernization

**Supports service roles:**

Yes

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

AWS Mainframe Modernization supports service roles for activity hooks (transaction / jobs abend or
completion, etc).

###### Warning

Changing the permissions for a service role might break AWS Mainframe Modernization
functionality. Edit service roles only when AWS Mainframe Modernization provides guidance to do
so.

### Choosing an IAM

role in AWS Mainframe Modernization

If you have previously created an IAM role that your applications running on
Amazon EC2 can assume, you can choose this role when you create a launch template or
launch configuration. AWS Mainframe Modernization provides you with a list of roles to choose
from. When creating these roles, it's important to associate least privilege
IAM policies that restrict access to the specific API calls that the
application requires. For more information, see [IAM role for applications
that run on Amazon EC2 instances](../../../autoscaling/ec2/userguide/us-iam-role.md "../../../autoscaling/ec2/userguide/us-iam-role.md") in the
_Amazon EC2 Auto Scaling User Guide_.

## Service-linked

roles for AWS Mainframe Modernization

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing AWS Mainframe Modernization service-linked roles, see [Using service-linked roles for
AWS Mainframe Modernization](using-service-linked-roles.md "using-service-linked-roles.md").

For details about creating or managing service-linked roles, see [AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find a service in the table that includes
a `Yes` in the **Service-linked role** column. Choose
the **Yes** link to view the service-linked role documentation for
that service.
