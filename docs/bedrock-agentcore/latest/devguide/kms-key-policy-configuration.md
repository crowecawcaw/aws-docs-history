# Set customer managed key policy

###### Note

Currently we don't support configuring CMK on token vault through console.

To use a customer managed key, your key must trust an Amazon Bedrock AgentCore Identity service
principal to perform encryption and decryption operations on the key. Configure the
[key
policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") of your KMS key as shown in the following example. The IAM principal
that writes this policy must have write access to your KMS key, with
`kms:PutKeyPolicy` permission.
