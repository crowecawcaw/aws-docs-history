

# Common rule group settings in AWS Network Firewall

Every firewall rule group and IPS rule group has the following top-level settings:
+ **Type** – Whether the rule group is a firewall rule group or an IPS rule group.
+ **Name** – Identifier for the rule group. You assign a unique name to every rule group. You can't change the name of a rule group after you create it.
+ **Description** – Optional additional information about the rule group. Fill in any information that might help you remember the purpose of the rule group and how you want to use it. The description is included in rule group lists in the console and through the APIs.
+ **Capacity** – Limit on the processing requirements for the rule group. You can't change this setting after you create the rule group. For the maximum number of rules per policy, see [AWS Network Firewall quotas](quotas.md).
+ **Rules** – Set of packet inspection criteria used in the rule group. Rules in a rule group are either firewall rules or IPS rules, depending on the rule group type. For information about authoring rules, see [Working with firewall rule groups in AWS Network Firewall](firewall-rule-groups.md) and [Working with IPS rule groups in AWS Network Firewall](ips-rule-groups.md).
+ **Encryption options** (Optional) – Network Firewall encrypts and decrypts Network Firewall resources, to protect against unauthorized access. By default, Network Firewall uses AWS owned keys for this. If you want to use your own keys, you can configure customer managed keys from AWS Key Management Service and provide them to Network Firewall. For information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md).
+ **Tags** – Zero or more key-value tag pairs. A tag is a label that you assign to an AWS resource. You can use tags to search and filter your resources and to track your AWS costs. For more information, see [Tagging AWS Network Firewall resources](tagging.md).