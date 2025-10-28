# Configuring server-side encryption for a

queue using SQS-managed encryption keys

In addition to the [default](creating-sqs-standard-queues.md#step-create-standard-queue "creating-sqs-standard-queues.md#step-create-standard-queue") Amazon SQS managed server-side encryption (SSE) option, Amazon SQS
managed SSE (SSE-SQS) lets you create custom managed server-side encryption that uses
SQS-managed encryption keys to protect sensitive data sent over message queues. With
SSE-SQS, you don't need to create and manage encryption keys, or modify your code to
encrypt your data. SSE-SQS lets you transmit data securely and helps you meet strict
encryption compliance and regulatory requirements at no additional cost.

SSE-SQS protects data at rest using 256-bit Advanced Encryption Standard (AES-256)
encryption. SSE encrypts messages as soon as Amazon SQS receives them. Amazon SQS stores messages in
encrypted form and decrypts them only when sending them to an authorized consumer.

###### Note

- The default SSE option is only effective when you create a queue without
  specifying encryption attributes.
- Amazon SQS allows you to turn off all queue encryption. Therefore, turning off
  KMS-SSE, will not automatically enable SQS-SSE. If you wish to enable SQS-SSE
  after turning off KMS-SSE, you must add an attribute change in the
  request.

###### To configure SSE-SQS encryption for a queue (console)

###### Note

Any new queue created using the HTTP (non-TLS) endpoint will not enable SSE-SQS
encryption by default. It is a security best practice to create Amazon SQS queues using
HTTPS or [Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md")
endpoints.

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. Choose a queue, and then choose **Edit**.
4. Expand **Encryption**.
5. For **Server-side encryption**, choose **Enabled**
   (default).

###### Note

With SSE enabled, anonymous `SendMessage` and
`ReceiveMessage` requests to the encrypted queue will be
rejected. Amazon SQS security best practises recommend against using anonymous
requests. If you wish to send anonymous requests to an Amazon SQS queue, make sure to
disable SSE. 6. Select **Amazon SQS key (SSE-SQS)**. There is no additional fee
for using this option. 7. Choose **Save**.
