# TELCOCOST04-BP01 Choose the appropriate type of storage for

network functions backups, metrics, KPIs and the event records to reduce costs

Telecom companies generate and store massive amounts of data to support their business and
customer operations. However, data is accessed or needed at various frequencies. By aligning
storage choices with data access needs and lifecycles, Telecoms can significantly reduce their
storage costs. For actively accessed data that needs high performance, flash storage or cache
are good options despite their higher costs. For medium-term data that is accessed occasionally,
lower-cost options like object storage, SAN or NAS storage are suitable. For long-term archive
data with infrequent access, cold storage options like tape or cloud archival storage are the
most cost-efficient.

**Desired outcome:**

- Align storage choices with the access patterns and retention requirements of different
  data types.
- Achieve cost savings by utilizing the most cost-effective storage options for each data
  category.
- Verify appropriate performance and durability characteristics for the various data
  workloads.

**Common anti-patterns:**

- One-size-fits-all storage approach, with the same storage solution used for each data
  type.
- Overreliance on high-cost storage options for data that does not require frequent
  access.
- Lack of visibility and control over storage usage and costs across the organization.

**Benefits of establishing this best practice:**

- Significant cost savings by optimizing storage costs based on data access patterns.
- Improved storage efficiency and resource utilization.
- Enhanced data management through appropriate retention and tiering strategies.
- Increased agility in responding to changing storage requirements.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Telecom companies generate and store large volumes of data to support their business and
customer operations. However, data is accessed or needed at different frequencies. By aligning
storage choices with data access needs and lifecycles, telecoms can significantly reduce their
storage costs.

For actively accessed data that needs high performance, flash storage or cache are good
options despite their higher costs. For medium-term data that is accessed occasionally,
lower-cost options like object storage, SAN, or NAS storage are suitable. For long-term
archive data with infrequent access, cold storage options like tape or cloud archival storage
are the most cost-efficient.

### Implementation steps

- Categorize your data based on access frequency, performance requirements, and
  retention needs (for example, active, medium-term, and long-term archive).
- For active data that requires high performance, use Amazon EBS Provisioned IOPS SSD
  volumes or Amazon EFS.
- For medium-term data that is accessed occasionally, use Amazon S3 Intelligent-Tiering or
  Amazon EFS.
- For long-term archive data with infrequent access, use Amazon Glacier or Amazon Glacier Deep
  Archive.
- Implement lifecycle policies to automatically transition data between storage tiers
  as access patterns change.
- Monitor storage usage and costs and adjust your storage tiering strategy as needed
  to optimize costs.

## Resources

**Key AWS services:**

- [Amazon EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/")
- [Amazon EFS](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/")
- [Amazon Glacier Deep Archive](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/")
