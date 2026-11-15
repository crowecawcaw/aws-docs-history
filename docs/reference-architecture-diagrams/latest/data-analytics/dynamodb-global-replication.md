

# DynamoDB global replication with data localization
<a name="dynamodb-global-replication"></a>

Publication date: **March 10, 2023 ([Diagram history](diagram-history.md))**

Use this architecture for global data-item replication in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) with scalability and performance while working to comply with data localization mandates for data to be stored in a specific Region only.

## DynamoDB global replication with data localization diagram
<a name="dynamodb-global-replication-diagram1"></a>

![Architecture diagram showing DynamoDB global replication with data localization using Lambda, EventBridge, and AWS AppConfig.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/dynamodb-global-replication.png)


The following steps describe the architecture:

1. On the main AWS Region, set services to add items with a localization-authority field into a regional DynamoDB table.

1. Enable DynamoDB Streams to capture events about mutated items and handle the events with an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) event-listener function.

1. Map localization authorities to Regions with [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/). Read the map on the function, then discard changes on items localized in the current Region and items already moved using event filtering.

1. Raise an event containing the mutated item details and the localization Region to an event bus in [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/).

1. Set up EventBridge rules for cross-Region event routing. Send global items to all Regions. Send remotely localized items only to the localization Region defined on the payload.

1. On destination Regions, handle received item details with a Lambda replicator function.

1. Replicate received items in regional DynamoDB tables, then raise an event to the Region of origin indicating that the replication finished.

1. On the Region of origin, handle the finished event with an anonymizer Lambda function.

1. Set the function to anonymize sensitive information from localized moved items, stamping them with the localized Region that they moved into. Ignore global items.

1. When services update items, only update global items and localized items that belong to the same Region where they are stored.

1. If a localized item to update has already moved to a different Region, make a cross-Region call to the DynamoDB table in the localized Region to update the record.

## Further reading
<a name="dynamodb-global-replication-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)