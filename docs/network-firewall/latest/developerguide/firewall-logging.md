# Logging network traffic from AWS Network Firewall

You can configure AWS Network Firewall logging for your firewall's stateful engine.
Logging gives you detailed information about network traffic, including the time that
the stateful engine received a packet, detailed information about the packet, and any
stateful rule action taken against the packet. The logs are published to the log
destination that you've configured, where you can retrieve and view them.

###### Note

Firewall logging is only available for traffic that you forward to
the stateful rules engine. You forward traffic to the stateful engine through stateless rule
actions and stateless default actions in the firewall policy. For information about these actions settings, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md "firewall-policy-settings.md") and [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

Metrics provide some higher-level information for both stateless and stateful
engine types. For more information, see [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

You can record the following types of logs from your Network Firewall stateful engine.

- Flow logs are standard network traffic flow logs. Each flow log record
  captures the network flow for a specific standard stateful rule group.
- Alert logs report traffic that matches your stateful rules that have an action
  that sends an alert. A stateful rule sends alerts for the rule actions
  `DROP`, `ALERT`, and `REJECT`. For more information,
  see [Actions for stateful rules](rule-action.md#rule-action-stateful "rule-action.md#rule-action-stateful").
- TLS logs report events that are related to TLS inspection. These logs require the firewall to be configured
  for TLS inspection. For information, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md "tls-inspection-configurations.md").
  You can use the same or different logging destination for each log type. You enable
  logging for a firewall after you create it. For information about how to do this, see
  [Updating a AWS Network Firewall logging configuration](firewall-update-logging-configuration.md "firewall-update-logging-configuration.md").

###### Topics

- [Contents of a AWS Network Firewall log](firewall-logging-contents.md "firewall-logging-contents.md")
- [Timing of AWS Network Firewall log delivery](firewall-logging-timing.md "firewall-logging-timing.md")
- [Permissions to configure AWS Network Firewall logging](firewall-logging-permissions.md "firewall-logging-permissions.md")
- [Pricing for AWS Network Firewall logging](firewall-logging-pricing.md "firewall-logging-pricing.md")
- [AWS Network Firewall logging destinations](firewall-logging-destinations.md "firewall-logging-destinations.md")
- [Logging in AWS Network Firewall with server-side encryption
  and customer-provided keys](firewall-logging-encrypt-kms.md "firewall-logging-encrypt-kms.md")
- [Updating a AWS Network Firewall logging configuration](firewall-update-logging-configuration.md "firewall-update-logging-configuration.md")
