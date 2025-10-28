# Integrated AWS Config controls available in AWS Control Tower

AWS Control Tower is integrated with AWS Config to provide over 500 selected additional detective controls that
help you monitor and manage your AWS environment. These AWS Config controls are available in the
AWS Control Tower console and the Control Catalog APIs. The **Control owner** or
**Implementation** field for these controls is displayed as
AWS Config or `AWS::Config::ConfigRule`.

You can use AWS Control Tower to search and discover the AWS Config rules that you need to govern your
multi-account environment; and you can enable and manage these controls directly from the AWS Control Tower console. To
search from the console, go to the Control Catalog and search for controls with the
**Implementation** filter AWS Config. (Example: `Implementation = AWS Config`)

The AWS Control Tower console and AWS Config console each display the same metqdata for these controls.

You can enable and disable the AWS Config controls through the AWS Control Tower console or the [`EnableControl`](../APIReference/API_EnableControl.md "../APIReference/API_EnableControl.md") and [`DisableControl`](../APIReference/API_DisableControl.md "../APIReference/API_DisableControl.md") APIs. Control details are viewable programmatically by
calling the Control Catalog
[`GetControl`](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md") and [`ListControls`](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") APIs.

###### Differences

- In AWS Config, these integrated controls are listed by identifier.
- In the AWS Control Tower console and APIs, the integrated controls are shown with names
  that summarize their function.

###### Note

AWS Control Tower documentation does not provide a comprehensive list of integrated AWS Config
controls. For more information about these controls, see [List of AWS Config
managed rules](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") in the _AWS Config Developer Guide_, or view them
in the AWS Control Tower console.

## Change in drift behavior with service-linked AWS Config rules

Before the introduction of service-linked Config rules in AWS Control Tower, you could modify AWS Config rule configurations or add remediations outside of AWS Control Tower. With the release of service-linked Config rules, this behavior has changed:

- Modifications made to Config rule settings outside of AWS Control Tower are treated as drift.
- External remediation configurations added to these Config rules are treated as drift.
- AWS Control Tower automatically removes these external modifications with the adoption of service-linked Config rules.
- To maintain consistent governance, all updates that AWS Control Tower supports for your service-linked Config rules must be managed through AWS Control Tower.

###### Important

Before you adopt service-linked Config rules, review the existing customizations,
such as remediations, that you have made to Config rules outside of AWS Control Tower,
because these customizations will be removed during the transition. The AWS Config APIs do
not support adding remediation configurations for service-linked AWS Config rules. See [`PutRemediationConfigurations`](../../../config/latest/APIReference/API_PutRemediationConfigurations.md "../../../config/latest/APIReference/API_PutRemediationConfigurations.md").
