# LSREL13-BP02 Monitor data integrity across scientific

processing pipelines

Implement monitoring specifically for data integrity across research
pipelines. Track errors such as checksum mismatches, validation
failures, or audit trail gaps. For scientific domains like genomics
or clinical processing, add plausibility checks to detect
biologically impossible or outlier results that may signal workflow
errors.

**Desired outcome:**

- Early detection of data corruption or processing errors.
- Continuous assurance of data accuracy, completeness, and
  traceability.
- Adherence to data integrity expectations for regulated research.

**Common anti-patterns:**

- Only validating data at ingestion or final outputs, not during
  processing.
- Ignoring intermediate pipeline results when monitoring for
  errors.
- Not capturing or preserving logs for data validation failures.

**Benefits of establishing this best
practice:**

- Protects reproducibility by keeping datasets accurate across
  processing steps.
- Reduces wasted compute from propagating corrupted or invalid
  data.
- Strengthens audit confidence through consistent integrity
  checks.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Incorporate integrity checks throughout pipelines. Validate the
following during this process:

- File checksums
- Schema conformance
- Expected data patterns

Retain metadata and logs for traceability. Define biologically
relevant plausibility thresholds (for example, variant frequencies
or image metrics) to detect anomalies early. Integrate alerts with
workflow orchestration so that failed steps are isolated.

### Implementation steps

1. Validate file integrity with Amazon S3 ETag checks or
   checksum verification jobs in AWS Lambda.
2. Store audit trails in Amazon DynamoDB or Amazon S3.
3. Use AWS Glue DataBrew or AWS Data Quality rules for schema
   and value checks.
4. Implement plausibility validations in genomics workflows
   through AWS HealthOmics Workflows.
5. Route alerts through Amazon EventBridge into incident
   response pipelines.
