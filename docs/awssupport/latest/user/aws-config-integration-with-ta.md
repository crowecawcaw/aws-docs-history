# View AWS Trusted Advisor checks powered by AWS Config

AWS Config is a service that continually assesses, audits, and evaluates your resource configurations for your desired settings. AWS Config provides managed rules, which are predefined, customizable compliance checks that AWS Config uses to evaluate if your AWS resources comply with common best practices.

The AWS Config console guides you through the configuration and activation of managed rules. You can also use the AWS Command Line Interface (AWS CLI) or AWS Config API to pass the JSON code that defines your configuration of a managed rule. You can customize the behavior of a managed rule to suit your needs. You can customize the rule's parameters to define attributes that your resources must have to comply with the rule. To learn more about enabling AWS Config, see the [AWS Config Developer Guide](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md").

AWS Config managed rules power a set of Trusted Advisor checks across all categories. When you enable certain managed rules, the corresponding Trusted Advisor checks are automatically enabled. To see which Trusted Advisor checks are powered by specific AWS Config managed rules, see [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md "trusted-advisor-check-reference.md").

The AWS Config powered checks are available to customers with [AWS Business Support](https://aws.amazon.com/premiumsupport/plans/business/ "https://aws.amazon.com/premiumsupport/plans/business/"), [AWS Enterprise On-Ramp](https://aws.amazon.com/premiumsupport/plans/enterprise-onramp/ "https://aws.amazon.com/premiumsupport/plans/enterprise-onramp/"), and [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/") plans. If you enable AWS Config and you have one of these AWS Support plans, then you automatically see recommendations powered by corresponding deployed AWS Config managed rules.

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
