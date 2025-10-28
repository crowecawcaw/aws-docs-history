**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Intelligent threat integration and

AWS Managed Rules

This section explains how the intelligent threat integration APIs work with the AWS Managed Rules rule groups.

The intelligent threat integration APIs work with protection packs (web ACLs) that use the intelligent threat
rule groups to enable the full functionality of these advanced managed rule groups.

- AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group `AWSManagedRulesACFPRuleSet`.

Account creation fraud is an online illegal activity in which an attacker
creates invalid accounts in your application for purposes such as receiving
sign-up bonuses or impersonating someone. The ACFP managed rule group provides
rules to block, label, and manage requests that might be part of fraudulent account
creation attempts. The APIs enable fine-tuned client browser verification and
human interactivity information that the ACFP rules use to separate valid client traffic from
malicious traffic.

For more information, see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md") and [AWS WAF Fraud Control account creation fraud prevention (ACFP)](waf-acfp.md "waf-acfp.md").

- AWS WAF Fraud Control account takeover prevention (ATP) managed rule group `AWSManagedRulesATPRuleSet`.

Account takeover is an online illegal activity in which an attacker gains
unauthorized access to a person's account. The ATP managed rule group provides
rules to block, label, and manage requests that might be part of malicious account
takeover attempts. The APIs enable fine-tuned client verification and behavior
aggregation that the ATP rules use to separate valid client traffic from
malicious traffic.

For more information, see [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md "aws-managed-rule-groups-atp.md") and [AWS WAF Fraud Control account takeover prevention (ATP)](waf-atp.md "waf-atp.md").

- Targeted protection level of the AWS WAF Bot Control managed rule group `AWSManagedRulesBotControlRuleSet`.

Bots run from self-identifying and useful ones, such as most search engines and crawlers,
to malicious bots that operate against your website and don't self-identify. The
Bot Control managed rule group provides rules to monitor, label, and manage the bot
activity in your web traffic. When you use the targeted protection level of this
rule group, the targeted rules use the client session information that the APIs
provide to better detect malicious bots.

For more information, see [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md") and [AWS WAF Bot Control](waf-bot-control.md "waf-bot-control.md").
To add one of these managed rule groups to your protection pack (web ACL), see the procedures [Adding the ACFP managed rule group to your web
ACL](waf-acfp-rg-using.md "waf-acfp-rg-using.md"), [Adding the ATP managed rule group to your protection pack (web ACL)](waf-atp-rg-using.md "waf-atp-rg-using.md"), and [Adding the AWS WAF Bot Control managed rule group to your web
ACL](waf-bot-control-rg-using.md "waf-bot-control-rg-using.md").

###### Note

The managed rule groups currently don't block requests that are missing tokens. In order to
block requests that are missing tokens, after you implement your application
integration APIs, follow the guidance at [Blocking requests that don't have a valid
AWS WAF token](waf-tokens-block-missing-tokens.md "waf-tokens-block-missing-tokens.md").
