# View AWS Trusted Advisor checks powered by AWS Config

###### Important

End of Support Notice: Developer Support will be discontinued January 1, 2027. Customers with Developer Support can continue using their existing plan or choose to upgrade to Business Support+ anytime before January 1, 2027. Business Support+ delivers AI-powered assistance that understands the context of your operations, with 24/7 access to AWS experts at $29/month minimum per account. For more information, see [Business Support+ plan details](https://aws.amazon.com/premiumsupport/plans/business-plus/ "https://aws.amazon.com/premiumsupport/plans/business-plus/")

End of Support Notice: Business Support will be discontinued January 1, 2027. Customers with Business Support can continue using their existing plan or choose to upgrade to Business Support+ anytime before January 1, 2027. Business Support+ delivers AI-powered assistance that understands the context of your operations, with 24/7 access to AWS experts at $29/month minimum per account. For more information see, [Business Support+ plan details](https://aws.amazon.com/premiumsupport/plans/business-plus/ "https://aws.amazon.com/premiumsupport/plans/business-plus/")

End of Support Notice: On January 1, 2027, AWS will discontinue Enterprise On-Ramp. Throughout 2026, Enterprise On-Ramp customers will be automatically upgraded to AWS Enterprise Support during contract renewal or in periodic batches. Customers will receive an email notification a month before their upgrade. No further action is required. Enterprise Support provides designated TAM assignment, 15-minute response times, and AWS Security Incident Response available at no additional cost, all at a lower $5,000 minimum (reduced from $15,000). For more information, see [AWS Enterprise Support plan details](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/").

For more information, see [Developer, Business, and Enterprise On-Ramp end of support](support-plans-eos.md "support-plans-eos.md").

Developer Support, Business Support, and Enterprise On-Ramp will remain available in the AWS GovCloud (US) Region.

AWS Config is a service that continually assesses, audits, and evaluates your resource configurations for your desired settings. AWS Config provides managed rules, which are predefined, customizable compliance checks that AWS Config uses to evaluate if your AWS resources comply with common best practices.

The AWS Config console guides you through the configuration and activation of managed rules. You can also use the AWS Command Line Interface (AWS CLI) or AWS Config API to pass the JSON code that defines your configuration of a managed rule. You can customize the behavior of a managed rule to suit your needs. You can customize the rule's parameters to define attributes that your resources must have to comply with the rule. To learn more about enabling AWS Config, see the [AWS Config Developer Guide](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md").

AWS Config managed rules power a set of Trusted Advisor checks across all categories. When you enable certain managed rules, the corresponding Trusted Advisor checks are automatically enabled. To see which Trusted Advisor checks are powered by specific AWS Config managed rules, see [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md "trusted-advisor-check-reference.md").

The AWS Config powered checks are available to customers with an AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan. If you enable AWS Config and you have one of these AWS Support plans, then you automatically see recommendations powered by corresponding deployed AWS Config managed rules.

###### Note

Results for these checks are automatically refreshed based on change-triggered updates to AWS Config managed rules. Refresh requests are not allowed. Currently, you can’t exclude resources from these checks.

## Troubleshooting

If you have issues with this integration, see the following troubleshooting
information.

###### Contents

- [I just enabled recording and managed rules for AWS Config, but I don’t see corresponding Trusted Advisor checks.](aws-config-integration-with-ta.md#ta-checks-not-appearing "aws-config-integration-with-ta.md#ta-checks-not-appearing")
- [I deployed the same AWS Config managed rule twice, what will I see in Trusted Advisor?](aws-config-integration-with-ta.md#config-managed-rule-deployed-twice "aws-config-integration-with-ta.md#config-managed-rule-deployed-twice")
- [I turned off recording for AWS Config in an AWS Region. What will I see in Trusted Advisor?](aws-config-integration-with-ta.md#turned-off-config-recording "aws-config-integration-with-ta.md#turned-off-config-recording")

### I just enabled recording and managed rules for AWS Config, but I don’t see corresponding Trusted Advisor checks.

After the AWS Config rule generates evalution results, you see the results in Trusted Advisor in near real-time. If you have issues with this feature, create a technical support case in the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

### I deployed the same AWS Config managed rule twice, what will I see in Trusted Advisor?

You see separate entries in the Trusted Advisor check results for each managed rule that you install.

### I turned off recording for AWS Config in an AWS Region. What will I see in Trusted Advisor?

If you turned off resource recording for AWS Config in an AWS Region, then Trusted Advisor no longer receives data for corresponding managed rules and checks in that Region. Existing managed rule results remain in AWS Config and in Trusted Advisor until AWS Config expires, based on the recorder retention policy. If you delete a managed rule, then the Trusted Advisor check data usually deletes in near real-time.
