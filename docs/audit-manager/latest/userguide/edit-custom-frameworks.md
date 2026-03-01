# Editing a custom framework in AWS Audit Manager

You might need to modify your custom frameworks in AWS Audit Manager as your compliance
requirements change.

This page outlines the steps to edit a custom framework's details and control sets.

## Prerequisites

The following procedure assumes that you have previously created a custom
framework.

Make sure your IAM identity has appropriate permissions to edit a custom framework in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### Tasks

- [Step 1: Edit framework details](#edit-step1 "#edit-step1")
- [Step 2: Edit control sets](#edit-step2 "#edit-step2")
- [Step 3. Review and save](#edit-step3 "#edit-step3")

### Step 1: Edit framework details

Start by reviewing and editing the existing framework details.

###### To edit framework details

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Framework library** and then
   choose the **Custom frameworks** tab.
3. Select the framework that you want to edit, choose **Actions**, and
   then choose **Edit**.
   - Alternatively, open a custom framework and choose **Edit** at
     the top right of the framework details page.

4. Under **Framework details**, review the name, compliance type, and
   description for your framework, and make any necessary changes.
5. Choose **Next**.

###### Tip

To edit the tags for a framework, open the framework and choose the [framework tags tab](review-frameworks.md "review-frameworks.md"). There you can view and edit the tags that are associated
with the framework.

### Step 2: Edit control sets

Next, review and edit the controls and control sets in the framework.

###### Note

When you use the AWS Audit Manager console to edit a custom framework, you can add up to 10
control sets for each framework.

When you use the Audit Manager API to edit a custom framework, you can add more than 10
control sets. To add more control sets than the console currently allows, use the [UpdateAssessmentFramework](../APIReference/API_UpdateAssessmentFramework.md "../APIReference/API_UpdateAssessmentFramework.md") API that Audit Manager provides.

###### To edit a control set

1. Under **Control set name**, review and edit the name for your
   control set as needed.
2. Under **Add controls**, use the **Control type**
   dropdown list to select one of the two control types: **Standard
   controls** or **Custom controls**.
3. Based on the option you selected in the previous step, a table list of standard
   controls or custom controls is displayed. Select one or more controls and choose
   **Add to control set**.
4. In the pop-up window that appears, choose **Add**.
5. Review and edit the controls that appear in the **Selected
   controls** list.
   - To add more controls, repeat steps 2–4.
   - To remove unwanted controls, select one or more controls and choose
     **Remove from control set**.

6. To add a new control set to the framework, choose **Add control
   set**.
7. To remove an unwanted control set, choose **Remove control
   set**.
8. After you finish adding control sets and controls, choose
   **Next**.

### Step 3. Review and save

Review the information for your framework. To change the information for a step, choose
**Edit**.

When you're finished, choose **Save changes**.

## Next steps

When you're certain that you no longer need a custom framework, you can clean up your
Audit Manager environment by deleting the framework. For instructions, see [Deleting a custom framework in AWS Audit Manager](delete-custom-framework.md "delete-custom-framework.md").

## Additional resources

For solutions to framework issues in Audit Manager, see [Troubleshooting framework issues](framework-issues.md "framework-issues.md").
