# Routing rules to connect API stages to a custom domain name for REST APIs

A routing rule is a set of conditions that when matched, invoke an action. For example, a rule can route any
incoming request to a custom domain name that contains the header `Hello:World` and contains the base
path `users` to the `production` stage of a REST API.

Rules are evaluated in priority order,
and if you set the routing mode to `ROUTING_RULE_THEN_API_MAPPING`, API Gateway always evaluates all routing
rules before evaluating any API mappings. The following list describes how a routing rule uses conditions, actions,
and priorities.

**Conditions**

When the conditions for a rule are met, then its actions are performed. API Gateway supports up to two header
conditions and one path condition. API Gateway evaluates header conditions and base path conditions together.

You can create a rule without any conditions. When API Gateway evaluates this rule, the
action is always performed. You can create a rule without any conditions as a catch-all rule.

For more information about header conditions, see [Match headers conditions](#rest-api-routing-rules-condition-headers "#rest-api-routing-rules-condition-headers"). For more information about path conditions, see [Match base path conditions](#rest-api-routing-rules-condition-path "#rest-api-routing-rules-condition-path").

**Actions**

Actions are the result of matching conditions to a routing rule. Currently, the only supported action is
to invoke a stage of a REST API.

Each rule can have one action.

**Priority**

The priority determines what order the rules are evaluated in, from the lowest value to the highest
value. Rules can't have the same priority.

You can set the priority from 1-1,000,000. If a rule has a priority of one, API Gateway evaluates it first. We
recommend that when you create a rule, you add gaps in priorities. This helps you switch the priority of rules
and add new rules. For more information, see [Change the priority of a routing rule](apigateway-routing-rules-use.md#rest-api-routing-rules-change-priority "apigateway-routing-rules-use.md#rest-api-routing-rules-change-priority").

For examples of how API Gateway evaluates routing rules, see [Examples of how API Gateway evaluates routing rules](rest-api-routing-rules-examples.md "rest-api-routing-rules-examples.md").

## API Gateway routing rule condition types

The following section describes the routing rule condition types. API Gateway only matches a rule if all conditions
are true.

### Match headers conditions

When you create a header condition, you can match the header name and header glob value, such as
`Hello:World`. API Gateway uses a literal match to validate match headers conditions. Your
condition can use up to two headers using `AND` between them. For example, your condition can match
if an incoming request contains `Hello:World` and `x-version:beta`.

The header name matching is case insensitive, but the
header glob value is case sensitive. `Hello:World` will match `hello:World`, but
not `Hello:world`.

For a list of restricted header values see, [Restrictions](#rest-api-routing-rules-restrictions "#rest-api-routing-rules-restrictions").

#### Using wildcards with header conditions

You can only use wildcards in the header glob value, and the wildcard must be `*prefix-match`,
`suffix-match*`, or `*contains*`. The following table shows examples for how to use
wildcards for matching for header conditions.

| Header conditions
| Requests that match the routing rule
| Requests that don't match the routing rule
|
| --- | --- | --- |
| `x-version: a*` | <br>• `x-version: account` <br>• `x-version: alpha` | <br>• `x-version: backup` <br>• `x-version: beta` <br>• `x-version: users` |
| `x-version: *a` | <br>• `x-version: alpha` <br>• `x-version: beta` | <br>• `x-version: account` <br>• `x-version: backup` <br>• `x-version: users` |
| `x-version: *a*` | <br>• `x-version: account` <br>• `x-version: alpha` <br>• `x-version: backup` <br>• `x-version: beta` | <br>• `x-version: users` |
| `x-version: *a*` and `x-version: *b*` | <br>• `x-version: backup` <br>• `x-version: beta` | <br>• `x-version: account` <br>• `x-version: alpha` <br>• `x-version: users` |
| `x-version: b*` and `x-version: *a` | <br>• `x-version: beta` | <br>• `x-version: account` <br>• `x-version: alpha` <br>• `x-version: backup` <br>• `x-version: users` |
| `x-version: *` | <br>• `x-version: account` <br>• `x-version: alpha` <br>• `x-version: backup` <br>• `x-version: beta` <br>• `x-version: users` | None | If you create conditions for multiple header values, such as `Accept:application/json,text/xml`, we recommend that you use `*contains*` for your header conditions and avoid creating conditions using the comma (`,`) character. Because API Gateway matches header conditions literally, semantic matches might be routed differently. The following table shows the difference in routing rules outcomes.
| Header conditions | Requests that match the routing rule | Requests that don't match the routing rule |
| --- | --- | --- |
| `Accept: *json` | <br>• `Accept:application/json Accept:text/xml` | <br>• `Accept:application/json,text/xml` |
| `Accept: *json*` | <br>• `Accept:application/json Accept:text/xml` <br>• `Accept:application/json,text/xml` | None | ### Match base path conditions When you create a base path condition, if the incoming request contains the path you specified, the rule is matched. The matching is case sensitive, so the path `New/Users` will not match with `new/users`. You can create a base path condition for only one base path. For a list of restricted base path conditions, [Restrictions](#rest-api-routing-rules-restrictions "#rest-api-routing-rules-restrictions"). #### Strip the base path with base path conditions When you create a base path condition, you can choose to strip the base path. When you strip the base path, API Gateway removes the incoming matched base path when it invokes the target API. This is the same behavior as when you use an API mapping. When you don't strip the base path, API Gateway forwards the entire base path to the target API. We recommend that you only strip the base path when you are recreating an API mapping. The following table shows examples for how API Gateway evaluates the strip base path condition.
| Condition | Strip base path | Incoming request | Result
|
| --- | --- | --- | --- |
| If base path contains `PetStoreShopper/dogs` | True | `GET https://example.com/PetStoreShopper/dogs` | API Gateway calls the `GET` method of the `/` resource. |
| If base path contains `PetStoreShopper/dogs`. | False | `GET https://example.com/PetStoreShopper/dogs` | API Gateway calls the `GET` method of the `PetStoreShopper/dogs` resource. |
| If base path contains `PetStoreShopper` | True | `GET https://example.com/PetStoreShopper/dogs` | API Gateway calls the `GET` method of the `dogs` resource. |
| If base path contains `PetStoreShopper` | False | `GET https://example.com/PetStoreShopper/dogs` | API Gateway calls the `GET` method of the `PetStoreShopper/dogs` resource. |
| If base path contains `PetStoreShopper` | True | `GET https://example.com/PetStoreShopper?birds=available` | API Gateway calls the `GET` method of the `/` resource with the query string parameter `birds=available`. |
| If base path contains `PetStoreShopper` | False | `GET https://example.com/PetStoreShopper?birds=available` | API Gateway calls the `GET` method of the `/PetStoreShopper` resource with the query string parameter `birds=available`. | ## Restrictions <br>• The target API and the custom domain name must be in the same AWS account. <br>• Each rule can have one target API. <br>• You can only create a routing rule for a private custom domain name to a private API, and for a public custom domain name to a public API. You can't mix public and private resources. <br>• If your custom domain name has API mappings to both REST and HTTP APIs, routing rules isn't supported. <br>• The maximum priority number is 1,000,000. <br>• Header restrictions: + Each `anyOf` condition can only contain one header value. + The only allowed characters for header names and header glob values are specified by [RFC 7230](https://datatracker.ietf.org/doc/html/rfc7230 "https://datatracker.ietf.org/doc/html/rfc7230"), which are `a-z`, `A-Z`, `0-9`, and the following special characters: `*?-!#$%&'.^_`|~`. + You can use a wildcard in the header glob value, but the wildcard must be `_prefix-match`, `suffix-match_`, or `_contains_`. You can't use `_`in the middle of a header glob value. + Wildcard header names aren't supported. + The header name must be less than 40 characters. + The header glob value must be less than 128 characters. + The header glob value for an infix match must be less than 40 characters. + The following headers aren't supported as conditions: <br>•`access-control-_`<br>•`apigw-_`<br>•`Authorization`<br>•`Connection`<br>•`Content-Encoding`<br>•`Content-Length`<br>•`Content-Location`<br>•`Forwarded`<br>•`Keep-Alive`<br>•`Origin`<br>•`Proxy-Authenticate`<br>•`Proxy-Authorization`<br>•`TE`<br>•`Trailers`<br>•`Transfer-Encoding`<br>•`Upgrade`<br>•`x-amz-_`<br>•`x-amzn-_`<br>•`x-apigw-api-id`<br>•`X-Forwarded-For`<br>•`X-Forwarded-Host`<br>•`X-Forwarded-Proto`<br>•`x-restAPI`<br>•`Via`<br>• Base path restrictions: + The base path length must be less than 128 characters. + The base path must contain only letters, numbers, and the following characters:`$-\_.+!_'()/`. These characters aren't supported for regular expressions (regex). + The base path can't start or end with backslash (`\`) character.
