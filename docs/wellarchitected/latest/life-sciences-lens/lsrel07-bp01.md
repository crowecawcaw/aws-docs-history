# LSREL07-BP01 Implement system-wide data checksums and transfer

validation

Incorporate integrity verification at every transfer and
transformation stage. Use cryptographic checksums (like SHA-256 or
MD5) or ETags to validate files when moved into or across the cloud.
Use managed services like AWS DataSync or Amazon S3 replication that
perform integrity checks automatically. For domain-specific use
cases (like genomics and imaging), add plausibility checks to detect
biologically inconsistent results that may indicate processing
corruption.

**Desired outcome:** Data fidelity is
preserved during ingestion, transfer, and transformation, with
verifiable proof that data has not been altered.

**Common anti-patterns:**

- Moving data without checksum or hash verification.
- Relying solely on application logs to detect corruption.
- Using manual copy processes without automated validation.

**Benefits of establishing this best
practice:**

- Reduces risk of silent corruption during high-volume genomic or
  imaging transfers.
- Increases trust in research outputs by deriving results
  validated input data.
- Provides auditors and regulators with evidence of data integrity
  safeguards.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Integrate checksums and validation at every stage where data is
moved or transformed. Cryptographic checksums (such as SHA-256) or
S3 ETags provide automated validation during transfers into cloud
storage. Managed services like AWS DataSync, S3 Replication, and
S3 Transfer Acceleration perform integrity checks by default,
reducing operational burden. For scientific pipelines, augment
checksum validation with domain-specific checks, such as detecting
biologically implausible variants in genomic data or corrupt
slices in imaging data.

### Implementation steps

1. Data should be ingested into Amazon S3 where ETag-based
   validation confirms file integrity.
2. Use AWS DataSync for on-premises to cloud transfers,
   verifying that validation occurs automatically.
3. Configure S3 Replication with replication metrics enabled to
   verify data consistency across buckets.
4. For sensitive research workloads, embed integrity checks
   directly into processing pipelines (for example, validating
   SHA-256 digests before and after transformation).
