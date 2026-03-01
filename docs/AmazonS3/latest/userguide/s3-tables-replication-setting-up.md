# Setting up S3 Tables replication

You can set up replication to automatically create table replicas from a source table to up
to five destination table buckets. Replication can be configured at the bucket level (applying
to all tables in the bucket) or at the table level (for specific tables). This topic explains
how to configure replication using the Amazon S3 console or the AWS Command Line Interface
(AWS CLI).

For more information about setting up replication, see the following topics.

###### Topics

- [Prerequisites for setting up replication](#s3-tables-replication-prerequisites "#s3-tables-replication-prerequisites")
- [Understanding replication configurations](#s3-tables-replication-understanding-configurations "#s3-tables-replication-understanding-configurations")
- [Choosing between bucket-level and table-level replication](#s3-tables-replication-choosing-configuration "#s3-tables-replication-choosing-configuration")
- [Setting up replication by using the Amazon S3 console](#s3-tables-replication-console "#s3-tables-replication-console")
- [Setting up replication by using the AWS CLI](#s3-tables-replication-cli "#s3-tables-replication-cli")

## Prerequisites for setting up replication

Before you configure replication, ensure you have the following:

### Required resources

- Source table bucket – The table bucket
  containing the table(s) you want to replicate
- Destination table bucket(s) – One or more
  table buckets where you want to replicate your tables (up to 5 destination table
  buckets)
- Source table(s) – Existing tables in your
  source table bucket to replicate
- IAM role(s) – An IAM role that grants Amazon S3
  permissions to replicate tables on your behalf

### Required permissions

The IAM identity that you use to set up replication must have the following
permissions:

###### For bucket-level replication:

- `s3tables:PutTableBucketReplication` on the source table bucket
- `s3tables:GetTableBucketReplication` on the source table bucket
- `iam:PassRole` for the replication IAM role

###### For table-level replication:

- `s3tables:PutTableReplication` on the source table
- `s3tables:GetTableReplication` on the source table
- `iam:PassRole` for the replication IAM role

###### For cross-account replication:

- Permissions from the destination account's bucket policy

### Additional requirements for cross-account replication

If your source and destination table buckets are in different AWS accounts, you also
need:

- A bucket policy on the destination table bucket that grants the source account
  permissions to replicate tables
- The destination account ID and table bucket Amazon Resource Name (ARN)

### Additional requirements for encrypted tables

If you want to encrypt replica tables with AWS KMS:

- A KMS key in the destination Region
- Permissions to use the KMS key in your IAM replication role
- A KMS key policy that allows the replication role to encrypt data

## Understanding replication configurations

A replication configuration defines how Amazon S3 replicates tables from your source table
bucket. Replication can be configured at two levels:

### Bucket-level replication

A bucket-level replication configuration applies to all tables in the source table
bucket. When you configure bucket-level replication, Amazon S3 automatically replicates any
existing tables and any new tables created in the bucket.

Use bucket-level replication when:

- You want to replicate all tables in a bucket
- You want consistent replication behavior across all tables
- You want to simplify management by having a single configuration

### Table-level replication

A table-level replication configuration applies to a specific table. Table-level
configurations override bucket-level configurations for that specific table.

Use table-level replication when:

- You want to replicate only specific tables
- You need different replication destinations for different tables
- You want to override a bucket-level configuration for certain tables

### Replication configuration elements

Each replication configuration contains:

- IAM role – The role that Amazon S3 assumes to
  perform replication operations
- Rules – One or more replication rules (limited
  to 1 rule at launch). Each rule contains:
  - Destinations – List of destination table
    bucket ARNs (up to 5 destinations)
  - Status – Whether the rule is enabled or
    disabled

- Version token – A token used to prevent write
  conflicts when updating configurations

## Choosing between bucket-level and table-level replication

### Configuration precedence

When both bucket-level and table-level configurations exist:

- Table-level configuration takes precedence for that specific table.
- Other tables follow the bucket-level configuration.

## Setting up replication by using the Amazon S3 console

This procedure shows you how to configure replication using the Amazon S3 console.

This procedure shows you how to create a table bucket replication configuration using
the Amazon S3 console. A table bucket replication configuration applies to all tables in the
source table bucket.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Table buckets**.
3. In the **Table buckets** list, choose the name of the table
   bucket for which you want to configure replication.
4. Choose the **Management** tab.
5. In the **Table bucket replication configuration** section, choose
   **Create table bucket replication configuration**.
6. In the **Destination** section, configure your replication
   destinations:
   1. In the **Table bucket ARN** field, enter the ARN of the
      destination table bucket. The format is:
      `arn:aws:s3tables:`region`:`account-id`:bucket/`table-bucket-name``

   Alternatively, choose **Browse S3** to select a table bucket
   from your account. 2. (Optional) To add additional destinations, choose **Add
   destination**. You can add up to 4 more table buckets for a total of 5
   destinations.

7. In the **IAM role** section, configure the replication
   role:
   1. For **IAM role selection method**, choose one of the
      following options:
      - **Create new IAM role** – Amazon S3 creates a new
        role with the necessary permissions for replication.
      - **Choose from existing IAM roles** – Select an
        existing role that has the required replication permissions.
      - **Enter IAM role ARN** – Manually enter the ARN
        of an existing IAM role.

   2. If you chose **Choose from existing IAM roles**, select a
      role from the **IAM role** dropdown list.
   3. (Optional) Choose **View** to review the selected role's
      permissions in the IAM console.

8. Choose **Create replication configuration**.

After you create the replication configuration, Amazon S3 begins the initial backfill
process. You can monitor the replication status in the **Table replication
status** section, which displays information about each destination
including replication status, destination table ARN, and last replicated
metadata.

This procedure shows you how to create a table-level replication configuration using
the Amazon S3 console. A table replication configuration applies to a specific table and
overrides any bucket-level replication configuration for that table.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Table buckets**.
3. In the **Table buckets** list, choose the name of the table
   bucket that contains the table you want to replicate.
4. Choose the **Tables** tab.
5. In the **Tables** list, choose the name of the table that you
   want to replicate.
6. Choose the **Management** tab.
7. In the **Table replication configuration** section, choose
   **Create table replication configuration**.
8. In the **Destination** section, configure your replication
   destinations:
   1. In the **Table bucket ARN** field, enter the ARN of the
      destination table bucket. The format is:
      `arn:aws:s3tables:`region`:`account-id`:bucket/`table-bucket-name``

   Alternatively, choose **Browse S3** to select a table bucket
   from your account. 2. (Optional) To add additional destinations, choose **Add
   destination**. You can add up to 4 more table buckets for a total of 5
   destinations.

9. In the **IAM role** section, configure the replication
   role:
   1. For **IAM role selection method**, choose one of the
      following options:
      - **Create new IAM role** – Amazon S3 creates a new
        role with the necessary permissions for replication.
      - **Choose from existing IAM roles** – Select an
        existing role that has the required replication permissions.
      - **Enter IAM role ARN** – Manually enter the ARN
        of an existing IAM role.

   2. If you chose **Choose from existing IAM roles**, select a
      role from the **IAM role** list.
   3. (Optional) Choose **View** to review the selected role's
      permissions in the IAM console.

10. Choose **Create replication configuration**.

### What happens next?

After you create the replication configuration:

- Amazon S3 begins the initial backfill process, creating replica tables in each
  destination bucket
- The replication status changes to **Replicating** once backfill
  begins
- You can monitor replication progress on the **Management**
  tab
- Initial replication time depends on the size of your source table

## Setting up replication by using the AWS CLI

This procedure shows you how to configure replication using the AWS CLI. Replace the account
IDs, regions, and bucket names with your actual values. Add all destination buckets to the
permissions.

### Step 1: Create an IAM role for replication

First, create an IAM role that Amazon S3 can assume to replicate your tables.

1. Create a trust policy document that allows S3 Tables to assume the role. Save this
   as `trust-policy.json`:

```

{
  "Version": "2012-10-17"
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "replication.s3tables.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

```

2. Create the IAM role:

```

aws iam create-role \
    --role-name `S3TablesReplicationRole` \
    --assume-role-policy-document file://trust-policy.json \
    --description "Role for S3 Tables replication"

```

3. Create a permissions policy that grants replication permissions. Save this as
   `replication-permissions.json`:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3tables:GetTable",
                "s3tables:GetTableMetadataLocation",
                "s3tables:GetTableMaintenanceConfiguration",
                "s3tables:GetTableData"
            ],
            "Resource": "arn:aws:s3tables:`us-east-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket-source`/table/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3tables:ListTables"
            ],
            "Resource": "arn:aws:s3tables:`us-east-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket-source`"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3tables:CreateTable",
                "s3tables:CreateNamespace"
            ],
            "Resource": "arn:aws:s3tables:`us-east-2`:`444455556666`:bucket/`amzn-s3-demo-table-bucket-destination`"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3tables:PutTableData",
                "s3tables:GetTableData",
                "s3tables:UpdateTableMetadataLocation",
                "s3tables:PutTableMaintenanceConfiguration"
            ],
            "Resource": "arn:aws:s3tables:`us-east-2`:`444455556666`:bucket/`amzn-s3-demo-table-bucket-destination`/table/*"
        }
    ]
}

