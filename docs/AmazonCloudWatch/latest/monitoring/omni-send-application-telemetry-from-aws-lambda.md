

# Send application telemetry from AWS Lambda
<a name="omni-send-application-telemetry-from-aws-lambda"></a>

Lambda functions send traces and logs to CloudWatch without a collector. Turn on active tracing so Lambda records the service segments, add a trace SDK for spans around your handler logic, and emit structured logs that join their traces.

If your application runs on Amazon EC2, ECS, EKS, or Microsoft Azure, see [Send application telemetry](omni-send-application-telemetry.md). If you are monitoring an AI agent, see [Send AI agent telemetry](omni-send-ai-agent-telemetry.md).

**Prerequisites**
+ **Transaction Search is enabled** in the account and Region that receive traces. See [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html).
+ You can change the function's configuration and attach policies to its execution role.

**Step 1: Enable active tracing**

```
aws lambda update-function-configuration --function-name <my-function> --tracing-config Mode=Active
aws iam attach-role-policy --role-name <my-function-role> --policy-arn arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess
```
+ The default `PassThrough` mode records no segments; only `Active` records the `AWS::Lambda` and `AWS::Lambda::Function` service segments, and only for sampled invocations.
+ `AWSXRayDaemonWriteAccess` carries the required `xray:PutTraceSegments` and `xray:PutTelemetryRecords`. The Lambda console attaches it when you enable tracing; with infrastructure as code, attach it yourself.

------
#### [ CDK TypeScript ]

```
import { Function, Runtime, Code, Tracing } from 'aws-cdk-lib/aws-lambda';

new Function(this, 'CheckoutFn', {
  runtime: Runtime.PYTHON_3_12,
  handler: 'app.handler',
  code: Code.fromAsset('lambda'),
  tracing: Tracing.ACTIVE,   // adds AWSXRayDaemonWriteAccess to the role
});
```

------
#### [ Terraform ]

```
resource "aws_lambda_function" "checkout" {
  function_name = "checkout"
  handler       = "app.handler"
  runtime       = "python3.12"
  role          = aws_iam_role.checkout_exec.arn
  filename      = "lambda.zip"

  tracing_config {
    mode = "Active"
  }
}

resource "aws_iam_role_policy_attachment" "xray" {
  role       = aws_iam_role.checkout_exec.name
  policy_arn = "arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess"
}
```

------
#### [ CloudFormation ]

```
Resources:
  CheckoutFn:
    Type: AWS::Lambda::Function
    Properties:
      TracingConfig:
        Mode: Active
      # Handler, Runtime, Role, Code …

  # AWS SAM (AWS::Serverless::Function):
  #   Properties:
  #     Tracing: Active
```

------
#### [ CDK Python ]

Set the function's tracing mode to `ACTIVE` (`aws_lambda.Tracing.ACTIVE` in Python, `Tracing.ACTIVE` in Java). The CDK `Function` construct adds `AWSXRayDaemonWriteAccess` to the execution role when tracing is active.

------

**Step 2: Add the trace SDK**

Attach the AWS Distro for OpenTelemetry (ADOT) Lambda layer for your runtime and set `AWS_LAMBDA_EXEC_WRAPPER` so the layer auto-instruments the handler with no code change, then enrich the active span in your code.

**Important**  
The ADOT layer ARN is Region-, runtime-, and version-specific. Look up the current ARN for your Region and runtime in the ADOT Lambda documentation; do not copy one from another example. Attach it the same way you enabled tracing: `--layers` with the CLI, `layers` in CDK and Terraform, `Layers` in CloudFormation and SAM.

------
#### [ Python ]

```
# Attach the ADOT Python Lambda layer, then set the exec wrapper:
AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument
```

**app.py**

```
from opentelemetry import trace

def handler(event, context):
    span = trace.get_current_span()
    span.set_attribute("cart.items", len(event.get("items", [])))
    return {"statusCode": 200, "body": "ok"}
```

------
#### [ Node.js ]

```
# Attach the ADOT JavaScript Lambda layer, then set the exec wrapper:
AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-handler
```

**index.js**

```
const { trace } = require('@opentelemetry/api');

exports.handler = async (event) => {
  trace.getActiveSpan()?.setAttribute('cart.items', (event.items ?? []).length);
  return { statusCode: 200, body: 'ok' };
};
```

