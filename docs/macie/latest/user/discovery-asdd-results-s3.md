# Reviewing automated sensitive data discovery results

If automated sensitive data discovery is enabled, Amazon Macie automatically generates and maintains additional
inventory data, statistics, and other information about the Amazon Simple Storage Service (Amazon S3) general purpose
buckets for your account. If you're the Macie administrator for an organization, by default this includes
S3 buckets that your member accounts own.

The additional information captures the results of automated sensitive data discovery activities that Macie has
performed thus far. It also supplements other information that Macie provides about your Amazon S3
data, such as public access and encryption settings for individual S3 buckets. In addition to
metadata and statistics, Macie produces records of the sensitive data it finds and the analysis
that it performs—_sensitive data findings_ and _sensitive data discovery results_.

As automated sensitive data discovery progresses each day, the following features and data can help you review and
evaluate the results:

- [Summary dashboard](discovery-asdd-results-s3-dashboard.md "discovery-asdd-results-s3-dashboard.md") – Provides aggregated
  statistics for your Amazon S3 data estate. The statistics include data for key metrics such as the
  total number of buckets that Macie has found sensitive data in, and how many of those buckets
  are publicly accessible. They also report issues that affect coverage of your Amazon S3 data.
- [S3
  buckets heat map](discovery-asdd-results-s3-inventory-map.md "discovery-asdd-results-s3-inventory-map.md") – Provides an interactive, visual
  representation of data sensitivity across your data estate, grouped by AWS account. For each
  account, the map includes aggregated sensitivity statistics and it uses colors to indicate the
  current sensitivity score for each bucket that the account owns. The map also uses symbols to help
  you identify buckets that are publicly accessible, can't be analyzed by Macie, and more.
- [S3 buckets table](discovery-asdd-results-s3-inventory-table.md "discovery-asdd-results-s3-inventory-table.md") – Provides summary
  information for each S3 bucket in your inventory. For each bucket, the table includes data such
  as the bucket's current sensitivity score, the number of objects that Macie can analyze in the
  bucket, and whether you configured any sensitive data discovery jobs to periodically analyze
  objects in the bucket. You can export data from the table to a comma-separated values (CSV)
  file.
- [S3 bucket details](discovery-asdd-results-s3-inventory-details.md "discovery-asdd-results-s3-inventory-details.md") – Provides detailed
  statistics and information about an S3 bucket. The details include a list of objects that Macie
  has analyzed in the bucket, and a breakdown of the types and number of occurrences of sensitive
  data that Macie has found in the bucket. These are in addition to details about settings that
  affect the security and privacy of the bucket’s data.
- [Sensitive data
  findings](discovery-asdd-results-s3-findings.md "discovery-asdd-results-s3-findings.md") – Provide detailed reports of sensitive data that Macie
  found in individual S3 objects. The details include when Macie found the sensitive data, and the
  types and number of occurrences of the sensitive data that Macie found. The details also include
  information about the affected S3 bucket and object, including the bucket's public access
  settings and when the object was most recently changed.
- [Sensitive data
  discovery results](discovery-asdd-results-s3-sddrs.md "discovery-asdd-results-s3-sddrs.md") – Provide records of the analysis that Macie
  performed for individual S3 objects. This includes objects that Macie doesn't find sensitive
  data in, and objects that Macie can't analyze due to issues or errors. If Macie finds sensitive
  data in an object, the sensitive data discovery result provides information about the sensitive data that Macie
  found.
  With this data, you can evaluate data sensitivity across your Amazon S3 data estate and drill down
  to evaluate and investigate individual S3 buckets and objects. Combined with information that
  Macie provides about the security and privacy of your Amazon S3 data, you can also identify cases where
  immediate remediation might be necessary—for example, a publicly accessible bucket that
  Macie found sensitive data in.

Additional data can help you assess and monitor coverage of your Amazon S3 data. With coverage
data, you can check the status of the analyses for your data estate overall and individual S3
buckets within it. You can also identify issues that prevented Macie from analyzing objects in
specific buckets. If you remediate the issues, you can increase coverage of your Amazon S3 data during
subsequent analysis cycles. For more information, see [Assessing automated sensitive data discovery coverage](discovery-coverage.md "discovery-coverage.md").

###### Topics

- [Reviewing data sensitivity statistics on
  the Summary dashboard](discovery-asdd-results-s3-dashboard.md "discovery-asdd-results-s3-dashboard.md")
- [Visualizing data sensitivity with the
  S3 buckets map](discovery-asdd-results-s3-inventory-map.md "discovery-asdd-results-s3-inventory-map.md")
- [Assessing data sensitivity with the
  S3 buckets table](discovery-asdd-results-s3-inventory-table.md "discovery-asdd-results-s3-inventory-table.md")
- [Reviewing data sensitivity details
  for S3 buckets](discovery-asdd-results-s3-inventory-details.md "discovery-asdd-results-s3-inventory-details.md")
- [Analyzing findings from automated sensitive data discovery](discovery-asdd-results-s3-findings.md "discovery-asdd-results-s3-findings.md")
- [Accessing discovery results from
  automated sensitive data discovery](discovery-asdd-results-s3-sddrs.md "discovery-asdd-results-s3-sddrs.md")
