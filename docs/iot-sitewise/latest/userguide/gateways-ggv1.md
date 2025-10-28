# Use AWS IoT SiteWise Edge gateways

AWS IoT SiteWise Edge extends cloud capabilities to industrial edge environments, enabling local
data processing, analysis, and decision-making. SiteWise Edge integrates with AWS IoT SiteWise and other
AWS services to provide comprehensive industrial IoT solutions. Gateways serve as the
intermediary between your industrial equipment and AWS IoT SiteWise.

SiteWise Edge gateways runs on two different deployment targets:

- AWS IoT Greengrass V2
- Siemens Industrial Edge
  You can use a SiteWise Edge gateway to collect data at the edge and publish it to the cloud. For
  gateways running on AWS IoT Greengrass, you can also process data at the edge using asset models and
  assets.

The AWS IoT SiteWise Edge application on Siemens Industrial Edge supports integration between industrial
equipment and AWS IoT SiteWise so that you can aggregate and process raw machine data and run analyses
locally before sending refined data to the AWS Cloud.

## Key concepts of SiteWise Edge gateways

SiteWise Edge has several useful features for edge computing in industrial
environments.

**Local data collection and processing**

Supports data collection from industrial assets using protocols like
OPC-UA and MQTT. Gateways run on AWS IoT Greengrass Core devices or
Siemens Industrial Edge.

**Offline operation**

Continues collecting and processing data during internet outages, syncing
with the cloud when connectivity is restored.

**Edge computing with AWS IoT Greengrass components**

Uses IoT SiteWise publisher to forward data to the cloud and AWS IoT SiteWise processor
for local transformations and calculations. Both the publisher and processor
are AWS IoT Greengrass V2 components. For more information on AWS IoT Greengrass components, see [AWS-provided
components](../../../greengrass/v2/developerguide/public-components.md "../../../greengrass/v2/developerguide/public-components.md").

**Integration with AWS IoT SiteWise to extend cloud
features**

Works with the AWS IoT SiteWise cloud features, extending asset models, analytics,
and dashboards to the edge.

For gateways with a data processing pack enabled, you can use AWS OpsHub for
AWS IoT SiteWise to centrally manage your SiteWise Edge gateways. AWS OpsHub provides remote
management and monitoring capabilities. For more information, see [Manage SiteWise Edge gateways using AWS OpsHub for AWS IoT SiteWise](manage-gateways-ggv2.md#opshub-app "manage-gateways-ggv2.md#opshub-app").

**Partner data source integration**

Connect a partner data source to your gateway and receive data from the
partner in your SiteWise Edge gateway and the AWS cloud. For more information,
see [Partner data sources on SiteWise Edge
gateways](partner-data-sources.md "partner-data-sources.md").

**Local visualization on the edge**

Provides custom dashboards for real-time insights at the edge.

Monitor data locally in your facility using SiteWise Monitor portals on your local
devices. For more information, see [Enabling your AWS IoT SiteWise portal at the edge](monitor-enable-edge.md "monitor-enable-edge.md").

## Benefits of implementing SiteWise Edge

SiteWise Edge offers numerous advantages that can significantly improve industrial
operations and decision-making processes.

- Real-time operational insights without cloud processing delays
- Operational continuity in disconnected environments
- Reduced bandwidth and storage costs through edge pre-processing
- Increased reliability with the ability to make local, data-driven
  decisions
