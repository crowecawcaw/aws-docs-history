# Managed query results

With managed query results, you can run SQL queries without providing an Amazon S3 bucket for
query result storage. This saves you from having to provision, manage, control access to,
and clean up your own S3 buckets. To get started, create a new workgroup or edit an existing
workgroup. Under **Query result configuration**, select **Athena
managed**.

###### Key features

- Simplifies your workflow by removing the requirement to choose an S3 bucket
  location before you run queries.
- No additional cost to use managed query results and automatic deletion of query
  results reduces administration overhead and the need for separate S3 bucket clean up
  processes.
- Simple to get started: new and pre-existing workgroups can be easily configured to
  use managed query results. You can have a mix of Athena managed and customer managed
  query results in your AWS account.
- Streamlined IAM permissions with access to read results through
  `GetQueryResults` and `GetQueryResultsStream` tied to
  individual workgroups.
- Query results are automatically encrypted with your choice of AWS owned keys or
  customer owned keys.

## Considerations and limitations

######

- Access to query results is managed at the workgroup level in Athena. For this,
  you need explicit permissions to `GetQueryResults` and
  `GetQueryResultsStream` IAM actions on the specific workgroup.
  The `GetQueryResults` action determines who can retrieve the results
  of a completed query in a paginated format, while the
  `GetQueryResultsStream` action determines who can stream the
  results of a completed query (commonly used by Athena drivers).
- You cannot download query result files larger than 200 MB from the console. Use the
  `UNLOAD` statement to write results larger than 200 MB to a
  location that you can download separately.
- Managed query results feature does not support [Query
  result reuse](reusing-query-results.md "reusing-query-results.md").
- Query results are available for 24 hours. Query results are stored at no cost
  to you during this period. After this period, query results are automatically
  deleted.

## Create or edit a workgroup with managed

query results

To create a workgroup or update an existing workgroup with managed query results from
the console:

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/ "https://console.aws.amazon.com/athena/").
2. From the left navigation, choose **Workgroups**.
3. Choose **Create Workgroup** to create a new workgroup or edit an existing
   workgroup from the list.
4. Under **Query result configuration**, choose **Athena
   managed**.

![The Query result configuration menu.](images/athena-managed.png) 5. For **Encrypt query results**, choose the encryption option
that you want. For more information, see [Choose query result
encryption](#managed-query-results-encryption-at-rest "#managed-query-results-encryption-at-rest"). 6. Fill in all the other required details and choose **Save
changes**.

## Choose query result

encryption

There are two options for encryption configuration:

- **Encrypt using an AWS owned key** –
  This is the default option when you use managed query results. Choose this option if you want
  query results encrypted by an AWS owned key.
- **Encrypt using customer managed key** –
  Choose this option if you want to encrypt and decrypt query results with a
  customer managed key. To use a customer managed key, add the Athena service in
  the Principal element of the key policy section. For more information, see [Set up an AWS KMS key policy for managed query results](#managed-query-results-set-up "#managed-query-results-set-up"). To run queries successfully,
  the user running queries needs permission to access the AWS KMS key.

## Set up an AWS KMS key policy for managed query results

The `Principal` section on the key policy specifies who can use this key.
The managed query results feature introduces the principal `encryption.athena.amazonaws.com`
that you must specify in the `Principal` section. This service principal is
specifically for accessing keys not owned by Athena. You must also add the
`kms:Decrypt`, `kms:GenerateDataKey`, and
`kms:DescribeKey` actions to the key policy that you use to access
managed results. These three actions are the minimum allowed actions.

Managed query results uses your workgroup ARN for [encryption
context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context"). Because the `Principal` section is an AWS service, you
also need to add `aws:sourceArn` and `aws:sourceAccount` to the
key policy conditions. The following example shows an AWS KMS key policy that has minimum
permissions on a single workgroup.

```
 {
    "Sid": "Allow athena service principal to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": "encryption.athena.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:DescribeKey"
      ],
    "Resource": "arn:aws:kms:us-east-1:{`account-id`}:key/{`key-id`}",
    "Condition": {
    "ArnLike": {
        "kms:EncryptionContext:aws:athena:arn": "arn:aws:athena:us-east-1:{`account-id`}:workgroup/{`workgroup-name`}",
        "aws:SourceArn": "arn:aws:athena:us-east-1:{`account-id`}:workgroup/{`workgroup-name`}"
    },
    "StringEquals": {
        "aws:SourceAccount": "{`account-id`}"
    }
}
```

The following example AWS KMS key policy allows all workgroups within the same account
`account-id` to use the same AWS KMS key.

```
{
    "Sid": "Allow athena service principal to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": "encryption.athena.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:DescribeKey"
    ],
    "Resource": "arn:aws:kms:us-east-1:`account-id`:key/{`key-id`}",
    "Condition": {
        "ArnLike": {
          "kms:EncryptionContext:aws:athena:arn": "arn:aws:athena:us-east-1:`account-id`:workgroup/*",
          "aws:SourceArn": "arn:aws:athena:us-east-1:`account-id`:workgroup/*"
        },
        "StringEquals": {
          "aws:SourceAccount": "`account-id`"
        }
    }
}
```

In addition to the Athena and Amazon S3 permissions, you must also get permissions to
perform `kms:GenerateDataKey` and `kms:Decrypt` actions. For more
information, see [Permissions to
encrypted data in Amazon S3](encryption.md#permissions-for-encrypting-and-decrypting-data "encryption.md#permissions-for-encrypting-and-decrypting-data").

For more information on managed query results encryption, see [Encrypt managed query results](encrypting-managed-results.md "encrypting-managed-results.md").
