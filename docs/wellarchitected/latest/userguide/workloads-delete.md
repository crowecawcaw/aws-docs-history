

# Delete a workload in AWS Well-Architected Tool
<a name="workloads-delete"></a>

You can delete a workload when it's no longer needed. Deleting a workload removes all data associated with the workload including any milestones and workload share invitations. Only the owner of a workload can delete it.

**Warning**  
Deleting a workload cannot be undone. All data associated with the workload is permanently removed.

**To delete a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the workload you want to delete and choose **Delete**.

1. In the **Delete** window, choose **Delete** to confirm the deletion of the workload and its milestones.

To prevent an entity from deleting workloads, attach a policy that denies `wellarchitected:DeleteWorkload` actions.