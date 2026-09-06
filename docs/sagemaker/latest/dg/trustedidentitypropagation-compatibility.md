

# Trusted identity propagation architecture and compatibility
<a name="trustedidentitypropagation-compatibility"></a>

Trusted identity propagation integrates AWS IAM Identity Center with Amazon SageMaker Studio and other connected AWS services to propagate users' identity context across services. The following page summarizes the trusted identity propagation architecture and compatibility with SageMaker AI. For a comprehensive overview of how trusted identity propagation works across AWS, see [Trusted identity propagation overview](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html).

The key components of the trusted identity propagation architecture include:
+ **Trusted identity propagation**: A methodology of propagating user's identity context between applications and services
+ **Identity context**: Information about a user
+ **Identity-enhanced IAM role session**: Identity-enhanced role sessions have an added identity context that carries a user identifier to the AWS service that it calls
+ **Connected AWS services**: Other AWS services that can recognize the identity context that is propagated through trusted identity propagation

Trusted identity propagation allows connected AWS services to make access decisions based on a user's identity. Within Studio itself, IAM roles are used as carriers of the identity context rather than for making access control decisions. The identity context is propagated to connected AWS services where it can be used for both access control and audit purposes. See [trusted identity propagation considerations](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.html#trustedidentitypropagation-considerations) for more information.

When you enable trusted identity propagation with Studio and authenticate through IAM Identity Center, SageMaker AI:
+ Captures the user's identity context from the IAM Identity Center
+ Creates an identity-enhanced IAM role session that include the user's identity context
+ Passes identity-enhanced IAM role session to compatible AWS services when the user accesses resources
+ Enables downstream AWS services to make access decisions and log activities based on the user identity

## Compatible SageMaker AI features
<a name="trustedidentitypropagation-compatibility-compatible-features"></a>

Trusted identity propagation works with the following Studio features:
+ [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html) private spaces (JupyterLab and Code Editor, based on Code-OSS, Visual Studio Code - Open Source)

**Note**  
When Studio launches with trusted identity propagation enabled, it uses your identity context in addition to your execution role permissions. However, the following processes during instance setup will only use the execution role permissions, without the identity context: Lifecycle Configuration, Bring-Your-Own-Image, CloudWatch agent for user log forwarding.
[Remote access](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access.html) is not currently supported with trusted identity propagation.
When you use assume role operations within Studio notebooks, the assumed roles don't propagate trusted identity propagation context. Only the original execution role maintains the identity context.
+  [SageMaker Training](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html) 
+  [SageMaker Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) 
+  [SageMaker AI realtime hosting](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-options.html) 
+  [SageMaker Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-overview.html) 
+  [SageMaker real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) 
+  [SageMaker Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) 
+  [Managed MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) 

## Compatible AWS services
<a name="trustedidentitypropagation-compatibility-compatible-services"></a>

Trusted identity propagation for Amazon SageMaker Studio integrates with compatible AWS services, where trusted identity propagation is enabled. See [use cases](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-integrations.html) for a comprehensive list with examples on how to enable trusted identity propagation. The trusted identity propagation compatible services include the following.
+  [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/workgroups-identity-center.html) 
+  [Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc-start.html) 
+  [EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop.html) 
+  [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/identity-center-integration.html) 
+  [Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-trusted-identity-propagation.html) 
+ Amazon S3 (via [Amazon S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-get-started.html))
+ [AWS Glue Connections](https://docs.aws.amazon.com/glue/latest/dg/security-trusted-identity-propagation.html)

When trusted identity propagation is enabled with SageMaker AI, each other AWS service with trusted identity propagation is enabled is connected. Once they are connected they recognize and use the user's identity context for access control and auditing.

## Supported AWS Regions
<a name="trustedidentitypropagation-compatibility-supported-regions"></a>

Studio supports trusted identity propagation where [IAM Identity Center is supported](https://docs.aws.amazon.com/singlesignon/latest/userguide/regions.html) and Studio with IAM Identity Center authentication is supported. Studio supports trusted identity propagation in the following AWS Regions:
+ af-south-1
+ ap-east-1
+ ap-northeast-1
+ ap-northeast-2
+ ap-northeast-3
+ ap-south-1
+ ap-southeast-1
+ ap-southeast-2
+ ap-southeast-3
+ ca-central-1
+ eu-central-1
+ eu-central-2
+ eu-north-1
+ eu-south-1
+ eu-west-1
+ eu-west-2
+ eu-west-3
+ il-central-1
+ me-south-1
+ sa-east-1
+ us-east-1
+ us-east-2
+ us-west-1
+ us-west-2