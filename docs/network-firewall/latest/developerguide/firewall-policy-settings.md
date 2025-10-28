# Firewall policy settings in AWS Network Firewall

A firewall policy in Network Firewall has the following configuration settings, which you define when you create or update the firewall policy. All
settings except for the firewall policy name are changeable.

###### Tip

If you own a firewall that is shared with others using VPC endpoint associations, you should review the settings in your
firewall policy to ensure they apply to VPC endpoint associations as needed.

- **Name** – The identifier for the firewall policy. You
  assign a unique name to every firewall policy. You can't change the name of a
  firewall policy after you create it.
- **Description** – Optional additional
  information about the firewall policy. Fill in any information that might help
  you remember the purpose of the firewall policy and how you want to use it. The
  description is included in firewall policy lists in the console and through the
  APIs.
- **Stream exception policy** – The stream exception policy determines how Network Firewall handles traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself. For more information, see [Stream exception policy options in your AWS Network Firewall firewall policy](stream-exception-policy.md "stream-exception-policy.md").
- **Stateless rule groups** – Zero or more collections of
  stateless rules, with priority settings that define their processing order
  within the policy. For information about creating and managing rule groups for
  use in your policies, see [Managing your own rule groups in AWS Network Firewall](rule-groups.md "rule-groups.md").
- **Stateless default actions** – Define how
  Network Firewall handles a packet that doesn't match any of the rules in the stateless rule groups.

You can specify same default settings for all packets or different default settings for full packets and for UDP packet fragments.

Network Firewall silently drops packet fragments for other protocols.

The options for the firewall policy's
default settings are the same as for stateless rules. For information about
the options, see [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

- **Default actions for fragmented packets** – Define how Network Firewall handles UDP packet fragments.
  Network Firewall silently drops packet fragments for other protocols.
- **Stateful engine options** – The structure that holds stateful rule order settings.
  Note that you can only configure RuleOrder settings when you first create the policy. RuleOrder can't be edited later.
- **Stateful rule groups** – Zero or more collections of
  stateful rules, provided in Suricata compatible format. For information about
  creating and managing rule groups for use in your policies, see [Managing your own rule groups in AWS Network Firewall](rule-groups.md "rule-groups.md").
- **Stateful default actions** – Define how
  Network Firewall handles a packet that doesn't match any of the
  rules in the stateful rule groups.

These settings apply when you use strict ordering for stateful rule evaluation, and you can provide them
even if you don't define stateful rule groups for the policy.

For more information about the options, see
[Strict evaluation order](suricata-rule-evaluation-order.md#suricata-strict-rule-evaluation-order "suricata-rule-evaluation-order.md#suricata-strict-rule-evaluation-order").

- **Customer-managed key** (Optional) – Network Firewall
  encrypts and decrypts Network Firewall resources, to protect against unauthorized access.
  By default, Network Firewall uses AWS owned keys for this. If you want to use your own
  keys, you can configure customer managed keys from AWS Key Management Service and provide them to Network Firewall.
  For information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md "kms-encryption-at-rest.md").
- **Policy variables** (Optional) – You can configure one or more IPv4 or IPv6 addresses in CIDR notation to override the default value of Suricata `HOME_NET`. If your firewall is deployed using a centralized deployment model, you might want to override `HOME_NET` with the CIDRs of your home network. Otherwise, Network Firewall uses the CIDR of your inspection VPC.

The firewall policy `EXTERNAL_NET` setting is the negation of its `HOME_NET` setting.
For example, if the `HOME_NET` is `11.0.0.0`, then `EXTERNAL_NET` is set to `!11.0.0.0`.

###### Note

Policy variables do not automatically apply to VPC endpoint associations.
For example, if `HOME_NET` is already configured for a primary firewall, you must also configure it to apply to VPC endpoints associated with that firewall.

- **TCP idle timeouts** (Optional) – Defines the number of seconds that can pass without any traffic sent through the firewall before the firewall determines that the TCP connection is idle. When you update this value, existing connections will be treated according to your stream exception policy configuration.

You can define the value to be between 60 and 6000 seconds. If no value is provided, it defaults to 350 seconds.

- **TLS inspection configuration** (Optional) – Contains settings to turn on
  decryption and re-encryption of the Secure Socket Layer (SSL)/Transport Layer
  Security (TLS) traffic going to your firewall so that the traffic can be
  inspected according to the policy's stateful rules. For more information, see
  [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md "tls-inspection-configurations.md").
- **Tags** (Optional) – Zero or more key-value tag pairs. A tag is a
  label that you assign to an AWS resource. You can use tags to search and filter
  your resources and to track your AWS costs. For more information about tags, see
  [Tagging AWS Network Firewall resources](tagging.md "tagging.md").

## AWS Network Firewall firewall policy capacity limitations

Network Firewall uses capacity calculations and limiting to control the operating resources
that are required to process your rule groups and firewall policies. Each rule group
has a capacity setting that's reserved for it in the firewall policy when you add
it. Additionally, the firewall policy has limits on the count of rule groups that
you can add. For information about limits, see [AWS Network Firewall quotas](quotas.md "quotas.md") for
information about rule group capacity, see [Setting rule group capacity in AWS Network Firewall](nwfw-rule-group-capacity.md "nwfw-rule-group-capacity.md").
