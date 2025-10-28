**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Testing and deploying ACFP

This section provides general guidance for configuring and testing an AWS WAF Fraud Control account creation fraud prevention (ACFP)
implementation for your site. The specific steps that you choose to follow will depend
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

Before you deploy your ACFP implementation for production traffic, test and tune it
in a staging or testing environment until you are comfortable with the potential
impact to your traffic. Then test and tune the rules in count mode with your
production traffic before enabling them.

AWS WAF provides test credentials that you can use to verify your ACFP configuration. In
the following procedure, you'll configure a test protection pack (web ACL) to use the ACFP managed rule
group, configure a rule to capture the label added by the rule group, and then run an
account creation attempt using these test credentials. You'll verify that your protection pack (web ACL)
has properly managed the attempt by checking the Amazon CloudWatch metrics for the account
creation attempt.

This guidance is intended for users who know generally how to create and manage
AWS WAF protection packs (web ACLs), rules, and rule groups. Those topics are covered in prior sections
of this guide.

###### To configure and test an AWS WAF Fraud Control account creation fraud prevention (ACFP) implementation

Perform these steps first in a test environment, then in production.

1. ###### Add the AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group in count mode

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

Add the AWS Managed Rules rule group `AWSManagedRulesACFPRuleSet` to a new or existing protection pack (web ACL) and
configure it so that it doesn't alter the current protection pack (web ACL) behavior. For details
about the rules and labels for this rule group, see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md").

    * When you add the managed rule group, edit it and do the following:




    	+ In the **Rule group configuration** pane, provide the details of your
    	 application's account registration and creation pages. The ACFP
    	 rule group uses this information to monitor sign-in activities.
    	 For more information, see [Adding the ACFP managed rule group to your web
    	 ACL](waf-acfp-rg-using.md "waf-acfp-rg-using.md").
    	+ In the **Rules** pane, open the **Override all rule
    	 actions** dropdown and choose
    	 **Count**. With this configuration,
    	 AWS WAF evaluates requests against all of the rules in the
    	 rule group and only counts the matches that result, while still
    	 adding labels to requests. For more information, see [Overriding rule actions in a rule
    	 group](web-acl-rule-group-settings.md#web-acl-rule-group-rule-action-override "web-acl-rule-group-settings.md#web-acl-rule-group-rule-action-override").


    	With this override, you can monitor the potential impact of the ACFP managed rules
    	 to determine whether you want to add exceptions, such as
    	 exceptions for internal use cases.
    * Position the rule group so that it's evaluated after your existing
     rules in the protection pack (web ACL), with a priority setting that's numerically higher
     than any rules or rule groups that you're already using.
     For more information, see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md").



    This way, your current handling of traffic isn't disrupted. For
     example, if you have rules that detect malicious traffic such as SQL
     injection or cross-site scripting, they'll continue to detect and log
     that. Alternately, if you have rules that allow known non-malicious
     traffic, they can continue to allow that traffic, without having it
     blocked by the ACFP managed rule group. You might decide to adjust the
     processing order during your testing and tuning activities.

2. ###### Implement the application integration SDKs

Integrate the AWS WAF JavaScript SDK into your browser's account registration
and account creation paths. AWS WAF also provides mobile SDKs to integrate iOS and
Android devices. For more information about the integration SDKs, see [Client application
integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md"). For information about this
recommendation, see [Using application integration SDKs with ACFP](waf-acfp-with-tokens.md "waf-acfp-with-tokens.md").

###### Note

If you are unable to use the application integration SDKs, it's possible
to test the ACFP rule group by editing it in your protection pack (web ACL) and removing
the override that you placed on the `AllRequests` rule. This
enables the rule's Challenge action setting, to ensure that requests
include a valid challenge token.

_Do this first in a test environment and then with great care in
your production environment._ This approach has the potential
to block users. For example, if your registration page path doesn't accept
`GET` text/html requests, then this rule configuration can
effectively block all requests at the registration page. 3. ###### Enable logging and metrics for the protection pack (web ACL)

As needed, configure logging, Amazon Security Lake data collection, request sampling, and Amazon CloudWatch metrics for the protection pack (web ACL).
You can use these visibility tools to monitor the interaction of the ACFP managed
rule group with your traffic.

    * For information about logging, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").
    * For information about Amazon Security Lake, see
     [What is Amazon Security Lake?](../../../security-lake/latest/userguide/what-is-security-lake.md "../../../security-lake/latest/userguide/what-is-security-lake.md")
     and [Collecting data from AWS services](../../../security-lake/latest/userguide/internal-sources.md "../../../security-lake/latest/userguide/internal-sources.md")
     in the *Amazon Security Lake user guide*.
    * For information about Amazon CloudWatch metrics, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
    * For information about web request sampling, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").

4. ###### Associate the protection pack (web ACL) with a resource

If the protection pack (web ACL) isn't already associated with a test resource, associate it.
For information, see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md"). 5. ###### Monitor traffic and ACFP rule matches

Make sure that your normal traffic is flowing and that the ACFP managed rule group rules
are adding labels to matching web requests. You can see the labels in the logs
and see the ACFP and label metrics in the Amazon CloudWatch metrics. In the logs, the
rules that you've overridden to count in the rule group show up in the
`ruleGroupList` with `action` set to count, and with
`overriddenAction` indicating the configured rule action that you
overrode. 6. ###### Test the rule group's credential checking capabilities

Perform an account creation attempt with test compromised credentials and check that the
rule group matches against them as expected.

    1. Access your protected resource's account registration page and try to add a new account.
     Use the following AWS WAF test credential pair and enter any test




    	* User: `WAF_TEST_CREDENTIAL@wafexample.com`
    	* Password: `WAF_TEST_CREDENTIAL_PASSWORD`
    These test credentials are categorized as compromised credentials, and the ACFP managed
     rule group will add the
     `awswaf:managed:aws:acfp:signal:credential_compromised`
     label to the account creation request, which you can see in the logs.
    2. In your protection pack (web ACL) logs, look for the
     `awswaf:managed:aws:acfp:signal:credential_compromised`
     label in the `labels` field on the log entries for your test
     account creation request. For information about logging, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").After you've verified that the rule group captures compromised credentials as

expected, you can take steps to configure its implementation as you need for
your protected resource. 7. ###### For CloudFront distributions, test the rule group's management of bulk account creation attempts

Run this test for each success response criteria that you configured for the
ACFP rule group. Wait at least 30 minutes between tests.

    1. For each of your success criteria, identify an account
     creation attempt that will succeed with that success criteria in the
     response. Then, from a single client session, perform at least 5
     successful account creation attempts in under 30 minutes. A user would
     normally only create a single account on your site.


    After the first successful account creation, the
     `VolumetricSessionSuccessfulResponse` rule should start
     matching against the rest of your account creation responses, labeling
     them and counting them, based on your rule action override. The rule
     might miss the first one or two due to latency.
    2. In your protection pack (web ACL) logs, look for the
     `awswaf:managed:aws:acfp:aggregate:volumetric:session:successful_creation_response:high`
     label in the `labels` field on the log entries for your test
     account creation web requests. For information about logging, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").These tests verify that your success criteria match your responses by checking that the

successful counts aggregated by the rule surpass the rule's threshold. After
you've reached the threshold, if you continue to send account creation requests
from the same session, the rule will continue to match until the success rate
drops below the threshold. While the threshold is exceeded, the rule matches
both successful or failed account creation attempts from the session address. 8. ###### Customize ACFP web request handling

As needed, add your own rules that explicitly allow or block requests, to
change how ACFP rules would otherwise handle them.

For example, you can use ACFP labels to allow or block requests or to customize
request handling. You can add a label match rule after the ACFP managed rule
group to filter labeled requests for the handling that you want to apply. After
testing, keep the related ACFP rules in count mode, and maintain the request
handling decisions in your custom rule. For an example, see [ACFP example: Custom
response for compromised credentials](waf-acfp-control-example-compromised-credentials.md "waf-acfp-control-example-compromised-credentials.md"). 9. ###### Remove your test rules and enable the ACFP managed rule group
settings

Depending on your situation, you might have decided that you want to leave some ACFP rules
in count mode. For the rules that you want to run as
configured inside the rule group, disable count mode in the protection pack (web ACL) rule group configuration.
When you're finished testing, you can also remove your test label match
rules. 10. ###### Monitor and tune

To be sure that web requests are being handled as you want, closely monitor
your traffic after you enable the ACFP functionality that you intend to use.
Adjust the behavior as needed with the rules count override on the rule group
and with your own rules.
After you finish testing your ACFP rule group implementation, if you haven't already
integrated the AWS WAF JavaScript SDK into your browser's account registration and account
creation pages, we strongly recommend that you do so. AWS WAF also provides mobile SDKs to
integrate iOS and Android devices. For more information about the integration SDKs, see
[Client application
integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md"). For information about this
recommendation, see [Using application integration SDKs with ACFP](waf-acfp-with-tokens.md "waf-acfp-with-tokens.md").
