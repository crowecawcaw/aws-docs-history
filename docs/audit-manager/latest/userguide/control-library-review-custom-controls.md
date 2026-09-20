

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Reviewing a custom control
<a name="control-library-review-custom-controls"></a>



You can review the details of a custom control by using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI). 

## Prerequisites
<a name="control-library-review-custom-controls-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view controls in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="control-library-review-custom-controls-procedure"></a>

You can review the details of a custom control by using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI). 

------
#### [ Audit Manager console ]

**To view custom control details on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Control library**. 

1. Choose **Custom** to see the custom controls that you created.

1. Choose any custom control name to view the details for that control.

1. Review the custom control details using the following information as reference.

**Overview section**  
This section describes the custom control and lists the [data source types](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#control-data-source) that it uses to collect evidence. It also provides information about when the control was created and last updated.

**Evidence sources tab**  
This tab shows where the custom control collects evidence from. It includes the following information:  


<table>
<thead>
  <tr><th>Name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Common controls</b></td><td>These are the common controls that collect evidence to support the custom control.<br />Common controls collect evidence using underlying data sources that AWS manages for you. For every common control that’s listed, Audit Manager collects the relevant evidence for all of the supporting core controls. Choose a common control to see the related core controls.</td></tr>
  <tr><td><b>Core controls</b></td><td>These are the core controls that collect evidence to support the custom control.<br />Core controls collect evidence by using a predefined group of data sources that AWS manages for you. Choose a core control to see the underlying data sources.</td></tr>
  <tr><td><b>Data sources</b></td><td>These are the data sources that collect evidence to support the custom control. These data sources aren't managed for you by AWS. You're responsible for maintaining them. <ul><li> <b>Name</b> – The name of the data source. </li><li> <b>Type</b> – The type of data source that the evidence comes from. <ul><li> If Audit Manager collects the evidence, the type can be <i>AWS Security Hub CSPM</i>, <i>AWS Config</i>, <i>AWS CloudTrail</i>, or <i>AWS API calls</i>.  </li><li> If you upload your own evidence, the type is <i>Manual</i>. A description indicates if the required manual evidence is a <i>File upload</i> or a <i>Text response</i>. </li></ul> </li><li> <b>Mapping</b> – The specific keyword that's used to collect evidence. <ul><li> If the type is <i>AWS Config</i>, the mapping is an AWS Config rule (such as <code>SNS_ENCRYPTED_KMS</code>). </li><li> If the type is <i>AWS Security Hub CSPM</i>, the mapping is a Security Hub CSPM control (such as <code>EC2.1</code>). </li><li> If the type is <i>AWS API calls</i>, the mapping is an API call (such as <code>kms_ListKeys</code>). </li><li> If the type is <i>AWS CloudTrail</i>, the mapping is a CloudTrail event (such as <code>CreateAccessKey</code>). </li></ul> </li><li> <b>Frequency</b> – How often Audit Manager collects evidence for an AWS API call data source. </li></ul></td></tr>
</tbody>
</table>


**Details tab**  
This tab includes the following information:  


<table>
<thead>
  <tr><th>Name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Instructions</b></td><td>The directions that describe how to test and remediate the control.</td></tr>
  <tr><td><b>Testing information</b></td><td>The recommended testing procedures.</td></tr>
  <tr><td><b>Action plan</b></td><td>The recommended actions to take if you need to remediate the control.</td></tr>
  <tr><td><b>Tags</b></td><td>The tags that are associated with the control.</td></tr>
  <tr><td><b>Key</b></td><td>The tag key (for example, a compliance standard, regulation, or category).</td></tr>
  <tr><td><b>Value</b></td><td>The tag value.</td></tr>
</tbody>
</table>


------
#### [ AWS CLI ]

**To view custom control details in the AWS CLI**

1. Follow the steps to [find a control](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html). Make sure to set the `--control-type` as `Custom`, and apply any optional filters as needed.

   ```
   aws auditmanager list-controls --control-type Custom
   ```

1. In the response, identify the control that you want to review and take note of the control ID and Amazon Resource Name (ARN).

1. Run the [get-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html) command and specify the `--control-id`. In the following example, replace the {{placeholder text}} with your own information.

   ```
   aws auditmanager get-control --control-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
   ```
**Tip**  
The control details are returned in JSON format. To help you understand this data, see [get-control Output](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html#output) in the *AWS CLI Command Reference*.

1. To see the tags for a control, use the [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-tags-for-resource.html) command and specify the `--resource-arn`. In the following example, replace the {{placeholder text}} with your own information:

   ```
   aws auditmanager list-tags-for-resource --resource-arn arn:aws:auditmanager:{{us-east-1:111122223333}}:control/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
   ```

------
#### [ Audit Manager API ]

**To view custom control details using the API**

1. Follow the steps to [find a control](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html). Make sure to set the [controlType](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html#auditmanager-ListControls-request-controlType) as `Custom`, and apply any optional filters as needed.

1. In the response, identify the control that you want to review and take note of the control ID and its Amazon Resource Name (ARN).

1. Use the [GetControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html) operation and specify the [controlId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html#auditmanager-GetControl-request-controlId) that you noted in step 2.
**Tip**  
The control details are returned in JSON format. To help you understand this data, see [GetControl Response Elements](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html#API_GetControl_ResponseElements) in the *AWS Audit Manager API Reference*.

1. To see tags for the control, use the [ListTagsForResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListTagsForResource.html) operation and specify the control [resourceArn](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListTagsForResource.html#auditmanager-ListTagsForResource-request-resourceArn) that you noted in step 2. 

For more information about these API operations, choose any of the links in this procedure to read more in the *AWS Audit Manager API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="control-library-review-custom-controls-next-steps"></a>

You can add a custom control to any of your custom frameworks. For instructions, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md).

You can also [edit a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-controls.html), [make an editable copy of a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/customize-control-from-existing.html), or [delete a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-controls.html) that you no longer need.

## Additional resources
<a name="control-library-review-custom-controls-additional-resources"></a>
+ [Reviewing a common control](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-common-controls.html)
+ [Reviewing a core control](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-core-controls.html)
+ [Reviewing a standard control](control-library-review-standard-controls.md)