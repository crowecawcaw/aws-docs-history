**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Adding the AWS WAF Bot Control managed rule group to your web

ACL

This section explains how to add and configure the `AWSManagedRulesBotControlRuleSet` rule group.

The Bot Control managed rule group `AWSManagedRulesBotControlRuleSet` requires additional configuration to identify the protection level that you want to implement.

For the rule group description and rules listing, see [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md").

This guidance is intended for users who know generally how to create and manage
AWS WAF protection packs (web ACLs), rules, and rule groups. Those topics are covered in prior sections
of this guide. For basic information about how to add a managed rule group to your protection pack (web ACL), see [Adding a managed rule group to a protection pack (web ACL) through
the console](waf-using-managed-rule-group.md "waf-using-managed-rule-group.md").

###### Follow best practices

Use the Bot Control rule group in accordance with the best practices at [Best practices for intelligent
threat mitigation in AWS WAF](waf-managed-protections-best-practices.md "waf-managed-protections-best-practices.md").

###### To use the `AWSManagedRulesBotControlRuleSet` rule group in your protection pack (web ACL)

1. Add the AWS managed rule group, `AWSManagedRulesBotControlRuleSet` to your protection pack (web ACL). For the full rule group
   description, see [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md").

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

When you add the rule group, edit it to open the configuration page for the rule
group. 2. On the rule group's configuration page, in the **Inspection level** pane,
select the inspection level that you want to use.

    * **Common** – Detects a variety of
     self-identifying bots, such as web scraping frameworks, search
     engines, and automated browsers. Bot Control protections at this level
     identify common bots using traditional bot detection techniques,
     such as static request data analysis. The rules label traffic from
     these bots and block the ones that they cannot verify.
    * **Targeted** – Includes the
     common-level protections and adds targeted detection for sophisticated bots that
     do not self identify. Targeted protections mitigate bot activity using a combination
     of rate limiting and CAPTCHA and background browser challenges.




    	+ **`TGT_`** – Rules that provide targeted protection have names that begin with
    	 `TGT_`. All targeted protections use detection
    	 techniques such as browser interrogation, fingerprinting, and behavior heuristics
    	 to identify bad bot traffic.
    	+ **`TGT_ML_`** – Targeted protection rules that use machine learning have names that begin with
    	 `TGT_ML_`. These rules use automated, machine-learning analysis of website traffic statistics to detect anomalous behavior indicative of distributed, coordinated bot activity. AWS WAF analyzes statistics about your website traffic such as timestamps, browser characteristics, and previous URL visited, to improve the Bot Control machine learning model. Machine learning capabilities are enabled by default, but you can disable them in your rule group configuration. When machine learning is disabled, AWS WAF does not evaluate these rules.

3. If you're using the targeted protection level and you don't want AWS WAF to use machine learning
   (ML) to analyze web traffic for distributed, coordinated bot activity,
   disable the machine learning option. Machine learning is required for the Bot Control
   rules whose names start with `TGT_ML_`. For
   details about these rules, see [Bot Control rules listing](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules").
4. Add a scope-down statement for the rule group, to contain the costs of using
   it. A scope-down statement narrows the set of requests that the rule group
   inspects. For example use cases, start with [Bot Control example: Using Bot Control only for the
   login page](waf-bot-control-example-scope-down-login.md "waf-bot-control-example-scope-down-login.md") and [Bot Control example: Using Bot Control only for dynamic content](waf-bot-control-example-scope-down-dynamic-content.md "waf-bot-control-example-scope-down-dynamic-content.md").
5. Provide any additional configuration that you need for the rule group.
6. Save your changes to the protection pack (web ACL).
   Before you deploy your Bot Control implementation for production traffic, test and tune it
   in a staging or testing environment until you are comfortable with the potential impact
   to your traffic. Then test and tune the rules in count mode with your production traffic
   before enabling them. See the sections that follow for guidance.
