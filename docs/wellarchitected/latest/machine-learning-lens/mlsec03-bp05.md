# MLSEC03-BP05 Keep only relevant data

Reduce data exposure risks by preserving only use-case relevant data
across computing environments. Implementing data lifecycle
management and privacy-preserving techniques maintains data security
while enabling effective machine learning workflows.

**Desired outcome:** You maintain a
streamlined dataset across development, staging, and production
environments that contains only the data elements needed for your
machine learning use cases. You have implemented automated data
lifecycle management processes that properly identify data, redact
it when necessary, and remove it when no longer needed. This
approach reduces your security risk exposure while maintaining data
usability for ML operations.

**Common anti-patterns:**

- Keeping collected data indefinitely in case it might be useful
  later.
- Failing to implement data redaction for personally identifiable
  information (PII) in ML datasets.
- Using production data with sensitive information in development
  environments.
- Not establishing clear timelines for data retention and removal.
- Ignoring privacy regulations when designing ML workflows.

**Benefits of establishing this best
practice:**

- Reduced risk of data breaches and privacy violations.
- Lower storage and computational costs from processing only
  necessary data.
- Improved adherence to data privacy regulations.
- Enhanced ML model performance through focus on relevant
  features.
- Streamlined data management processes across environments.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Managing data exposure is crucial for machine learning security.
The more data you collect and store, the greater your attack
surface and potential for data breaches. By focusing on data
minimization principles, you can reduce these risks while still
achieving your ML objectives.

Your data lifecycle management strategy should begin with a
thorough assessment of what data is truly needed for your ML use
cases. This requires close collaboration between data scientists,
security professionals, and business stakeholders to identify
essential features and acceptable levels of data granularity. Once
identified, implement mechanisms to maintain only the necessary
data elements across environments.