------
#### [ Java ]

```
# Attach the ADOT Java Lambda layer, then set the exec wrapper:
AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-handler   # auto-instrumentation agent
# For the SDK-only wrapper, use /opt/otel-proxy-handler
```

**Handler.java**

```
import io.opentelemetry.api.trace.Span;

public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent event, Context context) {
  Span.current().setAttribute("cart.items", event.getBody().length());
  return new APIGatewayProxyResponseEvent().withStatusCode(200);
}
```

------
#### [ .NET ]

There is no auto-instrumentation exec wrapper layer for .NET; configure the OpenTelemetry .NET SDK in code. Build a TracerProvider with the OTLP exporter at process start, and wrap the handler body in a span.

**Function.cs**

```
using System.Diagnostics;
using OpenTelemetry;
using OpenTelemetry.Trace;

// Build once, outside the handler, so it is reused across invocations:
static readonly TracerProvider Tp = Sdk.CreateTracerProviderBuilder()
    .AddSource("checkout").AddOtlpExporter().Build();
static readonly ActivitySource Source = new("checkout");

public APIGatewayProxyResponse Handler(APIGatewayProxyRequest req, ILambdaContext ctx)
{
    using var activity = Source.StartActivity("place_order");
    activity?.SetTag("cart.items", req.Body?.Length ?? 0);
    return new APIGatewayProxyResponse { StatusCode = 200, Body = "ok" };
}
```

------

**Step 3: Emit structured logs**

**app.py (Python shown; the same fields apply in every language)**

```
import json, logging
from opentelemetry import trace

log = logging.getLogger()

def handler(event, context):
    ctx = trace.get_current_span().get_span_context()
    log.info(json.dumps({
        "msg": "order placed",
        "requestId": context.aws_request_id,
        "trace_id": format(ctx.trace_id, "032x"),
        "items": len(event.get("items", [])),
    }))
    return {"statusCode": 200, "body": "ok"}
```
+ Lambda delivers standard output and error to the log group `/aws/lambda/<my-function>`.
+ Set the function's log format to JSON (`LoggingConfig.LogFormat = JSON`, or **Logging configuration** in the console) so records are structured and you can change the application log level without a code change.
+ Include `requestId` and `trace_id` in every record so log lines join their spans.
+ `AWSLambdaBasicExecutionRole` covers log delivery.

**Step 4: Verify**

Invoke the function, then open your space and choose **Trace Explorer**. A trace for the invocation shows the `AWS::Lambda` and `AWS::Lambda::Function` segments with your handler span beneath them, within about five minutes. In **Application map**, the function appears as a service, and its request, error, and duration metrics are span metrics generated from every exported span. They reflect all invocations, not only sampled ones. In the log group `/aws/lambda/<my-function>`, the JSON records carry the `trace_id` of the trace you just viewed.

**Note**  
When a traced caller invokes the function, such as an API Gateway stage with tracing enabled, the function's spans join the caller's trace. When the caller is not traced, no tracing header arrives and Lambda decides not to sample the invocation, but Transaction Search still captures the invocation's spans, because it is unaffected by the sampled flag in the trace context. Enable tracing on whatever invokes the function to get one end-to-end trace.

**Troubleshoot missing telemetry**


| Symptom | Cause and fix | 
| --- | --- | 
| No traces at all | Tracing mode is PassThrough. Set it to Active and confirm the execution role has AWSXRayDaemonWriteAccess. | 
| Service segments appear, but no handler spans | The layer is not attached, is the wrong Region or runtime, or AWS\_LAMBDA\_EXEC\_WRAPPER is unset or wrong for the runtime. | 
| Traces are intermittent or isolated | The caller is not traced, so no sampling decision propagates inbound and the function's spans are not connected to an upstream trace. Enable tracing on whatever invokes the function, such as the API Gateway stage; Transaction Search captures the spans either way. | 
| Logs do not join traces | The log format is not JSON, or records omit trace\_id. Set the log format to JSON and include the trace ID as shown in Step 3. | 
| Traces exist but are not searchable | Transaction Search was enabled after the traces were sent. Enable it, then invoke again. | 
| Only some invocations appear in the trace list | Transaction Search indexes only a sampled subset of spans for the trace list; all spans are stored. Raise the indexing percentage in Transaction Search settings. | 