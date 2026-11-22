

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Turning on Targeted bot control in the console

This section explains how to turn on the targeted protection level of Bot Control with a single setting in the console.

The **Targeted bot control** setting in the AWS WAF console configures the Bot Control managed rule group at the targeted protection level for you. The setting is available for protection packs (web ACLs) with the CloudFront scope. For regional protection packs (web ACLs), add the rule group yourself and override the actions of the confidence level rules. For more information about adding the rule group, see [Adding the AWS WAF Bot Control managed rule group to your web ACL](waf-bot-control-rg-using.md). The setting uses the recommended configuration. You choose the action for each bot confidence level, or keep the defaults, and AWS WAF configures the rest. You don't need to know which labels the rule group adds or write label match rules. For information about the confidence levels, see [Bot confidence levels](aws-managed-rule-groups-bot-confidence.md). 

When you turn on **Targeted bot control**, AWS WAF configures the following in your protection pack (web ACL): 
+ **Targeted protection level** – AWS WAF adds the Bot Control managed rule group to your protection pack (web ACL) if it isn't there yet. It sets the inspection level to **Targeted** and turns on machine learning. If the rule group is already in your protection pack (web ACL) at the common level, AWS WAF changes it to the targeted level. 
+ **Action for each bot confidence level** – AWS WAF sets the action for the High, Medium, and Low bot confidence levels by overriding the actions of the confidence level rules, which use Count by default. The default actions in the console are the recommended ones: CAPTCHA for High, CAPTCHA for Medium, and Challenge for Low. You can change any of them to Allow, Block, CAPTCHA, Challenge, Count, or Monetize. For more information about the Monetize action, see [AI traffic monetization with CloudFront](cloudfront-features.md#cloudfront-features-ai-traffic-monetization). 
+ **Rule group version** – AWS WAF sets the rule group version to `LATEST`, which always points to the newest version of the Bot Control rule group. You get new detections as AWS releases them, without upgrading manually. For more information about the `LATEST` version, see [LATEST version for the Bot Control managed rule group](waf-managed-rule-groups-versioning-latest.md). 
+ **Rule order** – If the Bot Control rule group isn't in your protection pack (web ACL) yet, AWS WAF adds it after your existing rules, so that your other protections evaluate each request first. Requests that your other rules block don't reach the Bot Control rule group, which keeps your bot inspection costs down. 
+ **Automatic SDK integration** – You can have CloudFront add the AWS WAF JavaScript SDK script tag to the HTML pages that your distributions serve, so that the targeted detections receive browser signals without changes to your application code. For more information about automatic SDK integration, see [Automatic SDK integration for CloudFront distributions](waf-challenge-javascript-sdk-injection.md). 

**Important**  
**Targeted bot control** uses the `LATEST` version of the Bot Control rule group. If you later change the rule group to a different version, **Targeted bot control** turns off in the console. The rule group stays in your protection pack (web ACL) and keeps evaluating traffic with the version that you chose, but the console no longer manages the confidence level actions for you. 

**Note**  
You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

**Targeted bot control** isn't available for protection packs (web ACLs) that are associated with CloudFront distributions on a CloudFront flat-rate pricing plan, because those plans don't include the targeted protection level of Bot Control. For more information about flat-rate pricing plans, see [Using AWS WAF with CloudFront Flat-Rate Pricing Plans](cloudfront-features.md#waf-cf-pricing-plans). 

**To turn on Targeted bot control when you create a protection pack (web ACL)**

1. Start creating a protection pack (web ACL) with the CloudFront scope, as described in [Creating a protection pack (web ACL) in AWS WAF](web-acl-creating.md). 

1. Under **Choose initial protections**, select **Recommended** or **Essentials**. The **Targeted bot control** section isn't available when you select **You build it**. 

1. In the **Targeted bot control** section, select **Enable Targeted bot control**. 

1. Review the action for each confidence level, and change any that you want. To observe how the confidence levels classify your traffic before you enforce them, select **Set all actions to Count**. 

1. Review the **Automatic SDK integration** setting. It's turned on by default for new protection packs (web ACLs). Turn it off if you integrate the SDK yourself. 

1. Finish creating the protection pack (web ACL). 

**To turn on Targeted bot control for an existing protection pack (web ACL)**

Use this procedure to move an existing protection pack (web ACL) to the targeted protection level with the recommended settings. It works whether your protection pack (web ACL) doesn't have the Bot Control rule group yet, has it at the common level, or has it at an older version. 

1. Sign in to the AWS Management Console and open the AWS WAF console at [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2). 

1. In the navigation pane, choose **Protection packs (web ACLs)**, and then select a protection pack (web ACL) with the CloudFront scope. 

1. In the panel for the protection pack (web ACL), choose **Configure Targeted bot control**. 

1. Select **Enable Targeted bot control**, and then review the summary of the changes to your protection pack (web ACL). For example, the summary might say that the inspection level changes from common to targeted, or that the rule group version changes to `LATEST`. 

1. Under **Confidence level actions**, review the action for each confidence level. To observe how the confidence levels classify your traffic before you enforce them, select **Set all actions to Count**. 

1. Review the **Automatic SDK integration** setting. It's turned off by default for existing protection packs (web ACLs). Turn it on to have CloudFront add the SDK script tag to your pages. 

1. Choose **Save**. If the change moves the Bot Control rule group to `LATEST` from another version, review the current and new versions in the confirmation dialog, and then confirm. 

**Reviewing your bot confidence level results**  
The **Configure Targeted bot control** page shows how your traffic is distributed across the bot confidence levels, along with summary statistics such as the number of High confidence requests mitigated and the number of challenges issued. For deeper analysis, follow the link on the page to the protection pack (web ACL) dashboards. The confidence level labels are also available as Amazon CloudWatch metrics and in your AWS WAF logs. For more information about labels and logging, see [Web request labeling in AWS WAF](waf-labels.md) and [Logging AWS WAF protection pack (web ACL) traffic](logging.md). 

After you turn on **Targeted bot control**, you can still customize the Bot Control rule group like any other managed rule group, for example by adding a scope-down statement to exclude traffic that you trust. For more information about configuring the rule group, see [Adding the AWS WAF Bot Control managed rule group to your web ACL](waf-bot-control-rg-using.md) and [Choosing and configuring Bot Control for your use case](waf-bot-control-use-cases.md). 