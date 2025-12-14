**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Editing a protection pack (web ACL) in AWS WAF

Using the new console
This section provides procedures for editing protection packs (web ACLs) through
the AWS console.

To add or remove rules from a protection pack (web ACL) or change configuration
settings, access the protection pack (web ACL) using the procedure on this page.
While updating a protection pack (web ACL), AWS WAF provides continuous coverage to
the resources that you have associated with the protection pack (web ACL).

###### Production traffic risk

Before you deploy changes in your protection pack (web ACL) for production
traffic, test and tune them in a staging or testing environment until
you are comfortable with the potential impact to your traffic. Then test
and tune your updated rules in count mode with your production traffic
before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Using more than 1,500 WCUs in a protection pack (web ACL) incurs costs beyond the basic protection pack (web ACL) price. For more information, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### To edit a protection pack (web ACL)

1. Sign in to the new AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2-pro](https://console.aws.amazon.com/wafv2-pro "https://console.aws.amazon.com/wafv2-pro").
2. In the navigation pane, choose **Resources &
   protection packs (web ACLs)**.
3. Choose the protection pack (web ACL) that you want to edit. The console
   makes the main protection pack (web ACL) card editable, and also opens a
   side pane with details you can edit.
4. Edit the protection pack (web ACL) as needed.

The following lists the editable protection pack (web ACL) configuration
components.

This section provides procedures for editing web ACLs through
the AWS console.

To add or remove rules from a web ACL or change configuration settings, access the web ACL
using the procedure on this page. While updating a web ACL, AWS WAF provides
continuous coverage to the resources that you have associated with the web ACL.

###### Production traffic risk

Before you deploy changes in your web ACL for production traffic, test and tune them in a
staging or testing environment until you are comfortable with the potential
impact to your traffic. Then test and tune your updated rules in count mode with your
production traffic before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Using more than 1,500 WCUs in a protection pack (web ACL) incurs costs beyond the basic protection pack (web ACL) price. For more information, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### Temporary inconsistencies during updates

When you create or change a protection pack (web ACL) or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:

- After you create a protection pack (web ACL), if you try to associate it with a resource, you might get an exception indicating that the protection pack (web ACL) is unavailable.
- After you add a rule group to a protection pack (web ACL), the new rule group rules might be in effect in one area where the protection pack (web ACL) is used and not in another.
- After you change a rule action setting, you might see the old action in some places and the new action in others.
- After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.

Using the standard console
This section provides procedures for editing web ACLs through the AWS
console.

To add or remove rules from a web ACL or change configuration settings,
access the web ACL using the procedure on this page. While updating a
web ACL, AWS WAF provides continuous coverage to the resources that you have
associated with the web ACL.

###### Production traffic risk

Before you deploy changes in your web ACL for production traffic,
test and tune them in a staging or testing environment until you are
comfortable with the potential impact to your traffic. Then test and
tune your updated rules in count mode with your production traffic
before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Using more than 1,500 WCUs in a protection pack (web ACL) incurs costs beyond the basic protection pack (web ACL) price. For more information, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### To edit a web ACL

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose
   **web ACLs**.
3. Choose the name of the web ACL that you want to edit. The console
   takes you to the web ACL's description.
4. Edit the web ACL as needed. Select the tabs for the configuration
   areas that you're interested in and edit the mutable settings. For
   each setting that you edit, when you choose
   **Save** and return to the web ACL's
   description page, the console saves your changes to the web ACL.

The following lists the tabs that contain web ACL configuration
components.

    * **Rules** tab




    	+ **Rules defined in the
    	 web ACL** – You can edit and
    	 manage the rules that you have defined in the
    	 web ACL, similar to how you did during web ACL
    	 creation.


    	###### Note

    	Don't change the names of any rules that you
    	 didn't add by hand to your web ACL. If you are
    	 using other services to manage rules for you,
    	 changing their names could remove or lessen their
    	 ability to provide the intended protections.
    	 AWS Shield Advanced and AWS Firewall Manager both can create rules
    	 in your web ACL. For information, see [Recognizing rule groups provided by other services](waf-service-owned-rule-groups.md "waf-service-owned-rule-groups.md").


    	###### Note

    	If you change the name of a rule and you want the rule's metric name to reflect the change, you
    	 must update the metric name as well. AWS WAF doesn't automatically update the metric name for a rule when you change the rule name.
    	 You can change the metric name when you edit the
    	 rule in the console, by using the rule JSON editor. You can also change both names through the APIs and in any JSON listing that you
    	 use to define your protection pack (web ACL) or rule group.


    	For information about rules and rule group
    	 settings, see [AWS WAF rules](waf-rules.md "waf-rules.md") and [AWS WAF rule groups](waf-rule-groups.md "waf-rule-groups.md").
    	+ **web ACL rule capacity units
    	 used** – The current capacity
    	 usage for your web ACL. This is view only.
    	+ **Default web ACL action for
    	 requests that don't match any
    	 rules**– For information about this
    	 setting, see [Setting the protection pack (web ACL) default action in AWS WAF](web-acl-default-action.md "web-acl-default-action.md").
    	+ **web ACL CAPTCHA and
    	 challenge configurations** – These
    	 immunity times determine how long a CAPTCHA or
    	 challenge token remains valid after it's acquired.
    	 You can only modify this setting here, after you
    	 create the web ACL. For information about these
    	 settings, see [Setting timestamp expiration and token immunity times in AWS WAF](waf-tokens-immunity-times.md "waf-tokens-immunity-times.md").
    	+ **Token domain list**
    	 – AWS WAF accepts tokens for all domains in the
    	 list and for the domain of the associated resource.
    	 For more information, see [AWS WAF protection pack (web ACL) token domain list configuration](waf-tokens-domains.md#waf-tokens-domain-lists "waf-tokens-domains.md#waf-tokens-domain-lists").
    * **Associated AWS resources** tab




    	+ **Web request inspection size
    	 limit** – Included only for
    	 web ACLs that protect CloudFront distributions. The body
    	 inspection size limit determines how much of the
    	 body component is forwarded to AWS WAF for inspection.
    	 For more information about this setting, see [Considerations for managing body inspection in AWS WAF](web-acl-setting-body-inspection-limit.md "web-acl-setting-body-inspection-limit.md").
    	+ **Associated AWS
    	 resources** – The list of
    	 resources that the web ACL is currently associated
    	 with and protecting. You can locate resources that
    	 are within the same Region as the web ACL and
    	 associate them to the web ACL. For more information,
    	 see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md").
    * **Custom response bodies** tab




    	+ Custom response bodies that are available for use
    	 by your web ACL rules that have the action set to
    	 Block. For more information, see [Sending custom responses for Block
    	 actions](customizing-the-response-for-blocked-requests.md "customizing-the-response-for-blocked-requests.md").
    * **Logging and metrics** tab




    	+ **Logging** –
    	 Logging for the traffic that the web ACL evaluates.
    	 For information, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").
    	+ **Security Lake
    	 integration** – The status of any
    	 data collection that you've configured for the
    	 web ACL in Amazon Security Lake. For information, see [Collecting data from AWS services](../../../security-lake/latest/userguide/internal-sources.md "../../../security-lake/latest/userguide/internal-sources.md") in
    	 the *Amazon Security Lake user guide*.
    	+ **Sampled requests**
    	 – Information about the rules that match web
    	 requests. For information about viewing sampled
    	 requests, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").
    	+ **Data protection
    	 settings** – You can configure web
    	 traffic data redaction and filtering for all data
    	 that's available for the web ACL and for just the
    	 data that the AWS WAF sends to the configured web ACL
    	 logging destination. For information about data
    	 protection, see [Data protection and logging for AWS WAF protection pack (web ACL) traffic](waf-data-protection-and-logging.md "waf-data-protection-and-logging.md").
    	+ **CloudWatch metrics**
    	 – Metrics for the rules in your web ACL. For
    	 information about Amazon CloudWatch metrics, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

###### Temporary inconsistencies during updates

When you create or change a protection pack (web ACL) or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:

- After you create a protection pack (web ACL), if you try to associate it with a resource, you might get an exception indicating that the protection pack (web ACL) is unavailable.
- After you add a rule group to a protection pack (web ACL), the new rule group rules might be in effect in one area where the protection pack (web ACL) is used and not in another.
- After you change a rule action setting, you might see the old action in some places and the new action in others.
- After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.
