# Assessing automated sensitive data discovery coverage

As automated sensitive data discovery progresses for your account or organization, Amazon Macie provides statistics and
details to help you assess and monitor its coverage of your Amazon Simple Storage Service (Amazon S3) data estate. With this
data, you can check the status of automated sensitive data discovery for your data estate overall and individual S3
buckets within it. You can also identify issues that prevented Macie from analyzing objects in
specific buckets. If you remediate the issues, you can increase coverage of your Amazon S3 data during
subsequent analysis cycles.

Coverage data provides a snapshot of the current status of automated sensitive data discovery for your S3 general
purpose buckets in the current AWS Region. If you're the Macie administrator for an organization, this
includes buckets that your member accounts own. For each bucket, the data indicates whether issues
occurred when Macie attempted to analyze objects in the bucket. If issues occurred, the data
indicates the nature of each issue and, in certain cases, the number of occurrences. The data is
updated as automated sensitive data discovery progresses each day. If Macie analyzes or attempts to analyze one or more
objects in a bucket during a daily analysis cycle, Macie updates coverage and other data to
reflect the results.

For certain types of issues, you can review the data in aggregate for all of your S3 general
purpose buckets and optionally drill down for additional details about each bucket. For example,
coverage data can help you quickly identify all the buckets that Macie isn't allowed to access for
your account. Coverage data also reports object-level issues that occurred. These issues, referred
to as _classification errors_, prevented Macie from analyzing
specific objects in a bucket. For example, you can determine how many objects Macie couldn't
analyze in a bucket because the objects are encrypted with an AWS Key Management Service (AWS KMS) key that's no
longer available.

If you use the Amazon Macie console to review coverage data, your view of the data includes
guidance for remediating each type of issue. Subsequent topics in this section also provide
remediation guidance for each type.

###### Topics

- [Reviewing coverage data](discovery-coverage-review.md "discovery-coverage-review.md")
- [Remediating coverage
  issues](discovery-coverage-remediate.md "discovery-coverage-remediate.md")
