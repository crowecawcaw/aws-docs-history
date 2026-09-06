

# Consumer Review Sentiment Analysis for CPG
<a name="consumer-review-sentiment-cpg"></a>

Publication date: **May 13, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to gain insights from consumer reviews in near real time. With a serverless event-driven architecture, consumer packaged goods (CPG) companies can analyze sentiment, extract key phrases, and identify entities from reviews across multiple sources.

## Consumer Review Sentiment Analysis for CPG
<a name="diagram1"></a>

![Architecture diagram showing consumer review sentiment analysis for CPG with Amazon Comprehend and Amazon Translate.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/consumer-review-sentiment-cpg/images/consumer-review-sentiment-cpg.png)


The following steps describe the architecture:

1. Review data is ingested into AWS through the ingestion pipeline from multiple sources such as e-commerce, product websites, and social media webhooks.

1. An [Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) delivery stream loads the reviews into an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket.

1. [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html) securely ingests data from SaaS applications (like Salesforce, Marketo, Slack, and ServiceNow) into Amazon S3.

1. An Amazon S3 event invokes an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function to analyze the raw reviews. The function uses [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html) for language translation and [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) for sentiment analysis, key-phrase extraction, and entity extraction.

1. The [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) Data Catalog contains a logical database that organizes tables for the data in Amazon S3.

1. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) uses these table definitions to query the data stored in Amazon S3 and return the information to an [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) dashboard.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Detect sentiment from customer reviews using Amazon Comprehend (blog post)](https://aws.amazon.com/blogs/machine-learning/detect-sentiment-from-customer-reviews-using-amazon-comprehend/)
+ [Amazon Comprehend product page](https://aws.amazon.com/comprehend/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 13, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.