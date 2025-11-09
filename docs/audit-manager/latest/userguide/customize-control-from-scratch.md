# Creating a custom control from scratch in

AWS Audit Manager

When your organization's compliance requirements don't align with the pre-built standard
controls that are available in AWS Audit Manager, you can create your own custom control from
scratch.

This page outlines the steps to create a custom control that's tailored to your specific
needs.

## Prerequisites

Make sure your IAM identity has appropriate permissions to create a custom control
in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

To successfully collect evidence from AWS Config and Security Hub, make sure that you do the
following:

- [Enable AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md"), then
  apply the [required settings for using AWS Config with Audit Manager](setup-recommendations.md#setup-recommendations-services "setup-recommendations.md#setup-recommendations-services")
- [Enable
  Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md"), then apply the [required settings for using Security Hub with Audit Manager](setup-recommendations.md#set-up-securityhub "setup-recommendations.md#set-up-securityhub")

Audit Manager can then collect evidence each time an evaluation occurs for a given AWS Config
rule or Security Hub control.

## Procedure

###### Tasks

- [Step 1: Specify control details](#from-scratch-step-1 "#from-scratch-step-1")
- [Step 2: Specify evidence sources](#from-scratch-step-2 "#from-scratch-step-2")
- [Step 3 (Optional): Define action plan](#from-scratch-step-3 "#from-scratch-step-3")
- [Step 4: Review and create the control](#from-scratch-step-4 "#from-scratch-step-4")

### Step 1: Specify control details

Start by specifying the details of your custom control.

###### Important

We strongly recommend that you never put sensitive identifying information into
free-form fields such as **Control details** or **Testing
information**. If you create custom controls that contain sensitive
information, you can’t share any of your custom frameworks that contain these
controls.

###### To specify control details

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Control library**, and then
   choose **Create custom control**.
3. Under **Control details**, enter the following information about
   the control.
   - **Control** – Enter a friendly name, a title, or a
     risk assessment question. This value helps you to identify your control in the
     control library.
   - **Description (optional)** – Enter details to help
     others understand the control's objective. This description appears on the control
     details page.

4. Under **Testing information**, enter the recommended steps for
   testing the control.
5. Under **Tags**, choose **Add new tag** to
   associate a tag with the control. You can specify a key for each tag that best
   describes the compliance framework that this control supports. The tag key is
   mandatory and can be used as a search criteria when you search for this control in the
   control library.
6. Choose **Next**.

### Step 2: Specify evidence sources

Next, specify some evidence sources. An evidence source determines where your custom
control collects evidence from. You can use AWS managed sources, customer managed
sources, or both.

###### Tip

We recommend that you use AWS managed sources. Whenever an AWS managed source is
updated, the same updates are automatically applied to all custom controls that use these
sources. This means that your custom controls collect evidence against the latest
definitions of that evidence source.

If you’re not sure which options to choose, see the following examples and our
recommendations.

| Your role        | Your goal                                                                 | Recommended evidence source                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GRC professional | I want to collect evidence for a particular domain or objective           | AWS managed ([common control](concepts.md#common-control "concepts.md#common-control"))<br>Use a predefined grouping of data sources that map to a specific common<br>control.    |
| Technical expert | I want to collect evidence about the AWS resources I'm responsible<br>for | AWS managed ([core control](concepts.md#core-control "concepts.md#core-control"))<br>Use a predefined grouping of data sources that map to an AWS<br>requirement.                 |
| Technical expert | I want to use a custom AWS Config rule to collect evidence                | Customer managed (Automated [data source](concepts.md#control-data-source "concepts.md#control-data-source"))<br>Use a custom data source to collect specific automated evidence. |
| GRC professional | I want to collect evidence, such as documents and text responses          | Customer managed (Manual [data source](concepts.md#control-data-source "concepts.md#control-data-source"))<br>Use a custom data source to upload your own manual evidence.        |

We recommend that you start by choosing one or more common controls. When you
choose the common control that represents your goal, Audit Manager collects the relevant
evidence for all of the supporting core controls. You can also choose individual core
controls if you want to collect targeted evidence about your AWS environment.

###### To specify an AWS managed source

1. Go to the **AWS managed sources** section of the
   page.
2. To add a common control, follow these steps:
   1. Select **Use a common control that matches your compliance
      goal**.
   2. Choose a common control from the dropdown list.
   3. (Optional) Repeat step 2 as needed. You can add up to five common
      controls.

3. To remove a common control, choose the **X** next to the
   control name.
4. To add a core control, follow these steps:
   1. Select **Use a core control that matches a prescriptive AWS
      guideline**.
   2. Choose a common control from the dropdown list.
   3. (Optional) Repeat step 4 as needed. You can add up to 50 core
      controls.

5. To remove a core control, choose the **X** next to the
   control name.
6. To add customer managed data sources, use the following procedure. Otherwise,
   choose **Next**.

To collect automated evidence from a data source, you must choose a data source
type and a data source mapping. These details map to your AWS usage, and tell Audit Manager
where to collect the evidence from. If you want to provide your own evidence, you’ll
choose a manual data source instead.

###### Note

You're responsible for maintaining the data source mappings that you create in
this step.

###### To specify a customer managed source

1. Go to the **Customer managed sources** section of the
   page.
2. Select **Use a data source to collect manual or automated
   evidence**.
3. Choose **Add**.
4. Choose one of the following options:
   - Choose **AWS API calls**, then choose an API call and
     an evidence collection frequency.
   - Choose **AWS CloudTrail event**, then choose an event
     name.
   - Choose **AWS Config managed rule**, then choose a rule
     identifier.
   - Choose **AWS Config custom rule**, then choose a rule
     identifier.
   - Choose **AWS Security Hub control**, then choose a Security Hub
     control.
   - Choose **Manual data source**, then choose an
     option:
     - **File upload** – Use this option if the
       control requires documentation as evidence.
     - **Text response** – Use this option if the
       control requires an answer to a risk assessment question.

###### Tip

For information about automated data source types and troubleshooting tips,
see [Supported data source types for automated
evidence](control-data-sources.md "control-data-sources.md").

If you need to validate your data source setup with an expert, choose
**Manual data source** for now. That way, you can create the
control and add it to a framework now, and then [edit the
control](edit-controls.md "edit-controls.md") as needed later. 5. Under **Data source name**, provide a descriptive
name. 6. (Optional) Under **Additional details**, enter a data source
description and a troubleshooting description. 7. Choose **Add data source**. 8. (Optional) To add another data source, choose **Add** and
repeat steps 1-7. You can add up to 100 data sources. 9. To remove a data source, select the data source from the table, then choose
**Remove**. 10. When you're finished, choose **Next**.

### Step 3 (Optional): Define action plan

Next, specify the actions to take if this control needs to be remediated.

###### Important

We strongly recommend that you never put sensitive identifying information into
free-form fields such as **Action plan**. If you create custom
controls that contain sensitive information, you can’t share any of your custom
frameworks that contain these controls.

###### To define action plan

1. Under **Title**, enter a descriptive title for the action
   plan.
2. Under **Instructions**, enter detailed instructions for the
   action plan.
3. Choose **Next**.

### Step 4: Review and create the control

Review the information for the control. To change the information for a step, choose
**Edit**.

When you're finished, choose **Create custom control**.

## Next steps

After you create a new custom control, you can add it to a custom framework. To learn
more, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md "custom-frameworks.md") or [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md "edit-custom-frameworks.md").

After you add the custom control to a custom framework, you can create an assessment
and start collecting evidence. To learn more, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

To revisit your custom control at a later date, see [Finding the available controls in AWS Audit Manager](access-available-controls.md "access-available-controls.md"). You can
follow these steps to locate your custom control so that you can view, edit, or delete
it.

## Additional resources

For solutions to control issues in Audit Manager, see [Troubleshooting control and control set issues](control-issues.md "control-issues.md").
