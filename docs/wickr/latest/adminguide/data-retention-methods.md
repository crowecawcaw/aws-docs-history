This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Data retention methods

AWS Wickr offers two data retention deployment options:

**Docker-Based Method (Traditional)**

**Advantages**

- Decryption can occur in your location of choice, including on-premises
- Data can be stored unencrypted on customer-controlled hardware
- Full control over infrastructure and deployment environment
  **Limitations**

- Complex setup requiring physical/virtual hardware and Docker expertise
- Customer responsibility to maintain bot, monitor health, and handle
  failures
- Manual scaling and upgrade processes
- No built-in monitoring or alerting
  **Serverless Method**

**Advantages**

- Easy deployment with console-guided setup and minimal steps
- No infrastructure maintenance required
- Decryption within secure AWS Nitro Enclaves
- Automatic scaling and fault tolerance
- Pre-configured monitoring and alerting
- Decrypted messages stored in your customer owned KMS-encrypted S3
  bucket
  **Limitations**

- Decryption occurs on AWS infrastructure (though within secure enclaves using
  your customer owned KMS keys)
- Reading S3 contents requires using the provided decryption lambda
