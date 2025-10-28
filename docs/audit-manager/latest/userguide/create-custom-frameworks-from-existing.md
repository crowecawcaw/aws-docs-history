# Making an editable copy of an

existing framework in AWS Audit Manager

Instead of creating a custom framework from scratch, you can use an existing framework
as a starting point and make an editable copy. When you do this, the existing framework
remains in the framework library, and a new custom framework is created with your specific
settings.

You can make an editable copy of any existing framework. It can be either a standard
framework or a custom framework.

## Prerequisites

Make sure your IAM identity has appropriate permissions to create a custom framework
in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### Tasks

- [Step 1: Specify framework details](#from-existing-step1 "#from-existing-step1")
- [Step 2: Specify control sets](#from-existing-step2 "#from-existing-step2")
- [Step 3: Review and create the framework](#from-existing-step3 "#from-existing-step3")

### Step 1: Specify framework details

All framework details, except tags, are carried over from the original framework.
Review and modify these details as needed.

###### To specify framework details

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Framework library**.
3. Choose the framework you want to use as a starting point, choose **Create
   custom framework**, and then choose **Make a
   copy**.
4. In the pop-up window that appears, enter a name for the new custom framework and
   choose **Continue**.
5. Under **Framework details**, review the name, compliance type,
   and description for your framework, and change them as needed. The compliance type
   should indicate the compliance standard or the regulation that's associated with your
   framework. You can use this keyword to search for your framework.
6. Under **Tags**, choose **Add new tag** to
   associate a tag with your framework. You can specify a key and a value for each tag.
   The tag key is mandatory and can be used as a search criteria when you search for this
   framework in the framework library.
7. Choose **Next**.

### Step 2: Specify control sets

The control sets are carried over from the original framework. Change the current
configuration by adding more controls or removing existing controls as needed.

###### Note

When you use the Audit Manager console to create a custom framework, you can add up to 10
control sets for each framework.

When you use the Audit Manager API to create a custom framework, you can add more than 10
control sets. To add more control sets than the console currently allows, use the [CreateAssessmentFramework](../APIReference/API_CreateAssessmentFramework.md "../APIReference/API_CreateAssessmentFramework.md") API that Audit Manager provides.

###### To specify a control set

1. Under **Control set name**, change the name of the control set as
   needed.
2. Under **Add controls**, add a new control by using the dropdown
   list to select one of the two control types: **Standard controls** or
   **Custom controls**.
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

6. To add a new control set to the framework, choose **Add control
   set**.
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

## Additional resources

For solutions
to framework issues in Audit Manager, see [Troubleshooting framework issues](framework-issues.md "framework-issues.md").
