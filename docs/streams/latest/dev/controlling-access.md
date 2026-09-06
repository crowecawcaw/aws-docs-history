

# Controlling access to Amazon Kinesis Data Streams resources using IAM
<a name="controlling-access"></a>

AWS Identity and Access Management (IAM) enables you to do the following:
+ Create users and groups under your AWS account
+ Assign unique security credentials to each user under your AWS account
+ Control each user's permissions to perform tasks using AWS resources
+ Allow the users in another AWS account to share your AWS resources
+ Create roles for your AWS account and define the users or services that can assume them
+ Use existing identities for your enterprise to grant permissions to perform tasks using AWS resources

By using IAM with Kinesis Data Streams, you can control whether users in your organization can perform a task using specific Kinesis Data Streams API actions and whether they can use specific AWS resources.

If you are developing an application using the Kinesis Client Library (KCL), your policy must include permissions for Amazon DynamoDB and Amazon CloudWatch; the KCL uses DynamoDB to track state information for the application, and CloudWatch to send KCL metrics to CloudWatch on your behalf. For more information about the KCL, see [Develop KCL 1.x consumers](developing-consumers-with-kcl.md).

For more information about IAM, see the following:
+ [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
+ [Getting started with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)
+ [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)

For more information about IAM and Amazon DynamoDB, see [Using IAM to Control Access to Amazon DynamoDB Resources](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/UsingIAMWithDDB.html) in the *Amazon DynamoDB Developer Guide*. 

For more information about IAM and Amazon CloudWatch, see [Controlling User Access to Your AWS Account](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/UsingIAM.html) in the *Amazon CloudWatch User Guide*.

**Topics**
+ [Policy syntax](#policy-syntax)
+ [Actions for Kinesis Data Streams](#kinesis-using-iam-actions)
+ [Amazon Resource Names (ARNs) for Kinesis Data Streams](#kinesis-using-iam-arn-format)
+ [Example policies for Kinesis Data Streams](#kinesis-using-iam-examples)
+ [Share your data stream with another account](#sharing-data-streams)
+ [Configure an AWS Lambda function to read from Kinesis Data Streams in another account](#sharing-data-streams-example)
+ [Share access using resource-based policies](resource-based-policy-examples.md)
+ [Access control for streaming tables and Amazon S3 delivery](controlling-access-data-delivery.md)

## Policy syntax
<a name="policy-syntax"></a>

An IAM policy is a JSON document that consists of one or more statements. Each statement is structured as follows:

```
{
  "Statement":[{
    "Effect":"{{effect}}",
    "Action":"{{action}}",
    "Resource":"{{arn}}",
    "Condition":{
      "{{condition}}":{
        "{{key}}":"{{value}}"
        }
      }
    }
  ]
}
```

There are various elements that make up a statement:
+ **Effect:** The *effect* can be `Allow` or `Deny`. By default, IAM users don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows.
+ **Action**: The *action* is the specific API action for which you are granting or denying permission.
+ **Resource**: The resource that's affected by the action. To specify a resource in the statement, you need to use its Amazon Resource Name (ARN).
+ **Condition**: Conditions are optional. They can be used to control when your policy will be in effect.

As you create and manage IAM policies, you might want to use the [IAM Policy Generator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-generator) and the [IAM Policy Simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html).

## Actions for Kinesis Data Streams
<a name="kinesis-using-iam-actions"></a>

In an IAM policy statement, you can specify any API action from any service that supports IAM. For Kinesis Data Streams, use the following prefix with the name of the API action: `kinesis:`. For example: `kinesis:CreateStream`, `kinesis:ListStreams`, and `kinesis:DescribeStreamSummary`.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": ["kinesis:action1", "kinesis:action2"]
```

You can also specify multiple actions using wildcards. For example, you can specify all actions whose name begins with the word "Get" as follows:

```
"Action": "kinesis:Get*"
```

To specify all Kinesis Data Streams operations, use the \* wildcard as follows:

```
"Action": "kinesis:*"
```

For the complete list of Kinesis Data Streams API actions, see the [Amazon Kinesis API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/).

## Amazon Resource Names (ARNs) for Kinesis Data Streams
<a name="kinesis-using-iam-arn-format"></a>

Each IAM policy statement applies to the resources that you specify using their ARNs.

Use the following ARN resource format for Kinesis data streams:

```
arn:aws:kinesis:{{region}}:{{account-id}}:stream/{{stream-name}}
```

For example:

```
"Resource": arn:aws:kinesis:*:111122223333:stream/my-stream
```

## Example policies for Kinesis Data Streams
<a name="kinesis-using-iam-examples"></a>

The following example policies demonstrate how you could control user access to your Kinesis data streams.

------
#### [ Example 1: Allow users to get data from a stream ]

**Example**  
 This policy allows a user or group to perform the `DescribeStreamSummary`, `GetShardIterator`, and `GetRecords` operations on the specified stream and `ListStreams` on any stream. This policy could be applied to users who should be able to get data from a specific stream.     
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kinesis:Get*",
                "kinesis:DescribeStreamSummary"
            ],
            "Resource": [
            "arn:aws:kinesis:{{us-east-1}}:{{111122223333}}:stream/{{stream1}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesis:ListStreams"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

------
#### [ Example 2: Allow users to add data to any stream in the account ]

**Example**  
This policy allows a user or group to use the `PutRecord` operation with any of the account's streams. This policy could be applied to users that should be able to add data records to all streams in an account.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kinesis:PutRecord"
            ],
            "Resource": [
                "arn:aws:kinesis:{{us-east-1}}:{{111122223333}}:stream/*"
            ]
        }
    ]
}
```

------
#### [ Example 3: Allow any Kinesis Data Streams action on a specific stream ]

**Example**  
This policy allows a user or group to use any Kinesis Data Streams operation on the specified stream. This policy could be applied to users that should have administrative control over a specific stream.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "kinesis:*",
            "Resource": [
            "arn:aws:kinesis:{{us-east-1}}:{{111122223333}}:stream/{{stream1}}"
            ]
        }
    ]
}
```

------
#### [ Example 4: Allow any Kinesis Data Streams action on any stream ]

**Example**  
This policy allows a user or group to use any Kinesis Data Streams operation on any stream in an account. Because this policy grants full access to all your streams, you should restrict it to administrators only.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "kinesis:*",
            "Resource": [
                "arn:aws:kinesis:*:{{111122223333}}:stream/*"
            ]
        }
    ]
}
```

------

## Share your data stream with another account
<a name="sharing-data-streams"></a>

**Note**  
 Kinesis Producer Library currently does not support specifying a stream ARN when writing to a data stream. Use the AWS SDK if you want to write to a cross-account data stream. 

Attach a [resource-based policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based) to your data stream to grant access to another account, IAM user, or IAM role. Resource-based policies are JSON policy documents that you attach to a resource such as a data stream. These policies grant the [specified principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) permission to perform specific actions on that resource and define under what conditions this applies. A policy can have multiple statements. You must specify a principal in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services. You can configure policies in the Kinesis Data Streams console, API or SDK. 

Note that sharing access to registered consumers such as [Enhanced Fan Out](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html) requires a policy on both the data stream ARN and the consumer ARN. 

### Enable cross-account access
<a name="sharing-data-streams-enabling"></a>

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. Adding a cross-account principal to a resource-based policy is only half of establishing the trust relationship. When the principal and the resource are in separate AWS accounts, you must also use an identity-based policy to grant the principal access to the resource. However, if a resource-based policy grants access to a principal in the same account, no additional identity-based policy is required. 

For more information about using resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html).

Data stream administrators can use AWS Identity and Access Management policies to specify who has access to what. That is, which *principal* can perform *actions* on what *resources*, and under what *conditions*. The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Policy actions usually have the same name as the associated AWS API operation. 

Kinesis Data Streams actions that can be shared:


| Action | Level of access | 
| --- | --- | 
| [DescribeStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamConsumer.html) | Consumer | 
| [DescribeStreamSummary](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html) | Data stream | 
| [GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html) | Data stream | 
| [GetShardIterator](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html) | Data stream | 
| [ListShards](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListShards.html) | Data stream | 
| [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) | Data stream | 
| [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) | Data stream | 
| [SubscribeToShard](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html) | Consumer | 

Following are examples of using a resource-based policy to grant cross-account access to your data stream or registered consumer. 

To perform a cross-account action, you must specify the stream ARN for data stream access and the consumer ARN for registered consumer access. 

### Example resource-based policies for Kinesis data streams
<a name="kinesis-stream-sharing-iam-examples"></a>

Sharing a registered consumer involves both a data stream policy and a consumer policy due to the actions needed. 

**Note**  
Following are examples of valid values for `Principal`:  
`{"AWS": "123456789012"}`
IAM User – `{"AWS": "arn:aws:iam::123456789012:user/user-name"}`
IAM Role – `{"AWS":["arn:aws:iam::123456789012:role/role-name"]}`
Multiple Principals (can be combination of account, user, role) – `{"AWS":["123456789012", "123456789013", "arn:aws:iam::123456789012:user/user-name"]}`

------
#### [ Example 1: Write access to the data stream ]

**Example**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "__default_write_policy_ID",
    "Statement": [
        {
            "Sid": "writestatement",
            "Effect": "Allow",
            "Principal": {
                "AWS": "Account12345"
            },
            "Action": [
                "kinesis:DescribeStreamSummary",
                "kinesis:ListShards",
                "kinesis:PutRecord",
                "kinesis:PutRecords"
            ],
            "Resource": "arn:aws:kinesis:us-east-2:123456789012:stream/datastreamABC"
        }
    ]
}
```

------
#### [ Example 2: Read access to the data stream ]

**Example**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "__default_sharedthroughput_read_policy_ID",
    "Statement": [
        {
            "Sid": "sharedthroughputreadstatement",
            "Effect": "Allow",
            "Principal": {
                "AWS": "Account12345"
            },
            "Action": [                
                "kinesis:DescribeStreamSummary",
                "kinesis:ListShards",
                "kinesis:GetRecords",
                "kinesis:GetShardIterator"
            ],
            "Resource": "arn:aws:kinesis:us-east-2:123456789012:stream/datastreamABC"
        }
    ]
}
```

------
#### [ Example 3: Share enhanced fan-out read access to a registered consumer ]

**Example**  
Data stream policy statement:     
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "__default_sharedthroughput_read_policy_ID",
    "Statement": [
        {
            "Sid": "consumerreadstatement",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/role-name"
            },
            "Action": [
                "kinesis:DescribeStreamSummary",
                "kinesis:ListShards"
            ],
            "Resource": "arn:aws:kinesis:us-east-2:123456789012:stream/datastreamABC"
        }
    ]
}
```
Consumer policy statement:    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "__default_efo_read_policy_ID",
    "Statement": [
        {
            "Sid": "eforeadstatement",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/role-name"
            },
            "Action": [
                "kinesis:DescribeStreamConsumer",
                "kinesis:SubscribeToShard"
            ],
            "Resource": "arn:aws:kinesis:us-east-2:123456789012:stream/datastreamABC/consumer/consumerDEF:1674696300"
        }
    ]
}
```
Wildcard (\*) is not supported for actions or principal field in order maintain the principle of least privilege.. 

