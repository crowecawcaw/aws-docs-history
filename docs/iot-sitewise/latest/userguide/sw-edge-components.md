# AWS IoT Greengrass components for AWS IoT SiteWise Edge

SiteWise Edge uses AWS IoT Greengrass components to collect, process, and transmit industrial data at the
edge. These components work together to enable local data processing and seamless
integration with the AWS IoT SiteWise cloud service.

**IoT SiteWise publisher**

The IoT SiteWise publisher component
(`aws.iot.SiteWiseEdgePublisher`)is responsible for:

- Securely transmitting collected data to the AWS IoT SiteWise cloud
  service
- Managing data buffering and retries during connectivity
  issues

For more information on configuring the publisher for SiteWise Edge, see [Configure the AWS IoT SiteWise publisher
component](configure-publisher-component.md "configure-publisher-component.md"). And, for more
information on the publisher component, see [IoT SiteWise publisher](../../../greengrass/v2/developerguide/iotsitewise-publisher-component.md "../../../greengrass/v2/developerguide/iotsitewise-publisher-component.md") in the _AWS IoT Greengrass Version 2 Developer Guide_.

**IoT SiteWise processor**

The IoT SiteWise processor component
(`aws.iot.SiteWiseEdgeProcessor`) performs the following
tasks:

- Executing data transformations and calculations at the edge
- Implementing asset property definitions and computations
  locally
- Reducing data volume by aggregating or filtering data before
  transmission

For more information about the processor component, see [IoT SiteWise processor](../../../greengrass/v2/developerguide/iotsitewise-processor-component.md "../../../greengrass/v2/developerguide/iotsitewise-processor-component.md") in the
_AWS IoT Greengrass Version 2 Developer Guide_.

**IoT SiteWise OPC UA collector**

The IoT SiteWise OPC UA collector
(`aws.iot.SiteWiseEdgeCollectorOpcua`) component is designed
to:

- Connect to OPC UA servers in industrial environments
- Collect data from OPC UA data sources efficiently
- Transform OPC UA data into a format compatible with AWS IoT SiteWise

For more information about OPC UA collector component, see [IoT SiteWise OPC UA collector](../../../greengrass/v2/developerguide/iotsitewise-opcua-collector-component.md "../../../greengrass/v2/developerguide/iotsitewise-opcua-collector-component.md") in the
_AWS IoT Greengrass Version 2 Developer Guide_.

**IoT SiteWise OPC UA data source simulator**

The IoT SiteWise OPC UA data source simulator component
(`aws.iot.SiteWiseEdgeOpcuaDataSourceSimulator`) provides the
following functionality:

- Starts a local OPC UA server that generates sample data
- Simulates a data source that can be read by the AWS IoT SiteWise OPC UA
  collector component on an AWS IoT SiteWise gateway
- Enables exploration of AWS IoT SiteWise features using the generated sample
  data

This component is particularly useful for testing and development
purposes, allowing you to simulate industrial data sources without the need
for physical equipment.

For more information about the data source simulation component, see
[IoT SiteWise OPC UA data source simulator](../../../greengrass/v2/developerguide/iotsitewise-opcua-data-source-simulator-component.md "../../../greengrass/v2/developerguide/iotsitewise-opcua-data-source-simulator-component.md") in the
_AWS IoT Greengrass Version 2 Developer Guide_.

These AWS IoT Greengrass components work to enable SiteWise Edge functionality. The IoT SiteWise publisher
ensures data is reliably sent to the cloud, the IoT SiteWise processor handles local
computations and data optimization, and the IoT SiteWise OPC UA collector facilitates
integration with common industrial protocols.

###### Note

To use these components, you must have AWS IoT Greengrass V2 or later installed on your edge
devices. Proper configuration of each component is important for optimal performance
of SiteWise Edge.
