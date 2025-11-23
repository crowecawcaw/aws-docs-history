# Control CloudFormation access with AWS Identity and Access Management

With AWS Identity and Access Management (IAM), you can create IAM users and control their access to specific
resources in your AWS account. When you use IAM, you can control what users can do with
CloudFormation, such as whether they can view stack templates, create stacks, or delete
stacks.

Beyond CloudFormation-specific actions, you can manage what AWS services and resources are
available to each user. That way, you can control which resources users can access when they
use CloudFormation. For example, you can specify which users can create Amazon EC2 instances, terminate
database instances, or update VPCs. Those same permissions apply anytime they use CloudFormation
to do those actions.

Use the information in the following sections to control who can access CloudFormation. We will
also explore how to authorize IAM resource creation in templates, give applications running
on EC2 instances the permissions they need, and make use of temporary security credentials for
enhanced security in your AWS environment.

## Defining IAM identity-based policies for

CloudFormation

To give access to CloudFormation, you need to create and assign IAM policies that give
your IAM identities (such as users or roles) permission to call the API actions they
need.

With IAM identity-based policies, you can specify allowed or denied actions and
resources, as well as the conditions under which actions are allowed or denied. CloudFormation
supports specific actions, resources, and condition keys.

If you're new to IAM, start by familiarizing yourself with the elements of an IAM
JSON policy. For more information, see [IAM JSON policy element
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_. To learn how to create
IAM policies, complete the tutorial [Create and attach your first customer
managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the IAM documentation.

###### Topics

- [Policy actions for CloudFormation](#using-iam-actions "#using-iam-actions")
- [Console-specific actions for
  CloudFormation](#console-specific-actions "#console-specific-actions")
- [Policy resources for CloudFormation](#resource-level-permissions "#resource-level-permissions")
- [Policy condition keys for CloudFormation](#using-iam-conditions "#using-iam-conditions")

### Policy actions for CloudFormation

In the `Action` element of your IAM policy statement, you can specify
any API action that CloudFormation offers. You must prefix the action name with the
lowercase string `cloudformation:`. For example:
`cloudformation:CreateStack`, `cloudformation:CreateChangeSet`,
and `cloudformation:UpdateStack`.

To specify multiple actions in a single statement, separate them with commas, as
follows:

```
"Action": [ "cloudformation:`action1`", "cloudformation:`action2`" ]
```

You can also specify multiple actions using wildcards. For example, you can specify
all actions whose names begin with the word `Get`, as follows:

```
"Action": "cloudformation:Get*"
```

To see a complete list of actions associated with the `cloudformation`
service prefix, see [Actions,
resources, and condition keys for CloudFormation](../../../service-authorization/latest/reference/list_awscloudformation.md "../../../service-authorization/latest/reference/list_awscloudformation.md") and [Actions,
resources, and condition keys for AWS Cloud Control API](../../../service-authorization/latest/reference/list_awscloudcontrolapi.md "../../../service-authorization/latest/reference/list_awscloudcontrolapi.md") in the
_Service Authorization Reference_.

#### Examples

The following shows an example of a permissions policy that grants permissions to
view CloudFormation stacks.

###### Example 1: A sample policy that grants view

stack permissions

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Effect":"Allow",
 "Action":[
 "cloudformation:DescribeStacks",
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeStackResource",
 "cloudformation:DescribeStackResources"
 ],
 "Resource":"*"
 }]
}`

```

Users who create or delete stacks need additional permissions based on their stack
templates. For example, if your template describes an Amazon SQS queue, users must have
permissions for both CloudFormation and Amazon SQS actions, as shown in the following sample
policy.

###### Example 2: A sample policy that grants create

and view stack actions and all Amazon SQS actions

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Effect":"Allow",
 "Action":[
 "sqs:*",
 "cloudformation:CreateStack",
 "cloudformation:DescribeStacks",
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeStackResources",
 "cloudformation:GetTemplate",
 "cloudformation:ValidateTemplate"
 ],
 "Resource":"*"
 }]
}`

```

