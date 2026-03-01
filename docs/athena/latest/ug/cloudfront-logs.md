# Query Amazon CloudFront logs

You can configure Amazon CloudFront CDN to export Web distribution access logs to Amazon Simple Storage Service. Use
these logs to explore users' surfing patterns across your web properties served by
CloudFront.

Before you begin querying the logs, enable Web distributions access log on your preferred
CloudFront distribution. For information, see [Access
logs](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md") in the _Amazon CloudFront Developer Guide_. Make a note
of the Amazon S3 bucket in which you save these logs.

###### Topics

- [Create a table for CloudFront standard logs (legacy)](create-cloudfront-table-standard-logs.md "create-cloudfront-table-standard-logs.md")
- [Create a table for CloudFront logs in Athena using manual partitioning with JSON](create-cloudfront-table-manual-json.md "create-cloudfront-table-manual-json.md")
- [Create a table for CloudFront logs in Athena using manual partitioning with Parquet](create-cloudfront-table-manual-parquet.md "create-cloudfront-table-manual-parquet.md")
- [Create a table for CloudFront logs in Athena using partition projection with JSON](create-cloudfront-table-partition-json.md "create-cloudfront-table-partition-json.md")
- [Create a table for CloudFront logs in Athena using partition projection with Parquet](create-cloudfront-table-partition-parquet.md "create-cloudfront-table-partition-parquet.md")
- [Create a table for CloudFront real-time logs](create-cloudfront-table-real-time-logs.md "create-cloudfront-table-real-time-logs.md")
- [Additional resources](cloudfront-logs-additional-resources.md "cloudfront-logs-additional-resources.md")
