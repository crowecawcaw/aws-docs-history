# Use AWS IoT Greengrass stream manager in AWS IoT SiteWise

AWS IoT Greengrass stream manager is an integration feature that facilitates the
transfer of data streams from local sources to the AWS Cloud.
It acts as an intermediary layer that manages data flows, enabling
devices operating at the edge to gather and store data before it is sent
to AWS IoT SiteWise, for further analysis and processing.

Add a data destination by configuring a local source on the
AWS IoT SiteWise console. You can also use stream manager in your custom AWS IoT Greengrass solution to ingest data to
AWS IoT SiteWise.

###### Note

To ingest data from OPC UA sources, configure an AWS IoT SiteWise Edge gateway that runs on
AWS IoT Greengrass. For more information, see [Use AWS IoT SiteWise Edge gateways](gateways.md "gateways.md").

For more information about how to **configure a destination** for local source data, see [Understand AWS IoT SiteWise Edge destinations](gw-destinations.md#source-destination "gw-destinations.md#source-destination").

For more information about how to **ingest data using stream manager** in a custom AWS IoT Greengrass
solution, see the following topics in the _AWS IoT Greengrass Version 2 Developer Guide_:

- [What is AWS IoT Greengrass?](../../../greengrass/v2/developerguide.md "../../../greengrass/v2/developerguide.md")
- [Manage data streams on the AWS IoT Greengrass
  core](../../../greengrass/v2/developerguide/manage-data-streams.md "../../../greengrass/v2/developerguide/manage-data-streams.md")
- [Exporting data to AWS IoT SiteWise asset properties](../../../greengrass/v2/developerguide/stream-export-configurations.md#export-to-iot-sitewise "../../../greengrass/v2/developerguide/stream-export-configurations.md#export-to-iot-sitewise")
