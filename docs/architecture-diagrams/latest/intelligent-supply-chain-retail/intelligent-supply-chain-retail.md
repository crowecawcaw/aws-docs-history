# Intelligent Supply Chain - Retail

Publication date: **February 14, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture shows a track and trace use case for a generic retailer.

###### Note

This is a supply chain reference architecture for a generic retailer. Specific item types are not captured in this reference architecture.

## Intelligent Supply Chain - Retail Diagram

![Reference architecture diagram showing how AWS services are used to depict a track and trace use case for a generic retailer.](images/intelligent-supply-chain-retail.png)

1. Suppliers receive the purchase order (PO) and demand signals, and raise Order Received, Order Shipped, Autonomous System Numbers (ASN), and Invoice events.
2. The logistics provider receives driver alerts, and sends Order Loaded, Location, and Temp sensor readings.
3. Consumers receive estimated time of arrival (ETA) notifications and origin provenance, and in turn send the Order Delivered notice.
4. Stores and warehouses receive ASN notifications and Order Received notifications, and raise Order Received, Order Shipped, Put Away, Pick-Pack, and Dispatch notifications, and invoice events.
5. Data ingestion and processing – Events from the various sources (systems and devices) are ingested and processed here. Services such as Amazon Textract help with extracting information.
6. The information from the various events is then fed into the Amazon Simple Storage Service (Amazon S3) data lake. The information can also be retrieved by the application from Amazon S3.
7. Business Intelligence (BI) and analytics - Management Information System (MIS) reports are produced on this data using various AWS services.
8. Various Artificial Intelligence/Machine Learning (AI/ML) services such as Amazon Forecast are run on the data, or the retailer can use Amazon SageMaker AI to build their own AI/ML services.
9. Various notifications (emails, texts, and so on) are sent out using Amazon Pinpoint services.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/intelligent-supply-chain-retail.md "samples/intelligent-supply-chain-retail.md") which contains an editable PowerPoint.

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

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | February 14, 2022 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
