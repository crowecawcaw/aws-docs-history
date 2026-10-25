

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Architecture Overview
<a name="architecture"></a>

The following diagram shows the components of serverless data retention and which account each one runs in. Wickr Message Routing and the Nitro Enclave run in the Wickr-managed service account. Your AWS KMS keys, the cross-account IAM role, the retention and decrypted Amazon S3 buckets, the on-demand decryption workflow, and CloudWatch monitoring run in your account.

A Wickr client sends an end-to-end encrypted message through Wickr Message Routing. Within the AWS Nitro Enclave, Wickr decrypts messages and re-encrypts them with your customer managed KMS key before sending them to your encrypted retention Amazon S3 bucket. The service uses your key through the cross-account IAM role. For more information, see [Where data retention components run](serverless-method.md#where-components-run).

![Serverless data retention architecture with two flows: numbered retention steps 1 to 5 from the Wickr client to the retention bucket, and lettered on-demand decryption steps A to C in your account.](https://docs.aws.amazon.com/wickr/latest/adminguide/images/serverless-dr-architecture.png)


The numbered steps in the diagram show how every message is retained:

1. A Wickr client sends an end-to-end encrypted copy of the message to the data retention bot user, through Wickr Message Routing.

1. Wickr Message Routing fetches the Data Retention Service keys, which are stored encrypted with your KMS key. It sends them with the ciphertext to the enclave host.

1. The enclave host assumes the cross-account IAM role in your account. The host relays only ciphertext to the Nitro Enclave.

1. The enclave uses your KMS key to decrypt the Data Retention Service keys. Wickr then decrypts the message and re-encrypts it with your customer managed KMS key.

1. The encrypted message is stored in your retention Amazon S3 bucket.

The lettered steps show on-demand decryption, which runs only when you start it:

1. Your compliance team starts the decryption workflow for a date range.

1. The workflow reads the encrypted objects from the retention bucket and decrypts them with your KMS key.

1. The workflow writes the decrypted output to the decrypted Amazon S3 bucket in your account.

CloudWatch monitors the retention bucket and your KMS key.

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