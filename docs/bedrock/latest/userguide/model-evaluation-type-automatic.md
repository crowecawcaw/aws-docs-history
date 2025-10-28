# Required steps prior to creating your

first automatic model evaluation job

Automatic model evaluation jobs require access to the following service level resources.
Use the linked topics to learn more about getting setting up.

###### Cross Origin Resource Sharing (CORS) permission requirements

All console-based model evaluation jobs require Cross Origin Resource Sharing (CORS)
permissions to be enabled on any Amazon S3 buckets specified in the model evaluation job. To
learn more, see [Required Cross Origin Resource Sharing
(CORS) permissions on S3 buckets](model-evaluation-security-cors.md "model-evaluation-security-cors.md")

###### Required service level resources to start an automatic model evaluation job

1. To start a automatic model evaluation job, you need access to at least one Amazon Bedrock
   foundation model. To learn more, see [Access Amazon Bedrock foundation models](model-access.md "model-access.md").
2. To create an automatic model evaluation job you need access to the [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/"),
   AWS Command Line Interface, or a supported AWS SDK. To learn more about the required IAM actions
   and resources, see [Required console permissions to create an automatic
   model evaluation job](#base-for-automatic "#base-for-automatic").
3. When the model evaluation job starts, a service role is used to perform actions on
   your behalf. To learn more about required IAM actions and the trust policy
   requirements, see [Service role requirements for automatic model evaluation jobs](automatic-service-roles.md "automatic-service-roles.md").
4. Amazon Simple Storage Service – All data used and generated must be placed in an Amazon S3 bucket that is
   in the same AWS Region in an automatic model evaluation job.
5. Cross Origin Resource Sharing (CORS) – Automatic model evaluations jobs
   that are created using the Amazon Bedrock console require that you specify a CORS
   configuration on the S3 bucket. To learn more, see [Required Cross Origin Resource Sharing
   (CORS) permissions on S3 buckets](model-evaluation-security-cors.md "model-evaluation-security-cors.md").
6. An IAM service role – To run an automatic model evaluation job you must
   create a service role. The service role allows Amazon Bedrock to perform actions on your
   behalf in your AWS account. To learn more, see [Service role requirements for automatic model evaluation jobs](automatic-service-roles.md "automatic-service-roles.md").

## Required console permissions to create an automatic

model evaluation job

The following policy contains the minimum set of IAM actions and resources in Amazon Bedrock
and Amazon S3 that are required to create an _automatic_ model evaluation
job using the Amazon Bedrock console.

In the policy, we recommend using the IAM JSON policy element [Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") to limit access to only the models and buckets required for the
IAM user, group, or role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPassingConsoleCreatedServiceRoles",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::111122223333:role/service-role/Amazon-Bedrock-IAM-Role-*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "bedrock.amazonaws.com"
 }
 }
 },
 {
 "Sid": "BedrockConsole",
 "Effect": "Allow",
 "Action": [
 "bedrock:CreateEvaluationJob",
 "bedrock:GetEvaluationJob",
 "bedrock:ListEvaluationJobs",
 "bedrock:StopEvaluationJob",
 "bedrock:GetCustomModel",
 "bedrock:ListCustomModels",
 "bedrock:CreateProvisionedModelThroughput",
 "bedrock:UpdateProvisionedModelThroughput",
 "bedrock:GetProvisionedModelThroughput",
 "bedrock:ListProvisionedModelThroughputs",
 "bedrock:GetImportedModel",
 "bedrock:ListImportedModels",
 "bedrock:ListMarketplaceModelEndpoints",
 "bedrock:ListTagsForResource",
 "bedrock:UntagResource",
 "bedrock:TagResource"
 ],
 "Resource": [
 "arn:aws:bedrock:us-west-2::foundation-model/model-id-of-foundational-model",
 "arn:aws:bedrock:us-west-2:111122223333:inference-profile/*",
 "arn:aws:bedrock:us-west-2:111122223333:provisioned-model/*",
 "arn:aws:bedrock:us-west-2:111122223333:imported-model/*"
 ]
 },
 {
 "Sid": "AllowConsoleS3AccessForModelEvaluation",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetBucketCORS",
 "s3:ListBucket",
 "s3:ListBucketVersions",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::my_output_bucket",
 "arn:aws:s3:::input_datasets/prompts.jsonl"
 ]
 }
 ]
}`

```
