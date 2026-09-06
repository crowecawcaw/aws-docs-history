

# HealthLake for Payers
<a name="reference-industry-payers"></a>

 Health plans and payer technology providers face a convergence of regulatory mandates and operational complexity. The CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F) and the CMS Interoperability and Patient Access Final Rule (CMS-9115-F) require FHIR APIs, and utilization management and chart review workflows operate at high volume. 

 AWS HealthLake provides a FHIR R4-native data foundation for these challenges: a single managed service that can serve as the canonical member protected health information (PHI) store, a CMS-aligned API surface, and a data backbone for payer analytics and AI workloads. 

 This guide covers how payers and payer platform ISVs use HealthLake to satisfy federal interoperability mandates, build intelligent utilization management workflows, and run population-level analytics without the lengthy integration cycles that legacy FHIR gateway projects typically require. 

![Overview diagram showing AWS HealthLake as the FHIR R4 data foundation for payers, connecting member data sources and CMS interoperability APIs with utilization management, analytics, and AI workloads.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-overview.png)


## Core capabilities
<a name="reference-industry-payers-capabilities"></a>

 HealthLake provides the following capabilities for health plans and payer technology providers: 
+  **Member data store with high-performance FHIR server** – Store member PHI (claims, clinical, pharmacy, coverage, and prior authorization decisions) in a single canonical member store at petabyte scale. High-performance FHIR REST APIs with full CRUD and FHIR search enable access across CMS-relevant resource types, so you can unify data across your book of business. 
+  **SMART on FHIR** – Authorize member-facing applications (PKCE for the Patient Access API), provider portals (EHR launch), and payer-to-payer exchange (backend services) through a single standards-based framework. Works with Amazon Cognito or any OAuth 2.0 compliant Identity Provider. 
+  **CMS interoperability endpoints** – Support CMS-9115-F and CMS-0057-F requirements through four dedicated paths (`/patientaccess/`, `/provideraccess/`, `/payertopayerdx/`, and `/priorauthservice/`) with automatic CloudWatch metrics by mandate category. For more information, see [CMS compliance features](reference-compliance-cms.md). 
+  **Bulk import and Da Vinci export** – Onboard claims and clinical data from Amazon S3 as NDJSON at scale. Share member data with providers and other payers using the `$davinci-data-export` operation, which supports multiple export types (ATR, Provider Access, Payer-to-Payer, Member Access, and Provider Snapshot). 
+  **Data Transformation Agent** – Convert legacy clinical documents received through TEFCA QHINs, HIE connections, direct EHR feeds, and chart retrieval sources into validated FHIR R4 resources. Supports C-CDA, CSV, and flat-file formats using reusable versioned profiles. 
+  **Resource matching (Preview)** – Deduplicate member records across fragmented sources (claims engine, EHR feeds, pharmacy, and labs) by continuously evaluating resource types using healthcare identifiers such as MBI, MRN, and NPI. Creates FHIR `Linkage` resources to enable a single-member view across siloed systems. 
+  **AI agent integration (MCP)** – Connect Amazon Bedrock and AgentCore agents to live FHIR data through the open-source HealthLake Model Context Protocol (MCP) server to support utilization management triage, risk adjustment chart review, care management workflows, and clinical decision support against the complete member record. 
+  **Zero-ETL analytics access** – Run quality measure calculation, claims analytics, fraud/waste/abuse (FWA) detection, and actuarial reporting directly against FHIR data that is automatically flattened into Apache Iceberg open table format. Query through analytics compute engines such as Athena, Amazon Redshift Spectrum, and Amazon SageMaker Unified Studio without custom extraction pipelines. 
+  **Clinical NLP** – Extract diagnoses, medications, and procedures from unstructured clinical text (progress notes, discharge summaries, and specialist consults) using Amazon Comprehend Medical. Supports hierarchical condition category (HCC) coding for risk adjustment, supplemental quality-measure data capture, and prior authorization evidence assembly. 

## Regulatory compliance
<a name="reference-industry-payers-compliance"></a>

**Note**  
 This information is provided for general reference and is not legal or regulatory compliance advice. You are responsible for conducting your own regulatory assessments and engaging qualified compliance counsel. For more information about CMS interoperability endpoints and metrics in HealthLake, see [CMS compliance features](reference-compliance-cms.md). 

