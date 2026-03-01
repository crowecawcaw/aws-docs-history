# Configure minimum encryption for a workgroup

As an administrator of an Athena SQL workgroup, you can enforce a minimal level of
encryption in Amazon S3 for all query results from the workgroup. You can use this feature to
ensure that query results are never stored in an Amazon S3 bucket in an unencrypted state.

When users in a workgroup with minimum encryption enabled submit a query, they can only
set the encryption to the minimum level that you configure, or to a higher level if one is
available. Athena encrypts query results at either the level specified when the user runs the
query or at the level set in the workgroup.

The following levels are available:

- Basic – Amazon S3 server side encryption with
  Amazon S3 managed keys (**SSE_S3**).
- Intermediate – Server Side encryption with
  KMS managed keys (**SSE_KMS**).
- Advanced – Client side encryption with KMS
  managed keys (**CSE_KMS**).

## Considerations and limitations

- The minimum encryption feature is not available for Apache Spark enabled
  workgroups.
- The minimum encryption feature is functional only when the workgroup does not
  enable the **[Override
  client-side settings](workgroups-settings-override.md "workgroups-settings-override.md")** option.
- If the workgroup has the **Override client-side settings**
  option enabled, the workgroup encryption setting prevails, and the minimum
  encryption setting has no effect.
- There is no cost to enable this feature.

## Enable minimum encryption for a workgroup

You can enable a minimum encryption level for the query results from your Athena SQL
workgroup when you create or update the workgroup. To do this, you can use the Athena
console, Athena API, or AWS CLI.

To get started creating or editing your workgroup using the Athena console, see
[Create a workgroup](workgroups-create-update-delete.md#creating-workgroups "workgroups-create-update-delete.md#creating-workgroups") or [Edit a workgroup](workgroups-create-update-delete.md#editing-workgroups "workgroups-create-update-delete.md#editing-workgroups"). When configuring your workgroup, use the following
steps to enable minimum encryption.

###### To configure the minimum encryption level for workgroup query results

1. Clear the **Override client-side settings** option, or
   verify that it is not selected.
2. Select the **Encrypt query results** option.
3. For **Encryption type**, select the encryption method
   that you want Athena to use for your workgroup's query results
   (**SSE_S3**, **SSE_KMS**, or
   **CSE_KMS**). These encryption types correspond to
   basic, intermediate, and advanced security levels.
4. To enforce the encryption method that you chose as the minimum level of
   encryption for all users, select **Set
   `encryption_method` as minimum
   encryption**.

When you select this option, a table shows the encryption hierarchy and
encryption levels that users will be allowed when the encryption type that
you choose becomes the minimum. 5. After you create your workgroup or update your workgroup configuration,
choose **Create workgroup** or **Save
changes**.
When you use the [CreateWorkGroup](../APIReference/API_CreateWorkGroup.md "../APIReference/API_CreateWorkGroup.md") or [UpdateWorkGroup](../APIReference/API_UpdateWorkGroup.md "../APIReference/API_UpdateWorkGroup.md") API to create or update an Athena SQL workgroup, set
[EnforceWorkGroupConfiguration](../APIReference/API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration "../APIReference/API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration") to `false`, [EnableMinimumEncryptionConfiguration](../APIReference/API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnableMinimumEncryptionConfiguration "../APIReference/API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnableMinimumEncryptionConfiguration") to `true`, and use the
[EncryptionOption](../APIReference/API_EncryptionConfiguration.md#athena-Type-EncryptionConfiguration-EncryptionOption "../APIReference/API_EncryptionConfiguration.md#athena-Type-EncryptionConfiguration-EncryptionOption") to specify the type of encryption.

In the AWS CLI, use the [`create-work-group`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-work-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-work-group.html") or [`update-work-group`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-work-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-work-group.html") command with the
`--configuration` or `--configuration-updates` parameters
and specify the options corresponding to those for the API.
