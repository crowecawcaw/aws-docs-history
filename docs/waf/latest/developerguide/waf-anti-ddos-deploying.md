**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Testing and deploying Anti-DDoS

You will want to configure and test AWS WAF Distributed Denial of Service (DDoS) prevention before deploying the feature. This section provides general guidance for configuring and testing, however the specific steps that you choose to follow will depend
on your needs, resources, and web requests that you receive.

This information is in addition to the general information about testing and tuning
provided at [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

AWS Managed Rules are designed to protect you from common web threats. When used in accordance
with the documentation, AWS Managed Rules rule groups add another layer of security for your
applications. However, AWS Managed Rules rule groups aren't intended as a replacement for your security
responsibilities, which are determined by the AWS resources that you select. Refer
to the [Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") to ensure that your resources in AWS are properly
protected.

###### Production traffic risk

Test and tune your anti-DDoS implementation in a staging or testing environment until you are comfortable with the potential impact to your traffic. Then test and tune the rules in count mode with your production traffic before enabling them.

This guidance is intended for users who know generally how to create and manage
AWS WAF protection packs (web ACLs), rules, and rule groups. Those topics are covered in prior sections of this guide.

###### To configure and test an AWS WAF Distributed Denial of Service (DDoS) prevention implementation

Perform these steps first in a test environment, then in production.

1. ###### Add the AWS WAF Distributed Denial of Service (DDoS) prevention managed rule group in count mode

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

Add the AWS Managed Rules rule group `AWSManagedRulesAntiDDoSRuleSet` to a new or existing protection pack (web ACL) and
configure it so that it doesn't alter the current protection pack (web ACL) behavior. For details
about the rules and labels for this rule group, see [AWS WAF Distributed Denial of Service (DDoS) prevention rule group](aws-managed-rule-groups-anti-ddos.md "aws-managed-rule-groups-anti-ddos.md").

    * When you add the managed rule group, edit it and do the following:




    	+ In the **Rule group configuration** pane,
    	 provide the details needed to perform anti-DDoS
    	 activities for your web traffic.
    	 For more information, see [Adding the Anti-DDoS managed rule group to your protection pack (web ACL)](waf-anti-ddos-rg-using.md "waf-anti-ddos-rg-using.md").
    	+ In the **Rules** pane, open the **Override all rule
    	 actions** dropdown and choose
    	 **Count**. With this configuration,
    	 AWS WAF evaluates requests against all of the rules in the
    	 rule group and only counts the matches that result, while still
    	 adding labels to requests. For more information, see [Overriding rule actions in a rule
    	 group](web-acl-rule-group-settings.md#web-acl-rule-group-rule-action-override "web-acl-rule-group-settings.md#web-acl-rule-group-rule-action-override").


    	With this override, you can monitor the potential impact of the Anti-DDoS managed rules
    	 to determine whether you want to make modifications, such as expanding
    	 the regex for the URIs that can't handle a silent browser challenge.
    * Position the rule group so that it's evaluated as early as possible, immediately after any
     rules that allow traffic. Rules are evaluated in ascending numeric priority order. The console
     sets the order for you, starting at the top of your rule list.
     For more information, see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md").

2. ###### Enable logging and metrics for the protection pack (web ACL)

As needed, configure logging, Amazon Security Lake data collection, request sampling, and Amazon CloudWatch metrics for the protection pack (web ACL).
You can use these visibility tools to monitor the interaction of the Anti-DDoS managed
rule group with your traffic.

    * For information about configuring and using logging, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").
    * For information about Amazon Security Lake, see
     [What is Amazon Security Lake?](../../../security-lake/latest/userguide/what-is-security-lake.md "../../../security-lake/latest/userguide/what-is-security-lake.md")
     and [Collecting data from AWS services](../../../security-lake/latest/userguide/internal-sources.md "../../../security-lake/latest/userguide/internal-sources.md")
     in the *Amazon Security Lake user guide*.
    * For information about Amazon CloudWatch metrics, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
    * For information about web request sampling, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").

3. ###### Associate the protection pack (web ACL) with a resource

If the protection pack (web ACL) isn't already associated with a test resource, associate it.

For information, see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md"). 4. ###### Monitor traffic and Anti-DDoS rule matches

Make sure that your normal traffic is flowing and that the Anti-DDoS managed rule group rules
are adding labels to matching web requests. You can see the labels in the logs
and see the Anti-DDoS and label metrics in the Amazon CloudWatch metrics. In the logs, the
rules that you've overridden to count in the rule group show up in the
`ruleGroupList` with `action` set to count, and with
`overriddenAction` indicating the configured rule action that you
overrode. 5. ###### Customize Anti-DDoS web request handling

As needed, add your own rules that explicitly allow or block requests, to
change how Anti-DDoS rules would otherwise handle them.

For example, you can use Anti-DDoS labels to allow or block requests or to customize
request handling. You can add a label match rule after the Anti-DDoS managed rule
group to filter labeled requests for the handling that you want to apply. After
testing, keep the related Anti-DDoS rules in count mode, and maintain the request
handling decisions in your custom rule. 6. ###### Remove test rules and configure Anti-DDoS settings

Review your testing results to determine which Anti-DDoS rules you want to keep in count mode for monitoring only. For any rules you want to run with active protection, disable count mode in the protection pack (web ACL) rule group configuration to allow them to perform their configured actions. Once you've finalized these settings, remove any temporary test label match rules while retaining any custom rules you created for production use. For additional Anti-DDoS configuration considerations, see
[Best practices for intelligent
threat mitigation in AWS WAF](waf-managed-protections-best-practices.md "waf-managed-protections-best-practices.md"). 7. ###### Monitor and tune

To be sure that web requests are being handled as you want, closely monitor
your traffic after you enable the Anti-DDoS functionality that you intend to use.
Adjust the behavior as needed with the rules count override on the rule group
and with your own rules.
