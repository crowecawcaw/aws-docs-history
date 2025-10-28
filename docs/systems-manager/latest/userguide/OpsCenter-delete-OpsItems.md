# Delete OpsItems

You can delete an individual OpsItem by calling the [DeleteOpsItem](../APIReference/API_DeleteOpsItem.md "../APIReference/API_DeleteOpsItem.md")
API operation using the AWS Command Line Interface or the AWS SDK. You can't delete an OpsItem in the
AWS Management Console. To delete an OpsItem, your AWS Identity and Access Management (IAM) user, group, or role must have
either administrator permission or you must have been granted permission to call the
`DeleteOpsItem` API operation.

###### Important

Note the following important information about this operation.

- Deleting an OpsItem is irreversible. You can't restore a deleted OpsItem.
- This operation uses an _eventual consistency model_,
  which means the system can take a few minutes to complete this operation. If
  you delete an OpsItem and immediately call, for example, [GetOpsItem](../APIReference/API_GetOpsItem.md "../APIReference/API_GetOpsItem.md"), the deleted OpsItem might still appear in the response.
- This operation is idempotent. The system doesn't throw an exception if you
  repeatedly call this operation for the same OpsItem. If the first call is
  successful, all additional calls return the same successful response as the
  first call.
- This operation doesn't support cross-account calls. A delegated
  administrator or management account can't delete OpsItems in other accounts,
  even if OpsCenter has been set up for cross-account administration. For more
  information about cross-account administration, see [(Optional) Setting up OpsCenter
  to centrally manage OpsItems across accounts](OpsCenter-setting-up-cross-account.md "OpsCenter-setting-up-cross-account.md").
- If you receive the `OpsItemLimitExceededException`, you can
  delete one or more OpsItems to reduce your total number of OpsItems below the
  quota limits. For more information about this exception, see [Troubleshooting issues with
  OpsCenter](OpsCenter-troubleshooting.md "OpsCenter-troubleshooting.md").

## Deleting an OpsItem

Use the following procedure to delete an OpsItem.

###### To delete an OpsItem

1. Install and configure the AWS CLI, if you haven't already. For more
   information, see [Installing or
   updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. Run the following command. Replace `ID` with the
   ID of the OpsItem you want to delete.

```
aws ssm delete-ops-item --ops-item-id `ID`
```

If successful, the command returns no data.
