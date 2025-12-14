**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Log fields for protection pack (web ACL) traffic

The following list describes the possible log fields.

**action**

The terminating action that AWS WAF applied to the request. This indicates either allow, block, CAPTCHA, or challenge. The CAPTCHA and Challenge actions are terminating when the web request doesn't contain a valid token.

**args**

The query string.

**captchaResponse**

The CAPTCHA action status for the request, populated when a CAPTCHA action is applied to the request.
This field is populated for any CAPTCHA action, whether terminating or non-terminating.
If a request has the CAPTCHA action applied multiple times, this field is populated from the last time the action was applied.

The CAPTCHA action terminates web request inspection when the request either doesn't include a token or the token is invalid or expired.
If the CAPTCHA action is terminating, this field includes a response code and failure reason. If the action is non-terminating,
this field includes a solve timestamp. To differentiate between a terminating and non-terminating action, you can filter for
a non-empty `failureReason` attribute in this field.

**cfDistributionTenantId**

The identifier for the CloudFront distribution tenant associated with the web request.
This field is optional and only applies to protection packs (web ACLs) associated with CloudFront distribution tenants.

**challengeResponse**

The challenge action status for the request, populated when a Challenge action is applied to the request.
This field is populated for any Challenge action, whether terminating or non-terminating.
If a request has the Challenge action applied multiple times, this field is populated from the last time the action was applied.

The Challenge action terminates web request inspection when the request either doesn't include a token or the token is invalid or expired.
If the Challenge action is terminating, this field includes a response code and failure reason. If the action is non-terminating,
this field includes a solve timestamp. To differentiate between a terminating and non-terminating action, you can filter for
a non-empty `failureReason` attribute in this field.

**clientAsn**

The Autonomous System Number (ASN) associated with the IP address of the
web request's origin.

###### Note

**clientAsn** is logged in AWS WAF logs
only when an ASN match statement is used. This field is not logged
otherwise.

**clientIp**

The IP address of the client sending the request.

**country**

The source country of the request. If AWS WAF is unable to determine the
country of origin, it sets this field to `-`.

**country**

The source country of the request. If AWS WAF is unable to determine the
country of origin, it sets this field to `-`.

**excludedRules**

Used only for rule group rules. The list of rules in the rule group that you have excluded. The action for
these rules is set to Count.

If you override a rule to count using the override rule action option, matches aren't listed here. They're listed as the action pairs `action` and `overriddenAction`.

exclusionType

A type that indicates that the excluded rule has the action
Count.

ruleId

The ID of the rule within the rule group that is
excluded.

**formatVersion**

The format version for the log.

**forwardedAsn**

The Autonomous System Number (ASN) associated with the IP address of from the entity that forwarded the web request.

**headers**

The list of headers.

**httpMethod**

The HTTP method in the request.

**httpRequest**

The metadata about the request.

**httpSourceId**

The ID of the associated resource:

- For an Amazon CloudFront distribution, the ID is the `*distribution-id*` in the ARN syntax:

`arn:*partition*cloudfront::*account-id*:distribution/*distribution-id*`

- For an Application Load Balancer, the ID is the `*load-balancer-id*` in the ARN syntax:

`arn:*partition*:elasticloadbalancing:*region*:*account-id*:loadbalancer/app/*load-balancer-name*/*load-balancer-id*`

- For an Amazon API Gateway REST API, the ID is the `*api-id*` in the ARN syntax:

`arn:*partition*:apigateway:*region*::/restapis/*api-id*/stages/*stage-name*`

- For an AWS AppSync GraphQL API, the ID is the `*GraphQLApiId*` in the ARN syntax:

`arn:*partition*:appsync:*region*:*account-id*:apis/*GraphQLApiId*`

- For an Amazon Cognito user pool, the ID is the `*user-pool-id*` in the ARN syntax:

`arn:*partition*:cognito-idp:*region*:*account-id*:userpool/*user-pool-id*`

- For an AWS App Runner service, the ID is the `*apprunner-service-id*` in the ARN syntax:

`arn:*partition*:apprunner:*region*:*account-id*:service/*apprunner-service-name*/*apprunner-service-id*`

**httpSourceName**

The source of the request. Possible values: `CF` for Amazon CloudFront, `APIGW` for Amazon API Gateway, `ALB` for Application Load Balancer, `APPSYNC` for AWS AppSync, `COGNITOIDP` for Amazon Cognito, `APPRUNNER` for App Runner, and `VERIFIED_ACCESS` for Verified Access.

**httpVersion**

The HTTP version.

**ja3Fingerprint**

The JA3 fingerprint of the request.

###### Note

JA3 fingerprint inspection is available only for Amazon CloudFront distributions and Application Load Balancers.

The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. AWS WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation.

You provide this value when you configure a JA3 fingerprint match in your
protection pack (web ACL) rules. For information about creating a match against the JA3
fingerprint, see [JA3 fingerprint](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-ja3-fingerprint "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-ja3-fingerprint")
in the [Request components in AWS WAF](waf-rule-statement-fields-list.md "waf-rule-statement-fields-list.md") for a rule
statement.

**ja4Fingerprint**

The JA4 fingerprint of the request.

###### Note

JA4 fingerprint inspection is available only for Amazon CloudFront distributions and Application Load Balancers.

The JA4 fingerprint is a 36-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. AWS WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation.

You provide this value when you configure a JA4 fingerprint match in your
protection pack (web ACL) rules. For information about creating a match against the JA4
fingerprint, see [JA4 fingerprint](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-ja4-fingerprint "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-ja4-fingerprint")
in the [Request components in AWS WAF](waf-rule-statement-fields-list.md "waf-rule-statement-fields-list.md") for a rule
statement.

