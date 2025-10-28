# Output Data and Storage Volume Encryption

With Amazon SageMaker Ground Truth, you can label highly sensitive data, stay in control of your data, and
employ security best practices. While your labeling job is running, Ground Truth encrypts data
in transit and at rest. Additionally, you can use AWS Key Management Service (AWS KMS) with Ground Truth to do the
following:

- Use a [customer managed key](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys")
  to encrypt your output data.
- Use AWS KMS customer managed key with your automated data labeling job to
  encrypt the storage volume attached to the compute instance used for model
  training and inference.
  Use the topics on this page to learn more about these Ground Truth security features.

## Use Your KMS Key to Encrypt Output Data

Optionally, you can provide an AWS KMS customer managed key when you create a
labeling job, which Ground Truth uses to encrypt your output data.

If you don't provide a customer managed key, Amazon SageMaker AI uses the default AWS managed key
for Amazon S3 for your role's account to encrypt your output data.

If you provide a customer managed key, you must add the required permissions to the
key described in [Encrypt Output Data and Storage Volume with
AWS KMS](sms-security-kms-permissions.md "sms-security-kms-permissions.md"). When you use the API operation
`CreateLabelingJob`, you can specify your customer managed key ID using the
parameter `KmsKeyId`. See the following procedure to learn how to add a
customer managed key when you create a labeling job using the console.

###### To add an AWS KMS key to encrypt output data (console):

1. Complete the first 7 steps in [Create a Labeling Job (Console)](sms-create-labeling-job-console.md "sms-create-labeling-job-console.md").
2. In step 8, select the arrow next to **Additional
   configuration** to expand this section.
3. For **Encryption key**, select the AWS KMS key that you want to
   use to encrypt output data.
4. Complete the rest of steps in [Create a Labeling Job (Console)](sms-create-labeling-job-console.md "sms-create-labeling-job-console.md") to create a labeling
   job.

## Use Your KMS Key to Encrypt Automated Data

Labeling Storage Volume (API Only)

When you create a labeling job with automated data labeling using the
`CreateLabelingJob` API operation, you have the option to encrypt the
storage volume attached to the ML compute instances that run the training and
inference jobs. To add encryption to your storage volume, use the parameter
`VolumeKmsKeyId` to input an AWS KMS customer managed key. For more
information about this parameter, see `LabelingJobResourceConfig`.

If you specify a key ID or ARN for `VolumeKmsKeyId`, your SageMaker AI
execution role must include permissions to call `kms:CreateGrant`. To
learn how to add this permission to an execution role, see [Create a SageMaker AI Execution Role for a
Ground Truth Labeling Job](sms-security-permission-execution-role.md "sms-security-permission-execution-role.md").

###### Note

If you specify an AWS KMS customer managed key when you create a labeling job in
the console, that key is _only_ used to encrypt your output
data. It is not used to encrypt the storage volume attached to the ML compute
instances used for automated data labeling.
