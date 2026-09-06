

# Connected Home Telemetry on AWS
<a name="connected-home-telemetry"></a>

Publication date: **March 22, 2021 ([Diagram history](#diagram-history))**

This reference architecture diagram shows how to measure and collect data from smart home devices by using AWS.

## Connected Home Telemetry on AWS
<a name="diagram1"></a>

![Reference architecture diagram showing how to measure and collect telemetry data from smart home devices by using AWS IoT Core, AWS IoT Analytics, AWS IoT Events, DynamoDB, and Quick.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/connected-home-telemetry/images/connected-home-telemetry.png)


1. The devices connect to [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) directly by using MQTT from FreeRTOS or through AWS IoT Greengrass.

1. AWS IoT Core topic rules route data to downstream services:
   + **2a.** A topic rule picks up meaningful data and saves it in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).
   + **2b.** Another topic rule triggers AWS IoT Events for certain data, like temperature.
   + **2c.** AWS IoT Analytics can ingest data directly from AWS IoT Greengrass.

1. Client applications can retrieve and visualize data:
   + **3a.** Client applications can make an API call to retrieve data through Amazon API Gateway.
   + **3b.** AWS IoT Events can trigger [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) actions in case certain changes occur in the data (for example, temperature exceeds 25 degrees).
   + **3c.** You can import data from AWS IoT Analytics into [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) for visualization and further insights.

1. Notifications and data retrieval:
   + **4a.** [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) invokes an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function with logic to retrieve data requested by the client applications from DynamoDB.

1. Visualization and alerts:
   + **5a.** Client applications can visualize the data in Amazon Quick Sight.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS IoT product page](https://aws.amazon.com/iot/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 22, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.