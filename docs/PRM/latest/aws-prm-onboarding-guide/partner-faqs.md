

# Partner FAQ
<a name="partner-faqs"></a>

The following questions are frequently asked by AWS Partners implementing Partner Revenue Measurement.

## 1. General Questions
<a name="general-faqs"></a>

### 1.1 What is Partner Revenue Measurement?
<a name="what-is-prm-faq"></a>

Partner Revenue Measurement is a set of capabilities that enables AWS Partners to measure the AWS service consumption driven by their solutions and quantify their impact on overall AWS revenue. These capabilities empower AWS Partners to better understand their AWS revenue impact and product consumption patterns. Partner Revenue Measurement offers three implementation options: [AWS Marketplace Metering](marketplace-metering.md), [Resource Tagging](resource-tagging.md), and [User Agent String](user-agent-string.md).

### 1.2 Which AWS services are supported by Partner Revenue Measurement?
<a name="supported-services-faq"></a>

Partner Revenue Measurement supports AWS services across implementation methods. The supported services vary by method. See [AWS Marketplace Metering included services](included-aws-services-marketplace-metering.md), [Resource Tagging included services](resource-tagging-included-services.md), and [User Agent String included services](user-agent-included-services.md) for complete lists.

### 1.3 Where do I find my AWS Marketplace product code?
<a name="product-code-location-faq"></a>

Log in to **AWS Marketplace Management Portal**, navigate to your **Products** page, select your product, and find the product code in the **Product Summary** section. The product code format is typically a long alphanumeric string like: **5ugbbrmu7ud3u5hsipfzug61p**. Please do **NOT** use the Product ID or the UUID formatted product ID from the AWS Marketplace listing. For further information, refer to [Retrieve your product code](product-code-retrieval.md).

### 1.4 What architecture patterns does Partner Revenue Measurement support?
<a name="architecture-patterns-faq"></a>

Partner Revenue Measurement supports three architecture patterns: 1) Partner Account - all components in partner's AWS account/VPC, 2) Customer Account - all components in customer's AWS account/VPC, 3) Hybrid - components distributed across both partner and customer accounts/VPCs.

### 1.5 How do I get support for Partner Revenue Measurement implementation?
<a name="support-contact-faq"></a>

Contact your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support) (Partner Central login required) for validation assistance and support with your Partner Revenue Measurement implementation.

### 1.6 Where do I find my Partner Central AWS Account ID?
<a name="where-account-id-faq"></a>

Your Partner Central AWS Account ID is the 12-digit number located in the upper right corner of the Partner Central homepage. For more information on the account ID, see [Viewing your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html) in the IAM User Guide. For how to construct your tag key, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction).

### 1.7 How should I handle if there is another partner's tag on the AWS resource?
<a name="handle-existing-tags-faq"></a>

If another partner has already tagged the resource, you can simply add your own tag. You do not need to remove any existing tags. Each partner uses their own partner-unique tag key in the format `aws-apn-id-{{partner-central-aws-account-id}}`, with the tag value `pc:{{product-code}}`, so multiple partners - up to 10 per resource - can tag the same resource independently and each receives attribution. You only need to remove and replace a tag when updating your own tag on the resource. The AWS customer is the decision maker on which partner tags can be used on a particular resource.

For how to construct your tag key, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction).

### 1.8 Who can remove tags?
<a name="who-can-remove-tags-faq"></a>

Any user that has access to the account can remove a tag. Both customers and partners (if they have access to the customer's account) can remove tags.

### 1.9 Which regions are currently supported?
<a name="supported-regions-faq"></a>

Partner Revenue Measurement currently supports only Commercial regions, not European Sovereign Cloud (ESC) or US GovCloud / Amazon Dedicated Cloud (ADC).

### 1.10 How often does my partner solution need to make regular AWS API/CLI calls for User Agent based attribution?
<a name="api-cadence-faq"></a>

Your partner solution must make at least one regular AWS API/CLI call per resource per month. Attribution is evaluated on a monthly billing cycle. If no calls are made on a resource in a given month, that resource does not contribute to revenue attribution for that month. Attribution resumes the next month a qualifying call is made. In scenarios where your partner solution does not make frequent calls, you can use non-mutating, read-only calls (such as `Describe*` operations) to demonstrate continued interaction. Refer to the [included services](user-agent-included-services.md) for supported API actions.

### 1.11 What are my options if the customer's environment does not permit additional resource tags?
<a name="customer-tag-restrictions-faq"></a>

Use the [User Agent String](user-agent-string.md) method instead. User Agent strings do not require adding user-defined tags to any AWS resource, do not consume the customer's tag quota, and do not interfere with existing tag policies. The User Agent string is captured in AWS CloudTrail logs, which also provides the customer with operational visibility into partner solution activity for auditing and operational excellence purposes.

**Note**  
When using the account-suffixed tag key format (`aws-apn-id-{{partner-central-aws-account-id}}`), each partner consumes one tag slot per resource. Ensure the total number of partner tags plus existing customer tags fits within the [50-tag-per-resource limit](https://docs.aws.amazon.com/tag-editor/latest/userguide/reference.html). For how to construct your tag key, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction).

## 2. Troubleshooting
<a name="troubleshooting-faqs"></a>

For troubleshooting guidance across all implementation methods, see [Troubleshooting Partner Revenue Measurement](troubleshooting.md).

## 3. Additional FAQs
<a name="additional-faqs"></a>

For additional FAQs, see the Partner Revenue Measurement FAQs on [AWS Partner Central](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Funding_Operations_and_Management&article=Partner-Revenue-Measurement-Overview) (login required).