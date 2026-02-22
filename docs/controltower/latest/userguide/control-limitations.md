# Control limitations

AWS Control Tower assists you with maintaining a secure, multi-account environment on AWS by
means of controls, which are implemented in various forms, such as service control
policies (SCPs), AWS Config rules, and CloudFormation hooks.

###### The Controls Reference Guide

Detailed information about AWS Control Tower controls has been moved to [the AWS Control Tower
Controls Reference Guide](../controlreference/introduction.md "../controlreference/introduction.md").

If
you modify AWS Control Tower resources, such as an SCP, or remove any AWS Config resource, such as a
Config recorder or aggregator, AWS Control Tower can no longer guarantee that the controls are
functioning as designed. Therefore, the security of your multi-account environment may
be compromised. The AWS [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model "https://aws.amazon.com/compliance/shared-responsibility-model") of security is applicable to any such changes you may
make.

###### Note

AWS Control Tower helps maintain the integrity of your environment by resetting the SCPs
of the preventive controls to their standard configuration when you update your
landing zone. Changes that you may have made to SCPs are replaced by the standard
version of the control, by design.

**Limitations by Region**

Some controls in AWS Control Tower do not operate in certain AWS Regions where AWS Control Tower is
available, because those Regions do not support the required underlying functionality.
As a result, when you deploy that control, it may not be operating in all Regions that
you govern with AWS Control Tower. This limitation affects certain detective controls, certain
proactive controls, and certain controls in the **Security Hub CSPM Service-managed
Standard: AWS Control Tower**. For more information about Regional availability, see
the [Security Hub
controls](../controlreference/security-hub-controls.md "../controlreference/security-hub-controls.md"). Also see the [Regional services list documentation](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") and the [Security Hub CSPM
controls reference documentation](../../../securityhub/latest/userguide/securityhub-controls-reference.md "../../../securityhub/latest/userguide/securityhub-controls-reference.md").

Control behavior also is limited in case of _mixed
governance_. For more information, see [Avoid mixed governance when configuring
Regions](mixed-governance.md "mixed-governance.md").

For more information about how AWS Control Tower manages the limitations of Regions and
controls, see [Considerations for activating AWS
opt-in Regions](opt-in-region-considerations.md "opt-in-region-considerations.md").

###### Note

For the most updated information about controls and Region support, we recommend
that you call the [`GetControl`](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md") and [`ListControls`](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") API operations.

## Find available controls and Regions

You can view the available Regions for each control in the AWS Control Tower console. You
can view the available Regions programmatically with the [`GetControl`](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md") and [`ListControls`](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") APIs from AWS Control Catalog.

For information about AWS Security Hub CSPM controls from the **Service-Managed
Standard: AWS Control Tower** that are not supported in certain AWS Regions,
see "Unsupported Regions" in the [Security Hub CSPM
standard](../controlreference/security-hub-controls.md "../controlreference/security-hub-controls.md").
