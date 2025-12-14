**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Viewing AWS Shield Advanced event details

You can see details about an event's detection, mitigation, and top contributors
in the bottom section of the console page for the event. This section can include a
mix of legitimate and potentially unwanted traffic, and may represent both traffic
that was passed to your protected resource and traffic that was blocked by Shield
mitigations.

- **Detection and mitigation** – Provides information about the
  observed event and any applied mitigations against it. For information about
  event mitigation, see [Responding to DDoS events in AWS](ddos-responding.md "ddos-responding.md").
- **Top contributors** – Categorizes the traffic that's involved in
  the event, and lists the primary sources of traffic that Shield has
  identified for each category. For application layer events, use the top
  contributors information to get a general idea of the nature of an event,
  but use the AWS WAF logs for your security decisions. For more information,
  see the sections that follow.
  Your event information in the Shield Advanced console is based on Shield Advanced metrics. For information about Shield Advanced metrics, see [AWS Shield Advanced metrics](shield-metrics.md "shield-metrics.md")

Mitigation metrics aren't included for Amazon CloudFront or Amazon Route 53 resources, because these
services are protected by a mitigation system that's always enabled and doesn't
require mitigations for individual resources.

The details sections vary according to whether the information is for an infrastructure
layer or application layer event.

###### Topics

- [Viewing application layer (layer 7) event details in Shield Advanced](ddos-event-details-application-layer.md "ddos-event-details-application-layer.md")
- [Viewing infrastructure layer (layer 3 or 4) event details in Shield Advanced](ddos-event-details-infrastructure-layer.md "ddos-event-details-infrastructure-layer.md")
