# Finding the available controls in AWS Audit Manager

You can find all available controls on the **Control library** page in
the Audit Manager console.

You can also view all available controls using the Audit Manager API or the AWS Command Line Interface (AWS CLI).

## Prerequisites

Make sure your IAM identity has appropriate permissions to view controls in AWS Audit Manager.
Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

Audit Manager console

###### To view available controls on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Control library**.
3. Choose a tab to browse the available controls.
   - Choose **Common** to see the common controls that are
     provided by AWS.
   - Choose **Standard** to see the standard controls that are
     provided by AWS.
   - Choose **Custom** to see the custom controls that you
     created.

AWS CLI

###### To find common controls in the (AWS CLI

Run the [list-common-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controlcatalog/list-common-controls.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controlcatalog/list-common-controls.html") command to see a list of common controls.

```
aws controlcatalog list-common-controls
```

You can also use the optional `common-control-filter` attribute to return
a list of common controls that have a specific objective.

In the following example, replace the `placeholder text` with your own information.

```
aws controlcatalog list-common-controls --common-control-filter `OBJECTIVE-ARN`
```

###### To find other types of controls in the AWS CLI

Run the [list-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-controls.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-controls.html") command and specify the `--control-type` as
`Custom`, `Standard`, or `Core`.

In the following example, replace the `placeholder text` with your own information.

```
aws auditmanager list-controls --control-type `Type`
```

Audit Manager API

###### To find common controls using the API

Use the [ListCommonControls](../../../controlcatalog/latest/APIReference/API_ListCommonControls.md "../../../controlcatalog/latest/APIReference/API_ListCommonControls.md") operation to see a list of available common controls.
You can also use the optional `commonControlFilter` attribute to return a
list of controls that have a specific objective.

###### To find other types of control using the API

Use the [ListControls](../APIReference/API_ListControls.md "../APIReference/API_ListControls.md")
operation and specify the [controlType](../APIReference/API_ListControls.md#auditmanager-ListControls-request-controlType "../APIReference/API_ListControls.md#auditmanager-ListControls-request-controlType") as `Custom`, `Standard`, or
`Core`.

For more information, choose any of the links in the previous procedure to read more
in the _AWS Audit Manager API Reference_. This includes
information about how to use these operations and parameters in one of the
language-specific AWS SDKs.

## Next steps

When you're ready to explore the details of a control, follow the steps in [Reviewing a control in AWS Audit Manager](control-library-review-controls.md "control-library-review-controls.md"). This page will guide you through the control details and explain the information that
you see there.

From the control library page, you can also [create a custom control](create-controls.md "create-controls.md"),
[edit a
custom control](edit-controls.md "edit-controls.md"), or [delete a custom
control](delete-controls.md "delete-controls.md").

## Additional resources

For solutions to control issues in Audit Manager see [Troubleshooting control and control set issues](control-issues.md "control-issues.md").
