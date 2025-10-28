# Troubleshooting AWS Network Firewall

The topics in this chapter can help you troubleshoot problems with configuring and using AWS Network Firewall.

###### Contents

- [Troubleshooting general issues in AWS Network Firewall](troubleshooting-general-issues.md "troubleshooting-general-issues.md")
  - [Firewall endpoint creation or deletion fails](troubleshooting-general-issues.md#troubleshoot-firewall-endpoint--creation-fails "troubleshooting-general-issues.md#troubleshoot-firewall-endpoint--creation-fails")
  - [Availability Zone is unsupported](troubleshooting-general-issues.md#troubleshoot-unsupported-az "troubleshooting-general-issues.md#troubleshoot-unsupported-az")
  - [How do I check if I have asymmetric routing?](troubleshooting-general-issues.md#troubleshoot-check-asymmetric-routing-tg "troubleshooting-general-issues.md#troubleshoot-check-asymmetric-routing-tg")
  - [I'm using Network Firewall with AWS Transit Gateway and Network Firewall is dropping traffic](troubleshooting-general-issues.md#troubleshoot-dropped-traffic-flows "troubleshooting-general-issues.md#troubleshoot-dropped-traffic-flows")
  - [High latency and intermittent packet drops when traffic passes through Network Firewall](troubleshooting-general-issues.md#troubleshoot-high-latency-package-drops "troubleshooting-general-issues.md#troubleshoot-high-latency-package-drops")

- [Troubleshooting logging in AWS Network Firewall](troubleshooting-logging.md "troubleshooting-logging.md")
  - [My firewall isn't logging all traffic that matches pass action rules](troubleshooting-logging.md#troubleshoot-logging-partial-traffic "troubleshooting-logging.md#troubleshoot-logging-partial-traffic")
  - [I don't see Alert logs that match drop action rules in my rule group](troubleshooting-logging.md#troubleshoot-logging-alert-logs-matching-rules "troubleshooting-logging.md#troubleshoot-logging-alert-logs-matching-rules")
  - [I don’t see any TLS logs even though I have
    TLS logging enabled](troubleshooting-logging.md#troubleshoot-logging-no-tls-logs "troubleshooting-logging.md#troubleshoot-logging-no-tls-logs")

- [Troubleshooting rules in AWS Network Firewall](troubleshooting-rules.md "troubleshooting-rules.md")
  - [Rules with the HOME_NET variable are not working as expected with managed rule groups](troubleshooting-rules.md#troubleshoot-rules-home-net "troubleshooting-rules.md#troubleshoot-rules-home-net")
  - [I created a rule to allow only outbound traffic from HOME_NET to EXTERNAL_NET, but EXTERNAL_NET was also able to initiate a connection back to HOME_NET. How do I prevent this from happening?](troubleshooting-rules.md#troubleshoot-rules-allow-outbound-home-net "troubleshooting-rules.md#troubleshoot-rules-allow-outbound-home-net")
  - [I'm using strict ordering, but stateful rules near the bottom of my ruleset appear to be handling traffic before rules near the top of my ruleset](troubleshooting-rules.md#troubleshoot-rules-strict-ordering-rule-order "troubleshooting-rules.md#troubleshoot-rules-strict-ordering-rule-order")
  - [I've configured a drop action rule but traffic still goes through the firewall](troubleshooting-rules.md#troubleshoot-rules-not-working-as-expected "troubleshooting-rules.md#troubleshoot-rules-not-working-as-expected")
  - [I have a rule that is intermittently not matching when I think it should](troubleshooting-rules.md#troubleshoot-rules-not-working-depth-limit-reached "troubleshooting-rules.md#troubleshoot-rules-not-working-depth-limit-reached")

- [Troubleshooting TLS inspection in AWS Network Firewall](troubleshooting-tls-inspection.md "troubleshooting-tls-inspection.md")
  - [Outbound TLS - Blocked connections to servers with revoked certificates](troubleshooting-tls-inspection.md#troubleshoot-blocked-connections-outbound-tls "troubleshooting-tls-inspection.md#troubleshoot-blocked-connections-outbound-tls")
  - [Outbound TLS - Passing traffic for specific target server with revoked certificates by adjusting scope](troubleshooting-tls-inspection.md#troubleshoot-how-to-pass-traffic-revoked-certificates "troubleshooting-tls-inspection.md#troubleshoot-how-to-pass-traffic-revoked-certificates")
  - [Troubleshooting connection issues with AWS service endpoints (including the AWS Systems Manager agent)](troubleshooting-tls-inspection.md#troubleshoot-connection-service-endpoints "troubleshooting-tls-inspection.md#troubleshoot-connection-service-endpoints")
  - [Troubleshooting TLS - Connections dropping or resetting](troubleshooting-tls-inspection.md#troubleshoot-connection-drops "troubleshooting-tls-inspection.md#troubleshoot-connection-drops")
