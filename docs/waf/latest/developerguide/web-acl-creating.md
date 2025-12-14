**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Creating a protection pack (web ACL) in AWS WAF

Using the new console
This section provides procedures for creating protection packs (web ACLs) through
the new AWS console.

To create a new protection pack (web ACL), use the protection pack (web ACL) creation wizard following the procedure
on this page.

###### Production traffic risk

Before you deploy changes in your protection pack (web ACL) for production traffic, test and
tune them in a staging or testing environment until you are comfortable with the
potential impact to your traffic. Then test and tune your updated rules in count
mode with your production traffic before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Using more than 1,500 WCUs in a protection pack (web ACL) incurs costs beyond the basic protection pack (web ACL) price. For more information, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

1. Sign in to the new AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2-pro](https://console.aws.amazon.com/wafv2-pro "https://console.aws.amazon.com/wafv2-pro").
2. In the navigation pane, choose **Resources & protection packs (web ACLs)**.
3. On the **Resources & protection packs (web ACLs)** page, choose **Add
   protection pack (web ACL)**.
4. Under **Tell us about your app**, for **App category**, select one or more app categories.
5. For **Traffic source**, choose the type of traffic the application engages with; **API**, **Web**, or **Both API and Web**.
6. Under **Resources to protect,** choose **Add
   resources**.
7. Choose the category of AWS
   resource that you want to associate with this protection pack (web ACL), either Amazon CloudFront
   distributions or Regional resources. For more information, see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md").
8. Under **Choose initial protections,** select your preferred protection level:
   **Recommended**,
   **Essentials**, or **You build
   it**.
9. (Optional) If you choose **You build it**, build your rules.
   1. (Optional) If you want to add your own rule, on the **Add rules** page,
      choose **Custom rule** and then choose
      **Next**.
      1. Choose the rule type.
      2. For **Action**, select the action
         you want the rule to take when it matches a web
         request. For information on your choices, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md") and [Using protection packs (web ACLs) with rules and rule groups in AWS WAF](web-acl-processing.md "web-acl-processing.md").

      If you are using the
      **CAPTCHA** or
      **Challenge** action,
      adjust the **Immunity time**
      configuration as needed for the rule. If you don't
      specify the setting, the rule inherits it from the
      protection pack (web ACL). To modify the protection pack (web ACL)
      immunity time settings, edit the protection pack (web ACL)
      after you create it. For more information about
      immunity times, see [Setting timestamp expiration and token immunity times in AWS WAF](waf-tokens-immunity-times.md "waf-tokens-immunity-times.md").

      ###### Note

      You are charged additional fees when you use the CAPTCHA or Challenge rule action in one of your rules or as a rule action override in a rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

      If you want to customize the request or response,
      choose the options for that and fill in the details
      of your customization. For more information, see
      [Customized web requests and responses in
      AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md").

      If you want to have your rule add labels to
      matching web requests, choose the options for that
      and fill in your label details. For more
      information, see [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md"). 3. For **Name**, enter the name that
      you want to use to identify this rule. Don't use
      names that start with `AWS`,
      `Shield`, `PreFM`, or
      `PostFM`. These strings are either
      reserved or could cause confusion with rule groups
      that are managed for you by other services. 4. Enter your rule definition, according to your
      needs. You can combine rules inside logical
      `AND` and `OR` rule
      statements. The wizard guides you through the
      options for each rule, according to context. For
      information about your rules options, see [AWS WAF rules](waf-rules.md "waf-rules.md"). 5. Choose **Create rule**.

      ###### Note

      If you add more than one rule to a
      protection pack (web ACL), AWS WAF evaluates the rules in
      the order that they're listed for the
      protection pack (web ACL). For more information, see [Using protection packs (web ACLs) with rules and rule groups in AWS WAF](web-acl-processing.md "web-acl-processing.md").

   2. (Optional) If you want to add managed rule groups, on the **Add
      rules** page, choose **AWS-managed
      rule group** or **AWS Marketplace
      rule group** and then choose
      **Next**. Do the following for each
      managed rule group that you want to add:
      1. On the **Add rules** page, expand the listing for AWS
         managed rule groups or for the AWS Marketplace seller.
      2. Choose the version of the rule group.
      3. To customize how your protection pack (web ACL) uses the rule group, choose
         **Edit**. The following are
         common customization settings:
         - Reduce the scope of the web requests that
           the rule group inspects by adding a scope-down
           statement in the **Inspection**
           section. For information about this option, see
           [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md").
         - Override the rule actions for some or all rules in **Rule
           overrides**. If you don't define an
           override action for a rule, the evaluation uses
           the rule action that's defined inside the rule
           group. For information about this option, see
           [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").
         - Some managed rule groups require you to provide additional
           configuration. See the documentation from your managed rule
           group provider. For information specific to the AWS Managed Rules rule groups,
           see [AWS Managed Rules for AWS WAF](aws-managed-rule-groups.md "aws-managed-rule-groups.md").

      4. Choose **Next**.

   3. (Optional) If you want to add your own rule group, on the **Add
      rules** page, choose **Custom rule
      group** and then choose
      **Next**. Do the following for each
      rule group that you want to add:
      1. For **Name**, enter the name that you want to use for the rule
         group rule in this protection pack (web ACL). Don't use
         names that start with `AWS`,
         `Shield`, `PreFM`, or
         `PostFM`. These strings are either
         reserved or could cause confusion with rule groups
         that are managed for you by other services. See
         [Recognizing rule groups provided by other services](waf-service-owned-rule-groups.md "waf-service-owned-rule-groups.md").
      2. Choose your rule group from the list.
      3. (Optional) Under **Rule
         configuration**, choose a **Rule
         override**. You can override the rule
         actions to any valid action setting, the same as you
         can do for managed rule groups.
      4. (Optional) Under **Add labels**, choose **Add
         label** and then enter any labels you
         want to add to requests that match the rule. Rules
         that are evaluated later in the same
         protection pack (web ACL) can reference the labels this rule
         adds.
      5. Choose **Create rule**.

10. Under **Name and description**, enter a name for your
    protection pack (web ACL). Optionally, enter a description.

###### Note

You can't change the name after you create the protection pack (web ACL). 11. (Optional) Under **Customize protection pack (web ACL)**, configure default
rule actions, configurations, and logging destination:

    1. (Optional) Under **Default rule actions**, choose the default action for the
     protection pack (web ACL). This is the action that AWS WAF takes on a
     request when the rules in the protection pack (web ACL) don't
     explicitly take an action. For more information, see [Customized web requests and responses in
     AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md").
    2. (Optional) Under Rule configuration, customize settings for rules in the
     protection pack (web ACL):




    	* **Default rate limits** - Set rate limits to block Denial of
    	 Service (DoS) attacts that can affect availability,
    	 compromise security, or consume excessive resources.
    	 This rule rate blocks requests per IP address that
    	 exceed the allowed rate for your application. For
    	 more information, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md")
    	* **IP Addresses** - Enter IP
    	 addresses to block or allow. This setting overrides
    	 other rules.
    	* **Country specific origins** -
    	 Block requests from specified countries or Count all
    	 traffic.
    3. For **Logging destination**, configure the logging destination type
     and the place to store logs. For more information, see [AWS WAF logging destinations](logging-destinations.md "logging-destinations.md").

12. Review your settings and choose **Add protection pack (web ACL)**.

Using the standard console
This section provides procedures for creating web ACLs through
the AWS console.

To create a new web ACL, use the web ACL creation wizard following the procedure
on this page.

###### Production traffic risk

Before you deploy changes in your web ACL for production traffic, test and
tune them in a staging or testing environment until you are comfortable with the
potential impact to your traffic. Then test and tune your updated rules in count
mode with your production traffic before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Using more than 1,500 WCUs in a protection pack (web ACL) incurs costs beyond the basic protection pack (web ACL) price. For more information, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### To create a web ACL

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. Choose **web ACLs** in the navigation pane, and then
   choose **Create web ACL**.
3. For **Name**, enter the name that you want to use to
   identify this web ACL.

###### Note

You can't change the name after you create the web ACL. 4. (Optional) For **Description - optional**, enter a longer
description for the web ACL if you want to. 5. For **CloudWatch metric name**, change the default name if
applicable. Follow the guidance on the console for valid characters. The
name can't contain special characters, white space, or metric names reserved
for AWS WAF, including "All" and "Default_Action."

###### Note

You can't change the CloudWatch metric name after you create the web
ACL. 6. Under **Resource type**, choose the category of AWS
resource that you want to associate with this web ACL, either Amazon CloudFront
distributions or Regional resources. For more information, see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md"). 7. For **Region**, if you've chosen a
Regional resource type, choose the Region where you want AWS WAF to store the
web ACL.

You only need to choose this option for Regional resource
types. For CloudFront distributions, the Region is hard-coded to the
US East (N. Virginia) Region, `us-east-1`, for Global (CloudFront)
applications. 8. (CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access) For **Web request inspection size
limit - optional**, if you want to specify a different body
inspection size limit, select the limit. Inspecting body sizes over the
default of 16 KB can incur additional costs. For information about this
option, see [Considerations for managing body inspection in AWS WAF](web-acl-setting-body-inspection-limit.md "web-acl-setting-body-inspection-limit.md"). 9. (Optional) For **Associated AWS resources - optional**,
if you want to specify your resources now, choose **Add AWS
resources**. In the dialog box, choose the resources that you
want to associate, and then choose **Add**. AWS WAF returns
you to the **Describe web ACL and associated AWS
resources** page.

###### Note

When you choose to associate an Application Load Balancer with your web ACL, **Resource-level DDoS protection** is enabled.
For more information, see [AWS WAF Distributed Denial of Service (DDoS) prevention](waf-anti-ddos.md "waf-anti-ddos.md"). 10. Choose **Next**. 11. (Optional) If you want to add managed rule groups, on the **Add
rules and rule groups** page, choose **Add
rules**, and then choose **Add managed rule
groups**. Do the following for each managed rule group that you
want to add:

    1. On the **Add managed rule groups** page, expand the listing for AWS
     managed rule groups or for the AWS Marketplace seller of your choice.
    2. For the rule group that you want to add, in the **Action**
     column, turn on the **Add
     to web ACL** toggle.


    To customize how your web ACL uses the rule group, choose **Edit**.
     The following are common customization settings:




    	* Override the rule actions for some or all rules. If you
    	 don't define an override action for a rule, the evaluation
    	 uses the rule action that's defined inside the rule group.
    	 For information about this option, see [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").
    	* Reduce the scope of the web requests that the rule group
    	 inspects by adding a scope-down statement. For information
    	 about this option, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md").
    	* Some managed rule groups require you to provide additional
    	 configuration. See the documentation from your managed rule
    	 group provider. For information specific to the AWS Managed Rules rule groups,
    	 see [AWS Managed Rules for AWS WAF](aws-managed-rule-groups.md "aws-managed-rule-groups.md").
    When you're finished with your settings, choose **Save
     rule**.Choose **Add rules** to finish adding managed rules and

return to the **Add rules and rule groups** page.

###### Note

If you add more than one rule to a web ACL, AWS WAF evaluates the rules in the order that
they're listed for the web ACL. For more information, see [Using protection packs (web ACLs) with rules and rule groups in AWS WAF](web-acl-processing.md "web-acl-processing.md"). 12. (Optional) If you want to add your own rule group, on the **Add
rules and rule groups** page, choose **Add
rules**, and then choose **Add my own rules and rule
groups**. Do the following for each rule group that you want to
add:

    1. On the **Add my own rules and rule groups** page,
     choose **Rule group**.
    2. For **Name**, enter the name that you want to use for the rule group
     rule in this web ACL. Don't use names that start with
     `AWS`, `Shield`, `PreFM`, or
     `PostFM`. These strings are either reserved or could
     cause confusion with rule groups that are managed for you by other
     services. See [Recognizing rule groups provided by other services](waf-service-owned-rule-groups.md "waf-service-owned-rule-groups.md").
    3. Choose your rule group from the list.


    ###### Note

    If you want to override the rule actions for a rule group of
     your own, first save it to the web ACL, and then edit the web
     ACL and the rule group reference statement in the web ACL's rule
     listing. You can override the rule actions to any valid action
     setting, the same as you can do for managed rule groups.
    4. Choose **Add rule**.

13. (Optional) If you want to add your own rule, on the **Add rules
    and rule groups** page, choose **Add rules**,
    **Add my own rules and rule groups**, **Rule
    builder**, then **Rule visual editor**.

###### Note

The console **Rule visual editor** supports one level of nesting. For
example, you can use a single logical `AND` or `OR` statement and nest one
level of other statements inside it, but you can't nest logical
statements within logical statements. To manage more complex rule
statements, use the **Rule JSON editor**. For
information about all options for rules, see [AWS WAF rules](waf-rules.md "waf-rules.md").

This procedure covers the **Rule visual editor**.

    1. For **Name**, enter the name that you want to use to identify this
     rule. Don't use names that start with `AWS`,
     `Shield`, `PreFM`, or `PostFM`.
     These strings are either reserved or could cause confusion with rule
     groups that are managed for you by other services.
    2. Enter your rule definition, according to your needs. You can combine rules inside
     logical `AND` and `OR` rule statements. The wizard guides you through
     the options for each rule, according to context. For information
     about your rules options, see [AWS WAF rules](waf-rules.md "waf-rules.md").
    3. For **Action**, select the action you want the rule to take when it
     matches a web request. For information on your choices, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md") and
     [Using protection packs (web ACLs) with rules and rule groups in AWS WAF](web-acl-processing.md "web-acl-processing.md").


    If you are using the **CAPTCHA** or
     **Challenge** action, adjust the
     **Immunity time** configuration as needed for
     the rule. If you don't specify the setting, the rule inherits it
     from the web ACL. To modify the web ACL immunity time settings,
     edit the web ACL after you create it. For more information about immunity times, see [Setting timestamp expiration and token immunity times in AWS WAF](waf-tokens-immunity-times.md "waf-tokens-immunity-times.md").


    ###### Note

    You are charged additional fees when you use the CAPTCHA or Challenge rule action in one of your rules or as a rule action override in a rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").


    If you want to customize the request or response, choose the
     options for that and fill in the details of your customization. For
     more information, see [Customized web requests and responses in
     AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md").


    If you want to have your rule add labels to matching web requests,
     choose the options for that and fill in your label details. For more
     information, see [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md").
    4. Choose **Add rule**.

14. Choose the default action for the web ACL, either Block or Allow. This is
    the action that AWS WAF takes on a request when the rules in the web ACL don't
    explicitly allow or block it. For more information, see [Setting the protection pack (web ACL) default action in AWS WAF](web-acl-default-action.md "web-acl-default-action.md").

If you want to customize the default action, choose the options for that
and fill in the details of your customization. For more information, see
[Customized web requests and responses in
AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md"). 15. You can define a **Token domain list** to enable token sharing between
protected applications. Tokens are used by the CAPTCHA and
Challenge actions and by the application integration SDKs that you
implement when you use the AWS Managed Rules rule groups for AWS WAF Fraud Control account creation fraud prevention (ACFP), AWS WAF Fraud Control account takeover prevention (ATP), and AWS WAF Bot Control.

Public suffixes aren't allowed. For example, you can't use `gov.au` or `co.uk` as a token domain.

By default, AWS WAF accepts tokens only for the domain of the protected resource. If you
add token domains in this list, AWS WAF accepts tokens for all domains in the
list and for the domain of the associated resource. For more information,
see [AWS WAF protection pack (web ACL) token domain list configuration](waf-tokens-domains.md#waf-tokens-domain-lists "waf-tokens-domains.md#waf-tokens-domain-lists"). 16. Choose **Next**. 17. In the **Set rule priority** page, select and move your
rules and rule groups to the order that you want AWS WAF to process them.
AWS WAF processes rules starting from the top of the list. When you save the web ACL
AWS WAF assigns numeric priority settings to the rules, in the order that you have them listed.
For more information, see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md"). 18. Choose **Next**. 19. In the **Configure metrics** page, review the options and apply any
updates that you need. You can combine metrics from multiple sources by
providing the same **CloudWatch metric name** for them. 20. Choose **Next**. 21. In the **Review and create web ACL** page, check over
your definitions. If you want to change any area, choose
**Edit** for the area. This returns you to the page in
the web ACL wizard. Make any changes, then choose **Next**
through the pages until you come back to the **Review and create web
ACL** page. 22. Choose **Create web ACL**. Your new web ACL is listed in the
**web ACLs** page.
