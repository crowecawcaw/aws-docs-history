

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Dynamic label interpolation
<a name="waf-dynamic-label-interpolation"></a>

Dynamic label interpolation lets you embed label values directly in custom request headers, custom response headers, and custom response bodies using `${namespace:}` syntax. AWS WAF resolves each placeholder at evaluation time against the labels attached to the request, so you don't have to write a separate rule for each label value.

Interpolation works within the existing AWS WAF API with no new fields or configuration steps. You use the placeholder syntax in your existing string values. Existing static header values continue to work unchanged. Interpolation only activates when a value contains `${namespace:}` clauses.

## Where interpolation is supported
<a name="waf-interpolation-where-supported"></a>

You can use `${namespace:}` interpolation in the following locations:
+ **Custom request headers** – Insert resolved label values into headers forwarded to your origin. Use the `${namespace:}` syntax in the header value field.
+ **Custom response bodies** – Embed label values and synthetic labels in block pages, challenge pages, and other custom responses. Use the `${namespace:}` syntax in the response body content field.
+ **Custom response headers** – Insert label values into response headers, for example in a `Location` header for redirects. Use the `${namespace:}` syntax in the response header value field.

## Interpolation syntax and resolution
<a name="waf-interpolation-syntax"></a>

To use interpolation, include `${namespace:}` clauses in your header values or custom response body content. The trailing colon is significant. It tells AWS WAF to resolve all labels within that namespace rather than match a single label literally.

AWS WAF resolves each clause at evaluation time using the following rules:

1. **Single label match** – The clause resolves to the label's terminal value. For example, if the request has the label `awswaf:managed:aws:bot-control:bot:category:scraping`, the clause `${awswaf:managed:aws:bot-control:bot:category:}` resolves to `scraping`.

1. **Multiple labels** – When multiple labels match the namespace, values are returned as a comma-separated list with the namespace prefix stripped. For example, `scraping,advertising`.

1. **No match** – The clause resolves to an empty string.

**Note**  
A single string value supports up to 10 `${namespace:}` placeholders. If a value contains more than 10 placeholders, AWS WAF resolves the first 10 and leaves any additional placeholders in the output as literal `${namespace:}` text. This limit applies for each string value, not for each request. You can use up to 10 placeholders in each of multiple headers without issue.

**Important**  
Custom labels use a short name in `ruleLabels`. For example, `app:tier:enterprise`. However, AWS WAF automatically prefixes the short name with the protection pack (web ACL) context, producing a fully-qualified label. For example, `awswaf:{{ACCOUNT_ID}}:webacl:{{WEBACL_NAME}}:app:tier:enterprise`. The label match statement works with the short namespace, but interpolation references must always use the fully-qualified namespace.

## Synthetic labels
<a name="waf-interpolation-synthetic-labels"></a>

Interpolation also supports synthetic labels. These are built-in values that AWS WAF resolves from the request context rather than from the label store. You can combine synthetic labels with namespace-based labels in the same value string.


| Synthetic label | Description | 
| --- | --- | 
| ${awswaf:request\_id:} | The unique AWS WAF request identifier. | 
| ${awswaf:ip:} | The client IP address. | 
| ${awswaf:ja3:} | The JA3 TLS fingerprint. | 
| ${awswaf:ja4:} | The JA4 TLS fingerprint. | 

## Dynamic label interpolation examples
<a name="waf-interpolation-examples"></a>

**Application signaling with dynamic headers**  
The following rule forwards several Bot Control signal namespaces to your origin as separate headers. One rule covers the whole namespace, so you don't need to update the rule when the managed rule group adds new labels.

```
{
  "Name": "forward-waf-signals",
  "Statement": {
    "LabelMatchStatement": {
      "Scope": "NAMESPACE",
      "Key": "awswaf:managed:aws:bot-control:bot:category:"
    }
  },
  "RuleAction": {
    "Count": {
      "CustomRequestHandling": {
        "InsertHeaders": [
          { "Name": "bot-category",
            "Value": "${awswaf:managed:aws:bot-control:bot:category:}" },
          { "Name": "bot-name",
            "Value": "${awswaf:managed:aws:bot-control:bot:name:}" },
          { "Name": "bot-signals",
            "Value": "${awswaf:managed:aws:bot-control:signal:}" },
          { "Name": "client-ip",
            "Value": "${awswaf:ip:}" }
        ]
      }
    }
  }
}
```

The `bot-signals` header (output: `x-amzn-waf-bot-signals`) demonstrates multi-value resolution. The `signal:` namespace may contain multiple labels, for example `non_browser_user_agent,automated_browser`, which resolve to a comma-separated list. The `client-ip` header (output: `x-amzn-waf-client-ip`) uses a synthetic label.

**Custom block page with debug information**  
Synthetic labels let you build block pages that include request-specific context. Embed the client's IP address and the AWS WAF request ID directly in the response body to give users something to share when they report a false positive.

```
{
  "CustomResponseBodies": {
    "BlockPage": {
      "Content": "Your request was blocked.\n\nIP: ${awswaf:ip:}\nRequest ID: ${awswaf:request_id:}\n\nIf you believe this is an error, contact support with the Request ID above.",
      "ContentType": "TEXT_PLAIN"
    }
  }
}
```

**Custom label interpolation**  
Interpolation works with any label namespace, including custom labels that you define in your own rules. The following example classifies requests by API key and forwards the tier value to the origin.

**Rule 1: Classify tier based on API key**  
This rule matches requests with an enterprise API key and applies a custom label.

```
{
{
  "Name": "classify-tier",
  "Priority": 100,
  "Statement": {
    "ByteMatchStatement": {
      "SearchString": "pk_enterprise_",
      "FieldToMatch": { "SingleHeader": { "Name": "x-api-key" } },
      "PositionalConstraint": "STARTS_WITH",
      "TextTransformations": [{ "Priority": 0, "Type": "NONE" }]
    }
  },
  "RuleLabels": [{ "Name": "app:tier:enterprise" }],
  "Action": { "Count": {} }
}

}
```

**Rule 2: Forward the resolved tier value**  
This rule matches any label in the `app:tier` namespace and forwards the resolved value as a header.

```
{
{
  "Name": "forward-tier",
  "Priority": 200,
  "Statement": {
    "LabelMatchStatement": {
      "Scope": "NAMESPACE",
      "Key": "app:tier:"
    }
  },
  "Action": {
    "Count": {
      "CustomRequestHandling": {
        "InsertHeaders": [{
          "Name": "customer-tier",
          "Value": "${awswaf:{{ACCOUNT_ID}}:webacl:{{WEBACL_NAME}}:app:tier:}"
        }]
      }
    }
  }
}
```

The first rule applies the label `app:tier:enterprise`. The second rule matches any label in the `app:tier` namespace and forwards the resolved value as the `customer-tier` header. The output header name is `x-amzn-waf-customer-tier`. You can add more classification rules for other tiers, such as `app:tier:standard` or `app:tier:trial`. The forwarding rule picks them up without any changes.

For a deployable sample that demonstrates all of these patterns, see the [AWS WAF Dynamic Label Interpolation sample](https://github.com/aws-samples/sample-aws-waf-dynamic-labels) on GitHub.