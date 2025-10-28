# Understanding Credentials Management in Amazon Bedrock AgentCore

## MicroVM Metadata Service (MMDS)

When you configure an execution role with Amazon Bedrock AgentCore Browser, AgentCore Code Interpreter, or AgentCore Runtime, the underlying compute
uses MMDS to access credentials, similar to how EC2 instances use the [Instance Metadata Service (IMDS)](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md").
This allows the service within the VM to retrieve temporary AWS credentials for operations like S3 access. This is
independent of the network mode that the AgentCore Code Interpreter, AgentCore Browser, or AgentCore Runtime is running in.

###### Important

When configuring the execution role permissions, use careful consideration since any code or actor running inside
the VM can access these credentials by calling the metadata endpoint.

## Best Practices for Role Setup

- Follow the principle of least privilege when setting up the execution role. Especially when using these tools with
  LLMs, that can generate arbitrary code, it's crucial to limit permissions to only what you intend.
- Avoid privilege escalation by ensuring that the execution role associated with your resource has equal or
  fewer privileges than the users who can invoke it.

The following shows an example of properly scoped permissions:

```
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::<your-specific-bucket>/*"
}
```
