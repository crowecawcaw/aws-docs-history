**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Blocking requests that don't have a valid

AWS WAF token

This section explains how to block login requests that are missing their tokens when using the AWS WAF mobile SDK.

When you use the intelligent threat AWS Managed Rules rule groups `AWSManagedRulesACFPRuleSet`, `AWSManagedRulesATPRuleSet`, and `AWSManagedRulesBotControlRuleSet`, the
rule groups invoke AWS WAF token management to evaluate the status of the web request
token and to label the requests accordingly.

###### Note

Token labeling is only applied to web requests that you evaluate using one of these
managed rule groups.

For information about the labeling that token management applies, see the preceding section,
[Types of token labels in AWS WAF](waf-tokens-labeling.md "waf-tokens-labeling.md").

The intelligent threat mitigation managed rule groups then handle token requirements
as follows:

- The `AWSManagedRulesACFPRuleSet` `AllRequests` rule is configured to run the Challenge
  action against all requests, effectively blocking any that don't have the
  `accepted` token label.
- The `AWSManagedRulesATPRuleSet` blocks requests that have the `rejected` token label, but it
  doesn't block requests with the `absent` token label.
- The `AWSManagedRulesBotControlRuleSet` targeted protection level challenges clients after they send five requests without an
  `accepted` token label. It doesn't block an individual request
  that doesn't have a valid token. The common protection level of the rule group doesn't manage
  token requirements.
  For additional details about the intelligent threat rule groups, see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md"), [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md "aws-managed-rule-groups-atp.md") and [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md").

###### To block requests that are missing tokens when using the Bot Control or ATP

managed rule group

With the Bot Control and ATP rule groups, it's possible for a request without a
valid token to exit the rule group evaluation and continue to be evaluated by the
protection pack (web ACL).

To block all requests that are missing their token or whose token is rejected, add a
rule to run immediately after the managed rule group to capture and block requests that
the rule group doesn't handle for you.

The following is an example JSON listing for a protection pack (web ACL) that uses the ATP managed rule
group. The protection pack (web ACL) has an added rule to capture the
`awswaf:managed:token:absent` label and handle it. The rule narrows its
evaluation to web requests going to the login endpoint, to match the scope of the
ATP rule group. The added rule is listed in bold.

```
{
  "Name": "exampleWebACL",
  "Id": "55555555-6666-7777-8888-999999999999",
  "ARN": "arn:aws:wafv2:us-east-1:111111111111:regional/webacl/exampleWebACL/55555555-4444-3333-2222-111111111111",
  "DefaultAction": {
    "Allow": {}
  },
  "Description": "",
  "Rules": [
    {
      "Name": "AWS-AWSManagedRulesATPRuleSet",
      "Priority": 1,
      "Statement": {
        "ManagedRuleGroupStatement": {
          "VendorName": "AWS",
          "Name": "AWSManagedRulesATPRuleSet",
          "ManagedRuleGroupConfigs": [
            {
              "AWSManagedRulesATPRuleSet": {
                "LoginPath": "/web/login",
                "RequestInspection": {
                  "PayloadType": "JSON",
                  "UsernameField": {
                    "Identifier": "/form/username"
                  },
                  "PasswordField": {
                    "Identifier": "/form/password"
                  }
                },
                "ResponseInspection": {
                  "StatusCode": {
                    "SuccessCodes": [
                      200
                    ],
                    "FailureCodes": [
                      401,
                      403,
                      500
                    ]
                  }
                }
              }
            }
          ]
        }
      },
      "OverrideAction": {
        "None": {}
      },
      "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "AWS-AWSManagedRulesATPRuleSet"
      }
    },
    {
      **"Name": "RequireTokenForLogins",
 "Priority": 2,
 "Statement": {
 "AndStatement": {
 "Statements": [
 {
 "Statement": {
 "LabelMatchStatement": {
 "Scope": "LABEL",
 "Key": "awswaf:managed:token:absent"
 }
 }
 },
 {
 "ByteMatchStatement": {
 "SearchString": "/web/login",
 "FieldToMatch": {
 "UriPath": {}
 },
 "TextTransformations": [
 {
 "Priority": 0,
 "Type": "NONE"
 }
 ],
 "PositionalConstraint": "STARTS\_WITH"
 }
 },
 {
 "ByteMatchStatement": {
 "SearchString": "POST",
 "FieldToMatch": {
 "Method": {}
 },
 "TextTransformations": [
 {
 "Priority": 0,
 "Type": "NONE"
 }
 ],
 "PositionalConstraint": "EXACTLY"
 }
 }
 ]
 }
 },
 "Action": {
 "Block": {}
 },
 "VisibilityConfig": {
 "SampledRequestsEnabled": true,
 "CloudWatchMetricsEnabled": true,
 "MetricName": "RequireTokenForLogins"
 }**
    }
  ],
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "exampleWebACL"
  },
  "Capacity": 51,
  "ManagedByFirewallManager": false,
  "RetrofittedByFirewallManager": false,
  "LabelNamespace": "awswaf:111111111111:webacl:exampleWebACL:"
}
```
