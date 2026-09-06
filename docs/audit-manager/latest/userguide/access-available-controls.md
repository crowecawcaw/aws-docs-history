

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Finding the available controls in AWS Audit Manager
<a name="access-available-controls"></a>



You can find all available controls on the **Control library** page in the Audit Manager console. 

You can also view all available controls using the Audit Manager API or the AWS Command Line Interface (AWS CLI). 

## Prerequisites
<a name="access-available-controls-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view controls in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="access-available-controls-procedure"></a>

------
#### [ Audit Manager console ]

**To view available controls on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Control library**. 

1. Choose a tab to browse the available controls. 
   + Choose **Common** to see the common controls that are provided by AWS.
   + Choose **Standard** to see the standard controls that are provided by AWS.
   + Choose **Custom** to see the custom controls that you created.

------
#### [ AWS CLI ]

**To find common controls in the (AWS CLI**  
Run the [list-common-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controlcatalog/list-common-controls.html) command to see a list of common controls.

```
aws controlcatalog list-common-controls
```

You can also use the optional `common-control-filter` attribute to return a list of common controls that have a specific objective. 

In the following example, replace the {{placeholder text }}with your own information.

```
aws controlcatalog list-common-controls --common-control-filter {{OBJECTIVE-ARN}}
```

**To find other types of controls in the AWS CLI**  
Run the [list-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-controls.html) command and specify the `--control-type` as `Custom`, `Standard`, or `Core`.

In the following example, replace the {{placeholder text }}with your own information.

```
aws auditmanager list-controls --control-type {{Type}}
```

------
#### [ Audit Manager API ]

**To find common controls using the API**  
Use the [ListCommonControls](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html) operation to see a list of available common controls. You can also use the optional `commonControlFilter` attribute to return a list of controls that have a specific objective. 

**To find other types of control using the API**  
Use the [ListControls](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html) operation and specify the [controlType](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html#auditmanager-ListControls-request-controlType) as `Custom`, `Standard`, or `Core`.

For more information, choose any of the links in the previous procedure to read more in the *AWS Audit Manager API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="access-available-controls-next-steps"></a>

When you're ready to explore the details of a control, follow the steps in [Reviewing a control in AWS Audit Manager](control-library-review-controls.md). This page will guide you through the control details and explain the information that you see there.

From the control library page, you can also [create a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-controls.html), [edit a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-controls.html), or [delete a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-controls.html).

## Additional resources
<a name="access-available-controls-additional-resources"></a>

For solutions to control issues in Audit Manager see [Troubleshooting control and control set issues](control-issues.md).