### CMS-9115-F: Interoperability and Patient Access Final Rule (2020)
<a name="reference-industry-payers-cms-9115"></a>

 Effective since 2021, CMS-9115-F requires impacted payers (Medicare Advantage, Medicaid, CHIP, and QHP issuers on the federally facilitated exchanges) to implement the following: 
+  **Patient Access API** – A FHIR R4 API exposing adjudicated claims, clinical data, and formulary information to members through third-party applications. Conformance target: CARIN Blue Button IG. 
+  **Provider Directory API** – A publicly accessible FHIR R4 endpoint exposing provider network data. Conformance target: Da Vinci PDex Plan Net IG. 

### CMS-0057-F: Interoperability and Prior Authorization Final Rule (2024)
<a name="reference-industry-payers-cms-0057"></a>

 Effective January 1, 2027 for API implementation (with metrics reporting beginning March 31, 2026 for CY 2025 data), CMS-0057-F requires impacted payers to implement the following: 
+  **Patient Access API (enhanced)** – Adds prior authorization decisions (excluding drugs) to the existing Patient Access API data, and adds an annual usage metrics reporting requirement. 
+  **Provider Access API** – A FHIR R4 API enabling in-network providers to access attributed member clinical and claims data through attribution (ATR) reconciliation and bulk export. Conformance target: Da Vinci PDex IG and ATR IG. 
+  **Payer-to-Payer Data Exchange API** – A FHIR R4 bulk exchange of member clinical and claims history between payers upon explicit member opt-in consent. Conformance target: Da Vinci PDex IG and HRex IG. 
+  **Prior Authorization API** – A FHIR R4 API for electronic prior authorization submission, documentation, and decision using the Da Vinci CRD, DTR, and PAS IGs. Service level agreement (SLA): 72 hours for urgent requests and 7 calendar days for standard requests. 
+  **Drug Formulary API** – FHIR-based formulary exposure using the Da Vinci PDex US Drug Formulary IG, exposing `InsurancePlan`, `FormularyItem`, and `FormularyDrug` with `RxNorm` coding. 

### HealthLake CMS compliance mapping
<a name="reference-industry-payers-cms-mapping"></a>


| CMS requirement | Key FHIR resources and operations | HealthLake support | 
| --- | --- | --- | 
| Patient Access API | ExplanationOfBenefit, Coverage, Patient, Condition; $davinci-data-export (member type) | Native R4 CRUD, search, and bulk export | 
| Provider Access API | Group (ATR), Patient, ExplanationOfBenefit, Coverage; $attribution-status, $member-add, $member-remove, $confirm-attribution-list, $davinci-data-export | Native ATR operations and bulk export | 
| Prior Authorization API | Claim (preauthorization), ClaimResponse, Questionnaire; $questionnaire-package, $submit, $inquire | Native PAS and DTR operations | 
| Payer-to-Payer Exchange | Patient, Coverage, ExplanationOfBenefit, Consent; $member-match, $bulk-member-match, $davinci-data-export (P2P type) | Native matching and bulk export | 
| Provider Directory API | Organization, Practitioner, Location, InsurancePlan | Native R4 CRUD and search | 
| Drug Formulary API | InsurancePlan, MedicationKnowledge, Basic (FormularyItem) | Native R4 CRUD and search | 

## Getting started with HealthLake for CMS-0057-F compliance
<a name="reference-industry-payers-getting-started"></a>

**Note**  
 This section provides a high-level starting path for implementing CMS-0057-F mandated APIs using HealthLake. It is not intended to be comprehensive and does not constitute legal or regulatory compliance advice. You are responsible for conducting your own regulatory assessments and engaging qualified compliance counsel. 

 CMS-0057-F requires impacted payers to implement five FHIR R4 APIs by January 1, 2027. HealthLake provides native infrastructure for each mandate. The following steps outline an implementation path. 

1. **Step 1: Create a SMART on FHIR-enabled data store.**
   + Provision a HealthLake FHIR R4 data store with the SMART on FHIR V2 authorization strategy.
   + Configure your OAuth 2.0 authorization server (Amazon Cognito or an external Identity Provider) and Lambda token decoder.

   For more information, see [Creating a HealthLake data store](managing-data-stores-create.md), [Getting started with SMART on FHIR](reference-smart-on-fhir-getting-started.md), and [HealthLake authentication requirements for SMART on FHIR](reference-smart-on-fhir-authentication.md).

