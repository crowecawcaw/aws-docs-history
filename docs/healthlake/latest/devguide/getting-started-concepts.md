# AWS HealthLake concepts

The following terminology and concepts are central to your understanding and use of
AWS HealthLake.

###### Concepts

- [Data store authorization
  strategy](#concept-data-store-authorization-strategy "#concept-data-store-authorization-strategy")
- [Integrated NLP](#concept-integrated-nlp "#concept-integrated-nlp")
- [Integrated analytics](#concept-integrated-analytics "#concept-integrated-analytics")

## Data store authorization

strategy

A HealthLake data store is a repository of FHIR R4 health data that resides within a single
AWS Region. HealthLake supports the following data store authorization strategies.

- **SigV4 authorization** — HealthLake authorizes FHIR
  API calls using [AWS Signature Version 4 (SigV4)](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") authorization.
- **SMART on FHIR authorization** — HealthLake authorizes
  FHIR API calls using [Substitutable Medical
  Applications and Reusable Technologies (SMART) on FHIR](https://docs.smarthealthit.org "https://docs.smarthealthit.org") authorization.

For more information, see [Creating a HealthLake data store](managing-data-stores-create.md "managing-data-stores-create.md").

## Integrated NLP

AWS HealthLake integrates with HIPAA eligible natural language processing (NLP) libraries to
extract meaningful health data from unstructured medical text. The NLP libraries identify
medical entities like conditions, medications, dosages, tests, treatments, and procedures.
They recognize relationships among the entities and link them to medical ontology libraries
such as ICD-10-CM and RxNorm. For more information, see [Integrated natural language processing (NLP) for HealthLake](integrating-nlp.md "integrating-nlp.md").

## Integrated analytics

AWS HealthLake goes beyond FHIR `search` and `bundle` APIs to provide
integrated analytics for querying and analyzing large volumes of health data. During import,
HealthLake automatically generates tables for SQL index and query. This enables you to gain
actionable insights from complex healthcare data without requiring extensive data engineering
work. For more information, see [Querying HealthLake data with Amazon Athena](integrating-athena.md "integrating-athena.md") and [AWS HealthLake sample projects](reference-healthlake-sample-projects.md "reference-healthlake-sample-projects.md").
