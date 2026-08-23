# Partner FAQ

The following questions are frequently asked by AWS Partners implementing Partner Revenue Measurement.

## 1. General Questions

### 1.1 What is Partner Revenue Measurement?

Partner Revenue Measurement is a set of capabilities that enables AWS Partners to measure the AWS service consumption driven by their solutions and quantify their impact on overall AWS revenue. These capabilities empower AWS Partners to better understand their AWS revenue impact and product consumption patterns. Partner Revenue Measurement offers three implementation options: [AWS Marketplace Metering](marketplace-metering.md "marketplace-metering.md"), [Resource Tagging](resource-tagging.md "resource-tagging.md"), and [User Agent String](user-agent-string.md "user-agent-string.md").

### 1.2 Which AWS services are supported by Partner Revenue Measurement?

Partner Revenue Measurement supports AWS services across implementation methods. The supported services vary by method. See [AWS Marketplace Metering included services](included-aws-services-marketplace-metering.md "included-aws-services-marketplace-metering.md"), [Resource Tagging included services](resource-tagging-included-services.md "resource-tagging-included-services.md"), and [User Agent String included services](user-agent-included-services.md "user-agent-included-services.md") for complete lists.

### 1.3 Where do I find my AWS Marketplace product code?

Log in to **AWS Marketplace Management Portal**, navigate to your **Products** page, select your product, and find the product code in the **Product Summary** section. The product code format is typically a long alphanumeric string like: **5ugbbrmu7ud3u5hsipfzug61p**. Please do **NOT** use the Product ID or the UUID formatted product ID from the AWS Marketplace listing. For further information, refer to [Retrieve your product code](product-code-retrieval.md "product-code-retrieval.md").

### 1.4 What architecture patterns does Partner Revenue Measurement support?

Partner Revenue Measurement supports three architecture patterns: 1) Partner Account - all components in partner's AWS account/VPC, 2) Customer Account - all components in customer's AWS account/VPC, 3) Hybrid - components distributed across both partner and customer accounts/VPCs.

### 1.5 How do I get support for Partner Revenue Measurement implementation?

Contact your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support") (Partner Central login required) for validation assistance and support with your Partner Revenue Measurement implementation.

### 1.6 How should I handle if there is another tag on the AWS resource?

Since an AWS resource can only have one tag with the `aws-apn-id` key, only one partner identifier is allowed per resource. For multi-partner scenarios where multiple partners operate on the same AWS resource, consider using the [User Agent String](user-agent-string.md "user-agent-string.md") method instead. If you must use resource tagging, coordinate with the other partner and the customer to determine tag ownership before making changes.

### 1.7 Who can remove tags?

Any user that has access to the account can remove a tag. Both customers and partners (if they have access to the customer's account) can remove tags.

### 1.8 Which regions are currently supported?

Partner Revenue Measurement currently supports only Commercial regions, not European Sovereign Cloud (ESC) or US GovCloud / Amazon Dedicated Cloud (ADC).

### 1.9 How often does my partner solution need to make regular AWS API/CLI calls for User Agent based attribution?

Your partner solution must make at least one regular AWS API/CLI call per resource per month. Attribution is evaluated on a monthly billing cycle. If no calls are made on a resource in a given month, that resource does not contribute to revenue attribution for that month. Attribution resumes the next month a qualifying call is made. In scenarios where your partner solution does not make frequent calls, you can use non-mutating, read-only calls (such as `Describe*` operations) to demonstrate continued interaction. Refer to the [included services](user-agent-included-services.md "user-agent-included-services.md") for supported API actions.

### 1.10 What are my options if the customer's environment does not permit additional resource tags?

Use the [User Agent String](user-agent-string.md "user-agent-string.md") method instead. User Agent strings do not require adding user-defined tags to any AWS resource, do not consume the customer's tag quota, and do not interfere with existing tag policies. The User Agent string is captured in AWS CloudTrail logs, which also provides the customer with operational visibility into partner solution activity for auditing and operational excellence purposes.

## 2. Troubleshooting

For troubleshooting guidance across all implementation methods, see [Troubleshooting Partner Revenue Measurement](troubleshooting.md "troubleshooting.md").

## 3. Additional FAQs

For additional FAQs, see the Partner Revenue Measurement FAQs on [AWS Partner Central](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Funding_Operations_and_Management&article=Partner-Revenue-Measurement-Overview "https://partnercentral.awspartner.com/partnercentral2/s/article?category=Funding_Operations_and_Management&article=Partner-Revenue-Measurement-Overview") (login required).
