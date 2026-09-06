

# Transforming healthcare data
<a name="data-transformation"></a>

AWS HealthLake Data Transformation Agent is a fully managed service that converts legacy healthcare data into the Fast Healthcare Interoperability Resources (FHIR) R4 standard. It accepts two source formats: C-CDA (Consolidated Clinical Document Architecture, the standard XML format for clinical documents such as discharge summaries and care plans) and CSV: and produces FHIR R4 resources that applications can query through standard FHIR APIs. No FHIR expertise is required: the Data Transformation AI agent authors and edits the conversion logic from a description of what you need.

Data Transformation Agent is a capability within AWS HealthLake. Common use cases include:
+ **Migrate legacy clinical archives**: Convert years of C-CDA documents or CSV exports into queryable FHIR R4 resources.
+ **Onboard a new data source**: An ISV or platform team can stand up a conversion for a new customer or feed in days instead of months.
+ **Build a longitudinal record**: Aggregate data from multiple sources into a HealthLake data store, where downstream analytics and AI consume it.

**Important**  
Data Transformation Agent is available as a preview capability and is subject to change. The APIs, features, and documentation described in this guide may be modified before general availability.

## Important notice
<a name="data-transformation-important-notice"></a>

Data Transformation Agent converts the format of healthcare data; it is not a substitute for professional medical advice, diagnosis, or treatment, and is not intended to cure, treat, mitigate, prevent, or diagnose any disease or health condition. You are responsible for validating converted data and for instituting human review as part of any use of Data Transformation Agent, including in association with any third-party product intended to inform clinical decision-making. **Converted data should only be used in patient care or clinical scenarios after review by trained medical professionals applying sound medical judgment.**

As part of the feature, AWS is offering Data Transformation AI agent - an LLM-powered agent designed to help you quickly and seamlessly configure the default data transformation profiles to your business logic and requirements by simply making conversational requests. These requests should not include any personally identifying, confidential, or sensitive information, and the agent only has access to the configuration request, not the underlying data (neither the source data, nor the converted data). AWS anticipates that these requests will be limited to managing and configuring the profile (the AWS resource).

## Features of Data Transformation Agent
<a name="data-transformation-features-overview"></a>

Data Transformation Agent provides the following features.

**Healthcare-aware data transformation AI agent**  
Data Transformation Agent is purpose-built for clinical data. It maps C-CDA document sections to the correct FHIR resources (for example, a "Problems" section to Condition resources) and maps legacy OIDs (Object Identifiers) to FHIR URIs. Describe a change in natural language, and the AI agent updates the underlying mappings and conversion logic using Velocity templates for C-CDA and a YAML mapping configuration for CSV, and presents the change for review before it is applied. The agent accepts natural-language instructions, sample data, schema documentation, and FHIR validation errors as input, and supports iterative refinement. Conversion logic can also be edited directly.

**Reusable, versioned profiles**  
Conversion logic lives in transformation profiles that you create once and reuse across all datastores and jobs in your account. Every published version is an immutable snapshot, so you can compare versions, roll back to any previous version, and keep editing a draft while transformation jobs run against the last published version.

**Starter and base profiles**  
Begin from a working profile instead of a blank one. For C-CDA, the AWS Starter Profile is a prebuilt profile that provides common section-to-resource mappings out of the box. For CSV, the AI agent generates a base profile tailored to your schema from sample CSV files in Amazon S3. Use either as-is, customize it with the AI agent, or clone it as the basis for a new profile.

**Real-time and bulk conversion**  
Convert a single document in real time for testing and interactive use, or run bulk jobs over Amazon S3. There is no infrastructure to manage, and malformed inputs are skipped and logged for refinement without failing the batch.

**Flexible output destinations**  
Write converted FHIR resources to a standalone Amazon S3 location, or convert and ingest directly into an AWS HealthLake datastore in a single step so that downstream analytics, AI, and resource matching can consume the data.

**Validation and quality reporting**  
Validate source C-CDA files, mappings, and FHIR output so you can catch errors early and confirm conversion quality.

**Drift detection**  
Enable a drift report that surfaces source elements not captured in the transformed output so you can find and close mapping gaps.

**Provenance and audit trail**  
When enabled, Data Transformation Agent generates a US Core-conformant FHIR Provenance resource for every conversion, tracing each output resource back to its source file and location.

**Access from the console, the SDK, and your IDE**  
Use the AWS Management Console for a visual workflow, the AWS CLI and SDKs for automation and CI/CD, or the Model Context Protocol (MCP) to author profiles, run conversions, and debug failures from an MCP-compatible IDE such as Kiro or Cursor. All interfaces share the same API surface.

## Accessing Data Transformation Agent
<a name="data-transformation-accessing"></a>

You can access Data Transformation Agent using the AWS Management Console, the AWS Command Line Interface, the AWS SDKs, and the Model Context Protocol (MCP).

**AWS Management Console**  
A web interface for creating profiles, running transformation jobs, and reviewing results.

**AWS CLI and AWS SDKs**  
Programmatic access to the Data Transformation AI agent APIs: the AWS CLI for the command line and shell automation, and the AWS SDKs for application code and CI/CD. Both wrap the same underlying REST API. (The synchronous, real-time conversion operation is available through the REST API only.)

**MCP (Model Context Protocol)**  
All Data Transformation AI agent APIs are available as MCP tools via AWS MCP server, so AI agents such as Kiro and Cursor can author profiles, run conversions, and debug failures.

## HIPAA eligibility and data security
<a name="data-transformation-hipaa"></a>

Data Transformation Agent is offered as a part of AWS HealthLake which is a HIPAA Eligible Service. For more information about AWS, the U.S. Health Insurance Portability and Accountability Act of 1996 (HIPAA), and using AWS services to process, store, and transmit protected health information (PHI), see [HIPAA Overview](https://docs.aws.amazon.com/health/latest/ug/hipaa.html).

Connections to Data Transformation Agent containing PHI must be encrypted. By default, all connections use HTTPS over TLS. You can also connect through an interface VPC endpoint powered by AWS PrivateLink, using the AWS HealthLake and interface VPC endpoints (AWS PrivateLink) service. Profile content and job output are encrypted at rest using either a customer-managed AWS KMS key or an AWS-owned key. See [Setting up permissions to do data transformation jobs](data-transformation-setting-up.md#data-transformation-setting-up-job-permissions) for encryption and access-control details.

## Pricing
<a name="data-transformation-pricing"></a>

Data Transformation AI agent is available in preview. Contact your AWS account team so we can confirm production readiness for your use case. Pricing will be announced when the capability becomes generally available. Any transformed data ingested into HealthLake will be subject to AWS HealthLake pricing.

## How to get started
<a name="data-transformation-how-to-get-started"></a>

If you are a first-time user of Data Transformation Agent, we recommend reading the following sections in order:

1. **[How Data Transformation Agent works](data-transformation-how-it-works.md)**: The core objects (transformation profile, transformation job, the AI agent) and how they relate.

1. **[Setting up](data-transformation-setting-up.md)**: The account access and permissions you need.

1. **Getting started** with the [Getting started with the SDK and AWS CLI](data-transformation-getting-started-cli.md), [Getting started with MCP](data-transformation-getting-started-mcp.md), or [Getting started with the console](data-transformation-getting-started-console.md): An end-to-end walkthrough in your preferred interface.