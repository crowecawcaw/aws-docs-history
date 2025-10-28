# Considerations and disclaimers for using AWS managed rule groups in Network Firewall

Before you add AWS managed rule groups to a firewall policy, consider the following.

###### Disclaimer

Managed rule groups are designed to protect you from common web threats. When used in accordance
with the documentation, AWS managed rule groups add another layer of security for your
applications. However, AWS managed rule groups aren't intended as a replacement for
your security responsibilities, which are determined by the AWS resources
that you select. Refer to the [Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") to ensure that your resources in AWS are
properly protected.

###### DNS traffic limitations

Network Firewall filters network traffic that is routed through firewall endpoints. However, DNS queries made to
Amazon Route 53 Resolver are not inspected because they are routed to a static address in the VPC. Any DNS inspection rules
in AWS managed rule groups, including active threat defense managed rule groups, cannot inspect traffic to Amazon Route 53 Resolver. For more information about
Network Firewall limitations, see [Limitations and caveats
for stateful rules in AWS Network Firewall](suricata-limitations-caveats.md "suricata-limitations-caveats.md").

###### Automatic updates

AWS automatically updates managed rule groups to protect against new vulnerabilities and threats. These updates can occur
daily to weekly, depending on threat severity.
Sometimes, AWS is notified of new vulnerabilities before public disclosure due to its participation in
a number of private disclosure communities. In those cases, Network Firewall may update rule groups and deploy
them to your environment before a new threat is widely known.

###### Copying AWS managed rules

You can copy managed threat signature rules into your own rule group and customize them for your specific needs, but Network Firewall does not
supporting copying active threat defense rules.
