**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Rate limit the requests to a login page

To limit the number of requests to the login page on your website without affecting traffic
to the rest of your site, you could create a rate-based rule with a scope-down
statement that matches requests to your login page and with the request
aggregation set to **Count all**.

The rate-based rule will count all requests for the login page in a single aggregation
instance and apply the rule action when the requests exceed the limit.

The following JSON listing shows an example of this rule configuration. The count all aggregation option
is listed in the JSON as the setting `CONSTANT`. This example matches login pages that start with
`/login`.

```
{
  "Name": "test-rbr",
  "Priority": 0,
  "Action": {
    "Block": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "test-rbr"
  },
  "Statement": {
    "RateBasedStatement": {
      "Limit": 1000,
      "EvaluationWindowSec": 300,
      "AggregateKeyType": "CONSTANT",
      "ScopeDownStatement": {
        "ByteMatchStatement": {
          "FieldToMatch": {
            "UriPath": {}
          },
          "PositionalConstraint": "STARTS_WITH",
          "SearchString": "/login",
          "TextTransformations": [
            {
              "Type": "NONE",
              "Priority": 0
            }
          ]
        }
      }
    }
  }
}
```
