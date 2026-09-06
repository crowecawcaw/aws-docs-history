

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Submitting a reviewed control set back to the audit owner
<a name="delegation-for-delegates-submitting-back-to-audit-owner"></a>



After reviewing the control set, adding comments or additional evidence, and updating the status of individual controls, you reach an important step – submitting the reviewed control set back to the audit owner. Submitting the reviewed control set marks the completion of your delegated tasks, and enables the audit owner to incorporate your insights and recommendations into the overall assessment.

## Prerequisites
<a name="delegation-for-delegates-submitting-back-to-audit-owner-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to submit the reviewed control set back to the audit owner in AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="delegation-for-delegates-submitting-back-to-audit-owner-procedure"></a>

Follow these steps to submit the control set to the audit owner.

**To submit a reviewed control set back to the audit owner**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. Choose **Notifications** in the left navigation pane. 

1. Review the list of control sets that were delegated to you. Find the control set that you want to submit back to the audit owner, and choose the name of the related assessment.

1. Scroll down to the **Control sets** table, select the control set that you want to submit to the audit owner, and then choose **Submit for review**.

1. In the pop-up window that appears, you can add comments before choosing **Submit for review**. 