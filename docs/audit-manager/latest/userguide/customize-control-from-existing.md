

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Making an editable copy of a control in AWS Audit Manager
<a name="customize-control-from-existing"></a>



Instead of creating a custom control from scratch, you can use an existing standard control or custom control as a starting point and make an editable copy that meets your needs. When you do this, the existing standard control remains in the control library, and a new control is created with your custom settings.

## Prerequisites
<a name="from-existing-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to create a custom framework in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

To successfully collect evidence from AWS Config and Security Hub CSPM, make sure that you do the following:
+ [Enable AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html), then apply the [required settings for using AWS Config with Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-recommendations.html#setup-recommendations-services).
+ [Enable Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html), then apply the [required settings for using Security Hub CSPM with Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-recommendations.html#set-up-securityhub).

 Audit Manager can then collect evidence each time an evaluation occurs for a given AWS Config rule or Security Hub CSPM control. 

## Procedure
<a name="customize-control-from-existing-procedure"></a>

**Topics**
+ [Step 1: Specify control details](#from-existing-step-1)
+ [Step 2: Specify evidence sources](#from-existing-step-2)
+ [Step 3: (Optional): Define an action plan](#from-existing-step-3)
+ [Step 4: Review and create the control](#from-existing-step-4)

### Step 1: Specify control details
<a name="from-existing-step-1"></a>

The control details are inherited from the original control. Review and modify these details as needed.

**Important**  
We strongly recommend that you never put sensitive identifying information into free-form fields such as **Control details** or **Testing information**. If you create custom controls that contain sensitive information, you can’t share any of your custom frameworks that contain these controls.

**To specify control details**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Control library**.

1. Select the standard control or custom control that you want to make changes to, and then choose **Make a copy**. 

1. Specify the new name of the control, and choose **Continue**. 

1. Under **Control details**, customize the control details as needed.

1. Under **Testing information**, make changes to the instructions as needed.

1. Under **Tags**, customize the tags as needed. 

1. Choose **Next**.

### Step 2: Specify evidence sources
<a name="from-existing-step-2"></a>

Evidence sources are inherited from the original control. You can change, add, or remove evidence sources as needed.

#### To specify an AWS managed source (recommended)
<a name="customize-using-aws-managed-evidence-sources"></a>

**Tip**  
We recommend that you start by choosing one or more common controls. If you have more fine-grained compliance requirements, you can also choose one or more specific core controls.

**To specify an AWS managed source**

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

1. To edit customer managed data sources, use the following procedure. Otherwise, choose **Next**.

#### To specify a customer managed source
<a name="customize-using-customer-managed-data-sources"></a>

To collect automated evidence from a data source, you must choose a data source type and a data source mapping. These details map to your AWS usage, and tell Audit Manager where to collect the evidence from. If you want to provide your own evidence, you’ll choose a manual data source instead.

**Note**  
You're responsible for maintaining the data source mappings that you create in this step.

**To specify a customer managed source**

1. Under **Customer managed sources**, review the current data sources and make changes as needed.

1. To remove a data source, select a data source from the table and choose **Remove**.

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

### Step 3: (Optional): Define an action plan
<a name="from-existing-step-3"></a>

The action plan is inherited from the original control. You can edit this action plan as needed.

**Important**  
We strongly recommend that you never put sensitive identifying information into free-form fields such as **Action plan**. If you create custom controls that contain sensitive information, you can’t share any of your custom frameworks that contain these controls.

**To specify instructions**

1. Under **Title**, review the title and make changes as needed.

1. Under **Instructions**, review the instructions and make changes as needed.

1. Choose **Next**.

### Step 4: Review and create the control
<a name="from-existing-step-4"></a>

Review the information for the control. To change the information for a step, choose **Edit**. When you're finished, choose **Create custom control**.

## Next steps
<a name="from-existing-whatnow"></a>

After you create a new custom control, you can add it to a custom framework. To learn more, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md) or [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md). 

After you add a custom control to a custom framework, you can create an assessment and start collecting evidence. To learn more, see [Creating an assessment in AWS Audit Manager](create-assessments.md).

To revisit your custom control at a later date, see [Finding the available controls in AWS Audit Manager](access-available-controls.md). You can follow these steps to locate your custom control so that you can view, edit, or delete it.

## Additional resources
<a name="customize-control-from-existing-additional-resources"></a>

For solutions to control issues in Audit Manager, see [Troubleshooting control and control set issues](control-issues.md).