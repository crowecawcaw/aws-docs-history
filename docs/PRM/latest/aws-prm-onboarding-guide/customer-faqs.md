

# Customer FAQ

## 1. What is AWS Revenue Measurement?
<a name="customer-what-is-prm-faq"></a>

AWS Revenue Measurement is a set of AWS capabilities that enables AWS and its Partners to measure the AWS service consumption Partners drive through their solutions or services engagements across applicable accounts. It gives Partners and AWS a clear, data-driven view of Partner impact so AWS can better support Partners as they deliver value to our mutual customers.

## 2. Why is my Partner asking to implement AWS Revenue Measurement?
<a name="customer-why-implement-faq"></a>

AWS Revenue Measurement allows AWS to recognize Partners who are driving customer success. To accurately measure the value these Partners are driving, AWS Revenue Measurement will attribute your AWS consumption to Partner engagement. This connection enables AWS to enhance the tools and programs that support our partners and our mutual customers.

## 3. What are the customer benefits of AWS Revenue Measurement?
<a name="customer-benefits-faq"></a>

With AWS Revenue Measurement, customers can map costs to specific Partner products and solutions, better manage their overall portfolio spending, and make more informed decisions about how to allocate resources. Additionally, AWS Revenue Measurement provides operational visibility through AWS CloudTrail logs, giving customers an audit trail of partner solution activity for compliance and operational efficiency.

## 4. What impact does AWS Revenue Measurement have on my AWS environment?
<a name="customer-environment-impact-faq"></a>

AWS Revenue Measurement has no impact on your infrastructure, security posture, and billing structure. AWS Revenue Measurement only enables AWS to recognize and measure the Partner's influence on that environment. AWS Revenue Measurement works by associating a Partner's contributions with existing AWS resource usage through lightweight mechanisms such as [resource tagging](resource-tagging.md), [user agent strings](user-agent-string.md), [identity tagging](identity-tagging.md), or [Account Tagging for SaaS products](account-tagging.md). There is no additional software to install, no performance overhead, and no changes to how workloads run. With this information, AWS can better support both our Partners and our mutual customers.

## 5. What specific data does AWS collect?
<a name="customer-data-collected-faq"></a>

AWS Revenue Measurement uses a tag or identifier--a simple label associated with your Partner's product--to correlate existing billing and usage information that AWS already maintains as part of its standard service operations. A customer's Partner does not receive their raw billing data; AWS provides them only with aggregated, attributed revenue metrics across all customers so a Partner can understand how their product drives AWS service consumption. AWS will collect an AWS Marketplace product code and resource tag, AWS Resource Name (ARN), API operation, ARN usage spend, Service Type, API operation or tag creation date and time, and the AWS Account ID hosting the AWS resource.

## 6. If I allow my Partner to implement AWS Revenue Measurement via resource tagging, how does AWS Revenue Measurement impact my tagging strategy?
<a name="customer-tagging-strategy-faq"></a>

The impact depends on which implementation method your partner uses:

**Resource Tagging:** Each participating partner applies one tag to relevant resources. When more than one partner works on the same resource, multiple partner tags might be present — up to 10 partner tags per resource — and each consumes one of your fifty available user-defined tag slots. You retain full control and can add or remove these tags at any time. If you enforce tag policies through AWS Organizations, you will need a one-time update to allow for the tag key. You remain in full control: the Partner can only apply tags using the IAM permissions you explicitly grant, and you can revoke that access at any time. If the additional tag or policy change does not fit your environment, ask your Partner to use an alternate method. View [Tag Management](manual-tagging.md#tag-management) for more information on managing resource tags.

**Identity Tagging:** The partner tags their own IAM role or user — not your workload resources. Identity Tagging does not consume your resource tag quota, does not require tag policy updates, and does not modify any of your AWS resources. The tag resides on the IAM principal the partner operates with in your account. You retain full control over the IAM permissions granted to the partner and can revoke access at any time.

**User Agent String:** No tags are applied to any resources or identities in your account. The partner includes an identifier in their AWS API calls, which is captured in AWS CloudTrail logs for your visibility.

## 7. How long do resource tags stay in my environment?
<a name="customer-tag-duration-faq"></a>

You have complete control over how long tags remain in your environment. Tags remain on resources until either you (or an authorized user) remove them, or the resource itself is terminated. Any user with the appropriate permissions in your account can remove a tag at any time. You are always the decision-maker on which Partner tags can be used on your resources. When a tag is removed, revenue attribution for the Partner's solution stops.

## 8. Does AWS Revenue Measurement give my Partner or AWS new access to my account?
<a name="customer-account-access-faq"></a>

No, AWS Revenue Measurement does not grant AWS or a Partner access to a customer's accounts, resources, or application code.

## 9. Is my usage shared with my Partner? What information is shared?
<a name="customer-usage-shared-faq"></a>

The AWS Revenue Measurement data AWS collects is only shared with your Partner on an aggregated basis. AWS does not share any AWS Revenue Measurement data specific to an individual customer with a Partner.

## 10. In which AWS regions is AWS Revenue Measurement supported?
<a name="customer-regions-faq"></a>

Today, AWS Revenue Measurement is supported only in [commercial regions](partner-faqs.md#supported-regions-faq). AWS is working to expand coverage to sovereign and government cloud regions in the future, and your Partner or AWS account team can keep you informed on timing as it becomes available. If you run workloads in both commercial and government regions, AWS Revenue Measurement can be enabled today for your commercial accounts while you wait for expanded coverage.

## 11. My Partner is using Identity Tagging. Does this give them new access to my account or affect my environment?
<a name="customer-identity-tagging-faq"></a>

No. Identity Tagging does not grant your Partner or AWS any new access to your account, resources, or application code. With Identity Tagging, the partner applies a tag to their own IAM role or user — the identity they already use to operate in your environment with the permissions you have explicitly granted. The tag is attribution metadata only; it does not change IAM authorization, modify your workload resources, or consume your resource tag quota. You retain full control over the IAM permissions granted to the partner and can revoke access at any time. If the partner's IAM principal is deleted or the tag is removed, revenue attribution stops.