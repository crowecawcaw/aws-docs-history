# LSPERF01-BP03 Performance optimizations should validate data

integrity

Maintain rigorous data integrity controls while pursuing performance
optimizations. Implement checksums, audit trails, and validation
steps within high-performance workflows, which assists to avoid
compromising scientific accuracy and reproducibility by
performance-focused architectural decisions, particularly for
regulated or clinically-relevant research.

**Desired outcome:** Implement a
balanced system architecture that maintains rigorous data integrity
controls while achieving optimal performance, verifying that
scientific accuracy and reproducibility for regulated and clinically
relevant research.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Working backward from your research regulatory requirements,
balance performance with data integrity to achieve scientific
accuracy and regulatory adherence.

Implement validation at each processing stage using cryptographic
checksums (MD5/SHA-256) to verify data remains unaltered during
transfers, storing these checksums for future validation.

Establish comprehensive audit trails documenting transformations
with timestamps, parameters, and identity information—essential
for regulated research.

Design your architecture with strategically positioned automated
validation steps that detect anomalies without manual
intervention, maximizing integrity assurance while minimizing
performance impact.

For high-throughput workflows, deploy parallel validation
processes that run concurrently rather than sequentially.

Use Amazon S3 Object Lock for immutable storage, AWS CloudTrail
for audit logging, and AWS Config for monitoring.

With regulated data, incorporate digital signatures and version
control to maintain unalterable provenance records, improving both
speed and trustworthiness throughout your research workflows.

### Implementation steps

1. Implement AWS KMS for encryption of sensitive research data.
2. Configure Amazon S3 checksums for data integrity validation.
3. Deploy AWS CloudTrail for comprehensive audit logging.
4. Use Amazon EventBridge to monitor validation workflows.
5. Implement AWS Config for adherence to research standards.

## Resources

**Related tools:**

- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
