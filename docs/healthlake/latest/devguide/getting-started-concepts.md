

# AWS HealthLake concepts
<a name="getting-started-concepts"></a>

The following terminology and concepts are central to your understanding and use of AWS HealthLake.

**Topics**
+ [Data store authorization strategy](#concept-data-store-authorization-strategy)
+ [Integrated NLP](#concept-integrated-nlp)
+ [Integrated analytics](#concept-integrated-analytics)

## Data store authorization strategy
<a name="concept-data-store-authorization-strategy"></a>

A HealthLake data store is a repository of FHIR R4 health data that resides within a single AWS Region. HealthLake supports the following data store authorization strategies.
+ **SigV4 authorization** — HealthLake authorizes FHIR API calls using [AWS Signature Version 4 (SigV4)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) authorization.
+ **SMART on FHIR authorization** — HealthLake authorizes FHIR API calls using [Substitutable Medical Applications and Reusable Technologies (SMART) on FHIR](https://docs.smarthealthit.org) authorization.

For more information, see [Creating a HealthLake data store](managing-data-stores-create.md).

## Integrated NLP
<a name="concept-integrated-nlp"></a>

AWS HealthLake integrates with HIPAA eligible natural language processing (NLP) libraries to extract meaningful health data from unstructured medical text. The NLP libraries identify medical entities like conditions, medications, dosages, tests, treatments, and procedures. They recognize relationships among the entities and link them to medical ontology libraries such as ICD-10-CM and RxNorm. For more information, see [Integrated natural language processing (NLP) for HealthLake](integrating-nlp.md).

## Integrated analytics
<a name="concept-integrated-analytics"></a>

AWS HealthLake goes beyond FHIR `search` and `bundle` APIs to provide integrated analytics for querying and analyzing large volumes of health data. During import, HealthLake automatically generates tables for SQL index and query. This enables you to gain actionable insights from complex healthcare data without requiring extensive data engineering work. For more information, see [Querying HealthLake data with Amazon Athena](integrating-athena.md) and [AWS HealthLake sample projects](reference-healthlake-sample-projects.md).