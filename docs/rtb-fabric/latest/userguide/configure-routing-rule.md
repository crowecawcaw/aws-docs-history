

# Configuring routing rules
<a name="configure-routing-rule"></a>

Routing rules determine how RTB Fabric maps incoming HTTP requests to links. Each rule specifies conditions that a request must satisfy. When a request arrives at the gateway, RTB Fabric evaluates rules across all links and forwards the request to the link whose highest-priority matching rule wins.

## Routing rule structure
<a name="routing-rule-structure"></a>

You create routing rules using the CreateLinkRoutingRule API. Each rule consists of a numeric priority and a set of conditions. The `ruleId` is system-generated.

```
{
  "gatewayId": "rtb-gw-abc123def456",
  "linkId": "link-001",
  "priority": 1,
  "conditions": {
    "hostHeader": "bid.example.com",
    "pathPrefix": "/openrtb"
  },
  "clientToken": "unique-idempotency-token"
}
```


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| gatewayId | String | Yes | The responder gateway that owns the link. | 
| linkId | String | Yes | The link to attach the rule to. | 
| priority | Integer (1-1000) | Yes | Evaluation priority. Lower values indicate higher precedence. Must be unique within a link. | 
| conditions | Object | Yes | One or more match conditions. At least one condition must be specified. | 
| clientToken | String | Yes | Idempotency token. | 

The response includes a system-generated `ruleId` (pattern: `rule-[a-z0-9-]+`) and a `status` field. Use the GetLinkRoutingRule API to check when the rule reaches `ACTIVE` status.

## Supported match types
<a name="supported-match-types"></a>

RTB Fabric supports six match types. All conditions within a single rule use AND logic — every specified condition must match for the rule to apply.

### Host header exact match (`hostHeader`)
<a name="host-header-exact-match"></a>

Matches the `Host` header of the incoming request against an exact hostname value.
+ **Comparison:** Case-insensitive, per RFC 7230 Section 5.4.
+ **Port stripping:** The port component is stripped before comparison. A request to `bid.example.com:443` matches a rule with `hostHeader` set to `bid.example.com`.
+ **IPv6 handling:** Bracket-enclosed IPv6 addresses are handled correctly. A request with `Host: [::1]:8080` is matched against `[::1]` after port stripping.

**Example:**

```
{
  "conditions": {
    "hostHeader": "east-bid.dsp.example.com"
  }
}
```

This condition matches requests with `Host: east-bid.dsp.example.com`, `Host: East-Bid.DSP.Example.com`, and `Host: east-bid.dsp.example.com:443`.

### Host header wildcard match (`hostHeaderWildcard`)
<a name="host-header-wildcard-match"></a>

Matches the `Host` header against a wildcard pattern. The `hostHeader` and `hostHeaderWildcard` conditions are mutually exclusive — a single rule cannot contain both.
+ **Syntax:** The wildcard character `*` replaces exactly one DNS label (single-level matching), per RFC 6125 Section 6.4.3.
+ **Comparison:** Case-insensitive, port-stripped.
+ **Restrictions:** The pattern `*.example.com` matches `api.example.com` but does not match `a.b.example.com` (multi-level) or `example.com` (the parent domain itself).

**Example:**

```
{
  "conditions": {
    "hostHeaderWildcard": "*.dsp.example.com"
  }
}
```


| Incoming Host | Matches? | 
| --- | --- | 
| east-bid.dsp.example.com | Yes | 
| west-bid.dsp.example.com | Yes | 
| a.b.dsp.example.com | No (multi-level) | 
| dsp.example.com | No (parent domain) | 

### Path prefix match (`pathPrefix`)
<a name="path-prefix-match"></a>

Matches the URL path against a prefix value with segment-boundary awareness.
+ **Segment-boundary matching:** The prefix `/api` matches `/api`, `/api/`, and `/api/users`, but does not match `/api2` or `/apiary`. The match verifies that the character immediately following the prefix is either `/`, end-of-path, or the prefix itself ends with `/`.
+ **Trailing slash normalization:** `/api` and `/api/` are equivalent as prefix values.

**Example:**

```
{
  "conditions": {
    "pathPrefix": "/openrtb/bid"
  }
}
```


| Incoming path | Matches? | 
| --- | --- | 
| /openrtb/bid | Yes | 
| /openrtb/bid/ | Yes | 
| /openrtb/bid/v2 | Yes | 
| /openrtb/bidstream | No (not a segment boundary) | 
| /openrtb | No (prefix is longer than the path) | 

### Path exact match (`pathExact`)
<a name="path-exact-match"></a>

Matches the URL path using a byte-for-byte comparison. The `pathPrefix` and `pathExact` conditions are mutually exclusive — a single rule cannot contain both.
+ **Case sensitivity:** The comparison is case-sensitive. `/OpenRTB/Bid` does not match `/openrtb/bid`.
+ **No percent-decoding:** Percent-encoded characters are compared as-is. `/path%2Fto` does not match `/path/to`.
+ **Trailing slash significance:** `/openrtb/bid` and `/openrtb/bid/` are different paths.

