

# Edit a workload in AWS Well-Architected Tool
<a name="workloads-edit"></a>

You can edit the details of a workload that you own.

**To edit a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the workload that you want to edit and choose **Edit**.

1. Make your changes to the workload.

   For a description of each of the fields, see [Defining a workload in AWS WA Tool](define-workload.md).
**Note**  
When updating an existing workload, you can **Activate Trusted Advisor**, which automatically creates the IAM role for the workload owner. The owners of associated accounts for workloads with Trusted Advisor activated need to create a role in IAM. For details, see [Activating Trusted Advisor for a workload in IAM](activate-ta-in-iam.md).

1. Choose **Save** to save your changes to the workload.

   If a required field is blank or if a specified value is not valid, you must correct the issue before your updates to the workload are saved.