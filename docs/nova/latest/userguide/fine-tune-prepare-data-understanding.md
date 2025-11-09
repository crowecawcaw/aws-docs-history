# Preparing data for fine-tuning Understanding models

The following are guidelines and requirements for preparing data for fine-tuning Understanding models:

1. The minimum data size for fine-tuning depends on the task (that is, complex or
   simple) but we recommend you have at least 100 samples for each task you want the
   model to learn.
2. We recommend using your optimized prompt in a zero-shot setting during both
   training and inference to achieve the best results.
3. Traning and validation datasets must be JSONL files, where each line is a JSON object corresponding to a record. These file names can consist of only alphanumeric characters, underscores,
   hyphens, slashes, and dots.
4. Image and video constraints
   1. Dataset can't contain different media modalities. That is, the dataset can
      either be text with images or text with videos.
   2. One sample (single record in messages) can have multiple images
   3. One sample (single record in messages) can have only 1 video

5. `schemaVersion` can be any string value
6. The (_optional_) `system` turn can be a
   customer-provided custom system prompt.
7. Supported roles are `user` and `assistant`.
8. The first turn in `messages` should always start with `"role":
"user"`. The last turn is the bot's response, denoted by "role":
   "assistant".
9. The `image.source.s3Location.uri` and
   `video.source.s3Location.uri` must be accessible to Amazon Bedrock.
10. Your Amazon Bedrock service role must be able to access the image files in Amazon S3. For more information about granting access, see
    [Create a service role for model customization](../../../bedrock/latest/userguide/model-customization-iam-role.md "../../../bedrock/latest/userguide/model-customization-iam-role.md")
11. The images or videos must be in the same Amazon S3 bucket as your dataset. For example, if your dataset is in
    `s3://amzn-s3-demo-bucket/train/train.jsonl`, then your images or videos must be in
    `s3://amzn-s3-demo-bucket`
12. The terms `User:`, `Bot:`, `Assistant:`, `System:`, `<image>`, `<video>`, and `[EOS]` are reserved keywords. If a user prompt or system prompt starts with any of these keywords, or have these keywords anywhere in their prompts, your training job will fail due to data issues. If you need to use these keywords for your use case, you must substitute it for a different keyword with a similar meaning so that your training can proceed.

###### Topics

- [Example dataset formats](#customize-fine-tune-examples "#customize-fine-tune-examples")
- [Dataset constraints](#custom-fine-tune-constraints "#custom-fine-tune-constraints")

## Example dataset formats

The following example dataset formats provide a guide for you to follow.

The following example is for custom fine tuning over text only.

```
`// train.jsonl
{
 "schemaVersion": "bedrock-conversation-2024",
 "system": [
 {
 "text": "You are a digital assistant with a friendly personality"
 }
 ],
 "messages": [
 {
 "role": "user",
 "content": [
 {
 "text": "What is the capital of Mars?"
 }
 ]
 },
 {
 "role": "assistant",
 "content": [
 {
 "text": "Mars does not have a capital. Perhaps it will one day."
 }
 ]
 }
 ]
}`
```

The following example is for custom fine tuning over text and a single image.

```
`// train.jsonl{
 "schemaVersion": "bedrock-conversation-2024",
 "system": [{
 "text": "You are a smart assistant that answers questions respectfully"
 }],
 "messages": [{
 "role": "user",
 "content": [{
 "text": "What does the text in this image say?"
 },
 {
 "image": {
 "format": "png",
 "source": {
 "s3Location": {
 "uri": "s3://`your-bucket/your-path/your-image.png`",
 "bucketOwner": "`your-aws-account-id`"
 }
 }
 }
 }
 ]
 },
 {
 "role": "assistant",
 "content": [{
 "text": "The text in the attached image says 'LOL'."
 }]
 }
 ]
}`
```

The following example is for custom fine tuning over text and video.

```
`{
 "schemaVersion": "bedrock-conversation-2024",
 "system": [{
 "text": "You are a helpful assistant designed to answer questions crisply and to the point"
 }],
 "messages": [{
 "role": "user",
 "content": [{
 "text": "How many white items are visible in this video?"
 },
 {
 "video": {
 "format": "mp4",
 "source": {
 "s3Location": {
 "uri": "s3://`your-bucket/your-path/your-video.mp4`",
 "bucketOwner": "`your-aws-account-id`"
 }
 }
 }
 }
 ]
 },
 {
 "role": "assistant",
 "content": [{
 "text": "There are at least eight visible items that are white"
 }]
 }
 ]
}`
```

## Dataset constraints

Amazon Nova applies the following constraints on model customizations for Understanding models.

| Model             | Minimum Samples | Maximum Samples | Context Length |
| ----------------- | --------------- | --------------- | -------------- |
| Amazon Nova Micro | 8               | 20k             | 32k            |
| Amazon Nova Lite  | 8               | 20k             | 32k            |
| Amazon Nova Pro   | 8               | 20k             | 32k            |

Image and video constraints| Maximum images | 10/sample |
| Maximum image file size | 10 MB |
| Maximum videos | 1/sample |
| Maximum video length/duration | 90 seconds |
| Maximum video file size | 50 MB |

###### Supported media formats

- Image - `png`, `jpeg`, `gif`,
  `webp`
- Video - `mov`, `mkv`, `mp4`,
  `webm`
