

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Using the control library to manage controls in AWS Audit Manager
<a name="control-library"></a>



You can access and manage controls from the control library in AWS Audit Manager. 

## Key points
<a name="control-library-key-points"></a>

In the control library, controls are organized into the following categories.
+ **Common controls** collect evidence that supports multiple overlapping compliance standards. Automated common controls contain one or more related [core controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#core-control) that each collect supporting evidence from a predefined group of data sources. This provides you with an efficient way to identify the AWS data sources that map to your portfolio of compliance requirements. The underlying data sources for each automated common control are validated and maintained by industry certified assessors in [AWS Security Assurance Services](https://aws.amazon.com/professional-services/security-assurance-services).
+ **Standard controls** collect evidence to support a specific compliance standard. You can view the details of standard controls, but you can't edit or delete them. However, you can make an editable copy of any standard control to create a new control that meets your specific requirements.
+ **Custom controls** are controls that you own and define. When you create a custom control, we recommend that you choose the common controls that represent your goals and use them as an evidence source. As a result, your custom control can collect all of the evidence that’s relevant to those common controls. You can also use core controls as an evidence source, or use other sources that you define yourself. When you’re done, add your custom controls to a custom framework, and then create an assessment to start collecting evidence.

## Additional resources
<a name="control-library-additional-resources"></a>

To create and manage controls in Audit Manager, follow the procedures that are outlined here.
+ [Finding the available controls in AWS Audit Manager](access-available-controls.md)
+ [Reviewing a control in AWS Audit Manager](control-library-review-controls.md)
  + [Reviewing a common control](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-common-controls.html)
  + [Reviewing a core control](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library-review-core-controls.html)
  + [Reviewing a standard control](control-library-review-standard-controls.md)
  + [Reviewing a custom control](control-library-review-custom-controls.md)
+ [Creating a custom control in AWS Audit Manager](create-controls.md)
  + [Creating a custom control from scratch in AWS Audit Manager](customize-control-from-scratch.md)
  + [Making an editable copy of a control in AWS Audit Manager](customize-control-from-existing.md)
+ [Editing a custom control in AWS Audit Manager](edit-controls.md)
+ [Changing how often a control collects evidence](change-evidence-collection-frequency.md)
+ [Deleting a custom control in AWS Audit Manager](delete-controls.md)
+ [Supported data source types for automated evidence](control-data-sources.md)
  + [AWS Config Rules supported by AWS Audit Manager](control-data-sources-config.md)
  + [AWS Security Hub CSPM controls supported by AWS Audit Manager](control-data-sources-ash.md)
  + [AWS API calls supported by AWS Audit Manager](control-data-sources-api.md)
  + [AWS CloudTrail event names supported by AWS Audit Manager](control-data-sources-cloudtrail.md)