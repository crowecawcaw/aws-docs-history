# SCPERF03-BP02 Select your storage architecture based on workload

Data lineage is important in the world of producers and consumers
of the data. This lineage can be verified and validated when it is
tracked from the source system to the destination systems. As a
result, well-organized data leads to better understanding.

**Desired outcome:** Well-organized
data with improved understanding.

**Benefits of establishing this best
practice:** Data lineage, scalability, resilience, and
re-usability.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

AWS Supply Chian needs a data lake with AI/ML models for supply
chains to understand, extract, and transform disparate,
incompatible data into a unified data model. The data lake can
ingest your data from various data sources, including your
existing ERP systems, such as SAP S/4HANA, and supply chain
management systems. To add data from variable sources such as
EDI 856, some applications use AI/ML and natural language
processing (NLP) to associate data from source systems to the
unified data model. EDI 850 and 860 messages are transformed
directly with predefined but customizable transformation
recipes.

### Implementation steps

1. Design a data lake architecture using Amazon S3 to store
   diverse supply chain data from multiple sources and
   formats.
2. Implement data ingestion pipelines using AWS Glue to
   extract, transform, and load data from ERP systems and
   supply chain applications.
3. Configure AI/ML models to process and standardize
   disparate data formats, including EDI messages and
   unstructured documents.
4. Establish data lineage tracking mechanisms to maintain
   visibility into data flow from source systems to
   destination applications.
5. Implement data governance policies and access controls to
   maintain data quality and security across the storage
   architecture.
6. Create automated data validation and quality monitoring
   processes to maintain data integrity throughout the supply
   chain environment.