### Console-specific actions for

CloudFormation

Users of the CloudFormation console require additional permissions beyond those needed
for the AWS Command Line Interface or CloudFormation APIs. These additional permissions support
console-specific features such as template uploads to Amazon S3 buckets and drop-down lists
for AWS-specific parameter types.

For all actions listed below, grant permissions to all resources; don't limit them to
specific stacks or buckets.

The following action is used only by the CloudFormation console and is not documented in
the API reference. The action allows users to upload templates to Amazon S3 buckets.

- `cloudformation:CreateUploadBucket`

When users upload templates, users also require the following Amazon S3
permissions:

- `s3:PutObject`
- `s3:ListBucket`
- `s3:GetObject`
- `s3:CreateBucket`

To see values in the parameter drop-down lists for templates with AWS-specific
parameter types, users need permissions to make the corresponding describe API calls.
For example, the following permissions are required when these parameter types are used
in the template:

- `ec2:DescribeKeyPairs` – Required for the
  `AWS::EC2::KeyPair::KeyName` parameter type.
- `ec2:DescribeSecurityGroups` – Required for the
  `AWS::EC2::SecurityGroup::Id` parameter type.
- `ec2:DescribeSubnets` – Required for the
  `AWS::EC2::Subnet::Id` parameter type.
- `ec2:DescribeVpcs` – Required for the
  `AWS::EC2::VPC::Id` parameter type.

For more information about AWS-specific parameter types, see [Specify existing resources at
runtime with CloudFormation-supplied parameter types](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md").

### Policy resources for CloudFormation

In an IAM policy statement, the `Resource` element specifies the object
or objects that the statement covers. For CloudFormation, each IAM policy statement
applies to the resources that you specify using their Amazon Resource Names (ARNs). The
specific ARN format depends on the resource.

For a complete list of CloudFormation resource types and their ARNs, see [Resource types defined by CloudFormation](../../../service-authorization/latest/reference/list_awscloudformation.md#awscloudformation-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awscloudformation.md#awscloudformation-resources-for-iam-policies") in the
_Service Authorization Reference_. To learn with which actions you can specify with
each resource's ARN, see [Actions defined by CloudFormation](../../../service-authorization/latest/reference/list_awscloudformation.md#awscloudformation-actions-as-permissions "../../../service-authorization/latest/reference/list_awscloudformation.md#awscloudformation-actions-as-permissions").

You can specify actions for a specific stack, as shown in the following policy
example. When you provide an ARN, replace the `placeholder
 text` with your resource-specific information.

###### Example 1: A sample policy that denies

the delete and update stack actions for the specified stack

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "cloudformation:DeleteStack",
 "cloudformation:UpdateStack"
 ],
 "Resource": "arn:aws:cloudformation:`us-east-1`:`111122223333`:stack/`MyProductionStack`/*"
 }
 ]
}`

```

The policy above uses a wild card at the end of the stack name so that delete stack
and update stack are denied on both the full stack ID (such as
`arn:aws:cloudformation:`region`:`account-id`:stack/`MyProductionStack`/`abc9dbf0-43c2-11e3-a6e8-50fa526be49c`)
 and the stack name (such as
 `MyProductionStack``).

To allow `AWS::Serverless` transforms to create a change set, include the
`arn:aws:cloudformation:`region`:aws:transform/Serverless-2016-10-31`
resource-level permission, as shown in the following policy.

###### Example 2: A sample policy that allows

the create change set action for the specified transform

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateChangeSet"
 ],
 "Resource": "arn:aws:cloudformation:`us-east-1`:aws:transform/Serverless-2016-10-31"
 }
 ]
}`

```

### Policy condition keys for CloudFormation

