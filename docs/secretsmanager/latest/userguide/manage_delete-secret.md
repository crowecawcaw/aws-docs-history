# Delete an AWS Secrets Manager secret

Because of the critical nature of secrets, AWS Secrets Manager intentionally makes deleting a secret
difficult. Secrets Manager does not immediately delete secrets. Instead, Secrets Manager immediately makes
the secrets inaccessible and scheduled for deletion after a recovery window of a minimum of
seven days. Until the recovery window ends, you can recover a secret you previously deleted.
There is no charge for secrets that you have marked for deletion.

You can't delete a primary secret if it is replicated to other Regions. First delete the
replicas, then delete the primary secret. When you delete a replica, it is deleted
immediately.

You can't directly delete a version of a secret. Instead, you remove all staging labels
from the version using the AWS CLI or AWS SDK. This marks the version as deprecated, and then
Secrets Manager can automatically delete the version in the background.

If you don't know whether an application still uses a secret, you can create an Amazon CloudWatch
alarm to alert you to any attempts to access a secret during the recovery window. For more
information, see [Monitor when AWS Secrets Manager secrets scheduled for
deletion are accessed](monitoring_cloudwatch_deleted-secrets.md "monitoring_cloudwatch_deleted-secrets.md").

To delete a secret, you must have `secretsmanager:ListSecrets` and `secretsmanager:DeleteSecret` permissions.

Secrets Manager generates a CloudTrail log entry when you delete a secret. For more information, see [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").

###### To delete a secret (console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. In the list of secrets, choose the secret you want to delete.
3. In the **Secret details** section, choose **Actions**, and
   then choose **Delete secret**.
4. In the **Disable secret and schedule deletion** dialog box, in
   **Waiting period**, enter the number of days to wait before the deletion
   becomes permanent. Secrets Manager attaches a field called `DeletionDate` and sets the
   field to the current date and time, plus the number of days specified for the recovery
   window.
5. Choose **Schedule deletion**.

###### To view deleted secrets

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. On the **Secrets** page, choose **Preferences** (
   ![Gear icon representing settings or configuration options.](images/preferences-gear.png)
   ).
3. In the Preferences dialog box, select **Show secrets scheduled for deletion**, and
   then choose **Save**.

###### To delete a replica secret

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose the primary secret.
3. In the **Replicate Secret** section, choose the replica secret.
4. From the **Actions** menu, choose **Delete
   Replica**.

## AWS CLI

###### Example Delete a secret

The following [`delete-secret`](../../../cli/latest/reference/secretsmanager/delete-secret.md "../../../cli/latest/reference/secretsmanager/delete-secret.md") example deletes a secret. You can recover the secret with [`restore-secret`](../../../cli/latest/reference/secretsmanager/restore-secret.md "../../../cli/latest/reference/secretsmanager/restore-secret.md") until the date and time in the DeletionDate response field. To delete a secret that is replicated to other regions, first remove its replicas with [`remove-regions-from-replication`](../../../cli/latest/reference/secretsmanager/remove-regions-from-replication.md "../../../cli/latest/reference/secretsmanager/remove-regions-from-replication.md"), and then call [`delete-secret`](../../../cli/latest/reference/secretsmanager/delete-secret.md "../../../cli/latest/reference/secretsmanager/delete-secret.md").

```
aws secretsmanager delete-secret \
    --secret-id MyTestSecret \
    --recovery-window-in-days 7
```

###### Example Delete a secret immediately

The following [`delete-secret`](../../../cli/latest/reference/secretsmanager/delete-secret.md "../../../cli/latest/reference/secretsmanager/delete-secret.md") example deletes a secret immediately without a recovery window. You can't recover this secret.

```
aws secretsmanager delete-secret \
    --secret-id MyTestSecret \
    --force-delete-without-recovery
```

###### Example Delete a replica secret

The following [`remove-regions-from-replication`](../../../cli/latest/reference/secretsmanager/remove-regions-from-replication.md "../../../cli/latest/reference/secretsmanager/remove-regions-from-replication.md") example deletes a replica secret in eu-west-3. To delete a primary secret that is replicated to other regions, first delete the replicas and then call [`delete-secret`](../../../cli/latest/reference/secretsmanager/delete-secret.md "../../../cli/latest/reference/secretsmanager/delete-secret.md").

```
aws secretsmanager remove-regions-from-replication \
    --secret-id MyTestSecret \
    --remove-replica-regions eu-west-3
```

## AWS SDK

To delete a secret, use the [`DeleteSecret`](../apireference/API_DeleteSecret.md "../apireference/API_DeleteSecret.md") command. To delete a version of a secret, use the
[`UpdateSecretVersionStage`](../apireference/API_UpdateSecretVersionStage.md "../apireference/API_UpdateSecretVersionStage.md") command. To delete a replica, use the
[`StopReplicationToReplica`](../apireference/API_StopReplicationToReplica.md "../apireference/API_StopReplicationToReplica.md") command. For more information, see [AWS SDKs](asm_access.md#asm-sdks "asm_access.md#asm-sdks").
