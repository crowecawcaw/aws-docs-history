

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Reviewing a common control
<a name="control-library-review-common-controls"></a>



When you need to review the details of a control, you'll find the information organized into several sections on the control details page. These sections help you easily access and understand the relevant information for that control.

## Prerequisites
<a name="control-library-review-common-controls-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view common controls in Audit Manager. More specifically, you need the following permissions to view the common controls, control objectives, and control domains that are provided by AWS Control Catalog:
+ `controlcatalog:ListCommonControls`
+ `controlcatalog:ListDomains` 
+ `controlcatalog:ListObjectives` 

A suggested policy that grants these permissions is [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html).

## Procedure
<a name="control-library-review-common-controls-procedure"></a>

You can review a common control using the Audit Manager console, the AWS Control Catalog API, or the AWS Command Line Interface (AWS CLI). 

------
#### [ Audit Manager console ]

**To view common control details on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Control library**. 

1. Choose **Common** to see the common controls that are provided by AWS.

1. Choose any common control name to view the details for that control.

1. Review the common control details using the following information as reference.

**Overview section**  
This section describes the common control.

**Evidence sources tab**  
This tab includes the following information:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-common-controls.html)

**Related requirements tab**  
When you collect evidence for this common control, the same evidence can help you to demonstrate compliance with the requirements of the related standard controls that are listed on this tab. Choose any standard control to see more details.   
+ The common control might produce evidence that demonstrates only partial compliance with a standard control. It’s possible that you might need additional evidence to demonstrate full compliance with a standard control.
+ At this time, the **Related requirements** tab shows related standard controls only. Although a common control can be related to one or more custom controls, those relationships aren't displayed in this tab. 

------
#### [ AWS CLI ]

**To view common control details in the AWS CLI**

1. Run the [list-common-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controlcatalog/list-common-controls.html) command to see a list of available common controls. When you use this operation, you can apply an optional `common-control-filter` to see common controls that have a specific objective. 

   ```
   aws controlcatalog list-common-controls
   ```

1. In the response, identify the common control that you want to review and take note of its details.

------
#### [ AWS Control Catalog API ]

**To view common control details using the API**

1. Use the [ListCommonControls](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html) operation to see a list of available common controls. When you use this operation, you can apply an optional `commonControlFilter` to see a list of controls that have a specific objective. 

1. In the response, identify the control that you want to review and take note of its details.

For more information about these API operations, choose the link in this procedure to read more in the *AWS Control Catalog API Reference*. This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.

------

## Next steps
<a name="control-library-review-common-controls-next-steps"></a>

You can choose the common controls that represent your goals and use them as building blocks to create a custom control. Each automated common control maps to a predefined grouping of AWS data sources that Audit Manager handles for you. This means that you don’t have to be an AWS expert to know which data sources collect the relevant evidence for your goals. Moreover, you don't have to maintain these data source mappings yourself. 

For instructions on how to create a custom control that uses common controls as an evidence source, see [Creating a custom control in AWS Audit Manager](create-controls.md).

## Additional resources
<a name="control-library-review-common-controls-additional-resources"></a>
+ [Reviewing a core control](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-core-controls.html)
+ [Reviewing a standard control](control-library-review-standard-controls.md)
+ [Reviewing a custom control](control-library-review-custom-controls.md)