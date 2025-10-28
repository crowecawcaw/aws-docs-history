# Use IAM Managed Policies with Ground Truth

SageMaker AI and Ground Truth provide AWS managed policies that you can use to create a
labeling job. If you are getting started using Ground Truth and you do not require granular
permissions for your use case, it is recommended that you use the following
policies:

- `AmazonSageMakerFullAccess` – Use this policy
  to give a user or role permission to create a labeling job. This is a
  broad policy that grants a entity permission to use SageMaker AI features, as
  well as features of necessary AWS services through the console and API.
  This policy gives the entity permission to create a labeling job and
  to create and manage workforces using Amazon Cognito. To learn more, see [AmazonSageMakerFullAccess Policy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess").
- `AmazonSageMakerGroundTruthExecution` – To
  create an _execution role_, you can attach
  the policy `AmazonSageMakerGroundTruthExecution` to a
  role. An execution role is the role that you specify when you create a
  labeling job and it is used to start your labeling job. This policy allows
  you to create both streaming and non-streaming labeling jobs, and to create
  a labeling job using any task type. Note the following limits of this
  managed policy.

      + **Amazon S3 permissions**: This policy
       grants an execution role permission to access Amazon S3 buckets with the
       following strings in the name: `GroundTruth`,
       `Groundtruth`, `groundtruth`,
       `SageMaker`, `Sagemaker`, and
       `sagemaker` or a bucket with an [object
       tag](../../../AmazonS3/latest/userguide/object-tagging.md "../../../AmazonS3/latest/userguide/object-tagging.md") that includes `SageMaker` in the name
       (case insensitive). Make sure your input and output bucket names
       include these strings, or add additional permissions to your
       execution role to [grant it permission to access your Amazon S3 buckets](../../../IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.md "../../../IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.md"). You must
       give this role permission to perform the following actions on your
       Amazon S3 buckets: `AbortMultipartUpload`,
       `GetObject`, and `PutObject`.
      + **Custom Workflows**: When you create
       a [custom
       labeling workflow](sms-custom-templates.md "sms-custom-templates.md"), this execution role is restricted to
       invoking AWS Lambda functions with one of the following strings as
       part of the function name: `GtRecipe`,
       `SageMaker`, `Sagemaker`,
       `sagemaker`, or `LabelingFunction`. This
       applies to both your pre-annotation and post-annotation Lambda
       functions. If you choose to use names without those strings, you
       must explicitly provide `lambda:InvokeFunction`
       permission to the execution role used to create the labeling
       job.

  To learn how to attach an AWS managed policy to a user or role, refer to
  [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in the
  IAM User Guide.