1. **Step 2: Load claims, clinical, provider, and formulary data.**

   Bulk import NDJSON FHIR bundles from Amazon S3 covering all API domains:
   + **Patient Access** – `ExplanationOfBenefit`, `Coverage`, `Patient`, `Condition`
   + **Provider Access** – Group (ATR profile), Patient, `ExplanationOfBenefit`, Coverage, and clinical resources
   + **TEFCA and clinical feeds** – C-CDA documents from QHINs, ADT notifications (HL7v2), and lab results (ORU). Use the Data Transformation Agent for C-CDA-to-FHIR conversion.
   + **Prior Authorization** – Claim (use=preauthorization), ClaimResponse, and Questionnaire
   + **Payer-to-Payer** – Patient, Coverage, Consent, `ExplanationOfBenefit`, and clinical resources
   + **Provider Directory** – Practitioner, Organization, Location, and InsurancePlan
   + **Drug Formulary** – InsurancePlan, MedicationKnowledge, and Basic (FormularyItem)

   For more information, see [Starting a FHIR import job](importing-fhir-data-start.md).

1. **Step 3: Validate against CMS-required Implementation Guides.**

   Use the `$validate` operation to verify resource conformance against the mandated Implementation Guides (IGs):
   + **Prior Authorization API** – Da Vinci PAS IG, DTR IG, and CRD IG
   + **Patient Access API** – CARIN Blue Button IG
   + **Provider Access API** – Da Vinci PDex IG and ATR IG
   + **Payer-to-Payer** – Da Vinci PDex IG and HRex IG
   + **Provider Directory API** – Da Vinci PDex Plan Net IG
   + **Drug Formulary API** – Da Vinci PDex US Drug Formulary IG

   For more information, see [Validating FHIR Resources with `$validate`](reference-fhir-operations-validate.md) and [FHIR profile validations for HealthLake](reference-fhir-profile-validations.md).

1. **Step 4: Enable CMS-0057-F interoperability endpoints.**

   Route API calls through the HealthLake dedicated CMS endpoint paths:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/healthlake/latest/devguide/reference-industry-payers.html)

   No code changes are required beyond updating the URL path. All FHIR CRUD and search operations work identically. For more information, see [CMS compliance features](reference-compliance-cms.md).

1. **Step 5: Configure the Patient Access API.**
   + **Authorization** – SMART App Launch 2.0 standalone (OAuth 2.0 with PKCE, member-facing).
   + **Scopes** – `launch/patient patient/*.read openid fhirUser`
   + **Access pattern** – Individual FHIR reads (such as GET Patient and GET ExplanationOfBenefit) or bulk retrieval through `$davinci-data-export` (member type).
   + **Data scope** – Adjudicated claims, USCDI clinical data, coverage, and prior authorization decisions (excluding drugs). Service date floor: January 1, 2016. Bulk retrieval has a 5-year temporal limit.  
