**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using AWS CloudFormation with

automatic application layer DDoS mitigation

This page explains how to use AWS CloudFormation to manage your protections and AWS WAF web ACLs.

###### Enabling or disabling automatic application layer DDoS mitigation

You can enable and disable automatic application layer DDoS mitigation through AWS CloudFormation, using the
`AWS::Shield::Protection` resource. The effect is the same as
when you enable or disable the feature through the console or any other
interface. For information about the AWS CloudFormation resource, see [AWS::Shield::Protection](../../../AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.md") in the _AWS CloudFormation user guide_.

###### Managing web ACLs used with automatic mitigation

Shield Advanced manages automatic mitigation for your protected resource using a rule
group rule in the protected resource's AWS WAF web ACL. Through
the AWS WAF console and APIs, you'll see the rule listed
in your web ACL rules, with a name that starts with
`ShieldMitigationRuleGroup`. This rule
is dedicated to your automatic application layer DDoS mitigation and it's
managed for you by Shield Advanced and AWS WAF. For more information, see [Protecting the application layer with the Shield Advanced
rule group](ddos-automatic-app-layer-response-rg.md "ddos-automatic-app-layer-response-rg.md") and [How Shield Advanced manages automatic mitigation](ddos-automatic-app-layer-response-behavior.md "ddos-automatic-app-layer-response-behavior.md").

If you use AWS CloudFormation to manage your web ACLs, don't add the Shield Advanced rule group
rule to your web ACL template. When you update a web ACL that's being
used with your automatic mitigation protections, AWS WAF automatically manages the
rule group rule in the web ACL.

You'll
see the following differences compared to other web ACLs that you manage through AWS CloudFormation:

- AWS CloudFormation won't report any drift in the stack drift status between the actual configuration of the
  web ACL, with the Shield Advanced rule group rule, and your web
  ACL template, without the rule. The Shield Advanced rule
  won't appear in the actual listing for the
  resource in the drift details.

You will be able to see the Shield Advanced rule group rule in
web ACL listings that you retrieve from AWS WAF, such as through the AWS WAF
console or AWS WAF APIs.

- If you modify the web ACL template in a stack, AWS WAF and Shield Advanced
  automatically maintain the Shield Advanced automatic mitigation rule
  in the updated web ACL. The automatic mitigation protections
  provided by Shield Advanced are not interrupted by your update to the web
  ACL.
  Don't manage the Shield Advanced rule in your AWS CloudFormation web ACL
  template. The web ACL template shouldn't list the Shield Advanced rule.
  Follow the best practices for web ACL management at [Best practices for
  using automatic application layer DDoS mitigation](ddos-automatic-app-layer-response-bp.md "ddos-automatic-app-layer-response-bp.md").
