# Access and security for Model Distillation

Before you can begin, make sure that you understand access and security controls for
Model Distillation. You must have an IAM service role that can access the Amazon S3 bucket
where you want to store your Model Distillation training and validation data. Amazon Bedrock also
has options for encrypting and further securing your distillation jobs and artifacts.
For more information, see [Model customization access and
security](custom-model-job-access-security.md "custom-model-job-access-security.md").

To use a cross-region inference profile for a teacher model in a Distillation job, your service role must
have permissions to invoke the inference profile in an AWS Region, in addition to the model in each Region
in the inference profile. For a policy example, see [(Optional) Permissions to create a Distillation job with a cross-region inference profile](custom-model-job-access-security.md#custom-models-cross-region-inference-profile-permissions "custom-model-job-access-security.md#custom-models-cross-region-inference-profile-permissions"). For more information about cross-region inference, see [Increase throughput with cross-Region inference](cross-region-inference.md "cross-region-inference.md").
