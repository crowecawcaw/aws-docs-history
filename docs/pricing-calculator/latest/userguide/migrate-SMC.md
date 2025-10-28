# Migrating Simple Monthly Calculator estimates to Pricing Calculator

###### Important

Simple Monthly Calculator (SMC) is no longer supported. You can convert your saved SMC estimates
to AWS Pricing Calculator using the steps outlined in this section. This conversion feature closes on December 31, 2023
at 11.59PM PST.

If you have existing SMC estimates, we recommend that you migrate to the AWS Pricing Calculator using the
conversion feature at your earliest convenience. If you don't need access to your saved SMC
estimates, no action is needed.

###### To convert your SMC estimate to an estimate compatible with AWS Pricing Calculator

1. Copy and paste your unique SMC estimate link into your browser. This link redirects you to the AWS Pricing Calculator
   website where you can view the status of your estimate conversion.
2. Generate an AWS Pricing Calculator migrated estimate link for your records. To do this, choose **Share**.

###### Note

If your SMC estimate failed to generate in AWS Pricing Calculator, choose **errors**
to see the reasons why the conversion failed.

## Differences between Simple Monthly Calculator and AWS Pricing Calculator estimates

There are several reasons why your SMC estimate and your AWS Pricing Calculator estimates don't match in total costs.

- **AWS Free Tier pricing**: The AWS Pricing Calculator doesn't account for Free Tier pricing in cost calculations.
- **Time period**: The AWS Pricing Calculator calculates using 730 hours in a month for cost calculations. This is based on the calculation, 365 days a year x 24 hours a day for 12 months a year.

### Services and features not supported by AWS Pricing Calculator

You might have Simple Monthly Calculator estimates saved previously that won't successfully migrate to AWS Pricing Calculator. This is because some services and features aren't supported in AWS Pricing Calculator at this time. The following table outlines what is currently not supported in AWS Pricing Calculator.

| Service name               | Pricing feature not supported in AWS Pricing Calculator                                       |
| -------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon EC2                 | Additional `T2/T3/T4g` Unlimited vCpu Hours Legacy Amazon EC2 instances and instance families |
| Amazon S3                  | Transfer acceleration Glacier select Cross region replication                                 |
| Amazon CloudFront          | HTTP requests Invalidation requests SSL certificates                                          |
| Amazon RDS                 | RDS Aurora Global Database                                                                    |
| Amazon DynamoDB            | Global tables                                                                                 |
| Amazon CloudWatch          | Archived logs Metric streams                                                                  |
| Amazon Redshift            | Previous generation node type                                                                 |
| Amazon Glacier             | Glacier select                                                                                |
| Amazon CloudSearch         | Entire service                                                                                |
| Amazon SimpleDB            | Entire service                                                                                |
| AWS Key Management Service | Customer managed keys (CMK) - multi Region                                                    | ###### Note You must generate new AWS Pricing Calculator sharable links if you make changes to your estimate. For more information, see [Sharing your estimate](save-share-estimate.md "save-share-estimate.md"). |
