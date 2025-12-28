# DRHCCOST04-BP01 Implement mechanisms to manage the lifecycle of Amazon S3 data, EBS volumes, and snapshots

Apply data lifecycle management practices to hybrid edge
environments.

**Desired outcome:** You can
implement familiar mechanisms like you would in-Region to manage
the lifecycle of your hybrid edge data.

**Benefits of establishing this best
practice:** Through the use of familiar mechanisms, you
can retain relevant data.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Outposts contain fixed capacity specific to their configuration.
You can manage the lifecycle of your data with familiar services
such as
[S3
Lifecycle](../../../AmazonS3/latest/s3-outposts/S3OutpostsLifecycleManaging.md "../../../AmazonS3/latest/s3-outposts/S3OutpostsLifecycleManaging.md") for Amazon S3 on Outposts and
[Data
Lifecycle Manager](https://aws.amazon.com/about-aws/whats-new/2021/02/introducing-amazon-ebs-local-snapshots-on-outposts/ "https://aws.amazon.com/about-aws/whats-new/2021/02/introducing-amazon-ebs-local-snapshots-on-outposts/") for Amazon EBS.
Consider [archiving
Amazon S3 content to AWS Regions using DataSync](https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/ "https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/") if
possible.
