# Prepare data for fine-tuning image generation and embedding

models

###### Note

Amazon Nova models have different fine-tuning requirements. To fine-tune these models, follow the
instructions at [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

For text-to-image or image-to-embedding models, prepare a training dataset. Validation datasets are
not supported. Each JSON object is a sample containing an `image-ref`, the Amazon S3 URI for an
image, and a `caption` that could be a prompt for the image.

The images must be in JPEG or PNG format.

```
{"image-ref": "s3://bucket/path/to/image001.png", "caption": "<prompt text>"}
{"image-ref": "s3://bucket/path/to/image002.png", "caption": "<prompt text>"}{"image-ref": "s3://bucket/path/to/image003.png", "caption": "<prompt text>"}

```

The following is an example item:

```
{"image-ref": "s3://*amzn-s3-demo-bucket*/my-pets/cat.png", "caption": "an orange cat with white spots"}
```

To allow Amazon Bedrock access to the image files, add an IAM policy similar to the one in [Permissions to access training and validation files and to write output files in S3](model-customization-iam-role.md#model-customization-iam-role-s3 "model-customization-iam-role.md#model-customization-iam-role-s3") to the
Amazon Bedrock model customization service role that you set up or that was automatically set up for you in the
console. The Amazon S3 paths you provide in the training dataset must be in folders that you specify in the
policy.
