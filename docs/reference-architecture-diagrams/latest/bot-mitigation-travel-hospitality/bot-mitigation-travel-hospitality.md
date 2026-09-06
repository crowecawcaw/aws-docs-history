

# Bot Mitigation for Travel and Hospitality
<a name="bot-mitigation-travel-hospitality"></a>

Publication date: **October 12, 2020 ([Diagram history](#botmit-history))**

With this architecture, you can build a fully serverless content delivery network (CDN) platform for travel and hospitality websites. Detect and mitigate bots in real time to reduce price scraping and automated purchases. The solution uses [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/), [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/)@Edge to profile and filter requests.

## Bot mitigation diagram
<a name="botmit-diagram"></a>

![How to detect and mitigate bots by using Amazon CloudFront, AWS WAF, and AWS Lambda.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/bot-mitigation-travel-hospitality/images/bot-mitigation-travel-hospitality.png)


The following steps describe the architecture:

1. Traffic hits the endpoints from sources such as a website, mobile app, or bot/scraper.

1. Use AWS WAF to create and update rules that block common attack patterns. Filter traffic patterns such as known bad IP lists, HTTP headers, or URI strings. Update rules programmatically.

1. Use Lambda@Edge to intercept HTTP requests to the CloudFront distribution. Write custom logic to make external HTTP requests and API calls to AWS services. Then process or reject the request.

1. 4A. Create a service that uses [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) to store fingerprint information about requesters.

   4B. Alternatively, integrate directly with an AWS Partner Network (APN) partner offering. Write custom code to validate IPs, user agents, and headers, or offload this work to a partner solution.

1. After validation, the HTTP request proceeds to CloudFront.

1. Stream CloudFront logs in real time to [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) for real-time traffic analytics.

1. CloudFront sends the request to the specified origin, such as an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) website or HTTP endpoint.

## Further reading
<a name="botmit-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="botmit-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#botmit-history) | Reference architecture diagram first published. | October 12, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.