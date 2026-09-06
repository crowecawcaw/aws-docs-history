

# Patient insights
<a name="patient-insights"></a>

Patient insights synthesizes longitudinal patient data into a concise, actionable pre-visit summary by retrieving structured clinical records, clinical documents, and ad-hoc files, then generating a focused summary for clinicians to review before each encounter.

Patient insights provides the following capabilities:
+  **Longitudinal data synthesis** – Retrieves and synthesizes patient data scattered across structured FHIR resources, FHIR DocumentReference/Binary resources, and S3 documents into a single unified pre-visit summary.
+  **Evidence-linked output** – Every clinical statement in the summary includes evidence references linking back to the specific FHIR resources or source documents that support it.
+  **Focus summaries by encounter reason** – Tailors insights to encounter reason or chief complaint. For example, a wellness visit summary emphasizes preventive screenings and immunization status, while a surgical follow-up summary prioritizes procedure history and post-operative notes.
+  **Seamless workflow integration** – Delivers a structured JSON document that gives full control over rendering within your existing workflows.
+  **AWS ecosystem integration** – Integrates with AWS HealthLake as a FHIR-compliant data store and Amazon S3 for both document ingestion and summary delivery.

Patient insights is available as a preview in US East (N. Virginia) (`us-east-1`) and US West (Oregon) (`us-west-2`) Regions.

**Important**  
Patient insights is available as a preview feature and is subject to change. Do not use preview features in production environments.

