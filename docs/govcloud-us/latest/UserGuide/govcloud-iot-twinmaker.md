

# AWS IoT TwinMaker in AWS GovCloud (US)
<a name="govcloud-iot-twinmaker"></a>

 AWS IoT TwinMaker is used to build operational digital twins of physical and digital systems. AWS IoT TwinMaker creates digital visualizations using measurements and analysis from a variety of real-world sensors, cameras, and enterprise applications to help you keep track of your physical factory, building, or industrial plant.

 AWS IoT TwinMaker is available in 6 Classic regions (us-east-1, us-west-2, eu-west-1, ap-southeast-1, eu-central-1, ap-southeast-2). AWS IoT TwinMaker is available in one GovCloud region: us-gov-west-1.

## How AWS IoT TwinMaker differs
<a name="how_shared_iottmlong_differs"></a>

The following differences apply to AWS IoT TwinMaker:
+ AWS IoT TwinMaker only supports the self-managed Grafana configuration option. Amazon Managed Grafana (AMG) is not available in the AWS GovCloud (US-West).
+  AWS IoT TwinMaker doesn’t support Edge Video feature and Kinesis Video Streams (KVS) connector in AWS GovCloud (US-West).
+ The `com.amazon.iotsitewise.connector.edgevideo` component type is not available.
+ The `com.amazon.kvs.video` component type is not available.
+ The metadata bulk import and export operations are not available in the GovCloud PDT (us-gov-west-1) region.

## Documentation
<a name="govcloud-docs-48"></a>
+  [AWS IoT TwinMaker documentation](https://docs.aws.amazon.com/iot-twinmaker/landingpage.html) 

## Export-controlled content
<a name="govcloud-itar-content-87"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Workspace ID
+ ComponentType name
+ Component Name
+ Scene ID
+ Property name
+ Entity name