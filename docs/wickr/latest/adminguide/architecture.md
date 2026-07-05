This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Architecture Overview

## Message flow

1. **Message Capture**: When users send messages, Wickr
   clients automatically copy all messages to the data retention bot
   user
2. **Message Routing**: AWS Switchboard routes data
   retention messages to an SNS topic, which feeds into an SQS FIFO
   queue
3. **Message Assembly**: Encrypted message content
4. **Secure Decryption**: Messages are sent to AWS Nitro
   Enclaves, which:

   - Use your Customer KMS key to decrypt the data retention bot's
     private keys
   - Decrypt the Wickr-encrypted message content
   - Re-encrypt will ensure each message encryption is unique.

5. **Storage**: KMS encrypted messages are written to your
   S3 bucket through PrivateLink
6. **On-Demand Decryption**: The service now includes a Step
   Functions state machine for on-demand decryption of retained messages

## Security architecture

- **End-to-End Encryption Maintained To Nitro**: Messages
  remain Wickr-encrypted until they reach the Nitro Enclave
- **Nitro Enclave Attestation**: KMS publishes the
  enclave's attestation when allowing decrypt operations
- **Customer KMS Control**: You maintain full control over
  encryption keys and can revoke access at any time
- **Data Sovereignty**: All decrypted data resides only in
  your AWS account
- **No AWS Access**: AWS Wickr service cannot access
  your decrypted message content
