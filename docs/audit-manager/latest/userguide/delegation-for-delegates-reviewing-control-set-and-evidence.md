

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Reviewing the delegated control set and its related evidence
<a name="delegation-for-delegates-reviewing-control-set-and-evidence"></a>



You can assist audit owners by reviewing the control sets that they have delegated to you. 

You can examine these controls and their related evidence to determine if any additional action is needed. Such additional action could include [manually uploading additional evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html) to demonstrate compliance, or [leaving a comment](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-delegates-add-comment.html) that details the remediation steps that you followed.

## Prerequisites
<a name="delegation-for-delegates-reviewing-control-set-and-evidence-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view a control set in AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="delegation-for-delegates-reviewing-control-set-and-evidence-procedure"></a>

**To review a control set**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Notifications**. 

1. On the **Notifications** page, you can see a list of control sets that were delegated to you. Identify which control set you want to review, and choose the name of the related assessment to open the assessment detail page.

1. Under the **Controls** tab of the assessment detail page, scroll down to the **Control sets** table. 

1. Under the **Controls grouped by control set** column, expand the name of a control set to show its controls.

1. Choose the name of a control to open the control detail page. 

1. (Optional) Choose **Update control status** to change the status of the control. While your review is in progress, you can mark the status as **Under Review**. 

1. Review information about the control in the **Evidence folders**, **Details**, **Data sources**, **Comments**, and **Changelog** tabs. 
   + To learn about each of these tabs and how to understand the data that they contain, see [Reviewing an assessment control in AWS Audit Manager](review-controls.md). 

**To review the evidence for a control**

1. From the control detail page, choose the **Evidence folders** tab. 

1. Navigate to the **Evidence folders** table to see a list of folders that contain evidence for that control. These folders are organized and named based on the date when the evidence was collected. 

1. Choose the name of an evidence folder to open it. Then, review a summary of all evidence gathered on that date. 
   + This summary includes the total number of compliance check issues that were reported directly from AWS Security Hub CSPM, AWS Config, or both. 
   + To learn more about this information, see [Reviewing an evidence folder in AWS Audit Manager](review-evidence-folders-detail.md). 

1. From the evidence folder summary page, navigate to the **Evidence** table. Under the **Time** column, choose a piece of evidence to open. 

1. Review the details of the evidence. 
   + To learn more about this information, see [Reviewing evidence in AWS Audit Manager](review-evidence.md). 

## Next steps
<a name="delegation-for-delegates-reviewing-control-set-and-evidence-next-steps"></a>

In some cases you might need to provide additional evidence to demonstrate compliance. In these cases, you can manually upload evidence. For instructions, see [Adding manual evidence in AWS Audit Manager](upload-evidence.md).

If you want to leave comments about one or more of the controls that were delegated to you, see [Adding comments about a control during a control set review](delegation-for-delegates-add-comment.md).