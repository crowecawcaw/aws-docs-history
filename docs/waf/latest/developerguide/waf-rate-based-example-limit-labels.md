**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Rate limit the requests with specific labels

To
limit the number of requests of various categories, you can combine rate limiting with any rule or rule
group that add labels to requests. To do this, you configure
your protection pack (web ACL) as follows:

- Add the rules or rule groups that add labels, and configure them so that they don't block
  or allow the requests that you want to rate limit. If you use managed
  rule groups, you might need to override some rule group rule actions to
  Count to achieve this behavior.
- Add a rate-based rule to your protection pack (web ACL) with a priority number setting that is higher than the labeling
  rules and rule groups. AWS WAF evaluates rules in numeric order, starting from the lowest,
  so your rate-based rule will run after the labeling rules.
  Configure your rate limiting on the labels using a combination of
  label matching in the rule's scope-down statement and label aggregation.
  The following example uses the Amazon IP reputation list AWS Managed Rules rule group. The rule group rule
  `AWSManagedIPDDoSList` detects and labels requests whose IPs are
  known to be actively engaging in DDoS activities. The rule's action is
  configured to Count in the rule group definition. For more information
  about the rule group, see [Amazon IP reputation list managed rule group](aws-managed-rule-groups-ip-rep.md#aws-managed-rule-groups-ip-rep-amazon "aws-managed-rule-groups-ip-rep.md#aws-managed-rule-groups-ip-rep-amazon").

The following protection pack (web ACL) JSON listing uses the IP reputation rule group followed by a
label-matching rate-based rule. The rate-based rule uses a scope-down statement
to filter for requests that have been marked by the rule group rule. The
rate-based rule statement aggregates and rate limits the filtered requests by
their IP addresses.

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
      "Name": "AWS-AWSManagedRulesAmazonIpReputationList",
      "Priority": 0,
      "Statement": {
        "ManagedRuleGroupStatement": {
          "VendorName": "AWS",
          "Name": "AWSManagedRulesAmazonIpReputationList"
        }
      },
      "OverrideAction": {
        "None": {}
      },
      "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "AWS-AWSManagedRulesAmazonIpReputationList"
      }
    },
    {
      "Name": "test-rbr",
      "Priority": 1,
      "Statement": {
        "RateBasedStatement": {
          "Limit": 100,
          "EvaluationWindowSec": 300,
          "AggregateKeyType": "IP",
          "ScopeDownStatement": {
            "LabelMatchStatement": {
              "Scope": "LABEL",
              "Key": "awswaf:managed:aws:amazon-ip-list:AWSManagedIPDDoSList"
            }
          }
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
  "Capacity": 28,
  "ManagedByFirewallManager": false,
  "RetrofittedByFirewallManager": false,
  "LabelNamespace": "awswaf:0000000000:webacl:test-web-acl:"
}
```
