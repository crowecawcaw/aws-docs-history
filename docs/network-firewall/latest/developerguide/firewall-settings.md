# Firewall settings in AWS Network Firewall

A firewall in Network Firewall has the following configuration settings, which you define when you create or update the firewall. All
settings except for the firewall name are mutable.

- **Name** – The identifier for the
  firewall. You assign a unique name to every firewall. You can't change the name
  of a firewall after you create it.
- **Description** – Optional additional
  information about the firewall. Fill in any information that might help you
  remember the purpose of the firewall and how you want to use it. The description
  is included in firewall lists in the console and through the APIs.
- **VPC** – The VPC that's associated with
  the firewall. This is the VPC that the firewall provides protection for.
- **Subnets** – The primary public subnets that
  Network Firewall should use for the firewall. Network Firewall
  creates a firewall endpoint in each subnet. Specify one subnet for each Availability Zone
  where you want to use the firewall. Each subnet establishes
  the availability of the firewall in its Availability Zone.

In addition to these subnets, you can define other endpoints for the firewall
in VPC endpoint associations. For more information, about firewall endpoints, see [Firewalls and firewall endpoints in AWS Network Firewall](firewalls.md "firewalls.md")

For information about using your configured subnets, see [Configuring your VPC and other components for AWS Network Firewall](vpc-config.md "vpc-config.md").

- **Firewall policy** – The firewall policy
  that's associated with the firewall. The firewall policy provides the monitoring
  and protection behavior for the firewall. You can use the same firewall policy
  for more than one firewall. For more information about firewall policies, see
  [Firewall policies in AWS Network Firewall](firewall-policies.md "firewall-policies.md").
- **Logging** – The type and location of the
  logs that Network Firewall provides for the firewall's stateful rules engine.
  You can enable flow logging for the network traffic that passes through the stateful
  rules engine. You can enable alert logging for traffic that matches the
  stateful rules that have an action setting of `Alert`,
  `Drop`, or `Reject`. You can enable TLS logging for
  TLS errors and for
  errors in server certificate revocation checks on outbound traffic.
  For more information about logging, see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").
- **Encryption options** (Optional) – Network Firewall
  encrypts and decrypts Network Firewall resources, to protect against unauthorized access.
  By default, Network Firewall uses AWS owned keys for this. If you want to use your own
  keys, you can configure customer managed keys from AWS Key Management Service and provide them to Network Firewall.
  For information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md "kms-encryption-at-rest.md").
- **Tags** – Zero or more key-value tag
  pairs. A tag is a label that you assign to an AWS resource. You can use tags
  to search and filter your resources and to track your AWS costs. For more
  information, see [Tagging AWS Network Firewall resources](tagging.md "tagging.md").
- **Delete protection** – A Boolean setting
  that is enabled when you create a firewall, and protects against accidental
  deletion of the firewall. The setting isn't shown in the console because the
  firewall deletion process disables this protection. Through the API, you must
  explicitly disable delete protection before you can delete the firewall.
- **Traffic analysis mode** (Optional) –
  An array of strings that let you generate traffic analysis reports on specific
  types of traffic monitored by your firewall. By default, Traffic analysis mode is
  not enabled. For more information, see [Reporting on network traffic in Network Firewall](reporting.md "reporting.md").
