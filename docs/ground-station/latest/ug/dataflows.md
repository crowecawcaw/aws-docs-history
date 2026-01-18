# Use cross-region data delivery

The AWS Ground Station cross-region data delivery feature gives you the flexibility to send your data from an
antenna to any AWS Ground Station supported AWS Region. This means you can maintain your infrastructure in a
single AWS Region and schedule contacts on any
[AWS Ground Station Locations](aws-ground-station-antenna-locations.md "aws-ground-station-antenna-locations.md")
you are onboarded to.

When receiving your contact data in an Amazon S3 Bucket, AWS Ground Station will manage all delivery aspects for you.

To use cross-region data delivery to an Amazon EC2 instance (using either the AWS Ground Station Agent or a dataflow endpoint),
the _dataflow-endpoint_
must be created in your current AWS Region and your
_dataflow-endpoint-config_
must specify the same region. AWS Ground Station will manage delivering the data cross-region for you.
