# Data Transformation features

Each feature below is documented with what it is, how it works, differences between
C-CDA and CSV sources, and when to use it.

- [Transformation profiles and versioning](#data-transformation-profiles "#data-transformation-profiles")
- [Data Transformation AI agent](#data-transformation-ai-agent "#data-transformation-ai-agent")
- [Synchronous (real-time) transform and preview](#data-transformation-sync "#data-transformation-sync")
- [Bulk (asynchronous) transformation jobs](#data-transformation-bulk-jobs "#data-transformation-bulk-jobs")
- [Validation](#data-transformation-validation "#data-transformation-validation")
- [OID-to-URI mapping](#data-transformation-oid-mapping "#data-transformation-oid-mapping")
- [Provenance](#data-transformation-provenance "#data-transformation-provenance")
- [Drift detection](#data-transformation-drift-detection "#data-transformation-drift-detection")
- [MCP access](#data-transformation-mcp "#data-transformation-mcp")

## Transformation profiles and versioning

A transformation profile is the reusable definition of how a source format converts to
FHIR R4. It holds the conversion logic (Velocity templates for C-CDA, a YAML mapping
configuration for CSV) and is created once and reused across all datastores and
transformation jobs in your account. Separating the definition (profile) from the
execution (job) means you author and test a conversion once, then apply the same published
version to any number of jobs.

### Creating a profile

You create a profile in one of three ways:

- From a starter or base profile: start from a working profile rather
  than a blank one. For C-CDA, the AWS Starter Profile is a prebuilt,
  AWS-defined profile that handles common C-CDA document formats out of the box.
  For CSV, you provide sample files in Amazon S3 when creating the profile, then
  invoke the AI agent to analyze them and generate a YAML mapping
  configuration.
- By cloning: clone any existing profile as the starting point for a
  new one.
- From a raw mapping: supply Velocity templates (C-CDA) or a YAML
  mapping (CSV) directly. This is the path for deploying version-controlled
  profiles through a CI/CD pipeline (see [Getting started with the SDK and AWS CLI](data-transformation-getting-started-cli.md "data-transformation-getting-started-cli.md")).

###### Important

Creating a CSV profile with SampleData registers the sample location but does
not run the AI agent. To generate the YAML mapping, you must call
UpdateProfileWithAgent after creation. The agent analyzes your sample files at
that point and produces the base profile.

### The version lifecycle

A profile can have at most one draft and up to 99 published versions:

- A new profile begins as a draft (version 0): a mutable working copy
  you can edit freely.
- Publishing the draft creates an immutable, numbered version (v1, v2, and so
  on, up to v99). Published versions never change.
- Transformation jobs always run against the latest published version. Because
  the draft is separate, you can keep editing while production jobs continue to
  run against the last published version: in-progress edits never affect
  running conversions.
- A profile with a published version and newer unpublished edits is in an
  unpublished-changes state; the published version stays live until you publish
  again.

### Comparing and rolling back

Because every published version is retained, you can see exactly how the conversion
logic changed over the version history. Rolling back does not delete anything:
it creates a new version from a previous snapshot, so the full history and audit trail
are preserved.

### When to use versioning

Publish a version before running a production job so the job is pinned to reviewed
logic. Use rollback when a change produces unexpected output, and compare to confirm
what a change actually altered.

## Data Transformation AI agent

The Data Transformation AI agent removes the manual effort of authoring and maintaining FHIR
mappings. Instead of writing conversion logic by hand, you describe the outcome you want
and the agent produces or updates the underlying logic: Velocity templates for
C-CDA, a YAML mapping configuration for CSV. The agent is embedded in the profile editor
in the AWS Management Console and is also available through the UpdateProfileWithAgent API and as an MCP
tool, so you can work with it from the AWS Management Console, from code, or from an MCP-compatible
IDE.

### What the agent does

- Generates conversion logic from your data. For CSV, the agent analyzes
  sample files you provided at profile creation and produces a base profile
  : inferring the target FHIR resources and fields, so you begin from a
  working draft rather than a blank profile. For C-CDA, it tailors the AWS
  Starter Profile to your documents.
- Edits conversion logic from natural language. Describe a change in plain
  language and the agent updates the underlying template or mapping. For
  example:

  - "Add a mapping for the Medication resource."
  - "Map the patient's preferred language from the
    languageCommunication section."
  - "Set the default state to Washington for Patient
    resources."
  - "Map the RACE\_CD column to a FHIR
    extension."
  - "Skip records where status is
    entered-in-error."

- Explains and reviews before applying. The agent presents the proposed change
  as a diff of the affected template or mapping for you to review, and applies
  it only after you accept. Nothing changes silently on the published profile,
  the agent only makes changes to the draft version.
- Refines iteratively. Work with the agent across multiple turns to adjust a
  mapping until the converted output is correct, previewing results against
  sample data between turn with the sync transform API.

### C-CDA workflow (Velocity templates)

The agent edits the Velocity templates that define how C-CDA sections map to FHIR
resources. Ask it to add a resource mapping, change how a section is interpreted, set
default values, or handle a document variation, and it updates the templates and
returns a diff. You preview the conversion against sample C-CDA documents before
publishing.

### CSV workflow (YAML mapping)

When you create a CSV profile with sample files and then invoke the agent, it
analyzes the headers, sample values, and data patterns from your files, then proposes
a YAML mapping configuration that includes:

- column-to-FHIR field mappings,
- date-format detection and reformatting to FHIR date/time formats,
- value translations (for example, M → male, INPATIENT →
  IMP),
- primary/foreign-key relationships between tables,
- aggregation rules that fold child-table rows into FHIR arrays on the
  parent resource,
- any assumptions the agent made and any questions it has about your
  data.

You accept, reject, or refine each proposed mapping, and can ask the agent for
further adjustments. The agent infers the mapping from a sample of your files rather
than the full dataset, so provide samples that are representative of your data and
review the proposed mapping before converting at scale.

### Inputs the agent accepts

You can communicate with the agent in natural language inputs. Some combinations
include:

- instructions,
- sample source data (C-CDA sections or CSV schemas),
- schema documentation,
- FHIR validation errors from a previous conversion.

### Manual editing

You are not required to use the agent. You can edit Velocity templates and YAML
mappings directly at any point, and mix manual edits with agent-authored changes on the
same profile.

## Synchronous (real-time) transform and preview

Synchronous transform converts a single input and returns the FHIR result
immediately, rather than running an asynchronous job over Amazon S3. It exists for two
purposes: testing a profile while you author it, and running small, interactive
transformations in a request/response flow.

### How it works

- You submit one input (a C-CDA document or a set of CSV files) against a
  profile and receive the converted FHIR resources as a FHIR Bundle in the
  response.
- The operation is available through the REST API only: it is not
  exposed as an AWS CLI or SDK command. See [Accessing Data Transformation Agent](data-transformation.md#data-transformation-accessing "data-transformation.md#data-transformation-accessing").
- You can enable drift detection on a sync call by setting
  DriftDetectionEnabled to true to see, in the response, which source elements a
  profile does not yet capture: useful while iterating on a
  mapping.

### Size limits

Synchronous transform accepts C-CDA inputs up to 1 MB and combined CSV inputs up to
1 MB per request. For larger datasets, use a bulk transformation job.

### Preview in the AWS Management Console

When authoring a profile in the AWS Management Console, synchronous transform powers the live
preview: you see the source on one side and the converted FHIR output on the other,
and the preview updates as you refine the mapping. Use it to confirm output is correct
before publishing.

### When to use sync vs. bulk

Use synchronous transform to validate a profile against representative documents
and for latency-sensitive, per-request conversions, such as a live feed that converts
documents as they arrive. Use a bulk transformation job (below) for large datasets and
for ingesting directly into a HealthLake datastore.

## Bulk (asynchronous) transformation jobs

A bulk transformation job converts a large dataset from Amazon S3 using a published
profile, running asynchronously while you monitor progress. This is the production path
for migrations and for loading data into a HealthLake datastore. Please refer to
[this
page](getting-started-setting-up.md "getting-started-setting-up.md") for IAM permissions setup.

### How it works

- Point a job at an Amazon S3 prefix of source files, choose a published profile,
  and choose an output destination. The job scans the input, converts each file
  (C-CDA) or set of rows (CSV), and writes the results.
- There is no infrastructure to provision: the job scales
  automatically.

### Output modes

- Standalone: write converted FHIR to an Amazon S3 location. Use
  the StartDataTransformationJob API.
- Composite (convert and ingest): convert source files and ingest the
  resulting FHIR resources directly into a HealthLake datastore in a single
  step, so the data is immediately queryable. Use the StartFHIRImportJob API
  with the ProfileId, InputFormat, and optionally DriftDetectionEnabled
  parameters. The datastore must be in ACTIVE state. See Step 7: Convert
  and ingest into a HealthLake datastore for a complete example.

### Graceful failure handling

Malformed inputs are skipped and logged rather than failing the batch, so a single
bad file never stops a large job. Failed inputs are written as JSON error files with
the input file path and error message, so you can review and reprocess them.

### Output layout

The service creates a job-scoped folder under your output Amazon S3 URI using the job ID.
Inside that folder:

- converted/: FHIR NDJSON output files (one per input file, e.g.,
  converted/patient-record.ndjson).
- ERROR/: error detail for failed inputs (JSON files with inputFile
  and errorMessage fields, e.g., ERROR/bad-file.json).
- Manifest.json: job summary with aggregate metrics (files scanned,
  converted, failed, resources generated).
- jobLevelDriftResult.json: the aggregate drift report for the job, if
  drift detection was enabled.
- driftDetectionPerFileResults/: for C-CDA jobs with drift detection
  enabled, per-file drift reports (e.g.,
  driftDetectionPerFileResults/patient-record\_driftMetrics.json), so you can
  inspect coverage for an individual source file rather than only the job-level
  aggregate.

### Monitoring

Track a running job through the AWS Management Console job detail page or the
DescribeDataTransformationJob API: status, files processed (rows for CSV), resources
generated, and failures. Job metrics and logs are also available in Amazon
CloudWatch.

## Validation

Data Transformation Agent validates at multiple points in the conversion lifecycle, so problems are caught
before they become failed conversions or non-compliant output.

- Source validation: checks that C-CDA inputs are well-formed and conform
  to the C-CDA specification. Errors include location details and remediation
  guidance, so you can fix source problems before running a large job. The
  ValidateSource operation is available through the REST API to screen inputs up
  front.
- Template / mapping validation: validates a profile's Velocity templates
  (C-CDA) or YAML mapping (CSV) independently of any data, so you can confirm the
  conversion logic is well-formed before publishing or running a job.
- Output FHIR validation: checks that generated resources conform to
  FHIR R4, so downstream FHIR APIs and datastores accept the output.

Together these mean a job fails less often for avoidable reasons: source validation
catches bad inputs, mapping validation catches bad logic, and output validation confirms
the result is standards-compliant.

## OID-to-URI mapping

C-CDA documents identify code systems using OIDs (Object Identifiers): legacy
numeric identifiers such as `2.16.840.1.113883.6.1` (LOINC). FHIR expects
modern system URIs such as `http://loinc.org`. If OIDs are carried through
unmapped, the resulting system values are not interoperable and downstream FHIR tooling
cannot resolve the codes. Data Transformation Agent maps between them during conversion.

- **Pre-built mappings**: mappings for
  common healthcare OIDs (for example, LOINC, SNOMED CT, ICD-10, RxNorm) are
  applied automatically, with no configuration.
- **Custom mappings**: add your own
  OID-to-URI mappings for code systems specific to your sources, so proprietary
  or local systems resolve correctly.

This applies to C-CDA sources, where OIDs are the native way code systems are identified.

## Provenance

Regulated healthcare workflows need to answer "where did this data come from, and how
was it produced?" for any resource. When provenance is enabled on a job, Data Transformation Agent generates
a FHIR Provenance resource for every conversion, giving each output resource a
complete, queryable lineage back to its source.

### The provenance chain

Provenance → DocumentReference → source file. The Provenance resource
references a DocumentReference, which records the source file's Amazon S3 URI and a
SHA-1 checksum. The checksum lets you prove the output was derived from a specific,
unaltered source file. A Device resource representing AWS HealthLake Data
Transformation as an entity is also provided should that information be necessary.

### Record-level locators

Provenance resolves not just to the source file but to the exact location within
it, and the locator differs by source format:

- **C-CDA**: an XPath pointing to the
  source element the resource was derived from.
- **CSV**: the table name, primary
  key, and row number of the source record.

### Captured fields

Each Provenance resource records the source file URI and checksum, the profile
version used for the conversion, a timestamp, and the record-level locator.

### Conformance and use

Provenance resources conform to the US Core Provenance profile, so they
interoperate with US Core-aware tooling. Enable provenance when you need
auditability for compliance, or when you need to trace a questionable output
resource back to the exact source element that produced it. Provenance is enabled
by default; set ProvenanceEnabled to false to disable it.

## Drift detection

A conversion can succeed while silently dropping source data a profile does not yet map.
Drift detection surfaces that gap. It is a report: when enabled, it compares what the
source contains against what the profile actually produced, and records what was left
behind.

### What the report contains

- The overall coverage rate for the conversion.
- A ranked list of unmapped source sections and elements, so you can
  prioritize the highest-impact gaps.
- Any expected resources that were not produced.
- Full traceability back to the source file and element location (file
  name and OID for C-CDA, row for CSV).

### How to use drift detection

Drift detection is available in both conversion modes, so you can use it whether
you are iterating on a single file or validating a full dataset:

- Sync (real-time): set DriftDetectionEnabled to true on a
  TransformData request to run drift detection on a single file and get the
  results back in the API response. This is the fastest way to check coverage
  while you author a profile: convert one representative document, see exactly
  what the profile missed, refine the mapping, and try again.
- Bulk (asynchronous): enable drift detection on a transformation
  job to measure coverage across the whole dataset. The report is written as
  jobLevelDriftResult.json in the job's Amazon S3 output location. For C-CDA jobs,
  per-file drift reports are also written under the
  driftDetectionPerFileResults/ folder, so you can pinpoint coverage gaps in
  an individual source file.

## MCP access

The Model Context Protocol (MCP) exposes Data Transformation Agent to IDE-based AI agents as callable tools,
so a developer can author profiles, run conversions, and investigate failures from an
assistant in their IDE: without switching to the AWS Management Console.

- Profile and job management APIs: all Data Transformation Agent profile and job management
  APIs are available as MCP tools, so you can create, edit, publish, and run jobs
  from any MCP-compatible client.
- Any MCP client: works with MCP-compatible IDEs and assistants,
  including Kiro and Cursor.
- Durable sessions: supports multi-turn sessions, so a debugging or
  authoring conversation holds context.

###### Note

The sync conversion operation (TransformData) and source validation
(ValidateSource) are REST-only and may not appear as MCP tools. Your agent can
construct and execute the REST calls on your behalf: see Step 3: Test
with sync conversion for the request format.

Because MCP shares the same API surface as the AWS CLI and SDKs for profile and job
operations, there is no capability gap for those workflows between working in your IDE
and working through code or the AWS Management Console. See [Getting started with MCP](data-transformation-getting-started-mcp.md "data-transformation-getting-started-mcp.md") for setup and an
example workflow.
