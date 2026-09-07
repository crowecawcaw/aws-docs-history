

# Deactivating Trusted Advisor for a workload
<a name="deactivate-ta-for-workload"></a>

**To deactivate Trusted Advisor for a workload**

You can deactivate Trusted Advisor for any workload from the AWS Well-Architected Tool by editing your workload and deselecting **Activate Trusted Advisor**. For more information on editing workloads, see [Edit a workload in AWS Well-Architected Tool](workloads-edit.md). 

Deactivating Trusted Advisor from the AWS WA Tool does not delete the roles created in IAM. Deleting roles from IAM requires a separate cleanup measure. Workload owners or owners of associated accounts should delete the IAM roles created when Trusted Advisor is deactivated in AWS WA Tool, or to stop AWS WA Tool from collecting Trusted Advisor data for the workload. 

**To delete the `WellArchitectedRoleForTrustedAdvisor` in IAM**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the **IAM** console, choose **Roles**.

1. Search for `WellArchitectedRoleForTrustedAdvisor-{{WORKLOAD_OWNER_ACCOUNT_ID}}` and select the role name.

1. Choose **Delete**. In the pop-up window, type the name of the role to confirm deletion, and select **Delete** again.

For more information about deleting a role from IAM, see [Deleting an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#roles-managingrole-deleting-console) in the *IAM User Guide*.