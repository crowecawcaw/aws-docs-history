# Customer FAQ

## 1. What is Partner Revenue Measurement?

Partner Revenue Measurement is a set of AWS capabilities that enables AWS and its Partners to measure the AWS service consumption Partners drive through their solutions or services engagements across applicable accounts. It gives Partners and AWS a clear, data-driven view of Partner impact so AWS can better support Partners as they deliver value to our mutual customers.

## 2. Why is my Partner asking to implement Partner Revenue Measurement?

Partner Revenue Measurement allows AWS to recognize Partners who are driving customer success. To accurately measure the value these Partners are driving, Partner Revenue Measurement will attribute your AWS consumption to Partner engagement. This connection enables AWS to enhance the tools and programs that support our partners and our mutual customers.

## 3. What are the customer benefits of Partner Revenue Measurement?

With Partner Revenue Measurement, customers can map costs to specific Partner products and solutions, better manage their overall portfolio spending, and make more informed decisions about how to allocate resources. Additionally, Partner Revenue Measurement provides operational visibility through AWS CloudTrail logs, giving customers an audit trail of partner solution activity for compliance and operational efficiency.

## 4. What impact does Partner Revenue Measurement have on my AWS environment?

Partner Revenue Measurement has no impact on your infrastructure, security posture, and billing structure. Partner Revenue Measurement only enables AWS to recognize and measure the Partner's influence on that environment. Partner Revenue Measurement works by associating a Partner's contributions with existing AWS resource usage through lightweight mechanisms such as [resource tagging](resource-tagging.md "resource-tagging.md") or [user agent strings](user-agent-string.md "user-agent-string.md"). There is no additional software to install, no performance overhead, and no changes to how workloads run. With this information, AWS can better support both our Partners and our mutual customers.

## 5. What specific data does AWS collect?

Partner Revenue Measurement uses a tag or identifier--a simple label associated with your Partner's product--to correlate existing billing and usage information that AWS already maintains as part of its standard service operations. A customer's Partner does not receive their raw billing data; AWS provides them only with aggregated, attributed revenue metrics across all customers so a Partner can understand how their product drives AWS service consumption. AWS will collect an AWS Marketplace product code and resource tag, AWS Resource Name (ARN), API operation, ARN usage spend, Service Type, API operation or tag creation date and time, and the AWS Account ID hosting the AWS resource.

## 6. If I allow my Partner to implement Partner Revenue Measurement via resource tagging, how does Partner Revenue Measurement impact my tagging strategy?

By allowing your Partner to implement Partner Revenue Measurement via resource tagging, a single tag is attributed to relevant resources. This consumes one of your fifty available user-defined tag slots. If you enforce tag policies through AWS Organizations, you will need a one-time update to allow for the tag key. You remain in full control: The Partner can only apply tags using the IAM permissions you explicitly grant, and you can revoke that access at any time. If the additional tag or policy change does not fit your environment, ask your Partner to use an alternate Partner Revenue Measurement method such as the [user agent string](user-agent-string.md "user-agent-string.md"), which requires no tags in your account. View [this guide](manual-tagging.md#tag-management "manual-tagging.md#tag-management") for more information on managing resource tags.

## 7. How long do resource tags stay in my environment?

You have complete control over how long tags remain in your environment. Tags remain on resources until either you (or an authorized user) remove them, or the resource itself is terminated. Any user with the appropriate permissions in your account can remove a tag at any time. You are always the decision-maker on which Partner tags can be used on your resources. When a tag is removed, revenue attribution for the Partner's solution stops.

## 8. Does Partner Revenue Measurement give my Partner or AWS new access to my account?

No, Partner Revenue Measurement does not grant AWS or a Partner access to a customer's accounts, resources, or application code.

## 9. Is my usage shared with my Partner? What information is shared?

The Partner Revenue Measurement data AWS collects is only shared with your Partner on an aggregated basis. AWS does not share any Partner Revenue Measurement data specific to an individual customer with a Partner.

## 10. In which AWS regions is Partner Revenue Measurement supported?

Today, Partner Revenue Measurement is supported only in [commercial regions](partner-faqs.md#supported-regions-faq "partner-faqs.md#supported-regions-faq"). AWS is working to expand coverage to sovereign and government cloud regions in the future, and your Partner or AWS account team can keep you informed on timing as it becomes available. If you run workloads in both commercial and government regions, Partner Revenue Measurement can be enabled today for your commercial accounts while you wait for expanded coverage.
