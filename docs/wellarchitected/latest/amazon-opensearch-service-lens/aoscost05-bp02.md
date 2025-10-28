# AOSCOST05-BP02 Examine the costs associated with Amazon S3

storage for manually creating snapshots of your OpenSearch Service
domain

Improve cost awareness and inform backup strategy by examining Amazon S3
storage costs associated with manually creating snapshots of your
OpenSearch Service domain.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome**: You can estimate
costs by examining the costs associated with Amazon S3 storage for
manually creating snapshots of your OpenSearch Service domain.

**Benefits of establishing this best
practice:**

- **Cost awareness**: Examining the
  costs associated with Amazon S3 storage for manually creating
  snapshots of your OpenSearch Service domain helps you understand
  that backups can incur standard Amazon S3 usage charges.
- **Informed backup strategy**: By
  considering the cost of manual backups, you can choose the most
  suitable backup strategy for your needs, whether it's manual
  backups or using AWS services like Automated Backups or
  Snapshots in OpenSearch.

## Implementation guidance

If you take manual backups of your OpenSearch Service domain,
understand that the manual snapshots storing in Amazon S3 can
incur standard Amazon S3 usage charges. For detailed information
about the cost of the different storage tiers available in Amazon S3, see
[Amazon S3 pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4 "https://aws.amazon.com/s3/pricing/?nc=sn&loc=4").

## Resources

- [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4 "https://aws.amazon.com/s3/pricing/?nc=sn&loc=4")
- [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/#Free_tier "https://aws.amazon.com/opensearch-service/pricing/#Free_tier")
