# Control access to Amazon Kinesis Video Streams with WebRTC

resources with AWS Identity and Access Management

By using AWS Identity and Access Management (IAM) with Amazon Kinesis Video Streams with WebRTC, you can control whether users in
your organization can perform a task using specific Kinesis Video Streams with WebRTC API operations and
whether they can use specific AWS resources.

For more information about IAM, see the following:

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Getting started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md")
- [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")

###### Contents

- [Policy syntax](#policy-syntax "#policy-syntax")
- [API actions](#kinesis-using-iam-actions "#kinesis-using-iam-actions")
- [Amazon Resource Names (ARNs)](#kinesis-using-iam-arn-format "#kinesis-using-iam-arn-format")
- [Grant other IAM accounts access to a Kinesis video stream](#how-iam-crossaccount "#how-iam-crossaccount")
- [Example policies](#how-iam-policies "#how-iam-policies")

## Policy syntax

An IAM policy is a JSON document that consists of one or more statements. Each statement
is structured as follows:

```
{
  "Statement":[{
    "Effect":"`effect`",
    "Action":"`action`",
    "Resource":"`arn`",
    "Condition":{
      "`condition`":{
        "`key`":"`value`"
        }
      }
    }
  ]
}
```

There are various elements that make up a statement:

- **Effect:** The _effect_ can be `Allow`
  or `Deny`. By default, IAM users don't have permission to use resources and
  API actions, so all requests are denied. An explicit allow overrides the default. An
  explicit deny overrides any allows.
- **Action**: The _action_ is the specific API
  action for which you are granting or denying permission.
- **Resource**: The resource that's affected by the action. To specify
  a resource in the statement, you need to use its Amazon Resource Name (ARN).
- **Condition**: Conditions are optional. They can be used to control
  when your policy is in effect.

As you create and manage IAM policies, you might want to use the [IAM Policy
Generator](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-generator "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-generator") and the [IAM Policy Simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md").

## API actions

In an IAM policy statement, you can specify any API action from any service that
supports IAM. For Kinesis Video Streams with WebRTC, use the following prefix with the name of the API
action: `kinesisvideo:`. For example:
`kinesisvideo:CreateSignalingChannel`,
`kinesisvideo:ListSignalingChannels`, and
`kinesisvideo:DescribeSignalingChannel`.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": ["kinesisvideo:*action1*", "kinesisvideo:*action2*"]
```

You can also specify multiple actions using wildcards. For example, you can specify all
actions whose name begins with the word "Get" as follows:

```
"Action": "kinesisvideo:Get*"
```

To specify all Kinesis Video Streams operations, use the asterisk (\*) wild card as follows:

```
"Action": "kinesisvideo:*"
```

For the complete list of Kinesis Video Streams API actions, see the [_Kinesis Video Streams API
reference_](../../../kinesisvideostreams/latest/dg/API_Reference.md "../../../kinesisvideostreams/latest/dg/API_Reference.md").

## Amazon Resource Names (ARNs)

Each IAM policy statement applies to the resources that you specify using their
ARNs.

Use the following ARN resource format for Kinesis Video Streams:

```
arn:aws:kinesisvideo:`region`:`account-id`:channel/`channel-name`/`code`
```

For example:

```
"Resource": arn:aws:kinesisvideo::*:111122223333:channel/my-channel/0123456789012
```

You can get the ARN of a channel using [DescribeSignalingChannel](../../../kinesisvideostreams/latest/dg/API_DescribeStream.md "../../../kinesisvideostreams/latest/dg/API_DescribeStream.md").

## Grant other IAM accounts access to a Kinesis video stream

You might need to grant permission to other IAM accounts to perform operations on Kinesis Video Streams
with WebRTC signaling channels.

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

## Example policies

The following example policies demonstrate how you can control user access to your Kinesis Video Streams
with WebRTC channels.

###### Example 1: Allow users to get data from any signaling channel

This policy allows a user or group to perform the `DescribeSignalingChannel`,
`GetSignalingChannelEndpoint`, `ListSignalingChannels`, and
`ListTagsForResource` operations on any signaling channel.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:Describe*",
 "kinesisvideo:Get*",
 "kinesisvideo:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Example 2: Allow a user to create a signaling channel

This policy allows a user or group to perform the `CreateSignalingChannel`
operation.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:CreateSignalingChannel"
            ],
            "Resource": "*"
        }
    ]
}

```

###### Example 3: Allow a user full access to all Kinesis Video Streams and Kinesis Video Streams with WebRTC resources

This policy allows a user or group to perform any Kinesis Video Streams operation on any resource. This
policy is appropriate for administrators.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kinesisvideo:*",
 "Resource": "*"
 }
 ]
}`

```

###### Example 4: Allow a user to get data from a specific signaling channel

This policy allows a user or group to get data from a specific signaling channel.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kinesisvideo:DescribeSignalingChannel",
 "Resource": "arn:aws:kinesisvideo:us-west-2:123456789012:channel/channel_name/0123456789012"
 }
 ]
}`

```
