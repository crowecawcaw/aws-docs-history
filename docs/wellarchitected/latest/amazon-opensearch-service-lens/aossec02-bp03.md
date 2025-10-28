# AOSSEC02-BP03 Monitor real-time events in your OpenSearch Service domains

Track real-time events in your OpenSearch Service domains using
Amazon EventBridge, enabling automated actions and notifications to improve
visibility and response times.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome:** Real-time events
in OpenSearch Service domains are tracked and monitored according to
your requirements. Automated actions and notifications are
configured for relevant events if required.

**Benefits of establishing this best
practice:**

- **Enhanced monitoring:** You can
  use Amazon EventBridge to monitor real-time events in OpenSearch Service domains to receive notifications about specific
  events that affect your domains, improving overall visibility
  and awareness.
- **Automated actions:** By
  creating rules to determine which events are relevant and
  defining automated actions to take when a rule initiates,
  organizations can streamline responses to domain-related events
  and reduce the risk of manual errors or delays.

## Implementation guidance

Amazon OpenSearch Service integrates with Amazon EventBridge,
which provides notifications about specific events that affect
your domains in near real-time. This integration also provides a
transition from Amazon CloudWatch Events.

With this setup, you can create simple rules to determine which
events are relevant to you and define automated actions to take
when a rule occurs. Amazon EventBridge can notify you of various
events related to your OpenSearch Service domain, such as software
updates, Auto-Tune activities, cluster health changes, VPC
endpoint modifications, node retirements, and domain errors.

To create a Lambda function that listens to these events, see
[Tutorial:
Listening for Amazon OpenSearch Service EventBridge events](../../../opensearch-service/latest/developerguide/listening-events.md "../../../opensearch-service/latest/developerguide/listening-events.md")
and
[Tutorial:
Sending Amazon SNS alerts for available software updates](../../../opensearch-service/latest/developerguide/sns-events.md "../../../opensearch-service/latest/developerguide/sns-events.md").

## Resources

- [Monitoring
  OpenSearch Service events with Amazon EventBridge](../../../opensearch-service/latest/developerguide/monitoring-events.md "../../../opensearch-service/latest/developerguide/monitoring-events.md")
