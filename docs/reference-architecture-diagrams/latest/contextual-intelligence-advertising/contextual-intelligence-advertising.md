# Guidance for Contextual Intelligence for Advertising

Publication date: **April 6, 2022 ([Diagram history](#cia-history "#cia-history"))**

With this architecture, you can build a contextual advertising solution that uses machine
learning to reach target audiences without third-party cookies. Contextual advertising reaches
an audience based on the content that users consume. The solution uses an event-driven,
serverless architecture that is scalable and cost-optimized.

This architecture helps demand-side platforms (DSPs), advertisement
publishers, and supply-side platforms (SSPs) build a contextual intelligence
solution. You use AWS AI and machine learning services to extract relevant metadata and map
it to your own or an industry-standard taxonomy.

## Architecture diagram

![Content flowing through AWS serverless services for analysis, taxonomy mapping, and programmatic advertising bid enrichment.](images/guidance-for-contextual-intelligence-for-advertising-ra.png)

The following steps describe the architecture:

1. DSPs, SSPs, or ad publishers invoke an API on [Amazon API Gateway](../../../apigateway/latest/developerguide.md "../../../apigateway/latest/developerguide.md") to
   trigger content discovery. The API fetches text, images, audio, and video from the
   provided content.
2. The [serverless
   crawler](https://aws.amazon.com/blogs/architecture/scaling-up-a-serverless-web-crawler-and-search-engine/ "https://aws.amazon.com/blogs/architecture/scaling-up-a-serverless-web-crawler-and-search-engine/") is built on [AWS Step Functions](../../../step-functions/latest/dg.md "../../../step-functions/latest/dg.md") to orchestrate exploration and
   download of content. [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide.md "../../../amazondynamodb/latest/developerguide.md") stores ephemeral
   discovery data.
3. You can use a crawler or a content management system API to extract media types and
   store them in an [Amazon S3](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") bucket.
4. Amazon S3 stores content (text, image, video), with available metadata in Amazon DynamoDB
   for analysis.
5. A content discovery completion event starts controller orchestration built on
   AWS Step Functions, [AWS Lambda](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md"), and [Amazon SNS](../../../sns/latest/dg.md "../../../sns/latest/dg.md").
6. Amazon SNS events invoke AWS Lambda functions to start content analysis by using Amazon Comprehend,
   Amazon Rekognition, and Amazon Transcribe.
7. Amazon DynamoDB stores topics, sentiment, and object labels from the content analysis
   workflow.
8. The Contextual Intelligence Taxonomy Mapper (CITM) uses the
   [Bidirectional Encoder
   Representations from Transformers (BERT)](https://arxiv.org/pdf/1810.04805.pdf "https://arxiv.org/pdf/1810.04805.pdf") model deployed on
   [Amazon SageMaker AI](../../../sagemaker/latest/dg.md "../../../sagemaker/latest/dg.md").
   CITM maps metadata in Amazon DynamoDB to an industry-standard taxonomy such
   as the [IAB
   Content Taxonomy](https://iabtechlab.com/standards/content-taxonomy/ "https://iabtechlab.com/standards/content-taxonomy/").
9. A AWS Lambda function gets the mapping and stores it in Amazon DynamoDB within the
   category service.
10. Bidding servers invoke an API built on Amazon API Gateway to fetch categories from Amazon DynamoDB.
    This informs programmatic advertising bids with low latency.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date          |
| ------------------- | ----------------------------------------------- | ------------- |
| Initial publication | Reference architecture diagram first published. | April 6, 2022 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you
are using.
