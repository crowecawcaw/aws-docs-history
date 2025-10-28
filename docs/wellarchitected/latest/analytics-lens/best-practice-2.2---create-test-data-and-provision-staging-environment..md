# Best practice 2.2 – Create test data and provision staging environment

Using a known and unchanging dataset for test purposes helps
ensure that when changes are made to the analytics
environment or analytics application code, test results can
be compared to previous versions.

Confirming that the test datasets accurately represent
real-world data allows the analytics workload developer to
confirm the outcomes from the analytics job, as well as
comparing test results to previous versions.

Your organization should use a staging environment for user
access testing. Your organization should create logically separated AWS accounts for your development, test, staging, and production
environments depending upon your development standards.

For more details, refer to the following information:

AWS Whitepaper:
[Establishing
your best practice AWS environment](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md")

## Suggestion 2.2.1 – Use a curated dataset to test application logic and performance improvements

Analytics projects that are being developed should use the
same curated dataset to compare results between tests of
different versions of your code. Using the same dataset for
all tests allows demonstrating improvement over time, as
well as making it easier to recognize regressions in your
code.

To help control access to sensitive data, your
organization should use data masking techniques when
restoring development data to non-production environments.
More information on data minimization techniques can be
found in [Security](security.md "security.md").

For more details, refer to the following information:

- AWS Database Blog: [Data Masking using AWS DMS (AWS
  Data Migration Service)](https://aws.amazon.com/blogs/database/data-masking-using-aws-dms/ "https://aws.amazon.com/blogs/database/data-masking-using-aws-dms/")
- Amazon Redshift Data Masking: [Dynamic data masking
  (DDM) in Amazon Redshift](../../../redshift/latest/dg/t_ddm.md "../../../redshift/latest/dg/t_ddm.md")

## Suggestion 2.2.2 – Use a random sample of recent data to validate application edge cases and help ensure that regressions have not been introduced

Use a statistically valid random sample of recent data to
confirm that the analytics solution continues to perform
under real-world conditions. Using a sample of recent data
also allows you to recognize whether your dataset
characteristics have shifted, or whether anomalous data
has recently been introduced to your data.

For more information, see the AWS Machine Learning Blog: [Create random and stratified samples of data with Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/create-random-and-stratified-samples-of-data-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/create-random-and-stratified-samples-of-data-with-amazon-sagemaker-data-wrangler/").
