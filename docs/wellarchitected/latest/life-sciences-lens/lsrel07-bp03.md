# LSREL07-BP03 Use staged validation and data quarantine

mechanisms

Introduce controlled validation stages where data is quarantined
before being processed further. Apply automated rules for schema
conformity, metadata completeness, and domain-specific plausibility
(for example, genomic variants outside biological ranges). Only data
that passes validation and adherence data standards (such as CDISC
or FHIR) proceeds. Isolate data that fails for human review, with
full audit trails to support regulatory adherence.

**Desired outcome:** Only data that
meets predefined quality and plausibility criteria enters production
pipelines, while problematic data is isolated for review.

**Common anti-patterns:**

- Directly processing incoming data without validation.
- Overlooking schema, metadata, or biological plausibility checks.
- Mixing invalid data with production datasets, causing downstream
  corruption.

**Benefits of establishing this best
practice:**

- Stops invalid datasets from contaminating results.
- Accelerates regulatory reviews by providing traceable validation
  evidence.
- Improves scientific trust by verifying that only high-quality
  data enters analysis.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data pipelines should incorporate a quarantine stage where
incoming data is validated before processing. Automated rules must
check for schema adherence, metadata completeness, and
instrument-specific error patterns. Apply domain-specific rules,
such as filtering out biologically implausible values in clinical
data. Flag and isolate quarantined data, with human review
workflows for resolution.

### Implementation steps

1. Ingest new datasets into a quarantine Amazon S3 bucket with
   tagging enabled to indicate that data is pending validation.
2. Use AWS Glue or AWS Lambda to validate schema, metadata, and
   plausibility.
3. Store failed validation results in Amazon DynamoDB or
   OpenSearch for investigation, and configure notifications
   through Amazon SNS to alert data stewards.
4. Only validated data should be transitioned into production
   pipelines using S3 lifecycle policies or Step Functions
   orchestration.
