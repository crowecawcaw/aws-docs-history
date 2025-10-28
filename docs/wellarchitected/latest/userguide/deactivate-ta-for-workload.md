# Deactivating Trusted Advisor for a

workload

**To deactivate Trusted Advisor for a workload**

You can deactivate Trusted Advisor for any workload from the AWS Well-Architected Tool by editing your workload
and deselecting **Activate Trusted Advisor**. For more information on
editing workloads, see [Edit a workload in AWS Well-Architected Tool](workloads-edit.md "workloads-edit.md").

Deactivating Trusted Advisor from the AWS WA Tool does not delete the roles created in IAM.
Deleting roles from IAM requires a separate cleanup measure. Workload owners or
owners of associated accounts should delete the IAM roles created when Trusted Advisor is
deactivated in AWS WA Tool, or to stop AWS WA Tool from collecting Trusted Advisor data for the
workload.

**To delete the `WellArchitectedRoleForTrustedAdvisor`
in IAM**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the **IAM** console, choose
   **Roles**.
3. Search for
   `WellArchitectedRoleForTrustedAdvisor-`WORKLOAD_OWNER_ACCOUNT_ID``
   and select the role name.
4. Choose **Delete**. In the pop-up window, type the
   name of the role to confirm deletion, and select **Delete** again.
   For more information about deleting a role from IAM, see [Deleting an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#roles-managingrole-deleting-console "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#roles-managingrole-deleting-console") in the _IAM User
   Guide_.
