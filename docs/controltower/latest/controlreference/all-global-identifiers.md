# All global identifiers for AWS Control Tower controls

###### Warning

The data previously displayed on this page was outdated and has been removed. This page will be removed in a future release.

A _global identifier_ for a control is a unique identifier, independent of the Region in which a control is deployed. Global identifiers are associated with controls that are included in [AWS Control Catalog](../../../controlcatalog/latest/userguide/what-is-controlcatalog.md "../../../controlcatalog/latest/userguide/what-is-controlcatalog.md"), which is a compendium of controls from several AWS services.

The global identifier fulfills the final portion of the Amazon Resource Name (ARN), which is of the following form:

```
arn:`{PARTITION}`:controlcatalog:::control/`{CONTROL_CATALOG_OPAQUE_ID}`
```

To obtain the complete global identifier programmatically, with the full ARN, you can call the [`GetControl`](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md") and [`ListControls`](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") APIs. You also can view the complete global ARN in the AWS Control Tower console, on the **Control details** page.

For more information about control identifiers and ARNs, see [Resource identifiers for APIs and controls](control-identifiers.md "control-identifiers.md").
