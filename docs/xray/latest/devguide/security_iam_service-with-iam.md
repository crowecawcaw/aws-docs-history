# How AWS X-Ray works with

IAM

Before you use IAM to manage access to X-Ray, you should understand what
IAM features are available to use with X-Ray. To get a high-level view of how
X-Ray and other AWS services work with IAM, see [AWS services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

You can use AWS Identity and Access Management (IAM) to grant X-Ray permissions to users and compute resources in your account. IAM
controls access to the X-Ray service at the API level to enforce permissions uniformly, regardless of which client
(console, AWS SDK, AWS CLI) your users employ.

To [use the X-Ray console](aws-xray-interface-console.md#xray-console "aws-xray-interface-console.md#xray-console") to view trace maps and segments, you only need
read permissions. To enable console access, add the `AWSXrayReadOnlyAccess`
[managed policy](security_iam_id-based-policy-examples.md#xray-permissions-managedpolicies "security_iam_id-based-policy-examples.md#xray-permissions-managedpolicies") to your IAM user.

For [local development and testing](#xray-permissions-local "#xray-permissions-local"), create an IAM role with
read and write permissions. [Assume the role](../../../IAM/latest/UserGuide/id_roles_use.md "../../../IAM/latest/UserGuide/id_roles_use.md") and store temporary credentials for the role.
You can use these credentials with the X-Ray daemon, the AWS CLI, and the AWS SDK. See
[using temporary security credentials with the AWS CLI](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md#using-temp-creds-sdk-cli "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md#using-temp-creds-sdk-cli")
for more information.

To [deploy your instrumented app to AWS](#xray-permissions-aws "#xray-permissions-aws"), create an IAM role with
write permissions and assign it to the resources running your application. `AWSXRayDaemonWriteAccess` includes
permission to upload traces, and some read permissions as well to support the use of [sampling rules](xray-console-sampling.md "xray-console-sampling.md").

The read and write policies do not include permission to configure [encryption key settings](xray-console-encryption.md "xray-console-encryption.md") and sampling rules. Use `AWSXrayFullAccess` to access these settings, or add
[configuration APIs](xray-api-configuration.md "xray-api-configuration.md") in a custom policy. For encryption and decryption
with a customer managed key that you create, you also need [permission to
use the key](#xray-permissions-encryption "#xray-permissions-encryption").

###### Topics

- [X-Ray
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [X-Ray
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  X-Ray tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Running your application locally](#xray-permissions-local "#xray-permissions-local")
- [Running your application in AWS](#xray-permissions-aws "#xray-permissions-aws")
- [User permissions for encryption](#xray-permissions-encryption "#xray-permissions-encryption")

## X-Ray

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
X-Ray supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in X-Ray use the following prefix before the action:
`xray:`. For example, to grant someone permission to
retrieve group resource details with the X-Ray `GetGroup` API operation, you include
the `xray:GetGroup` action in their policy. Policy statements must
include either an `Action` or `NotAction` element.
X-Ray defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "xray:*action1*",
      "xray:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Get`, include the following
action:

```
`"Action": "xray:Get*"`
```

To see a list of X-Ray actions, see [Actions Defined by AWS X-Ray](../../../IAM/latest/UserGuide/list_awsx-ray.md "../../../IAM/latest/UserGuide/list_awsx-ray.md") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

You can control access to resources by using an IAM policy. For actions that support resource-level
permissions, you use an Amazon Resource Name (ARN) to identify the resource that the policy applies to.

All X-Ray actions can be used in an IAM policy to grant or deny users permission to use that action.
However, not all [X-Ray actions](../api/API_Operations.md "../api/API_Operations.md") support resource-level permissions, which enable you to specify the resources on
which an action can be performed.

For actions that don't support resource-level permissions, you must use "`*`" as the
resource.

The following X-Ray actions support resource-level permissions:

- `CreateGroup`
- `GetGroup`
- `UpdateGroup`
- `DeleteGroup`
- `CreateSamplingRule`
- `UpdateSamplingRule`
- `DeleteSamplingRule`

The following is an example of an identity-based permissions policy for a `CreateGroup` action. The
example shows the use of an ARN relating to Group name `local-users` with the unique ID as a wildcard. The
unique ID is generated when the group is created, and so it can't be predicted in the policy in advance. When using
`GetGroup`, `UpdateGroup`, or `DeleteGroup`, you can define this as either a
wildcard or the exact ARN, including ID.

###### Note

The ARN of a sampling rule is defined by its name. Unlike group ARNs, sampling rules have no uniquely generated ID.

To see a list of X-Ray resource types and their ARNs, see
[Resources Defined by AWS X-Ray](../../../IAM/latest/UserGuide/list_awsx-ray.md#awsx-ray-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsx-ray.md#awsx-ray-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS X-Ray](../../../IAM/latest/UserGuide/list_awsx-ray.md "../../../IAM/latest/UserGuide/list_awsx-ray.md").

### Condition keys

X-Ray
does not provide any service-specific condition keys, but it does support using some
global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

### Examples

To view examples of X-Ray identity-based policies, see [AWS X-Ray identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## X-Ray

resource-based policies

X-Ray supports resource-based policies for current and future AWS service integration, such
as [Amazon SNS active tracing](../../../sns/latest/dg/sns-active-tracing.md "../../../sns/latest/dg/sns-active-tracing.md").
X-Ray resource-based policies can be updated by other AWS Management Consoles, or through the AWS SDK or
CLI. For example, the Amazon SNS console attempts to automatically configure resource-based policy for sending
traces to X-Ray. The following policy document provides an example of manually configuring X-Ray
resource-based policy.

###### Example X-Ray resource-based policy for Amazon SNS active tracing

This example policy document specifies the permissions that Amazon SNS needs to send trace data to X-Ray:

```
{
    Version: "2012-10-17",
    Statement: [
      {
        Sid: "SNSAccess",
        Effect: Allow,
        Principal: {
          Service: "sns.amazonaws.com",
        },
        Action: [
          "xray:PutTraceSegments",
          "xray:GetSamplingRules",
          "xray:GetSamplingTargets"
        ],
        Resource: "*",
        Condition: {
          StringEquals: {
            "aws:SourceAccount": "`account-id`"
          },
          StringLike: {
            "aws:SourceArn": "arn:`partition`:sns:`region`:`account-id`:`topic-name`"
          }
        }
      }
    ]
  }
```

Use the CLI to create a resource-based policy that gives Amazon SNS permissions to send trace data to X-Ray:

```
aws xray put-resource-policy --policy-name MyResourcePolicy --policy-document '{ "Version": "2012-10-17",		 	 	  "Statement": [ { "Sid": "SNSAccess", "Effect": "Allow", "Principal": { "Service": "sns.amazonaws.com" }, "Action": [ "xray:PutTraceSegments", "xray:GetSamplingRules", "xray:GetSamplingTargets" ], "Resource": "*", "Condition": { "StringEquals": { "aws:SourceAccount": "`account-id`" }, "StringLike": { "aws:SourceArn": "arn:`partition`:sns:`region`:`account-id`:`topic-name`" } } } ] }'
```

To use these examples, replace `partition`,
`region`, `account-id`, and
`topic-name` with your specific AWS partition, region, account ID, and
Amazon SNS topic name. To give all Amazon SNS topics permission to send trace data to X-Ray, replace the topic name with
`*`.

## Authorization based on

X-Ray tags

You can attach tags to X-Ray groups or sampling rules, or pass tags in a
request to X-Ray. To control access based on tags, you provide tag information
in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`xray:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging
X-Ray resources, see [Tagging X-Ray sampling rules and groups](xray-tagging.md "xray-tagging.md").

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [Managing
access to X-Ray groups and sampling rules based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-manage-sampling-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-manage-sampling-tags").

## Running your application locally

Your instrumented application sends trace data to the X-Ray daemon. The daemon buffers segment documents and
uploads them to the X-Ray service in batches. The daemon needs write permissions to upload trace data and
telemetry to the X-Ray service.

When you [run the daemon locally](xray-daemon-local.md "xray-daemon-local.md"), create an IAM role,
[assume the role](../../../IAM/latest/UserGuide/id_roles_use.md "../../../IAM/latest/UserGuide/id_roles_use.md")
and store temporary credentials in environment variables, or in a file named
`credentials` within a folder named `.aws` in your
user folder. See
[using temporary security credentials with the AWS CLI](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md#using-temp-creds-sdk-cli "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md#using-temp-creds-sdk-cli")
for more information.

###### Example ~/.aws/credentials

```
[default]
aws_access_key_id=`{access key ID}`
aws_secret_access_key=`{access key}`
aws_session_token=`{AWS session token}`
```

If you already configured credentials for use with the AWS SDK or AWS CLI, the daemon can use those. If multiple
profiles are available, the daemon uses the default profile.

## Running your application in AWS

When you run your application on AWS, use a role to grant permission to the Amazon EC2 instance or Lambda function
that runs the daemon.

- **Amazon Elastic Compute Cloud (Amazon EC2)** – Create an IAM role and attach it to the EC2 instance
  as an [instance profile](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md").
- **Amazon Elastic Container Service (Amazon ECS)** – Create an IAM role and attach it to container
  instances as a [container instance IAM role](../../../AmazonECS/latest/developerguide/instance_IAM_role.md "../../../AmazonECS/latest/developerguide/instance_IAM_role.md").
- **AWS Elastic Beanstalk (Elastic Beanstalk)** – Elastic Beanstalk includes X-Ray permissions in its [default instance profile](../../../elasticbeanstalk/latest/dg/concepts-roles.md#concepts-roles-instance "../../../elasticbeanstalk/latest/dg/concepts-roles.md#concepts-roles-instance"). You can use
  the default instance profile, or add write permissions to a custom instance profile.
- **AWS Lambda (Lambda)** – Add write permissions to your function's execution
  role.

###### To create a role for use with X-Ray

1.  Open the [IAM console](https://console.aws.amazon.com/iam/home "https://console.aws.amazon.com/iam/home").
2.  Choose **Roles**.
3.  Choose **Create New Role**.
4.  For **Role Name**, type `xray-application`. Choose **Next
    Step.**
5.  For **Role Type**, choose **Amazon EC2**.
6.  Attach the following managed policy to give your application access to AWS services:

        * **AWSXRayDaemonWriteAccess** – Gives the X-Ray daemon permission to upload trace
         data.

    If your application uses the AWS SDK to access other services, add policies that grant access to those
    services.

7.  Choose **Next Step**.
8.  Choose **Create Role**.

## User permissions for encryption

X-Ray encrypts all trace data and by default, and you can [configure
it to use a key that you manage](xray-console-encryption.md "xray-console-encryption.md"). If you choose a AWS Key Management Service customer managed key,
you need to ensure that the key's access policy lets you grant permission to X-Ray to use it to encrypt. Other
users in your account also need access to the key to view encrypted trace data in the X-Ray console.

For a customer managed key, configure your key with an access policy that allows the following actions:

- User who configures the key in X-Ray has permission to call `kms:CreateGrant` and
  `kms:DescribeKey`.
- Users who can access encrypted trace data have permission to call `kms:Decrypt`.

When you add a user to the **Key users** group in the key configuration section of the
IAM console, they have permission for both of these operations. Permission only needs to be set on the key
policy, so you don't need any AWS KMS permissions on your users, groups, or roles. For more information, see [Using Key Policies in the AWS KMS Developer Guide](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md").

For default encryption, or if you choose the AWS managed CMK (`aws/xray`), permission is based on
who has access to X-Ray APIs. Anyone with access to [`PutEncryptionConfig`](../api/API_PutEncryptionConfig.md "../api/API_PutEncryptionConfig.md"), included in
`AWSXrayFullAccess`, can change the encryption configuration. To prevent a user from changing the
encryption key, do not give them permission to use [`PutEncryptionConfig`](../api/API_PutEncryptionConfig.md "../api/API_PutEncryptionConfig.md").
