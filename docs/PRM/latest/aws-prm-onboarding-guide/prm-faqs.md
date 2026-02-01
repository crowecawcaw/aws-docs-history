# FAQs

## 1. General Questions

### 1.1 What is Partner Revenue Measurement?

Partner Revenue Measurement refers to AWS Partner Network's (APN) capabilities to track and quantify the impact AWS partners have on overall AWS revenue. Partner Revenue Measurement empowers AWS Partners to demonstrate their AWS revenue impact by tagging AWS resources with their product identifier.

### 1.2 Which AWS services are supported by Partner Revenue Measurement?

Partner Revenue Measurement supports AWS services for resource tagging. See [Resource Tagging supported services](included-aws-services.md#resource-tagging-supported-services "included-aws-services.md#resource-tagging-supported-services") for complete list.

### 1.3 Where do I find my AWS Marketplace product code?

Log in to **AWS Marketplace Management Portal**, navigate to your **Products** page, select your product, and find the product code in the **Product Summary** section. The product code format is typically a long alphanumeric string like: **5ugbbrmu7ud3u5hsipfzug61p**. Please do **NOT** use the Product ID or the UUID formatted product ID from the AWS Marketplace listing. For further information, refer to [Retrieve your product code](product-code-retrieval.md "product-code-retrieval.md").

### 1.4 What architecture patterns does Partner Revenue Measurement support?

Partner Revenue Measurement supports three architecture patterns: 1) Partner Account - all components in partner's AWS account/VPC, 2) Customer Account - all components in customer's AWS account/VPC, 3) Hybrid - components distributed across both partner and customer accounts/VPCs.

### 1.5 How do I get support for Partner Revenue Measurement implementation?

Contact your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support") (Partner Central login required) for validation assistance and support with your Partner Revenue Measurement implementation.

### 1.6 How should I handle if there is another tag on the AWS resource?

Since an AWS resource can only have one tag with the 'aws-apn-id' key, you must remove the existing tag and add your new tag. For example, if an S3 bucket has a tag with key 'aws-apn-id' and value 'pc:5ugbbrmu7ud3u5hsipfzug61p', you need to remove that tag and add your own with key 'aws-apn-id' and value 'pc:5ugbbrmu7ud3u5hsipfzug61p'.

### 1.7 Who can remove tags?

Any user that has access to the account can remove a tag. Both customers and partners (if they have access to the customer's account) can remove tags.

### 1.8 Which regions are currently supported?

Partner Revenue Measurement currently supports only Commercial regions, not European Sovereign Cloud (ESC) or US GovCloud / Amazon Dedicated Cloud (ADC).

## 2. Troubleshooting

### 2.1 My tags are not showing revenue attribution. What should I check?

- Verify tag format: Key must be **aws-apn-id**, value must start with **pc:**
- Confirm product code matches AWS Marketplace listing exactly (see [Retrieve your product code](product-code-retrieval.md "product-code-retrieval.md"))
- Ensure resources are in [supported services](included-aws-services.md#resource-tagging-supported-services "included-aws-services.md#resource-tagging-supported-services")
- Check that resources are actively consuming AWS services and incurring spend. Partner Revenue Measurement tracks revenue attribution based on AWS service consumption. For example, IAM is a no-cost AWS service, so tagging IAM resources will not generate revenue attribution. Focus on tagging resources that incur charges such as EC2 instances, S3 buckets with storage, RDS databases, or Lambda functions with invocations
- Verify tags are applied correctly using [AWS Tag Editor](automated-tagging.md#tag-editor-bulk-tagging "automated-tagging.md#tag-editor-bulk-tagging") or reach out to your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support") (Partner Central login required) for assistance
