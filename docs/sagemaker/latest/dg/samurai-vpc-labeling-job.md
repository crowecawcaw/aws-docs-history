# Run an Amazon SageMaker Ground Truth Labeling Job in an Amazon Virtual Private Cloud

Ground Truth supports the following functionalities in Amazon VPC.

- You can use Amazon S3 bucket policies to control access to buckets from specific Amazon VPC endpoints, or specific VPCs. If you launch a labeling job and your input data is located in an Amazon S3 bucket that is restricted to users in your VPC, you can add a bucket policy to also grant a Ground Truth endpoint permission to access the bucket. To learn more, see [Allow Ground Truth to Access VPC Restricted Amazon S3 Buckets](#sms-vpc-permissions-s3 "#sms-vpc-permissions-s3").
- You can launch an [automated data labeling job](sms-automated-labeling.md "sms-automated-labeling.md") in your VPC. You use a VPC configuration to specify VPC subnets and security groups. SageMaker AI uses this configuration to launch the training and inference jobs used for automated data labeling in your VPC. To learn more, see [Create an Automated Data
  Labeling Job in a VPC](#sms-vpc-permissions-automated-labeling "#sms-vpc-permissions-automated-labeling").
  You may want to use these options in any of the following ways.

- You can use both of these methods to launch a labeling job using a VPC-protected
  Amazon S3 bucket with automated data labeling enabled.
- You can launch a labeling job using any [built-in task type](sms-task-types.md "sms-task-types.md") using a VPC-protected bucket.
- You can launch a [custom labeling workflow](sms-custom-templates.md "sms-custom-templates.md") using a VPC-protected bucket. Ground Truth interacts
  with your pre-annotation and post-annotation Lambda functions using an [AWS PrivateLink](../../../vpc/latest/privatelink/endpoint-services-overview.md "../../../vpc/latest/privatelink/endpoint-services-overview.md") endpoint.
  We recommend that you review [Prerequisites for running a Ground Truth labeling job in a VPC](#sms-vpc-gt-prereq "#sms-vpc-gt-prereq") before you create a labeling job in an Amazon VPC.

## Prerequisites for running a Ground Truth labeling job in a VPC

Review the following prerequisites before you create a Ground Truth labeling job in an Amazon VPC.

- If you are a new user of Ground Truth, review [Getting started](sms-getting-started.md "sms-getting-started.md") to learn how to create a labeling job.
- If your input data is located in a VPC-protected Amazon S3 bucket, your workers must access the worker portal from your VPC. VPC based labeling jobs require the use of a private work team. To learn more about creating a private work team, see [Use a Private Workforce](sms-workforce-private.md "sms-workforce-private.md").
- The following prerequisites are specific to launching a labeling job in your VPC.
  - Use the instructions in [Create an Amazon S3 VPC Endpoint](train-vpc.md#train-vpc-s3 "train-vpc.md#train-vpc-s3"). Training and inference
    containers used in the automated data labeling workflow use this
    endpoint to communicate with your buckets in Amazon S3.
  - Review [Automate Data Labeling](sms-automated-labeling.md "sms-automated-labeling.md") to learn more about this feature.
    Note that automated data labeling is supported for the following [built-in task types](sms-task-types.md "sms-task-types.md"): [Image Classification (Single Label)](sms-image-classification.md "sms-image-classification.md"), [Image Semantic Segmentation](sms-semantic-segmentation.md "sms-semantic-segmentation.md"), [Bounding Box](sms-bounding-box.md "sms-bounding-box.md"), and [Text Classification (Single Label)](sms-text-classification.md "sms-text-classification.md"). Streaming labeling jobs
    do not support automated data labeling.

- Review the [Ground Truth Security and Permissions](sms-security-general.md "sms-security-general.md") section and ensure that you have met the following conditions.
  - The
    user creating the labeling job has all necessary permissions
  - You have created
    an IAM execution role with required permissions. If you do not require
    fine-tuned permissions for your use case, we recommend you use the IAM managed
    policies described in [Grant General Permissions To Get Started Using Ground Truth](sms-security-permission.md#sms-security-permissions-get-started "sms-security-permission.md#sms-security-permissions-get-started").
  - Allow your VPC to have access to the `sagemaker-labeling-data-`region``and`sm-bxcb-`region`-saved-task-states` S3 buckets.
    These are system owned regionalized S3 buckets that are
    accessed from worker portal when worker is working on a task. We use these buckets to interact with system managed data.

## Allow Ground Truth to Access VPC Restricted Amazon S3 Buckets

The following sections provide details about the permissions Ground Truth requires to launch
labeling jobs using Amazon S3 buckets that have access restricted to your VPC and VPC
endpoints. To learn how to restrict access to an Amazon S3 bucket to a VPC, see [Controlling access from VPC endpoints with bucket policies](../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md "../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md") in the
Amazon Simple Storage Service User Guide guide. To learn how to add a policy to an S3 bucket, see [Adding a bucket policy using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md").

###### Note

Modifying policies on existing buckets can cause
`IN_PROGRESS` Ground Truth jobs to fail. We recommend you start new jobs
using a new bucket. If you want to continue using the same bucket,
you can do one of the following.

- Wait for an `IN_PROGRESS` job to finish.
- Terminate the job using the console or the AWS CLI.

You can restrict Amazon S3 bucket access to users in your VPC using an [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") endpoint. For
example, the following S3 bucket policy allows access to a specific bucket,
`<bucket-name>`, from
`<vpc>` and the endpoint
`<vpc-endpoint>` only. When you modify this
policy, you must replace all `red-italized text` with your
resources and specifications.

###### Note

The following policy _denies_ all entities
_other than_ users within a VPC to perform the
actions listed in `Action`. If you do not include actions in this list,
they are still accessible to any entity that has access to this bucket and
permission to perform those actions. For example, if a user has permission to
perform `GetBucketLocation` on your Amazon S3 bucket, the policy below does
not restrict the user from performing this action outside of your VPC.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy1415115909152",
 "Statement": [
 {
 "Sid": "AccessToSpecificVPCEOnly",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Effect": "Deny",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:sourceVpce": [
 "`vpce-12345678`",
 "`vpce-12345678901234567`"
 ]
 }
 }
 }
 ]
}`

```

Ground Truth must be able to perform the following Amazon S3 actions on the S3 buckets you use
to configure the labeling job.

```
"s3:AbortMultipartUpload",
"s3:GetObject",
"s3:PutObject",
"s3:ListBucket",
"s3:GetBucketLocation"
```

You can do this by adding a Ground Truth endpoint to the bucket policy like the one previously mentioned.
The following table includes Ground Truth service endpoints for each AWS Region. Add an
endpoint in the same [AWS Region](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md")
you use to run your labeling job to your bucket policy.

| AWS Region     | Ground Truth endpoint  |
| -------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| us-east-2      | vpce-02569ba1c40aad0bc |
| us-east-1      | vpce-08408e335ebf95b40 |
| us-west-2      | vpce-0ea07aa498eb78469 |
| ca-central-1   | vpce-0d46ea4c9ff55e1b7 |
| eu-central-1   | vpce-0865e7194a099183d |
| eu-west-2      | vpce-0bccd56798f4c5df0 |
| eu-west-1      | vpce-0788e7ed8628e595d |
| ap-south-1     | vpce-0d7fcda14e1783f11 |
| ap-southeast-2 | vpce-0b7609e6f305a77d4 |
| ap-southeast-1 | vpce-0e7e67b32e9efed27 |
| ap-northeast-2 | vpce-007893f89e05f2bbf |
| ap-northeast-1 | vpce-0247996a1a1807dbd | For example, the following policy restricts `GetObject` and `PutObject` actions on: <br>• An Amazon S3 bucket to users in a VPC (`<vpc>`) <br>• A VPC endpoint (`<vpc-endpoint>`) <br>• A Ground Truth service endpoint (`<ground-truth-endpoint>`) JSON `` `{ "Version":"2012-10-17", "Id": "1", "Statement": [ { "Sid": "DenyAccessFromNonGTandCustomerVPC", "Effect": "Deny", "Principal": "*", "Action": [ "s3:GetObject", "s3:PutObject" ], "Resource": [ "arn:aws:s3:::`bucket-name`", "arn:aws:s3:::`bucket-name`/*" ], "Condition": { "StringNotEquals": { "aws:SourceVpc": "`vpc-12345678`", "aws:sourceVpce": [ "`vpce-12345678`", "`vpce-12345678`" ] } } } ] }` `` If you want a user to have permission to launch a labeling job using the Ground Truth console, you must also add the user's ARN to the bucket policy using the `aws:PrincipalArn` condition. This user must also have permission to perform the following Amazon S3 actions on the bucket you use to launch the labeling job. `"s3:GetObject", "s3:PutObject", "s3:ListBucket", "s3:GetBucketCors", "s3:PutBucketCors", "s3:ListAllMyBuckets",` The following code is an example of a bucket policy that restricts permission to perform the actions listed in `Action` on the S3 bucket `<bucket-name>` to the following. <br>• `<role-name>` <br>• The VPC endpoints listed in `aws:sourceVpce` <br>• Users within the VPC named `<vpc>` JSON `` `{ "Version":"2012-10-17", "Id": "1", "Statement": [ { "Sid": "DenyAccessFromNonGTandCustomerVPC", "Effect": "Deny", "Principal": "*", "Action": [ "s3:GetObject", "s3:PutObject" ], "Resource": [ "arn:aws:s3:::`bucket-name`/*", "arn:aws:s3:::`bucket-name`" ], "Condition": { "StringNotEquals": { "aws:SourceVpc": "`vpc-12345678`", "aws:PrincipalArn": "arn:aws:iam::`111122223333`:role/`role-name`" }, "StringNotEquals": { "aws:sourceVpce": [ "`vpce-12345678`", "`vpce-12345678`" ] } } } ] }` `` ###### Note The Amazon VPC interface endpoints and the protected Amazon S3 buckets you use for input and output data must be located in the same AWS Region that you use to create the labeling job. After you have granted Ground Truth permission to access your Amazon S3 buckets, you can use one of the topics in [Create a Labeling Job](sms-create-labeling-job.md "sms-create-labeling-job.md") to launch a labeling job. Specify the VPC-restricted Amazon S3 buckets for your input and output data buckets. ## Create an Automated Data Labeling Job in a VPC To create an automated data labeling job using an Amazon VPC, you provide a VPC configuration using the Ground Truth console or `CreateLabelingJob` API operation. SageMaker AI uses the subnets and security groups you provide to launch the training and inferences jobs used for automated labeling. ###### Important Before you launch an automated data labeling job with a VPC configuration, make sure you have created an Amazon S3 VPC endpoint using the VPC you want to use for the labeling job. To learn how, see [Create an Amazon S3 VPC Endpoint](train-vpc.md#train-vpc-s3 "train-vpc.md#train-vpc-s3"). Additionally, if you create an automated data labeling job using a VPC-restricted Amazon S3 bucket, you must follow the instructions in [Allow Ground Truth to Access VPC Restricted Amazon S3 Buckets](#sms-vpc-permissions-s3 "#sms-vpc-permissions-s3") to give Ground Truth permission to access the bucket. Use the following procedures to learn how to add a VPC configuration to your labeling job request. ###### Add a VPC configuration to an automated data labeling job (console): 1. Follow the instructions in [Create a Labeling Job (Console)](sms-create-labeling-job-console.md "sms-create-labeling-job-console.md") and complete each step in the procedure, up to step 15. 2. In the **Workers** section, select the checkbox next to **Enable automated data labeling**. 3. Maximize the **VPC configuration** section of the console by selecting the arrow. 4. Specify the **Virtual private cloud (VPC)** that you want to use for your automated data labeling job. 5. Choose the dropdown list under **Subnets** and select one or more subnets. 6. Choose the dropdown list under **Security groups** and select one or more groups. 7. Complete all remaining steps of the procedure in [Create a Labeling Job (Console)](sms-create-labeling-job-console.md "sms-create-labeling-job-console.md"). ###### Add a VPC configuration to an automated data labeling job (API): To configure a labeling job using the Ground Truth API operation, `CreateLabelingJob`, follow the instructions in [Create an Automated Data Labeling Job (API)](sms-automated-labeling.md#sms-create-automated-labeling-api "sms-automated-labeling.md#sms-create-automated-labeling-api") to configure your request. In addition to the parameters described in this documentation, you must include a `VpcConfig` parameter in `LabelingJobResourceConfig` to specify one or more subnets and security groups using the following schema. ``"LabelingJobAlgorithmsConfig": { "InitialActiveLearningModelArn": "`string`", "LabelingJobAlgorithmSpecificationArn": "`string`", "LabelingJobResourceConfig": { "VolumeKmsKeyId": "`string`", "VpcConfig": { "SecurityGroupIds": [ "`string`" ], "Subnets": [ "`string`" ] } } }`` The following is an example of an [AWS Python SDK (Boto3) request](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job") to create an automated data labeling job in the US East (N. Virginia) Region using a private workforce. Replace all `red-italicized text` with your labeling job resources and specifications. To learn more about the `CreateLabelingJob` operation, see the [Create a Labeling Job (API)](sms-create-labeling-job-api.md "sms-create-labeling-job-api.md") tutorial and [CreateLabelingJob](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") API documentation. ``import boto3 client = boto3.client(service_name='sagemaker') response = client.create_labeling_job( LabelingJobName=`"example-labeling-job"`, LabelAttributeName=`"label"`, InputConfig={ 'DataSource': { 'S3DataSource': { 'ManifestS3Uri': `"s3://bucket/path/manifest-with-input-data.json"` } } }, "LabelingJobAlgorithmsConfig": { "LabelingJobAlgorithmSpecificationArn": "`arn:aws:sagemaker:us-east-1:027400017018:labeling-job-algorithm-specification/tasktype`", "LabelingJobResourceConfig": { "VpcConfig": { "SecurityGroupIds": [ "`sg-01233456789`", "`sg-987654321`" ], "Subnets": [ "`subnet-e0123456`", "`subnet-e7891011`" ] } } }, OutputConfig={ 'S3OutputPath': `"s3://bucket/path/file-to-store-output-data"`, 'KmsKeyId': `"string"` }, RoleArn=`"arn:aws:iam::*:role/*`, LabelCategoryConfigS3Uri=`"s3://bucket/path/label-categories.json"`, StoppingConditions={ 'MaxHumanLabeledObjectCount': `123`, 'MaxPercentageOfInputDatasetLabeled': `123` }, HumanTaskConfig={ 'WorkteamArn': `"arn:aws:sagemaker:region:*:workteam/private-crowd/*"`, 'UiConfig': { 'UiTemplateS3Uri': `"s3://bucket/path/custom-worker-task-template.html"` }, 'PreHumanTaskLambdaArn': "arn:aws:lambda:`us-east-1:432418664414`:function:PRE-`tasktype`", 'TaskKeywords': [ "`Images`", "`Classification`", "`Multi-label`" ], 'TaskTitle': `"Add task title here"`, 'TaskDescription': `"Add description of task here for workers"`, 'NumberOfHumanWorkersPerDataObject': `1`, 'TaskTimeLimitInSeconds': `3600`, 'TaskAvailabilityLifetimeInSeconds': `21600`, 'MaxConcurrentTaskCount': `1000`, 'AnnotationConsolidationConfig': { 'AnnotationConsolidationLambdaArn': "arn:aws:lambda:`us-east-1:432418664414`:function:ACS-`tasktype`" }, Tags=[ { 'Key': `"string"`, 'Value': `"string"`        }, ] )`` |
