

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Editing a custom control in AWS Audit Manager
<a name="edit-controls"></a>



You might need to modify your custom controls in AWS Audit Manager as your compliance requirements change. 

This page outlines the steps to edit a custom control's details, evidence sources, and action plan instructions. 

## Prerequisites
<a name="edit-controls-prerequisites"></a>

The following procedure assumes that you have previously created a custom control.

Make sure your IAM identity has appropriate permissions to edit a custom control in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="edit-controls-procedure"></a>

Follow these steps to edit a custom control.

**Note**  
When you edit a control, your changes are applied to all assessments where the control is active. In all of those assessments, Audit Manager will automatically start to collect evidence according to the latest control definition.

**Tasks**
+ [Step 1: Edit control details](#edit-controls-step1)
+ [Step 2: Edit evidence sources](#edit-controls-step2)
+ [Step 3: Edit action plan](#edit-controls-step3)

### Step 1: Edit control details
<a name="edit-controls-step1"></a>

Review and edit the control details as needed.

**Important**  
We strongly recommend that you never put sensitive identifying information into free-form fields such as **Control details** or **Testing information**. If you create custom controls that contain sensitive information, you can’t share any of your custom frameworks that contain these controls.

**To edit control details**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Control library** and then choose the **Custom** tab.

1. Select the control that you want to edit and then choose **Edit**.

1. Under **Control details**, edit the control details as needed.

1. Under **Testing information**, edit the description as needed.

1. Choose **Next**.

### Step 2: Edit evidence sources
<a name="edit-controls-step2"></a>

Next, you can edit, remove, or add evidence sources for the control.

**Note**  
When you edit a control to include more or fewer evidence sources, this might affect how much evidence your control collects in any assessments where it’s active. For example, if you add evidence sources, you might notice that Audit Manager performs more resource assessments and collects more evidence than before. If you remove evidence sources, it’s likely that your control will collect less evidence moving forward.   
For more information about resource assessments and pricing, see [AWS Audit Manager Pricing](https://aws.amazon.com/audit-manager/pricing/).

#### To edit an AWS managed source
<a name="edit-using-aws-managed-evidence-sources"></a>

**To edit an AWS managed source**

1. Under **AWS managed sources**, review the current selections and make changes as needed.

1. To add a common control, follow these steps:

   1. Select **Use a common control that matches your compliance goal**.

   1. Choose a common control from the dropdown list.

   1. (Optional) Repeat step 2 as needed. You can add up to five common controls.

1. To remove a common control, choose the **X** next to the control name.

1. To add a core control, follow these steps: 

   1. Select **Use a core control that matches a prescriptive AWS guideline**.

   1. Choose a common control from the dropdown list.

   1. (Optional) Repeat step 4 as needed. You can add up to 50 core controls.

1. To remove a core control, choose the **X** next to the control name. 

1. To add customer managed data sources, use the following procedure. Otherwise, choose **Next**.

#### To edit a customer managed source
<a name="edit-using-customer-managed-data-sources"></a>

**Note**  
You're responsible for maintaining the data source mappings that you edit in this step.

**To edit a customer managed source**

1. Under **Customer managed sources**, review the current data sources and make changes as needed.

1. To remove a data source, select a data source from the table, then choose **Remove**.

1. To add a new data source, follow these steps:

   1. Select **Use a data source to collect manual or automated evidence**.

   1. Choose **Add**.

   1. Choose one of the following options:
      + Choose **AWS API calls**, then choose an API call and an evidence collection frequency.
      + Choose **AWS CloudTrail event**, then choose an event name.
      + Choose **AWS Config managed rule**, then choose a rule identifier.
      + Choose **AWS Config custom rule**, then choose a rule identifier. 
      + Choose **AWS Security Hub CSPM control**, then choose a Security Hub CSPM control.
      + Choose **Manual data source**, then choose an option:
        + **File upload** – Use this option if the control requires documentation as evidence.
        + **Text response** – Use this option if the control requires an answer to a risk assessment question. 
**Tip**  
For information about automated data source types and troubleshooting tips, see [Supported data source types for automated evidence](control-data-sources.md).  
If you need to validate your data source setup with an expert, choose **Manual data source** for now. That way, you can create the control and add it to a framework now, and then [edit the control](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-controls.html) as needed later.

   1. Under **Data source name**, provide a descriptive name.

   1. (Optional) Under **Additional details**, enter a data source description and a troubleshooting description.

   1. Choose **Add data source**.

   1. (Optional) To add another data source, choose **Add** and repeat step 3. You can add up to 100 data sources.

1. When you're finished, choose **Next**.

### Step 3: Edit action plan
<a name="edit-controls-step3"></a>

Next, review and edit the optional action plan.

**Important**  
We strongly recommend that you never put sensitive identifying information into free-form fields such as **Action plan**. If you create custom controls that contain sensitive information, you can’t share any of your custom frameworks that contain these controls.

**To edit an action plan**

1. Under **Title**, edit the title as needed.

1. Under **Instructions**, edit the instructions as needed.

1. Choose **Next**.

### Step 4: Review and save
<a name="edit-controls-step4"></a>

Review the information for the control. To change the information for a step, choose **Edit**. 

When you're finished, choose **Save changes**.

**Note**  
After you edit a control, the changes take effect as follows in all active assessments that include the control:  
For controls with *AWS API calls* as the data source type, changes take effect at 00:00 UTC the following day.
For all other controls, changes take effect immediately. 

## Next steps
<a name="edit-controls-next-steps"></a>

When you're certain that you no longer need a custom control, you can clean up your Audit Manager environment by deleting the control. For instructions, see [Deleting a custom control in AWS Audit Manager](delete-controls.md).

## Additional resources
<a name="edit-controls-additional-resources"></a>

For solutions to control issues in Audit Manager, see [Troubleshooting control and control set issues](control-issues.md). 