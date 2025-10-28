**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF Bot Control components

The main components of a Bot Control implementation are the following:

- **`AWSManagedRulesBotControlRuleSet`** – The Bot Control managed rule group whose
  rules detect and handle various categories of bots. This rule group add labels to web requests
  that it detects as bot traffic.

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

The Bot Control managed rule group provides two levels of protection that you
can choose from:

    + **Common** – Detects a variety of
     self-identifying bots, such as web scraping frameworks, search
     engines, and automated browsers. Bot Control protections at this level
     identify common bots using traditional bot detection techniques,
     such as static request data analysis. The rules label traffic from
     these bots and block the ones that they cannot verify.
    + **Targeted** – Includes the
     common-level protections and adds targeted detection for sophisticated bots that
     do not self identify. Targeted protections mitigate bot activity using a combination
     of rate limiting and CAPTCHA and background browser challenges.




    	- **`TGT_`** – Rules that provide targeted protection have names that begin with
    	 `TGT_`. All targeted protections use detection
    	 techniques such as browser interrogation, fingerprinting, and behavior heuristics
    	 to identify bad bot traffic.
    	- **`TGT_ML_`** – Targeted protection rules that use machine learning have names that begin with
    	 `TGT_ML_`. These rules use automated, machine-learning analysis of website traffic statistics to detect anomalous behavior indicative of distributed, coordinated bot activity. AWS WAF analyzes statistics about your website traffic such as timestamps, browser characteristics, and previous URL visited, to improve the Bot Control machine learning model. Machine learning capabilities are enabled by default, but you can disable them in your rule group configuration. When machine learning is disabled, AWS WAF does not evaluate these rules.

For details including information about the rule group's rules, see [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md").

You include this rule group
in your protection pack (web ACL) using a managed rule group reference statement and indicating the
inspection level that you want to use. For the targeted level, you also indicate
whether to enable machine learning. For more information about adding this
managed rule group to your protection pack (web ACL), see [Adding the AWS WAF Bot Control managed rule group to your web
ACL](waf-bot-control-rg-using.md "waf-bot-control-rg-using.md").

- **Bot Control dashboard** – The bot monitoring dashboard for
  your protection pack (web ACL), available through the protection pack (web ACL) Bot Control tab. Use this dashboard to
  monitor your traffic and understand how much of it comes from various types of
  bots. This can be a starting point for customizing your bot management, as
  described in this topic. You can also use it to verify your changes and monitor
  activity for various bots and bot categories.
- **JavaScript and mobile application integration SDKs**
  – You should implement the AWS WAF JavaScript and mobile SDKs if you use
  the targeted protection level of the Bot Control rule group. The targeted rules use
  information provided by the SDKs in the client tokens for enhanced detection
  against malicious bots. For more information about the SDKs, see [Client application
  integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md").
- **Logging and metrics** – You can monitor your bot
  traffic and understand how the Bot Control managed rule group evaluates and handles your traffic by
  studying the data that's collected for your protection pack (web ACL) by AWS WAF logs, Amazon Security Lake, and Amazon CloudWatch.
  The labels that Bot Control adds to your web requests are included in the data.
  For information about these options, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md"),
  [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"), and
  [What is Amazon Security Lake?](../../../security-lake/latest/userguide/what-is-security-lake.md "../../../security-lake/latest/userguide/what-is-security-lake.md").

Depending on your needs and the traffic that you see, you might want to customize your
Bot Control implementation. The following are some of the most commonly used
options.

- **Scope-down statements** – You can exclude some
  traffic from the web requests that the Bot Control managed rule group evaluates by
  adding a scope-down statement inside the Bot Control managed rule group reference
  statement. A scope-down statement can be any nestable rule statement. When a
  request doesn't match the scope-down statement, AWS WAF evaluates it as not
  matching the rule group reference statement without evaluating it against the
  rule group. For more information about scope-down statements, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md").

Your costs for using the Bot Control managed rule group increase with the number of web requests that
AWS WAF evaluates with it. You can help reduce these costs by using a
scope-down statement to limit the requests that the rule group evaluates. For
example, you might want to allow your homepage to load for everyone, including
bots, and then apply the rule group rules to requests that are going to your
application APIs or that contain a particular type of content.

- **Labels and label matching rules** – You can customize
  how the Bot Control rule group handles some of the bot traffic that it identifies
  using the AWS WAF label match rule statement. The Bot Control rule group adds labels to
  your web requests. You can add label matching rules after the Bot Control rule group
  that match on Bot Control labels and apply the handling that you need. For more
  information about labeling and using label match statements, see [Label match rule
  statement](waf-rule-statement-type-label-match.md "waf-rule-statement-type-label-match.md") and [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md").
- **Custom requests and responses** – You can add custom
  headers to requests that you allow and you can send custom responses for requests
  that you block by pairing label matching with the AWS WAF custom request and response
  features. For more information about customizing requests and responses, see [Customized web requests and responses in
  AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md").
