# Viewing Configuration Snapshots in Amazon S3

bucket

A _configuration snapshot_ is a collection of the configuration
items for the supported resources that exist in your account. This configuration
snapshot is a complete picture of the resources that are being recorded and their
configurations. The configuration snapshot can be a useful tool for validating your
configuration. For example, you may want to examine the configuration snapshot regularly
for resources that are configured incorrectly or that potentially should not exist. The
configuration snapshot is available in multiple formats. You can have the configuration
snapshot delivered to an Amazon Simple Storage Service (Amazon S3) bucket that you specify. Additionally, you can
select a point in time in the AWS Config console and navigate through the snapshot of
configuration items using the relationships between the resources.

## Viewing Configuration

Snapshots

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the Amazon S3 console **All Buckets** list, choose the name
   of your Amazon S3 bucket.
3. Go through the nested folders in your bucket until you see the
   `ConfigSnapshot` object with a snapshot ID that
   matches with the ID returned by the command.
   Download
   and open the object to view the configuration snapshot..
   The S3 bucket also contains an empty file named
   `ConfigWritabilityCheckFile`. AWS Config creates this file
   to verify that the service can successfully write to the S3 bucket.
