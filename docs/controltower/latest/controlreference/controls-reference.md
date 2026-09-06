

# The AWS Control Tower Control Catalog
<a name="controls-reference"></a>

The following sections include an individual reference entry for each of the controls available in AWS Control Tower. The controls are grouped into sections according to common characteristics. Each control reference entry includes the details, artifacts, additional information, and considerations to keep in mind when enabling a specific control on a OU in your landing zone.

**Note**  
The Control Catalog was formerly called the Controls Library. We have renamed it for consistency.

**How to view controls**
+ To retrieve information about individual controls programmatically, call the [`GetControl`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_GetControl.html) API from the *controlcatalog* namespace of AWS Control Tower.
+ To retrieve a list of available controls programmatically, call the [`ListControls`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControls.html) API from the *controlcatalog* namespace of AWS Control Tower.
+ Additional detail about each control is available in the AWS Control Tower console, on the **Control details** pages and Control Catalog APIs. For more information, see [View control details](https://docs.aws.amazon.com/controltower/latest/controlreference/control-details.html).
+ To understand control ARNs, see [Resource identifiers for APIs and controls](https://docs.aws.amazon.com/controltower/latest/controlreference/control-identifiers.html).

**Topics**
+ [Mandatory controls](mandatory-controls.md)
+ [Proactive controls](proactive-controls.md)
+ [Preventive controls](preventive-controls.md)
+ [Detective controls](detective-controls.md)
+ [Controls with parameters](control-parameter-concepts.md)
+ [Optional controls](optional-controls.md)
+ [Strongly recommended controls](strongly-recommended-controls.md)
+ [Elective controls](elective-controls.md)
+ [Search for controls with Amazon Q](q-search.md)

**Note**  
The four mandatory controls with `"Sid": "GRCLOUDTRAILENABLED"` are identical by design. The sample code is correct.