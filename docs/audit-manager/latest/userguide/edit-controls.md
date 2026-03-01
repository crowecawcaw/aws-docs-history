# Editing a custom control in AWS Audit Manager

You might need to modify your custom controls in AWS Audit Manager as your compliance requirements
change.

This page outlines the steps to edit a custom control's details, evidence sources, and
action plan instructions.

## Prerequisites

The following procedure assumes that you have previously created a custom
control.

Make sure your IAM identity has appropriate permissions to edit a custom control in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

Follow these steps to edit a custom control.

###### Note

When you edit a control, your changes are applied to all assessments where the control
is active. In all of those assessments, Audit Manager will automatically start to collect evidence
according to the latest control definition.

###### Tasks

- [Step 1: Edit control details](#edit-controls-step1 "#edit-controls-step1")
- [Step 2: Edit evidence sources](#edit-controls-step2 "#edit-controls-step2")
- [Step 3: Edit action plan](#edit-controls-step3 "#edit-controls-step3")

### Step 1: Edit control details

Review and edit the control details as needed.

###### Important

We strongly recommend that you never put sensitive identifying information into
free-form fields such as **Control details** or **Testing
information**. If you create custom controls that contain sensitive
information, you can’t share any of your custom frameworks that contain these
controls.

###### To edit control details

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Control library** and then choose
   the **Custom** tab.
3. Select the control that you want to edit and then choose
   **Edit**.
4. Under **Control details**, edit the control details as
   needed.
5. Under **Testing information**, edit the description as
   needed.
6. Choose **Next**.

### Step 2: Edit evidence sources

Next, you can edit, remove, or add evidence sources for the control.

###### Note

When you edit a control to include more or fewer evidence sources, this might affect
how much evidence your control collects in any assessments where it’s active. For example,
if you add evidence sources, you might notice that Audit Manager performs more resource assessments
and collects more evidence than before. If you remove evidence sources, it’s likely that
your control will collect less evidence moving forward.

For more information about resource assessments and pricing, see [AWS Audit Manager Pricing](https://aws.amazon.com/audit-manager/pricing/ "https://aws.amazon.com/audit-manager/pricing/").

###### To edit an AWS managed source

1. Under **AWS managed sources**, review the current selections
   and make changes as needed.
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

5. To remove a core control, choose the **X** next to the control
   name.
6. To add customer managed data sources, use the following procedure. Otherwise,
   choose **Next**.

###### Note

You're responsible for maintaining the data source mappings that you edit in this
step.

###### To edit a customer managed source

1. Under **Customer managed sources**, review the current data
   sources and make changes as needed.
2. To remove a data source, select a data source from the table, then choose
   **Remove**.
3. To add a new data source, follow these steps:
   1. Select **Use a data source to collect manual or automated
      evidence**.
   2. Choose **Add**.
   3. Choose one of the following options:
      - Choose **AWS API calls**, then choose an API call and
        an evidence collection frequency.
      - Choose **AWS CloudTrail event**, then choose an event
        name.
      - Choose **AWS Config managed rule**, then choose a rule
        identifier.
      - Choose **AWS Config custom rule**, then choose a rule
        identifier.
      - Choose **AWS Security Hub CSPM control**, then choose a Security Hub CSPM
        control.
      - Choose **Manual data source**, then choose an
        option:
        - **File upload** – Use this option if the
          control requires documentation as evidence.
        - **Text response** – Use this option if the
          control requires an answer to a risk assessment question.

   ###### Tip

   For information about automated data source types and troubleshooting
   tips, see [Supported data source types for automated evidence](control-data-sources.md "control-data-sources.md").

   If you need to validate your data source setup with an expert, choose
   **Manual data source** for now. That way, you can create
   the control and add it to a framework now, and then [edit the control](edit-controls.md "edit-controls.md") as needed later. 4. Under **Data source name**, provide a descriptive
   name. 5. (Optional) Under **Additional details**, enter a data
   source description and a troubleshooting description. 6. Choose **Add data source**. 7. (Optional) To add another data source, choose **Add** and
   repeat step 3. You can add up to 100 data sources.

4. When you're finished, choose **Next**.

### Step 3: Edit action plan

Next, review and edit the optional action plan.

###### Important

We strongly recommend that you never put sensitive identifying information into
free-form fields such as **Action plan**. If you create custom controls
that contain sensitive information, you can’t share any of your custom frameworks that
contain these controls.

###### To edit an action plan

1. Under **Title**, edit the title as needed.
2. Under **Instructions**, edit the instructions as needed.
3. Choose **Next**.

### Step 4: Review and save

Review the information for the control. To change the information for a step, choose
**Edit**.

When you're finished, choose **Save changes**.

###### Note

After you edit a control, the changes take effect as follows in all active assessments
that include the control:

- For controls with _AWS API calls_ as the data
  source type, changes take effect at 00:00 UTC the following day.
- For all other controls, changes take effect immediately.

## Next steps

When you're certain that you no longer need a custom control, you can clean up your Audit Manager
environment by deleting the control. For instructions, see [Deleting a custom control in AWS Audit Manager](delete-controls.md "delete-controls.md").

## Additional resources

For solutions to control issues in Audit Manager, see [Troubleshooting control and control set issues](control-issues.md "control-issues.md").
