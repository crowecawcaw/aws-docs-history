

# All global identifiers for AWS Control Tower controls
<a name="all-global-identifiers"></a>

**Warning**  
The data previously displayed on this page was outdated and has been removed. This page will be removed in a future release.

A *global identifier* for a control is a unique identifier, independent of the Region in which a control is deployed. Global identifiers are associated with controls that are included in [AWS Control Catalog](https://docs.aws.amazon.com/controlcatalog/latest/userguide/what-is-controlcatalog.html), which is a compendium of controls from several AWS services.

The global identifier fulfills the final portion of the Amazon Resource Name (ARN), which is of the following form:

```
arn:{{{PARTITION}}}:controlcatalog:::control/{{{CONTROL_CATALOG_OPAQUE_ID}}}
```

To obtain the complete global identifier programmatically, with the full ARN, you can call the [`GetControl`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_GetControl.html) and [`ListControls`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControls.html) APIs. You also can view the complete global ARN in the AWS Control Tower console, on the **Control details** page.

For more information about control identifiers and ARNs, see [Resource identifiers for APIs and controls](https://docs.aws.amazon.com/controltower/latest/controlreference/control-identifiers.html).