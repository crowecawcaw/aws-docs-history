**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Adjusting rule statement settings in AWS WAF

This section describes the settings that you can specify in rule statements that inspect a
component of the web request. For information on usage, see the individual rule
statements at [Using match rule statements in AWS WAF](waf-rule-statements-match.md "waf-rule-statements-match.md").

A subset of these web request components can also be used in rate-based rules, as custom request aggregation keys.
For information, see [Aggregating rate-based rules in AWS WAF](waf-rule-statement-type-rate-based-aggregation-options.md "waf-rule-statement-type-rate-based-aggregation-options.md").

For the request component settings, you specify the component type itself,
and any additional options, depending on the component type. For example, when
you inspect a component type that contains text, you can apply text transformations to it before inspecting it.

###### Note

Unless otherwise noted, if a web request doesn't have the request component
that's specified in the rule statement, AWS WAF evaluates the request as not matching the
rule criteria.

###### Contents

- [Request components in AWS WAF](waf-rule-statement-fields-list.md "waf-rule-statement-fields-list.md")
  - [HTTP
    method](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-http-method "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-http-method")
  - [Single
    header](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-single-header "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-single-header")
  - [All headers](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-headers "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-headers")
  - [Header order](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-header-order "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-header-order")
  - [Cookies](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-cookies "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-cookies")
  - [URI fragment](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-uri-fragment "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-uri-fragment")
  - [URI
    path](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-uri-path "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-uri-path")
  - [JA3 fingerprint](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-ja3-fingerprint "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-ja3-fingerprint")
  - [JA4 fingerprint](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-ja4-fingerprint "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-ja4-fingerprint")
  - [Query
    string](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-query-string "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-query-string")
  - [Single query parameter](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-single-query-param "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-single-query-param")
  - [All query parameters](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-all-query-params "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-all-query-params")
  - [Body](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-body "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-body")
  - [JSON body](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-json-body "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-json-body")

- [Using forwarded IP
  addresses in AWS WAF](waf-rule-statement-forwarded-ip-address.md "waf-rule-statement-forwarded-ip-address.md")
- [Inspecting HTTP/2 pseudo headers in AWS WAF](waf-rule-statement-request-components-for-http2-pseudo-headers.md "waf-rule-statement-request-components-for-http2-pseudo-headers.md")
- [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md")
