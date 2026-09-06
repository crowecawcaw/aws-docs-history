

# Intelligent Supply Chain - Retail
<a name="intelligent-supply-chain-retail"></a>

Publication date: **February 14, 2022 ([Diagram history](#diagram-history))**

This architecture shows a track and trace use case for a generic retailer.

**Note**  
This is a supply chain reference architecture for a generic retailer. Specific item types are not captured in this reference architecture.

## Intelligent Supply Chain - Retail Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how AWS services are used to depict a track and trace use case for a generic retailer.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/intelligent-supply-chain-retail/images/intelligent-supply-chain-retail.png)


1. Suppliers receive the purchase order (PO) and demand signals, and raise Order Received, Order Shipped, Autonomous System Numbers (ASN), and Invoice events. 

1. The logistics provider receives driver alerts, and sends Order Loaded, Location, and Temp sensor readings. 

1. Consumers receive estimated time of arrival (ETA) notifications and origin provenance, and in turn send the Order Delivered notice. 

1. Stores and warehouses receive ASN notifications and Order Received notifications, and raise Order Received, Order Shipped, Put Away, Pick-Pack, and Dispatch notifications, and invoice events. 

1. Data ingestion and processing – Events from the various sources (systems and devices) are ingested and processed here. Services such as Amazon Textract help with extracting information. 

1. The information from the various events is then fed into the Amazon Simple Storage Service (Amazon S3) data lake. The information can also be retrieved by the application from Amazon S3. 

1. Business Intelligence (BI) and analytics - Management Information System (MIS) reports are produced on this data using various AWS services. 

1. Various Artificial Intelligence/Machine Learning (AI/ML) services such as Amazon Forecast are run on the data, or the retailer can use Amazon SageMaker AI to build their own AI/ML services. 

1. Various notifications (emails, texts, and so on) are sent out using Amazon Pinpoint services. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 14, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.