# Use AMS SSP to provision Amazon SageMaker AI in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon SageMaker AI capabilities directly in your AMS managed account. SageMaker AI provides every developer and data scientist with the ability to build, train, and deploy machine learning models quickly.
Amazon SageMaker AI is a fully-managed service that covers the entire machine learning workflow to label and prepare your data, choose an algorithm, train the model,
tune and optimize it for deployment, make predictions, and take action. Your models get to production faster with much less effort and lower cost.
To learn more, see [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/").

## SageMaker AI in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to SageMaker AI in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type. This RFC provisions the
following IAM roles to your account: `customer_sagemaker_admin_role` and service role `AmazonSageMaker-ExecutionRole-Admin`.
After SageMaker AI is provisioned in your account, you must onboard the `customer_sagemaker_admin_role` role in your federation solution.
The service role cannot be accessed by you directly; the SageMaker AI service uses it while doing various actions as described here:
[Passing Roles](../../../sagemaker/latest/dg/sagemaker-roles.md#sagemaker-roles-pass-role "../../../sagemaker/latest/dg/sagemaker-roles.md#sagemaker-roles-pass-role").

**Q: What are the restrictions to using SageMaker AI in my AMS account?**

- The following use cases are not supported by the AMS Amazon SageMaker AI IAM role:
  - SageMaker AI Studio is not supported at this time.
  - SageMaker AI Ground Truth to manage private workforces is not supported since this feature requires
    overly permissive access to Amazon Cognito resources. If managing a private workforce is required, you can request a
    custom IAM role with combined SageMaker AI and Amazon Cognito permissions. Otherwise, we recommend using public workforce
    (backed by Amazon Mechanical Turk), or AWS Marketplace service providers, for data labeling.

- Creating VPC Endpoints to support API calls to SageMaker AI services
  (aws.sagemaker.{region}.notebook, com.amazonaws.{region}.sagemaker.api
  & com.amazonaws.{region}.sagemaker.runtime) is not supported as permissions can’t be scoped down to
  SageMaker AI related services only. To support this use case, submit a Management | Other | Other
  RFC to create related VPC endpoints.
- SageMaker AI endpoint auto scaling is not supported as SageMaker AI requires
  `DeleteAlarm` permissions on any ("\*") resource. To support
  endpoint auto scaling, submit a Management | Other | Other
  RFC to setup auto scaling for a SageMaker AI endpoint.

**Q: What are the prerequisites or dependencies to using SageMaker AI in my AMS
account?**

- The following use cases require special configuration prior to use:
  - If an S3 bucket will be used to store model artifacts and data,
    then you must request an S3 bucket named with the required keywords
    ("SageMaker", "Sagemaker", "sagemaker" or "aws-glue")
    with a Deployment | Advanced stack components | S3 storage | Create RFC.
  - If Elastic File Store (EFS) will be used, then EFS storage must be configured in the same
    subnet, and allowed by security groups.
  - If other resources require direct access to SageMaker AI services (notebooks, API, runtime, and so
    on), then configuration must be requested by:
    - Submitting an RFC to create a security group for the
      endpoint (Deployment | Advanced stack components | Security group | Create
      (auto)).
    - Submitting a Management | Other | Other | Create RFC to set up related VPC endpoints.

**Q: What are the supported naming conventions for resources that the
`customer_sagemaker_admin_role` can access directly?**
(The following are for update and delete permissions; if you require
additional supported naming conventions for your resources, reach
out to an AMS Cloud Architect for consultation.)

- Resource: Passing `AmazonSageMaker-ExecutionRole-*` role
  - Permissions: The SageMaker AI self-provisioned service role supports your use of the SageMaker AI service role
    (`AmazonSageMaker-ExecutionRole-*`)
    with AWS Glue, AWS RoboMaker, and AWS Step Functions.

- Resource: Secrets on AWS Secrets Manager
  - Permissions: Describe, Create, Get, Update secrets with a
    `AmazonSageMaker-*`
    prefix.
  - Permissions: Describe, Get secrets when the `SageMaker`
    resource tag is set to
    `true`.

- Resource: Repositories on AWS CodeCommit
  - Permissions: Create/ delete repositories with a `AmazonSageMaker-*` prefix.
  - Permissions: Git Pull/Push on repositories with following prefixes,
    `*sagemaker*`,
    `*SageMaker*`, and
    `*Sagemaker*`.

- Resource: Amazon ECR (Amazon Elastic Container Registry) Repositories
  - Permissions: Permissions: Set, delete repository policies, and upload
    container images, when
    the following resource naming convention is used,
    `*sagemaker*`.

- Resource: Amazon S3 buckets
  - Permissions: Get, Put, Delete object, abort multipart upload S3 objects when
    resources have the following prefixes: `*SageMaker*`,
    `*Sagemaker*`, `*sagemaker*`
    and `aws-glue`.
  - Permissions: Get S3 objects when the `SageMaker` tag is set to
    `true`.

- Resource: Amazon CloudWatch Log Group
  - Permissions: Create Log Group or Stream, Put Log Event, List, Update, Create , Delete log
    delivery with following prefix:
    `/aws/sagemaker/*`.

- Resource: Amazon CloudWatch Metric
  - Permissions: Put metric data when the following prefixes are used:
    `AWS/SageMaker`,
    `AWS/SageMaker/`,
    `aws/SageMaker`,
    `aws/SageMaker/`,
    `aws/sagemaker`,
    `aws/sagemaker/`, and
    `/aws/sagemaker/.`.

- Resource: Amazon CloudWatch Dashboard
  - Permissions: Create/Delete dashboards when the following prefixes are used:
    `customer_*`.

- Resource: Amazon SNS (Simple Notification Service) topic
  - Permissions: Subscribe/Create topic when following prefixes are used:
    `*sagemaker*`, `*SageMaker*`,
    and `*Sagemaker*`.

**Q: What’s the difference between `AmazonSageMakerFullAccess`
and `customer_sagemaker_admin_role`?**

The `customer_sagemaker_admin_role` with the `customer_sagemaker_admin_policy`
provides almost the same permissions as AmazonSageMakerFullAccess except:

- Permission to connect with AWS RoboMaker, Amazon Cognito, and AWS Glue resources.
- SageMaker AI endpoint autoscaling. You must submit a RFC with Management | Advanced stack components | Identity and Access Management (IAM) | Update entity or policy (managed automation) change type (ct-27tuth19k52b4) to elevate autoscaling
  permissions temporarily, or permanently, as autoscaling requires permissive access on CloudWatch service.

**Q: How do I adopt AWS KMS customer managed key in data encryption at rest?**

You must ensure that the key policy has been set up properly on the customer managed keys so that related IAM users or roles
can use the keys. For more information, see the
[AWS KMS Key Policy document](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users").
