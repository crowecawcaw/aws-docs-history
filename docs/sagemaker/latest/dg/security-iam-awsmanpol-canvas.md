# AWS managed policies for Amazon SageMaker Canvas

These AWS managed policies add permissions required to use Amazon SageMaker Canvas. The policies are
available in your AWS account and are used by execution roles created from the SageMaker AI
console.

###### Topics

- [AWS managed
  policy: AmazonSageMakerCanvasFullAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess")
- [AWS managed
  policy: AmazonSageMakerCanvasDataPrepFullAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasDataPrepFullAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasDataPrepFullAccess")
- [AWS
  managed policy: AmazonSageMakerCanvasDirectDeployAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasDirectDeployAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasDirectDeployAccess")
- [AWS
  managed policy: AmazonSageMakerCanvasAIServicesAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess")
- [AWS
  managed policy: AmazonSageMakerCanvasBedrockAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasBedrockAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasBedrockAccess")
- [AWS
  managed policy: AmazonSageMakerCanvasForecastAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasForecastAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasForecastAccess")
- [AWS
  managed policy: AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy](#security-iam-awsmanpol-AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy "#security-iam-awsmanpol-AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy")
- [AWS managed policy: AmazonSageMakerCanvasSMDataScienceAssistantAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasSMDataScienceAssistantAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasSMDataScienceAssistantAccess")
- [Amazon SageMaker AI updates to Amazon SageMaker Canvas
  managed policies](#security-iam-awsmanpol-canvas-updates "#security-iam-awsmanpol-canvas-updates")

## AWS managed

policy: AmazonSageMakerCanvasFullAccess

This policy grants permissions that allow full access to Amazon SageMaker Canvas through the
AWS Management Console and SDK. The policy also provides select access to related services [for
example, Amazon Simple Storage Service (Amazon S3), AWS Identity and Access Management (IAM), Amazon Virtual Private Cloud (Amazon VPC), Amazon Elastic Container Registry (Amazon ECR),
Amazon CloudWatch Logs, Amazon Redshift, AWS Secrets Manager, Amazon SageMaker Autopilot, SageMaker Model Registry, and Amazon Forecast].

This policy is intended to help customers experiment and get started with all the
capabilities of SageMaker Canvas. For more fine-grained control, we suggest customers build their
own scoped down versions as they move to production workloads. For more information, see
[IAM
policy types: How and when to use them](https://aws.amazon.com/blogs/security/iam-policy-types-how-and-when-to-use-them/ "https://aws.amazon.com/blogs/security/iam-policy-types-how-and-when-to-use-them/").

**Permissions details**

This AWS managed policy includes the following permissions.

- `sagemaker` – Allows principals to create and host SageMaker AI
  models on resources whose ARN contains "Canvas", "canvas", or
  "model-compilation-". Additionally, users can register their SageMaker Canvas model to SageMaker AI
  Model Registry in the same AWS account. Also allows principals to create and
  manage SageMaker training, transform, and AutoML jobs.
- `application-autoscaling` – Allows principals to
  automatically scale a SageMaker AI inference endpoint.
- `athena` – Allows principals to query a list of data
  catalogs, databases, and table metadata from Amazon Athena, and access the tables
  in the catalogs.
- `cloudwatch` – Allows principals to create and manage
  Amazon CloudWatch alarms.
- `ec2` – Allows principals to create Amazon VPC endpoints.
- `ecr` – Allows principals to get information about a
  container image.
- `emr-serverless` – Allows principals to create and manage
  Amazon EMR Serverless applications and job runs.
  Also allows principals to tag SageMaker Canvas resources.
- `forecast` – Allows principals to use Amazon Forecast.
- `glue` – Allows principals to retrieve the tables,
  databases, and partitions in the AWS Glue catalog.
- `iam` – Allows principals to pass an IAM role to
  Amazon SageMaker AI, Amazon Forecast, and Amazon EMR Serverless.
  Also allows principals to create a service-linked role.
- `kms` – Allows principals to read an AWS KMS key that is
  tagged with `Source:SageMakerCanvas`.
- `logs` – Allows principals to publish logs from training
  jobs and endpoints.
- `quicksight` – Allows principals to list the namespaces
  in the Quick Suite account.
- `rds` – Allows principals to return information about
  provisioned Amazon RDS instances.
- `redshift` – Allows principals to get credentials for a
  "sagemaker_access\*" dbuser on any Amazon Redshift cluster if that user exists.
- `redshift-data` – Allows principals to run queries on
  Amazon Redshift using the Amazon Redshift Data API. This only provides access to the Redshift Data APIs themselves
  and does not directly provide access to your Amazon Redshift clusters. For more
  information, see
  [Using the Amazon Redshift Data API](../../../redshift/latest/mgmt/data-api.md "../../../redshift/latest/mgmt/data-api.md").
- `s3` – Allows principals to add and retrieve objects from
  Amazon S3 buckets. These objects are limited to those whose name includes
  "SageMaker", "Sagemaker", or "sagemaker". Also allows principals to retrieve
  objects from Amazon S3 buckets whose ARN starts with "jumpstart-cache-prod-" in
  specific regions.
- `secretsmanager` – Allows principals to store customer
  credentials to connect to a Snowflake database using Secrets Manager.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SageMakerUserDetailsAndPackageOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeDomain",
 "sagemaker:DescribeUserProfile",
 "sagemaker:ListTags",
 "sagemaker:ListModelPackages",
 "sagemaker:ListModelPackageGroups",
 "sagemaker:ListEndpoints"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SageMakerPackageGroupOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateModelPackageGroup",
 "sagemaker:CreateModelPackage",
 "sagemaker:DescribeModelPackageGroup",
 "sagemaker:DescribeModelPackage"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:model-package/*",
 "arn:aws:sagemaker:*:*:model-package-group/*"
 ]
 },
 {
 "Sid": "SageMakerTrainingOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateCompilationJob",
 "sagemaker:CreateEndpoint",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:CreateModel",
 "sagemaker:CreateProcessingJob",
 "sagemaker:CreateAutoMLJob",
 "sagemaker:CreateAutoMLJobV2",
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateTransformJob",
 "sagemaker:DeleteEndpoint",
 "sagemaker:DescribeCompilationJob",
 "sagemaker:DescribeEndpoint",
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:DescribeModel",
 "sagemaker:DescribeProcessingJob",
 "sagemaker:DescribeAutoMLJob",
 "sagemaker:DescribeAutoMLJobV2",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:DescribeTransformJob",
 "sagemaker:ListCandidatesForAutoMLJob",
 "sagemaker:StopAutoMLJob",
 "sagemaker:StopTrainingJob",
 "sagemaker:StopTransformJob",
 "sagemaker:AddTags",
 "sagemaker:DeleteApp"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:*Canvas*",
 "arn:aws:sagemaker:*:*:*canvas*",
 "arn:aws:sagemaker:*:*:*model-compilation-*"
 ]
 },
 {
 "Sid": "SageMakerHostingOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DeleteEndpointConfig",
 "sagemaker:DeleteModel",
 "sagemaker:InvokeEndpoint",
 "sagemaker:UpdateEndpointWeightsAndCapacities",
 "sagemaker:InvokeEndpointAsync"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:*Canvas*",
 "arn:aws:sagemaker:*:*:*canvas*"
 ]
 },
 {
 "Sid": "EC2VPCOperation",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateVpcEndpoint",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcEndpointServices"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ECROperations",
 "Effect": "Allow",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer",
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMGetOperations",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/*"
 },
 {
 "Sid": "IAMPassOperation",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 },
 {
 "Sid": "LoggingOperation",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/sagemaker/*"
 },
 {
 "Sid": "S3Operations",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:CreateBucket",
 "s3:GetBucketCors",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*SageMaker*",
 "arn:aws:s3:::*Sagemaker*",
 "arn:aws:s3:::*sagemaker*"
 ]
 },
 {
 "Sid": "ReadSageMakerJumpstartArtifacts",
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": [
 "arn:aws:s3:::jumpstart-cache-prod-us-west-2/*",
 "arn:aws:s3:::jumpstart-cache-prod-us-east-1/*",
 "arn:aws:s3:::jumpstart-cache-prod-us-east-2/*",
 "arn:aws:s3:::jumpstart-cache-prod-eu-west-1/*",
 "arn:aws:s3:::jumpstart-cache-prod-eu-central-1/*",
 "arn:aws:s3:::jumpstart-cache-prod-ap-south-1/*",
 "arn:aws:s3:::jumpstart-cache-prod-ap-northeast-2/*",
 "arn:aws:s3:::jumpstart-cache-prod-ap-northeast-1/*",
 "arn:aws:s3:::jumpstart-cache-prod-ap-southeast-1/*",
 "arn:aws:s3:::jumpstart-cache-prod-ap-southeast-2/*"
 ]
 },
 {
 "Sid": "S3ListOperations",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GlueOperations",
 "Effect": "Allow",
 "Action": "glue:SearchTables",
 "Resource": [
 "arn:aws:glue:*:*:table/*/*",
 "arn:aws:glue:*:*:database/*",
 "arn:aws:glue:*:*:catalog"
 ]
 },
 {
 "Sid": "SecretsManagerARNBasedOperation",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:DescribeSecret",
 "secretsmanager:GetSecretValue",
 "secretsmanager:CreateSecret",
 "secretsmanager:PutResourcePolicy"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:AmazonSageMaker-*"
 ]
 },
 {
 "Sid": "SecretManagerTagBasedOperation",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:DescribeSecret",
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "secretsmanager:ResourceTag/SageMaker": "true"
 }
 }
 },
 {
 "Sid": "RedshiftOperations",
 "Effect": "Allow",
 "Action": [
 "redshift-data:ExecuteStatement",
 "redshift-data:DescribeStatement",
 "redshift-data:CancelStatement",
 "redshift-data:GetStatementResult",
 "redshift-data:ListSchemas",
 "redshift-data:ListTables",
 "redshift-data:DescribeTable"
 ],
 "Resource": "*"
 },
 {
 "Sid": "RedshiftGetCredentialsOperation",
 "Effect": "Allow",
 "Action": [
 "redshift:GetClusterCredentials"
 ],
 "Resource": [
 "arn:aws:redshift:*:*:dbuser:*/sagemaker_access*",
 "arn:aws:redshift:*:*:dbname:*"
 ]
 },
 {
 "Sid": "ForecastOperations",
 "Effect": "Allow",
 "Action": [
 "forecast:CreateExplainabilityExport",
 "forecast:CreateExplainability",
 "forecast:CreateForecastEndpoint",
 "forecast:CreateAutoPredictor",
 "forecast:CreateDatasetImportJob",
 "forecast:CreateDatasetGroup",
 "forecast:CreateDataset",
 "forecast:CreateForecast",
 "forecast:CreateForecastExportJob",
 "forecast:CreatePredictorBacktestExportJob",
 "forecast:CreatePredictor",
 "forecast:DescribeExplainabilityExport",
 "forecast:DescribeExplainability",
 "forecast:DescribeAutoPredictor",
 "forecast:DescribeForecastEndpoint",
 "forecast:DescribeDatasetImportJob",
 "forecast:DescribeDataset",
 "forecast:DescribeForecast",
 "forecast:DescribeForecastExportJob",
 "forecast:DescribePredictorBacktestExportJob",
 "forecast:GetAccuracyMetrics",
 "forecast:InvokeForecastEndpoint",
 "forecast:GetRecentForecastContext",
 "forecast:DescribePredictor",
 "forecast:TagResource",
 "forecast:DeleteResourceTree"
 ],
 "Resource": [
 "arn:aws:forecast:*:*:*Canvas*"
 ]
 },
 {
 "Sid": "RDSOperation",
 "Effect": "Allow",
 "Action": "rds:DescribeDBInstances",
 "Resource": "*"
 },
 {
 "Sid": "IAMPassOperationForForecast",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "forecast.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AutoscalingOperations",
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:PutScalingPolicy",
 "application-autoscaling:RegisterScalableTarget"
 ],
 "Resource": "arn:aws:application-autoscaling:*:*:scalable-target/*",
 "Condition": {
 "StringEquals": {
 "application-autoscaling:service-namespace": "sagemaker",
 "application-autoscaling:scalable-dimension": "sagemaker:variant:DesiredInstanceCount"
 }
 }
 },
 {
 "Sid": "AsyncEndpointOperations",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:DescribeAlarms",
 "sagemaker:DescribeEndpointConfig"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DescribeScalingOperations",
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:DescribeScalingActivities"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "SageMakerCloudWatchUpdate",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:DeleteAlarms"
 ],
 "Resource": [
 "arn:aws:cloudwatch:*:*:alarm:TargetTracking*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "application-autoscaling.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AutoscalingSageMakerEndpointOperation",
 "Action": "iam:CreateServiceLinkedRole",
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/aws-service-role/sagemaker.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_SageMakerEndpoint",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "sagemaker.application-autoscaling.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AthenaOperation",
 "Action": [
 "athena:ListTableMetadata",
 "athena:ListDataCatalogs",
 "athena:ListDatabases"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "GlueOperation",
 "Action": [
 "glue:GetDatabases",
 "glue:GetPartitions",
 "glue:GetTables"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:glue:*:*:table/*",
 "arn:aws:glue:*:*:catalog",
 "arn:aws:glue:*:*:database/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "QuicksightOperation",
 "Action": [
 "quicksight:ListNamespaces"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "AllowUseOfKeyInAccount",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Source": "SageMakerCanvas",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessCreateApplicationOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:CreateApplication",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessListApplicationOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:ListApplications",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessApplicationOperations",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:UpdateApplication",
 "emr-serverless:StopApplication",
 "emr-serverless:GetApplication",
 "emr-serverless:StartApplication"
 ],
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessStartJobRunOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:StartJobRun",
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessListJobRunOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:ListJobRuns",
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessJobRunOperations",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:GetJobRun",
 "emr-serverless:CancelJobRun"
 ],
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*/jobruns/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessTagResourceOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:TagResource",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "IAMPassOperationForEMRServerless",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::*:role/service-role/AmazonSageMakerCanvasEMRSExecutionAccess-*",
 "arn:aws:iam::*:role/AmazonSageMakerCanvasEMRSExecutionAccess-*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "emr-serverless.amazonaws.com",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")

## AWS managed

policy: AmazonSageMakerCanvasDataPrepFullAccess

This policy grants permissions that allow full access to the data preparation
functionality of Amazon SageMaker Canvas. The policy also provides least privilege permissions for
the services that integrate with the data preparation functionality [for example,
Amazon Simple Storage Service (Amazon S3), AWS Identity and Access Management (IAM), Amazon EMR, Amazon EventBridge, Amazon Redshift, AWS Key Management Service (AWS KMS)
and AWS Secrets Manager].

**Permissions details**

This AWS managed policy includes the following permissions.

- `sagemaker` – Allows principals to access processing jobs,
  training jobs, inference pipelines, AutoML jobs, and feature groups.
- `athena` – Allows principals to query a list of data
  catalogs, databases, and table metadata from Amazon Athena.
- `elasticmapreduce` – Allows principals to read and list
  Amazon EMR clusters.
- `emr-serverless` – Allows principals to create and manage
  Amazon EMR Serverless applications and job runs.
  Also allows principals to tag SageMaker Canvas resources.
- `events` – Allows principals to create, read, update, and
  add targets to Amazon EventBridge rules for scheduled jobs.
- `glue` – Allows principals to get and search tables from
  databases in the AWS Glue catalog.
- `iam` – Allows principals to pass an IAM role to Amazon SageMaker AI,
  EventBridge, and Amazon EMR Serverless. Also allows principals to create a service-linked role.
- `kms` – Allows principals to retrieve AWS KMS aliases stored
  in jobs and endpoints, and access the associated KMS key.
- `logs` – Allows principals to publish logs from training
  jobs and endpoints.
- `redshift` – Allows principals to get credentials to
  access an Amazon Redshift database.
- `redshift-data` – Allows principals to run, cancel,
  describe, list, and get the results of Amazon Redshift queries. Also allows principals
  to list Amazon Redshift schemas and tables.
- `s3` – Allows principals to add and retrieve objects from
  Amazon S3 buckets. These objects are limited to those whose name includes
  "SageMaker", "Sagemaker", or "sagemaker"; or is tagged with "SageMaker",
  case-insensitive.
- `secretsmanager` – Allows principals to store and retrieve
  customer database credentials using Secrets Manager.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SageMakerListFeatureGroupOperation",
 "Effect": "Allow",
 "Action": "sagemaker:ListFeatureGroups",
 "Resource": "*"
 },
 {
 "Sid": "SageMakerFeatureGroupOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateFeatureGroup",
 "sagemaker:DescribeFeatureGroup"
 ],
 "Resource": "arn:aws:sagemaker:*:*:feature-group/*"
 },
 {
 "Sid": "SageMakerProcessingJobOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateProcessingJob",
 "sagemaker:DescribeProcessingJob",
 "sagemaker:AddTags"
 ],
 "Resource": "arn:aws:sagemaker:*:*:processing-job/*canvas-data-prep*"
 },
 {
 "Sid": "SageMakerProcessingJobListOperation",
 "Effect": "Allow",
 "Action": "sagemaker:ListProcessingJobs",
 "Resource": "*"
 },
 {
 "Sid": "SageMakerPipelineOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribePipeline",
 "sagemaker:CreatePipeline",
 "sagemaker:UpdatePipeline",
 "sagemaker:DeletePipeline",
 "sagemaker:StartPipelineExecution",
 "sagemaker:ListPipelineExecutionSteps",
 "sagemaker:DescribePipelineExecution"
 ],
 "Resource": "arn:aws:sagemaker:*:*:pipeline/*canvas-data-prep*"
 },
 {
 "Sid": "KMSListOperations",
 "Effect": "Allow",
 "Action": "kms:ListAliases",
 "Resource": "*"
 },
 {
 "Sid": "KMSOperations",
 "Effect": "Allow",
 "Action": "kms:DescribeKey",
 "Resource": "arn:aws:kms:*:*:key/*"
 },
 {
 "Sid": "S3Operations",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetBucketCors",
 "s3:GetBucketLocation",
 "s3:AbortMultipartUpload"
 ],
 "Resource": [
 "arn:aws:s3:::*SageMaker*",
 "arn:aws:s3:::*Sagemaker*",
 "arn:aws:s3:::*sagemaker*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "S3GetObjectOperation",
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "s3:ExistingObjectTag/SageMaker": "true"
 },
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "S3ListOperations",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMListOperations",
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "*"
 },
 {
 "Sid": "IAMGetOperations",
 "Effect": "Allow",
 "Action": "iam:GetRole",
 "Resource": "arn:aws:iam::*:role/*"
 },
 {
 "Sid": "IAMPassOperation",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "sagemaker.amazonaws.com",
 "events.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "EventBridgePutOperation",
 "Effect": "Allow",
 "Action": [
 "events:PutRule"
 ],
 "Resource": "arn:aws:events:*:*:rule/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-data-prep-job": "true"
 }
 }
 },
 {
 "Sid": "EventBridgeOperations",
 "Effect": "Allow",
 "Action": [
 "events:DescribeRule",
 "events:PutTargets"
 ],
 "Resource": "arn:aws:events:*:*:rule/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-data-prep-job": "true"
 }
 }
 },
 {
 "Sid": "EventBridgeTagBasedOperations",
 "Effect": "Allow",
 "Action": [
 "events:TagResource"
 ],
 "Resource": "arn:aws:events:*:*:rule/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-data-prep-job": "true",
 "aws:ResourceTag/sagemaker:is-canvas-data-prep-job": "true"
 }
 }
 },
 {
 "Sid": "EventBridgeListTagOperation",
 "Effect": "Allow",
 "Action": "events:ListTagsForResource",
 "Resource": "*"
 },
 {
 "Sid": "GlueOperations",
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabases",
 "glue:GetTable",
 "glue:GetTables",
 "glue:SearchTables"
 ],
 "Resource": [
 "arn:aws:glue:*:*:table/*",
 "arn:aws:glue:*:*:catalog",
 "arn:aws:glue:*:*:database/*"
 ]
 },
 {
 "Sid": "EMROperations",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:DescribeCluster",
 "elasticmapreduce:ListInstanceGroups"
 ],
 "Resource": "arn:aws:elasticmapreduce:*:*:cluster/*"
 },
 {
 "Sid": "EMRListOperation",
 "Effect": "Allow",
 "Action": "elasticmapreduce:ListClusters",
 "Resource": "*"
 },
 {
 "Sid": "AthenaListDataCatalogOperation",
 "Effect": "Allow",
 "Action": "athena:ListDataCatalogs",
 "Resource": "*"
 },
 {
 "Sid": "AthenaQueryExecutionOperations",
 "Effect": "Allow",
 "Action": [
 "athena:GetQueryExecution",
 "athena:GetQueryResults",
 "athena:StartQueryExecution",
 "athena:StopQueryExecution"
 ],
 "Resource": "arn:aws:athena:*:*:workgroup/*"
 },
 {
 "Sid": "AthenaDataCatalogOperations",
 "Effect": "Allow",
 "Action": [
 "athena:ListDatabases",
 "athena:ListTableMetadata"
 ],
 "Resource": "arn:aws:athena:*:*:datacatalog/*"
 },
 {
 "Sid": "RedshiftOperations",
 "Effect": "Allow",
 "Action": [
 "redshift-data:DescribeStatement",
 "redshift-data:CancelStatement",
 "redshift-data:GetStatementResult"
 ],
 "Resource": "*"
 },
 {
 "Sid": "RedshiftArnBasedOperations",
 "Effect": "Allow",
 "Action": [
 "redshift-data:ExecuteStatement",
 "redshift-data:ListSchemas",
 "redshift-data:ListTables"
 ],
 "Resource": "arn:aws:redshift:*:*:cluster:*"
 },
 {
 "Sid": "RedshiftGetCredentialsOperation",
 "Effect": "Allow",
 "Action": "redshift:GetClusterCredentials",
 "Resource": [
 "arn:aws:redshift:*:*:dbuser:*/sagemaker_access*",
 "arn:aws:redshift:*:*:dbname:*"
 ]
 },
 {
 "Sid": "SecretsManagerARNBasedOperation",
 "Effect": "Allow",
 "Action": "secretsmanager:CreateSecret",
 "Resource": "arn:aws:secretsmanager:*:*:secret:AmazonSageMaker-*"
 },
 {
 "Sid": "SecretManagerTagBasedOperation",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:DescribeSecret",
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "arn:aws:secretsmanager:*:*:secret:AmazonSageMaker-*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SageMaker": "true",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "RDSOperation",
 "Effect": "Allow",
 "Action": "rds:DescribeDBInstances",
 "Resource": "*"
 },
 {
 "Sid": "LoggingOperation",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/sagemaker/studio:*"
 },
 {
 "Sid": "EMRServerlessCreateApplicationOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:CreateApplication",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessListApplicationOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:ListApplications",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessApplicationOperations",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:UpdateApplication",
 "emr-serverless:GetApplication"
 ],
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessStartJobRunOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:StartJobRun",
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessListJobRunOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:ListJobRuns",
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessJobRunOperations",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:GetJobRun",
 "emr-serverless:CancelJobRun"
 ],
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*/jobruns/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessTagResourceOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:TagResource",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "IAMPassOperationForEMRServerless",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::*:role/service-role/AmazonSageMakerCanvasEMRSExecutionAccess-*",
 "arn:aws:iam::*:role/AmazonSageMakerCanvasEMRSExecutionAccess-*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "emr-serverless.amazonaws.com",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")

