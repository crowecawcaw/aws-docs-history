# Restore a Amazon DynamoDB table

## Use the AWS Backup console to restore DynamoDB recovery

points

###### To restore a DynamoDB table

1.  Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2.  In the navigation pane, choose **Protected resources** and the
    DynamoDB resource ID you want to restore.
3.  On the **Resource details** page, a list of recovery points for
    the selected resource ID is shown. To restore a resource, in the
    **Backups** pane, choose the radio button next to the recovery
    point ID of the resource. In the upper-right corner of the pane, choose
    **Restore**.
4.  For **Settings**, **New table name** text field,
    enter a new table name.
5.  For **Restore role**, choose the IAM role that AWS Backup will
    assume for this restore.
6.  For **Encryption settings**:
    1. If your backup is managed by DynamoDB (its ARN begins with
       `arn:aws:dynamodb`), AWS Backup encrypts your restored table using an
       AWS-owned key.

    To choose a different key to encrypt your restored table, you can either use
    the AWS Backup [StartRestoreJob
    operation](API_StartRestoreJob.md "API_StartRestoreJob.md") or perform the restore from the [DynamoDB console](../../../amazondynamodb/latest/developerguide/Restore.md#restoretable_console "../../../amazondynamodb/latest/developerguide/Restore.md#restoretable_console"). 2. If your backup supports full AWS Backup management (its ARN begins with
    `arn:aws:backup`), you can choose any of the following encryption
    options to protect your restored table:

        * (Default) DynamoDB-owned KMS key (no additional charge for encryption)
        * DynamoDB-managed KMS key (KMS charges apply)
        * Customer-managed KMS key (KMS charges apply)

    "DynamoDB-owned" and "DynamoDB-managed" keys are the same as "AWS-owned" and
    "AWS-managed" keys, respectively. For clarification, see [Encryption at Rest: How It Works](../../../amazondynamodb/latest/developerguide/encryption.md "../../../amazondynamodb/latest/developerguide/encryption.md") in the _Amazon DynamoDB Developer Guide_.

    For more information about full AWS Backup management, see [Advanced DynamoDB backup](advanced-ddb-backup.md "advanced-ddb-backup.md").###### Note

The following guidance applies only if you restore a copied backup AND want to
encrypt the restored table with the same key you used to encrypt your original
table.

When restoring a cross-Region backup, to encrypt your restored table using the
same key you used to encrypt your original table, your key must be a multi-Region
key. AWS-owned and AWS-managed keys are not multi-Region keys. To learn more,
see [Multi-Region
keys](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") in the _AWS Key Management Service Developer Guide_.

When restoring a cross-account backup, to encrypt your restored table using the
same key you used to encrypt your original table, you must share the key in your
source account with your destination account. AWS-owned and AWS-managed keys
cannot be shared between accounts. To learn more, see [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the
_AWS Key Management Service Developer Guide_. 7. Choose **Restore backup**.

The **Restore jobs** pane appears. A message at the top of the
page provides information about the restore job.

## Use the AWS Backup API, CLI, or SDK to restore DynamoDB recovery

points

Use `StartRestoreJob`. You can specify the following metadata during any DynamoDB
restore. The metadata is not case-sensitive.

```
targetTableName
encryptionType
kmsMasterKeyArn
aws:backup:request-id

```

The following is an example of the `restoreMetadata` argument for a
`StartRestoreJob` operation in the CLI:

```
aws backup start-restore-job \
--recovery-point-arn "arn:aws:backup:us-east-1:123456789012:recovery-point:abcdef12-g3hi-4567-8cjk-012345678901" \
--iam-role-arn "arn:aws:iam::123456789012:role/YourIamRole" \
--metadata 'TargetTableName=TestRestoreTestTable,EncryptionType=KMS,kmsMasterKeyArn=arn:aws:kms:us-east-1:123456789012:key/abcdefg' \
--region us-east-1 \
--endpoint-url https://endpointurl.com
```

The preceding example encrypts the restored table using an AWS-owned key. The part
of the restore metadata that specifies encryption using the AWS-owned key is:
`\"encryptionType\":\"Default\","kmsMasterKeyArn\":\"Not
 Applicable\"`.

To encrypt your restored table using an AWS-managed key, specify the following
restore metadata: `"encryptionType\":\"KMS\",\"kmsMasterKeyArn\":\"Not
 Applicable\"`.

To encrypt your restored table using an customer-managed key, specify the following
restore metadata:
`"encryptionType\":\"KMS\",\"kmsMasterKeyArn\":\"`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`\"`.