```

4. Attach the permissions policy to the role:

```

aws iam put-role-policy \
    --role-name `S3TablesReplicationRole` \
    --policy-name `S3TablesReplicationPermissions` \
    --policy-document file://replication-permissions.json

```

5. (Optional) If using KMS encryption, add KMS permissions to your policy:

```

{
  "Effect": "Allow",
  "Action": [
     "kms:Decrypt",
     "kms:GenerateDataKey",
     "kms:Encrypt"

  ],
  "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`SOURCE-KEY-ID`"
},
{
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": [
    "arn:aws:kms:`us-west-2`:`444455556666`:key/`DESTINATION-KEY-ID-1`"
  ]
}

```

### (Cross-account only) Step 2: Configure destination bucket policy

If you are replicating to a different AWS account, the destination account must grant
permissions to the source account.

1. In the destination account, create a bucket policy for the destination table bucket.
   Save this as `destination-bucket-policy.json`:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`444455556666`:role/`cross-account-test`"
            },
            "Action": [
                "s3tables:PutTableData",
                "s3tables:GetTableData",
                "s3tables:UpdateTableMetadataLocation",
                "s3tables:PutTableMaintenanceConfiguration"
            ],
            "Resource": "arn:aws:s3tables:`us-east-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket-cross-account-destination`/table/*"
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`444455556666`:role/`cross-account-test`"
            },
            "Action": [
                "s3tables:CreateTable",
                "s3tables:CreateNamespace"
            ],
            "Resource": "arn:aws:s3tables:`us-east-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket-cross-account-destination`"
        }
    ]
}
```

