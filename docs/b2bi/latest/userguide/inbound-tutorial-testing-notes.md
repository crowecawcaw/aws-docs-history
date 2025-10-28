# Testing notes - Documentation team

validation

**Account Used:** Merlon account (smrcua) for testing and
validation

## Resources created for testing

(us-east-1)

1. **Amazon S3 Buckets:**
   - `arn:aws:s3:::my-b2bi-input-bucket-smrcua`
   - `arn:aws:s3:::my-b2bi-output-bucket-smrcua`

2. **EventBridge Configuration:**
   - Turned on EventBridge notifications for both buckets

3. **AWS B2B Data Interchange Resources:**
   - **Profile:** AcmeCorpProfile
   - **Transformer:** Created and
     activated using S3 sample files approach
   - **Trading Capability:** Successfully
     configured with S3 bucket validation
   - **Partnership:** Created with inbound
     EDI configuration

## Documentation updates

made

- **Transformer Creation Procedure:**
  Significant changes made to align with outbound tutorial improvements
- **S3 Sample Files Approach:** Updated to use
  S3-stored sample files instead of inline content pasting
- **UI Field Updates:** Restructured to match
  current AWS Management Console interface with separate Input/Output details
  sections
- **Phone Number Format:** Updated to
  consistent format (+1-555-012-3456)
- **Status:** Changes align with outbound
  tutorial improvements and current AWS Management Console behavior

###### Note

This testing validates the tutorial steps work correctly in a real AWS
environment and ensures consistency with the outbound tutorial
improvements.
