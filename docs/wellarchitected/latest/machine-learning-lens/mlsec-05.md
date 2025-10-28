# MLSEC-05: Protect sensitive data privacy

Protect sensitive data used in training against unintended
disclosure. Identify and classify the sensitive data. Handle the
sensitive data using strategies including: removing, masking,
tokenizing, and principal component analysis (PCA). Document
best governance practices for future reuse and references.

## Implementation plan

- **Use automated mechanisms to
  classify data where possible** - Use
  [automated
  sensitive data discovery in Amazon Macie](../../../macie/latest/user/discovery-asdd.md "../../../macie/latest/user/discovery-asdd.md") that
  provides continual, cost efficient, organization-wide
  visibility into where sensitive data resides across your
  Amazon S3 environment. Macie automatically and
  intelligently inspects your S3 buckets for sensitive data
  such as personally identifiable information (PII),
  financial data, and AWS credentials. Macie then builds and
  continuously maintains an interactive data map of the
  locations in Amazon S3 where your sensitive data resides,
  and provides a sensitivity score for each bucket.
- **Use tagging** – Tag
  resources and models that are made from sensitive elements
  to quickly differentiate between resources requiring
  protection and those that do not.
- **Encrypt sensitive data**

* Encrypt sensitive data using services such as
  [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"), the
  [AWS Encryption](../../../encryption-sdk/latest/developer-guide/getting-started.md "../../../encryption-sdk/latest/developer-guide/getting-started.md")
  [SDK](../../../encryption-sdk/latest/developer-guide/getting-started.md "../../../encryption-sdk/latest/developer-guide/getting-started.md"),
  or client-side encryption.

- **Reduce data sensitivity**

* Evaluate and identify data for anonymization or
  de-identification to reduce sensitivity.

## Documents

- [Running
  sensitive data discovery jobs in Amazon Macie](../../../macie/latest/user/discovery-jobs.md "../../../macie/latest/user/discovery-jobs.md")
- [Categorizing
  your storage using tags](../../../AmazonS3/latest/userguide/object-tagging.md "../../../AmazonS3/latest/userguide/object-tagging.md")
- [AWS Key Management Service best practices](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md")
- [Getting
  started with the AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/getting-started.md "../../../encryption-sdk/latest/developer-guide/getting-started.md")

## Blogs

- [7
  ways to improve security of your machine learning
  workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/ "https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/")
- [Macie
  for Data Classification](https://aws.amazon.com/blogs/security/use-macie-to-discover-sensitive-data-as-part-of-automated-data-pipelines/ "https://aws.amazon.com/blogs/security/use-macie-to-discover-sensitive-data-as-part-of-automated-data-pipelines/")
- [Building
  a Serverless Tokenization Solution to Mask Sensitive
  Data](https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/ "https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/")

## Examples

- [Amazon SageMaker AI Solution for Privacy in Natural Language
  Processing](https://github.com/awslabs/sagemaker-privacy-for-nlp "https://github.com/awslabs/sagemaker-privacy-for-nlp")
- [How
  Amazon is advancing privacy-aware data processing](https://www.aboutamazon.com/news/amazon-ai/protecting-data-privacy "https://www.aboutamazon.com/news/amazon-ai/protecting-data-privacy")
