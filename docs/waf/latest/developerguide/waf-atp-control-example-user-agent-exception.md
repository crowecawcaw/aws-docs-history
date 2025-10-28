**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# ATP example: Custom

handling for missing and compromised credentials

By default, the credentials checks that are performed by the rule group `AWSManagedRulesATPRuleSet`
handle web requests as follows:

- **Missing credentials** – Label and block
  request.
- **Compromised credentials** – Label request but don't
  block or count it.
  For details about the rule group and rule behavior, see [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md "aws-managed-rule-groups-atp.md").

You can add custom handling for web requests that have missing or compromised credentials
by doing the following:

- **Override the `MissingCredential` rule to Count**
  – This rule action override causes the rule to only count and label matching requests.
- **Add a label match rule with custom handling** –
  Configure this rule to match against both of the ATP labels and to perform
  your custom handling. For example, you might redirect the customer to your
  sign-up page.
  The following rule shows the ATP managed rule group from the prior example, with the
  `MissingCredential` rule action overridden to count. This causes the
  rule to apply its label to matching requests, and then only count the requests,
  instead of blocking them.

```
"Rules": [
    {
        "Priority": 1,
        "OverrideAction": {
            "None": {}
        },
        "VisibilityConfig": {
            "SampledRequestsEnabled": true,
            "CloudWatchMetricsEnabled": true,
            "MetricName": "AccountTakeOverValidationRule"
        },
        "Name": "DetectCompromisedUserCredentials",
        "Statement": {
            "ManagedRuleGroupStatement": {
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
                      "EnableRegexInPath": false
                    }
                  }
                ]
                "VendorName": "AWS",
                "Name": "`AWSManagedRulesATPRuleSet`",
 **"RuleActionOverrides": [
 {
 "ActionToUse": {
 "Count": {}
 },
 "Name": "MissingCredential"
 }
 ],**
                "ExcludedRules": []
            }
        }
    }
],

```

With this configuration, when this rule group evaluates any web request that has missing or
compromised credentials, it will label the request, but not block it.

The following rule has a priority setting that is higher numerically than the preceding rule group.
AWS WAF evaluates rules in numeric order, starting from the lowest,
so this rule will be evaluated after the rule group evaluation. The rule is configured to match either of
the credentials labels and to send a custom response for matching requests.

```
"Name": "redirectToSignup",
      "Priority": 10,
      "Statement": {
        "OrStatement": {
          "Statements": [
            {
              "LabelMatchStatement": {
                "Scope": "LABEL",
                "Key": "awswaf:managed:aws:atp:signal:missing_credential"
              }
            },
            {
              "LabelMatchStatement": {
                "Scope": "LABEL",
                "Key": "awswaf:managed:aws:atp:signal:credential_compromised"
              }
            }
          ]
        }
      },
      "Action": {
        "Block": {
          "CustomResponse": {
             `your custom response settings`
          }
        }
      },
      "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "redirectToSignup"
      }

```
