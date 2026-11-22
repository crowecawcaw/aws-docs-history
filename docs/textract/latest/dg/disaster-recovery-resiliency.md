

# Resilience in Amazon Textract

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

Amazon Textract Insights uses cross-Region inference, so any request can be processed in another AWS Region in the same geography. This keeps throughput up when demand is high, but an individual job can see variable latency. For the AWS Regions involved, see [Cross-Region inference](insights-cross-region.md).

To make client retries safe, pass a `ClientRequestToken` to `StartDocumentInsights`. A retry with the same token and the same parameters returns the original job instead of starting a duplicate. See [Running and monitoring Document Insights jobs](insights-running-monitoring.md).

**Note**  
The Amazon Textract Core APIs process your data only in the AWS Region where you call them. Amazon Textract Insights can run inference in another AWS Region in the same geography, as described in [Cross-Region inference for Amazon Textract Insights](textract-cross-region-inference.md).