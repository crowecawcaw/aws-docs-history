# HealthLake for EHRs

For EHR builders, AWS HealthLake provides a fully managed FHIR R4 data store that serves
as the unified foundation for your transactional FHIR server, analytics, and AI
workloads. Rather than building and operating a custom FHIR server — including the
database, search index, bulk export pipeline, and compliance infrastructure — you
delegate that layer to HealthLake and focus on clinical workflows, UI, and business logic.

AWS HealthLake stores data natively as FHIR JSON resources. Every resource is indexed and
versioned at ingest and immediately queryable through standard FHIR RESTful APIs. The
service scales automatically. You don't need to plan capacity, tune databases, or
perform administration.

## Core capabilities

HealthLake provides the following capabilities for EHR builders:

- **Comprehensive FHIR R4 API** — CRUD
  operations across 105+ FHIR R4 resource types. Includes FHIR Search
  with chained parameters and `_include`/`_revinclude`,
  batch/transaction bundles, resource versioning with `_history`,
  and the `$export` operation writing NDJSON directly to Amazon S3.
- **US Core IG** — Supports profiles up to US
  Core STU v7.0.0, starting with US Core v3.1.1 (the normative basis for ONC
  certification).
- **SMART on FHIR** — Supports SMART App Launch
  Framework IG v2.0.0, including standalone launch, EHR launch, and backend
  services flows through any OAuth 2.0 compliant Identity Provider host
  including Amazon Cognito.
- **Bulk Data Access** — Supports FHIR Bulk
  Data Access IG v2.0.0 for Patient, Group, and System-level
  `$export`.
- **ONC Inferno Validation** — You can use
  HealthLake's FHIR API to pass the ONC Inferno test suite to support EHR
  certification requirements for §(g)(10) Single Patient API and Multi-Patient
  API sequences.
- **Zero-ETL Access** — Automatically transforms
  FHIR data into Apache Iceberg formats for direct SQL queries through
  Athena, Redshift, or .

###### Note

HealthLake is not itself an ONC-certified Health IT Module — certification applies to
your complete EHR product. HealthLake provides the FHIR infrastructure layer.

## Regulatory compliance

The following table maps regulatory requirements to HealthLake support:

| Requirement      | Standard                   | HealthLake Support                                              |
| ---------------- | -------------------------- | --------------------------------------------------------------- |
| US Core IG       | US Core STU v7.0.0         | Native profile validation                                       |
| SMART on FHIR    | SMART App Launch IG v2.0.0 | Cognito integration; standalone, EHR, and backend service flows |
| Bulk Data Access | Bulk Data Access IG v2.0.0 | Patient, Group, and System-level `$export`                      |
| ONC Inferno      | §(g)(10) test sequences    | Validated Single and Multi-Patient API                          |

## Differentiation

HealthLake differentiates from self-managed FHIR servers in the following ways:

- No infrastructure to operate
- Delivers performance at scale with thousands of transactions per second, petabytes of storage, and sub-second latency.
- Pay-as-you-go cost structure with no upfront licensing
- Compliance inheritance — HIPAA-eligible under AWS BAA, ISO/SOC, AES-256,
  TLS 1.2+, IAM, VPC endpoints, and CloudTrail
- Speed to production — transactional database, analytics database, and data-as-service in one managed offering

## Use cases

The following are common EHR use cases for HealthLake:

- **ONC-Certified EHR FHIR Backend** — HealthLake
  serves as the transactional FHIR server layer for EHR applications
  pursuing ONC certification.
- **EHR Data Analytics** — HealthLake's zero-ETL
  integration makes real-time clinical data available for SQL-based analytics
  through Athena or Redshift.

## Case studies

The following case studies demonstrate how EHR companies use HealthLake:

- [Greenway Health](https://aws.amazon.com/solutions/case-studies/latest-greenway-aws-healthlake-case-study/ "https://aws.amazon.com/solutions/case-studies/latest-greenway-aws-healthlake-case-study/")
- [MEDHOST](https://aws.amazon.com/blogs/machine-learning/how-medhost-is-migrating-electronic-health-record-data-to-aws-for-compliance-and-gaining-valuable-insights/ "https://aws.amazon.com/blogs/machine-learning/how-medhost-is-migrating-electronic-health-record-data-to-aws-for-compliance-and-gaining-valuable-insights/")
