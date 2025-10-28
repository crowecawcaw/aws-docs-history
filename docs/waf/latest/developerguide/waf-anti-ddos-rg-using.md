**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Adding the Anti-DDoS managed rule group to your protection pack (web ACL)

This section explains how to add and configure the `AWSManagedRulesAntiDDoSRuleSet` rule group.

To configure the Anti-DDoS managed rule group, you provide settings that include
how sensitive the rule group is to DDoS attacks and the actions that it takes
on requests that are or might be participating in the attacks.
This configuration is in addition to the
normal configuration for a managed rule group.

For the rule group description and rules and labels listing, see [AWS WAF Distributed Denial of Service (DDoS) prevention rule group](aws-managed-rule-groups-anti-ddos.md "aws-managed-rule-groups-anti-ddos.md").

This guidance is intended for users who know generally how to create and manage
AWS WAF protection packs (web ACLs), rules, and rule groups. Those topics are covered in prior sections
of this guide. For basic information about how to add a managed rule group to your protection pack (web ACL), see [Adding a managed rule group to a protection pack (web ACL) through
the console](waf-using-managed-rule-group.md "waf-using-managed-rule-group.md").

###### Follow best practices

Use the Anti-DDoS rule group in accordance with the best practices at [Best practices for intelligent
threat mitigation in AWS WAF](waf-managed-protections-best-practices.md "waf-managed-protections-best-practices.md").

###### To use the `AWSManagedRulesAntiDDoSRuleSet` rule group in your protection pack (web ACL)

1. Add the AWS managed rule group, `AWSManagedRulesAntiDDoSRuleSet` to your protection pack (web ACL), and
   **Edit** the rule group settings before saving.

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/"). 2. In the **Rule group configuration** pane, provide any custom
configuration for the `AWSManagedRulesAntiDDoSRuleSet` rule group.

    1. For **Block sensitivity level**, specify how sensitive you
     want the rule `DDoSRequests` to be when matching on the rule group's DDoS suspicion labeling.
     The higher the sensitivity, the lower the levels of labeling that the rule matches:




    	* Low sensitivity is less sensitive, causing the rule to match only on the most obvious participants in an attack, which have the high suspicion label `awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request`.
    	* Medium sensitivity causes the rule to match on the medium and high suspicion labels.
    	* High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.
    This rule provides the most severe handling of web requests that are suspected of participating in
     DDoS attacks.
    2. For **Enable challenge**, choose whether to enable the
     rules `ChallengeDDoSRequests` and `ChallengeAllDuringEvent`,
     which by default apply the Challenge action to matching requests.


    These rules provide request handling that's intended to permit legitimate users to proceed with
     their requests while blocking participants in the DDoS attack. You can override their action
     settings to Allow or Count or you can disable their use entirely.


    If you enable these rules, then provide any additional configuration that you want:




    	* For **Challenge sensitivity level**,
    	 specify how sensitive you want the rule `ChallengeDDoSRequests` to be.


    	The higher the sensitivity, the lower the levels of labeling that the rule matches:




    		+ Low sensitivity is less sensitive, causing the rule to match only on the most obvious participants in an attack, which have the high suspicion label `awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request`.
    		+ Medium sensitivity causes the rule to match on the medium and high suspicion labels.
    		+ High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.
    	* For **Exempt URI regular expressions**, provide a regular expression
    	 that matches against URIs for web requests that can't handle a silent browser challenge. The Challenge action will effectively block requests from URIs that are missing the challenge token unless they can handle the silent browser challenge.


    	The Challenge action
    	 can only be handled properly by a client that's expecting HTML content. For more
    	 information about how the action works, see [CAPTCHA and Challenge action behavior](waf-captcha-and-challenge-actions.md "waf-captcha-and-challenge-actions.md").


    	Review the default regular expression and update it as needed. The rules
    	 use the specified regular expression to identify
    	 request URIs that can't handle the Challenge action and prevent the rules
    	 from sending a challenge back. Requests that you exclude in this way can only be blocked
    	 by the rule group with the rule `DDoSRequests`.


    	The default expression that's provided in the console covers most use cases,
    	 but you should review and adapt it for your application.


    	AWS WAF supports the pattern syntax used by the PCRE library `libpcre` with some exceptions. The library is documented at [PCRE - Perl Compatible Regular Expressions](http://www.pcre.org/ "http://www.pcre.org/"). For information about AWS WAF support, see [Supported regular expression syntax in AWS WAF](waf-regex-pattern-support.md "waf-regex-pattern-support.md").

3. Provide any additional configuration that you want for the rule group and save the rule.

###### Note

AWS recommends against using a scope-down statement with this managed rule group.
The scope-down statement limits the requests that the rule group observes, and so can result
in an inaccurate traffic baseline and diminished DDoS event detection.
The scope-down statement option is available for all of the managed rule group statements, but
should not be used for this one. For information
about scope-down statements, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md"). 4. In the **Set rule priority** page, move the new anti-DDoS managed rule group rule up so that it runs
only after any Allow action rules that you have and before any other rules.
This gives the rule group the ability to track the most traffic for Anti-DDoS protection. 5. Save your changes to the protection pack (web ACL).
Before you deploy your anti-DDoS implementation for production traffic, test and tune it in
a staging or testing environment until you are comfortable with the potential impact to
your traffic. Then test and tune the rules in count mode with your production traffic
before enabling them. See the section that follows for guidance.