2. Apply the policy using the S3 Tables API:

```

aws s3tables put-table-bucket-policy \
    --table-bucket-arn arn:aws:s3tables:`us-west-2`:`444455556666`:bucket/``amzn-s3-demo-table-bucket-cross-account-destination`` \
    --policy file://`destination-bucket-policy.json` \
    --profile `destination-account`

```

3. Modify your source KMS key to allow S3 Tables replication and maintenance:

```

{
  "Version": "2012-10-17",
  "Id": "key-consolepolicy-3",
  "Statement": [
        {
            "Sid": "allow replication to decrypt",
            "Effect": "Allow",
            "Principal": {
                "AWS": "`replication_role_arn`"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/SOURCE-KEY-ID"
        },
        {
            "Sid": "allow maintenance",
            "Effect": "Allow",
            "Principal": {
                "Service": "maintenance.s3tables.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/SOURCE-KEY-ID"
        }
  ]
}

```

4. Similarly, add permissions in your destination KMS key policy

```
{
    "Version": "2012-10-17",
    "Id": "key-policy-3",
    "Statement": [
        {
            "Sid": "allow maintenance",
            "Effect": "Allow",
            "Principal": {
                "Service": "maintenance.s3tables.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-west-2:`444455556666`:key/DESTINATION-KEY-ID-1"
        },
        {
            "Sid": "allow replication to encrypt/decrypt",
            "Effect": "Allow",
            "Principal": {
                "AWS": "`replication_role_arn`"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-west-2:`444455556666`:key/DESTINATION-KEY-ID-1"
        }
    ]

```

