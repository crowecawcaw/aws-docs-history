# LSOPS07-BP02 Isolate GxP data from non-GxP

data

Take steps to isolate and segment GxP data from non-GxP data. In
conjunction with the recommendations around data discovery and
classification, separate GxP data so the organization can implement
the necessary technical and administrative controls.

**Desired outcome:** Demonstrable
division between GxP and non-GxP data.

**Common anti-patterns:**

- Granting access at a workload level grants access to the data,
  GxP and non-GxP.
- Retaining logs that are adjacent to GxP relevant metadata.
- Including GxP data in logs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Incorporate system separation, including table and row-level
access controls.

### Implementation steps

1. Foster system separation though architecture design and
   deployment.  Create distinct datastores (like Amazon S3 and
   Amazon RDS) for GxP data.
2. Implement table and row-level access controls through
   application logic.
3. Apply AWS Lake Formation rules for consistent control to
   data sets.
4. Produce evidence of verification of access controls.

## Resources

**Related tools:**

- [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/")
- [AWS Lake Formation](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
