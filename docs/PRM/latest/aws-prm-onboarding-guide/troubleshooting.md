

# Troubleshooting AWS Revenue Measurement

This section provides troubleshooting guidance for each AWS Revenue Measurement implementation method:
+ [AWS Marketplace Metering Issues](#marketplace-metering-troubleshooting)
+ [Resource Tagging Issues](#resource-tagging-troubleshooting)
+ [User Agent String Issues](#user-agent-troubleshooting)
+ [Identity Tagging Issues](#identity-tagging-troubleshooting)

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

1. Check tag key matches the format: **aws-apn-id-{{partner-central-aws-account-id}}** (or the simple `aws-apn-id` key). For how to construct your tag key, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction)

1. Confirm your Partner Central AWS account ID is correct. For where to find it, see [Where do I find my Partner Central AWS Account ID?](partner-faqs.md#where-account-id-faq)

1. Verify tag value format: **pc:product-code**

1. Confirm product code matches AWS Marketplace listing (see [Product Code Retrieval](product-code-retrieval.md))

1. Ensure resources are in [supported services](resource-tagging-included-services.md)

1. Check that resources are actively consuming AWS services and incurring spend. For example, IAM is a no-cost AWS service, so tagging IAM resources does not generate revenue attribution. Focus on tagging resources that incur charges such as EC2 instances, S3 buckets with storage, RDS databases, or Lambda functions with invocations

1. Verify tags are applied correctly using [AWS Tag Editor](automated-tagging.md#tag-editor-bulk-tagging) or reach out to your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support) (Partner Central login required) for assistance

### Multi-partner scenarios
<a name="tag-conflicts"></a>

Multiple partners can tag the same AWS resource without conflict. Each partner uses their own partner-unique tag key in the format `aws-apn-id-{{partner-central-aws-account-id}}`, with the tag value `pc:{{product-code}}`, and up to 10 partners can tag the same resource. Because each partner tags under their own unique key, an existing partner tag does not need to be removed and does not create a conflict. If your tag is not generating attribution, confirm your key uses the exact format `aws-apn-id-{{partner-central-aws-account-id}}` and that the value is `pc:{{product-code}}`. For how to construct your tag key, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction).

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

## Identity Tagging Issues
<a name="identity-tagging-troubleshooting"></a>

### Tag not generating revenue attribution
<a name="identity-tag-not-working"></a>

If your Identity Tagging tag is not generating revenue attribution:
+ **Verify tag key format:** Confirm the tag key matches the format `aws-apn-id-{{partner-central-aws-account-id}}` (e.g., `aws-apn-id-123456789012`). Ensure your Partner Central AWS account ID is correct.
+ **Verify tag value format:** Confirm the tag value is `pc:{{product-code}}` and that the product code matches your AWS Marketplace listing.
+ **Confirm product listing:** The product code must correspond to a product listing on AWS Marketplace for your partner account. Tags referencing a product code without a matching listing are rejected for attribution.
+ **Confirm supported principal type:** Identity Tagging supports IAM roles (cross-account and same-account) and IAM users only. Federated users via AWS IAM Identity Center (permission sets) are not supported at launch.
+ **Confirm activity on billable resources:** Attribution requires that the tagged principal perform API actions on billable AWS resources. Account-level operations that do not reference a billable resource (e.g., `sts:AssumeRole`, `iam:ListRoles`) do not generate attribution. Ensure your tagged identity is performing operations on resources that incur AWS charges.
+ **Check attribution timing:** Attribution does not begin in the same billing month the tag is detected. Attribution starts from the billing month following tag detection. The detection SLA is five calendar days.

### Verification steps
<a name="identity-verification-steps"></a>

Verify your tag is correctly applied using the AWS CLI:

For IAM roles:

```
aws iam list-role-tags --role-name MyPartnerRole
```

For IAM users:

```
aws iam list-user-tags --user-name MyPartnerUser
```

Confirm the output includes your tag key (`aws-apn-id-{{partner-central-aws-account-id}}`) and value (`pc:{{product-code}}`).

To verify your tagged identity's activity on billable resources, search CloudTrail for API events from your tagged principal ARN and confirm the events reference billable resource ARNs.

### Multi-partner Identity Tagging scenarios
<a name="identity-multi-partner"></a>

Multiple partners can independently tag the same IAM principal using their own partner-scoped keys. Each partner receives attribution when their tagged identity performs API actions on billable resources. If you are not receiving attribution in a multi-partner scenario, confirm your tag key uses the exact format `aws-apn-id-{{partner-central-aws-account-id}}` and that the value is `pc:{{product-code}}`.

### Common implementation errors
<a name="identity-common-errors"></a>


**Common Identity Tagging Implementation Issues**  

| Issue | Cause | Solution | 
| --- | --- | --- | 
| Tag key missing account ID | Used aws-apn-id without the partner account ID suffix | Use the full format: aws-apn-id-<partner-central-aws-account-id> | 
| Product code mismatch | Product code in tag value does not match any Marketplace listing | Verify your product code in the AWS Marketplace Management Portal | 
| Unsupported principal type | Tag applied to an IAM Identity Center permission set or federated session | Use an IAM role (cross-account or same-account) or IAM user instead | 
| No billable resource activity | Tagged identity only performs non-billable operations (e.g., sts:AssumeRole) | Ensure the tagged identity performs API actions on resources that incur AWS charges | 
| Attribution not appearing | Tag was applied in the current billing month | Wait for the following billing month — attribution begins the month after tag detection | 
| Tag removed by customer | Customer or another user removed the tag from the IAM principal | Re-apply the tag; attribution is retained for the month of removal and stops the following month | 

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


**Common AWS Revenue Measurement Implementation Issues**  

| Method | Issue | Cause | Solution | 
| --- | --- | --- | --- | 
| Resource Tagging | Tags not working | Wrong tag format | Use aws-apn-id-{{partner-central-aws-account-id}} key (or aws-apn-id) with pc:product-code value. See [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction) | 
| Resource Tagging | No revenue attribution | Resources not incurring spend | Ensure resources are actively consuming AWS services and incurring charges | 
| Resource Tagging | Product code mismatch | Incorrect product code | Verify code in AWS Marketplace Management Portal (see [Product Code Retrieval](product-code-retrieval.md)) | 
| User Agent String | String not in CloudTrail | SDK not configured correctly | Verify SDK client configuration includes User Agent string for all service clients | 
| User Agent String | Missing delimiter | $ stripped by shell | Use single quotes or escape the $ character appropriately | 
| Marketplace Metering | No attribution | Product not purchased via Marketplace | Ensure customers purchase and use the product through AWS Marketplace. Open a support ticket via [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support) | 

## Contact Information
<a name="contact-information"></a>

For any further questions about AWS Revenue Measurement compliance requirements, please contact your AWS Partner Development team or [AWS Partner Network support](https://partnercentral.awspartner.com/partnercentral2/s/support).