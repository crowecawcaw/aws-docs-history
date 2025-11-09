# MIDASEC03-BP05 Implement data retention policies for each data class

Define and enforce data retention rules based on classification and regulatory
requirements to reduce storage costs and minimize compliance risks.

**Desired outcome:** Only required data is retained, improving
cost efficiency and reducing exposure of legacy data.

**Benefits of establishing this best practice:** Helps prevent
unnecessary storage costs, reduce audit complexity, and support lifecycle compliance.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use Amazon S3 lifecycle policies, AWS Glue table TTLs, and tagging strategies to
automate enforcement of retention policies.

### Implementation steps

- Define data retention durations based on classification and compliance needs.
- Apply tags and metadata to datasets to identify lifecycle requirements.
- Use S3 lifecycle rules or Glue jobs to delete or archive data.
- Regularly review and update retention policies based on changing regulations.

## Resources

- [Managing your storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md")
- [AWS Glue Documentation](../../../glue/index.md "../../../glue/index.md")
