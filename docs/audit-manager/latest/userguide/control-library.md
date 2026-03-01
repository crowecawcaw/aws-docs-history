# Using the control library to manage controls in AWS Audit Manager

You can access and manage controls from the control library in AWS Audit Manager.

## Key points

In the control library, controls are organized into the following categories.

- **Common controls** collect evidence that supports
  multiple overlapping compliance standards. Automated common controls contain one or more
  related [core controls](concepts.md#core-control "concepts.md#core-control")
  that each collect supporting evidence from a predefined group of data sources. This
  provides you with an efficient way to identify the AWS data sources that map to your
  portfolio of compliance requirements. The underlying data sources for each automated
  common control are validated and maintained by industry certified assessors in [AWS Security
  Assurance Services](https://aws.amazon.com/professional-services/security-assurance-services "https://aws.amazon.com/professional-services/security-assurance-services").
- **Standard controls** collect evidence to support a
  specific compliance standard. You can view the details of standard controls, but you can't
  edit or delete them. However, you can make an editable copy of any standard control to
  create a new control that meets your specific requirements.
- **Custom controls** are controls that you own and define.
  When you create a custom control, we recommend that you choose the common controls that
  represent your goals and use them as an evidence source. As a result, your custom control
  can collect all of the evidence that’s relevant to those common controls. You can also use
  core controls as an evidence source, or use other sources that you define yourself. When
  you’re done, add your custom controls to a custom framework, and then create an assessment
  to start collecting evidence.

## Additional resources

To create and manage controls in Audit Manager, follow the procedures that are outlined here.

- [Finding the available controls in AWS Audit Manager](access-available-controls.md "access-available-controls.md")
- [Reviewing a control in AWS Audit Manager](control-library-review-controls.md "control-library-review-controls.md")
  - [Reviewing a common control](control-library-review-common-controls.md "control-library-review-common-controls.md")
  - [Reviewing a core control](control-library-review-core-controls.md "control-library-review-core-controls.md")
  - [Reviewing a standard control](control-library-review-standard-controls.md "control-library-review-standard-controls.md")
  - [Reviewing a custom control](control-library-review-custom-controls.md "control-library-review-custom-controls.md")

- [Creating a custom control in AWS Audit Manager](create-controls.md "create-controls.md")
  - [Creating a custom control from scratch in AWS Audit Manager](customize-control-from-scratch.md "customize-control-from-scratch.md")
  - [Making an editable copy of a control in AWS Audit Manager](customize-control-from-existing.md "customize-control-from-existing.md")

- [Editing a custom control in AWS Audit Manager](edit-controls.md "edit-controls.md")
- [Changing how often a control collects evidence](change-evidence-collection-frequency.md "change-evidence-collection-frequency.md")
- [Deleting a custom control in AWS Audit Manager](delete-controls.md "delete-controls.md")
- [Supported data source types for automated evidence](control-data-sources.md "control-data-sources.md")
  - [AWS Config Rules supported by AWS Audit Manager](control-data-sources-config.md "control-data-sources-config.md")
  - [AWS Security Hub CSPM controls supported by AWS Audit Manager](control-data-sources-ash.md "control-data-sources-ash.md")
  - [AWS API calls supported by AWS Audit Manager](control-data-sources-api.md "control-data-sources-api.md")
  - [AWS CloudTrail event names supported by AWS Audit Manager](control-data-sources-cloudtrail.md "control-data-sources-cloudtrail.md")
