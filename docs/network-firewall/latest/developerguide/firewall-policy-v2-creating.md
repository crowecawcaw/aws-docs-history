

# Creating a Next Generation policy in AWS Network Firewall

To create a Next Generation policy in Network Firewall, you can reference firewall rule groups and IPS rule groups that you've already defined, author embedded rules directly in the policy, or both. For information about creating rule groups, see [Working with firewall rule groups in AWS Network Firewall](firewall-rule-groups.md) and [Working with IPS rule groups in AWS Network Firewall](ips-rule-groups.md).

If you want to use TLS inspection, you need to first create a TLS inspection configuration to use in the policy. Next Generation policies support session holding only. For information about authoring rules for TLS-inspected traffic in a Next Generation policy, see [TLS inspection with a Next Generation policy in AWS Network Firewall](tls-inspection-policy-v2.md).

For a description of each policy setting, see [Next Generation policy settings in AWS Network Firewall](firewall-policy-v2-settings.md).

The console takes you through the policy creation wizard one page at a time. The following procedure walks through the wizard in order—entering the policy details, setting the firewall default action and policy mode, configuring optional traffic inspection, adding rule groups, and reviewing and creating the policy. Choose **Next** to move from one page to the next.

**To create a Next Generation policy in the console**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

   In the navigation pane, under **Network Firewall**, choose **Firewall policies**, and then choose **Create firewall policy**.

   On the **Firewall policy details** page, for **Policy version**, select **Next Generation** (recommended, and selected by default). To create a Classic Network Firewall policy instead, select **Classic**; for information about the policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md). Enter a **Name** to identify the policy (you can't change the name after you create the policy) and an optional **Description**. Set the **Firewall default action** (**Drop** is recommended and selected by default), the **Policy mode** (**Enforce** by default), and the **Stream exception setting** (**Reject** is recommended and selected by default). Leave **Enable Active Threat Defense** selected (the default) to add the AWS managed Active Threat Defense rule group to the policy, or clear it if you don't want it. Under **Tags**, add any tags that you want to apply to the policy. For a description of each setting, see [Next Generation policy settings in AWS Network Firewall](firewall-policy-v2-settings.md). Then choose **Next**.

1. On the **Traffic inspection** page, all settings are optional: turn on **Route 53 Resolved IP validation** to validate destination IP addresses against Amazon Route 53 resolved domains, attach a TLS inspection configuration under **TLS inspection configurations** to inspect SSL/TLS traffic (Next Generation policies support session holding only), and customize the TCP idle timeout under **Idle timeouts**. For a description of each setting, see [Next Generation policy settings in AWS Network Firewall](firewall-policy-v2-settings.md). Then choose **Next**.

1. On the **Add firewall rule groups** page, choose **Add rule group**, and then either choose **Add existing rule group** to select a firewall rule group that you've already created and assign it a priority, or choose **Add embedded rules** to author rules directly in the policy with the visual or text rule builder (see [Embedded rules in a Next Generation policy](firewall-policy-v2-embedded-rules.md)). For more information, see [Creating a rule group for a Next Generation policy](rule-groups-v2-creating.md). Then choose **Next**.

1. On the **Add IPS rule groups** page, choose **Add rule group**, and then choose **Add existing rule group** to select an IPS rule group that you've already created, **Add embedded rules** to author rules directly in the policy (see [Embedded rules in a Next Generation policy](firewall-policy-v2-embedded-rules.md)), or **Add managed rule group** to choose from the available AWS managed rule groups (see [Using managed rule groups](nwfw-managed-rule-groups.md)). Then choose **Next**.

1. (Optional) On the **Network and encryption** page, under **Customer managed key** customize the encryption settings to use a AWS Key Management Service customer managed key (see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md)), and for **Policy variables** enter any CIDR ranges that you want to use to override the Suricata `HOME_NET` variable. Choose **Next**, and then on the **Review and create** page, review your policy settings—choose **Edit** for any section you want to change—and choose **Create firewall policy**.

You can also create a Next Generation policy with the AWS CLI. Each section can contain both referenced rule groups and embedded rule groups. A referenced entry uses a `ResourceArn` that points to an existing rule group, and an embedded entry uses an `InlineRuleGroup` whose rules are defined directly in the policy. The following example creates a policy in enforce mode with a drop default action, where the firewall section and the IPS section each have one referenced rule group and one embedded rule group. Firewall section entries have a unique `Priority`; IPS section entries don't. The policy definition is in a local file named `policy.json`:

```
{
    "FirewallRuleGroupEntries": [
        { "Priority": 1, "ResourceArn": "arn:aws:network-firewall:us-west-2:111122223333:firewall-rulegroup/example-firewall-rule-group" },
        {
            "Priority": 2,
            "InlineRuleGroup": {
                "RulesSource": {
                    "RulesString": "accept:flow tcp:all any any -> any 443 (sid:1001;)\n"
                }
            }
        }
    ],
    "IpsRuleGroupEntries": [
        { "ResourceArn": "arn:aws:network-firewall:us-west-2:111122223333:ips-rulegroup/example-ips-rule-group" },
        {
            "InlineRuleGroup": {
                "RulesSource": {
                    "RulesString": "drop http any any -> any any (msg:\"block evil host\"; http.host; content:\"evil.example.com\"; sid:2001; rev:1;)\n"
                }
            }
        }
    ],
    "PolicyMode": "ENFORCE",
    "FirewallDefaultAction": "DROP"
}
```

```sh
aws network-firewall create-firewall-policy-v2 \
--firewall-policy-v2-name example-policy \
--firewall-policy-v2 file://policy.json \
--region us-west-2
```

The following shows an example response. The `UpdateToken` is required for subsequent update and delete calls, and the `ConsumedFirewallRuleCapacity` and `ConsumedIpsRuleCapacity` fields report how much of each section's capacity the policy uses.

```
{
    "UpdateToken": "3e965e1d-2b9f-40c2-a218-5aabe88b4b2e",
    "FirewallPolicyV2Response": {
        "FirewallPolicyV2Name": "example-policy",
        "FirewallPolicyV2Arn": "arn:aws:network-firewall:us-west-2:111122223333:firewall-policy-v2/example-policy",
        "FirewallPolicyV2Id": "745d879a-7813-4839-af58-e129de777454",
        "FirewallPolicyV2Status": "ACTIVE",
        "ConsumedFirewallRuleCapacity": 101,
        "ConsumedIpsRuleCapacity": 101,
        "ConsumedIpsDomainCapacity": 0,
        "EncryptionConfiguration": { "KeyId": "AWS_OWNED_KMS_KEY", "Type": "AWS_OWNED_KMS_KEY" },
        "LastModifiedTime": "2026-10-15T20:50:42.409000+00:00"
    }
}
```

**Note**  
A firewall rule group that you reference must already be active before you can reference it in a policy. The Next Generation policy operations use dedicated commands—`create-firewall-policy-v2`, `describe-firewall-policy-v2`, `update-firewall-policy-v2`, `list-firewall-policies-v2`, and `delete-firewall-policy-v2`. The commands for Classic Network Firewall policies don't operate on Next Generation policies.