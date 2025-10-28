# Example SCPs for

Amazon Q Developer in chat applications

###### Topics

- [Deny all IAM operation](#example_cloudwatch_1 "#example_cloudwatch_1")
- [Deny S3 bucket put requests from a specified Slack channel](#example_cloudwatch_2 "#example_cloudwatch_2")

## Deny all IAM operation

The following SCP denies all IAM operations invoked through all Amazon Q Developer in chat applications configurations.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "iam:*",
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:ChatbotSourceArn": "arn:aws:chatbot::*:*"
        }
      }
    }
  ]
}
```

## Deny S3 bucket put requests from a specified Slack channel

The following policy denies S3 put requests on the specified bucket for all requests originating from a Slack channel.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ExampleS3Deny",
 "Effect": "Deny",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "Condition": {
 "ArnLike": {
 "aws:ChatbotSourceArn": "arn:aws:chatbot::*:chat-configuration/slack-channel/*"
 }
 }
 }
 ]
}`

```
