# Deleting a custom control in AWS Audit Manager

If you created a custom control and you no longer need it, you can delete it from your
Audit Manager environment. This enables you to clean up your workspace and focus on the custom controls
that are relevant to your current tasks and priorities.

## Prerequisites

The following procedure assumes that you have previously created a custom
control.

Make sure your IAM identity has appropriate permissions to delete a custom control in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can delete custom controls using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface
(AWS CLI).

###### Important

When you delete a custom control, this action removes the control from any custom
frameworks or assessments that it's currently related to. As a result, Audit Manager will stop
collecting evidence for that custom control in all of your assessments. This includes
assessments that you previously created before you deleted the custom control.

Audit Manager console

###### To delete a custom control on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Control library** and then
   choose the **Custom controls** tab.
3. Select the control that you want to delete, and then choose
   **Delete**.
4. In the pop-up window that appears, choose **Delete** to confirm
   deletion.

AWS CLI

###### To delete a custom control in the AWS CLI

1. First, identify the custom control that you want to delete. To do this, run the
   [list-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-controls.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-controls.html") command and specify the `--control-type` as
   `Custom`.

```
 aws auditmanager list-controls --control-type Custom
```

The response returns a list of custom controls. Find the control that you want
to delete, and take note of the control ID. 2. Next, run the [delete-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-control.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-control.html") command and use the `--control-id` parameter to
specify the control that you want to delete.

In the following example, replace the `placeholder
 text` with your own information.

```
aws auditmanager delete-control --control-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

Audit Manager API

###### To delete a custom control using the API

1. Use the [ListControls](../APIReference/API_ListControls.md "../APIReference/API_ListControls.md")
   operation and specify the [controlType](../APIReference/API_ListControls.md#auditmanager-ListControls-request-controlType "../APIReference/API_ListControls.md#auditmanager-ListControls-request-controlType") as `Custom`. From the response, find the control
   that you want to delete and note the control ID.
2. Use the [DeleteControl](../APIReference/API_DeleteControl.md "../APIReference/API_DeleteControl.md") operation to delete the custom control. In the request, use
   the [controlId](../APIReference/API_DeleteControl.md#auditmanager-DeleteControl-request-controlId "../APIReference/API_DeleteControl.md#auditmanager-DeleteControl-request-controlId") parameter to specify the control that you want to
   delete.

For more information about these API operations, choose any of the links in the
previous procedure to read more in the _AWS Audit Manager API
Reference_. This includes information about how to use these operations and
parameters in one of the language-specific AWS SDKs.

## Additional resources

For information about data retention in Audit Manager, see [Deletion of Audit Manager data](data-protection.md#data-deletion-and-retention "data-protection.md#data-deletion-and-retention").
