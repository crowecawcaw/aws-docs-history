

# Configuring IAM
<a name="cdc-iam"></a>

CDC streams require two separate sets of IAM permissions:
+ **Caller permissions** – The IAM principal that calls the CDC stream API operations (`CreateStream`, `GetStream`, `DeleteStream`, `ListStreams`) needs permission for these actions and for `iam:PassRole`.
+ **Service role** – An IAM role that Aurora DSQL assumes at runtime to write CDC records to your target. You create this role, attach a trust policy that allows the Aurora DSQL service principal to assume it, and attach a permissions policy that grants write access to the target.

**Note**  
The CDC service role is separate from any resource-based policy on your Aurora DSQL cluster. A cluster resource-based policy controls which principals can connect to and query the cluster. The CDC service role controls which target Aurora DSQL can write CDC records to.

## Caller permissions
<a name="cdc-iam-caller-permissions"></a>

The IAM principal that calls the CDC stream API operations needs permissions for the relevant `dsql` actions and `iam:PassRole`. The `CreateStream` operation requires `iam:PassRole` because it passes the service role ARN to Aurora DSQL. The following is an example policy:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DSQLStreamActions",
            "Effect": "Allow",
            "Action": [
                "dsql:CreateStream",
                "dsql:GetStream",
                "dsql:ListStreams",
                "dsql:DeleteStream"
            ],
            "Resource": [
                "arn:aws:dsql:{{region}}:{{your-account-id}}:cluster/{{cluster-id}}",
                "arn:aws:dsql:{{region}}:{{your-account-id}}:cluster/{{cluster-id}}/stream/*"
            ]
        },
        {
            "Sid": "PassServiceRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{your-account-id}}:role/{{dsql-cdc-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "dsql.amazonaws.com"
                }
            }
        }
    ]
}
```

The `Resource` element includes both the cluster ARN (required by `CreateStream` and `ListStreams`) and the stream ARN pattern (required by `GetStream` and `DeleteStream`).

For a full list of permissions required for each operation, see [CreateStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateStream.html), [GetStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetStream.html), [DeleteStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteStream.html), and [ListStreams](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListStreams.html) in the [Amazon Aurora DSQL API Reference](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_api_reference.html).

## Service role
<a name="cdc-iam-service-role"></a>

The service role is the IAM role that Aurora DSQL assumes to write CDC records to your target. You create this role and pass its ARN in the `targetDefinition.kinesis.roleArn` field when you call `CreateStream`. The role requires a trust policy and a permissions policy.

## Service role trust policy
<a name="cdc-iam-trust-policy"></a>

The trust policy must allow the Aurora DSQL service principal to assume the role. To protect against [confused deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) attacks, use the `aws:SourceAccount` and `aws:SourceArn` condition keys.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DSQLAssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "dsql.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{your-account-id}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:dsql:{{region}}:{{your-account-id}}:cluster/{{cluster-id}}/stream/*"
                }
            }
        }
    ]
}
```

The `aws:SourceArn` condition restricts the role to streams under a specific cluster. You must use the wildcard (`stream/*`) when creating a stream because Aurora DSQL hasn't assigned the stream identifier yet. After you create a stream, you can tighten the condition to the exact stream ARN (`arn:aws:dsql:{{region}}:{{your-account-id}}:cluster/{{cluster-id}}/stream/{{stream-id}}`) if the role serves a single stream.

To use the role with streams on any cluster in your account, use a broader wildcard: `arn:aws:dsql:{{region}}:{{your-account-id}}:cluster/*/stream/*`.

To learn more about confused deputy prevention, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md) in this guide.

## Service role permissions policy
<a name="cdc-iam-permissions-policy"></a>

The permissions policy grants the service role access to write records to your Kinesis data stream. The following policy includes both Kinesis write permissions and AWS KMS permissions. The `KMSAccess` statement is only required if your Kinesis data stream uses an AWS KMS customer managed key, but you can include it preemptively so that adding a customer managed key later doesn't break your CDC stream.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "KinesisAccess",
            "Effect": "Allow",
            "Action": [
                "kinesis:PutRecord",
                "kinesis:PutRecords",
                "kinesis:DescribeStreamSummary",
                "kinesis:ListShards"
            ],
            "Resource": "arn:aws:kinesis:{{region}}:{{your-account-id}}:stream/{{kinesis-stream-name}}"
        },
        {
            "Sid": "KMSAccess",
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:*:*:key/*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "kinesis.{{region}}.amazonaws.com",
                    "kms:EncryptionContext:aws:kinesis:arn": "arn:aws:kinesis:{{region}}:{{your-account-id}}:stream/{{kinesis-stream-name}}",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}
```

The conditions in the AWS KMS statement provide the following protections:
+ `kms:ViaService` – Restricts key usage to requests that come through the Kinesis service in the specified Region.
+ `kms:EncryptionContext:aws:kinesis:arn` – Restricts key usage to encryption operations for the specified Kinesis data stream.
+ `aws:ResourceAccount` – The key must belong to the same AWS account as the calling principal, which prevents cross-account key usage.

**Note**  
The AWS KMS key referenced here is the encryption key on the Kinesis data stream, not the cluster's AWS KMS key. The cluster's encryption key protects CDC data inside the Aurora DSQL boundary. The Kinesis encryption key protects CDC data after Aurora DSQL writes it to the Kinesis data stream.

## Data protection
<a name="cdc-data-protection"></a>

Aurora DSQL uses Transport Layer Security (TLS) to encrypt CDC data in transit between Aurora DSQL and your target. Within the Aurora DSQL boundary, Aurora DSQL encrypts CDC data at rest by using the cluster's encryption key.

If the cluster uses an AWS KMS customer managed key and that key becomes inaccessible, an `ACTIVE` or `IMPAIRED` stream transitions to `IMPAIRED` with the error code `CLUSTER_CMK_INACCESSIBLE`. If the key becomes inaccessible before the stream finishes creating, the stream transitions directly to `FAILED`.

For a detailed explanation of encryption in Aurora DSQL, see [Data encryption for Amazon Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/data-encryption.html) in this guide.