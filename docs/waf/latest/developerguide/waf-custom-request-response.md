**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Customized web requests and responses in

AWS WAF

This section explains how to add custom web request and response handling behavior to your AWS WAF rule actions and
default protection pack (web ACL) actions. Your custom settings apply whenever the action they're attached to
applies.

You can customize web requests and responses in the following ways:

- With Allow, Count, CAPTCHA, and Challenge actions, you can insert custom headers into the web request. When AWS WAF
  forwards the web request to the protected resource, the request contains the entire
  original request plus the custom headers that you've inserted. For the CAPTCHA and Challenge actions,
  AWS WAF only applies the customization if the request passes the CAPTCHA or challenge token inspection.

- With Block actions, you can define a complete custom response, with response code, headers,
  and body. The protected resource responds to the request using the custom response
  provided by AWS WAF. Your custom response replaces the default Block action response
  of `403 (Forbidden)`.

###### Action settings that you can customize

You can specify a custom request or response when you define the following action settings:

- Rule action. For information, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").
- Default action for a protection pack (web ACL). For information, see [Setting the protection pack (web ACL) default action in AWS WAF](web-acl-default-action.md "web-acl-default-action.md").

###### Action settings that you cannot customize

You _cannot_ specify custom request handling in the
override action for a rule group that you use in a protection pack (web ACL). See [Using protection packs (web ACLs) with rules and rule groups in AWS WAF](web-acl-processing.md "web-acl-processing.md"). Also see [Using managed rule group
statements in AWS WAF](waf-rule-statement-type-managed-rule-group.md "waf-rule-statement-type-managed-rule-group.md") and [Using rule group
statements in AWS WAF](waf-rule-statement-type-rule-group.md "waf-rule-statement-type-rule-group.md").

###### Temporary inconsistencies during updates

When you create or change a protection pack (web ACL) or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:

- After you create a protection pack (web ACL), if you try to associate it with a resource, you might get an exception indicating that the protection pack (web ACL) is unavailable.
- After you add a rule group to a protection pack (web ACL), the new rule group rules might be in effect in one area where the protection pack (web ACL) is used and not in another.
- After you change a rule action setting, you might see the old action in some places and the new action in others.
- After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.

###### Limits on your use of custom requests and responses

AWS WAF defines maximum settings for your use of custom requests and responses. For example, a maximum number of
request headers per protection pack (web ACL) or rule group, and a maximum number of custom headers for a single custom response
definition. For information, see [AWS WAF quotas](limits.md "limits.md").

###### Topics

- [Inserting custom request headers for non-blocking actions](customizing-the-incoming-request.md "customizing-the-incoming-request.md")
- [Sending custom responses for Block
  actions](customizing-the-response-for-blocked-requests.md "customizing-the-response-for-blocked-requests.md")
- [Supported status codes for
  custom responses](customizing-the-response-status-codes.md "customizing-the-response-status-codes.md")