------

### Manage the policy for your data stream programmatically
<a name="sharing-data-streams-managing-policy"></a>

Outside of the AWS Management Console, Kinesis Data Streams has three APIS for managing your data stream policy: 
+ [PutResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutResourcePolicy.html)
+ [GetResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetResourcePolicy.html)
+ [DeleteResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeleteResourcePolicy.html)

Use `PutResourePolicy` to attach or overwrite a policy for a data stream or consumer. Use `GetResourcePolicy` to check and view a policy for the specified data stream or consumer. Use `DeleteResourcePolicy` to delete a policy for the specified data stream or consumer. 

### Policy limits
<a name="sharing-data-streams-validating"></a>

Kinesis Data Streams resource policies have the following restrictions: 
+ Wildcards (\*) are not supported to help prevent broad access from being granted through the resource policies that are directly attached to a data stream or registered consumer. In addition, carefully inspect the following policies to confirm that they do not grant broad access:
  + Identity-based policies attached to associated AWS principals (for example, IAM roles)
  + Resource-based policies attached to associated AWS resources (for example, AWS Key Management Service KMS keys)
+ AWS Service Principals are not supported for principals to prevent potential [confused deputies](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html). 
+ Federated principals are not supported. 
+ Canonical user IDs are not supported. 
+ The size of the policy cannot exceed 20KB. 

### Share access to encrypted data
<a name="sharing-access-to-encrypted-data-1"></a>

If you have enabled server-side encryption for a data stream with AWS managed KMS key and want to share access via a resource policy, you must switch to using customer-managed key (CMK). For more information, see [What is server-side encryption for Kinesis Data Streams?](what-is-sse.md). In addition, you must allow your sharing principal entities to have access to your CMK, using KMS cross account sharing capabilities. Make sure to also make the change in the IAM policies for the sharing principal entities. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html).

## Configure an AWS Lambda function to read from Kinesis Data Streams in another account
<a name="sharing-data-streams-example"></a>

For an example of how to configure a Lambda function to read from Kinesis Data Streams in another account, see [Share access with cross-account AWS Lambda functions](resource-based-policy-examples.md#Resource-based-policy-examples-lambda). 