**labels**

The labels on the web request. These labels were applied by rules that
were used to evaluate the request. AWS WAF logs the first 100 labels.

**nonTerminatingMatchingRules**

The list of non-terminating rules that matched the request. Each item in the list contains the following information.

action

The action that AWS WAF applied to the request. This indicates either count, CAPTCHA, or challenge. The CAPTCHA and Challenge are
non-terminating when the web request contains a valid token.

ruleId

The ID of the rule that matched the
request and was non-terminating.

ruleMatchDetails

Detailed information about the rule that matched the request.
This field is only populated for SQL injection and cross-site
scripting (XSS) match rule statements. A matching rule might
require a match for more than one inspection criteria, so these match details
are provided as an array of match criteria.

Any additional information provided for each rule varies according factors such as the rule configuration, rule match type, and details of the match. For example for rules with a CAPTCHA or Challenge action, the `captchaResponse` or `challengeResponse` will be listed. If the matching rule is in a rule group and you've overridden its configured rule action, the configured action will be provided in `overriddenAction`.

**oversizeFields**

The list of fields in the web request that were inspected by the protection pack (web ACL)
and that are over the AWS WAF inspection limit. If a field is
oversize but the protection pack (web ACL) doesn't inspect it, it won't be listed here.

This list can contain zero or
more of the following values: `REQUEST_BODY`, `REQUEST_JSON_BODY`,
`REQUEST_HEADERS`, and `REQUEST_COOKIES`. For
more information about oversize fields, see [Oversize web request components
in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

**rateBasedRuleList**

The list of rate-based rules that acted on the request. For information
about rate-based rules, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md").

rateBasedRuleId

The ID of the rate-based rule that acted on the request. If
this has terminated the request, the ID for
`rateBasedRuleId` is the same as the ID for
`terminatingRuleId`.

rateBasedRuleName

The name of the rate-based rule that acted on the request.

limitKey

The type of aggregation that the rule is using. Possible
values are `IP` for web request origin,
`FORWARDED_IP` for an IP forwarded in a header in
the request, `CUSTOMKEYS` for custom aggregate key
settings. and `CONSTANT` for count all requests
together, with no aggregation.

limitValue

Used only when rate limiting by a single IP address type. If a
request contains an IP address that isn't valid, the
`limitvalue` is `INVALID`.

maxRateAllowed

The maximum number of requests allowed in the specified time
window for a specific aggregation instance. The aggregation
instance is defined by the `limitKey` plus any
additional key specifications that you've provided in the
rate-based rule configuration.

evaluationWindowSec

The amount of time that AWS WAF included in its request counts, in seconds.

customValues

Unique values identified by the rate-based rule in the
request. For string values, the logs print the first 32
characters of the string value. Depending on the key type, these
values might be for just a key, such as for HTTP method or query
string, or they might be for a key and name, such as for header
and the header name.

**requestHeadersInserted**

The list of headers inserted for custom request handling.

**requestId**

The ID of the request, which is generated by the underlying host service.
For Application Load Balancer, this is the trace ID. For all others, this is the request ID.

**responseCodeSent**

The response code sent with a custom response.

**ruleGroupId**

The ID of the rule group. If the rule blocked the request, the ID for
`ruleGroupID` is the same as the ID for
`terminatingRuleId`.

**ruleGroupList**

The list of rule groups that acted on this request, with match information.

**terminatingRule**

The rule that terminated the request. If this is present, it contains the following information.

action

The terminating action that AWS WAF applied to the request. This indicates either allow, block, CAPTCHA, or challenge. The CAPTCHA and Challenge actions are
terminating when the web request doesn't contain a valid token.

ruleId

The ID of the rule that matched the request.

ruleMatchDetails

Detailed information about the rule that matched the request.
This field is only populated for SQL injection and cross-site
scripting (XSS) match rule statements. A matching rule might
require a match for more than one inspection criteria, so these match details
are provided as an array of match criteria.

Any additional information provided for each rule varies according factors such as the rule configuration, rule match type, and details of the match. For example for rules with a CAPTCHA or Challenge action, the `captchaResponse` or `challengeResponse` will be listed. If the matching rule is in a rule group and you've overridden its configured rule action, the configured action will be provided in `overriddenAction`.

**terminatingRuleId**

The ID of the rule that terminated the request. If nothing terminates the
request, the value is `Default_Action`.

**terminatingRuleMatchDetails**

Detailed information about the terminating rule that matched the request. A terminating
rule has an action that ends the inspection process against a web request.
Possible actions for a terminating rule include Allow,
Block, CAPTCHA, and Challenge.
During the inspection of a web request, at the first rule that matches the request and that
has a terminating action, AWS WAF stops the inspection and applies the action.
The web request might contain other threats, in addition to the one that's reported in the log
for the matching terminating rule.

This is only populated for SQL injection and cross-site scripting (XSS) match rule
statements. The matching rule might
require a match for more than one inspection criteria, so these match details
are provided as an array of match criteria.

**terminatingRuleType**

The type of rule that terminated the request. Possible values: RATE_BASED,
REGULAR, GROUP, and MANAGED_RULE_GROUP.

**timestamp**

The timestamp in milliseconds.

**uri**

The URI of the request.

**fragment**

The part of a URL that follows the "#" symbol, providing additional information about the resource, for example, #section2.

**webaclId**

The GUID of the protection pack (web ACL).
