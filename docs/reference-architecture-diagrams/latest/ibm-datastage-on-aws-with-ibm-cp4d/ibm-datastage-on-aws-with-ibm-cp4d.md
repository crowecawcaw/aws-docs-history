

# IBM DataStage on AWS with IBM CP4D
<a name="ibm-datastage-on-aws-with-ibm-cp4d"></a>

Publication date: **May 3, 2023 ([Diagram history](#diagram-history))**

This architecture shows how to build a modern, cloud-native, secure data integration solution to collect, transform, enrich, and deliver data at any scale and complexity. 

## IBM DataStage on AWS with IBM CP4D Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how to build a modern, cloud-native, secure data integration solution to collect, transform, enrich, and deliver data at any scale and complexity.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ibm-datastage-on-aws-with-ibm-cp4d/images/ibm-datastage-on-aws-with-ibm-cp4d.png)


1. Data is collected from multiple data sources across the enterprise data bases and **AWS Cloud** data stores, such as **Amazon Simple Storage Service** (Amazon S3) and **Amazon DocumentDB (with MongoDB compatibility)**. 

1. [IBM DataStage](https://www.ibm.com/products/datastage) for IBM Cloud Pak for Data (IBM CP4D), an integration tool that helps jobs move and transfer data from multiple data sources, is built on a **Red Hat OpenShift Service on AWS** (ROSA) platform. 

1. You can use [IBM DB2 Warehouse](https://www.ibm.com/products/db2/warehouse) to store and analyze large amounts of data. Data from multiple data sources uses in-memory capability to process and provide sales and marketing analytics. 

1. Use IBM DB2 Warehouse data mart to deliver high-performance complex analytics and the processed data with facts and dimensions for reporting and analytics. 

1. IBM CP4D runs as a container workload running on OpenShift. **ROSA** is a fully managed OpenShift implementation on **AWS**. Red Hat site reliability engineering (SRE) teams manage the OpenShift clusters, allowing customers to focus on other critical business aspects. 

1. Marketing and finance users access the data from data marts and build visualization and dashboards using tools like IBM Cognos Analytics and **Amazon Quick Sight**. 

1. Users can create self-service data access and business and compliance reports. Data from data marts helps users self-serve analytics with scale and performance. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [IBM DataStage](https://www.ibm.com/products/datastage) 
+  [IBM DB2 Warehouse](https://www.ibm.com/products/db2/warehouse) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 3, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.