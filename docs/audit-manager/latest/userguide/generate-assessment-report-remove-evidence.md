

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Removing evidence from an assessment report
<a name="generate-assessment-report-remove-evidence"></a>



If you need to remove evidence from an assessment report, follow these steps. You can either remove an entire evidence folder, or you can remove specific evidence items from within a folder. 

## Procedure
<a name="generate-assessment-report-remove-evidence-procedure"></a>

**To remove evidence from an assessment report**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Assessments** and then choose the name of the assessment to open it.

1. On the **Controls** tab, scroll down to the **Control sets** table and choose the name of a control to open it.

1. Choose how you want to remove evidence from your assessment report.

   1. To remove an entire evidence folder, scroll down to **Evidence folders**, select the folder that you want to remove, and then choose **Remove from assessment report**. 
**Tip**  
If you can't see the folder that you're looking for, change the dropdown filter to **All time**. Otherwise, you'll see the last seven days of folders by default.   
If **Remove from assessment report** is greyed out, the evidence folder was already removed from the assessment report.

   1. To remove specific evidence, choose an evidence folder to open its contents. Select one or more items from the list, and then choose **Remove from assessment report**. 
**Tip**  
If **Remove from assessment report** is greyed out, make sure that you selected the check box next to the evidence, and then try again.

1. After you add the evidence to the assessment report, a green success banner appears. Choose **View evidence in assessment report** to see the evidence that will be included in your assessment report.
   + Alternatively, you can see the evidence that will be included in your assessment report by navigating back to your assessment and choosing the **Assessment report selection** tab.

## Next steps
<a name="generate-assessment-report-remove-evidence-next-steps"></a>

When you're ready to generate an assessment report, see [Generating an assessment report](generate-assessment-report-generation-steps.md).

## Additional resources
<a name="generate-assessment-report-remove-evidence-additional-resources"></a>

To find answers to common questions and issues, see [Troubleshooting assessment report issues](assessment-report-issues.md) in the *Troubleshooting* section of this guide.