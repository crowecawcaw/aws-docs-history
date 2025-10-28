# DRHCSEC08-BP01 Implement backups to enable recovery from data corruption and data deletion, as well as point-in-time views of data

Configure backups to be taken automatically based on a periodic
schedule informed by the Recovery Point Objective (RPO), or by
changes in the dataset. Critical datasets with low data loss
requirements need to be backed up automatically on a frequent
basis, whereas less critical data where some loss is acceptable
can be backed up less frequently.

**Desired outcome:** Successful
periodic test results of ability to recover data.

**Common anti-patterns:**

- Failing to fully test if your data backup and recovery
  procedures are functional

**Benefits of establishing this best
practice:** Helps you detect and fix backup and recovery
misconfigurations if they occur. 

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

- Configure Amazon EBS snapshots. If your compliance
  requirements allow backups to be stored in-Region, that can
  be a lower cost option. Otherwise, configure Amazon EBS
  local snapshots on Outposts, or implement a third-party
  backup solution.
  1.  For implementations details, see
      [Amazon Elastic Block Store Local Snapshots on AWS Outposts](https://aws.amazon.com/blogs/aws/new-amazon-elastic-block-store-local-snapshots-on-aws-outposts/ "https://aws.amazon.com/blogs/aws/new-amazon-elastic-block-store-local-snapshots-on-aws-outposts/") and
      [Amazon EBS local snapshots on Outposts](../../../ebs/latest/userguide/snapshots-outposts.md "../../../ebs/latest/userguide/snapshots-outposts.md").

- Enable
  [S3
  Versioning on Outposts](../../../AmazonS3/latest/userguide/S3OutpostsManagingVersioning.md "../../../AmazonS3/latest/userguide/S3OutpostsManagingVersioning.md") to preserve, retrieve, and
  restore every version of every object stored in your S3
  buckets on Outposts.
- Enable
  [S3
  Replication on Outposts](../../../AmazonS3/latest/userguide/S3OutpostsReplication.md "../../../AmazonS3/latest/userguide/S3OutpostsReplication.md") to replicate the Amazon S3
  objects to another Outpost or even another bucket on the
  same Outpost. If copies of data may be stored in-Region,
  then configure
  [AWS Datasync](https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/ "https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/") to replicate the data to the S3 bucket in
  the Region.
- Perform capacity planning, and periodically review your
  plans to reduce risk of running out of capacity within S3
  Outposts.
- Third-party backup solutions are available from
  [AWS Partners who have tested their solutions on Outposts](https://partners.amazonaws.com/search/partners/?facets=Product%20%3A%20AWS%20Outposts&keyword=Backup&page=1 "https://partners.amazonaws.com/search/partners/?facets=Product%20%3A%20AWS%20Outposts&keyword=Backup&page=1").
- Periodically test your ability to fully recover data,
  including from specific points in time.

## Resources

**Related best practices:**

- [REL09-BP03
  Perform data backup automatically](../reliability-pillar/rel_backing_up_data_automated_backups_data.md "../reliability-pillar/rel_backing_up_data_automated_backups_data.md")
- [Incident
  Response](../framework/a-incident-response.md "../framework/a-incident-response.md")
