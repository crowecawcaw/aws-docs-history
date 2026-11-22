

# Web bot records

Web bot is a record type for an agent that cryptographically signs its outbound web requests. This topic describes the Web bot record type and its conceptual relationship to AWS WAF. It does not cover the end-to-end request-enforcement experience, which is documented separately.

## What a Web bot record is
<a name="registry-web-bot-what-is"></a>

A Web bot record represents a signed-request bot identity. The agent signs its outbound HTTP requests with its private key and publishes the corresponding public key so that content providers can verify the signature. By registering the identity as a record and associating it with a verified Publisher, you give the signed identity a discoverable, trusted name in the registry.

Web bot is a record type alongside `AGENT`, `MCP`, `SKILL`, and `CUSTOM`. For more information about record types, see [Supported record types and descriptors](registry-supported-record-types.md).

A Web bot record uses the `signatureAgentCard` descriptor, its record-type value is `WEB_BOT`, and it carries a category. For the descriptor fields, the JWKS URL, and the category values, see [Supported record types and descriptors](registry-supported-record-types.md).

## How Web bot relates to AWS WAF
<a name="registry-web-bot-waf"></a>

After a Web bot identity is registered and associated with a verified Publisher, [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) can recognize the signed, verified agent. Content providers can then write [web ACL rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html) that act on the verification result — for example, allowing verified agents from a specific domain while blocking unverified crawlers. The registry provides the verified identity; AWS WAF makes the enforcement decision.

## Tagging Web bot records
<a name="registry-web-bot-tagging"></a>

You can tag Web bot records. The `TagResource`, `UntagResource`, and `ListTagsForResource` actions apply to this record type. Use tags to categorize Web bot records for cost allocation, access control, and organizational tracking, the same way you tag other registry resources. For more information about tags, see [Tags](registry-concepts.md#registry-concept-tags).