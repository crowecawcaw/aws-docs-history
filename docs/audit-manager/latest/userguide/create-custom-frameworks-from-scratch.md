# Creating a custom framework from

scratch in AWS Audit Manager

When your organization's compliance requirements don't align with the pre-built standard
frameworks that are available in AWS Audit Manager, you can create your own custom framework from
scratch instead.

This page outlines the steps to create a custom framework that's tailored to your
specific needs.

## Prerequisites

Make sure your IAM identity has appropriate permissions to create a custom framework
in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### Tasks

- [Step 1: Specify framework details](#from-scratch-step1 "#from-scratch-step1")
- [Step 2: Specify control sets](#from-scratch-step2 "#from-scratch-step2")
- [Step 3: Review and create the framework](#from-scratch-step3 "#from-scratch-step3")

### Step 1: Specify framework details

Start by specifying details about your custom framework.

###### To specify framework details

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Framework library** and
   then choose **Create custom framework**.
3. Under **Framework details**, enter a name, a compliance type
   (optional), and a description for your framework (also optional). Entering a
   compliance type such as _PCI_DSS_ or _GDPR_ means you can use this keyword to search for your
   framework later.
4. Under **Tags**, choose **Add new tag** to associate a tag
   with your framework. You can specify a key and a value for each tag. The tag key is
   mandatory. You can use it as search criteria when searching for this framework in the
   framework library.
5. Choose **Next**.

### Step 2: Specify control sets

Next, you specify which controls you want add to your framework and how you want to
organize them. Start by adding control sets to the framework, and then add controls to the
control set.

###### Note

When you use the AWS Audit Manager console to create a custom framework, you can add up to
10 control sets for each framework.

When you use the Audit Manager API to create a custom framework, you can create more than 10 control
sets. To add more control sets than the console currently allows, use the [CreateAssessmentFramework](../APIReference/API_CreateAssessmentFramework.md "../APIReference/API_CreateAssessmentFramework.md") API that Audit Manager provides.

###### To specify a control set

1. Under **Control set name**, enter a name for your control
   set.
2. Under **Add controls**, use the **Control type**
   dropdown list to select one of the two control types: **Standard
   controls** or **Custom controls**.
3. Based on the option that you selected in the previous step, a list of standard
   controls or custom controls is displayed. Select one or more controls and choose
   **Add to control set**.
4. In the pop-up window that appears, choose **Add to control
   set**.
5. Review the controls that appear in the **Selected controls**
   list.
   - To add more controls, repeat steps 2–4.
   - To remove unwanted controls, select one or more controls and choose
     **Remove control**.

6. To add a new control set, choose **Add control set**.
7. To remove an unwanted control set, choose **Remove control
   set**.
8. After you finish adding control sets and controls, choose
   **Next**.

### Step 3: Review and create the framework

Review the information for your framework. To change the information for a step,
choose **Edit**.

When you're finished, choose **Create custom framework**.

## Next steps

After you create your new custom framework, you can create an assessment from your
framework. For more information, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

To revisit your custom framework at a later date, see [Finding the available frameworks in AWS Audit Manager](access-frameworks.md "access-frameworks.md"). You can follow these
steps to locate your custom framework so that you can then view, edit, share, or delete
it.

## Additional

resources

For solutions to framework issues in Audit Manager, see [Troubleshooting framework issues](framework-issues.md "framework-issues.md").