When working with potentially sensitive information, apply
privacy-preserving techniques like anonymization,
pseudonymization, or redaction of PII. AWS services like
[Amazon Comprehend](https://aws.amazon.com/comprehend/ "https://aws.amazon.com/comprehend/") and
[Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") can identify sensitive data automatically, while
[Amazon Transcribe](https://aws.amazon.com/transcribe/ "https://aws.amazon.com/transcribe/") offers automatic redaction capabilities. For
more advanced scenarios, consider techniques like differential
privacy or federated learning that allow you to derive insights
from sensitive data without exposing the raw information.

Regular data audits and automated cleanup processes are essential
components of an effective data lifecycle management strategy. By
implementing automated policies for data retention and deletion,
you can verify that data doesn't linger unnecessarily in your
systems after its useful life has ended.

### Implementation steps

1. **Assess data requirements**.
   Begin by thoroughly analyzing your ML use case to determine
   exactly which data elements are required for model training,
   validation, and inference. Document the minimum data
   requirements for each stage of your ML pipeline and justify
   the need for each attribute. Consider using techniques like
   feature importance analysis to identify which data elements
   contribute most to model performance.
2. **Develop a comprehensive data
   lifecycle plan**. Create a documented plan that
   defines how data will flow through your ML pipeline,
   including data collection, processing, storage, usage, and
   eventual deletion. Identify usage patterns and requirements
   for debugging and operational tasks. Specify retention
   periods based on business needs, regulatory requirements,
   and the purpose of the data.
3. **Implement data minimization
   techniques**. Design your data collection and
   preprocessing pipelines to capture only the necessary data
   attributes identified in your assessment. Use
   [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") or similar ETL services to filter out
   unnecessary fields before storage. Consider implementing
   record-level filtering in addition to column-level
   filtering.
4. **Set up automated PII detection and
   redaction**. Deploy solutions to automatically
   identify and redact sensitive information. Use
   [Amazon Comprehend](https://aws.amazon.com/comprehend/ "https://aws.amazon.com/comprehend/") for detecting PII in text data and
   [Amazon Rekognition](https://aws.amazon.com/rekognition/ "https://aws.amazon.com/rekognition/") for identifying sensitive elements in
   images. Implement
   [Amazon Transcribe's automatic redaction feature](https://aws.amazon.com/blogs/aws/now-available-in-amazon-transcribe-automatic-redaction-of-personally-identifiable-information/ "https://aws.amazon.com/blogs/aws/now-available-in-amazon-transcribe-automatic-redaction-of-personally-identifiable-information/") for audio
   transcriptions.
5. **Establish data governance
   controls**. Implement access controls and
   encryption mechanisms using
   [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") and
   [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). Use
   [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") to automatically discover, classify, and
   protect sensitive data in AWS. Apply data classification
   tags to facilitate appropriate handling of different data
   types.
6. **Configure automated data lifecycle
   policies**. Set up
   [S3
   Lifecycle configurations](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to automatically transition
   or expire data based on your retention policies. Implement
   similar mechanisms for other storage systems used in your ML
   pipeline. Create automated jobs to periodically review and
   remove stale data from environments.
7. **Implement privacy-preserving ML
   techniques**. Where possible, use privacy-enhancing
   technologies like differential privacy, federated learning,
   or encrypted computation. Consider using
   [AWS Lake Formation](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/") to centrally define and enforce
   fine-grained access controls. For sensitive use cases,
   explore options for machine learning on encrypted data.
8. **Monitor and audit data
   usage**. Set up logging and monitoring using
   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") and
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to track data access patterns.
   Periodically audit data usage against documented
   requirements to identify and avoid unnecessary data
   collection. Use
   [Amazon Athena with user-defined functions](https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/ "https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/") for analyzing and
   redacting sensitive information in logs and audit trails.
9. **Implement responsible data practices
   for AI models**. When using AI models, be
   especially careful with training data to block memorization
   of sensitive information. Utilize
   [Amazon SageMaker AI's feature store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/") for centralized feature
   management with built-in security controls. Consider data
   poisoning risks and implement appropriate data validation
   before model training.

## Resources

**Related documents:**

- [Reference
  Guide: Extract More Value from your Data](https://pages.awscloud.com/data-lifecycle-reference-guide.html?sc_channel=bl&sc_campaign=datalifecycleandanalyticsintheawscloud&sc_geo=mult&sc_country=global&sc_outcome=multi "https://pages.awscloud.com/data-lifecycle-reference-guide.html?sc_channel=bl&sc_campaign=datalifecycleandanalyticsintheawscloud&sc_geo=mult&sc_country=global&sc_outcome=multi")
- [Data
  Privacy Center](https://aws.amazon.com/compliance/data-privacy/ "https://aws.amazon.com/compliance/data-privacy/")
- [Building
  a data analytics practice across the data lifecycle](https://aws.amazon.com/blogs/publicsector/building-a-data-analytics-practice-across-the-data-lifecycle/ "https://aws.amazon.com/blogs/publicsector/building-a-data-analytics-practice-across-the-data-lifecycle/")
- [Detecting
  and redacting PII using Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/detecting-and-redacting-pii-using-amazon-comprehend/ "https://aws.amazon.com/blogs/machine-learning/detecting-and-redacting-pii-using-amazon-comprehend/")
- [Now
  available in Amazon Transcribe: Automatic Redaction of
  Personally Identifiable Information](https://aws.amazon.com/blogs/aws/now-available-in-amazon-transcribe-automatic-redaction-of-personally-identifiable-information/ "https://aws.amazon.com/blogs/aws/now-available-in-amazon-transcribe-automatic-redaction-of-personally-identifiable-information/")
- [Redacting
  sensitive information with user-defined functions in Amazon Athena](https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/ "https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/")

**Related videos:**

- [Privacy-preserving
  machine learning](https://www.youtube.com/watch?v=ZQkB9XRqdnc "https://www.youtube.com/watch?v=ZQkB9XRqdnc")
- [Best
  practices for Amazon S3](https://youtu.be/HT3QiuzgjZg?t=524 "https://youtu.be/HT3QiuzgjZg?t=524")

**Related examples:**

- [Field
  Notes: Redacting Personal Data from Connected Cars Using
  Amazon Rekognition](https://aws.amazon.com/blogs/architecture/field-notes-redacting-personal-data-from-connected-cars-using-amazon-rekognition/ "https://aws.amazon.com/blogs/architecture/field-notes-redacting-personal-data-from-connected-cars-using-amazon-rekognition/")
- [How
  to Create a Modern CPG Data Architecture with Data Mesh](https://aws.amazon.com/blogs/industries/how-to-create-a-modern-cpg-data-architecture-with-data-mesh/ "https://aws.amazon.com/blogs/industries/how-to-create-a-modern-cpg-data-architecture-with-data-mesh/")
- [Building
  a secure enterprise machine learning platform on AWS](../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md")
