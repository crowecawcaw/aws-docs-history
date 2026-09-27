

# Protect sensitive data
<a name="omni-data-protection"></a>

Agent telemetry can contain sensitive information: prompts and responses often include user messages, retrieved documents, and personal data. You control what is captured and who can see it. CloudWatch Omni does not automatically detect or redact personally identifiable information (PII); no data is removed unless you configure it. Choose where in the pipeline filtering happens based on your compliance requirements.

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or into free-form text fields such as a **Name** field. This includes when you work with CloudWatch Omni or other AWS services using the Omni web UI, the AWS Management Console, the API, the AWS CLI, or the AWS SDKs. Any data that you enter into tags or free-form text fields used for names might be used for billing or diagnostic logs. CloudWatch Omni accepts tags on several resource types, and free-form names on spaces, grants, access profiles, dashboards, and alerts. For the resource types that accept tags, see [Custom grant actions](omni-custom-grant-actions.md).

You can apply controls at five points, from most restrictive to least. Each layer involves a trade-off between eliminating data and keeping it available for debugging.

![The five points where sensitive telemetry can be filtered: capture-time redaction in the application, which is most restrictive, then the collector, ingestion masking, encrypted storage, and read-time access filters, which are least restrictive.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-data-protection-layers.png)


**At capture time (most restrictive)**

Strip or redact fields before spans leave your application, using standard OpenTelemetry mechanisms. Sensitive data filtered here is redacted in process and never leaves your application, so this is the only layer that satisfies a requirement that the data never be exported.

`AWS_REDACT_SPAN_ATTRIBUTES` takes a comma-separated list of span attributes to redact. Matching values in spans, span events, and span links are all replaced with `REDACTED`. This applies to all span attributes, not only those from ADOT instrumentation.

```
export AWS_REDACT_SPAN_ATTRIBUTES=gen_ai.input.messages,gen_ai.output.messages
```

The variable also accepts wildcard patterns, so you can redact a group of attributes without naming each one. For example, to redact all input and output message attributes from a third-party instrumentation library:

```
export AWS_REDACT_SPAN_ATTRIBUTES='llm.input_messages.*,llm.output_messages.*'
```

**Warning** Redaction occurs in the agent process, before telemetry is exported. This might affect other integrations that rely on these attribute values.

`AWS_REDACT_SPAN_ATTRIBUTES` applies equally to OpenInference-instrumented agents running on Amazon Bedrock AgentCore.

To redact all prompt and response content from an agent instrumented with OpenInference, set the OpenInference environment flags before your agent starts. Content is replaced with `__REDACTED__` before spans are created:

```
OPENINFERENCE_HIDE_INPUTS=True
OPENINFERENCE_HIDE_OUTPUTS=True
```

For finer control, add a custom span processor that removes specific attributes. This is standard OpenTelemetry and works with the AWS Distro for OpenTelemetry (ADOT), OpenInference, and other OpenTelemetry SDKs. The span-processor API differs by language, and the following example is Python. **JavaScript does not provide an equivalent custom span-processor approach, so we recommend the environment variable approach described above.**

```
from opentelemetry.sdk.trace import SpanProcessor, Span, ReadableSpan

class SensitiveDataRedactingProcessor(SpanProcessor):
    """Redacts sensitive attributes from spans before export."""

    REDACT_KEYS = {"gen_ai.input.messages", "gen_ai.output.messages",
                   "user.email", "http.request.header.authorization"}

    def on_start(self, span, parent_context=None):
        pass

    def _on_ending(self, span: Span):
        if not span.attributes:
            return
        redacted = {k: v for k, v in span.attributes.items()
                    if k not in self.REDACT_KEYS}
        if len(redacted) != len(span.attributes):
            span._attributes = redacted  # noqa: SLF001

    def on_end(self, span: ReadableSpan):
        pass

    def shutdown(self):
        pass

    def force_flush(self, timeout_millis=None):
        return True

# Wire up before your agent starts:
from opentelemetry import trace
provider = trace.get_tracer_provider()
provider.add_span_processor(SensitiveDataRedactingProcessor())
```

This example requires `opentelemetry-sdk` version 1.39.0 or later.

**Note** Capture-time redaction is irreversible. Redacted data is not available for root-cause analysis later. If a trace shows blank input and output that you expected to see, check these flags first. See [Send AI agent telemetry](omni-send-ai-agent-telemetry.md).

**At the collector (defense in depth)**

If you run an OpenTelemetry Collector, its built-in processors provide a second redaction layer before data reaches CloudWatch:
+ `attributes` — remove or modify specific attributes.
+ `redaction` — drop attributes that are not on an allow list.
+ `transform` — replace values using regular expressions.
+ `filter` — drop entire spans that match a condition.

At this layer, data has already left your application process. Use collector processors as an additional safety net. They are not sufficient on their own if your compliance model requires that data never leave your infrastructure.

For each processor's configuration, see its documentation: [attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/attributesprocessor/README.md), [redaction](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/redactionprocessor/README.md), [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/transformprocessor/README.md), and [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/filterprocessor/README.md).

This layer is available wherever you run the collector yourself, for example on Amazon EC2, Amazon ECS, or Amazon EKS. If your agent runs on Amazon Bedrock AgentCore Runtime, you do not manage a collector there, so redact at capture time instead.

**At ingestion: pattern-based masking**

For log data in Amazon CloudWatch Logs, CloudWatch Logs data protection can detect and mask sensitive patterns, such as Social Security numbers and credit card numbers, as it is ingested. For more information, see [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) in the *Amazon CloudWatch Logs User Guide*.

**Important**  
CloudWatch Logs data protection policies apply to log data in CloudWatch Logs. They do not apply to the telemetry in your space's CloudWatch Dataset. A masking policy you configured for your log groups does not carry over. To keep sensitive values out of your space, filter at capture time or at the collector.

**At read time: row-level data scope**

Telemetry is stored in full, and a member's grant controls what their queries and views return. A grant's advanced data scope can limit a member to specific signal types (logs, traces) and to rows matching conditions on agent, service, account, or field value. Configure it when you add or edit a member. See [Limit what members can see](omni-limit-what-members-can-see.md).

**At rest: encryption**

Telemetry is encrypted in transit with TLS and at rest in the CloudWatch Dataset, where you can use a customer managed AWS KMS key. For the encryption model, see [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md).

**Data sent to the judge model**

Evaluators that use a model as a judge send data to that model: the evaluator prompt and the trace content it evaluates go to the judge model you configure, and to the provider that serves it. If your compliance model restricts where trace content can flow, choose the judge model accordingly, or restrict evaluation to traces that do not contain sensitive content. For how evaluators work and which models you can choose, see [Evaluators and evaluations](omni-agents-evaluators.md).

**Choose the right layer**


| Requirement | Layer | Trade-off | 
| --- | --- | --- | 
| Sensitive data must never leave the application | Capture time | Redacted data is unavailable for debugging | 
| Extra safety net on the export path | Collector processors | Data has already left the process | 
| Catch sensitive patterns you did not anticipate | Ingestion-time masking | Data has been sent; masking depends on pattern detection | 
| Store in full; limit which rows a member sees | Per-grant row-level data scope | Data is stored; controls govern reads | 
| Control the encryption keys | Customer managed KMS key | You manage key policy and rotation | 