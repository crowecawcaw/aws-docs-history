

# Dynamic Media Content for Games
<a name="dynamic-media-content-games"></a>

Publication date: **October 8, 2020 ([Diagram history](#dynamic-media-history))**

Game developers often build custom solutions to engage with players through daily messages and custom media content, including Message of the Day (MOTD). This architecture provides a serverless approach for serving customized content based on request parameters and edge computing.

## Dynamic Media Content for Games diagram
<a name="dynamic-media-diagram"></a>

![Reference architecture diagram showing how to build a serverless solution for customized in-game media content by using CloudFront, Lambda@Edge, DynamoDB Global Tables, and Amazon S3.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/dynamic-media-content-games/images/dynamic-media-content-games.png)


The following steps describe the architecture:

1. Game clients send a request with parameters to [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) to download dynamic content. Request parameters represent attributes about the player, but use low-cardinality values to maintain high cache rates and reduce cost.

1. CloudFront invokes an AWS [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html) function closest to the user. The function dynamically modifies the content that should be retrieved from origin based on request parameters.

1. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) Global Tables provides a multi-Region rules engine for custom routing. The Lambda function queries the table closest to the user to determine the content to serve.

1. CloudFront uses the response from Lambda to fetch the relevant content from [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (origin). CloudFront returns the content to the client and caches the response in edge locations to reduce cost and improve performance for future requests.

## Further reading
<a name="dynamic-media-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="dynamic-media-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#dynamic-media-history) | Reference architecture diagram first published. | October 8, 2020 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.