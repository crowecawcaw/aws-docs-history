# Security in Amazon SageMaker AI inference optimization

Cloud security at AWS is the highest priority. As an AWS customer, you benefit
from a data center and network architecture that is built to meet the requirements of
the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The
[shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the
cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is
  responsible for protecting the infrastructure that runs AWS services in the
  AWS Cloud. AWS also provides you with services that you can use securely.
  Third-party auditors regularly test and verify the effectiveness of our security
  as part of the
  [AWS compliance
  programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to
  Amazon SageMaker AI, see
  [AWS
  Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your
  responsibility is determined by the AWS service that you use. You are also
  responsible for other factors including the sensitivity of your data, your
  company's requirements, and applicable laws and regulations.
  This documentation helps you understand how to apply the shared responsibility model
  when using SageMaker AI inference optimization features, including AI benchmarking jobs, AI
  recommendation jobs, and AI workload configurations.

## Data protection

The AWS
[shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Amazon SageMaker AI inference
optimization. As described in this model, AWS is responsible for protecting the
global infrastructure that runs all of the AWS Cloud. You are responsible for
maintaining control over your content that is hosted on this infrastructure.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS
Identity and Access Management (IAM). That way, each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you
secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2
  and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security
  controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which
  assists in discovering and securing sensitive data that is stored in
  Amazon S3.

We strongly recommend that you never put confidential or sensitive information,
such as your customers' email addresses, into tags or free-form text fields such
as a **Name** field.

### What data SageMaker AI inference optimization stores

SageMaker AI inference optimization stores the following types of data:

- **Job metadata** – When you
  create AI benchmark jobs or AI recommendation jobs, the service stores
  job configuration metadata such as job names, status, creation
  timestamps, and resource configuration parameters.
- **Workload configurations** –
  When you create AI workload configurations, the service stores the
  configuration parameters you provide, including benchmark parameters,
  dataset configuration, and tags.
- **Benchmark results and recommendations**
  – Job outputs such as performance metrics, cost estimates, and
  deployment recommendations are stored as job metadata within the
  service.

SageMaker AI inference optimization does not store your model weights, training data,
or inference results. Your model artifacts and benchmark output files remain in
your Amazon S3 buckets within your AWS account.

### Encryption at rest

SageMaker AI inference optimization encrypts all stored data at rest by default. Job
metadata and workload configurations are stored in Amazon DynamoDB, with
encryption at rest. You do not need to take any action to enable encryption at
rest.

### Encryption in transit

SageMaker AI inference optimization uses TLS to encrypt all data in transit. API
requests to the service are made over HTTPS using TLS 1.2 or later.

All communication between SageMaker AI inference optimization and other AWS
services (such as Amazon DynamoDB, AWS Lambda, Amazon S3, and AWS Secrets
Manager) uses TLS-encrypted connections.

### Internetwork traffic privacy

SageMaker AI inference optimization API endpoints are accessible over the public
internet using HTTPS. You can use VPC endpoints for SageMaker AI API to keep traffic
between your VPC and the SageMaker AI API within the AWS network, without traversing
the public internet.

When you provide a VPC configuration for your AI benchmark jobs, the service
creates resources within your specified VPC subnets and security groups.

## Identity and Access Management

Amazon SageMaker AI inference optimization uses AWS Identity and Access Management
(IAM) to control access to its resources and operations.

### How SageMaker AI inference optimization works with IAM

SageMaker AI inference optimization is accessed through the SageMaker AI API. All API calls
are authenticated and authorized using IAM.

The inference optimization APIs use the following IAM action
namespace:

- `sagemaker:CreateAIWorkloadConfig`
- `sagemaker:DescribeAIWorkloadConfig`
- `sagemaker:ListAIWorkloadConfigs`
- `sagemaker:DeleteAIWorkloadConfig`
- `sagemaker:CreateAIBenchmarkJob`
- `sagemaker:DescribeAIBenchmarkJob`
- `sagemaker:ListAIBenchmarkJobs`
- `sagemaker:StopAIBenchmarkJob`
- `sagemaker:DeleteAIBenchmarkJob`
- `sagemaker:CreateAIRecommendationJob`
- `sagemaker:DescribeAIRecommendationJob`
- `sagemaker:ListAIRecommendationJobs`
- `sagemaker:StopAIRecommendationJob`
- `sagemaker:DeleteAIRecommendationJob`

### Execution roles

When you create an AI benchmark job or AI recommendation job, you provide an
IAM execution role (`RoleArn`). The service assumes this role to
perform operations in your AWS account, such as:

- Creating and managing SageMaker AI training jobs, endpoints, and
  optimization jobs
- Reading model artifacts from Amazon S3
- Writing benchmark results to Amazon S3
- Accessing secrets from AWS Secrets Manager

The execution role must have a trust policy that allows the SageMaker AI service to
assume it. For more information about creating SageMaker AI execution roles, see
[SageMaker AI
Roles](sagemaker-roles.md "sagemaker-roles.md").

### Resource isolation

SageMaker AI inference optimization enforces account-level isolation. Each job and
workload configuration is scoped to the AWS account that created it. You
cannot access or modify resources belonging to another AWS account.

All SageMaker AI resources created by the service (training jobs, endpoints,
optimization jobs) are created in your AWS account using your execution role,
and are subject to your account's IAM policies and service quotas.

## Security best practices

The following best practices are general guidelines and don't represent a
complete security solution. Because these best practices might not be appropriate
or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

### Preventative best practices

- **Use least privilege for IAM
  policies.** Grant only the minimum permissions required for users
  and execution roles. Avoid using wildcard (`*`) actions or
  resources in IAM policies.
- **Use separate execution roles for
  different workloads.** Create dedicated IAM execution roles for
  benchmark jobs and recommendation jobs rather than sharing a single role
  across all workloads.
- **Use AWS Secrets Manager for sensitive
  values.** When your workload specification requires sensitive
  values such as Hugging Face access tokens, use the `secrets`
  field to reference AWS Secrets Manager secrets by ARN instead of passing
  them as plaintext parameters.
- **Restrict execution role trust
  policies.** Use `aws:SourceAccount` and
  `aws:SourceArn` conditions in your execution role trust policies
  to prevent the confused deputy problem.
- **Scope Amazon S3 permissions to specific
  buckets.** Restrict `s3:GetObject` and
  `s3:PutObject` permissions to the specific Amazon S3 buckets and
  prefixes used for model artifacts and benchmark outputs.
- **Enable Amazon S3 bucket
  encryption.** Ensure that the Amazon S3 buckets used for model
  artifacts and benchmark results have server-side encryption
  enabled.
- **Use tags for access control.**
  Apply tags to your AI workload configurations, benchmark jobs, and
  recommendation jobs. You can use tag-based conditions in IAM policies to
  control access to specific resources.

### Detective best practices

- **Enable AWS
  CloudTrail.** CloudTrail provides a record of all SageMaker AI API calls
  made in your account, including inference optimization
  operations.
- **Monitor with Amazon CloudWatch.** Use
  Amazon CloudWatch metrics and alarms to monitor the status and performance of your
  benchmark and recommendation jobs.
- **Review IAM Access Analyzer
  findings.** Use IAM Access Analyzer to identify IAM policies
  that grant overly broad access to your SageMaker AI
  resources.
- **Enable Amazon S3 access
  logging.** Enable server access logging on Amazon S3 buckets used for
  model artifacts and benchmark results to track access
  patterns.
