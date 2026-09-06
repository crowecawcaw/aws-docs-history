

# DynamoDB Global Replication with Data Localization
<a name="dynamodb-global-replication"></a>

Publication date: **March 10, 2023 ([Diagram history](#diagram-history))**

Use this architecture for global data-item replication in [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) with scalability and performance while working to comply with data localization mandates for data to be stored in a specific Region only.

## DynamoDB Global Replication with Data Localization
<a name="diagram1"></a>

![Architecture diagram showing DynamoDB global replication with data localization using Lambda, EventBridge, and AWS AppConfig.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/dynamodb-global-replication/images/dynamodb-global-replication.png)


The following steps describe the architecture:

1. On the main AWS Region, set services to add items with a localization-authority field into a regional DynamoDB table.

1. Enable [DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) to capture events about mutated items and handle the events with an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) event-listener function.

1. Map localization authorities to Regions with [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html). Read the map on the function, then discard changes on items localized in the current Region and items already moved using event filtering.

1. Raise an event containing the mutated item details and the localization Region to an event bus in [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

1. Set up EventBridge rules for cross-Region event routing. Send global items to all Regions. Send remotely localized items only to the localization Region defined on the payload.

1. On destination Regions, handle received item details with a Lambda replicator function.

1. Replicate received items in regional DynamoDB tables, then raise an event to the Region of origin indicating that the replication finished.

1. On the Region of origin, handle the finished event with an anonymizer Lambda function.

1. Set the function to anonymize sensitive information from localized moved items, stamping them with the localized Region that they moved into. Ignore global items.

1. When services update items, only update global items and localized items that belong to the same Region where they are stored.

1. If a localized item to update has already moved to a different Region, make a cross-Region call to the DynamoDB table in the localized Region to update the record.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 10, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.