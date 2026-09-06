

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Reviewing a standard control
<a name="control-library-review-standard-controls"></a>



You can review the details of a standard control by using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI). 

## Prerequisites
<a name="control-library-review-standard-controls-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view controls in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="control-library-review-standard-controls-procedure"></a>

You can review the details of a standard control by using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI). 

------
#### [ Audit Manager console ]

**To view standard control details on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Control library**. 

1. Choose **Standard** to see the standard controls that are provided by AWS.

1. Choose any standard control name to view the details for that control.

1. Review the standard control details using the following information as reference.

**Overview section**  
This section describes the standard control and lists the [data source types](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#control-data-source) that it uses to collect evidence.

**Evidence sources tab**  
This tab includes the following information:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-standard-controls.html)

**Details tab**  
This tab includes the following information:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-standard-controls.html)

------
#### [ AWS CLI ]

**To view standard control details in the AWS CLI**

1. Follow the steps to [find a control](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html). Make sure to set the `--control-type` as `Standard`, and apply any optional filters as needed.

   ```
   aws auditmanager list-controls --control-type Standard
   ```

1. In the response, identify the control that you want to review and take note of the control ID and Amazon Resource Name (ARN).

1. Run the [get-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html) command and specify the `--control-id`. In the following example, replace the {{placeholder text}} with your own information.

   ```
   aws auditmanager get-control --control-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
   ```
**Tip**  
The control details are returned in JSON format. To help you understand this data, see [get-control Output](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html#output) in the *AWS CLI Command Reference*

1. To see tag details, run the [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-tags-for-resource.html) command and specify the `--resource-arn`. In the following example, replace the {{placeholder text}} with your own information.

   ```
   aws auditmanager list-tags-for-resource --resource-arn arn:aws:auditmanager:{{us-east-1}}:111122223333:control/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
   ```

------
#### [ Audit Manager API ]

**To view standard control details using the API**

1. Follow the steps to [find a control](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html). Make sure to set the [controlType](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html#auditmanager-ListControls-request-controlType) as `Standard`, and apply any optional filters as needed.

1. In the response, identify the control that you want to review and take note of the control ID and Amazon Resource Name (ARN).

1. Use the [GetControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html) operation and specify the [controlId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html#auditmanager-GetControl-request-controlId) that you noted in step 2.
**Tip**  
The control details are returned in JSON format. To help you understand this data, see [GetControl Response Elements](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html#API_GetControl_ResponseElements) in the *AWS Audit Manager API Reference*.

1. To see tag details, use the [ListTagsForResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListTagsForResource.html) operation and specify the [resourceArn](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListTagsForResource.html#auditmanager-ListTagsForResource-request-resourceArn) that you noted in step 2.

For more information about these API operations, choose any of the links in this procedure to read more in the *AWS Audit Manager API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="control-library-review-standard-controls-next-steps"></a>

You can add a standard control to any of your custom frameworks. For instructions, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md).

You can also customize any standard control so that it meets your needs. For instructions, see [Making an editable copy of a control in AWS Audit Manager](customize-control-from-existing.md).

## Additional resources
<a name="control-library-review-standard-controls-additional-resources"></a>
+ [Reviewing a common control](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-common-controls.html)
+ [Reviewing a core control](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-core-controls.html)
+ [Reviewing a custom control](control-library-review-custom-controls.md)