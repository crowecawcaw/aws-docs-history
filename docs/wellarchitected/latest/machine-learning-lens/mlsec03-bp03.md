# MLSEC03-BP03 Protect sensitive data privacy

Protect sensitive data used in training against unintended
disclosure by implementing appropriate identification,
classification, and handling strategies. This practice improves data
privacy while maintaining model utility through techniques such as
data removal, masking, tokenization, and principal component
analysis (PCA).

**Desired outcome:** You establish
effective protocols to identify, classify, and protect sensitive
data throughout your machine learning workflows. Your sensitive data
is appropriately secured with encryption, access controls, and data
minimization techniques. Your organization maintains clear
documentation of governance practices for consistent application
across projects.

**Common anti-patterns:**

- Failing to identify sensitive data before using it for model
  training.
- Using raw PII or other sensitive data when anonymized data would
  suffice.
- Not implementing proper encryption for sensitive training data.
- Assuming cloud services automatically protect sensitive data
  without proper configuration.
- Neglecting to document data handling processes for future
  reference.

**Benefits of establishing this best
practice:**

- Reduced risk of data breaches and privacy violations.
- Improves adherence to data protection regulations.
- Increased trust from customers and stakeholders.
- Improved ability to use sensitive data for legitimate machine
  learning purposes.
- Better governance through documented protocols.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Protecting sensitive data privacy in machine learning workflows
requires a systematic approach that begins with data
identification and classification. You need to understand what
data you have and its sensitivity levels before determining
appropriate protection mechanisms. Different types of sensitive
data may require different handling strategies—some might need
complete removal, while others can be effectively masked or
tokenized.

When working with sensitive data in ML workflows, you should adopt
a defense-in-depth approach. This means implementing multiple
layers of protection, including access controls, encryption, data
minimization techniques, and monitoring systems. For example, you
might use [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") to encrypt your training data,
implement role-based access controls, and use
[Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") to continuously monitor for sensitive data exposure.

Privacy-preserving machine learning techniques are increasingly
important as models become more sophisticated. Techniques like
differential privacy, federated learning, and secure multi-party
computation can allow you to train effective models while
minimizing exposure of sensitive data. These approaches maintain
privacy while still extracting valuable insights from your data.

### Implementation steps

1. **Implement automated data discovery
   and classification**. Use automated sensitive data
   discovery in
   [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") to gain continuous, cost-efficient,
   organization-wide visibility into where sensitive data
   resides across your Amazon S3 environment. Macie
   automatically inspects your S3 buckets for sensitive data
   such as personally identifiable information (PII), financial
   data, and AWS credentials, then builds and maintains an
   interactive data map of sensitive data locations and
   provides sensitivity scores for each bucket.
2. **Apply resource tagging for sensitive
   data tracking**. Tag resources and models that
   contain or are derived from sensitive elements to quickly
   differentiate between resources requiring protection and
   those that do not. Use
   [AWS resource tagging](../../../AmazonS3/latest/userguide/object-tagging.md "../../../AmazonS3/latest/userguide/object-tagging.md") to systematically identify and
   manage resources containing sensitive data throughout their
   lifecycle.
3. **Implement comprehensive encryption
   strategies**. Encrypt sensitive data using services
   such as [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"), the
   [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/getting-started.md "../../../encryption-sdk/latest/developer-guide/getting-started.md"), or client-side encryption. Apply
   encryption consistently across data at rest and in transit,
   with appropriate key management practices.
4. **Implement data minimization
   techniques**. Evaluate and identify data for
   anonymization or de-identification to reduce sensitivity.
   Use techniques such as masking, tokenization, or principal
   component analysis to reduce the risk associated with using
   sensitive data for training. Consider using
   [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/") with appropriate
   transformation techniques to create privacy-preserving
   feature representations.
5. **Establish governance documentation
   and processes**. Create comprehensive documentation
   of your sensitive data handling practices, including
   classification schemes, protection mechanisms, access
   control policies, and incident response procedures.
   Regularly review and update these documents to reflect
   changes in regulations, technologies, and organizational
   practices.
6. **Implement differential privacy
   techniques**. Apply differential privacy methods to
   add controlled noise to your data or models to block the
   extraction of individual data points while maintaining
   overall statistical validity.
   [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/ "https://aws.amazon.com/clean-rooms/") assist organizations with collaborating
   on sensitive data while maintaining privacy and adherence to
   regulations.
7. **Perform regular privacy impact
   assessments**. Conduct systematic evaluations of
   how your ML workflows collect, use, and protect sensitive
   data. Use the results to identify areas for improvement in
   your privacy protection mechanisms and adhere to relevant
   regulations.
8. **Implement safeguards for large
   language models**. When using large language
   models, implement safeguards to block memorization and
   exposure of sensitive training data. Use
   [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/") with appropriate
   privacy-preserving configurations and implement proper data
   filtering and anonymization techniques during model training
   and fine-tuning.

## Resources

**Related documents:**

- [Running
  sensitive data discovery jobs in Amazon Macie](../../../macie/latest/user/discovery-jobs.md "../../../macie/latest/user/discovery-jobs.md")
- [Categorizing
  your storage using tags](../../../AmazonS3/latest/userguide/object-tagging.md "../../../AmazonS3/latest/userguide/object-tagging.md")
- [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
- [Using
  the AWS Encryption SDK with AWS KMS](../../../encryption-sdk/latest/developer-guide/getting-started.md "../../../encryption-sdk/latest/developer-guide/getting-started.md")
- [7
  ways to improve security of your machine learning
  workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/ "https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/")
- [Use
  Macie to discover sensitive data as part of automated data
  pipelines](https://aws.amazon.com/blogs/security/use-macie-to-discover-sensitive-data-as-part-of-automated-data-pipelines/ "https://aws.amazon.com/blogs/security/use-macie-to-discover-sensitive-data-as-part-of-automated-data-pipelines/")
- [Building
  a Serverless Tokenization Solution to Mask Sensitive
  Data](https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/ "https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/")

**Related videos:**

- [Security
  for AI/ML Models in AWS](https://www.youtube.com/watch?v=toDQL_c8Zug "https://www.youtube.com/watch?v=toDQL_c8Zug")
- [Security
  best practices the AWS Well-Architected way](https://www.youtube.com/watch?v=wfIVI-M7lbQ "https://www.youtube.com/watch?v=wfIVI-M7lbQ")

**Related examples:**

- [Secure
  Data Science Reference Architecture](https://github.com/aws-samples/secure-data-science-reference-architecture "https://github.com/aws-samples/secure-data-science-reference-architecture")
- [Amazon SageMaker AI Secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops "https://github.com/aws-samples/amazon-sagemaker-secure-mlops")
