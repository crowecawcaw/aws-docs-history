# Data lake

You can use AWS Supply Chain to ingest your data stored in the following data sources and
extract your supply chain information. AWS Supply Chain can store the extracted information
in your Amazon S3 buckets and use the data for _Demand planning_, _Insights_, _Supply Planning_, _N-Tier Visibility_, _Work Order Insights_, and _Sustainability_.

- **Amazon S3 source data** – You can use the Amazon S3 data source
  flow option if you don't have an ERP system, or if you use another extraction
  tool. You can extract raw data from your data source, map the data fields with
  AWS Supply Chain data model, and upload them to Amazon S3 with an integration tool
  of your choice. You can only upload CSV files to Amazon S3 when you're using
  Auto-association.
- **Electronic data interchange (EDI)** – AWS Supply Chain
  supports X12 ANSI version 4010 for EDI messages 850, 860, and 856. Supported
  data formats are .edi or .txt. You can add your raw EDI messages to Amazon S3 using
  an integration tool of your choice. AWS Supply Chain can extract and associate
  your raw EDI messages using default templates by Natural Language Processing
  (NLP) for EDI 856. NLP templates are not supported for EDI 850 and 860 and come
  with pre-defined, but customizable recipes in AWS Supply Chain.
- **SAP S/4HANA** – To extract your supply chain data from
  an SAP S/4HANA data source, AWS Supply Chain can use the Amazon AppFlow connector to
  connect to this source. AWS Supply Chain can associate your supply chain data
  stored in SAP S/4HANA system to the AWS Supply Chain data model using
  AWS Glue DataBrew.
- **SAP ECC 6.0** – You can use an integration
  tool (for example, ETL or iPaaS) to extract your supply chain data stored in the
  SAP ECC 6.0 system and put it into the Amazon S3 bucket using an API.
  AWS Supply Chain can associate your supply chain data stored in the SAP ECC 6.0
  system to the AWS Supply Chain data model using DataBrew.

###### Topics

- [Terminology used in data lake](data_lake_terminology.md "data_lake_terminology.md")
- [Data lake dashboard](data_ingestion.md "data_ingestion.md")
- [Adding a new data source](adding_new_flows.md "adding_new_flows.md")
- [Ingesting data for existing connections](ingesting-data.md "ingesting-data.md")