![Sequence diagram of the Patient Access API for a member-facing application. The app authenticates with SMART App Launch 2.0 standalone (PKCE), receives a patient-scoped access token, and queries HealthLake for individual FHIR resources (Patient, ExplanationOfBenefit, Coverage, Condition, InsurancePlan). A separate bulk export path uses $davinci-data-export (member type) with system/*.read scopes.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-patient-access-sequence.png)

1. **Step 6: Configure the Provider Access API.**
   + **Authorization** – SMART Backend Services (machine-to-machine, signed JWT).
   + **Scopes** – `system/*.read system/Group.write`
   + **Workflow**:

     1. The payer publishes a draft Group (ATR) per provider NPI.

     1. The provider reconciles using `$attribution-status`, `$member-add`, and `$member-remove`.

     1. The provider confirms using `$confirm-attribution-list` (status becomes "final").

     1. The provider exports using `$davinci-data-export` (PDex type).
   + **Data scope** – Clinical (US Core 6.1) plus non-financial claims (CARIN Blue Button 2.x basis) plus prior authorization decisions. No temporal limit. Financial data is automatically stripped.
   + **Consent** – Opt-out (the default is to share).
**Note**  
The PDex 2.1 IG defines two paths: v1 (ATR roster), where the payer publishes an attribution list and the provider reconciles it; and v2 (provider-attested match), where the provider submits treatment-relationship attestations. The IG recommends v2 for CMS-0057-F conformance. The IG calls the v2 operation `$provider-member-match`; HealthLake implements it as `$bulk-member-match` with the same semantics and output structure.  
![Sequence diagram of the end-to-end Provider Access API. The PDex 2.1 IG defines a v1 (ATR roster) path, where the payer publishes an attribution list and the provider reconciles it using $attribution-status, $member-add, $member-remove, and $confirm-attribution-list; and a v2 (provider-attested match) path using $bulk-member-match. Both paths converge at $davinci-data-export for bulk retrieval to Amazon S3.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-provider-access-sequence.png)

1. **Step 7: Configure Payer-to-Payer Data Exchange.**
   + **Authorization** – SMART Backend Services (machine-to-machine; requesting payer to responding payer's Identity Provider).
   + **Scopes** – `system/*.read system/Group.write system/Consent.write`
   + **Workflow**:

     1. The member opts in (HRex Consent).

     1. `$bulk-member-match` (up to 500 members per batch), then poll status to receive a persisted MatchedMembers Group.

     1. `$davinci-data-export` (P2P type) on the matched Group.
   + **Data scope** – Clinical plus non-financial claims plus prior authorization decisions. 5-year temporal limit. Financial data is automatically stripped.
   + **Consent** – Opt-in (explicit). Request within 1 week. Quarterly refresh for concurrent payers.
   + **Consent-Patient linkage** – The `Consent.patient` reference is stored as-is (the requesting payer's reference). HealthLake provides the mapping in the MatchedMembers Group output (`member.entity.reference` maps to the matched Patient, and `member.entity.extension` maps to the input Patient). Build the Consent-to-Patient linkage in your application layer.

   For more information, see [`$bulk-member-match` operation for HealthLake](reference-fhir-operations-bulk-member-match.md), [`$member-match` operation for HealthLake](reference-fhir-operations-member-match.md), and [FHIR R4 `$davinci-data-export` operation for HealthLake](reference-fhir-operations-davinci-data-export.md).  
![Sequence diagram of the end-to-end Payer-to-Payer data exchange. The requesting payer authenticates to the responding payer's HealthLake instance via SMART Backend Services, submits member demographics and consent via $bulk-member-match (up to 500 members per batch with inline HRex Consent), polls for match results, and exports matched member history via $davinci-data-export (P2P type). A $member-match path supports single-member pre-validation only.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-payer-to-payer-sequence.png)

1. **Step 8: Configure the Prior Authorization API.**
   + **Authorization** – A dual model: SMART App Launch 2.0 (PKCE) for DTR and PAS interactions; a pre-registered token per the CDS Hooks specification for CRD service invocation; and IAM SigV4 for server-to-server calls (Lambda to HealthLake).
   + **Scopes** – `patient/*.read` (DTR launch context) and `system/Claim.write` (PAS submission).
   + **Workflow (three IGs)**:
     + **CRD** – The EHR invokes CDS Hooks, and API Gateway with Lambda evaluates prior authorization requirements using clinical data from HealthLake (customer-built decision logic).
     + **DTR** – `$questionnaire-package` resolves a payer-defined Questionnaire, CQL/FHIRPath pre-population logic, and ValueSets for the given Coverage and service type. CQL executes client-side in the EHR, not in HealthLake.
     + **PAS** – `$submit` submits a prior authorization Bundle (`Claim` plus `DocumentReference` resources) and returns a `ClaimResponse` (outcome=queued). `$inquire` polls status. Asynchronous adjudication (through EventBridge or FHIR Subscriptions) writes decisions (approved, denied, or pended) back to HealthLake.
   + **Cancel or update** – Resubmit `$submit` with the same `Claim.identifier`. An update uses modified items or documents; a cancel uses `Claim.status=cancelled`.
   + **Customer-built components** – CRD decision logic (Lambda) and the prior authorization adjudication engine (rules, ML, or manual review queue).
   + **SLA** – 72 hours (urgent) and 7 calendar days (standard) per CMS-0057-F.

   For more information, see [FHIR `$submit` operation for HealthLake](reference-fhir-operations-submit.md), [FHIR `$inquire` operation for HealthLake](reference-fhir-operations-inquire.md), and [FHIR `$questionnaire-package` operation for HealthLake](reference-fhir-operations-questionnaire-package.md).  
![Sequence diagram of the end-to-end Prior Authorization API across the three Da Vinci IGs. The CRD phase invokes a CDS Hooks service (customer-built on API Gateway and Lambda) using clinical data from HealthLake. The DTR phase uses $questionnaire-package to resolve the payer Questionnaire, CQL/FHIRPath logic, and ValueSets (CQL executes client-side in the EHR). The PAS phase uses $submit for bundle submission and $inquire for status polling, with async adjudication writing ClaimResponse decisions back to HealthLake.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-prior-authorization-sequence.png)

1. **Step 9: Configure the Drug Formulary API.**
   + Load `InsurancePlan`, `MedicationKnowledge`, and `Basic` (FormularyItem) resources with `RxNorm` coding.
   + Expose the data through a standard FHIR R4 endpoint with Da Vinci PDex US Drug Formulary IG conformance.
   + Support coverage-specific formulary queries and tier/cost-sharing information.

1. **Step 10: Monitor and report for CMS compliance.**
   + Use enhanced CloudWatch metrics dimensioned by `URIType`, `Sub`, and `ClientId` per CMS API category.
   + Set alarms for prior authorization SLA compliance (72 hours urgent and 7 days standard).
   + Perform annual reporting (effective 2026): report Patient Access API usage metrics to CMS. The first report covers CY 2025 data and is due by March 31, 2026.

   For more information, see [CMS compliance features](reference-compliance-cms.md) and [Monitoring HealthLake metrics using Amazon CloudWatch](monitoring-cloudwatch.md).

## Use cases
<a name="reference-industry-payers-use-cases"></a>

 Beyond compliance, HealthLake serves as the operational FHIR backbone for payer workloads across transactional, agentic, and analytics use cases. 

### Utilization management
<a name="reference-industry-payers-uc-um"></a>

 Prior authorization, concurrent review, and retrospective review operate at high volume, and CMS-0057-F mandates a sub-72-hour turnaround for urgent requests and 7 calendar days for standard requests. 
+ **Native prior authorization operations** – `$submit`, `$inquire`, and `$questionnaire-package` through `/priorauthservice/v2/r4/` handle the full prior authorization lifecycle.
+ **Agentic criteria evaluation** – Amazon Bedrock AgentCore agents query HealthLake through MCP, apply payer criteria, and produce auditable `ClaimResponse` and `Provenance` resources.
+ **Asynchronous adjudication** – EventBridge triggers determination logic post-submission, writes decisions back to HealthLake, and notifies providers within CMS timelines.

![End-to-end prior authorization flow: EHR triggers and clinical documentation enter through API Gateway; Amazon Bedrock AgentCore evaluates criteria via MCP against HealthLake's native $submit, $inquire, and $questionnaire-package operations; EventBridge routes to async adjudication; and determinations (auto-approved, pended, denied, cancel/update) write back.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-utilization-management-flow.png)


### Member 360 and longitudinal record
<a name="reference-industry-payers-uc-member360"></a>

 HealthLake serves as the canonical member PHI store. Operational systems handle runtime workloads, and results sync to HealthLake as the single source of truth. 
+ **Multi-source ingestion** – Claims (`ExplanationOfBenefit`), EHR clinical data (FHIR Bulk `$export`), TEFCA clinical feeds (C-CDA through QHINs, converted by the Data Transformation Agent), pharmacy (`MedicationDispense`), labs (`Observation` from HL7v2), and remote patient monitoring device data, in a single FHIR store.
+ **Data Transformation Agent** – AI-powered C-CDA and CSV conversion into FHIR R4 resources to onboard historical clinical data.
+ **Resource matching (Preview)** – Continuous deduplication across resource types using healthcare identifiers (MBI, MRN, and NPI). Creates `Linkage` resources to enable a single-member view across siloed systems.

![Multi-source ingestion pattern: seven data categories flow through Amazon S3 bulk import, HealthLake data transformation, and Lambda into HealthLake's canonical store, with resource matching for deduplication. Downstream consumers (MCP agents, Athena analytics, CMS interoperability APIs, and EventBridge) read from a single unified member record.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-member-360-ingestion.png)


### Risk adjustment and HCC coding
<a name="reference-industry-payers-uc-risk"></a>
+ **Clinical NLP pipeline** – The Data Transformation Agent converts C-CDAs into FHIR resources, and Amazon Comprehend Medical extracts ICD-10-CM diagnoses from unstructured notes, surfacing hierarchical condition categories (HCCs) that claims-only approaches miss.
+ **Chart review agents** – Amazon Bedrock AgentCore agents query HealthLake through MCP, evaluate documentation against CMS-HCC model requirements, and produce evidence-referenced recommendations.
+ **RADV audit readiness** – Every HCC carries its evidence chain (`DocumentReference` to `Condition` to `Provenance`) stored natively in HealthLake.

![Dual-pipeline extraction pattern: HealthLake data transformation handles structured data (C-CDA/CSV to FHIR) while Amazon Bedrock Data Automation processes unstructured clinical documents. Both feed HealthLake, which runs built-in Amazon Comprehend Medical NLP on DocumentReferences. Amazon Bedrock AgentCore agents then evaluate HCCs against CMS model requirements via MCP.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-risk-adjustment-pipeline.png)


### Care management and member engagement
<a name="reference-industry-payers-uc-care"></a>

 Value-based contracts require longitudinal member engagement and proactive intervention. 
+ **Care resources** – `CarePlan`, `CareTeam`, `Goal`, and `EpisodeOfCare` model active programs. MCP-enabled agents maintain longitudinal context across member interactions.
+ **Transitions and alerting** – EventBridge subscriptions on `Encounter` (discharge) and `Observation` (threshold breach) trigger post-discharge outreach and chronic disease intervention workflows.
+ **Payer-to-payer continuity** – `$bulk-member-match` and `$davinci-data-export` transfer the longitudinal record when members transition plans.

![Event-driven care management flow: clinical triggers (ADT, utilization, pharmacy gaps, and payer-to-payer transitions) route through EventBridge and Step Functions into HealthLake's CarePlan store, where Amazon Bedrock AgentCore agents generate personalized outreach via MCP.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-care-management-flow.png)


### Quality measurement
<a name="reference-industry-payers-uc-quality"></a>
+ **Population gap scanning** – Athena queries HealthLake data to identify open quality-measure gaps at scale.
+ **Supplemental data capture** – The Data Transformation Agent converts clinical documents containing measure evidence that claims-only logic misses, closing gaps without member outreach.
+ **Measure computation** – Zero-ETL flattens FHIR resources into Iceberg tables. Athena SQL evaluates each measure as set logic (initial population, denominator, exclusions, and numerator) at population scale. Results write back to HealthLake as `MeasureReport` resources per member. No CQL engine is required.

![Quality measurement pipeline: claims, labs, EHR, and supplemental data ingest via Amazon S3 and the Data Transformation Agent into HealthLake, which materializes via Zero-ETL to Iceberg tables where Athena runs population-scale gap logic. MeasureReport resources write back to HealthLake, and Amazon QuickSight surfaces quality forecasts.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-quality-measurement-pipeline.png)


### Claims analytics, payment integrity, and FWA
<a name="reference-industry-payers-uc-claims"></a>
+ **Medallion architecture** – HealthLake through Zero-ETL to Amazon S3/Iceberg (Bronze), to Glue (Silver), to Athena or Redshift Serverless (Gold), with no extraction pipelines.
+ **FWA detection** – Athena SQL identifies duplicates, unbundling, upcoding, and provider outliers. SageMaker Unified Studio trains anomaly detection models against the Gold layer.
+ **Financial reporting** – Per member per month (PMPM) trending, medical loss ratio (MLR) monitoring, risk adjustment forecasting, and actuarial reserving through Athena and Redshift Serverless.

![Medallion data flow: raw EDI lands in Amazon S3 (Bronze); Glue parses, enriches, and cleans into tabular form, and the Data Transformation Agent converts tabular/CSV to FHIR (Silver); HealthLake serves as the curated Gold layer; and Zero-ETL materializes data to Iceberg for SageMaker anomaly models and Athena rule-based detection.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/payers-claims-analytics-medallion.png)
