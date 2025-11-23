# Manage data encryption in

IAM-based domains

Data encryption in IAM-based domains protects your data at rest and in transit within
Amazon SageMaker Unified Studio. You can choose between AWS-managed encryption keys for simplified
management or customer-managed AWS KMS keys for enhanced control over encryption
operations. Encryption settings are configured during domain setup and cannot be changed
after domain creation.

AWS-managed encryption provides automatic key management with no additional
configuration required. Customer-managed encryption enables you to control key policies,
rotation schedules, and access permissions while requiring additional IAM policy
configuration for your roles.

All data stored in the default Amazon S3 bucket created by Amazon SageMaker Unified Studio is encrypted
according to your chosen encryption configuration. The encryption settings apply to all
projects and resources within the domain.

Prerequisites:

- Understanding of AWS KMS key management concepts
- Appropriate IAM permissions to use or create KMS keys
- Decision on encryption approach based on your security requirements
  Configure AWS-managed encryption (default):

1. During domain setup, leave the **Customize encryption settings
   (advanced)** option unchecked.
2. The system automatically configures encryption using AWS-owned and managed
   keys.
3. No additional IAM policy configuration is required for AWS-managed
   encryption.
   Configure customer-managed encryption:

4. During domain setup, check **Customize encryption settings
   (advanced)**.
5. Choose **Choose an AWS KMS key** and select one of the following
   options:
   - Select an existing KMS key from the dropdown menu
   - Enter a KMS key ARN directly in the text field
   - Choose **Create new KMS Key** to create a new key

6. If creating a new key, configure the key policy to allow access from your IAM
   roles.
7. Add the inline policy to your Login and Execution IAM roles to enable KMS key
   usage.
8. Replace the resource ARN with your actual KMS key ARN.
9. Complete the domain setup process with your encryption configuration.

###### Warning

Encryption settings cannot be modified after domain creation. Choose your encryption
approach carefully based on your long-term security requirements.
