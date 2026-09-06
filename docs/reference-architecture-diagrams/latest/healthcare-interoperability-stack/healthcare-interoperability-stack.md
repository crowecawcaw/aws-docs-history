

# Healthcare Interoperability Stack on AWS
<a name="healthcare-interoperability-stack"></a>

Publication date: **January 31, 2023 ([Diagram history](#interop-history))**

With this architecture, you can build a modular interoperability platform to ingest, parse, and store healthcare data of any shape, size, and format. The solution uses connectors with syntactic and semantic parsers to convert and standardize both standard and non-standard data into Health Level Seven Fast Healthcare Interoperability Resources (HL7 FHIR) format.

## Healthcare interoperability stack diagram
<a name="interop-diagram"></a>

![Reference architecture diagram showing how to build a healthcare interoperability platform by using EventBridge, Step Functions, AWS HealthLake, Amazon Textract, and Amazon SQS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/healthcare-interoperability-stack/images/healthcare-interoperability-stack.png)


The following steps describe the data flow and processing pipeline for this architecture:

1. Establish on-premises connectivity for data ingestion. Use a private channel such as AWS Site-to-Site VPN, AWS Direct Connect, or HTTPS connectivity.

1. Use different connectors depending on the incoming message type. For public-facing [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) instances, configure [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) as a web application firewall. Use [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/), [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/), or Elastic Load Balancing depending on your data source.

1. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) to handle data processing pipeline orchestration. Store intermediate data in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Use [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/) to extract text from files where required, such as PDFs.

1. Use a data classifier to determine the incoming message type and route information to the appropriate parser by using event rules.

1. Use a set of configurable templates in the syntactic parser to transform incoming data formats into HL7 FHIR if required.

1. Use the semantic parser to standardize data values into common ontologies.

1. Use the distribution module to fan out converted messages to appropriate destinations by using [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/) and [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

1. Bring your own identity solutions to normalize resources such as patients and providers.

1. Use [Amazon HealthLake](https://docs.aws.amazon.com/healthlake/latest/devguide/) as a durable storage destination for messages transformed into HL7 FHIR. Use Amazon S3 to store other resources.

1. Benefit from standardized data to gain insights and to improve care.

## Further reading
<a name="interop-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="interop-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#interop-history) | Reference architecture diagram first published. | January 31, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.