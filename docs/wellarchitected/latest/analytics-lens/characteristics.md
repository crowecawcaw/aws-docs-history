# Characteristics

The common issue that can hold you back from maximizing the value of your data is the
variety of data silos within your organization. Silos can prevent you from extracting maximum
value from all your data with the greatest flexibility. Data warehouses can help with this to
a point, but often only a small portion of raw data is brought into the data warehouse.
Organizations often end up with multiple data warehouses, so you can still have these silos.
There are a number of modern approaches to enterprise-wide analytics that can help solve this
– such as data lakes, modern data architectures, and data mesh. If you are not already
exploring these modern approaches, this is a good opportunity to learn more about these
architectures in the following sections.

Another common issue is whether you can benefit from increasing the velocity at which you
ingest and process your data. Many organizations still have a predominantly batch-oriented
strategy to processing the data, where a majority of your data is processed on a daily
schedule. You can ask yourself questions such as ‘How can we benefit if we have access to more
up-to-date data?” AWS can help you explore options for ingesting streaming data, and for
processing data in micro-batches or employ stream processing.

If you have previously explored streaming options in the past, you might have been
concerned about the complexity of some of these solutions, but there are many AWS-managed
solutions for streaming that significantly reduces much of this complexity.

In general, data discovery consists of five steps:

## 1.  Define the business value

This is the first step in data discovery where you define the business value or
opportunity by conducting interactive sessions. Here are a few example questions to define
the business opportunity.

- What insights are you getting from the data?
- How would getting insight into data provide value to the business?
- Are you looking to create a new revenue stream from your data?
- What are challenges with your current approach and tool?
- What are you not providing to your customers that you would like to provide?
- Who is the executive level stakeholder for this effort?
- Example-specific use case questions:
  - How does data define your customer acquisition strategy?
  - Would your business benefit from exploring modern approaches to managing fraud
    detection, predictive maintenance, customer 360, IoT, clickstream, operational
    analytics, root-cause analysis to reduce mean time to detection and mean time to
    recovery?
  - How are you continually innovating on behalf of your customers and improving
    their user experience?

## 2. Identify your user personas

In this step, you focus on your data consumers, such as business analysts, data
engineers, data analysts, and data scientists. Once you have developed your user personas,
enable them for purpose-built analytics and machine learning. 

Here are few example questions to identify your data consumers.

- Who are the end users?
- What insights are you currently getting from your data?
- What insights are on your roadmap?
- Do you have a multi-tenant data model?
- What are the different consumption models?
  - Which tool or interface do your data consumers use?
  - How real time does the data need to be for this use case (for example, near
    real time, every 15 minutes, hourly, daily)?
  - What is the total number of consumers for this consumption model?
  - What is the peak concurrency?

## 3. Identify your data sources

In this step, you focus on your data sources and tools to bring that data into the data
platform. This allows you to perform comprehensive analytics and machine learning from a
wide variety of data from various data sources.

**Data types and sources**

Table 3: Typical data sources in an organization

| **Data type**        | **Example data sources**                                                                                                                                            |     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Structured data      | ERP applications, CRM applications, ERP applications, CMS applications, SaaS applications, SAP applications, line of business (LOB) applications, and SQL databases |     |
| Semi-structured data | Web applications, NoSQL databases, EDI (electronic data interchange), CSV, XML, and JSON documents                                                                  |     |
| Unstructured data    | Video files, audio files, images, IoT data, sensors data, and invoices                                                                                              |     |
| Batch                | Internal applications generate structured data at regularly defined schedules                                                                                       |     |
| Streaming data       | Sensors, social media, video streams, IoT devices, mobile devices that generate semi-structured and unstructured data as continuous streams                         |     | Here are a few example questions to identify your data consumers. <br>• How many data sources do you have to support? + Where and how is the data generated? + What are the different types of your data? (for example, structured, semi-structured, unstructured, batch, streaming) + What are the different formats of your data? (for example, JSON, CSV, FHIR) + Is your data originating from on premises, a third-party vendor, or the cloud? + Is the data source streaming, batch, or micro-batch? + What is the rate and volume of ingestion? + What is the ingestion interface (for example, API, SFTP, Amazon S3, AWS Marketplace) <br>• How does your team on-board new data sources? ## 4. Define your data storage, catalog, and data access needs In this step, you focus on your data storage, data cataloging, security, compliance, and data access requirements. Here are few example questions to identify your data storage and data access requirements. <br>• What data stores do you have? <br>• What is the purpose of each data store? <br>• Why that storage method? (for example, files, SQL, NoSQL, data warehouse) <br>• How do you currently organize your data? (for example, data tiering, partition) <br>• How much data are you storing now, and how much do you expect to be storing in the future, for example, 18 months from now? <br>• How do you manage data governance? <br>• What data regulatory and governance compliance do you face? <br>• What is your disaster recovery (DR) strategy? ## 5. Define your data processing requirements In this step, you focus on your data processing requirements. Here are few example questions to identify your data processing requirements. <br>• Do you have to transform or enrich the data before you consume it? <br>• What tools do you use for transforming your data? <br>• Do you have a visual editor for the transformation code? <br>• What is your frequency of data transformation? (for example, real time, micro-batching, overnight batch) <br>• Are there any constraints with your current tool of choice? |
