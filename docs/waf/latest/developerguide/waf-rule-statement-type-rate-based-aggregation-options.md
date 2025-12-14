**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Aggregating rate-based rules in AWS WAF

This section explains your options for aggregating requests.

By default, a rate-based rule aggregates and rate limits requests based on the request IP address.
You can configure the rule to use various other aggregation
keys and key combinations. For example, you can aggregate based on a forwarded IP address,
on the HTTP method, or on a query argument. You
can also specify aggregation key combinations, such as IP address and HTTP method, or
the values of two different cookies.

###### Note

All of the request components that you specify in the aggregation key must be present in a web request for the request to be evaluated or rate limited by the rule.

You can configure your rate-based rule with the following aggregation options.

- **Source IP address** – Aggregate using only the IP
  address from the web request origin.

The source IP address might not contain the address of the originating client. If a web request goes through one or
more proxies or load balancers, this will contain the address of the last
proxy.

- **IP address in header** – Aggregate using only a client
  address in an HTTP header. This is also referred to as a forwarded IP address.

With this configuration, you also specify a fallback behavior to apply to
a web request with a malformed IP address in the header. The fallback
behavior sets the matching result for the request, to match or no match. For
no match, the rate-based rule doesn't count or rate limit the request. For
match, the rate-based rule groups the request together with other requests
that have a malformed IP address in the specified header.

Use caution with this option, because headers can be handled inconsistently by proxies
and they can also be modified to bypass inspection. For additional
information and best practices, see [Using forwarded IP
addresses in AWS WAF](waf-rule-statement-forwarded-ip-address.md "waf-rule-statement-forwarded-ip-address.md").

- **ASN** – Aggregate using an
  Autonomous System Number (ASN) associated with the source IP address as an
  aggregate key. This might not be the address of the originating client. If a
  web request goes through one or more proxies or load balancers, this
  contains the address of the last proxy.

If AWS WAF can’t derive an ASN from the IP address, it counts the ASN as ASN 0. If you don't want to apply rate limiting to unmapped ASNs, you can create
a scope-down rule that excludes requests with ASN 0.

- **ASN in header** – Aggregate using an
  ASN associated with a client IP address in an HTTP header. This is also
  referred to as a forwarded IP address. With this configuration, you also
  specify a fallback behavior to apply to a web request with an invalid or
  malformed IP address. The fallback behavior sets the matching result for the
  request, to match or no match. If you set the fallback behavior to match in
  the forwarded IP configuration, AWS WAF treats the invalid IP address as a
  matching value. This allows AWS WAF to continue evaluating any remaining parts
  of your rate-based rule's composite key. For no match, the rate-based rule
  doesn't count or rate limit the request.

Use caution with this option, as headers can be handled inconsistently by
proxies and they can be modified to bypass inspection. For additional
information and best practices, see [Using forwarded IP
addresses in AWS WAF](waf-rule-statement-forwarded-ip-address.md "waf-rule-statement-forwarded-ip-address.md").

- **Count all** – Count and rate limit all requests that match the rule's scope-down statement. This option requires a scope-down statement. This is typically used to rate limit a specific set of requests, such as all requests with a specific label or all requests from a specific geographic area.
- **Custom keys** – Aggregate using one or more custom
  aggregation keys. To combine either of the IP address options with other
  aggregation keys, define them here under custom keys.

Custom aggregation keys are a subset of the web request component options described at [Request components in AWS WAF](waf-rule-statement-fields-list.md "waf-rule-statement-fields-list.md").

The key options are the following. Except where noted, you can use an option multiple times, for example, two headers or three label namespaces.

    + **Label namespace** – Use a label namespace as an aggregation key. Each distinct fully qualified label name that has the specified label namespace contributes to the aggregation instance. If you use just one label namespace as your custom key, then each label name fully defines an aggregation instance.


    The rate-based rule uses only labels that have been added to the request by rules that are evaluated beforehand in the protection pack (web ACL).


    For information about label namespaces and names, see [Label syntax and naming requirements in AWS WAF](waf-rule-label-requirements.md "waf-rule-label-requirements.md").
    + **Header** – Use a named header
     as an aggregation key. Each distinct value in the header contributes to the aggregation instance.


    Header takes an optional text transformation. See [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").
    + **Cookie** – Use a named cookie
     as an aggregation key. Each distinct value in the cookie contributes to the aggregation instance.


    Cookie takes an optional text transformation. See [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").
    + **Query argument** – Use a single query argument in the request as an aggregate key. Each distinct value for the named query argument contributes to the aggregation instance.


    Query argument takes an optional text transformation. See [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").
    + **Query string** – Use the entire query string in the request as an aggregate key. Each distinct query string contributes to the aggregation instance. You can use this key type once.


    Query string takes an optional text transformation. See [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").
    + **URI path** – Use the URI
     path in the request as an aggregate key. Each distinct URI path
     contributes to the aggregation instance. You can use this key type
     once.


    URI path takes an optional text transformation. See [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").
    + **JA3 fingerprint** – Use the JA3
     fingerprint in the request as an aggregate key. Each distinct JA3
     fingerprint contributes to the aggregation instance. You can use this key type once.
    + **JA4 fingerprint** – Use the JA4
     fingerprint in the request as an aggregate key. Each distinct JA4
     fingerprint contributes to the aggregation instance. You can use this key type once.
    + **HTTP method** – Use the request's HTTP method as an aggregate key. Each distinct HTTP method contributes to the aggregation instance. You can use this key type once.
    + **IP address** – Aggregate using the IP
     address from the web request origin in combination with other keys.


    This might not contain the address of the originating client. If a web request goes through one or
     more proxies or load balancers, this will contain the address of the last
     proxy.
    + **IP address in header** – Aggregate using the client
     address in an HTTP header in combination with other keys. This is also referred to as a forwarded IP address.


    Use caution with this option, as headers can be
     handled inconsistently by proxies and they can be modified to bypass
     inspection. For additional information and best practices, see [Using forwarded IP
     addresses in AWS WAF](waf-rule-statement-forwarded-ip-address.md "waf-rule-statement-forwarded-ip-address.md").
