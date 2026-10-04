

# Example metric filters
<a name="gr-cloudwatch-metric-filters"></a>

This section contains example metric filter patterns and Amazon CloudWatch Logs Insights queries for Route 53 Global Resolver DNS query logs.

**Blocked queries by Global Resolver**

```
{
 "logGroupName": "/aws/vendedlogs/route53globalresolver/global-resolver/GLOBAL_RESOLVER_LOGS/gr-<resolverId>",
 "filterName": "BlockedQueriesByGlobalResolverId",
 "filterPattern": "{ $.disposition = \"Blocked\" }",
 "metricTransformations": [
   {
     "metricName": "BlockedQueriesByGlobalResolverId",
     "metricNamespace": "Route53GlobalResolver",
     "metricValue": "1",
     "dimensions": { "GlobalResolverId": "$.enrichments[0].value" }
   }
 ]
}
```

**Allowed queries by Access Source**

```
{
 "logGroupName": "/aws/vendedlogs/route53globalresolver/global-resolver/GLOBAL_RESOLVER_LOGS/gr-<resolverId>",
 "filterName": "AllowedQueriesByAccessSourceCidr",
 "filterPattern": "{ $.disposition = \"Allowed\" }",
 "metricTransformations": [
   {
     "metricName": "AllowedQueriesByAccessSourceCidr",
     "metricNamespace": "Route53GlobalResolver",
     "metricValue": "1",
     "dimensions": { "AccessSourceCidr": "$.enrichments[0].data.access_source_cidr" }
   }
 ]
}
```

**Alert queries by Access Token**

```
{
 "logGroupName": "/aws/vendedlogs/route53globalresolver/global-resolver/GLOBAL_RESOLVER_LOGS/gr-<resolverId>",
 "filterName": "AlertQueriesByAccessTokenId",
 "filterPattern": "{ $.disposition = \"Alert\" }",
 "metricTransformations": [
   {
     "metricName": "AlertQueriesByAccessTokenId",
     "metricNamespace": "Route53GlobalResolver",
     "metricValue": "1",
     "dimensions": { "AccessTokenId": "$.enrichments[0].data.token_id" }
   }
 ]
}
```

**Total queries by DNS View**

```
{
 "logGroupName": "/aws/vendedlogs/route53globalresolver/global-resolver/GLOBAL_RESOLVER_LOGS/gr-<resolverId>",
 "filterName": "TotalQueriesByDNSViewId",
 "filterPattern": "{ $.query_time = * }",
 "metricTransformations": [
   {
     "metricName": "TotalQueriesByDNSViewId",
     "metricNamespace": "Route53GlobalResolver",
     "metricValue": "1",
     "dimensions": { "DNSViewId": "$.enrichments[0].data.dns_view_id" }
   }
 ]
}
```

**SERVFAIL by Global Resolver**

```
{
 "logGroupName": "/aws/vendedlogs/route53globalresolver/global-resolver/GLOBAL_RESOLVER_LOGS/gr-<resolverId>",
 "filterName": "ServfailQueriesByGlobalResolverId",
 "filterPattern": "{ $.rcode = \"SERVFAIL\" }",
 "metricTransformations": [
   {
     "metricName": "ServfailQueriesByGlobalResolverId",
     "metricNamespace": "Route53GlobalResolver",
     "metricValue": "1",
     "dimensions": { "GlobalResolverId": "$.enrichments[0].value" }
   }
 ]
}
```

**REFUSED by Access Source**

```
{
 "logGroupName": "/aws/vendedlogs/route53globalresolver/global-resolver/GLOBAL_RESOLVER_LOGS/gr-<resolverId>",
 "filterName": "RefusedQueriesByAccessSourceCidr",
 "filterPattern": "{ $.rcode = \"REFUSED\" }",
 "metricTransformations": [
   {
     "metricName": "RefusedQueriesByAccessSourceCidr",
     "metricNamespace": "Route53GlobalResolver",
     "metricValue": "1",
     "dimensions": { "AccessSourceCidr": "$.enrichments[0].data.access_source_cidr" }
   }
 ]
}
```

**NXDOMAIN by Access Token**

```
{
 "logGroupName": "/aws/vendedlogs/route53globalresolver/global-resolver/GLOBAL_RESOLVER_LOGS/gr-<resolverId>",
 "filterName": "NxdomainQueriesByAccessTokenId",
 "filterPattern": "{ $.rcode = \"NXDOMAIN\" }",
 "metricTransformations": [
   {
     "metricName": "NxdomainQueriesByAccessTokenId",
     "metricNamespace": "Route53GlobalResolver",
     "metricValue": "1",
     "dimensions": { "AccessTokenId": "$.enrichments[0].data.token_id" }
   }
 ]
}
```

**NOERROR by DNS View**

```
{
 "logGroupName": "/aws/vendedlogs/route53globalresolver/global-resolver/GLOBAL_RESOLVER_LOGS/gr-<resolverId>",
 "filterName": "NoerrorQueriesByDNSViewId",
 "filterPattern": "{ $.rcode = \"NOERROR\" }",
 "metricTransformations": [
   {
     "metricName": "NoerrorQueriesByDNSViewId",
     "metricNamespace": "Route53GlobalResolver",
     "metricValue": "1",
     "dimensions": { "DNSViewId": "$.enrichments[0].data.dns_view_id" }
   }
 ]
}
```

**Amazon CloudWatch Logs Insights queries for P90 response time**

**P90 Response Time by Global Resolver**

```
fields @timestamp,
      enrichments.0.value as GlobalResolverId,
      (response_time - query_time) as ResponseTime
| filter ispresent(response_time) and ispresent(query_time)
| stats pct(ResponseTime, 90) as P90ResponseTime by GlobalResolverId
```

**Days until token expiry by Access Token**

```
fields @timestamp,
      enrichments.0.data.token_id as AccessTokenId,
      enrichments.0.data.token_ttl_days as DaysUntilExpiry
| filter ispresent(enrichments.0.data.token_ttl_days)
| stats latest(DaysUntilExpiry) by AccessTokenId
```