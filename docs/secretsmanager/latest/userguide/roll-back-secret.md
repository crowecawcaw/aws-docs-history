# Roll back a secret to a previous version

You can revert a secret to a previous version by moving the labels attached to secret versions using the AWS CLI. For information about how Secrets Manager stores versions of secrets, see [Secret versions](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version").

The following [`update-secret-version-stage`](../../../cli/latest/reference/secretsmanager/update-secret-version-stage.md "../../../cli/latest/reference/secretsmanager/update-secret-version-stage.md") example moves the AWSCURRENT staging label to the previous version of a secret, which reverts the secret to the previous version. To find the ID for the previous version, use [`list-secret-version-ids`](../../../cli/latest/reference/secretsmanager/list-secret-version-ids.md "../../../cli/latest/reference/secretsmanager/list-secret-version-ids.md") or view the versions in the Secrets Manager console.

For this example, the version with the AWSCURRENT label is a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 and the version with the AWSPREVIOUS label is a1b2c3d4-5678-90ab-cdef-EXAMPLE22222. In this example, you move the AWSCURRENT label from version 11111 to 22222. Because the AWSCURRENT label is removed from a version, `update-secret-version-stage` automatically moves the AWSPREVIOUS label to that version (11111). The effect is that the AWSCURRENT and AWSPREVIOUS versions are swapped.

```
aws secretsmanager update-secret-version-stage \
  --secret-id `MyTestSecret` \
  --version-stage AWSCURRENT \
  --move-to-version-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE22222` \
  --remove-from-version-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```
