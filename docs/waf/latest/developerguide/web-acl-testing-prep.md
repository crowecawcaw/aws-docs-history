**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Preparing for testing your AWS WAF protections

This section describes how to get set up to test and tune your AWS WAF protections.

###### Note

To follow the guidance in this section, you need to understand generally how to create and
manage AWS WAF protections like protection packs (web ACLs), rules, and rule groups. That information is
covered in earlier sections of this guide.

###### To prepare for testing

1. ###### Enable protection pack (web ACL) logging, Amazon CloudWatch metrics, and web request sampling for the protection pack (web ACL)

Use logging, metrics, and sampling to monitor the interaction of the protection pack (web ACL) rules
with your web traffic.

    * **Logging** – You can configure AWS WAF to log the web
     requests that a protection pack (web ACL) evaluates. You can send logs to CloudWatch logs, an
     Amazon S3 bucket, or an Amazon Data Firehose delivery stream. You can redact fields and apply filtering.
     For more information, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").
    * **Amazon Security Lake** – You can configure Security Lake to collect protection pack (web ACL) data.
     Security Lake collects log and event data from various sources for normalization, analysis, and management.
     For information about this option,
     see [What is Amazon Security Lake?](../../../security-lake/latest/userguide/what-is-security-lake.md "../../../security-lake/latest/userguide/what-is-security-lake.md")
     and [Collecting data from AWS services](../../../security-lake/latest/userguide/internal-sources.md "../../../security-lake/latest/userguide/internal-sources.md")
     in the *Amazon Security Lake user guide*.
    * **Amazon CloudWatch metrics** – In your protection pack (web ACL)
     configuration, provide metric specifications for everything that you
     want to monitor. You can view metrics through the AWS WAF and CloudWatch
     consoles. For more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
    * **Web request sampling** – You can view a sample of
     all web requests that your protection pack (web ACL) evaluates. For information about web
     request sampling, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").

2. ###### Set your protections to Count mode

In your protection pack (web ACL) configuration, switch anything that you want to test to count mode. This
causes the test protections to record matches against web requests without
altering how the requests are handled. You'll be able to see the matches in your
metrics, logs, and sampled requests, to verify the match criteria and to
understand what the effects might be on your web traffic. Rules that add labels to matching
requests will add labels regardless of the rule action.

    * **Rule defined in the protection pack (web ACL)** – Edit the rules in
     the protection pack (web ACL) and set their actions to Count.
    * **Rule group** – In your protection pack (web ACL) configuration, edit
     the rule statement for the rule group and, in the
     **Rules** pane, open the **Override all
     rule actions** dropdown and choose
     **Count**. If you manage the protection pack (web ACL) in
     JSON, add the rules to the `RuleActionOverrides` settings in
     the rule group reference statement, with `ActionToUse` set to
     Count. The following example listing shows overrides for two
     rules in the `AWSManagedRulesAnonymousIpList` AWS Managed Rules rule group.



    ```
      "ManagedRuleGroupStatement": {
        "VendorName": "AWS",
        "Name": "AWSManagedRulesAnonymousIpList",
          "RuleActionOverrides": [
            {
              "ActionToUse": {
                "Count": {}
              },
              "Name": "AnonymousIPList"
            },
            {
              "ActionToUse": {
                "Count": {}
              },
              "Name": "HostingProviderIPList"
            }
          ],
          "ExcludedRules": []
        }
      },
    ```

    For more information about rule action overrides, see [Overriding rule actions in a rule
     group](web-acl-rule-group-settings.md#web-acl-rule-group-rule-action-override "web-acl-rule-group-settings.md#web-acl-rule-group-rule-action-override").


    For your own rule group, don't modify the rule actions in the rule group itself. Rule
     group rules with Count action don't generate the metrics or
     other artifacts that you need for your testing. In addition, changing a
     rule group affects all protection packs (web ACLs) that use it, while the changes inside
     the protection pack (web ACL) configuration only affect the single protection pack (web ACL).
    * **protection pack (web ACL)** – If you're testing a new protection pack (web ACL), set the
     default action for the protection pack (web ACL) to allow requests. This lets you try out the web
     ACL without affecting traffic in any way.

In general, count mode generates more matches than production. This is because a rule that
counts requests doesn't stop the evaluation of the request by the protection pack (web ACL), so
rules that run later in the protection pack (web ACL) might also match the request. When you
change your rule actions to their production settings, rules that allow or block
requests will terminate the evaluation of requests that they match. As a result,
matching requests will generally be inspected by fewer rules in the protection pack (web ACL). For
more information about the effects of rule actions on the overall evaluation of
a web request, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

With these settings, your new protections won't alter web traffic, but will generate match
information in metrics, protection pack (web ACL) logs, and request samples. 3. ###### Associate the protection pack (web ACL) with a resource

If the protection pack (web ACL) isn't already associated with the resource, associate it.

See [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md").
You're now ready to monitor and tune your protection pack (web ACL).
