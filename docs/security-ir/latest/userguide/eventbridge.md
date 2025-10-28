# Amazon EventBridge

Using Amazon EventBridge, you can to react, monitor, and orchestrate events associated with AWS Security Incident Response cases and memberships.
You can either route these events via Rules (for fan-out scenarios to one or more targets) or through Pipes (for point-to-point integrations with enhanced
filtering, enrichment, and transformation capabilities).

You can create integrations between Security Incident Response and third-party tooling or aggregate data to analyze using generative AI and other
AWS tooling. For example, when Security Incident Response proactively creates a case, you can use EventBridge automations to trigger systems to notify
stakeholders. Additionally, if you manage multiple AWS environments, you can use the Amazon EventBridge integration to monitor AWS Security Incident Response
memberships to ensure all environments maintain a strong security posture.

For more information you can review the [What is Amazon EventBridge?](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md")

###### Contents

- [Managing Security Incident Response events using Amazon EventBridge](eventbridge-integration-full.md "eventbridge-integration-full.md")
- [Using AWS Security Incident Response Events](using-events.md "using-events.md")
- [Tutorial: Sending Amazon Simple Notification Service alerts for Membership Updated events](service_sns_tutorial.md "service_sns_tutorial.md")