**Example:**

```
{
  "conditions": {
    "pathExact": "/openrtb/bid/v2"
  }
}
```

### Query string equals match (`queryStringEquals`)
<a name="query-string-equals-match"></a>

Matches a specific query string key-value pair.
+ **URL decoding:** Both the key and value are URL-decoded before comparison. A query parameter `format=json` matches regardless of whether the URL contains `format=json` or `format%3Djson` in the encoded form.
+ **Case sensitivity:** After URL decoding, comparison is case-sensitive.

**Example:**

```
{
  "conditions": {
    "queryStringEquals": {
      "key": "format",
      "value": "json"
    }
  }
}
```

A request to `/bid?format=json` matches. A request to `/bid?format=XML` does not match (case-sensitive value comparison).

**Important**  
Each rule supports at most one `queryStringEquals` condition. The `queryStringEquals` and `queryStringExists` conditions are mutually exclusive — a single rule cannot contain both. To match on multiple query parameters, create separate rules with appropriate priorities.

### Query string exists match (`queryStringExists`)
<a name="query-string-exists-match"></a>

Checks whether a specific query string key is present, regardless of its value.
+ **URL decoding:** The key is URL-decoded before the presence check.
+ **Case sensitivity:** After URL decoding, the key comparison is case-sensitive.

**Example:**

```
{
  "conditions": {
    "queryStringExists": "debug"
  }
}
```

A request to `/bid?debug=true` matches. A request to `/bid?debug` (key present with no value) also matches. A request to `/bid?Debug=true` does not match (case-sensitive key).

**Important**  
Each rule supports at most one `queryStringExists` condition. The `queryStringExists` and `queryStringEquals` conditions are mutually exclusive — a single rule cannot contain both.

## Composite rules
<a name="composite-rules"></a>

All conditions within a single rule are combined with AND logic. A request must satisfy every specified condition for the rule to match.

The following rule matches requests that meet all three criteria simultaneously:

```
{
  "gatewayId": "rtb-gw-abc123def456",
  "linkId": "link-001",
  "priority": 10,
  "conditions": {
    "hostHeader": "bid.example.com",
    "pathPrefix": "/openrtb/bid",
    "queryStringEquals": {
      "key": "format",
      "value": "json"
    }
  },
  "clientToken": "unique-idempotency-token"
}
```

A request to `https://bid.example.com/openrtb/bid/v2?format=json` matches this rule. A request to `https://bid.example.com/openrtb/bid/v2?format=xml` does not match because the `queryStringEquals` condition fails.

**Note**  
There is no OR logic within a single rule. To express OR conditions, create multiple rules with different priorities.

## Rule evaluation order
<a name="rule-evaluation-order"></a>

RTB Fabric evaluates routing rules globally across all links, not per-link. The evaluation follows this process:

1. **Flatten** — Collect all routing rules from all links on the gateway.

1. **Sort** — Sort rules by `priority` in ascending order (lower values first).

1. **Evaluate** — Iterate through sorted rules. The first rule whose conditions all match the incoming request wins.

1. **Resolve** — Forward the request to the link that owns the winning rule.

Priority must be unique within each link. Across different links, rules may share the same priority value. If two rules from different links have the same priority and both match, the result is non-deterministic. Assign distinct priority values across all links to avoid ambiguous routing.

### Example: Interleaved priorities across links
<a name="example-interleaved-priorities"></a>

Consider two links with the following rules:

Link A (`link-east`) has two rules with priorities 1 and 3:


| Rule | Priority | Conditions | 
| --- | --- | --- | 
| rule-east-openrtb | 1 | hostHeader: east-bid.example.com, pathPrefix: /openrtb | 
| rule-east-native | 3 | hostHeader: east-bid.example.com, pathPrefix: /native | 

Link B (`link-west`) has two rules with priorities 2 and 4:


| Rule | Priority | Conditions | 
| --- | --- | --- | 
| rule-west-openrtb | 2 | hostHeader: west-bid.example.com, pathPrefix: /openrtb | 
| rule-west-native | 4 | hostHeader: west-bid.example.com, pathPrefix: /native | 

The global evaluation order is: `rule-east-openrtb` (1) → `rule-west-openrtb` (2) → `rule-east-native` (3) → `rule-west-native` (4).

A request to `https://west-bid.example.com/openrtb/bid` skips `rule-east-openrtb` (host mismatch), matches `rule-west-openrtb` (priority 2), and routes to `link-west`.

## Link ID resolution chain
<a name="link-id-resolution-chain"></a>

When a request arrives at the gateway, RTB Fabric resolves the target link using a three-step resolution chain. Rule-based routing is the final step in this chain:

