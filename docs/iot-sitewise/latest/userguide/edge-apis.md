# Use AWS IoT SiteWise APIs on the edge

AWS IoT SiteWise provides a subset of its APIs, along with edge-specific APIs, enabling seamless
interaction with asset models and their associated assets deployed at the edge. These
asset models must be configured to run on the edge. For more information, see [Configure an asset model for data
processing on SiteWise Edge](edge-processing.md#process-gateway-data-edge "edge-processing.md#process-gateway-data-edge") for
detailed instructions on this setup process.

After you configure these APIs, you can retrieve comprehensive data about your asset
models and individual assets. Retrieving asset model, asset, dashboard, portal and
project information can help you monitor deployed portals and dashboards, and access
asset data collected at the edge level. This provides a central host in your network for
interactions with AWS IoT SiteWise without requiring a web API call.

###### Topics

- [All available AWS IoT SiteWise Edge device APIs](edge-apis-available.md "edge-apis-available.md")
- [Edge-only APIs for use with AWS IoT SiteWise edge
  devices](edge-local-apis.md "edge-local-apis.md")
- [Enable CORS on AWS IoT SiteWise Edge APIs](enable-cors-edge-apis.md "enable-cors-edge-apis.md")
- [Configure session timeouts for
  AWS IoT SiteWise Edge](edge-apis-session-timeout.md "edge-apis-session-timeout.md")
- [Tutorial: List asset models on an AWS IoT SiteWise Edge
  gateway](edge-apis-tutorial.md "edge-apis-tutorial.md")
