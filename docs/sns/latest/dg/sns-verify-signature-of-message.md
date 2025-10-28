# Verifying the signatures of Amazon SNS

messages

Amazon SNS uses message signatures to confirm the authenticity of messages sent to your HTTP
endpoint. To ensure message integrity and prevent spoofing, you **must** verify the signature before processing any Amazon SNS messages.

**When should you verify Amazon SNS signatures?**

You should verify Amazon SNS message signatures in the following scenarios:

- When Amazon SNS sends a notification message to your HTTP(S) endpoint.
- When Amazon SNS sends a confirmation message to your endpoint after a [`Subscribe`](../api/API_Subscribe.md "../api/API_Subscribe.md") or [`Unsubscribe`](../api/API_Unsubscribe.md "../api/API_Unsubscribe.md") API
  call.
  **Amazon SNS supports two signature versions:**

- SignatureVersion1 – Uses an SHA1 hash of the message.
- SignatureVersion2 – Uses an SHA256 hash of the message. This
  provides stronger security and is the recommended option.
  **To correctly verify SNS message signatures, follow these best
  practices:**

- Always retrieve the signing certificate using HTTPS to prevent unauthorized interception
  attacks.
- Check that the certificate is issued by Amazon SNS.
- Confirm that the certificate’s chain of trust is valid.
- The certificate should come from an SNS-signed URL.
- Don't trust any certificates provided in the message without validation.
- Reject any message with an unexpected `TopicArn` to prevent spoofing.
- The AWS SDKs for Amazon SNS provide built-in validation logic, reducing the risk of
  misimplementation.