## AWS

managed policy: AmazonSageMakerCanvasDirectDeployAccess

This policy grants permissions needed for Amazon SageMaker Canvas to create and manage Amazon SageMaker AI
endpoints.

**Permissions details**

This AWS managed policy includes the following permissions.

- `sagemaker` – Allows principals to create and manage SageMaker AI
  endpoints with an ARN resource name that starts with "Canvas" or "canvas".
- `cloudwatch` – Allows principals to retrieve Amazon CloudWatch
  metric data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SageMakerEndpointPerms",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateEndpoint",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:DeleteEndpoint",
 "sagemaker:DescribeEndpoint",
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:InvokeEndpoint",
 "sagemaker:UpdateEndpoint"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:Canvas*",
 "arn:aws:sagemaker:*:*:canvas*"
 ]
 },
 {
 "Sid": "ReadCWInvocationMetrics",
 "Effect": "Allow",
 "Action": "cloudwatch:GetMetricData",
 "Resource": "*"
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerCanvasAIServicesAccess

This policy grants permissions for Amazon SageMaker Canvas to use Amazon Textract, Amazon Rekognition,
Amazon Comprehend, and Amazon Bedrock.

**Permissions details**

This AWS managed policy includes the following permissions.

- `textract` – Allows principals to use Amazon Textract to detect
  documents, expenses, and identities within an image.
- `rekognition` – Allows principals to use Amazon Rekognition to detect
  labels and text within an image.
- `comprehend` – Allows principals to use Amazon Comprehend to detect
  sentiment and dominant language, and named and personally identifiable
  information (PII) entities within a text document.
- `bedrock` – Allows principals to use Amazon Bedrock to list
  and invoke foundation models.
- `iam` – Allows principals to pass an IAM role to Amazon Bedrock.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Textract",
 "Effect": "Allow",
 "Action": [
 "textract:AnalyzeDocument",
 "textract:AnalyzeExpense",
 "textract:AnalyzeID",
 "textract:StartDocumentAnalysis",
 "textract:StartExpenseAnalysis",
 "textract:GetDocumentAnalysis",
 "textract:GetExpenseAnalysis"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Rekognition",
 "Effect": "Allow",
 "Action": [
 "rekognition:DetectLabels",
 "rekognition:DetectText"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Comprehend",
 "Effect": "Allow",
 "Action": [
 "comprehend:BatchDetectDominantLanguage",
 "comprehend:BatchDetectEntities",
 "comprehend:BatchDetectSentiment",
 "comprehend:DetectPiiEntities",
 "comprehend:DetectEntities",
 "comprehend:DetectSentiment",
 "comprehend:DetectDominantLanguage"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Bedrock",
 "Effect": "Allow",
 "Action": [
 "bedrock:InvokeModel",
 "bedrock:ListFoundationModels",
 "bedrock:InvokeModelWithResponseStream"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateBedrockResourcesPermission",
 "Effect": "Allow",
 "Action": [
 "bedrock:CreateModelCustomizationJob",
 "bedrock:CreateProvisionedModelThroughput",
 "bedrock:TagResource"
 ],
 "Resource": [
 "arn:aws:bedrock:*:*:model-customization-job/*",
 "arn:aws:bedrock:*:*:custom-model/*",
 "arn:aws:bedrock:*:*:provisioned-model/*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": [
 "SageMaker",
 "Canvas"
 ]
 },
 "StringEquals": {
 "aws:RequestTag/SageMaker": "true",
 "aws:RequestTag/Canvas": "true",
 "aws:ResourceTag/SageMaker": "true",
 "aws:ResourceTag/Canvas": "true"
 }
 }
 },
 {
 "Sid": "GetStopAndDeleteBedrockResourcesPermission",
 "Effect": "Allow",
 "Action": [
 "bedrock:GetModelCustomizationJob",
 "bedrock:GetCustomModel",
 "bedrock:GetProvisionedModelThroughput",
 "bedrock:StopModelCustomizationJob",
 "bedrock:DeleteProvisionedModelThroughput"
 ],
 "Resource": [
 "arn:aws:bedrock:*:*:model-customization-job/*",
 "arn:aws:bedrock:*:*:custom-model/*",
 "arn:aws:bedrock:*:*:provisioned-model/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SageMaker": "true",
 "aws:ResourceTag/Canvas": "true"
 }
 }
 },
 {
 "Sid": "FoundationModelPermission",
 "Effect": "Allow",
 "Action": [
 "bedrock:CreateModelCustomizationJob"
 ],
 "Resource": [
 "arn:aws:bedrock:*::foundation-model/*"
 ]
 },
 {
 "Sid": "BedrockFineTuningPassRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "bedrock.amazonaws.com"
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")

## AWS

managed policy: AmazonSageMakerCanvasBedrockAccess

This policy grants permissions commonly needed to use Amazon SageMaker Canvas with Amazon Bedrock.

**Permissions details**

This AWS managed policy includes the following permissions.

- `s3` – Allows principals to add and retrieve objects from
  Amazon S3 buckets in the "sagemaker-\*/Canvas" directory.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3CanvasAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::sagemaker-*/Canvas",
 "arn:aws:s3:::sagemaker-*/Canvas/*"
 ]
 },
 {
 "Sid": "S3BucketAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::sagemaker-*"
 ]
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerCanvasForecastAccess

This policy grants permissions commonly needed to use Amazon SageMaker Canvas with Amazon Forecast.

**Permissions details**

This AWS managed policy includes the following permissions.

- `s3` – Allows principals to add and retrieve objects from
  Amazon S3 buckets. These objects are limited to those whose name
  starts with "sagemaker-".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::sagemaker-*/Canvas",
 "arn:aws:s3:::sagemaker-*/canvas"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::sagemaker-*"
 ]
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy

