

# Configure HTTP endpoint visibility
<a name="Application-Signals-EndpointVisibility"></a>

This page provides guidance for Application Signals customers who expect to see their HTTP service operations separated by specific endpoint names, but instead see multiple endpoints grouped into the same metric. By default, Application Signals truncates the `Operation` metric dimension to the first URL path segment for HTTP services (for example, `/api/v1/users` becomes `GET /api`) to preserve low-cardinality metrics. As a result, users may find that services with multiple endpoints sharing the same prefix have limited visibility into the operational health of individual endpoints. You can follow the steps below to configure service operation endpoints to your desired granularity.

**Important**  
Modifying endpoint visibility is a breaking change as it affects the Application Signals metric dimensions for service operations. Remember to update your SLO thresholds, alarms, and/or dashboards accordingly.

## AWS Distro for OpenTelemetry (ADOT) solution
<a name="Application-Signals-EndpointVisibility-ADOT"></a>

For customers using AWS Distro for OpenTelemetry (ADOT), set the `OTEL_AWS_HTTP_OPERATION_PATHS` environment variable with a comma-separated list of URL path templates for the HTTP service:

```
export OTEL_AWS_HTTP_OPERATION_PATHS="/path/to/endpoint, /another/{placeholder}/endpoint"
```

This variable uses the longest matching prefix against the HTTP server span's `url.path` attribute to determine the operation name. Wildcard patterns match any single URL segment and can be denoted by `{placeholder}`, `:placeholder`, or `*`. After setting the variable, restart your application for the new endpoint groupings to take effect.

This variable is supported in ADOT for Java, Python, Node.js, and .NET.

**Example**

Consider an API service that receives the following traffic:

```
GET  /api/users
GET  /api/users/42
GET  /api/users/42/orders
POST /api/users/99/orders
POST /api/users/42/orders
GET  /api/users/42/orders/7/items
GET  /api/products
```

By default, Application Signals groups all of these into `GET /api` or `POST /api` service metrics, making it impossible to distinguish performance between endpoints.

To fix this, set the environment variable with the desired path templates:

```
export OTEL_AWS_HTTP_OPERATION_PATHS="/api/users/{userId}/orders/{orderId}/items, /api/users/{userId}/orders, /api/users/{userId}, /api/users, /api/products"
```

With this configuration, Application Signals shows distinct operations. Multiple requests can resolve to the same configured template:


| Incoming request | Default operation | With config | 
| --- | --- | --- | 
| GET /api/users | GET /api | GET /api/users | 
| GET /api/users/42 | GET /api | GET /api/users/{userId} | 
| GET /api/users/42/orders | GET /api | GET /api/users/{userId}/orders | 
| POST /api/users/99/orders | POST /api | POST /api/users/{userId}/orders | 
| POST /api/users/42/orders | POST /api | POST /api/users/{userId}/orders | 
| GET /api/users/42/orders/7/items | GET /api | GET /api/users/{userId}/orders/{orderId}/items | 
| GET /api/products | GET /api | GET /api/products | 

## Native OpenTelemetry solution
<a name="Application-Signals-EndpointVisibility-NativeOTel"></a>

If you are using the native OpenTelemetry SDK (without ADOT), you can either override the span name using the transform processor in your OpenTelemetry Collector or directly in application code.

**Note**  
You must configure your collector with an OTLP exporter to preserve the OpenTelemetry span name so that CloudWatch can parse it for the Application Signals operation name. For more information, see [Sending OTLP data to CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPSimplesetup.html).

**Option 1 (recommended): Collector-side transformation**

Use the [transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/transformprocessor) to set span names based on URL patterns. The transform processor uses OTTL (OpenTelemetry Transformation Language) and can modify the span `name` field directly.

Order rules from shallowest to deepest – statements run sequentially, so more specific matches later in the list override the general ones set earlier. In the following example, the value of the span attribute `url.path` is matched and the resulting span name is set to the request method followed by the desired URL pattern.

```
processors:
  transform/operation_names:
    trace_statements:
      - context: span
        conditions:
          - IsMatch(attributes["url.path"], "^/api/contests(/|$)")
        statements:
          - set(name, Concat([attributes["http.request.method"], "/api/contests"], " "))

      - context: span
        conditions:
          - IsMatch(attributes["url.path"], "^/api/contests/[^/]+$")
        statements:
          - set(name, Concat([attributes["http.request.method"], "/api/contests/{id}"], " "))

      - context: span
        conditions:
          - IsMatch(attributes["url.path"], "^/api/contests/[^/]+/leaderboard(/|$)")
        statements:
          - set(name, Concat([attributes["http.request.method"], "/api/contests/{id}/leaderboard"], " "))

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [resourcedetection, transform/operation_names, batch]
      exporters: [otlphttp/xray]
```

**Option 2: Setting span name in application code**

You can manually set the span name for server spans in your application code using the OpenTelemetry API. Set the name to `{HTTP_METHOD} {route_template}` where the route template uses parameterized placeholders. Note that this is a hardcoded fallback option, and you must manually update the span name in each HTTP request handler to apply this change.

**Java**

```
import io.opentelemetry.api.trace.Span;

// Inside your request handler
Span.current().updateName("GET /api/contests/{id}/leaderboard");
```

**Python**

```
from opentelemetry import trace

# Inside your request handler
span = trace.get_current_span()
span.update_name("GET /api/contests/{id}/leaderboard")
```

**Go**

```
import "go.opentelemetry.io/otel/trace"

// Inside your request handler
span := trace.SpanFromContext(ctx)
span.SetName("GET /api/contests/{id}/leaderboard")
```

**Node.js**

```
import { trace } from '@opentelemetry/api';

// Inside your request handler
const span = trace.getActiveSpan();
if (span) {
  span.updateName('GET /api/contests/{id}/leaderboard');
}
```