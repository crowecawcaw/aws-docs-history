# Restore an AWS Secrets Manager secret

Secrets Manager considers a secret scheduled for deletion _deprecated_ and you
can no longer directly access it. After the recovery window has passed, Secrets Manager deletes the secret
permanently. Once Secrets Manager deletes the secret, you can't recover it. Before the end of the
recovery window, you can recover the secret and make it accessible again. This removes the
`DeletionDate` field, which cancels the scheduled permanent deletion.

To restore a secret and the metadata in the console, you must have `secretsmanager:ListSecrets` and `secretsmanager:RestoreSecret`
permissions.

Secrets Manager generates a CloudTrail log entry when you restore a secret. For more information, see [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").

###### To restore a secret (console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. In the list of secrets, choose the secret you want to restore.

If deleted secrets don't appear in your list of secrets, choose
**Preferences** (
![Gear icon representing settings or configuration options.](images/preferences-gear.png)
). In the Preferences dialog box, select **Show secrets scheduled for deletion**, and then choose **Save**. 3. On the **Secret details** page, choose **Cancel
deletion**. 4. In the **Cancel secret deletion** dialog box, choose **Cancel
deletion**.

## AWS CLI

###### Example Restore a previously deleted secret

The following [`restore-secret`](../../../cli/latest/reference/secretsmanager/restore-secret.md "../../../cli/latest/reference/secretsmanager/restore-secret.md") example restores a secret that was previously scheduled for deletion.

```
aws secretsmanager restore-secret \
    --secret-id MyTestSecret
```

## AWS SDK

To restore a secret marked for deletion, use the [`RestoreSecret`](../apireference/API_RestoreSecret.md "../apireference/API_RestoreSecret.md") command. For
more information, see [AWS SDKs](asm_access.md#asm-sdks "asm_access.md#asm-sdks").