This policy grants permissions to Amazon EMR Serverless for AWS services, such as
Amazon S3, used by Amazon SageMaker Canvas for large data processing.

**Permissions details**

This AWS managed policy includes the following permissions.

- `s3` – Allows principals to add and retrieve objects from
  Amazon S3 buckets. These objects are limited to those whose name includes "SageMaker"
  or "sagemaker"; or is tagged with "SageMaker", case-insensitive.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3Operations",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetBucketCors",
 "s3:GetBucketLocation",
 "s3:AbortMultipartUpload"
 ],
 "Resource": [
 "arn:aws:s3:::*SageMaker*",
 "arn:aws:s3:::*sagemaker*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "S3GetObjectOperation",
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "s3:ExistingObjectTag/SageMaker": "true"
 },
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "S3ListOperations",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

## AWS managed policy: AmazonSageMakerCanvasSMDataScienceAssistantAccess

This policy grants permissions for users in Amazon SageMaker Canvas to start conversations with Amazon Q Developer.
This feature requires permissions to both Amazon Q Developer and the SageMaker AI Data Science Assistant service.

**Permissions details**

This AWS managed policy includes the following permissions.

- `q` – Allows principals to send
  prompts to Amazon Q Developer.
- `sagemaker-data-science-assistant` – Allows principals to
  send prompts to the SageMaker Canvas Data Science Assistant service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SageMakerDataScienceAssistantAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker-data-science-assistant:SendConversation"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "AmazonQDeveloperAccess",
 "Effect": "Allow",
 "Action": [
 "q:SendMessage",
 "q:StartConversation"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

## Amazon SageMaker AI updates to Amazon SageMaker Canvas

managed policies

View details about updates to AWS managed policies for SageMaker Canvas since this service
began tracking these changes.

| Policy                                                                                                                                                                                                                                       | Version | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Date               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AmazonSageMakerCanvasSMDataScienceAssistantAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasSMDataScienceAssistantAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasSMDataScienceAssistantAccess")<br>• Update to an existing policy | 2       | Add `q:StartConversation` permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | January 14, 2025   |
| [AmazonSageMakerCanvasSMDataScienceAssistantAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasSMDataScienceAssistantAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasSMDataScienceAssistantAccess")<br>• New policy                   | 1       | Initial policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | December 4, 2024   |
| [AmazonSageMakerCanvasDataPrepFullAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasDataPrepFullAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasDataPrepFullAccess")<br>• Update to an existing policy                               | 4       | Add resource to `IAMPassOperationForEMRServerless` permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | August 16, 2024    |
| [AmazonSageMakerCanvasFullAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess")<br>• Update to an existing policy                                                       | 11      | Add resource to `IAMPassOperationForEMRServerless` permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | August 15, 2024    |
| [AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy](#security-iam-awsmanpol-AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy "#security-iam-awsmanpol-AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy")<br>• New policy       | 1       | Initial policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | July 26, 2024      |
| AmazonSageMakerCanvasDataPrepFullAccess<br>• Update to an existing policy                                                                                                                                                                    | 3       | Add `emr-serverless:CreateApplication`,<br>`emr-serverless:ListApplications`,<br>`emr-serverless:UpdateApplication`,<br>`emr-serverless:GetApplication`,<br>`emr-serverless:StartJobRun`,<br>`emr-serverless:ListJobRuns`,<br>`emr-serverless:GetJobRun`,<br>`emr-serverless:CancelJobRun`, and<br>`emr-serverless:TagResource` permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | July 18, 2024      |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing policy                                                                                                                                                                            | 10      | Add `application-autoscaling:DescribeScalingActivities`<br>`iam:PassRole`,<br>`kms:DescribeKey`, and<br>`quicksight:ListNamespaces` permissions.<br>Add `sagemaker:CreateTrainingJob`,<br>`sagemaker:CreateTransformJob`,<br>`sagemaker:DescribeTrainingJob`,<br>`sagemaker:DescribeTransformJob`,<br>`sagemaker:StopAutoMLJob`,<br>`sagemaker:StopTrainingJob`, and<br>`sagemaker:StopTransformJob` permissions.<br>Add `athena:ListTableMetadata`,<br>`athena:ListDataCatalogs`, and<br>`athena:ListDatabases` permissions.<br>Add `glue:GetDatabases`,<br>`glue:GetPartitions`, and<br>`glue:GetTables` permissions.<br>Add `emr-serverless:CreateApplication`,<br>`emr-serverless:ListApplications`,<br>`emr-serverless:UpdateApplication`,<br>`emr-serverless:StopApplication`,<br>`emr-serverless:GetApplication`,<br>`emr-serverless:StartApplication`,<br>`emr-serverless:StartJobRun`,<br>`emr-serverless:ListJobRuns`,<br>`emr-serverless:GetJobRun`,<br>`emr-serverless:CancelJobRun`, and<br>`emr-serverless:TagResource` permissions. | July 9, 2024       |
| [AmazonSageMakerCanvasBedrockAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasBedrockAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasBedrockAccess")<br>• New policy                                                                | 1       | Initial policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | February 2, 2024   |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing policy                                                                                                                                                                            | 9       | Add `sagemaker:ListEndpoints` permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | January 24, 2024   |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing policy                                                                                                                                                                            | 8       | Add `sagemaker:UpdateEndpointWeightsAndCapacities`,<br>`sagemaker:DescribeEndpointConfig`,<br>`sagemaker:InvokeEndpointAsync`,<br>`athena:ListDataCatalogs`,<br>`athena:GetQueryExecution`,<br>`athena:GetQueryResults`,<br>`athena:StartQueryExecution`,<br>`athena:StopQueryExecution`,<br>`athena:ListDatabases`,<br>`cloudwatch:DescribeAlarms`,<br>`cloudwatch:PutMetricAlarm`,<br>`cloudwatch:DeleteAlarms`, and<br>`iam:CreateServiceLinkedRole` permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | December 8, 2023   |
| AmazonSageMakerCanvasDataPrepFullAccess<br>• Update to an existing policy                                                                                                                                                                    | 2       | Small update to enforce the intents of the previous policy,<br>version 1; no permissions added or deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | December 7, 2023   |
| [AmazonSageMakerCanvasAIServicesAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess")<br>• Update to an existing policy                                     | 3       | Add `bedrock:InvokeModelWithResponseStream`,<br>`bedrock:GetModelCustomizationJob`,<br>`bedrock:StopModelCustomizationJob`,<br>`bedrock:GetCustomModel`,<br>`bedrock:GetProvisionedModelThroughput`,<br>`bedrock:DeleteProvisionedModelThroughput`,<br>`bedrock:TagResource`,<br>`bedrock:CreateModelCustomizationJob`,<br>`bedrock:CreateProvisionedModelThroughput`, and<br>`iam:PassRole` permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | November 29, 2023  |
| AmazonSageMakerCanvasDataPrepFullAccess<br>• New policy                                                                                                                                                                                      | 1       | Initial policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | October 26, 2023   |
| [AmazonSageMakerCanvasDirectDeployAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasDirectDeployAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasDirectDeployAccess")<br>• New policy                                                 | 1       | Initial policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | October 6, 2023    |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing<br>policy                                                                                                                                                                         | 7       | Add `sagemaker:DeleteEndpointConfig`,<br>`sagemaker:DeleteModel`, and<br>`sagemaker:InvokeEndpoint` permissions.<br>Also add `s3:GetObject` permission for JumpStart<br>resources in specific regions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | September 29, 2023 |
| AmazonSageMakerCanvasAIServicesAccess<br>• Update to an existing<br>policy                                                                                                                                                                   | 2       | Add `bedrock:InvokeModel` and<br>`bedrock:ListFoundationModels` permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | September 29, 2023 |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing<br>policy                                                                                                                                                                         | 6       | Add `rds:DescribeDBInstances` permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | August 29, 2023    |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing<br>policy                                                                                                                                                                         | 5       | Add `application-autoscaling:PutScalingPolicy` and<br>`application-autoscaling:RegisterScalableTarget` permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | July 24, 2023      |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing<br>policy                                                                                                                                                                         | 4       | Add `sagemaker:CreateModelPackage`,<br>`sagemaker:CreateModelPackageGroup`,<br>`sagemaker:DescribeModelPackage`,<br>`sagemaker:DescribeModelPackageGroup`,<br>`sagemaker:ListModelPackages`, and<br>`sagemaker:ListModelPackageGroups`<br>permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | May 4, 2023        |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing<br>policy                                                                                                                                                                         | 3       | Add `sagemaker:CreateAutoMLJobV2`,<br>`sagemaker:DescribeAutoMLJobV2`, and<br>`glue:SearchTables` permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | March 24, 2023     |
| AmazonSageMakerCanvasAIServicesAccess<br>• New policy                                                                                                                                                                                        | 1       | Initial policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | March 23, 2023     |
| AmazonSageMakerCanvasFullAccess<br>• Update to an existing<br>policy                                                                                                                                                                         | 2       | Add `forecast:DeleteResourceTree` permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | December 6, 2022   |
| AmazonSageMakerCanvasFullAccess<br>• New policy                                                                                                                                                                                              | 1       | Initial policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | September 8, 2022  |
| [AmazonSageMakerCanvasForecastAccess](#security-iam-awsmanpol-AmazonSageMakerCanvasForecastAccess "#security-iam-awsmanpol-AmazonSageMakerCanvasForecastAccess")<br>• New policy                                                             | 1       | Initial policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | August 24, 2022    |
