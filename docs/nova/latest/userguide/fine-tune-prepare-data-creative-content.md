# Preparing data for fine-tuning Creative Content Generation models

The following are guidelines and requirements for preparing data for fine-tuning Creative Content Generation models.

1. The optimal amount of training data depends on the complexity of the task and the desired outcome.
   - Increasing the variety and volume in your training data can improve model accuracy.
   - The more images you use, the more time
     it can take for the fine-tuning job to complete.
   - The number of images increases your fine-tuning cost. For more information, see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") for more information.

2. Training and validation datasets must be JSONL files, where each line is a JSON object corresponding to a record. These file names can consist of only alphanumeric characters, underscores,
   hyphens, slashes, and dots.
3. Each record in your JSONL must include an `image-ref` attribute with the Amazon S3 URI for an image, and a `caption` attribute with a prompt for the image.
   The images must be in JPEG or PNG format. For examples, see [Required dataset format](#customize-fine-tune-example-creative-content "#customize-fine-tune-example-creative-content").
4. Your traning and validation datasets must conform to the size requirements listed in
   [Dataset constraints](#custom-fine-tune-constraints-creative-content "#custom-fine-tune-constraints-creative-content").
5. Your Amazon Bedrock service role must be able to access the image files in Amazon S3. For more information about granting access, see
   [Create a service role for model customization](../../../bedrock/latest/userguide/model-customization-iam-role.md "../../../bedrock/latest/userguide/model-customization-iam-role.md").

###### Topics

- [Required dataset format](#customize-fine-tune-example-creative-content "#customize-fine-tune-example-creative-content")
- [Dataset constraints](#custom-fine-tune-constraints-creative-content "#custom-fine-tune-constraints-creative-content")

## Required dataset format

The following shows the required format for your JSONL files.

```
{"image-ref": "s3://amzn-s3-demo-bucket/path/to/image001.png", "caption": "<prompt text>"}
{"image-ref": "s3://amzn-s3-demo-bucket/path/to/image002.png", "caption": "<prompt text>"}
{"image-ref": "s3://amzn-s3-demo-bucket/path/to/image003.png", "caption": "<prompt text>"}
```

The following is an example record:

```
{"image-ref": "s3://amzn-s3-demo-bucket/my-pets/cat.png", "caption": "an orange cat with white spots"}
```

## Dataset constraints

The following are dataset constraints for fine-tuning Amazon Nova Canvas. Amazon Nova Reel doesn't support fine-tuning.

**Size requirements for training and validation datasets**

|                                                      | Minimum | Maximum    |
| ---------------------------------------------------- | ------- | ---------- | ------------------------------------------------ |
| Records in a training dataset                        | 5       | 10k        |
| Text prompt length in training sample, in characters | 3       | 1,024      | **Input image size constraints**                 |
|                                                      | Minimum | Maximum    |
| ---                                                  | ---     | ---        |
| Input image size                                     | 0       | 50 MB      |
| Input image height in pixels                         | 512     | 4,096      |
| Input image width in pixels                          | 512     | 4,096      |
| Input image total pixels                             | 0       | 12,582,912 |
| Input image aspect ratio                             | 1:4     | 4:1        | **Supported media formats** <br>• PNG <br>• JPEG |
