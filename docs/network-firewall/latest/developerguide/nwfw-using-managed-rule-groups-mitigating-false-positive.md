# Troubleshooting AWS managed rule groups in Network Firewall

As a best practice, before using a rule group in production,
with logging enabled,
run the managed rule group in **alert
mode** if you're using an intrusion
detection system (IDS), or in **drop mode**
if you use an intrusion prevention system (IPS) in a
non-production environment. Either mode sends alert messages to the logs for traffic that doesn't pass inspection. For
more information, see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").

Running a managed rule group in either alert mode or drop mode allows you to do a dry run
with alert logs that show you what the resulting behavior
would be before you commit to making changes to your traffic. Evaluate the rule group using Network Firewall logs. When
you're satisfied that the rule group does what you want it to do,
disable test mode on the group.

###### Mitigating false-positive scenarios

If you are encountering false-positive scenarios with
AWS managed rule groups, perform the following
steps:

1. In the firewall policy's AWS managed rule
   group settings in the Network Firewall console, override the
   actions in the rules of the rule groups by
   enabling **Run in alert mode**.
   This stops them from blocking legitimate
   traffic.
2. Use [Network Firewall
   logs](logging-monitoring.md "logging-monitoring.md") to identify which AWS managed rule
   group is triggering the false positive.
3. In the AWS Network Firewall console, edit the firewall
   policy, and locate the AWS managed rule group
   that you've identified. Then, disable
   **Run in alert mode** for the
   rules that aren't causing the false positive, and
   leave the rule group that is causing the false
   positive in
   alert
   mode.
   For more information about a rule in an AWS managed rule
   group, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
