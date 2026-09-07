

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Architecture Overview
<a name="architecture"></a>

## Message flow
<a name="message-flow"></a>

1. **Message Capture**: When users send messages, Wickr clients automatically copy all messages to the data retention bot user

1. **Message Routing**: AWS Switchboard routes data retention messages to an SNS topic, which feeds into an SQS FIFO queue

1. **Message Assembly**: Encrypted message content

1. **Secure Decryption**: Messages are sent to AWS Nitro Enclaves, which:
   + Use your Customer KMS key to decrypt the data retention bot's private keys
   + Decrypt the Wickr-encrypted message content
   + Re-encrypt will ensure each message encryption is unique.

1. **Storage**: KMS encrypted messages are written to your S3 bucket through PrivateLink

1. **On-Demand Decryption**: The service now includes a Step Functions state machine for on-demand decryption of retained messages

## Security architecture
<a name="security-architecture"></a>
+ **End-to-End Encryption Maintained To Nitro**: Messages remain Wickr-encrypted until they reach the Nitro Enclave
+ **Nitro Enclave Attestation**: KMS publishes the enclave's attestation when allowing decrypt operations
+ **Customer KMS Control**: You maintain full control over encryption keys and can revoke access at any time
+ **Data Sovereignty**: All decrypted data resides only in your AWS account
+ **No AWS Access**: AWS Wickr service cannot access your decrypted message content