1. **URL extraction** — Check if the request URL contains an explicit link ID.

1. **Host header extraction** — Check if the Host header maps directly to a link.

1. **Rule-based routing** — Evaluate routing rules to determine the target link.

RTB Fabric uses the first method that returns a result. Rule-based routing applies only when the first two methods do not resolve a link ID.

## Example: Multi-partner routing
<a name="example-multi-partner-routing"></a>

The following example demonstrates routing for a partner (AnyCompany) with multiple regional endpoints and path-based traffic segmentation.

AnyCompany operates four combinations of region and traffic type:


| Endpoint | Path | Traffic type | Link ID | 
| --- | --- | --- | --- | 
| east-bid.dsp.example.com | /openrtb/bid | OpenRTB (East) | link-anyco-east-openrtb | 
| east-bid.dsp.example.com | /native/bid | Native (East) | link-anyco-east-native | 
| west-bid.dsp.example.com | /openrtb/bid | OpenRTB (West) | link-anyco-west-openrtb | 
| west-bid.dsp.example.com | /native/bid | Native (West) | link-anyco-west-native | 

**Rule on link 1 (`link-anyco-east-openrtb`):**

```
{
  "gatewayId": "rtb-gw-abc123def456",
  "linkId": "link-anyco-east-openrtb",
  "priority": 1,
  "conditions": {
    "hostHeader": "east-bid.dsp.example.com",
    "pathPrefix": "/openrtb"
  },
  "clientToken": "token-east-openrtb"
}
```

**Rule on link 2 (`link-anyco-east-native`):**

```
{
  "gatewayId": "rtb-gw-abc123def456",
  "linkId": "link-anyco-east-native",
  "priority": 2,
  "conditions": {
    "hostHeader": "east-bid.dsp.example.com",
    "pathPrefix": "/native"
  },
  "clientToken": "token-east-native"
}
```

**Rule on link 3 (`link-anyco-west-openrtb`):**

```
{
  "gatewayId": "rtb-gw-abc123def456",
  "linkId": "link-anyco-west-openrtb",
  "priority": 3,
  "conditions": {
    "hostHeader": "west-bid.dsp.example.com",
    "pathPrefix": "/openrtb"
  },
  "clientToken": "token-west-openrtb"
}
```

**Rule on link 4 (`link-anyco-west-native`):**

```
{
  "gatewayId": "rtb-gw-abc123def456",
  "linkId": "link-anyco-west-native",
  "priority": 4,
  "conditions": {
    "hostHeader": "west-bid.dsp.example.com",
    "pathPrefix": "/native"
  },
  "clientToken": "token-west-native"
}
```

With this configuration:
+ A request to `https://east-bid.dsp.example.com/openrtb/bid` routes to `link-anyco-east-openrtb` (priority 1).
+ A request to `https://east-bid.dsp.example.com/native/bid` routes to `link-anyco-east-native` (priority 2).
+ A request to `https://west-bid.dsp.example.com/openrtb/bid` routes to `link-anyco-west-openrtb` (priority 3).
+ A request to `https://west-bid.dsp.example.com/native/bid` routes to `link-anyco-west-native` (priority 4).

**Note**  
Because each rule combines a distinct `hostHeader` and `pathPrefix`, the priority ordering in this example affects evaluation performance but not correctness — only one rule can match any given request. Assign lower priority values to higher-traffic routes for faster evaluation.

## Testing routing rules with `/resolve-link`
<a name="testing-routing-rules-resolve-link"></a>

The gateway exposes a `/resolve-link` endpoint that evaluates your routing rules against a given URL without sending actual traffic. Use this endpoint to verify that rules are configured correctly before migrating DNS.

**Request:** GET /resolve-link?url=<url-encoded-value>

The `url` query parameter must be a fully qualified, URL-encoded URL (including scheme, host, path, and optional query string).

**Responses:**


| Status | Meaning | Response body | 
| --- | --- | --- | 
| 200 | A routing rule matched | {"link\_id": "link-abc123", "rule\_id": "rule-xyz789"} | 
| 404 | No routing rule matched | {"message": "No routing rules matched the provided URL"} | 
| 400 | Missing or invalid input | {"message": "Missing or invalid 'url' query parameter"} | 

**Example:**

```
curl "https://<GATEWAY_ENDPOINT>/resolve-link?url=https%3A%2F%2Fbid.example.com%2Fopenrtb%2Fbid"
```

A successful match returns the `link_id` and `rule_id` of the first matching rule:

```
{"link_id": "link-abc123", "rule_id": "rule-xyz789"}
```

**Note**  
The `/resolve-link` endpoint evaluates rules in the same global priority order as live traffic. A 404 response indicates that no rule matches — review your rule conditions and priorities. See Troubleshooting inbound external links with custom domains if requests return unexpected results.