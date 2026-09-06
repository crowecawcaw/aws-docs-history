

# Consumer Review Sentiment Analysis for CPG
<a name="consumer-review-sentiment-analysis-cpg"></a>

Publication date: **May 13, 2021 ([Diagram history](#sentiment-history))**

With this architecture, you can gain insights from consumer reviews in near real time. Consumer packaged goods (CPG) companies use review data to understand consumption-related decisions and proactively address issues. You use [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/) for natural language processing (NLP) sentiment analysis, [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/) for translation, and a serverless event-driven architecture.

For more information about this approach, see [Detect sentiment from customer reviews using Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/detect-sentiment-from-customer-reviews-using-amazon-comprehend/) on the AWS Machine Learning Blog.

## Sentiment analysis diagram
<a name="sentiment-diagram"></a>

![Architecture diagram showing consumer review data flowing from ecommerce sites through Amazon Data Firehose to Amazon Simple Storage Service, processed by AWS Lambda with Amazon Comprehend for sentiment analysis, and visualized in Amazon Quick Sight.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/consumer-review-sentiment-analysis-cpg/images/consumer-review-sentiment-analysis-cpg.png)


The following steps describe the architecture:

1. Review data flows into AWS through the ingestion pipeline from multiple sources such as ecommerce sites, product websites, and social media webhooks.

1. An Amazon Data Firehose delivery stream loads the reviews into an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket.

1. [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/) ingests data from software-as-a-service (SaaS) applications such as Salesforce, Marketo, Slack, and ServiceNow into Amazon S3.

1. An Amazon S3 event invokes an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function to analyze raw reviews. Use Amazon Translate to translate reviews into a base language if necessary. Use Amazon Comprehend for NLP to perform sentiment analysis, key-phrase extraction, and entity extraction.

1. The [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) Data Catalog contains a logical database that organizes tables for the data in Amazon S3.

1. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) uses these table definitions to query data in Amazon S3. Results display in an [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) dashboard.

## Further reading
<a name="sentiment-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sentiment-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#sentiment-history) | Reference architecture diagram first published. | May 13, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.