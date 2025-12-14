# Fraud detection

| ADVSEC05: How do you detect and block fraud in your advertisement solution? |
| --------------------------------------------------------------------------- |
|                                                                             |

Traffic fraud in digital advertising could impact the
advertising solution by affecting ad spend through fake clicks,
bot traffic, and manipulation schemes. Workloads benefit from
resilient and secure systems that implement defense in depth
strategies for fraud prevention. Effective protection assists
advertisers optimize budgets by focusing on genuine traffic and
properly represented inventory, while publishers can maintain
reputation and revenue by addressing fraudulent activities on
their solution.

Consider using AWS WAF to evaluate traffic to your advertising
solution and filter out suspicious or un-wanted bot traffic
through customizable rules. Amazon GuardDuty can also be
utilized to help protect your AWS accounts, workloads, and data
from threats.

###### Best practices

- [ADVSEC05-BP01 Validate and sanitize content before running a campaign](advsec05-bp01.md "advsec05-bp01.md")
- [Key AWS services](#key-aws-services-7 "#key-aws-services-7")
- [Resources](#resources-12 "#resources-12")

## Key AWS services

- AWS WAF
- Amazon GuardDuty
- Amazon Fraud Detector

## Resources

- [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/")
- [AWS WAF rules](../../../waf/latest/developerguide/waf-rules.md "../../../waf/latest/developerguide/waf-rules.md")
- [Amazon Fraud Detector FAQs](https://aws.amazon.com/fraud-detector/faqs/#topic-0 "https://aws.amazon.com/fraud-detector/faqs/#topic-0")