In an IAM policy statement, you can optionally specify conditions that control when
a policy is in effect. For example, you can define a policy that allows users to create
a stack only when they specify a certain template URL. You can define
CloudFormation-specific conditions and AWS-wide conditions, such as
`DateLessThan`, which specifies when a policy stops taking effect. For
more information and a list of AWS-wide conditions, see Condition in [IAM policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition "../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition") in _IAM User Guide_.

###### Note

Don't use the `aws:SourceIp` AWS-wide condition. CloudFormation
provisions resources by using its own IP address, not the IP address of the
originating request. For example, when you create a stack, CloudFormation makes requests
from its IP address to launch an Amazon EC2 instance or to create an Amazon S3 bucket, not from
the IP address from the `CreateStack` call or the
**create-stack** command.

The following list describes the CloudFormation-specific conditions. These conditions are
applied only when users create or update stacks:

`cloudformation:ChangeSetName`

An CloudFormation change set name that you want to associate with a policy. Use
this condition to control which change sets users can execute or delete.

`cloudformation:ImportResourceTypes`

The template resource types that you want to associate with a policy, such
as `AWS::EC2::Instance`. Use this condition to control which
resource types users can work with when they import resources into a stack.
This condition is checked against the resource types that users declare in the
`ResourcesToImport` parameter, which is currently supported only
for AWS CLI and API requests. When using this parameter, you must specify all the
resource types you want users to control during import operations. For more
information about the `ResourcesToImport` parameter, see the [CreateChangeSet](../APIReference/API_CreateChangeSet.md "../APIReference/API_CreateChangeSet.md") action in the
_AWS CloudFormation API Reference_.

For a list of possible `ResourcesToImport`, see [Resource type
support](resource-import-supported-resources.md "resource-import-supported-resources.md").

Use the three-part resource naming convention to specify which resource
types users can work with, from all resources across an organization, down to
an individual resource type.

``organization`::\*`

Specify all resource types for a given organization.

``organization`::``service_name``::*`

Specify all resource types for the specified service within a given
organization.

``organization`::``service_name``::`resource_type``

Specify a specific resource type.

For example:

`AWS::*`

Specify all supported AWS resource types.

`AWS::`service_name`::*`

Specify all supported resources for a specific AWS
service.

`AWS::`service_name`::`resource_type``

Specify a specific AWS resource type, such as
`AWS::EC2::Instance` (all EC2 instances).

`cloudformation:ResourceTypes`

The template resource types, such as `AWS::EC2::Instance`, that
you want to associate with a policy. Use this condition to control which
resource types users can work with when they create or update a stack. This
condition is checked against the resource types that users declare in the
`ResourceTypes` parameter, which is currently supported only for
AWS CLI and API requests. When using this parameter, users must specify all the
resource types that are in their template. For more information about the
`ResourceTypes` parameter, see the [CreateStack](../APIReference/API_CreateStack.md "../APIReference/API_CreateStack.md")
action in the _AWS CloudFormation API Reference_.

For a list of resource types, see [CloudFormation Template Reference Guide](../TemplateReference/introduction.md "../TemplateReference/introduction.md").

Use the three-part resource naming convention to specify which resource
types users can work with, from all resources across an organization, down to
an individual resource type.

``organization`::\*`

Specify all resource types for a given organization.

``organization`::``service_name``::*`

Specify all resource types for the specified service within a given
organization.

``organization`::``service_name``::`resource_type``

Specify a specific resource type.

For example:

`AWS::*`

Specify all supported AWS resource types.

`AWS::`service_name`::*`

Specify all supported resources for a specific AWS
service.

`AWS::`service_name`::`resource_type``

Specify a specific AWS resource type, such as
`AWS::EC2::Instance` (all EC2 instances).

`Alexa::ASK::*`

Specify all resource types in the Alexa Skill Kit.

`Alexa::ASK::Skill`

Specify the individual [Alexa::ASK::Skill](../TemplateReference/alexa-resource-ask-skill.md "../TemplateReference/alexa-resource-ask-skill.md") resource type.