### Step 3: Create a replication configuration

You can use the AWS CLI to create a replication configuration at the table bucket-level or the table-level. For more information, see the following procedures.

Use this approach to replicate all tables in a bucket.

1. Create a replication configuration file. Save this as
   `bucket-replication-config.json`:

###### Example: Single destination in same account

```

{
  "role": "arn:aws:iam::`111122223333`:role/`S3TablesReplicationRole`",
  "rules": [
    {
      "destinations": [
        {
          "destinationTableBucketARN": "arn:aws:s3tables:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket-dr`"
        }
      ]
    }
  ]
}

```

###### Example: Multiple destinations across regions

```

{
  "role": "arn:aws:iam::`111122223333`:role/`S3TablesReplicationRole`",
  "rules": [
    {
      "destinations": [
        {
          "destinationTableBucketARN": "arn:aws:s3tables:`us-west-2`:`111122223333`:bucket/``amzn-s3-demo-table-bucket`-dr`"
        },
        {
          "destinationTableBucketARN": "arn:aws:s3tables:`eu-west-1`:`111122223333`:bucket/``amzn-s3-demo-table-bucket`-eu`"
        },
        {
          "destinationTableBucketARN": "arn:aws:s3tables:`ap-south-1`:`111122223333`:bucket/``amzn-s3-demo-table-bucket`-apac`"
        }
      ]
    }
  ]
}

```

###### Example: Cross-account replication

```

{
  "role": "arn:aws:iam::`111122223333`:role/`S3TablesReplicationRole`",
  "rules": [
    {
      "destinations": [
        {
          "destinationTableBucketARN": "arn:aws:s3tables:`us-east-1`:`444455556666`:bucket/``amzn-s3-demo-table-bucket`-partner`"
        }
      ]
    }
  ]
}

```

2. Apply the bucket-level replication configuration:

```

aws s3tables put-table-bucket-replication \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket` \
    --configuration file://bucket-replication-config.json

```

Expected output:

```

{
  "versionToken": "`3HL4kqtJl40Nr8X8gdRQBpUMLUo`",
  "status": "Success"
}

```

Use this approach to replicate specific tables or to override bucket-level
replication.

1. Create a replication configuration file. Save this as
   `table-replication-config.json`:

###### Example: Single table replication

```

{
  "role": "arn:aws:iam::`111122223333`:role/`S3TablesReplicationRole`",
  "rules": [
    {
      "destinations": [
        {
          "destinationTableBucketARN": "arn:aws:s3tables:`us-west-2`:`111122223333`:bucket/``amzn-s3-demo-table-bucket-`analytics-bucket`"
        }
      ]
    }
  ]
}

```

###### Example: Table with multiple destinations

```

{
  "role": "arn:aws:iam::`111122223333`:role/`S3TablesReplicationRole`",
  "rules": [
    {
      "destinations": [
        {
          "destinationTableBucketARN": "arn:aws:s3tables:`us-west-2`:`111122223333`:bucket/``amzn-s3-demo-table-bucket-`dr`"
        },
        {
          "destinationTableBucketARN": "arn:aws:s3tables:`eu-west-1`:`111122223333`:bucket/``amzn-s3-demo-table-bucket`-eu`"
        }
      ]
    }
  ]
}

```

2. Apply the table-level replication configuration:

```

aws s3tables put-table-replication \
    --table-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`/table/``amzn-s3-demo-table-bucket-`sales-data` \
    --configuration file://`table-replication-config.json`

```

Expected output:

```

{
  "versionToken": "`xT2LZkFZ0UuTC2h8XqtGLx2Ak6M`",
  "status": "Success"
}

```
