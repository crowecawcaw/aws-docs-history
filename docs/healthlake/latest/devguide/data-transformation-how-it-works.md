

# How Data Transformation Agent works
<a name="data-transformation-how-it-works"></a>

The following terms and concepts are essential for working with the AWS HealthLake Data Transformation Agent.
+ [Transformation profile](#data-transformation-how-it-works-profile)
+ [Transformation job](#data-transformation-how-it-works-job)
+ [Data Transformation AI agent](#data-transformation-how-it-works-agent)

## Transformation profile
<a name="data-transformation-how-it-works-profile"></a>

A transformation profile is the reusable, versioned definition of how source data converts to FHIR R4. You create a profile once and reuse it across all datastores and jobs in your account.
+ For C-CDA, a profile contains Velocity templates.
+ For CSV, a profile contains a YAML mapping configuration.

![Diagram showing the transformation profile lifecycle from draft to published versions.](http://docs.aws.amazon.com/healthlake/latest/devguide/images/profile_lifecycle_diagram.png)

+ A draft (version 0) is a mutable working copy you can edit freely.
+ Publishing creates an immutable, numbered version (v1, v2, ...).
+ Transformation jobs always use the profile's latest published version, so in-progress draft edits never affect in-progress transformations.
+ Rollback returns to any previous version by creating a new version that preserves the full audit trail.
+ Cloning creates a new profile from any existing version, giving you a separate profile to modify without affecting the original.

## Transformation job
<a name="data-transformation-how-it-works-job"></a>

A transformation job is an execution that applies a published profile to your data.

Data Transformation Agent offers two run modes:
+ Sync (real-time): convert a single input and get FHIR back immediately. Used for testing a profile and for real-time, per-request conversions.
+ Bulk (asynchronous): convert large datasets from Amazon Amazon S3 at scale.

Sync conversions return the converted FHIR resources as a FHIR Bundle in the API response. Bulk transformation jobs return FHIR resources in one of two locations:
+ Amazon S3: write FHIR NDJSON to an Amazon Amazon S3 location.
+ HealthLake: convert and ingest FHIR resources directly into a HealthLake datastore.

## Data Transformation AI agent
<a name="data-transformation-how-it-works-agent"></a>

Data Transformation AI agent authors and edits a profile's conversion logic.
+ For C-CDA, it edits Velocity templates from natural language instructions.
+ For CSV, it analyzes sample files to produce a YAML configuration with column-to-FHIR field mappings, date and value translations, primary/foreign-key relationships, and aggregation rules, flagging anything that needs review.

You can interact with the agent through natural language including any of the following combinations: instructions, FHIR validation errors, schema documentation, and sample data. You can also edit profiles manually.