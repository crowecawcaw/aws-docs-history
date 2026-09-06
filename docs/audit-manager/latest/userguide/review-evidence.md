

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Reviewing evidence in AWS Audit Manager
<a name="review-evidence"></a>



When you need to review a specific piece of evidence, follow the instructions on this page. You'll find the evidence details organized into several sections. 

**Contents**
+ [Prerequisites](#review-evidence-prerequisites)
+ [Procedure](#review-evidence-procedure)
  + [Summary](#review-evidence-folders-detail-1)
  + [Attributes](#review-evidence-folders-detail-2)
  + [Resources included](#review-evidence-folders-detail-3)
+ [Additional resources](#review-evidence-additional-resources)

## Prerequisites
<a name="review-evidence-prerequisites"></a>

The following procedure assumes that you have previously created at least one assessment. If you haven’t created an assessment yet, you won’t see any results when you follow these steps.

Make sure your IAM identity has appropriate permissions to view an assessment in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

Keep in mind that it takes up to 24 hours for an assessment to start collecting automated evidence. If your assessment has no evidence yet, you won’t see any results when you follow these steps. 

## Procedure
<a name="review-evidence-procedure"></a>

**To open and review an evidence details page**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Assessments**, and then choose an assessment.

1. From the assessment page, choose the **Controls** tab, scroll down to the **Controls** table, and then choose a control.

1. From the control page, choose the **Evidence folders** tab.

1. In the **Evidence folders** table, choose the name of an evidence folder.

1. Choose the evidence name under the **Time** column to open the evidence details page.

1. Review the evidence details using the following information as reference.

**Topics**
+ [Summary](#review-evidence-folders-detail-1)
+ [Attributes](#review-evidence-folders-detail-2)
+ [Resources included](#review-evidence-folders-detail-3)

### Summary
<a name="review-evidence-folders-detail-1"></a>

You can use the **Summary** section to see an overview of the evidence. 

![Screenshot of the evidence details with labels that relate to the following definitions.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/evidence-detail-console.png)


In this section, you can review the following information:


| Name | Description | 
| --- | --- | 
| **1. Evidence ID** | The unique identifier for the evidence. | 
| **2. Date and time** | The time and date when the evidence was collected. This is represented in Coordinated Universal Time (UTC). | 
| 3. Compliance check | The evaluation status for compliance check evidence. +  For evidence that's collected from AWS Security Hub CSPM, a **Pass** or **Fail** result is reported directly from AWS Security Hub CSPM. <br />+  For evidence that's collected from AWS Config, a **Compliant** or **Non-compliant** result is reported directly from AWS Config. <br />+  If **Not applicable** is shown, this indicates one of two things. Either you don't have AWS Security Hub CSPM or AWS Config enabled. Or, the evidence comes from a different data source.  | 
| 4. Data source mapping | The mapping keyword that was used to collect the evidence. | 
| 5. Data source type | The type of data source where the evidence was collected from. | 
| 6. Account ID | The AWS account that's associated with the evidence. | 
| 7. IAM ID | The relevant user or role, if applicable. | 
| 8. Assessment | The name of the assessment that's associated with the evidence.  | 
| 9. Control | The name of the control that's associated with the evidence.  | 
| 10. Evidence folder name | The name of the evidence folder that contains the evidence. | 
| 11. Include in assessment report | The switch that enables you to include or exclude the evidence from the assessment report. | 

### Attributes
<a name="review-evidence-folders-detail-2"></a>

You can use the **Attributes** table to see the evidence attributes in detail. 

In this table, you can review the following information:


| Name | Description | 
| --- | --- | 
| **Attribute name** | The key for the attribute. | 
| **Value** | The value of the attribute. In some cases, a link to a JSON file is provided with more information. | 

### Resources included
<a name="review-evidence-folders-detail-3"></a>

You can use the **Resources included** table to see the resources that were assessed to generate this evidence. 

In this section, you can review the following information:


| Name | Description | 
| --- | --- | 
| **ARN** | The Amazon Resource Name (ARN) of the resource. An ARN might not be available for all evidence types. | 
| **Resource compliance** | The evaluation status for the resource.+  For evidence that's collected from AWS Security Hub CSPM, a **Pass** or **Fail** result is reported directly from Security Hub CSPM. <br />+  For evidence that's collected from AWS Config, a **Compliant** or **Non-compliant** result is reported directly from AWS Config. <br />+  If **Not applicable** is shown, this indicates that you either don't have AWS Config or Security Hub CSPM enabled, or the evidence comes from a different data source.  | 
| Value | More information about the resource assessment. In some cases, a link to a JSON file is provided with more information. | 

## Additional resources
<a name="review-evidence-additional-resources"></a>
+ For solutions to evidence issues in Audit Manager, see [Troubleshooting assessment and evidence collection issues](evidence-collection-issues.md).