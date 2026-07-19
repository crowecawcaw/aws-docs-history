# Getting started with the AWS Management Console

## Step 1: Navigate to Data Transformation Agent

1. Open the [AWS HealthLake console](https://console.aws.amazon.com/healthlake/ "https://console.aws.amazon.com/healthlake/").
2. On landing page, Click Get started, and choose Transform Data.
3. In the left navigation, under the Data Transformation Agent section, choose Profiles to manage profiles, or Jobs to run conversions.

## Step 2: Create a transformation profile

1. Choose Profiles in the left navigation and click on Create profile.
2. Choose the source format:

   - C-CDA: clinical XML documents (hospital records, discharge summaries, continuity-of-care documents).
   - CSV: tabular exports (data-warehouse extracts, EHR flat files, claims data).

3. Choose how to initialize the profile:

   - For C-CDA: start from the AWS Starter Profile (a prebuilt profile with common section-to-resource mappings).
   - For CSV: provide an Amazon S3 path to a folder containing representative CSV files. The AI agent analyzes your files and generates a base profile.

4. Enter a profile name and optional description.
5. Choose Create.

The profile is created in draft state (version 0): a mutable working copy you can edit freely.

## Step 3: Customize with the Data Transformation AI agent (optional)

For C-CDA profiles:

1. Open the profile and go to the edit view; the Data Transformation AI agent panel appears on the right.
2. Describe changes in natural language (for example, "Set default state to Washington for Patient resources").
3. The agent edits the Velocity templates.
4. Select the Test tab, paste your sample C-CDA and click Run test to preview the conversion.
5. Iterate until the output is correct.

For CSV profiles:

1. The agent analyzes your sample files and proposes a YAML mapping: column-to-FHIR mappings, date/value translations, PK/FK relationships, and aggregation rules.
2. Review each proposed mapping: accept, reject, or refine.
3. Ask for adjustments in natural language (for example, "Map the RACE\_CD column to a FHIR extension").
4. Preview conversion results in the test tab (source on the left, FHIR output on the right).

## Step 4: Publish the profile

1. When satisfied, choose Publish. This creates an immutable version.
2. Your draft remains editable. Bulk jobs always use the latest published version.

To roll back: choose a previous version and publish it again. This creates a new version from the prior snapshot: nothing is deleted.

## Step 5: Run a transformation job

1. In the left navigation under Data Transformation Agent, choose Jobs.
2. Choose Start new job.
3. Fill in Job details:

   - Job name: a descriptive name (appears in CloudWatch logs and metrics).
   - Description: optional.

4. Configure Transformation settings:

   - Data source format: C-CDA or CSV.
   - Transformation profile: choose a published profile (only published profiles with version ≥ 1 appear).
   - Output mode:

     - Amazon Amazon S3: write converted FHIR to an Amazon S3 location (standalone conversion).
     - AWS HealthLake: convert and ingest directly into a HealthLake datastore. If selected, choose the target HealthLake datastore (must be in ACTIVE state).

   - Provenance: enabled by default. Generates FHIR Provenance resources tracing output back to source. Disable only if provenance is not needed.
   - Drift detection: enabled by default. Produces a report showing unmapped source elements.

5. Configure Source data:

   - Amazon S3 source location: the Amazon S3 folder containing your source files (must include a prefix, not just a bucket name).
   - Data access role: the IAM role HealthLake assumes to read your source files and write output. See [Setting up](data-transformation-setting-up.md "data-transformation-setting-up.md") for the trust and permissions policies.

6. Configure Output configuration (if):

   - Output Amazon S3 URI: where to write converted output and job logs.
   - AWS KMS key: the AWS KMS key to encrypt output at rest (required).

7. Choose Create job.

## Step 6: Review results

1. The job detail page shows real-time progress: status, files processed (rows for CSV), FHIR resources generated, and failures.
2. When complete, navigate to the output Amazon S3 location. The service creates a job-scoped folder under your output URI using the job ID. Inside that folder:

   - converted/: FHIR NDJSON output files (one per input file, e.g., converted/patient-record.ndjson).
   - ERROR/: error detail for failed inputs (JSON files with inputFile and errorMessage fields, e.g., ERROR/bad-file.json).
   - Manifest.json: job summary with aggregate metrics (files scanned, converted, failed, resources generated).
   - jobLevelDriftResult.json: the aggregate drift report for the job (if drift detection was enabled).
   - driftDetectionPerFileResults/: per-file drift reports for C-CDA jobs (if drift detection was enabled), e.g., driftDetectionPerFileResults/patient-record\_driftMetrics.json.
