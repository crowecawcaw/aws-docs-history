# Configure AWS KMS key policies for CloudTrail

You can create an AWS KMS key in three ways:

- The CloudTrail console
- The AWS Management console
- The AWS CLI

###### Note

If you create a KMS key in the CloudTrail console, CloudTrail adds the required KMS key policy for you.
You do not need to manually add the policy statements. See [Default KMS key policy created in CloudTrail console](default-kms-key-policy.md "default-kms-key-policy.md").

If you create a KMS key in the AWS Management Console or the AWS CLI, you must add policy sections to the
key so that you can use it with CloudTrail. The policy must allow CloudTrail to use the key to encrypt
your log files, digest files, and event data stores, and allow the users you specify to read
log files and digest files in unencrypted form.

See the following resources:

- To create a KMS key with the AWS CLI, see [create-key](../../../cli/latest/reference/kms/create-key.md "../../../cli/latest/reference/kms/create-key.md").
- To edit a KMS key policy for CloudTrail, see [Editing a Key
  Policy](../../../kms/latest/developerguide/key-policies.md#key-policy-editing "../../../kms/latest/developerguide/key-policies.md#key-policy-editing") in the _AWS Key Management Service Developer Guide_.
- For technical details on how CloudTrail uses AWS KMS, see [How AWS CloudTrail uses AWS KMS](how-kms-works-with-cloudtrail.md "how-kms-works-with-cloudtrail.md").

###### Topics

- [Required KMS key policy sections for use with CloudTrail](#create-kms-key-policy-for-cloudtrail-policy-sections "#create-kms-key-policy-for-cloudtrail-policy-sections")
- [Granting encrypt permissions for trails](#create-kms-key-policy-for-cloudtrail-encrypt "#create-kms-key-policy-for-cloudtrail-encrypt")
- [Granting encrypt permissions for event data stores](#create-kms-key-policy-for-cloudtrail-encrypt-eds "#create-kms-key-policy-for-cloudtrail-encrypt-eds")
- [Granting decrypt permissions for trails](#create-kms-key-policy-for-cloudtrail-decrypt "#create-kms-key-policy-for-cloudtrail-decrypt")
- [Granting decrypt permissions for event data stores](#create-kms-key-policy-for-cloudtrail-decrypt-eds "#create-kms-key-policy-for-cloudtrail-decrypt-eds")
- [Enable CloudTrail to describe KMS key properties](#create-kms-key-policy-for-cloudtrail-describe "#create-kms-key-policy-for-cloudtrail-describe")
- [Default KMS key policy created in CloudTrail console](default-kms-key-policy.md "default-kms-key-policy.md")

## Required KMS key policy sections for use with CloudTrail

If you created a KMS key with the AWS Management console or the AWS CLI, then you must, at minimum,
add the following statements to your KMS key policy for it to work with CloudTrail.

###### Topics

- [Required KMS key policy elements for trails](#required-kms-key-policy-trails "#required-kms-key-policy-trails")
- [Required KMS key policy elements for event data stores](#required-kms-key-policy-eventdatastores "#required-kms-key-policy-eventdatastores")

### Required KMS key policy elements for trails

1. Grant permissions to encrypt CloudTrail log and digest files. For more information, see [Granting encrypt permissions for trails](#create-kms-key-policy-for-cloudtrail-encrypt "#create-kms-key-policy-for-cloudtrail-encrypt").
2. Grant permissions to decrypt CloudTrail log and digest files. For more information, see [Granting decrypt permissions for trails](#create-kms-key-policy-for-cloudtrail-decrypt "#create-kms-key-policy-for-cloudtrail-decrypt"). If you
   are using an existing S3 bucket with an [S3
   Bucket Key](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md"), `kms:Decrypt` permissions are required to
   create or update a trail with SSE-KMS encryption enabled.
3. Enable CloudTrail to describe KMS key properties. For more information, see [Enable CloudTrail to describe KMS key properties](#create-kms-key-policy-for-cloudtrail-describe "#create-kms-key-policy-for-cloudtrail-describe").

As a security best practice, add an `aws:SourceArn` condition key to
the KMS key policy. The IAM global condition key `aws:SourceArn`
helps ensure that CloudTrail uses the KMS key only for a specific trail or trails. The
value of `aws:SourceArn` is always the trail ARN (or array of trail ARNs)
that is using the KMS key. Be sure to add the `aws:SourceArn` condition
key to KMS key policies for existing trails.

The `aws:SourceAccount` condition key is also supported, but not
recommended. The value of `aws:SourceAccount` is the account ID of the
trail owner, or for organization trails, the management account ID.

###### Important

When you add the new sections to your KMS key policy, do not change any
existing sections in the policy.

If encryption is enabled on a trail, and the KMS key is disabled, or the
KMS key policy is not correctly configured for CloudTrail, CloudTrail cannot deliver
logs.

### Required KMS key policy elements for event data stores

1. Grant permissions to encrypt a CloudTrail Lake event data store. For more information, see [Granting encrypt permissions for event data stores](#create-kms-key-policy-for-cloudtrail-encrypt-eds "#create-kms-key-policy-for-cloudtrail-encrypt-eds").
2. Grant permissions to decrypt a CloudTrail Lake event data store. For more information, see [Granting decrypt permissions for event data stores](#create-kms-key-policy-for-cloudtrail-decrypt-eds "#create-kms-key-policy-for-cloudtrail-decrypt-eds").

When you create an event data store and encrypt it with a KMS key, or
run queries on an event data store that you're encrypting with a KMS key,
you should have write access to the KMS key. The KMS key policy must
have access to CloudTrail, and the KMS key should be manageable by users who run
operations (such as queries) on the event data store. 3. Enable CloudTrail to describe KMS key properties. For more information, see [Enable CloudTrail to describe KMS key properties](#create-kms-key-policy-for-cloudtrail-describe "#create-kms-key-policy-for-cloudtrail-describe").

The `aws:SourceArn` and `aws:SourceAccount` condition keys
are not supported in KMS key policies for event data stores.

###### Important

When you add the new sections to your KMS key policy, do not change any
existing sections in the policy.

If encryption is enabled on an event data store, and the KMS key is disabled
or deleted, or the KMS key policy is not correctly configured for CloudTrail, CloudTrail
cannot deliver events to your event data store.

## Granting encrypt permissions for trails

###### Example Allow CloudTrail to encrypt log files and digest files on behalf of specific accounts

CloudTrail needs explicit permission to use the KMS key to encrypt log files and digest files on behalf of specific
accounts. To specify an account, add the following required statement to your KMS key policy
and replace `account-id`,
`region`, and `trailName` with the
appropriate values for your configuration. You can add additional account IDs to the
`EncryptionContext` section to enable those accounts to use CloudTrail to use your
KMS key to encrypt log files and digest files.

As a security best practice, add an `aws:SourceArn` condition key to
the KMS key policy for a trail. The IAM global condition key
`aws:SourceArn` helps ensure that CloudTrail uses the KMS key only
for a specific trail or trails.

```
{
   "Sid": "AllowCloudTrailEncryptLogs",
   "Effect": "Allow",
   "Principal": {
       "Service": "cloudtrail.amazonaws.com"
    },
    "Action": "kms:GenerateDataKey*",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:SourceArn": "arn:aws:cloudtrail:`region`:`account-id`:trail/`trail-name`"
         },
         "StringLike": {
             "kms:EncryptionContext:aws:cloudtrail:arn": "arn:aws:cloudtrail:*:`account-id`:trail/*"
         }
    }
}
```

The following example policy statement illustrates how another account can use
your KMS key to encrypt CloudTrail log files and digest files.

###### Scenario

- Your KMS key is in account `111111111111`.
- Both you and account `222222222222` will encrypt logs.

In the policy, you add one or more accounts that encrypt with your key to the CloudTrail
**EncryptionContext**. This restricts CloudTrail to using
your key to encrypt log files and digest files only for the accounts that you specify. When you give the root
of account `222222222222` permission to encrypt log files and digest files,
it delegates permission to the account administrator to encrypt the necessary permissions
to other users in that account. The account administrator does this by changing the
policies associated with those IAM users.

As a security best practice, add an `aws:SourceArn` condition key to the
KMS key policy. The IAM global condition key `aws:SourceArn` helps ensure
that CloudTrail uses the KMS key only for the specified trails. This condition isn't
supported in KMS key policies for event data stores.

KMS key policy statement:

```
{
  "Sid": "EnableCloudTrailEncryptPermissions",
  "Effect": "Allow",
  "Principal": {
    "Service": "cloudtrail.amazonaws.com"
  },
  "Action": "kms:GenerateDataKey*",
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:EncryptionContext:aws:cloudtrail:arn": [
        "arn:aws:cloudtrail:*:`111111111111`:trail/*",
        "arn:aws:cloudtrail:*:`222222222222`:trail/*"
      ]
    },
    "StringEquals": {
        "aws:SourceArn": "arn:aws:cloudtrail:`region`:`account-id`:trail/`trail-name`"
    }
  }
}
```

For more information about editing a KMS key policy for use with CloudTrail, see [Editing a key policy](../../../kms/latest/developerguide/key-policies.md#key-policy-editing "../../../kms/latest/developerguide/key-policies.md#key-policy-editing")
in the AWS Key Management Service Developer Guide.

## Granting encrypt permissions for event data stores

A policy for a KMS key used to encrypt a CloudTrail Lake event data store
cannot use the condition keys `aws:SourceArn` or
`aws:SourceAccount`. The following is an example of a KMS key policy
for an event data store.

```
{
    "Sid": "AllowCloudTrailEncryptEds",
    "Effect": "Allow",
    "Principal": {
        "Service": "cloudtrail.amazonaws.com"
     },
     "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "*"
}
```

## Granting decrypt permissions for trails

Before you add your KMS key to your CloudTrail configuration, it is important to give
decrypt permissions to all users who require them. Users who have encrypt permissions
but no decrypt permissions cannot read encrypted logs. If you are using an existing S3
bucket with an [S3 Bucket Key](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md"), `kms:Decrypt` permissions are
required to create or update a trail with SSE-KMS encryption enabled.

###### Enable CloudTrail log decrypt permissions

Users of your key must be given explicit permissions to read the log files that
CloudTrail has encrypted. To enable users to read encrypted logs, add the following
required statement to your KMS key policy, modifying the `Principal` section
to add a line for every principal that you want to be able decrypt by
using your KMS key.

```
{
  "Sid": "EnableCloudTrailLogDecryptPermissions",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::`account-id`:user/`username`"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "Null": {
      "kms:EncryptionContext:aws:cloudtrail:arn": "false"
    }
  }
}
```

The following is an example policy that is required to allow the CloudTrail service principal to decrypt trail logs.

```
{
      "Sid": "AllowCloudTrailDecryptTrail",
      "Effect": "Allow",
      "Principal": {
          "Service": "cloudtrail.amazonaws.com"
        },
      "Action": "kms:Decrypt",
      "Resource": "*"
}
```

### Allow

users in your account to decrypt trail logs with your KMS key

###### Example

This policy statement illustrates how to allow a user or role in your
account to use your key to read the encrypted logs in your account's S3
bucket.

###### Example Scenario

- Your KMS key, S3 bucket, and IAM user Bob are in account
  `111111111111`.
- You give IAM user Bob permission to decrypt CloudTrail logs in the S3
  bucket.

In the key policy, you enable CloudTrail log decrypt permissions for IAM user
Bob.

KMS key policy statement:

```
{
  "Sid": "EnableCloudTrailLogDecryptPermissions",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::`111111111111`:user/Bob"
  },
  "Action": "kms:Decrypt",
  "Resource": "arn:aws:kms:`region`:`account-id`:key/`key-id`",
  "Condition": {
    "Null": {
      "kms:EncryptionContext:aws:cloudtrail:arn": "false"
    }
  }
}
```

###### Topics

### Allow

users in other accounts to decrypt trail logs with your KMS key

You can allow users in other accounts to use your KMS key to decrypt trail logs.
The changes required to your key policy depend on whether the S3 bucket is in your
account or in another account.

#### Allow users of a bucket in a different account to decrypt logs

###### Example

This policy statement illustrates how to allow an IAM user or role in
another account to use your key to read encrypted logs from an S3 bucket in
the other account.

###### Scenario

- Your KMS key is in account
  `111111111111`.
- The IAM user Alice and S3 bucket are in account
  `222222222222`.

In this case, you give CloudTrail permission to decrypt logs under account
`222222222222`, and you
give Alice's IAM user policy permission to use your key
`KeyA`, which is in account
`111111111111`.

KMS key policy statement:

```
{
  "Sid": "EnableEncryptedCloudTrailLogReadAccess",
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "arn:aws:iam::`222222222222`:root"
    ]
  },
  "Action": "kms:Decrypt",
  "Resource": "arn:aws:kms:`region`:`111111111111`:key/`key-id`",
  "Condition": {
    "Null": {
      "kms:EncryptionContext:aws:cloudtrail:arn": "false"
    }
  }
}
```

Alice's IAM user policy statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:us-west-2:`111111111111`:key/`KeyA`"
 }
 ]
}`

```

#### Allow

users in a different account to decrypt trail logs from your bucket

###### Example

This policy illustrates how another account can use your key to read
encrypted logs from your S3 bucket.

###### Example Scenario

- Your KMS key and S3 bucket are in account
  `111111111111`.
- The user who reads logs from your bucket is in account
  `222222222222`.

To enable this scenario, you enable decrypt permissions for the IAM role
**CloudTrailReadRole** in your account, and
then give the other account permission to assume that role.

KMS key policy statement:

```
{
  "Sid": "EnableEncryptedCloudTrailLogReadAccess",
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "arn:aws:iam::111111111111:role/CloudTrailReadRole"
    ]
  },
  "Action": "kms:Decrypt",
  "Resource": "arn:aws:kms:`region`:`account-id`:key/`key-id`",
  "Condition": {
    "Null": {
      "kms:EncryptionContext:aws:cloudtrail:arn": "false"
    }
  }
}
```

**CloudTrailReadRole** trust entity policy
statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow CloudTrail access",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`222222222222`:root"
 },
 "Action": "sts:AssumeRole"
 }
 ]
 }`

```

For information about editing a KMS key policy for use with CloudTrail, see [Editing a Key
Policy](../../../kms/latest/developerguide/key-policies.md#key-policy-editing "../../../kms/latest/developerguide/key-policies.md#key-policy-editing") in the _AWS Key Management Service Developer Guide_.

## Granting decrypt permissions for event data stores

A decrypt policy for a KMS key that is used with a CloudTrail Lake event
data store is similar to the following. The user or role ARNs specified as values for
`Principal` need decrypt permissions to create or update event data
stores, run queries, or get query results.

```
{
      "Sid": "EnableUserKeyPermissionsEds"
      "Effect": "Allow",
      "Principal": {
          "AWS": "arn:aws:iam::`account-id`:user/`username`"
      },
      "Action": [
          "kms:Decrypt",
          "kms:GenerateDataKey"
      ],
      "Resource": "*"
  }
```

The following is an example policy that is required to allow the CloudTrail
service principal to decrypt an event data store.

```
{
      "Sid": "AllowCloudTrailDecryptEds",
      "Effect": "Allow",
      "Principal": {
          "Service": "cloudtrail.amazonaws.com"
        },
      "Action": "kms:Decrypt",
      "Resource": "*"
}
```

## Enable CloudTrail to describe KMS key properties

CloudTrail requires the ability to describe the properties of the KMS key. To enable this
functionality, add the following required statement as is to your KMS key policy. This statement
does not grant CloudTrail any permissions beyond the other permissions that you specify.

As a security best practice, add an `aws:SourceArn` condition key to the
KMS key policy. The IAM global condition key `aws:SourceArn` helps ensure
that CloudTrail uses the KMS key only for a specific trail or trails.

```
{
  "Sid": "AllowCloudTrailAccess",
  "Effect": "Allow",
  "Principal": {
    "Service": "cloudtrail.amazonaws.com"
  },
  "Action": "kms:DescribeKey",
  "Resource": "arn:aws:kms:`region`:`account-id`:key/`key-id`",
  "Condition": {
    "StringEquals": {
        "aws:SourceArn": "arn:aws:cloudtrail:`region`:`account-id`:trail/`trail-name`"
    }
  }
}
```

For more information about editing KMS key policies, see [Editing a Key Policy](../../../kms/latest/developerguide/key-policies.md#key-policy-editing "../../../kms/latest/developerguide/key-policies.md#key-policy-editing")
in the _AWS Key Management Service Developer Guide_.
