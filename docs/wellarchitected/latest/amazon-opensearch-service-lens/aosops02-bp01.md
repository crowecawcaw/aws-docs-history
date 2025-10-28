# AOSOPS02-BP01 Establish a manual snapshot repository

Maintain control over your OpenSearch Service data by creating a
centralized manual snapshot repository.

**Level of risk exposed if this best practice
is not established**: Medium

**Desired outcome:** Complete control
and flexibility over OpenSearch Service domain data through centralized
manual snapshot management.

**Benefits of establishing this best
practice**: By establishing a manual snapshot repository,
you maintain full control over your OpenSearch Service data, which
helps you comply with regulatory requirements and data retention
policies. Additionally, you can simplify disaster recovery processes
by having a centralized repository for snapshots.

## Implementation guidance

Establishing a manual snapshot repository for stored snapshots in
OpenSearch Service enables full control over domain data, promotes
manual backup and recovery of indices and documents, and provides
a centralized location for storing copies of critical data, which
can be restored into multiple OpenSearch Service domains.

Amazon OpenSearch Service automatically creates hourly snapshots
of your indices within the same domain. However, these automatic
snapshots are not restorable across different domains.

If you rely solely on the automatic hourly snapshot, there's no
need to follow this recommendation. However, if you prefer to take
control of your snapshot schedule and have the flexibility to
restore them in other OpenSearch Service domains, then continue following
this best practice.

To implement this best practice, use an S3 bucket that exists in
the same AWS Region that hosts your OpenSearch Service domain. You also
need the necessary permissions to manage the S3 bucket and run
administrative commands in your OpenSearch Service domain.

### Implementation steps

To create an ISM policy for snapshots:

- **Understand snapshot
  types:** Familiarize yourself with the two
  available snapshot options in Amazon OpenSearch Service:
  _automatic_ and
  _manual_.
- **Set up manual snapshots:**
  If you choose to use manual snapshots:
  - Create an IAM role with the necessary permissions
  - Set up a custom Amazon S3 bucket for storing your
    snapshots
  - Register the S3 bucket in your OpenSearch Service domain
  - Test the repository by taking a manual snapshot and
    restoring it

- **Create an ISM policy:**
  Design and implement an ISM policy that captures snapshots
  of your most critical indices, storing them securely in your
  custom S3 bucket.

## Resources

- [Creating
  index snapshots in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md")
- [Registering
  a manual snapshot repository](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-registerdirectory "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-registerdirectory")
- [Take
  manual snapshots and restore in a different domain spanning
  across various Regions and accounts in Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/")
