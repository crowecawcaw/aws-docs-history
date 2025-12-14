**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Rate limit the requests with specific ASNs

To limit the number of requests from specific Autonomous System Numbers (ASNs) based on the
IP address of the requests, set the request aggregation to _Custom
keys_ and provide the aggregation criteria.

The following JSON shows an example of a rule aggregating ASNs derived from forwarded IP addresses found in the `X-Forwarded-For` header. If AWS WAF can't derive an ASN because the IP address is malformed, the fallback behavior is set to `MATCH`.

```
{
    "Name": "test-rbr",
    "Priority": 0,
    "Statement": {
        "RateBasedStatement": {
            "AggregateKeyType": "CUSTOM_KEYS",
            "CustomKeys": [
                {
                    "ASN": {}
                },
                {
                    "ForwardedIP": {}
                }
            ],
            "EvaluationWindowSec": 300,
            "ForwardedIPConfig": {
                "FallbackBehavior": "MATCH",
                "HeaderName": "X-Forwarded-For"
            },
            "Limit": 2000
        }
    },
    "VisibilityConfig": {
        "CloudWatchMetricsEnabled": true,
        "MetricName": "test-rbr",
        "SampledRequestsEnabled": true
    }
}
```
