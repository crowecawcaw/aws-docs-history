# AWS Managed Policies for SageMaker Projects and JumpStart

These AWS managed policies add permissions to use built-in Amazon SageMaker AI project templates
and JumpStart solutions. The policies are available in your AWS account and are used by
execution roles created from the SageMaker AI console.

SageMaker Projects and JumpStart use AWS Service Catalog to provision AWS resources in customers'
accounts. Some created resources need to assume an execution role. For example, if AWS Service Catalog
creates a CodePipeline pipeline on behalf of a customer for a SageMaker AI machine learning CI/CD project,
then that pipeline requires an IAM role.

The
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
role has the permissions required to launch the SageMaker AI portfolio of products from AWS Service Catalog. The
[AmazonSageMakerServiceCatalogProductsUseRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsUseRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsUseRole")
role has the permissions required to use the SageMaker AI portfolio of products from AWS Service Catalog. The
`AmazonSageMakerServiceCatalogProductsLaunchRole` role passes an
`AmazonSageMakerServiceCatalogProductsUseRole` role to the provisioned AWS Service Catalog
product resources.

###### Topics

- [AWS
  managed policy: AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerPartnerServiceCatalogProductsApiGatewayServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsApiGatewayServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsApiGatewayServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerPartnerServiceCatalogProductsCloudFormationServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsCloudFormationServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsCloudFormationServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerPartnerServiceCatalogProductsLambdaServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsLambdaServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsLambdaServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerServiceCatalogProductsApiGatewayServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsApiGatewayServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsApiGatewayServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerServiceCatalogProductsCloudformationServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCloudformationServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCloudformationServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerServiceCatalogProductsEventsServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsEventsServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsEventsServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerServiceCatalogProductsGlueServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsGlueServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsGlueServiceRolePolicy")
- [AWS
  managed policy: AmazonSageMakerServiceCatalogProductsLambdaServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsLambdaServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsLambdaServiceRolePolicy")
- [Amazon SageMaker AI updates to AWS Service Catalog AWS managed
  policies](#security-iam-awsmanpol-sc-updates "#security-iam-awsmanpol-sc-updates")

## AWS

managed policy: AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy

This service role policy is used by the AWS Service Catalog service to provision products from the
Amazon SageMaker AI portfolio. The policy grants permissions to a set of related AWS
services including AWS CodePipeline, AWS CodeBuild, AWS CodeCommit, AWS Glue, AWS CloudFormation, and others.

The `AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy` policy
is intended to be used by the
`AmazonSageMakerServiceCatalogProductsLaunchRole`
role created from the SageMaker AI console. The policy adds permissions to provision AWS resources
for SageMaker Projects and JumpStart using Service Catalog to a customer's account.

**Permissions details**

This policy includes the following permissions.

- `apigateway` – Allows the role to call API Gateway endpoints that
  are tagged with `sagemaker:launch-source`.
- `cloudformation` – Allows AWS Service Catalog to create, update, and delete
  CloudFormation stacks. Also allows Service Catalog to tag and untag resources.
- `codebuild` – Allows the role assumed by AWS Service Catalog and passed to
  CloudFormation to create, update and delete CodeBuild projects.
- `codecommit` – Allows the role assumed by AWS Service Catalog and passed to
  CloudFormation to create, update and delete CodeCommit repositories.
- `codepipeline` – Allows the role assumed by AWS Service Catalog and passed to
  CloudFormation to create, update and delete CodePipelines.
- `codeconnections`, `codestar-connections` – Also allows
  the role to pass AWS CodeConnections and AWS CodeStar connections.
- `cognito-idp` – Allows the role to create, update, and delete
  groups and user pools. Also allows tagging resources.
- `ecr` – Allows the role assumed by AWS Service Catalog and passed to
  CloudFormation to create and delete Amazon ECR repositories. Also allows tagging resources.
- `events` – Allows the role assumed by AWS Service Catalog and passed to
  CloudFormation to create and delete EventBridge rules. Used for tying together the various
  components of the CICD pipeline.
- `firehose` – Allows the role to interact with Firehose streams.
- `glue` – Allows the role to interact with AWS Glue.
- `iam` – Allows the role to pass roles prepended with
  `AmazonSageMakerServiceCatalog`. This is needed when Projects provisions a
  AWS Service Catalog product, as a role needs to be passed to AWS Service Catalog.
- `lambda` – Allows the role to interact with
  AWS Lambda. Also allows tagging resources.
- `logs` – Allows the role to create, delete and access log
  streams.
- `s3` – Allows the role assumed by AWS Service Catalog and passed to
  CloudFormation to access Amazon S3 buckets where the Project template code is stored.
- `sagemaker` – Allows the role to interact with various
  SageMaker AI services. This is done both in CloudFormation during template
  provisioning, as well as in CodeBuild during CICD pipeline execution.
  Also allows tagging the following resources: endpoints, endpoint configurations,
  models, pipelines, projects, and model packages.
- `states` – Allows the role to create, delete, and update Step Functions prepended with `sagemaker`.

To view the permissions for this policy, see
[AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy.md")
in the AWS Managed Policy Reference.

## AWS

managed policy: AmazonSageMakerPartnerServiceCatalogProductsApiGatewayServiceRolePolicy

This policy is used by Amazon API Gateway within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by API Gateway that require a role.

**Permissions details**

This policy includes the following permissions.

- `lambda` – Invoke a function created by a
  partner template.
- `sagemaker` – Invoke an endpoint created by a partner template.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:*:*:function:sagemaker-*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/sagemaker:project-name": "false",
 "aws:ResourceTag/sagemaker:partner": "false"
 },
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "sagemaker:InvokeEndpoint",
 "Resource": "arn:aws:sagemaker:*:*:endpoint/*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/sagemaker:project-name": "false",
 "aws:ResourceTag/sagemaker:partner": "false"
 },
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerPartnerServiceCatalogProductsCloudFormationServiceRolePolicy

This policy is used by AWS CloudFormation within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by AWS CloudFormation that require a role.

**Permissions details**

This policy includes the following permissions.

- `iam` – Pass the
  `AmazonSageMakerServiceCatalogProductsLambdaRole` and
  `AmazonSageMakerServiceCatalogProductsApiGatewayRole` roles.
- `lambda` – Create, update, delete, and invoke AWS Lambda functions;
  retrieve, publish, and delete versions of a Lambda layer.
- `apigateway` – Create, update, and delete Amazon API Gateway resources.
- `s3` – Retrieve the `lambda-auth-code/layer.zip`
  file from an Amazon Simple Storage Service (Amazon S3) bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/service-role/AmazonSageMakerServiceCatalogProductsLambdaRole"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "lambda.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/service-role/AmazonSageMakerServiceCatalogProductsApiGatewayRole"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "apigateway.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:DeleteFunction",
 "lambda:UpdateFunctionCode",
 "lambda:ListTags",
 "lambda:InvokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:*:*:function:sagemaker-*"
 ],
 "Condition": {
 "Null": {
 "aws:ResourceTag/sagemaker:project-name": "false",
 "aws:ResourceTag/sagemaker:partner": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:CreateFunction",
 "lambda:TagResource"
 ],
 "Resource": [
 "arn:aws:lambda:*:*:function:sagemaker-*"
 ],
 "Condition": {
 "Null": {
 "aws:ResourceTag/sagemaker:project-name": "false",
 "aws:ResourceTag/sagemaker:partner": "false"
 },
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": [
 "sagemaker:project-name",
 "sagemaker:partner"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:PublishLayerVersion",
 "lambda:GetLayerVersion",
 "lambda:DeleteLayerVersion",
 "lambda:GetFunction"
 ],
 "Resource": [
 "arn:aws:lambda:*:*:layer:sagemaker-*",
 "arn:aws:lambda:*:*:function:sagemaker-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "apigateway:GET",
 "apigateway:DELETE",
 "apigateway:PATCH",
 "apigateway:POST",
 "apigateway:PUT"
 ],
 "Resource": [
 "arn:aws:apigateway:*::/restapis/*",
 "arn:aws:apigateway:*::/restapis"
 ],
 "Condition": {
 "Null": {
 "aws:ResourceTag/sagemaker:project-name": "false",
 "aws:ResourceTag/sagemaker:partner": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "apigateway:POST",
 "apigateway:PUT"
 ],
 "Resource": [
 "arn:aws:apigateway:*::/restapis",
 "arn:aws:apigateway:*::/tags/*"
 ],
 "Condition": {
 "Null": {
 "aws:ResourceTag/sagemaker:project-name": "false",
 "aws:ResourceTag/sagemaker:partner": "false"
 },
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": [
 "sagemaker:project-name",
 "sagemaker:partner"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::sagemaker-*/lambda-auth-code/layer.zip"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")

## AWS

managed policy: AmazonSageMakerPartnerServiceCatalogProductsLambdaServiceRolePolicy

This policy is used by AWS Lambda within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by Lambda that require a role.

**Permissions details**

This policy includes the following permissions.

- `secretsmanager` – Retrieve data from partner provided secrets for a partner template.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "arn:aws:secretsmanager:*:*:secret:*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/sagemaker:partner": false
 },
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")

## AWS

managed policy: AmazonSageMakerServiceCatalogProductsApiGatewayServiceRolePolicy

This policy is used by Amazon API Gateway within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by API Gateway that require a role.

**Permissions details**

This policy includes the following permissions.

- `logs` – Create and read CloudWatch Logs groups, streams, and events;
  update events; describe various resources.

These permissions are limited to resources whose log
group prefix starts with "aws/apigateway/".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DeleteLogDelivery",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:DescribeResourcePolicies",
 "logs:DescribeDestinations",
 "logs:DescribeExportTasks",
 "logs:DescribeMetricFilters",
 "logs:DescribeQueries",
 "logs:DescribeQueryDefinitions",
 "logs:DescribeSubscriptionFilters",
 "logs:GetLogDelivery",
 "logs:GetLogEvents",
 "logs:PutLogEvents",
 "logs:PutResourcePolicy",
 "logs:UpdateLogDelivery"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/apigateway/*"
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerServiceCatalogProductsCloudformationServiceRolePolicy

This policy is used by AWS CloudFormation within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by AWS CloudFormation that require a role.

**Permissions details**

This policy includes the following permissions.

- `sagemaker` – Allow access to various SageMaker AI resources excluding
  domains, user-profiles, apps, and flow definitions.
- `iam` – Pass the
  `AmazonSageMakerServiceCatalogProductsCodeBuildRole` and
  `AmazonSageMakerServiceCatalogProductsExecutionRole` roles.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:AddAssociation",
 "sagemaker:AddTags",
 "sagemaker:AssociateTrialComponent",
 "sagemaker:BatchDescribeModelPackage",
 "sagemaker:BatchGetMetrics",
 "sagemaker:BatchGetRecord",
 "sagemaker:BatchPutMetrics",
 "sagemaker:CreateAction",
 "sagemaker:CreateAlgorithm",
 "sagemaker:CreateApp",
 "sagemaker:CreateAppImageConfig",
 "sagemaker:CreateArtifact",
 "sagemaker:CreateAutoMLJob",
 "sagemaker:CreateCodeRepository",
 "sagemaker:CreateCompilationJob",
 "sagemaker:CreateContext",
 "sagemaker:CreateDataQualityJobDefinition",
 "sagemaker:CreateDeviceFleet",
 "sagemaker:CreateDomain",
 "sagemaker:CreateEdgePackagingJob",
 "sagemaker:CreateEndpoint",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:CreateExperiment",
 "sagemaker:CreateFeatureGroup",
 "sagemaker:CreateFlowDefinition",
 "sagemaker:CreateHumanTaskUi",
 "sagemaker:CreateHyperParameterTuningJob",
 "sagemaker:CreateImage",
 "sagemaker:CreateImageVersion",
 "sagemaker:CreateInferenceRecommendationsJob",
 "sagemaker:CreateLabelingJob",
 "sagemaker:CreateLineageGroupPolicy",
 "sagemaker:CreateModel",
 "sagemaker:CreateModelBiasJobDefinition",
 "sagemaker:CreateModelExplainabilityJobDefinition",
 "sagemaker:CreateModelPackage",
 "sagemaker:CreateModelPackageGroup",
 "sagemaker:CreateModelQualityJobDefinition",
 "sagemaker:CreateMonitoringSchedule",
 "sagemaker:CreateNotebookInstance",
 "sagemaker:CreateNotebookInstanceLifecycleConfig",
 "sagemaker:CreatePipeline",
 "sagemaker:CreatePresignedDomainUrl",
 "sagemaker:CreatePresignedNotebookInstanceUrl",
 "sagemaker:CreateProcessingJob",
 "sagemaker:CreateProject",
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateTransformJob",
 "sagemaker:CreateTrial",
 "sagemaker:CreateTrialComponent",
 "sagemaker:CreateUserProfile",
 "sagemaker:CreateWorkforce",
 "sagemaker:CreateWorkteam",
 "sagemaker:DeleteAction",
 "sagemaker:DeleteAlgorithm",
 "sagemaker:DeleteApp",
 "sagemaker:DeleteAppImageConfig",
 "sagemaker:DeleteArtifact",
 "sagemaker:DeleteAssociation",
 "sagemaker:DeleteCodeRepository",
 "sagemaker:DeleteContext",
 "sagemaker:DeleteDataQualityJobDefinition",
 "sagemaker:DeleteDeviceFleet",
 "sagemaker:DeleteDomain",
 "sagemaker:DeleteEndpoint",
 "sagemaker:DeleteEndpointConfig",
 "sagemaker:DeleteExperiment",
 "sagemaker:DeleteFeatureGroup",
 "sagemaker:DeleteFlowDefinition",
 "sagemaker:DeleteHumanLoop",
 "sagemaker:DeleteHumanTaskUi",
 "sagemaker:DeleteImage",
 "sagemaker:DeleteImageVersion",
 "sagemaker:DeleteLineageGroupPolicy",
 "sagemaker:DeleteModel",
 "sagemaker:DeleteModelBiasJobDefinition",
 "sagemaker:DeleteModelExplainabilityJobDefinition",
 "sagemaker:DeleteModelPackage",
 "sagemaker:DeleteModelPackageGroup",
 "sagemaker:DeleteModelPackageGroupPolicy",
 "sagemaker:DeleteModelQualityJobDefinition",
 "sagemaker:DeleteMonitoringSchedule",
 "sagemaker:DeleteNotebookInstance",
 "sagemaker:DeleteNotebookInstanceLifecycleConfig",
 "sagemaker:DeletePipeline",
 "sagemaker:DeleteProject",
 "sagemaker:DeleteRecord",
 "sagemaker:DeleteTags",
 "sagemaker:DeleteTrial",
 "sagemaker:DeleteTrialComponent",
 "sagemaker:DeleteUserProfile",
 "sagemaker:DeleteWorkforce",
 "sagemaker:DeleteWorkteam",
 "sagemaker:DeregisterDevices",
 "sagemaker:DescribeAction",
 "sagemaker:DescribeAlgorithm",
 "sagemaker:DescribeApp",
 "sagemaker:DescribeAppImageConfig",
 "sagemaker:DescribeArtifact",
 "sagemaker:DescribeAutoMLJob",
 "sagemaker:DescribeCodeRepository",
 "sagemaker:DescribeCompilationJob",
 "sagemaker:DescribeContext",
 "sagemaker:DescribeDataQualityJobDefinition",
 "sagemaker:DescribeDevice",
 "sagemaker:DescribeDeviceFleet",
 "sagemaker:DescribeDomain",
 "sagemaker:DescribeEdgePackagingJob",
 "sagemaker:DescribeEndpoint",
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:DescribeExperiment",
 "sagemaker:DescribeFeatureGroup",
 "sagemaker:DescribeFlowDefinition",
 "sagemaker:DescribeHumanLoop",
 "sagemaker:DescribeHumanTaskUi",
 "sagemaker:DescribeHyperParameterTuningJob",
 "sagemaker:DescribeImage",
 "sagemaker:DescribeImageVersion",
 "sagemaker:DescribeInferenceRecommendationsJob",
 "sagemaker:DescribeLabelingJob",
 "sagemaker:DescribeLineageGroup",
 "sagemaker:DescribeModel",
 "sagemaker:DescribeModelBiasJobDefinition",
 "sagemaker:DescribeModelExplainabilityJobDefinition",
 "sagemaker:DescribeModelPackage",
 "sagemaker:DescribeModelPackageGroup",
 "sagemaker:DescribeModelQualityJobDefinition",
 "sagemaker:DescribeMonitoringSchedule",
 "sagemaker:DescribeNotebookInstance",
 "sagemaker:DescribeNotebookInstanceLifecycleConfig",
 "sagemaker:DescribePipeline",
 "sagemaker:DescribePipelineDefinitionForExecution",
 "sagemaker:DescribePipelineExecution",
 "sagemaker:DescribeProcessingJob",
 "sagemaker:DescribeProject",
 "sagemaker:DescribeSubscribedWorkteam",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:DescribeTransformJob",
 "sagemaker:DescribeTrial",
 "sagemaker:DescribeTrialComponent",
 "sagemaker:DescribeUserProfile",
 "sagemaker:DescribeWorkforce",
 "sagemaker:DescribeWorkteam",
 "sagemaker:DisableSagemakerServicecatalogPortfolio",
 "sagemaker:DisassociateTrialComponent",
 "sagemaker:EnableSagemakerServicecatalogPortfolio",
 "sagemaker:GetDeviceFleetReport",
 "sagemaker:GetDeviceRegistration",
 "sagemaker:GetLineageGroupPolicy",
 "sagemaker:GetModelPackageGroupPolicy",
 "sagemaker:GetRecord",
 "sagemaker:GetSagemakerServicecatalogPortfolioStatus",
 "sagemaker:GetSearchSuggestions",
 "sagemaker:InvokeEndpoint",
 "sagemaker:InvokeEndpointAsync",
 "sagemaker:ListActions",
 "sagemaker:ListAlgorithms",
 "sagemaker:ListAppImageConfigs",
 "sagemaker:ListApps",
 "sagemaker:ListArtifacts",
 "sagemaker:ListAssociations",
 "sagemaker:ListAutoMLJobs",
 "sagemaker:ListCandidatesForAutoMLJob",
 "sagemaker:ListCodeRepositories",
 "sagemaker:ListCompilationJobs",
 "sagemaker:ListContexts",
 "sagemaker:ListDataQualityJobDefinitions",
 "sagemaker:ListDeviceFleets",
 "sagemaker:ListDevices",
 "sagemaker:ListDomains",
 "sagemaker:ListEdgePackagingJobs",
 "sagemaker:ListEndpointConfigs",
 "sagemaker:ListEndpoints",
 "sagemaker:ListExperiments",
 "sagemaker:ListFeatureGroups",
 "sagemaker:ListFlowDefinitions",
 "sagemaker:ListHumanLoops",
 "sagemaker:ListHumanTaskUis",
 "sagemaker:ListHyperParameterTuningJobs",
 "sagemaker:ListImageVersions",
 "sagemaker:ListImages",
 "sagemaker:ListInferenceRecommendationsJobs",
 "sagemaker:ListLabelingJobs",
 "sagemaker:ListLabelingJobsForWorkteam",
 "sagemaker:ListLineageGroups",
 "sagemaker:ListModelBiasJobDefinitions",
 "sagemaker:ListModelExplainabilityJobDefinitions",
 "sagemaker:ListModelMetadata",
 "sagemaker:ListModelPackageGroups",
 "sagemaker:ListModelPackages",
 "sagemaker:ListModelQualityJobDefinitions",
 "sagemaker:ListModels",
 "sagemaker:ListMonitoringExecutions",
 "sagemaker:ListMonitoringSchedules",
 "sagemaker:ListNotebookInstanceLifecycleConfigs",
 "sagemaker:ListNotebookInstances",
 "sagemaker:ListPipelineExecutionSteps",
 "sagemaker:ListPipelineExecutions",
 "sagemaker:ListPipelineParametersForExecution",
 "sagemaker:ListPipelines",
 "sagemaker:ListProcessingJobs",
 "sagemaker:ListProjects",
 "sagemaker:ListSubscribedWorkteams",
 "sagemaker:ListTags",
 "sagemaker:ListTrainingJobs",
 "sagemaker:ListTrainingJobsForHyperParameterTuningJob",
 "sagemaker:ListTransformJobs",
 "sagemaker:ListTrialComponents",
 "sagemaker:ListTrials",
 "sagemaker:ListUserProfiles",
 "sagemaker:ListWorkforces",
 "sagemaker:ListWorkteams",
 "sagemaker:PutLineageGroupPolicy",
 "sagemaker:PutModelPackageGroupPolicy",
 "sagemaker:PutRecord",
 "sagemaker:QueryLineage",
 "sagemaker:RegisterDevices",
 "sagemaker:RenderUiTemplate",
 "sagemaker:Search",
 "sagemaker:SendHeartbeat",
 "sagemaker:SendPipelineExecutionStepFailure",
 "sagemaker:SendPipelineExecutionStepSuccess",
 "sagemaker:StartHumanLoop",
 "sagemaker:StartMonitoringSchedule",
 "sagemaker:StartNotebookInstance",
 "sagemaker:StartPipelineExecution",
 "sagemaker:StopAutoMLJob",
 "sagemaker:StopCompilationJob",
 "sagemaker:StopEdgePackagingJob",
 "sagemaker:StopHumanLoop",
 "sagemaker:StopHyperParameterTuningJob",
 "sagemaker:StopInferenceRecommendationsJob",
 "sagemaker:StopLabelingJob",
 "sagemaker:StopMonitoringSchedule",
 "sagemaker:StopNotebookInstance",
 "sagemaker:StopPipelineExecution",
 "sagemaker:StopProcessingJob",
 "sagemaker:StopTrainingJob",
 "sagemaker:StopTransformJob",
 "sagemaker:UpdateAction",
 "sagemaker:UpdateAppImageConfig",
 "sagemaker:UpdateArtifact",
 "sagemaker:UpdateCodeRepository",
 "sagemaker:UpdateContext",
 "sagemaker:UpdateDeviceFleet",
 "sagemaker:UpdateDevices",
 "sagemaker:UpdateDomain",
 "sagemaker:UpdateEndpoint",
 "sagemaker:UpdateEndpointWeightsAndCapacities",
 "sagemaker:UpdateExperiment",
 "sagemaker:UpdateImage",
 "sagemaker:UpdateModelPackage",
 "sagemaker:UpdateMonitoringSchedule",
 "sagemaker:UpdateNotebookInstance",
 "sagemaker:UpdateNotebookInstanceLifecycleConfig",
 "sagemaker:UpdatePipeline",
 "sagemaker:UpdatePipelineExecution",
 "sagemaker:UpdateProject",
 "sagemaker:UpdateTrainingJob",
 "sagemaker:UpdateTrial",
 "sagemaker:UpdateTrialComponent",
 "sagemaker:UpdateUserProfile",
 "sagemaker:UpdateWorkforce",
 "sagemaker:UpdateWorkteam"
 ],
 "NotResource": [
 "arn:aws:sagemaker:*:*:domain/*",
 "arn:aws:sagemaker:*:*:user-profile/*",
 "arn:aws:sagemaker:*:*:app/*",
 "arn:aws:sagemaker:*:*:flow-definition/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/service-role/AmazonSageMakerServiceCatalogProductsCodeBuildRole",
 "arn:aws:iam::*:role/service-role/AmazonSageMakerServiceCatalogProductsExecutionRole"
 ]
 }
 ]
}`

```

[Show moreShow less](# "#")

## AWS

managed policy: AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy

This policy is used by AWS CodeBuild within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by CodeBuild that require a role.

**Permissions details**

This policy includes the following permissions.

- `sagemaker` – Allow access to various SageMaker AI resources.
- `codecommit` – Upload CodeCommit archives to CodeBuild pipelines, get
  upload status, and cancel uploads; get branch and commit information.
  These permissions are limited to resources whose name starts with "sagemaker-".
- `ecr` – Create Amazon ECR repositories and container images; upload
  image layers. These permissions are limited to repositories whose name starts with "sagemaker-".

`ecr` – Read all resources.

- `iam` – Pass the following roles:
  - `AmazonSageMakerServiceCatalogProductsCloudformationRole` to AWS CloudFormation.
  - `AmazonSageMakerServiceCatalogProductsCodeBuildRole` to AWS CodeBuild.
  - `AmazonSageMakerServiceCatalogProductsCodePipelineRole` to AWS CodePipeline.
  - `AmazonSageMakerServiceCatalogProductsEventsRole` to Amazon EventBridge.
  - `AmazonSageMakerServiceCatalogProductsExecutionRole` to Amazon SageMaker AI.

- `logs` – Create and read CloudWatch Logs groups, streams, and events;
  update events; describe various resources.

These permissions are limited to resources
whose name prefix starts with "aws/codebuild/".

- `s3` – Create, read, and list Amazon S3 buckets. These permissions
  are limited to buckets whose name starts with "sagemaker-".
- `codeconnections`, `codestar-connections` – Use
  AWS CodeConnections and AWS CodeStar connections.

To view the permissions for this policy, see
[AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy.md")
in the AWS Managed Policy Reference.

## AWS

managed policy: AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy

This policy is used by AWS CodePipeline within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by CodePipeline that require a role.

**Permissions details**

This policy includes the following permissions.

- `cloudformation` – Create, read, delete, and update CloudFormation
  stacks; create, read, delete, and execute change sets; set stack policy; tag and untag
  resources. These permissions are limited to resources whose name starts with "sagemaker-".
- `s3` – Create, read, list, and delete Amazon S3 buckets;
  add, read, and delete objects from the buckets;
  read and set the CORS configuration; read the access control list (ACL); and read the
  AWS Region the bucket resides in.

These permissions are limited to buckets whose name
starts with "sagemaker-" or "aws-glue-.

- `iam` – Pass the
  `AmazonSageMakerServiceCatalogProductsCloudformationRole` role.
- `codebuild` – Get CodeBuild build information and start builds.
  These permissions are limited to project and build resources whose name starts with
  "sagemaker-".
- `codecommit` – Upload CodeCommit archives to CodeBuild pipelines, get
  upload status, and cancel uploads; get branch and commit information.
- `codeconnections`, `codestar-connections` – Use AWS CodeConnections and AWS CodeStar connections.

To view the permissions for this policy, see
[AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy.md")
in the AWS Managed Policy Reference.

## AWS

managed policy: AmazonSageMakerServiceCatalogProductsEventsServiceRolePolicy

This policy is used by Amazon EventBridge within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by EventBridge that require a role.

**Permissions details**

This policy includes the following permissions.

- `codepipeline` – Start a CodeBuild execution. These
  permissions are limited to pipelines whose name starts with "sagemaker-".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codepipeline:StartPipelineExecution",
 "Resource": "arn:aws:codepipeline:*:*:sagemaker-*"
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy

This policy is used by Amazon Data Firehose within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by Firehose that require a role.

**Permissions details**

This policy includes the following permissions.

- `firehose` – Send Firehose records. These permissions are limited
  to resources whose delivery stream name starts with "sagemaker-".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "firehose:PutRecord",
 "firehose:PutRecordBatch"
 ],
 "Resource": "arn:aws:firehose:*:*:deliverystream/sagemaker-*"
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerServiceCatalogProductsGlueServiceRolePolicy

This policy is used by AWS Glue within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by Glue that require a role.

**Permissions details**

This policy includes the following permissions.

- `glue` – Create, read, and delete AWS Glue partitions, tables,
  and table versions. These permissions are limited to those resources whose name starts
  with "sagemaker-". Create and read AWS Glue databases. These permissions are limited
  to databases whose name is "default", "global_temp", or starts with "sagemaker-".
  Get user defined functions.
- `s3` – Create, read, list, and delete Amazon S3 buckets;
  add, read, and delete objects from the buckets;
  read and set the CORS configuration; read the access control list (ACL), and read the
  AWS Region the bucket resides in.

These permissions are limited to buckets whose name
starts with "sagemaker-" or "aws-glue-".

- `logs` – Create, read, and delete CloudWatch Logs log group, streams, and
  deliveries; and create a resource policy.

These permissions are limited to resources
whose name prefix starts with "aws/glue/".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:BatchCreatePartition",
 "glue:BatchDeletePartition",
 "glue:BatchDeleteTable",
 "glue:BatchDeleteTableVersion",
 "glue:BatchGetPartition",
 "glue:CreateDatabase",
 "glue:CreatePartition",
 "glue:CreateTable",
 "glue:DeletePartition",
 "glue:DeleteTable",
 "glue:DeleteTableVersion",
 "glue:GetDatabase",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetTableVersion",
 "glue:GetTableVersions",
 "glue:SearchTables",
 "glue:UpdatePartition",
 "glue:UpdateTable",
 "glue:GetUserDefinedFunctions"
 ],
 "Resource": [
 "arn:aws:glue:*:*:catalog",
 "arn:aws:glue:*:*:database/default",
 "arn:aws:glue:*:*:database/global_temp",
 "arn:aws:glue:*:*:database/sagemaker-*",
 "arn:aws:glue:*:*:table/sagemaker-*",
 "arn:aws:glue:*:*:tableVersion/sagemaker-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:DeleteBucket",
 "s3:GetBucketAcl",
 "s3:GetBucketCors",
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:PutBucketCors"
 ],
 "Resource": [
 "arn:aws:s3:::aws-glue-*",
 "arn:aws:s3:::sagemaker-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::aws-glue-*",
 "arn:aws:s3:::sagemaker-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DeleteLogDelivery",
 "logs:Describe*",
 "logs:GetLogDelivery",
 "logs:GetLogEvents",
 "logs:ListLogDeliveries",
 "logs:PutLogEvents",
 "logs:PutResourcePolicy",
 "logs:UpdateLogDelivery"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/glue/*"
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerServiceCatalogProductsLambdaServiceRolePolicy

This policy is used by AWS Lambda within the AWS Service Catalog provisioned products from the
Amazon SageMaker AI portfolio. The policy is intended to be attached to an IAM role that the
[AmazonSageMakerServiceCatalogProductsLaunchRole](https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole "https://console.aws.amazon.com/iam/home?#/roles/AmazonSageMakerServiceCatalogProductsLaunchRole")
passes to the AWS resources created by Lambda that require a role.

**Permissions details**

This policy includes the following permissions.

- `sagemaker` – Allow access to various SageMaker AI resources.
- `ecr` – Create and delete Amazon ECR repositories; create, read,
  and delete container images; upload image layers. These permissions are
  limited to repositories whose name starts with "sagemaker-".
- `events` – Create, read, and delete Amazon EventBridge rules;
  and create and remove targets. These permissions are limited to rules whose name
  starts with "sagemaker-".
- `s3` – Create, read, list, and delete Amazon S3 buckets;
  add, read, and delete objects from the buckets;
  read and set the CORS configuration; read the access control list (ACL), and read the
  AWS Region the bucket resides in.

These permissions are limited to buckets whose name
starts with "sagemaker-" or "aws-glue-".

- `iam` – Pass the
  `AmazonSageMakerServiceCatalogProductsExecutionRole` role.
- `logs` – Create, read, and delete CloudWatch Logs log group, streams, and
  deliveries; and create a resource policy.

These permissions are limited to resources
whose name prefix starts with "aws/lambda/".

- `codebuild` – Start and get information about AWS CodeBuild builds.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid" : "AmazonSageMakerLambdaECRPermission",
 "Effect": "Allow",
 "Action": [
 "ecr:DescribeImages",
 "ecr:BatchDeleteImage",
 "ecr:CompleteLayerUpload",
 "ecr:CreateRepository",
 "ecr:DeleteRepository",
 "ecr:InitiateLayerUpload",
 "ecr:PutImage",
 "ecr:UploadLayerPart"
 ],
 "Resource": [
 "arn:aws:ecr:*:*:repository/sagemaker-*"
 ]
 },
 {
 "Sid" : "AmazonSageMakerLambdaEventBridgePermission",
 "Effect": "Allow",
 "Action": [
 "events:DeleteRule",
 "events:DescribeRule",
 "events:PutRule",
 "events:PutTargets",
 "events:RemoveTargets"
 ],
 "Resource": [
 "arn:aws:events:*:*:rule/sagemaker-*"
 ]
 },
 {
 "Sid" : "AmazonSageMakerLambdaS3BucketPermission",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:DeleteBucket",
 "s3:GetBucketAcl",
 "s3:GetBucketCors",
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:PutBucketCors"
 ],
 "Resource": [
 "arn:aws:s3:::aws-glue-*",
 "arn:aws:s3:::sagemaker-*"
 ]
 },
 {
 "Sid" : "AmazonSageMakerLambdaS3ObjectPermission",
 "Effect": "Allow",
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::aws-glue-*",
 "arn:aws:s3:::sagemaker-*"
 ]
 },
 {
 "Sid" : "AmazonSageMakerLambdaSageMakerPermission",
 "Effect": "Allow",
 "Action": [
 "sagemaker:AddAssociation",
 "sagemaker:AddTags",
 "sagemaker:AssociateTrialComponent",
 "sagemaker:BatchDescribeModelPackage",
 "sagemaker:BatchGetMetrics",
 "sagemaker:BatchGetRecord",
 "sagemaker:BatchPutMetrics",
 "sagemaker:CreateAction",
 "sagemaker:CreateAlgorithm",
 "sagemaker:CreateApp",
 "sagemaker:CreateAppImageConfig",
 "sagemaker:CreateArtifact",
 "sagemaker:CreateAutoMLJob",
 "sagemaker:CreateCodeRepository",
 "sagemaker:CreateCompilationJob",
 "sagemaker:CreateContext",
 "sagemaker:CreateDataQualityJobDefinition",
 "sagemaker:CreateDeviceFleet",
 "sagemaker:CreateDomain",
 "sagemaker:CreateEdgePackagingJob",
 "sagemaker:CreateEndpoint",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:CreateExperiment",
 "sagemaker:CreateFeatureGroup",
 "sagemaker:CreateFlowDefinition",
 "sagemaker:CreateHumanTaskUi",
 "sagemaker:CreateHyperParameterTuningJob",
 "sagemaker:CreateImage",
 "sagemaker:CreateImageVersion",
 "sagemaker:CreateInferenceRecommendationsJob",
 "sagemaker:CreateLabelingJob",
 "sagemaker:CreateLineageGroupPolicy",
 "sagemaker:CreateModel",
 "sagemaker:CreateModelBiasJobDefinition",
 "sagemaker:CreateModelExplainabilityJobDefinition",
 "sagemaker:CreateModelPackage",
 "sagemaker:CreateModelPackageGroup",
 "sagemaker:CreateModelQualityJobDefinition",
 "sagemaker:CreateMonitoringSchedule",
 "sagemaker:CreateNotebookInstance",
 "sagemaker:CreateNotebookInstanceLifecycleConfig",
 "sagemaker:CreatePipeline",
 "sagemaker:CreatePresignedDomainUrl",
 "sagemaker:CreatePresignedNotebookInstanceUrl",
 "sagemaker:CreateProcessingJob",
 "sagemaker:CreateProject",
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateTransformJob",
 "sagemaker:CreateTrial",
 "sagemaker:CreateTrialComponent",
 "sagemaker:CreateUserProfile",
 "sagemaker:CreateWorkforce",
 "sagemaker:CreateWorkteam",
 "sagemaker:DeleteAction",
 "sagemaker:DeleteAlgorithm",
 "sagemaker:DeleteApp",
 "sagemaker:DeleteAppImageConfig",
 "sagemaker:DeleteArtifact",
 "sagemaker:DeleteAssociation",
 "sagemaker:DeleteCodeRepository",
 "sagemaker:DeleteContext",
 "sagemaker:DeleteDataQualityJobDefinition",
 "sagemaker:DeleteDeviceFleet",
 "sagemaker:DeleteDomain",
 "sagemaker:DeleteEndpoint",
 "sagemaker:DeleteEndpointConfig",
 "sagemaker:DeleteExperiment",
 "sagemaker:DeleteFeatureGroup",
 "sagemaker:DeleteFlowDefinition",
 "sagemaker:DeleteHumanLoop",
 "sagemaker:DeleteHumanTaskUi",
 "sagemaker:DeleteImage",
 "sagemaker:DeleteImageVersion",
 "sagemaker:DeleteLineageGroupPolicy",
 "sagemaker:DeleteModel",
 "sagemaker:DeleteModelBiasJobDefinition",
 "sagemaker:DeleteModelExplainabilityJobDefinition",
 "sagemaker:DeleteModelPackage",
 "sagemaker:DeleteModelPackageGroup",
 "sagemaker:DeleteModelPackageGroupPolicy",
 "sagemaker:DeleteModelQualityJobDefinition",
 "sagemaker:DeleteMonitoringSchedule",
 "sagemaker:DeleteNotebookInstance",
 "sagemaker:DeleteNotebookInstanceLifecycleConfig",
 "sagemaker:DeletePipeline",
 "sagemaker:DeleteProject",
 "sagemaker:DeleteRecord",
 "sagemaker:DeleteTags",
 "sagemaker:DeleteTrial",
 "sagemaker:DeleteTrialComponent",
 "sagemaker:DeleteUserProfile",
 "sagemaker:DeleteWorkforce",
 "sagemaker:DeleteWorkteam",
 "sagemaker:DeregisterDevices",
 "sagemaker:DescribeAction",
 "sagemaker:DescribeAlgorithm",
 "sagemaker:DescribeApp",
 "sagemaker:DescribeAppImageConfig",
 "sagemaker:DescribeArtifact",
 "sagemaker:DescribeAutoMLJob",
 "sagemaker:DescribeCodeRepository",
 "sagemaker:DescribeCompilationJob",
 "sagemaker:DescribeContext",
 "sagemaker:DescribeDataQualityJobDefinition",
 "sagemaker:DescribeDevice",
 "sagemaker:DescribeDeviceFleet",
 "sagemaker:DescribeDomain",
 "sagemaker:DescribeEdgePackagingJob",
 "sagemaker:DescribeEndpoint",
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:DescribeExperiment",
 "sagemaker:DescribeFeatureGroup",
 "sagemaker:DescribeFlowDefinition",
 "sagemaker:DescribeHumanLoop",
 "sagemaker:DescribeHumanTaskUi",
 "sagemaker:DescribeHyperParameterTuningJob",
 "sagemaker:DescribeImage",
 "sagemaker:DescribeImageVersion",
 "sagemaker:DescribeInferenceRecommendationsJob",
 "sagemaker:DescribeLabelingJob",
 "sagemaker:DescribeLineageGroup",
 "sagemaker:DescribeModel",
 "sagemaker:DescribeModelBiasJobDefinition",
 "sagemaker:DescribeModelExplainabilityJobDefinition",
 "sagemaker:DescribeModelPackage",
 "sagemaker:DescribeModelPackageGroup",
 "sagemaker:DescribeModelQualityJobDefinition",
 "sagemaker:DescribeMonitoringSchedule",
 "sagemaker:DescribeNotebookInstance",
 "sagemaker:DescribeNotebookInstanceLifecycleConfig",
 "sagemaker:DescribePipeline",
 "sagemaker:DescribePipelineDefinitionForExecution",
 "sagemaker:DescribePipelineExecution",
 "sagemaker:DescribeProcessingJob",
 "sagemaker:DescribeProject",
 "sagemaker:DescribeSubscribedWorkteam",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:DescribeTransformJob",
 "sagemaker:DescribeTrial",
 "sagemaker:DescribeTrialComponent",
 "sagemaker:DescribeUserProfile",
 "sagemaker:DescribeWorkforce",
 "sagemaker:DescribeWorkteam",
 "sagemaker:DisableSagemakerServicecatalogPortfolio",
 "sagemaker:DisassociateTrialComponent",
 "sagemaker:EnableSagemakerServicecatalogPortfolio",
 "sagemaker:GetDeviceFleetReport",
 "sagemaker:GetDeviceRegistration",
 "sagemaker:GetLineageGroupPolicy",
 "sagemaker:GetModelPackageGroupPolicy",
 "sagemaker:GetRecord",
 "sagemaker:GetSagemakerServicecatalogPortfolioStatus",
 "sagemaker:GetSearchSuggestions",
 "sagemaker:InvokeEndpoint",
 "sagemaker:InvokeEndpointAsync",
 "sagemaker:ListActions",
 "sagemaker:ListAlgorithms",
 "sagemaker:ListAppImageConfigs",
 "sagemaker:ListApps",
 "sagemaker:ListArtifacts",
 "sagemaker:ListAssociations",
 "sagemaker:ListAutoMLJobs",
 "sagemaker:ListCandidatesForAutoMLJob",
 "sagemaker:ListCodeRepositories",
 "sagemaker:ListCompilationJobs",
 "sagemaker:ListContexts",
 "sagemaker:ListDataQualityJobDefinitions",
 "sagemaker:ListDeviceFleets",
 "sagemaker:ListDevices",
 "sagemaker:ListDomains",
 "sagemaker:ListEdgePackagingJobs",
 "sagemaker:ListEndpointConfigs",
 "sagemaker:ListEndpoints",
 "sagemaker:ListExperiments",
 "sagemaker:ListFeatureGroups",
 "sagemaker:ListFlowDefinitions",
 "sagemaker:ListHumanLoops",
 "sagemaker:ListHumanTaskUis",
 "sagemaker:ListHyperParameterTuningJobs",
 "sagemaker:ListImageVersions",
 "sagemaker:ListImages",
 "sagemaker:ListInferenceRecommendationsJobs",
 "sagemaker:ListLabelingJobs",
 "sagemaker:ListLabelingJobsForWorkteam",
 "sagemaker:ListLineageGroups",
 "sagemaker:ListModelBiasJobDefinitions",
 "sagemaker:ListModelExplainabilityJobDefinitions",
 "sagemaker:ListModelMetadata",
 "sagemaker:ListModelPackageGroups",
 "sagemaker:ListModelPackages",
 "sagemaker:ListModelQualityJobDefinitions",
 "sagemaker:ListModels",
 "sagemaker:ListMonitoringExecutions",
 "sagemaker:ListMonitoringSchedules",
 "sagemaker:ListNotebookInstanceLifecycleConfigs",
 "sagemaker:ListNotebookInstances",
 "sagemaker:ListPipelineExecutionSteps",
 "sagemaker:ListPipelineExecutions",
 "sagemaker:ListPipelineParametersForExecution",
 "sagemaker:ListPipelines",
 "sagemaker:ListProcessingJobs",
 "sagemaker:ListProjects",
 "sagemaker:ListSubscribedWorkteams",
 "sagemaker:ListTags",
 "sagemaker:ListTrainingJobs",
 "sagemaker:ListTrainingJobsForHyperParameterTuningJob",
 "sagemaker:ListTransformJobs",
 "sagemaker:ListTrialComponents",
 "sagemaker:ListTrials",
 "sagemaker:ListUserProfiles",
 "sagemaker:ListWorkforces",
 "sagemaker:ListWorkteams",
 "sagemaker:PutLineageGroupPolicy",
 "sagemaker:PutModelPackageGroupPolicy",
 "sagemaker:PutRecord",
 "sagemaker:QueryLineage",
 "sagemaker:RegisterDevices",
 "sagemaker:RenderUiTemplate",
 "sagemaker:Search",
 "sagemaker:SendHeartbeat",
 "sagemaker:SendPipelineExecutionStepFailure",
 "sagemaker:SendPipelineExecutionStepSuccess",
 "sagemaker:StartHumanLoop",
 "sagemaker:StartMonitoringSchedule",
 "sagemaker:StartNotebookInstance",
 "sagemaker:StartPipelineExecution",
 "sagemaker:StopAutoMLJob",
 "sagemaker:StopCompilationJob",
 "sagemaker:StopEdgePackagingJob",
 "sagemaker:StopHumanLoop",
 "sagemaker:StopHyperParameterTuningJob",
 "sagemaker:StopInferenceRecommendationsJob",
 "sagemaker:StopLabelingJob",
 "sagemaker:StopMonitoringSchedule",
 "sagemaker:StopNotebookInstance",
 "sagemaker:StopPipelineExecution",
 "sagemaker:StopProcessingJob",
 "sagemaker:StopTrainingJob",
 "sagemaker:StopTransformJob",
 "sagemaker:UpdateAction",
 "sagemaker:UpdateAppImageConfig",
 "sagemaker:UpdateArtifact",
 "sagemaker:UpdateCodeRepository",
 "sagemaker:UpdateContext",
 "sagemaker:UpdateDeviceFleet",
 "sagemaker:UpdateDevices",
 "sagemaker:UpdateDomain",
 "sagemaker:UpdateEndpoint",
 "sagemaker:UpdateEndpointWeightsAndCapacities",
 "sagemaker:UpdateExperiment",
 "sagemaker:UpdateImage",
 "sagemaker:UpdateModelPackage",
 "sagemaker:UpdateMonitoringSchedule",
 "sagemaker:UpdateNotebookInstance",
 "sagemaker:UpdateNotebookInstanceLifecycleConfig",
 "sagemaker:UpdatePipeline",
 "sagemaker:UpdatePipelineExecution",
 "sagemaker:UpdateProject",
 "sagemaker:UpdateTrainingJob",
 "sagemaker:UpdateTrial",
 "sagemaker:UpdateTrialComponent",
 "sagemaker:UpdateUserProfile",
 "sagemaker:UpdateWorkforce",
 "sagemaker:UpdateWorkteam"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:action/*",
 "arn:aws:sagemaker:*:*:algorithm/*",
 "arn:aws:sagemaker:*:*:app-image-config/*",
 "arn:aws:sagemaker:*:*:artifact/*",
 "arn:aws:sagemaker:*:*:automl-job/*",
 "arn:aws:sagemaker:*:*:code-repository/*",
 "arn:aws:sagemaker:*:*:compilation-job/*",
 "arn:aws:sagemaker:*:*:context/*",
 "arn:aws:sagemaker:*:*:data-quality-job-definition/*",
 "arn:aws:sagemaker:*:*:device-fleet/*/device/*",
 "arn:aws:sagemaker:*:*:device-fleet/*",
 "arn:aws:sagemaker:*:*:edge-packaging-job/*",
 "arn:aws:sagemaker:*:*:endpoint/*",
 "arn:aws:sagemaker:*:*:endpoint-config/*",
 "arn:aws:sagemaker:*:*:experiment/*",
 "arn:aws:sagemaker:*:*:experiment-trial/*",
 "arn:aws:sagemaker:*:*:experiment-trial-component/*",
 "arn:aws:sagemaker:*:*:feature-group/*",
 "arn:aws:sagemaker:*:*:human-loop/*",
 "arn:aws:sagemaker:*:*:human-task-ui/*",
 "arn:aws:sagemaker:*:*:hyper-parameter-tuning-job/*",
 "arn:aws:sagemaker:*:*:image/*",
 "arn:aws:sagemaker:*:*:image-version/*/*",
 "arn:aws:sagemaker:*:*:inference-recommendations-job/*",
 "arn:aws:sagemaker:*:*:labeling-job/*",
 "arn:aws:sagemaker:*:*:model/*",
 "arn:aws:sagemaker:*:*:model-bias-job-definition/*",
 "arn:aws:sagemaker:*:*:model-explainability-job-definition/*",
 "arn:aws:sagemaker:*:*:model-package/*",
 "arn:aws:sagemaker:*:*:model-package-group/*",
 "arn:aws:sagemaker:*:*:model-quality-job-definition/*",
 "arn:aws:sagemaker:*:*:monitoring-schedule/*",
 "arn:aws:sagemaker:*:*:notebook-instance/*",
 "arn:aws:sagemaker:*:*:notebook-instance-lifecycle-config/*",
 "arn:aws:sagemaker:*:*:pipeline/*",
 "arn:aws:sagemaker:*:*:pipeline/*/execution/*",
 "arn:aws:sagemaker:*:*:processing-job/*",
 "arn:aws:sagemaker:*:*:project/*",
 "arn:aws:sagemaker:*:*:training-job/*",
 "arn:aws:sagemaker:*:*:transform-job/*",
 "arn:aws:sagemaker:*:*:workforce/*",
 "arn:aws:sagemaker:*:*:workteam/*"
 ]
 },
 {
 "Sid" : "AmazonSageMakerLambdaPassRolePermission",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/service-role/AmazonSageMakerServiceCatalogProductsExecutionRole"
 ]
 },
 {
 "Sid" : "AmazonSageMakerLambdaLogPermission",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DeleteLogDelivery",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:DescribeResourcePolicies",
 "logs:DescribeDestinations",
 "logs:DescribeExportTasks",
 "logs:DescribeMetricFilters",
 "logs:DescribeQueries",
 "logs:DescribeQueryDefinitions",
 "logs:DescribeSubscriptionFilters",
 "logs:GetLogDelivery",
 "logs:GetLogEvents",
 "logs:ListLogDeliveries",
 "logs:PutLogEvents",
 "logs:PutResourcePolicy",
 "logs:UpdateLogDelivery"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/lambda/*"
 },
 {
 "Sid" : "AmazonSageMakerLambdaCodeBuildPermission",
 "Effect": "Allow",
 "Action": [
 "codebuild:StartBuild",
 "codebuild:BatchGetBuilds"
 ],
 "Resource": "arn:aws:codebuild:*:*:project/sagemaker-*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/sagemaker:project-name": "*"
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")

## Amazon SageMaker AI updates to AWS Service Catalog AWS managed

policies

View details about updates to AWS managed policies for Amazon SageMaker AI since this service
began tracking these changes.

| Policy                                                                                                                                                                                                                                                                                   | Version | Change                                                                                                                                                                      | Date               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy")<br>• Updated policy                          | 10      | Updated `codestar-connections:PassConnection` and<br>`codeconnections:PassConnection` permissions.                                                                          | September 27, 2025 |
| [AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy")<br>• Updated policy        | 3       | Updated `codestar-connections:UseConnection` and<br>`codeconnections:UseConnection` permissions.                                                                            | September 27, 2025 |
| [AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy")<br>• Updated policy                 | 3       | Updated `codestar-connections:UseConnection` and<br>`codeconnections:UseConnection` permissions.                                                                            | September 27, 2025 |
| [AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy")<br>• Updated policy                          | 9       | Add `cloudformation:TagResource`, `cloudformation:UntagResource`,<br>and `codeconnections:PassConnection` permissions.                                                      | July 1, 2024       |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy<br>• Updated policy                                                                                                                                                                                                         | 7       | Roll back the policy to version 7 (v7). Remove<br>`cloudformation:TagResource`, `cloudformation:UntagResource`,<br>and `codeconnections:PassConnection` permissions.        | June 12, 2024      |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy<br>• Updated policy                                                                                                                                                                                                         | 8       | Add `cloudformation:TagResource`, `cloudformation:UntagResource`,<br>and `codeconnections:PassConnection` permissions.                                                      | June 11, 2024      |
| [AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy")<br>• Updated policy                 | 2       | Add `codestar-connections:UseConnection` and `codeconnections:UseConnection` permissions.                                                                                   | June 11, 2024      |
| [AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy")<br>• Updated policy        | 2       | Add `cloudformation:TagResource`, `cloudformation:UntagResource`,<br>`codestar-connections:UseConnection` and `codeconnections:UseConnection` permissions.                  | June 11, 2024      |
| [AmazonSageMakerServiceCatalogProductsLambdaServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsLambdaServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsLambdaServiceRolePolicy")<br>• Updated policy                          | 2       | Add `codebuild:StartBuild` and `codebuild:BatchGetBuilds` permissions.                                                                                                      | June 11, 2024      |
| [AmazonSageMakerPartnerServiceCatalogProductsApiGatewayServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsApiGatewayServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsApiGatewayServiceRolePolicy")             | 1       | Initial policy                                                                                                                                                              | August 1, 2023     |
| [AmazonSageMakerPartnerServiceCatalogProductsCloudFormationServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsCloudFormationServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsCloudFormationServiceRolePolicy") | 1       | Initial policy                                                                                                                                                              | August 1, 2023     |
| [AmazonSageMakerPartnerServiceCatalogProductsLambdaServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsLambdaServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerPartnerServiceCatalogProductsLambdaServiceRolePolicy")                         | 1       | Initial policy                                                                                                                                                              | August 1, 2023     |
| [AmazonSageMakerServiceCatalogProductsGlueServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsGlueServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsGlueServiceRolePolicy")<br>• Updated policy                                | 2       | Add permission for `glue:GetUserDefinedFunctions`.                                                                                                                          | August 26, 2022    |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy<br>• Updated policy                                                                                                                                                                                                         | 7       | Add permission for `sagemaker:AddTags`.                                                                                                                                     | August 2, 2022     |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy<br>• Updated policy                                                                                                                                                                                                         | 6       | Add permission for `lambda:TagResource`.                                                                                                                                    | July 14, 2022      |
| AmazonSageMakerServiceCatalogProductsLambdaServiceRolePolicy                                                                                                                                                                                                                             | 1       | Initial policy                                                                                                                                                              | April 4, 2022      |
| [AmazonSageMakerServiceCatalogProductsApiGatewayServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsApiGatewayServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsApiGatewayServiceRolePolicy")                                  | 1       | Initial policy                                                                                                                                                              | March 24, 2022     |
| [AmazonSageMakerServiceCatalogProductsCloudformationServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCloudformationServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsCloudformationServiceRolePolicy")                      | 1       | Initial policy                                                                                                                                                              | March 24, 2022     |
| AmazonSageMakerServiceCatalogProductsCodeBuildServiceRolePolicy                                                                                                                                                                                                                          | 1       | Initial policy                                                                                                                                                              | March 24, 2022     |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy<br>• Updated policy                                                                                                                                                                                                         | 5       | Add permission for `ecr-idp:TagResource`.                                                                                                                                   | March 21, 2022     |
| AmazonSageMakerServiceCatalogProductsCodePipelineServiceRolePolicy                                                                                                                                                                                                                       | 1       | Initial policy                                                                                                                                                              | February 22, 2022  |
| [AmazonSageMakerServiceCatalogProductsEventsServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsEventsServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsEventsServiceRolePolicy")                                              | 1       | Initial policy                                                                                                                                                              | February 22, 2022  |
| [AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy")                                        | 1       | Initial policy                                                                                                                                                              | February 22, 2022  |
| AmazonSageMakerServiceCatalogProductsGlueServiceRolePolicy                                                                                                                                                                                                                               | 1       | Initial policy                                                                                                                                                              | February 22, 2022  |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy<br>• Updated policy                                                                                                                                                                                                         | 4       | Add permissions for `cognito-idp:TagResource` and<br>`s3:PutBucketCORS`.                                                                                                    | February 16, 2022  |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy<br>• Updated policy                                                                                                                                                                                                         | 3       | Add new permissions for `sagemaker`.<br>Create, read, update, and delete SageMaker Images.                                                                                  | September 15, 2021 |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy<br>• Updated policy                                                                                                                                                                                                         | 2       | Add permissions for `sagemaker` and<br>`codestar-connections`.<br>Create, read, update, and delete code repositories.<br>Pass AWS CodeStar connections to AWS CodePipeline. | July 1, 2021       |
| AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy                                                                                                                                                                                                                             | 1       | Initial policy                                                                                                                                                              | November 27, 2020  |