`Custom::*`

Specify all custom resources.

For more information, see [Create custom provisioning logic with custom
resources](template-custom-resources.md "template-custom-resources.md").

`Custom::`resource_type``

Specify a specific custom resource type.

For more information, see [Create custom provisioning logic with custom
resources](template-custom-resources.md "template-custom-resources.md").

`cloudformation:RoleARN`

The Amazon Resource Name (ARN) of an IAM service role that you want to
associate with a policy. Use this condition to control which service role users
can use when they work with stacks or change sets.

`cloudformation:StackPolicyUrl`

An Amazon S3 stack policy URL that you want to associate with a policy. Use this
condition to control which stack policies users can associate with a stack
during a create or update stack action. For more information about stack
policies, see [Prevent updates to stack resources](protect-stack-resources.md "protect-stack-resources.md").

###### Note

To ensure that users can only create or update stacks with the stack
policies that you uploaded, set the S3 bucket to read only for those
users.

`cloudformation:TemplateUrl`

An Amazon S3 template URL that you want to associate with a policy. Use this
condition to control which templates users can use when they create or update
stacks.

###### Note

To ensure that users can only create or update stacks with the templates
that you uploaded, set the S3 bucket to read only for those users.

###### Note

The following CloudFormation-specific conditions apply to the API parameters
of the same name:

- `cloudformation:ChangeSetName`
- `cloudformation:RoleARN`
- `cloudformation:StackPolicyUrl`
- `cloudformation:TemplateUrl`
  For example, `cloudformation:TemplateUrl` only applies to the
  `TemplateUrl` parameter for `CreateStack`,
  `UpdateStack`, and `CreateChangeSet` APIs.

