# Ingest data to AWS IoT SiteWise

AWS IoT SiteWise is designed to efficiently collect and correlate industrial data with corresponding
assets, representing various aspects of industrial operations. This documentation focuses on the
practical aspects of ingesting data into AWS IoT SiteWise, offering multiple methods tailored to diverse
industrial use cases. For instructions to build your virtual industrial operation, see [Model industrial assets](industrial-asset-models.md "industrial-asset-models.md").

You can send industrial data to AWS IoT SiteWise using any of the following options:

- **AWS IoT SiteWise Edge**–Use [SiteWise Edge gateway](gateways.md "gateways.md") as an intermediary between AWS IoT SiteWise and your data servers. AWS IoT SiteWise
  provides AWS IoT Greengrass components that you can deploy on any platform that can run AWS IoT Greengrass to set up a
  SiteWise Edge gateway. This option supports linking with [OPC UA](https://en.wikipedia.org/wiki/OPC_Unified_Architecture "https://en.wikipedia.org/wiki/OPC_Unified_Architecture") server
  protocol.
- **AWS IoT SiteWise API**–Use the [AWS IoT SiteWise API](ingest-api.md "ingest-api.md") to upload data from any other
  source. Use our streaming [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") API for ingestion within seconds, or the batch-oriented [CreateBulkImportJob](../APIReference/API_CreateBulkImportJob.md "../APIReference/API_CreateBulkImportJob.md") API to
  facilitate cost-effective ingestion in larger batches.
- **AWS IoT Core rules**–Use [AWS IoT Core rules](iot-rules.md "iot-rules.md") to upload data from MQTT messages published by an AWS IoT thing or
  another AWS service.
- **AWS IoT Events actions**–Use [AWS IoT Events actions](iot-events.md "iot-events.md") triggered by specific events in AWS IoT Events. This method is suitable
  for scenarios where data upload is tied to event occurrences.
- **AWS IoT Greengrass stream manager**–Use [AWS IoT Greengrass stream manager](greengrass-stream-manager.md "greengrass-stream-manager.md") to upload data
  from local data sources using an edge device. This option caters to situations where data originates from on-premises or edge locations.
  These methods offer a range of solutions for managing data from different sources. Delve into the details of each option to gain a comprehensive understanding of the data ingestion capabilities AWS IoT SiteWise provides.
