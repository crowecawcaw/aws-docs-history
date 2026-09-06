

# Server-Side Rendering Micro-Frontends in AWS
<a name="server-side-rendering-micro-frontends"></a>

Publication date: **September 9, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to implement server-side rendering micro-frontends in AWS using a serverless approach. Every serverless micro-frontend returns an HTML fragment (HTML-on-the-wire), and a UI composer stitches together these independent parts to create a seamless experience for users.

## Server-Side Rendering Micro-Frontends in AWS
<a name="diagram1"></a>

![Architecture diagram showing server-side rendering micro-frontends using Amazon CloudFront, Amazon Simple Storage Service, AWS Fargate, AWS Lambda, AWS Step Functions, and Amazon DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/server-side-rendering-micro-frontends/images/server-side-rendering-micro-frontends.png)


The following steps describe the architecture:

1. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) serves as the entry point with two origins: an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket and a public Application Load Balancer.

1. The Amazon S3 bucket contains all static files for the browser such as common micro-frontend dependencies, images, and CSS files. It also contains the templates the UI composer uses to place every micro-frontend on an HTML page.

1. The UI composer runs on an [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) cluster and stitches together different micro-frontends, streaming the response to improve performance. Use [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) to cache micro-frontend output or entire pages for additional performance gains.

1. Use [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) Parameter Store to collect all micro-service endpoints. They can be HTTP endpoints or Amazon Resource Names (ARNs), decoupling team-level dependencies.

1. A serverless micro-frontend uses [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) to store data and render an HTML fragment ready for embedding in the UI composer template.

1. For third-party micro-frontends, use [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) to validate tokens or API keys, ensuring only your application can access that endpoint.

1. Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) Express as a low-code solution for generating micro-frontends. Step Functions integrates with over 200 services to reduce computation, retrieves data from DynamoDB natively, and delegates rendering to a Lambda function.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | September 9, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.