For examples of IAM policies that use condition keys to control access, see [Example IAM identity-based
policies for CloudFormation](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Acknowledging IAM resources in CloudFormation

templates

Before you can create a stack, CloudFormation validates your template. During validation,
CloudFormation checks your template for IAM resources that it might create. IAM resources,
such as a user with full access, can access and modify any resource in your AWS account.
Therefore, we suggest that you review the permissions associated with each IAM resource
before proceeding so that you don't unintentionally create resources with escalated
permissions. To ensure that you've done so, you must acknowledge that the template contains
those resources, giving CloudFormation the specified capabilities before it creates the
stack.

You can acknowledge the capabilities of CloudFormation templates by using the CloudFormation
console, AWS Command Line Interface (AWS CLI), or API:

- In the CloudFormation console, on the **Configure stack options**
  page of the Create Stack or Update Stack wizards, choose **I acknowledge that
  this template may create IAM resources**.
- In the AWS CLI, when you use the [create-stack](../../../cli/latest/reference/cloudformation/create-stack.md "../../../cli/latest/reference/cloudformation/create-stack.md") and [update-stack](../../../cli/latest/reference/cloudformation/update-stack.md "../../../cli/latest/reference/cloudformation/update-stack.md") commands, specify the
  `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` value for the
  `--capabilities` option. If your template includes IAM resources, you
  can specify either capability. If your template includes custom names for IAM
  resources, you must specify `CAPABILITY_NAMED_IAM`.
- In the API, when you use the [CreateStack](../APIReference/API_CreateStack.md "../APIReference/API_CreateStack.md") and [UpdateStack](../APIReference/API_UpdateStack.md "../APIReference/API_UpdateStack.md") actions, specify
  `Capabilities.member.1=CAPABILITY_IAM` or
  `Capabilities.member.1=CAPABILITY_NAMED_IAM`. If your template includes
  IAM resources, you can specify either capability. If your template includes custom
  names for IAM resources, you must specify `CAPABILITY_NAMED_IAM`.

###### Important

If your template contains custom named IAM resources, don't create multiple stacks
reusing the same template. IAM resources must be globally unique within your account.
If you use the same template to create multiple stacks in different Regions, your stacks
might share the same IAM resources, rather than each having a unique one. Shared
resources among stacks can have unintended consequences from which you can't recover.
For example, if you delete or update shared IAM resources in one stack, you will
unintentionally modify the resources of other stacks.

## Managing credentials for applications running on

Amazon EC2 instances

If you have an application that runs on an Amazon EC2 instance and needs to make requests to
AWS resources such as Amazon S3 buckets or an DynamoDB table, the application requires AWS
security credentials. However, distributing and embedding long-term security credentials in
every instance that you launch is a challenge and a potential security risk. Instead of
using long-term credentials, like IAM user credentials, we recommend that you create an
IAM role that is associated with an Amazon EC2 instance when the instance is launched. An
application can then get temporary security credentials from the Amazon EC2 instance. You don't
have to embed long-term credentials on the instance. Also, to make managing credentials
easier, you can specify just a single role for multiple Amazon EC2 instances; you don't have to
create unique credentials for each instance.

For a template snippet that shows how to launch an instance with a role, see [IAM role template examples](quickref-iam.md#scenarios-iamroles "quickref-iam.md#scenarios-iamroles").

###### Note

Applications on instances that use temporary security credentials can call any
CloudFormation actions. However, because CloudFormation interacts with many other AWS
services, you must verify that all the services that you want to use support temporary
security credentials. For a list of the services that accept temporary security
credentials, see [AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Granting temporary access (federated

access)

In some cases, you might want to grant users with no AWS credentials temporary access
to your AWS account. Rather than creating and deleting long-term credentials whenever you
want to grant temporary access, use AWS Security Token Service (AWS STS). For example, you can use IAM
roles. From one IAM role, you can programmatically create and then distribute many
temporary security credentials (which include an access key, secret access key, and
security token). These credentials have a limited life, so they cannot be used to access
your AWS account after they expire. You can also create multiple IAM roles in order to
grant individual users different levels of permissions. IAM roles are useful for
scenarios like federated identities and single sign-on.

A federated identity is a distinct identity that you can use across multiple systems.
For enterprise users with an established on-premises identity system (such as LDAP or
Active Directory), you can handle all authentication with your on-premises identity system.
After a user has been authenticated, you provide temporary security credentials from the
appropriate IAM user or role. For example, you can create an administrators role and a
developers role, where administrators have full access to the AWS account and developers
have permissions to work only with CloudFormation stacks. After an administrator is
authenticated, the administrator is authorized to obtain temporary security credentials
from the administrators role. However, for developers, they can obtain temporary security
credentials from only the developers role.

You can also grant federated users access to the AWS Management Console. After users authenticate
with your on-premises identity system, you can programmatically construct a temporary URL
that gives direct access to the AWS Management Console. When users use the temporary URL, they won't
need to sign in to AWS because they have already been authenticated (single sign-on).
Also, because the URL is constructed from the users' temporary security credentials, the
permissions that are available with those credentials determine what permissions users have
in the AWS Management Console.

You can use several different AWS STS APIs to generate temporary security credentials. For
more information about which API to use, see [Compare AWS STS
credentials](../../../IAM/latest/UserGuide/id_credentials_sts-comparison.md "../../../IAM/latest/UserGuide/id_credentials_sts-comparison.md") in the _IAM User Guide_.

###### Important

You cannot work with IAM when you use temporary security credentials that were
generated from the `GetFederationToken` API. Instead, if you need to work
with IAM, use temporary security credentials from a role.

CloudFormation interacts with many other AWS services. When you use temporary security
credentials with CloudFormation, verify that all the services that you want to use support
temporary security credentials. For a list of the services that accept temporary security
credentials, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

For more information, see the following related resources in the
_IAM User Guide_:

- [Common
  scenarios for temporary credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md#sts-introduction "../../../IAM/latest/UserGuide/id_credentials_temp.md#sts-introduction")
- [Enable custom identity broker access to the AWS console](../../../IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.md")
