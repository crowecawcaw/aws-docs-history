# Regional differences for AWS Control Tower

functionality

Certain differences exist in the behavior of AWS Control Tower across AWS Regions, because
AWS Control Tower orchestrates the behavior of other AWS services. For example:

- AWS Service Catalog is not available in all AWS Regions where AWS Control Tower is available, which
  changes the behavior of Account Factory in those Regions.
- In certain Regions, Account Factory Customizations (AFC) is not available because
  Service Catalog is not available to support the underlying functionality for blueprints.
- Certain controls are not available in all AWS Regions due to lack of underlying
  functionality.
- AFT and CfCT are not available in all AWS Regions due to lack of underlying
  functionality.
  To make the best determination of behavior for your AWS Control Tower environment, ascertain your
  home Region. Then, evaluate the following items. For more details, see [Limitations and
  quotas in AWS Control Tower](limits.md "limits.md").

- Is AWS Service Catalog available in your desired home Region?
- Are the controls available that you require? See [Control
  limitations](control-limitations.md "control-limitations.md").
- Is IAM Identity Center available in your desired home Region?
  **Deployable Regions for controls**

AWS Control Tower cannot activate certain controls when you deploy them in certain Regions, due
to lack of underlying dependencies. You can find the most updated information about
the deployable Regions for any control by calling the `ListControls` and
`GetControl` APIs. You also can view the deployable Regions in the AWS Control Tower
console.

When you activate a control on an OU that's governed by AWS Control Tower, the control's effective
area is the _intersection_ of your AWS Control Tower governed Regions with the control's deployable Regions.

For example, a control can be enabled on an OU that operates in governed Regions X, Y and
Z. But after it is enabled, the same control is deployed only on Regions X and Z, because
the control itself does not support Region Y.

It's important to monitor the relationships among controls that you deploy and Regions
where you operate workloads in AWS Control Tower, so that you don't experience gaps in protection of
your AWS resources.

**How to check your protected Regions**

- In the AWS Control Tower console, you can view the enabled controls and Regions in the
  **Enabled controls** section.
- If you call the
  `GetEnabledControl` API, the **targetRegions** parameter
  will show only those Regions where you can deploy the control effectively, not the
  non-deployable Regions.
