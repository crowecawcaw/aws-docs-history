

# Data ingestion
<a name="mfg-data-ingestion"></a>

The data ingestion diagram shows how to bring data from factory floors and enterprise applications into AWS.

![Data ingestion diagram showing how to bring factory and enterprise data into AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-on-aws/images/manufacturing-on-aws-ra-2.png)


1. Connect industrial devices with [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) on an Edge gateway.

1. Stream industrial data with [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/) into the data lake.

1. With [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), model assets and visualize data with AWS IoT SiteWise Monitor.

1. Sync unstructured data with AWS Storage Gateway from on-premises file shares.

1. Use [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/) for file transfers into the data lake.

1. Use [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for enterprise application interfaces.

1. Use AWS Snowball Edge for large data set migration from on-premises systems.

1. Use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) to synchronize databases into [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) (Amazon RDS).