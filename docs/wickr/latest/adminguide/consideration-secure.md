This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Security considerations

Carefully evaluate where and how to deploy a data retention bot. These bots
centrally collect and decrypt all end-to-end encrypted messages sent or received by
users, consolidating content that was previously accessible only on individual
devices. As a result, this component and its data storage have exceptionally high
security value.

If you deploy a data retention bot, ensure it meets the highest security standards
and aligns with your organizations security policy. For deployments using AWS
services, follow the additional guidance in our [Security best practices for AWS Wickr](security-best-practices.md "security-best-practices.md") and AWS Cloud Security [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
