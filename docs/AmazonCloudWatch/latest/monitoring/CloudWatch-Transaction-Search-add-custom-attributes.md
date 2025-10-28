# Adding custom attributes

CloudWatch Application Signals utilizes OpenTelemetry to auto-instrument your applications and collect spans from popular libraries in different languages, such as Java, Python, and more.

Auto-instrumentation captures information, such as database queries, HTTP requests, cache accesses, and external service calls, which allows you to troubleshoot application performance issues.

You can add custom instrumentation to enrich spans with business-specific data or other information you wish to capture.
This data can be recorded as a custom attribute or a span event, providing insights tailored to your troubleshooting needs.

###### Note

For information about adding custom attributes or span events in a different language, see [Language APIs and SDKS](https://opentelemetry.io/docs/languages/ "https://opentelemetry.io/docs/languages/") in the _OpenTelemetry website_.

## Custom attributes

You can add business related attributes or any other attributes to your spans in all languages OpenTelemetry supports.
The following is a Java code snippet that adds an order id and customer details to a span.

```
import io.opentelemetry.api.trace.Span;

public class OrderProcessor {

    public void processOrder() {
        Span span = Span.current();
        span.setAttribute("order.id", "123456");
        span.setAttribute("customer.name", "John Doe");
        span.setAttribute("customer.id", "4343dfdd");

        // Your order processing logic here
        System.out.println("Order processed with custom attributes");
    }
}
```

After these attributes have been added to the span, they become available to search and analyze in [the Transaction Search visual editor](CloudWatch-Transaction-Search-search-analyze-spans.md "CloudWatch-Transaction-Search-search-analyze-spans.md").

## Span events

A span event is typically used to denote a meaningful, singular point in time during a span duration.
Exceptions are auto-captured as span events through auto-instrumentation, but you can also add custom business events, such as payment-status or cart-abandonment.
For more information, see [Span events](https://opentelemetry.io/docs/concepts/signals/traces/#span-events "https://opentelemetry.io/docs/concepts/signals/traces/#span-events") on the OpenTelemetry website.

You can embed span events to your spans in all the languages CloudWatch Application Signals and OpenTelemetry support.
The following is a Java code snippet of adding a custom event to a span.

```
import io.opentelemetry.api.trace.Span;

public class OrderProcessor {

    public void bookOrder() {
        Span span = Span.current();

        // Add a booking started event
        span.addEvent("booking started");

        // Add a payment succeeded event or failed event
        span.addEvent("booking failed");
    }
}
```

### Prerequisites for the CloudWatch agent

When using the CloudWatch agent to emit span events to X-Ray, you must turn on the `transit_spans_in_otlp_format` flag in your configuration.

```
{
  "traces": {
    ...
    "transit_spans_in_otlp_format": true
    ...
  }
}
```

After you add these events, they become available in the [Transaction Search visual editor](CloudWatch-Transaction-Search-search-analyze-spans.md "CloudWatch-Transaction-Search-search-analyze-spans.md").

## CloudWatch Logs queries

You can query span events in CloudWatch Logs to view advanced insights.
The following example query commands show how to analyze exceptions thrown by your application:

````

fields jsonparse(@message) as js
| unnest js.events into event
| filter event.name = "exception"
| display event.attributes.`exception.stacktrace` ``` ``` fields jsonparse(@message) as js
| unnest js.events into event
| filter event.name = "exception"
| stats count() by event.attributes.`exception.type` ```
````
