# Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall

AWS Network Firewall uses _TLS inspection configurations_ to decrypt your firewall's inbound
and outbound SSL/TLS traffic. After decryption, Network Firewall inspects the traffic according to
your firewall policy's stateful rules, and then re-encrypts it before sending it to its
destination. You can enable inspection of your firewall's inbound traffic, outbound traffic,
or both. To use TLS inspection with your firewall, you must import or provision certificates
to AWS Certificate Manager, create a TLS inspection configuration, add that configuration to a new firewall policy, and then
associate that policy with your firewall.

Pricing for using TLS inspection configurations is based on the amount of traffic that Network Firewall
inspects—which appears on your bill as advanced inspection—and the number
of deployed firewall endpoints. For information about TLS inspection configuration pricing, see [Network Firewall pricing](https://aws.amazon.com/network-firewall/pricing/ "https://aws.amazon.com/network-firewall/pricing/"). To use the
AWS pricing calculator to check Network Firewall costs, see [Network Firewall pricing
calculator](https://calculator.aws/#/addService/networkfirewall "https://calculator.aws/#/addService/networkfirewall").

###### Topics

- [Considerations when
  working with TLS inspection configurations in AWS Network Firewall](tls-inspection-considerations.md "tls-inspection-considerations.md")
- [Logging for TLS inspection in AWS Network Firewall](tls-inspection-logging.md "tls-inspection-logging.md")
- [Using
  SSL/TLS certificates with TLS inspection configurations in AWS Network Firewall](tls-inspection-certificate-requirements.md "tls-inspection-certificate-requirements.md")
- [TLS inspection configuration settings in AWS Network Firewall](tls-inspection-settings.md "tls-inspection-settings.md")
- [Using session holding with TLS inspection in AWS Network Firewall](session-holding-tls.md "session-holding-tls.md")
- [Managing your TLS inspection configuration in Network Firewall](managing-tls-configuration.md "managing-tls-configuration.md")