**Topics**
+ [How patient insights works](#pi-how-it-works)
+ [Inputs](#pi-inputs)
+ [Submitting and tracking jobs](#pi-submitting-tracking-jobs)
+ [Output](#pi-output)
+ [Rendering the summary](#pi-rendering)

## How patient insights works
<a name="pi-how-it-works"></a>

Patient insights uses an asynchronous job-based workflow with four stages:

1.  **Job submission** – Your application submits a patient insights job by calling the StartPatientInsightsJob API. The request specifies the patient, encounter type, requesting clinician, data sources, and output location. The API returns a unique job identifier.

1.  **Data retrieval and synthesis** – Patient insights retrieves the patient’s clinical data from your configured data sources. The service connects to your FHIR-compliant data store (such as AWS HealthLake) to pull structured clinical records. It also retrieves clinical documents from FHIR DocumentReference and Binary resources, and can ingest ad-hoc documents from Amazon S3.

1.  **Polling for completion** – Your application polls for completion using the GetPatientInsightsJob API. A typical job completes in 2 to 5 minutes, depending on the volume and complexity of the patient’s clinical history.

1.  **Output retrieval** – When the job status reaches SUCCEEDED, the generated pre-visit summary is available at the S3 output path you specified. Your application retrieves the summary and presents it to the clinician.

## Inputs
<a name="pi-inputs"></a>

### Patient context
<a name="pi-patient-context"></a>

Provide a unique patient identifier that corresponds to the patient’s FHIR ID in your FHIR server. This identifier is the key the service uses to query the FHIR endpoint for that patient’s clinical history.

### Encounter reason
<a name="pi-encounter-reason"></a>

The encounter reason tells the service what type of visit is planned and why the patient is coming in. This helps the service prioritize which clinical information is most relevant. For example, a wellness visit summary emphasizes preventive screenings and immunization status, while a surgical follow-up summary prioritizes procedure history and post-operative notes.

### User context
<a name="pi-user-context"></a>

Identify the clinician requesting the summary, their role, and their specialty. This information helps the service tailor the summary to the clinician’s needs.

### Input data configuration
<a name="pi-data-sources"></a>

Specify where the service should look for the patient’s clinical data:
+  **FHIR server** – Provide a FHIR endpoint URL pointing to your FHIR-compliant data store (such as AWS HealthLake) along with an OAuth token for authentication. The service supports a configurable lookback period ranging from 1 to 24 months.
+  **FHIR DocumentReference and Binary resources** – The service retrieves clinical documents such as discharge summaries, consultation notes, and diagnostic reports from the same FHIR endpoint.
+  **S3 sources** – Specify documents stored in Amazon S3 that the service should include, such as faxed specialist referral letters, outside hospital records, or scanned imaging reports.

### Supported file formats
<a name="pi-supported-formats"></a>


| File format | Maximum size | 
| --- | --- | 
| PDF (application/pdf) | 500 MB or 3,000 pages | 
| JPEG (image/jpeg) | 10 MB | 
| PNG (image/png) | 10 MB | 

**Note**  
The service handles unsupported or oversized files differently depending on the source. S3 sources cause the job to fail if any file is unsupported or oversized. FHIR DocumentReference and Binary resources that are unsupported or oversized are silently skipped.

### Document processing limits
<a name="pi-document-limits"></a>

Patient insights accepts a maximum of 10 documents per job across all document sources combined. The service processes documents in this order:

1. S3 source documents are processed first.

1. FHIR DocumentReference and Binary documents are processed in sequential order.

If the total number of documents exceeds 10, only the first 10 are processed according to this ordering.

### Output data configuration
<a name="pi-output-data-configuration"></a>

Specify an S3 output path where the service delivers the completed pre-visit summary. You manage the retention and lifecycle of patient insights output through your S3 bucket lifecycle policies.

## Submitting and tracking jobs
<a name="pi-submitting-tracking-jobs"></a>

After you submit a patient insights job, you can track its progress by polling the GetPatientInsightsJob API. The following table describes the possible job statuses:


| Status | Description | 
| --- | --- | 
| SUBMITTED | The job has been accepted and is queued for processing. | 
| IN\_PROGRESS | The service is retrieving clinical data, processing source documents, and generating the patient summary. | 
| SUCCEEDED | The job has completed successfully. The generated summary is available at the specified S3 output path. | 
| FAILED | The job did not complete successfully. Check the error details in the GetPatientInsightsJob response for the specific failure reason. | 

## Output
<a name="pi-output"></a>

When a patient insights job completes successfully, Amazon Connect Health delivers a structured JSON document to your configured S3 output path. This document contains the pre-visit summary organized into clearly defined sections, with every clinical statement linked back to its supporting evidence.

### Summary sections
<a name="pi-output-sections"></a>

The following tree shows the structure of the output schema:

```
PatientSummaries[] (array)
└── PatientSummary
    ├── JobId
    ├── SummaryType (e.g., "Pre-visit")
    ├── PatientId
    ├── GeneratedAt (ISO 8601 timestamp)
    └── Sections[] (array)
        ├── SectionName
        └── ClinicalNarrative[] (array)
            ├── Text (clinical content with markdown formatting)
            └── Evidence[] (array of FHIR resource references)
TotalCount
GeneratedAt (ISO 8601 timestamp)
HccIncluded (boolean)
```

The pre-visit summary is organized into five sections:


| Section | What it contains | 
| --- | --- | 
| PATIENT\_AND\_ENCOUNTER\_OVERVIEW | Medical history, active conditions, current medications, allergies, past surgeries, and family history. | 
| SINCE\_LAST\_VISIT | New labs, specialist notes, medication changes, symptoms, and interventions that have occurred since the patient’s last encounter with this provider. | 
| TRENDS | Patterns over time for key clinical metrics such as A1c, blood pressure, weight, and lab values. | 
| CMS\_HCC\_CODING\_ANALYSIS | Conditions previously documented that are relevant to CMS Hierarchical Condition Category (HCC) risk adjustment. The clinician confirms whether each condition is still present. | 
| HHS\_HCC\_CODING\_ANALYSIS | Conditions previously documented that are relevant to HHS-HCC risk adjustment. The clinician confirms whether each condition is still present. | 

Each section contains an array of clinical narrative objects. A clinical narrative is a discrete unit of clinical content that the service generates from the patient’s data. The text within clinical narratives might include markdown formatting (such as bullet markers, headers, and emphasis) that your application can parse and render according to your display context.

The first three sections answer the questions clinicians typically need answered before walking into the exam room: Who is this patient? What’s happened since I last saw them? How have things changed? The final two sections support Condition Review, which helps organizations capture appropriate revenue across both Fee-for-Service and Value-Based Care models. These sections surface previously documented conditions that carry HCC risk adjustment weight, along with the date each condition was last assessed and a prompt to confirm whether the condition is still clinically present. The CMS and HHS sections might surface overlapping conditions where both risk adjustment models apply, or might surface different conditions depending on each model’s category definitions.

### Evidence references
<a name="pi-evidence-references"></a>

Every clinical narrative in the summary includes an evidence array that links the generated statement back to the specific FHIR resources or source documents that support it. Evidence references use the format `ResourceType/ResourceId`, such as `Condition/d68e8fc6-2e5f-4a3e-a2a7-942a435e78ec`.

Structural elements such as section headers or summary statements that synthesize across multiple sources might have an empty evidence array. Clinical statements derived from specific patient data — a particular lab result, a documented allergy, a past encounter, a previously assessed condition — include the corresponding FHIR resource references.

### HccIncluded flag
<a name="pi-hcc-included-flag"></a>

The output includes a top-level `HccIncluded` flag indicating whether the Condition Review sections (CMS and HHS HCC Coding Analysis) were generated for the job.

## Rendering the summary
<a name="pi-rendering"></a>

To present the summary to clinicians in your application:

1. Iterate through each section in order.

1. Concatenate the text values from each clinical narrative within the section.

1. Parse the markdown formatting for your display context.

1. Use the evidence references to provide drill-down links to source FHIR resources or documents.

For the Condition Review sections, render each surfaced condition as an interactive element that allows the clinician to confirm, dismiss, or annotate each condition directly within the workflow. The structured output format gives you full control over how the summary is rendered.

For complete API parameter details and request/response schemas, see the [Amazon Connect Health API Reference](https://docs.aws.amazon.com/connecthealth/latest/APIReference/Welcome.html).