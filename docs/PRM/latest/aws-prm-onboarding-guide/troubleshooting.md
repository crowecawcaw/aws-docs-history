# Troubleshooting Partner Revenue Measurement

## Resource Tagging Issues

### Tags not providing revenue attribution

If resource tags are not generating revenue attribution:

###### Verify tag implementation

1. Check tag key is exactly: **aws-apn-id** (lowercase)
2. Verify tag value format: **pc:product-code**
3. Confirm product code matches AWS Marketplace listing (see [Retrieve your product code](product-code-retrieval.md "product-code-retrieval.md"))
4. Ensure resources are in [supported services](included-aws-services.md#resource-tagging-supported-services "included-aws-services.md#resource-tagging-supported-services")
5. Check that resources are actively consuming AWS services and incurring spend. Partner Revenue Measurement tracks revenue attribution based on AWS service consumption. For example, IAM is a no-cost AWS service, so tagging IAM resources will not generate revenue attribution. Focus on tagging resources that incur charges such as EC2 instances, S3 buckets with storage, RDS databases, or Lambda functions with invocations
6. Verify tags are applied correctly using [AWS Tag Editor](automated-tagging.md#tag-editor-bulk-tagging "automated-tagging.md#tag-editor-bulk-tagging") or reach out to your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support") (Partner Central login required) for assistance

### Tag conflicts with other partners

When multiple partners try to tag the same resource:

###### Resolve tag conflicts

1. Identify existing `aws-apn-id` tag on resource
2. Remove existing tag: `aws resourcegroupstaggingapi untag-resources`
3. Add your tag: `aws resourcegroupstaggingapi tag-resources`
4. Document tag ownership change for audit purposes

## Validation and Testing

### AWS Partner Team validation

For official validation, contact your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support") (Partner Central login required):

- Include: AWS account ID, region, product code, sample resource ARN
- Provide: Tag screenshots and test timestamps
- Allow: 3-5 business days for validation response

## Common Implementation Errors

| Common Partner Revenue Measurement Implementation Issues | Issue                         | Cause                                                                                                                                                                                                                                                                                                                                | Solution |
| -------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| Tags not working                                         | Wrong tag format              | Use aws-apn-id key with pc:product-code value                                                                                                                                                                                                                                                                                        |
| No revenue attribution                                   | Resources not incurring spend | Ensure resources are actively consuming AWS services and incurring charges. For example, IAM is a no-cost service, so tagging IAM resources will not generate revenue attribution. Focus on tagging resources that incur charges such as EC2 instances, S3 buckets with storage, RDS databases, or Lambda functions with invocations |
| Product code mismatch                                    | Incorrect product code        | Verify code in AWS Marketplace Management Portal (see Product Code Retrieval section)                                                                                                                                                                                                                                                |
