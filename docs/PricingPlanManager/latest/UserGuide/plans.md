

# Available Plans
<a name="plans"></a>

## CloudFront Flat-Rate Plans
<a name="cloudfront-plans"></a>

CloudFront Flat-Rate Plans combine global content delivery with AWS WAF, DDoS protection, Amazon Route 53 DNS, Amazon CloudWatch Logs ingestion, Amazon S3 storage credits, and serverless edge compute into a simple monthly price with no overage charges. Each plan includes predefined usage allowances for these integrated services.

### Plan Tiers
<a name="plan-tiers"></a>
+ Free (USD $0/month) - 1M requests, 100GB transfer
+ Pro (USD $15/month) - 10M requests, 50TB transfer
+ Business (USD $200/month) - 125M requests, 50TB transfer
+ Premium (from USD $1,000/month) - 500M requests, 50TB transfer at the default usage level

On the Premium plan, you can increase your monthly usage allowances by selecting a higher usage level. For more information, see [Premium usage levels](#premium-usage-levels).

#### Premium usage levels
<a name="premium-usage-levels"></a>

The Premium plan offers configurable monthly usage allowances. When you subscribe to or manage a Premium plan, you can select a higher monthly usage allowance from the following levels:


| Usage level | Monthly data transfer | Monthly requests | Flat-rate price per month | 
| --- | --- | --- | --- | 
|  `DEFAULT`  | 50 TB | 500 M | USD $1,000 | 
|  `CF_PREMIUM_L2`  | 75 TB | 750 M | USD $1,450 | 
|  `CF_PREMIUM_L3`  | 125 TB | 1.25 B | USD $2,250 | 
|  `CF_PREMIUM_L4`  | 200 TB | 2 B | USD $3,500 | 
|  `CF_PREMIUM_L5`  | 350 TB | 3.5 B | USD $6,000 | 
|  `CF_PREMIUM_L6`  | 600 TB | 6 B | USD $10,000 | 

When you select a higher usage level, your monthly price and usage allowance both increase. The features and services included in the Premium plan remain the same at every usage level. You are only changing your usage allowance and flat-rate price.

When you increase your usage level, the changes take effect immediately and AWS prorates your price. When you decrease your usage level, the change takes effect at the beginning of the next billing cycle.

If your application’s baseline usage exceeds 6 B requests or 600 TB per month, contact [AWS Sales Support](https://aws.amazon.com/contact-us/sales-support/) on the AWS website for custom pricing.

### Usage Monitoring
<a name="usage-monitoring"></a>

You can monitor your CloudFront flat-rate plan usage through the CloudFront console. The console displays your usage percentage tracking against monthly allowances and days remaining in the current billing cycle. Email notifications are sent when you reach 50%, 80%, and 100% of your monthly allowance.

### Account Requirements
<a name="account-requirements"></a>

Free Tier accounts cannot use CloudFront Flat-Rate Plans.

### Service Code
<a name="service-code"></a>

 `CloudFrontPlans` 

For technical details and feature specifications, see the [CloudFront documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html).