# Exporting your workflow to IaC templates

The AWS Step Functions console provides the ability to export and download saved workflows as AWS CloudFormation or AWS SAM (SAM) templates. For AWS Regions that support
AWS Infrastructure Composer, it additionally provides the ability to export your workflows to Infrastructure Composer and navigates to the Infrastructure Composer console, where you can continue to work with
the newly generated template.

## Template configuration options

The following options are available with this feature. If you select to export and download an IaC template file, the console displays the options
that apply to your saved state machine for selection. If you’re exporting to Infrastructure Composer, the Step Functions console automatically implements the configurations that
apply to your state machine.

- Include IAM role created by console on your behalf – This option exports the execution role policies. It
  constructs an IAM role in the template and attaches it to the state machine resource. This option is only applicable if the state machine has an
  execution role that’s created by the console.
- Include CloudWatch Log Group – Constructs a CloudWatch log group in the template and attaches it to the state machine
  resource. This option is only applicable if the state machine has a CloudWatch log group attached to it and the [log
  level](cw-logs.md#cloudwatch-log-level "cw-logs.md#cloudwatch-log-level") is _not_ set to `OFF`.
- Replace resource references with DefinitionSubstitutions – This option generates [DefinitionSubstitutions](concepts-sam-sfn.md#sam-definition-substitution-eg "concepts-sam-sfn.md#sam-definition-substitution-eg") for the following components:
  - [Distributed Map](state-map-distributed.md "state-map-distributed.md") S3 fields.
  - `Activity` resources. The export includes `Activity` resources in the CloudFormation template for any `Run Activity`
    task. The export also provides `DefinitionSubstitutions` referencing the created `Activity` resources.
  - Any `ARN` or `S3URI` in the Payload field for all service integrations.
  - In addition to the `ARN` and `S3URI` fields, the export generates `DefinitionSubstitutions` for other
    frequently used service integration payload fields. The specific service integrations are the following:
    - `athena:startQueryExecution`
    - `batch:submitJob`
    - `dynamodb:getItem`, `dynamodb:updateItem`, `dynamodb:updateItem`, `dynamodb:deleteItem`
    - `ecs:runTask`
    - `glue:startJobRun`
    - `http:invoke`
    - `lambda:invoke`
    - `sns:publish`
    - `sqs:sendMessage`
    - `states:startExecution`

## Export and download your workflow's IaC template

###### To export your workflow into an IaC template file

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/") and select the state machine you want to
   work with. Make sure that any changes to the state machine are saved before you proceed to the next step.
2. Select **Export to CloudFormation or SAM template** from the **Actions** menu.
3. Select **Type** as either **SAM** or **CloudFormation** from the dialog box that appears.
   - If you selected the **CloudFormation** template, next choose either the **JSON** or **YAML**
     file format.
   - If you selected the **SAM** template, no formats choices are presented. The SAM template defaults to YAML file format.

4. Expand **Additional configurations**. By default all of the options are selected. Review and update the selection of options for
   your IaC template. The options are described in detail in the previous section titled [Template configuration options](#exporting-iac-templates-config-options "#exporting-iac-templates-config-options").

If an option doesn't apply to your specific workflow, then it won't display in the dialogue box. 5. Choose **Download** to export and download your generated IaC template file.

## Export your workflow directly into AWS Infrastructure Composer

###### To export your workflow into Infrastructure Composer

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/") and select the state machine you want to
   work with. Make sure that any changes to the state machine are saved before you proceed to the next step.
2. Select **Export to Infrastructure Composer** from the **Actions** menu.
3. The **Export to Infrastructure Composer** dialog box displays. You can use the default name that displays in the **Transfer bucket
   name** field or enter a new name. Amazon S3 bucket names must be globally unique and follow the [bucket naming rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md "../../../AmazonS3/latest/userguide/bucketnamingrules.md").
4. Choose the **Confirm and create project** to export your workflow to Infrastructure Composer.
5. To save your project and workflow definition in Infrastructure Composer, activate [local sync mode](../../../application-composer/latest/dg/reference-features-local-sync.md "../../../application-composer/latest/dg/reference-features-local-sync.md").

###### Note

If you've used the **Export to Infrastructure Composer** feature before and created an Amazon S3 bucket using the default name, Step Functions can re-use this
bucket if it still exists. Accept the default bucket name in the dialog box to re-use the existing bucket.

### Amazon S3 transfer bucket configuration

The Amazon S3 bucket that Step Functions creates to transfer your workflow automatically encrypts objects using the AES 256 encryption standard. Step Functions also
configures the bucket to use the [bucket owner condition](../../../AmazonS3/latest/userguide/bucket-owner-condition.md "../../../AmazonS3/latest/userguide/bucket-owner-condition.md")
to ensure that only your AWS account is able to add objects to the bucket.

The default bucket name uses the prefix `states-templates`, a 10-digit alphanumeric string, and the AWS Region you created your
workflow in: `states-templates-`amzn-s3-demo-bucket`-`us-east-1``. To avoid additional
charges being added to your AWS account, we recommend that you delete the Amazon S3 bucket as soon as you have finished exporting your workflow to
Infrastructure Composer.

Standard [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") applies.

### Required permissions

To use this Step Functions export feature with Infrastructure Composer, you need certain permissions to download an AWS SAM template and to write your template configuration to
Amazon S3.

To download an AWS SAM template, you must have permission to use the following API actions:

- [iam:GetPolicy](../../../IAM/latest/APIReference/API_GetPolicy.md "../../../IAM/latest/APIReference/API_GetPolicy.md")
- [iam:GetPolicyVersion](../../../IAM/latest/APIReference/API_GetPolicyVersion.md "../../../IAM/latest/APIReference/API_GetPolicyVersion.md")
- [iam:GetRole](../../../IAM/latest/APIReference/API_GetRole.md "../../../IAM/latest/APIReference/API_GetRole.md")
- [iam:GetRolePolicy](../../../IAM/latest/APIReference/API_GetRolePolicy.md "../../../IAM/latest/APIReference/API_GetRolePolicy.md")
- [iam:ListAttachedRolePolicies](../../../IAM/latest/APIReference/API_ListAttachedRolePolicies.md "../../../IAM/latest/APIReference/API_ListAttachedRolePolicies.md")
- [iam:ListRolePolicies](../../../IAM/latest/APIReference/API_ListRolePolicies.md "../../../IAM/latest/APIReference/API_ListRolePolicies.md")
- [iam:ListRoles](../../../IAM/latest/APIReference/API_ListRoles.md "../../../IAM/latest/APIReference/API_ListRoles.md")

For Step Functions to write your function's configuration to Amazon S3, you must have permission to use the following API actions:

- [S3:PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")
- [S3:CreateBucket](../../../AmazonS3/latest/API/API_CreateBucket.md "../../../AmazonS3/latest/API/API_CreateBucket.md")
- [S3:PutBucketEncryption](../../../AmazonS3/latest/API/API_PutBucketEncryption.md "../../../AmazonS3/latest/API/API_PutBucketEncryption.md")

If you are unable to export your function's configuration to Infrastructure Composer, check that your account has the required permissions for these operations.
