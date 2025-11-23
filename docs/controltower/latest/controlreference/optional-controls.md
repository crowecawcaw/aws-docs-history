# Optional controls

Optional controls in AWS Control Tower are applied at the OU level. You can activate and
deactivate these optional controls through the AWS Control Tower console, or by means of the
[control APIs](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### AWS Control Tower offers several types of optional controls:

- [Proactive controls](proactive-controls.md "proactive-controls.md"),
  which are based on CloudFormation hooks.
- [Controls implemented with resource control policies
  (RCPs)](rcp-controls.md "rcp-controls.md"),
  which are based on RCPs from AWS Organizations. For more information, see [Resource control policies](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the AWS Organizations documentation.
- [Controls implemented with declarative policies](declarative-controls.md "declarative-controls.md"),
  which are based on _declarative policies_ from AWS Organizations. For more information, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the AWS Organizations documentation.
- [Security Hub controls](security-hub-controls.md "security-hub-controls.md"), which are based on AWS Config rules – these
  controls are owned by Security Hub and integrated with AWS Control Tower, by means of the
  **Service-Managed Standard: AWS Control Tower**.
- [Digital sovereignty controls](digital-sovereignty-controls.md "digital-sovereignty-controls.md"), which are elective controls based
  on SCPs and AWS Config rules, implemented within AWS Control Tower. This group includes the
  [data residency controls](data-residency-controls.md "data-residency-controls.md").
- [Strongly recommended controls](strongly-recommended-controls.md "strongly-recommended-controls.md"), which are based on SCPs and AWS Config
  rules, implemented within AWS Control Tower.
- [Elective controls](elective-controls.md "elective-controls.md"), which are based on SCPs and AWS Config rules,
  implemented within AWS Control Tower.
  The strongly recommended and elective controls owned by AWS Control Tower are optional,
  which means that you can customize the level of enforcement for OUs in your landing zone
  by choosing which ones to enable. Optional controls are not enabled by default. For
  more information about optional controls, see the following control reference pages
  in the next sections.

###### Note

It is important to know that some detective controls in AWS Control Tower do not
operate in certain AWS Regions where AWS Control Tower is available, because those
Regions do not support the required underlying functionality. As a result, when
you deploy a detective control, the control may not be operating in all Regions
that you govern with AWS Control Tower. For details, see [Control limitations](../userguide/control-limitations.md "../userguide/control-limitations.md") and [Security Hub controls](security-hub-controls.md "security-hub-controls.md").

You can view the Regions for each control in the AWS Control Tower console, or by calling the [`GetControl`](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md") API that is part of the [Control Catalog namespace](../../../controlcatalog/latest/userguide/what-is-controlcatalog.md "../../../controlcatalog/latest/userguide/what-is-controlcatalog.md").

For more information about the detective controls that cannot be deployed in
certain Regions, see the [Regional services list documentation](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") to learn more about the
Regions where AWS Config is available. If the detective control is implemented as
a managed AWS Config rule, see the [Security Hub controls reference documentation](../../../securityhub/latest/userguide/securityhub-controls-reference.md "../../../securityhub/latest/userguide/securityhub-controls-reference.md").
