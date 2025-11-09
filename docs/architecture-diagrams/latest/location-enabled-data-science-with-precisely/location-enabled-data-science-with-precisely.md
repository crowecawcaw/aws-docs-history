# Location-enabled Data Science with Precisely on AWS

Publication date: **September 06, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

This reference architecture shows how customers can deploy [Precisely](https://www.precisely.com/solution/geocoding-and-data-enrichment-solutions "https://www.precisely.com/solution/geocoding-and-data-enrichment-solutions") geo addressing capabilities on Amazon SageMaker AI or Amazon EMR Studio to enhance experiments with location-aware data.

## Location-enabled Data Science with Precisely on AWS Diagram

![Reference architecture diagram showing how customers can deploy Precisely’s geo addressing capabilities on Amazon SageMaker AI or Amazon EMR Studio to enhance experiments with location-aware data.](images/location-enabled-data-science-with-precisely.png)

1. **Amazon CloudWatch** is scheduled to invoke
   **AWS Lambda** at a set intervals (such as
   monthly or quarterly).
2. **LambdaLambda** is invoked and starts to
   compute resources.
3. An **Amazon Elastic Compute Cloud** (Amazon EC2) compute instance is
   started.
4. Precisely datasets are updated at established intervals. Automatic Data
   Downloader monitors changes and automatically downloads data from Precisely
   Data Experience into **Amazon Simple Storage Service** (Amazon S3) in a
   variety of formats, including flat files (.txt, .csv), spatial data (.shp,
   .tab), and geocoding reference data (.spd).
5. Use **Amazon S3** to get the Geo Addressing SDK
   from Precisely Fulfillment.
6. Reference data is downloaded to your **Amazon S3** bucket.
7. Reference data and SDKs are ready to be used for geo addressing on
   **Amazon SageMaker AI** or **Amazon EMR** Studio.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/location-enabled-data-science-with-precisely.md "samples/location-enabled-data-science-with-precisely.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [Precisely - Geo addressing, geocoding, and data enrichment solutions](https://www.precisely.com/solution/geocoding-and-data-enrichment-solutions/ "https://www.precisely.com/solution/geocoding-and-data-enrichment-solutions/")

## Contributors

Contributors to this reference architecture diagram include:

- Ayan Ray, Senior Partner Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- |
| Initial publication | Reference architecture diagram first published. | September 6, 2023 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
