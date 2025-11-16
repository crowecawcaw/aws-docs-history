# Configure edge data processing for AWS IoT SiteWise models

and assets

###### Note

The data processing pack (DPP) feature is no longer availabke to new customers. Existing customers can continue to use the service as normal. For more information, see
[Data processing pack availability change](../appguide/iotsitewise-dpp-availability-change.md "../appguide/iotsitewise-dpp-availability-change.md").

You can use AWS IoT SiteWise Edge to collect, store, organize and monitor equipment data
locally. You can use SiteWise Edge so that you can model your industrial data and
visualize it locally. You can process your data locally and send it to the AWS
Cloud, or process it on-premises by using the AWS IoT SiteWise API.

With AWS IoT SiteWise Edge, you can process raw data locally and choose to send only
aggregated data to the AWS Cloud to optimize your bandwidth usage and cloud
storage costs.

###### Note

- AWS IoT SiteWise retains your edge data on your SiteWise Edge gateways up to 30 days.
  The retention period of your data is dependent on the available disk
  space of your device.
- If your SiteWise Edge gateway has been disconnected from the AWS Cloud for
  30 days, the [Set up an OPC UA source in
  SiteWise Edge](configure-opcua-source.md "configure-opcua-source.md") is automatically
  disabled.

## Configure an asset model for data

processing on SiteWise Edge

You must configure your asset model for the edge before your
can process your SiteWise Edge gateway data at the edge. Your asset model edge
configuration specifies where your assets properties are computed. You can
choose to compute all properties at the edge and send the results to the AWS
Cloud, or customize where to compute each asset property separately. For more
information, see [Configure edge data processing for AWS IoT SiteWise models
and assets](edge-processing.md "edge-processing.md").

Asset properties include metrics, transforms, and measurements:

- Metrics are the asset's aggregated data over a specified period of
  time. You can compute new metrics by using existing metric data. AWS IoT SiteWise
  always sends your metrics to the AWS Cloud for long-term storage.
  AWS IoT SiteWise computes metrics on the AWS Cloud by default. You can configure
  your asset model to compute your metrics at the edge. AWS IoT SiteWise sends
  processed results to the AWS Cloud.
- Transforms are mathematical expressions that map an asset property's
  data points from one form to another. Transforms can use metrics as
  input data and must be computed and stored at the same location as their
  inputs. If you configure a metric input to compute at the edge, AWS IoT SiteWise
  also computes its associated transform at the edge.
- Measurements are formatted as raw data that your device collects and
  sends to the AWS Cloud by default. You can configure your asset model
  to store this data on your local device.

For more information about asset properties, see [Define data properties](asset-properties.md "asset-properties.md").

After you create your asset model, you can then configure it for the edge.
For more information about configuring your asset model for the edge, see [Create an asset model (console)](create-asset-models.md#create-asset-model-console "create-asset-models.md#create-asset-model-console").

###### Note

Asset models and dashboards are automatically synced between the AWS
Cloud and your SiteWise Edge gateway every 10 minutes. You can also sync manually
from the [Manage SiteWise Edge gateways](manage-gateways-ggv2.md "manage-gateways-ggv2.md").

You can use the AWS IoT SiteWise REST APIs and the AWS Command Line Interface (AWS CLI) to query your
SiteWise Edge gateway for data at the edge. Before you query your SiteWise Edge gateway for
data at the edge, you must meet the following prerequisites:

- Your credentials must be set for the REST APIs. For more information
  about setting credentials, see [Manage SiteWise Edge gateways](manage-gateways-ggv2.md "manage-gateways-ggv2.md").
- The SDK endpoint must point to the IP address of your SiteWise Edge gateway.
  You can find more information in the documentation for your SDK. For
  example, see [Specifying Custom Endpoints](../../../sdk-for-javascript/v2/developer-guide/specifying-endpoints.md "../../../sdk-for-javascript/v2/developer-guide/specifying-endpoints.md") in the
  _AWS SDK for Java 2.x Developer Guide_.
- Your SiteWise Edge gateway certificate must be registered. You can find more
  information about registering your SiteWise Edge gateway certificate in the
  documentation for your SDK. For example, see the [Registering Certificate Bundles in Node.js](../../../sdk-for-javascript/v2/developer-guide/node-registering-certs.md "../../../sdk-for-javascript/v2/developer-guide/node-registering-certs.md") in the
  _AWS SDK for Java 2.x Developer Guide_.

For more information about querying data with AWS IoT SiteWise, see [Query data from AWS IoT SiteWise](query-industrial-data.md "query-industrial-data.md").
