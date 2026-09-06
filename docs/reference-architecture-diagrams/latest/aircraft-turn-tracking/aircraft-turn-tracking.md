

# Aircraft Turn Tracking Passive Data Collection
<a name="aircraft-turn-tracking"></a>

Publication date: **March 10, 2021 ([Diagram history](#turn-tracking-history))**

Airlines and airports can realize cost savings by improving turn cycle time and reducing turn variation time at the gate. Reducing cycle time frees aircraft and gates for more efficient schedule usage.

Reducing cycle time by 4 to 6 minutes can potentially free 2 to 3 percent of a fleet of 500 aircraft. With aircraft costing USD $3M to USD $5M per year, this might result in cost savings of USD $30M to USD $75M.

This architecture uses cameras and edge inference to passively collect turn event data. It provides real-time tracking and analytics for turn optimization.

## Aircraft turn tracking diagram
<a name="turn-tracking-diagram"></a>

![Architecture for aircraft turn tracking using AWS IoT Greengrass and Amazon SageMaker AI on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/aircraft-turn-tracking/images/travel-ra-turn-tracking.png)


The following steps describe the architecture:

1. Gate cameras: three cameras outside the aircraft cover tarmac turn events. Jet bridge cameras: two cameras cover boarding. Gate counter camera: one camera covers crew and agent arrival.

1. For inference training, install cameras at one or two gates. Record the video stream for 4 to 6 weeks. Use [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) Ground Truth to label turn events.

1. [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), and AWS IoT Device Management manage cameras and run inference on the edge with [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) and SageMaker AI.

1. Use purpose-built databases and serverless architecture. [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/), [Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/), Lambda, [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), and AWS AppSync provide real-time microservices, notifications, and events for mobile apps and dashboards.

1. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), and [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) provide the data lake and analytics platform. Use SageMaker AI for AI/ML models for turn optimization. Use [Athena](https://docs.aws.amazon.com/athena/latest/ug/) for ad hoc analysis.

## Further reading
<a name="turn-tracking-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="turn-tracking-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#turn-tracking-history) | Reference architecture diagram first published. | March 10, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.