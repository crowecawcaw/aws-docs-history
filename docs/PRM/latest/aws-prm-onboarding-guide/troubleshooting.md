

# Troubleshooting Partner Revenue Measurement
<a name="troubleshooting"></a>

This section provides troubleshooting guidance for each Partner Revenue Measurement implementation method:
+ [AWS Marketplace Metering Issues](#marketplace-metering-troubleshooting)
+ [Resource Tagging Issues](#resource-tagging-troubleshooting)
+ [User Agent String Issues](#user-agent-troubleshooting)

## AWS Marketplace Metering Issues
<a name="marketplace-metering-troubleshooting"></a>

AWS Marketplace Metering is a fully automated, zero-touch experience. Revenue attribution occurs automatically when customers purchase and use your AMI or ML product through AWS Marketplace. No additional implementation is required from partners.

If you are experiencing issues with revenue attribution for your AWS Marketplace Metering products, open a support ticket through [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support) (Partner Central login required). Include the following details:
+ AWS account ID
+ AWS Marketplace product code
+ Product type (AMI or ML)
+ Description of the issue and expected behavior

## Resource Tagging Issues
<a name="resource-tagging-troubleshooting"></a>

### Tags not providing revenue attribution
<a name="tags-not-working"></a>

If resource tags are not generating revenue attribution:

**Verify tag implementation**

1. Check tag key is exactly: **aws-apn-id** (lowercase)

1. Verify tag value format: **pc:product-code**

1. Confirm product code matches AWS Marketplace listing (see [Product Code Retrieval](product-code-retrieval.md))

1. Ensure resources are in [supported services](resource-tagging-included-services.md)

1. Check that resources are actively consuming AWS services and incurring spend. For example, IAM is a no-cost AWS service, so tagging IAM resources does not generate revenue attribution. Focus on tagging resources that incur charges such as EC2 instances, S3 buckets with storage, RDS databases, or Lambda functions with invocations

1. Verify tags are applied correctly using [AWS Tag Editor](automated-tagging.md#tag-editor-bulk-tagging) or reach out to your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support) (Partner Central login required) for assistance

### Tag conflicts with other partners
<a name="tag-conflicts"></a>

Since an AWS resource can only have one tag with the `aws-apn-id` key, only one partner identifier is allowed per resource. If another partner's tag exists on a resource, resource tagging creates a conflict.

For multi-partner scenarios where multiple partners operate on the same AWS resource, consider using the [User Agent String](user-agent-string.md) method instead. Each partner can independently use their own identifier within their respective regular AWS API/CLI calls without conflicts.

If you must use resource tagging, coordinate with the other partner and the customer to determine tag ownership before making changes.

## User Agent String Issues
<a name="user-agent-troubleshooting"></a>

### User Agent string not appearing in CloudTrail
<a name="user-agent-not-in-cloudtrail"></a>

If your User Agent string is not visible in CloudTrail logs:

**Verify User Agent implementation**

1. Confirm the format is exactly: `APN_1.1/pc_<YOUR-PRODUCT-CODE>$`

1. Verify the `$` end delimiter is present and not stripped by your shell or runtime

1. Confirm product code matches AWS Marketplace listing (see [Product Code Retrieval](product-code-retrieval.md))

1. Ensure the User Agent string is applied to the correct AWS SDK client configuration, not just one service client

1. Check CloudTrail is enabled and logging the relevant API calls in the correct region

1. Verify the `userAgent` field in CloudTrail events contains your string

### Common format errors
<a name="user-agent-format-errors"></a>


**Common User Agent String Format Issues**  

| Issue | Cause | Solution | 
| --- | --- | --- | 
| Missing end delimiter | The $ character was omitted or escaped by the shell | Ensure the string ends with $. Use single quotes or escape appropriately for your shell | 
| Wrong prefix | Using incorrect prefix format | Use exactly APN\_1.1/pc\_ as the prefix | 
| Product code mismatch | Using Product ID or UUID instead of product code | Retrieve the alphanumeric product code from AWS Marketplace Management Portal (see [Product Code Retrieval](product-code-retrieval.md)) | 
| No API operations on resources | Resources not receiving API calls in a given month | Ensure your product performs at least one API operation on an AWS resource per month for attribution | 

### CloudTrail Logs Verification
<a name="cloudtrail-logs-verification"></a>

Use the following command to verify your User Agent string appears in CloudTrail logs:

```
aws logs filter-log-events \
  --log-group-name CloudTrail/YourLogGroup \
  --filter-pattern "APN_1.1" \
  --start-time 1640995200000
```

Look for the `userAgent` field in CloudTrail events. The format should match: `APN_1.1/pc_<YOUR-PRODUCT-CODE>$`

## Validation and Testing
<a name="validation-troubleshooting"></a>

### AWS Partner Team validation
<a name="partner-team-validation"></a>

For official validation, contact your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support) (Partner Central login required):
+ Include: AWS account ID, region, product code, sample resource ARN
+ Provide: Tag screenshots or CloudTrail log excerpts and test timestamps
+ Allow: 3-5 business days for validation response

## Common Implementation Errors
<a name="common-errors"></a>


**Common Partner Revenue Measurement Implementation Issues**  

| Method | Issue | Cause | Solution | 
| --- | --- | --- | --- | 
| Resource Tagging | Tags not working | Wrong tag format | Use aws-apn-id key with pc:product-code value | 
| Resource Tagging | No revenue attribution | Resources not incurring spend | Ensure resources are actively consuming AWS services and incurring charges | 
| Resource Tagging | Product code mismatch | Incorrect product code | Verify code in AWS Marketplace Management Portal (see [Product Code Retrieval](product-code-retrieval.md)) | 
| User Agent String | String not in CloudTrail | SDK not configured correctly | Verify SDK client configuration includes User Agent string for all service clients | 
| User Agent String | Missing delimiter | $ stripped by shell | Use single quotes or escape the $ character appropriately | 
| Marketplace Metering | No attribution | Product not purchased via Marketplace | Ensure customers purchase and use the product through AWS Marketplace. Open a support ticket via [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support) | 

## Contact Information
<a name="contact-information"></a>

For any further questions about Partner Revenue Measurement (PRM) compliance requirements, please contact your AWS Partner Development team or [AWS Partner Network support](https://partnercentral.awspartner.com/partnercentral2/s/support).