# Amazon EventBridge integration with AWS X-Ray

You can use AWS X-Ray to trace [events](eb-events.md "eb-events.md") that pass through
EventBridge. EventBridge passes the original trace header to the [target](eb-targets.md "eb-targets.md")
so that target services can track, analyze, and debug.

EventBridge can pass a trace header for an event only if the event came from a
`PutEvents` request that passed the trace context. X-Ray doesn't trace
events that originate from third-party partners, scheduled events, or [AWS services](eb-events.md#eb-service-event "eb-events.md#eb-service-event"), and these event sources don't appear
on your X-Ray service map.

X-Ray validates trace headers, and trace headers that aren't valid are dropped. However,
the event is still processed.

###### Important

The trace header is **not** available on the event that's delivered to the
invocation target.

- If you have an [event archive](eb-archive-event.md "eb-archive-event.md"), the trace header isn't
  available on archived events. If you replay archived events, the trace header
  isn't included.
- If you have a [dead-letter queue (DLQ)](eb-rule-dlq.md "eb-rule-dlq.md"), the trace header is
  included in the `SendMessage` request that sends the event to the
  DLQ. If you retrieve events (messages) from the DLQ by using
  `ReceiveMessage`, the trace header associated with the event is
  included on the Amazon SQS message attribute, but it isn't included in the event
  message.
  For information about how an EventBridge event node connects source and target services, see
  [Viewing source and targets in the X-Ray service map](../../../xray/latest/devguide/xray-services-eventbridge.md#xray-services-eventbridge-service-map "../../../xray/latest/devguide/xray-services-eventbridge.md#xray-services-eventbridge-service-map") in the
  _AWS X-Ray Developer Guide_.

You can pass the following trace header information through EventBridge:

- **Default HTTP header** – The X-Ray SDK automatically populates the
  trace header as the `X-Amzn-Trace-Id` HTTP header for all invocation
  targets. To learn more about the default HTTP header, see [Tracing header](../../../xray/latest/devguide/xray-concepts.md#xray-concepts-tracingheader "../../../xray/latest/devguide/xray-concepts.md#xray-concepts-tracingheader") in the _AWS X-Ray Developer Guide_..
- **`TraceHeader` system attribute** –
  `TraceHeader` is a [PutEventsRequestEntry attribute](../APIReference/API_PutEventsRequestEntry.md "../APIReference/API_PutEventsRequestEntry.md") reserved by EventBridge to carry the X-Ray
  trace header to a target. If you also use `PutEventsRequestEntry`,
  `PutEventsRequestEntry` overrides the HTTP trace header.

###### Note

The trace header doesn't count towards the `PutEventsRequestEntry` event size. For
more information, see [Calculating PutEvents event entry size](eb-putevents.md#eb-putevent-size "eb-putevents.md#eb-putevent-size").

The following video demonstrates the use of X-Ray and EventBridge together:
