**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Rate limit the requests for labels

that have a specified label namespace

###### Note

The common level rules in the Bot Control managed rule group add labels for bots of various categories, but
they only block requests from unverified bots. For information about these rules, see [Bot Control rules listing](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules").

If you use the Bot Control managed rule group, you can add rate limiting for requests from
individual verified bots. To do this, you add a rate-based rule that runs after
the Bot Control rule group and aggregates requests by their bot name labels. You
specify the **Label namespace** aggregation key and set the
namespace key to `awswaf:managed:aws:bot-control:bot:name:`. Each
unique label with the specified namespace will define an aggregation instance.
For example, the labels
`awswaf:managed:aws:bot-control:bot:name:axios` and
`awswaf:managed:aws:bot-control:bot:name:curl` each define an
aggregation instance.

The following protection pack (web ACL) JSON listing shows this configuration. The rule in this example
limits requests for any single bot aggregation instance to 1,000 in a two minute
period.

```
{
  "Name": "test-web-acl",
  "Id": ...
  "ARN": ...
  "DefaultAction": {
    "Allow": {}
  },
  "Description": "",
  "Rules": [
    {
      "Name": "AWS-AWSManagedRulesBotControlRuleSet",
      "Priority": 0,
      "Statement": {
        "ManagedRuleGroupStatement": {
          "VendorName": "AWS",
          "Name": "AWSManagedRulesBotControlRuleSet",
          "ManagedRuleGroupConfigs": [
            {
              "AWSManagedRulesBotControlRuleSet": {
                "InspectionLevel": "COMMON"
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
        "MetricName": "AWS-AWSManagedRulesBotControlRuleSet"
      }
    },
    {
      "Name": "test-rbr",
      "Priority": 1,
      "Statement": {
        "RateBasedStatement": {
          "Limit": 1000,
          "EvaluationWindowSec": 120,
          "AggregateKeyType": "CUSTOM_KEYS",
          "CustomKeys": [
            {
              "LabelNamespace": {
                "Namespace": "awswaf:managed:aws:bot-control:bot:name:"
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
        "MetricName": "test-rbr"
      }
    }
  ],
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "test-web-acl"
  },
  "Capacity": 82,
  "ManagedByFirewallManager": false,
  "RetrofittedByFirewallManager": false,
  "LabelNamespace": "awswaf:0000000000:webacl:test-web-acl:"
}
```
