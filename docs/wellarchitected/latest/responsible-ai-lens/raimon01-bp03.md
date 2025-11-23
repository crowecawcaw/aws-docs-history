# RAIMON01-BP03 Preserve data privacy and set access controls on

monitored data

Apply data governance processes that specify what monitoring data
can be collected, processed, stored, and accessed throughout the
monitoring lifecycle. Consider implementing privacy-preserving
techniques including anonymization, differential privacy, and secure
computation methods that enable system oversight without exposing
individual user information. Using the principle of least privilege,
create role-based access controls that limit monitoring data access
to authorized personnel based on job function, with detailed audit
trails tracking data access activities. Establish data retention
policies that specify how long different types of monitoring data
should be stored, with automated deletion processes and procedures
for handling individual data requests.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Apply data governance processes that specify what AI
   monitoring data can be collected, processed, stored, and
   accessed throughout the monitoring lifecycle. This involves
   implementing policies that define permissible data collection
   scope, processing methods, storage requirements, and access
   protocols for AI model monitoring activities. For instance, a
   facial recognition AI system allows collection of prediction
   accuracy metrics and inference latency but prohibits storage
   of actual facial images or biometric features. Use AWS Config
   to enforce data governance rules and AWS CloudTrail to audit
   adherence with data collection policies.
2. Implement privacy-preserving techniques including
   anonymization, differential privacy, and secure computation
   methods that enable AI system oversight without exposing
   individual user information. This requires deploying technical
   safeguards that protect user privacy while maintaining
   monitoring capabilities. For example, a healthcare chatbot
   application could anonymize patient identifiers in
   conversation logs, apply differential privacy to response
   accuracy metrics, and encrypt the monitoring data. Use Amazon SageMaker AI Processing jobs to run anonymization and
   differential privacy implementations, Amazon Macie to identify
   and protect sensitive data in monitoring datasets, and AWS KMS
   for encryption and key management.
3. Create role-based access controls that limit AI monitoring
   data access to authorized personnel based on job function,
   with detailed audit trails tracking data access activities.
   This involves implementing granular permissions that restrict
   monitoring data visibility to specific roles and
   responsibilities. For example, data scientists access model
   accuracy metrics while security teams access only anomaly
   detection alerts, with access types logged and monitored. Use
   AWS IAM to implement role-based access controls and AWS CloudTrail to maintain detailed audit trails of monitoring
   data access.
4. Establish data retention policies that specify how long
   different types of AI monitoring data should be stored, with
   automated deletion processes and procedures for handling
   individual data requests. This requires defining lifecycle
   management rules for various monitoring data types and
   implementing automated compliance-aligned processes.

## Resources

**Related documents:**

- [Amazon SageMaker AI solution for privacy in natural language
  processing](https://www.amazon.science/code-and-datasets/amazon-sagemaker-solution-for-privacy-in-natural-language-processing "https://www.amazon.science/code-and-datasets/amazon-sagemaker-solution-for-privacy-in-natural-language-processing")
- [Differentially
  Private Fair Learning](https://arxiv.org/abs/1812.02696 "https://arxiv.org/abs/1812.02696")
- [Approximate,
  adapt, anonymize (3A): A framework for privacy preserving
  training data release for machine learning](https://www.amazon.science/publications/approximate-adapt-anonymize-3a-a-framework-for-privacy-preserving-training-data-release-for-machine-learning "https://www.amazon.science/publications/approximate-adapt-anonymize-3a-a-framework-for-privacy-preserving-training-data-release-for-machine-learning")
- [Privacy
  preserving data selection for bias mitigation in speech
  models](https://www.amazon.science/publications/privacy-preserving-data-selection-for-bias-mitigation-in-speech-models "https://www.amazon.science/publications/privacy-preserving-data-selection-for-bias-mitigation-in-speech-models")
- [ISO/IEC
  42001:2023 A.6.2.6 AI system operation and monitoring](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools:**

- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [Amazon SageMaker AI Processing](https://aws.amazon.com/sagemaker/processing/ "https://aws.amazon.com/sagemaker/processing/")
- [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/")
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
