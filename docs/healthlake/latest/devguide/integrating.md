

# Integrating AWS HealthLake

AWS HealthLake supports two types of integration. Natural language processing (NLP) extracts medical information from unstructured text. Analytics engines and platforms query your FHIR data with SQL.

**Natural language processing**

Amazon Comprehend Medical is a HIPAA eligible natural language processing (NLP) service that uses machine learning to extract health data from unstructured medical text in HealthLake. To learn about the service, see the [*Amazon Comprehend Medical Developer Guide*](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-welcome.html). For more information, see [Integrated natural language processing (NLP) for HealthLake](integrating-nlp.md).

**Analytics engines and platforms**

HealthLake stores each data store's FHIR data as Apache Iceberg tables, one for each resource type, and keeps them current. Lake Formation governs access to these tables, so any engine you authorize reads the same data without exports or copies.

The following table describes when to use each option. All options read the same Lake Formation-governed tables, so you can use more than one.


**Analytics options for HealthLake data**  

| Option | Choose when | Get started | 
| --- | --- | --- | 
| AWS analytics services (Amazon Athena, Amazon Redshift Spectrum, and Apache Spark on Amazon EMR) | You want to query HealthLake data inside AWS with services that integrate with Lake Formation. | [Using AWS analytics services](integrating-analytics-aws.md) | 
| Databricks | Your organization already uses Databricks and Unity Catalog for analytics, notebooks, or machine learning, and you want HealthLake data alongside your other data. | [Databricks integration](integrating-databricks.md) | 
| Snowflake | Your organization already uses Snowflake, and you want HealthLake data alongside your other Snowflake data. | [Snowflake integration](integrating-snowflake.md) | 

Databricks and Snowflake are third-party platforms that AWS doesn't provide or support. For the server that connects Databricks to HealthLake, see the [HealthLake OpenSharing repository](https://github.com/databricks-industry-solutions/healthlake-opensharing) on the GitHub website.

To learn how access works, see [How analytics access works](integrating-analytics.md#integrating-analytics-how-it-works).

**Topics**
+ [Natural language processing](integrating-nlp.md)
+ [Analytics](integrating-analytics.md)