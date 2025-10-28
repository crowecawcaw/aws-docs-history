# Configuring the

message signature version on Amazon SNS topics

Configuring the message signature version on Amazon SNS topics allows you to enhance the
security and compatibility of your message verification process.

Select between `SignatureVersion`**1** (SHA1) and
`SignatureVersion`**2** (SHA256) to control the
hashing algorithm used for signing messages. Amazon SNS topics default to
`SignatureVersion`**1**. You can configure this
setting using the [`SetTopicAttributes`](../api/API_SetTopicAttributes.md "../api/API_SetTopicAttributes.md") API action.

Use the following example to set the topic attribute `SignatureVersion` using
the AWS CLI:

```
aws sns set-topic-attributes \
    --topic-arn arn:aws:sns:us-east-2:123456789012:MyTopic \
    --attribute-name SignatureVersion \
    --attribute-value 2
```
