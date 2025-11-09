# AWS IoT TwinMaker in AWS GovCloud (US)

AWS IoT TwinMaker is used to build operational digital twins of physical and digital systems. AWS IoT TwinMaker creates digital visualizations using measurements and analysis from a variety of real-world sensors, cameras, and enterprise applications to help you keep track of your physical factory, building, or industrial plant.

AWS IoT TwinMaker is available in 6 Classic regions (us-east-1, us-west-2, eu-west-1, ap-southeast-1, eu-central-1, ap-southeast-2). AWS IoT TwinMaker is available in one GovCloud region: us-gov-west-1.

## How AWS IoT TwinMaker differs for AWS GovCloud (US)

The following differences exist between AWS IoT TwinMaker in AWS GovCloud (US) and standard regions:

- AWS IoT TwinMaker only supports the self-managed Grafana configuration option. Amazon Managed Grafana (AMG) is not available in the AWS GovCloud (US-West).
- AWS IoT TwinMaker doesn’t support Edge Video feature and Kinesis Video Streams (KVS) connector in AWS GovCloud (US-West).
- The `com.amazon.iotsitewise.connector.edgevideo` component type is not supported.
- The `com.amazon.kvs.video` component type is not supported.
- The metadata bulk import and export operations are not available in the GovCloud PDT (us-gov-west-1) region.

## Documentation for AWS IoT TwinMaker

[AWS IoT TwinMaker documentation](../../../iot-twinmaker/landingpage.md "../../../iot-twinmaker/landingpage.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Workspace ID
- ComponentType name
- Component Name
- Scene ID
- Property name
- Entity name
