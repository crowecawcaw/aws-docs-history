# The AWS Control Tower Control Catalog

The following sections include an individual reference entry for each of the controls
available in AWS Control Tower. The controls are grouped into sections according to common
characteristics.

Each control reference entry includes the details, artifacts, additional information, and
considerations to keep in mind when enabling a specific control on a OU in your landing
zone.

###### Note

The Control Catalog was formerly called the Controls Library. We have renamed it for consistency.

###### How to view controls

- To retrieve information about individual controls programmatically, call the [`GetControl`](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md") API from the _controlcatalog_ namespace of AWS Control Tower.
- To retrieve a list of available controls programmatically, call the [`ListControls`](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") API from the _controlcatalog_ namespace of AWS Control Tower.
- Additional detail about each control is available in the AWS Control Tower console, on the **Control details** pages and Control Catalog APIs. For more information, see [View control details](control-details.md "control-details.md").
- To understand control ARNs, see [Resource identifiers for APIs and controls](control-identifiers.md "control-identifiers.md").

###### Topics

- [Mandatory controls](mandatory-controls.md "mandatory-controls.md")
- [Proactive controls](proactive-controls.md "proactive-controls.md")
- [Preventive controls](preventive-controls.md "preventive-controls.md")
- [Detective controls](detective-controls.md "detective-controls.md")
- [Controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md")
- [Optional controls](optional-controls.md "optional-controls.md")
- [Strongly recommended
  controls](strongly-recommended-controls.md "strongly-recommended-controls.md")
- [Elective controls](elective-controls.md "elective-controls.md")
- [Search for controls with Amazon Q](q-search.md "q-search.md")

###### Note

The four mandatory controls with `"Sid": "GRCLOUDTRAILENABLED"` are
identical by design. The sample code is correct.
