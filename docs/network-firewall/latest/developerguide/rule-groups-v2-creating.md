

# Creating a rule group for a Next Generation policy
<a name="rule-groups-v2-creating"></a>

Use the following procedure to create a firewall rule group or an IPS rule group in the console. The pages that you see after you select the rule group type depend on the type and, for a firewall rule group, on the authoring format that you select.

**To create a rule group for a Next Generation policy**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

   In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**, and then choose **Create rule group**.

1. On the **Describe rule group** page, enter a **Name** to identify this rule group (you can't change the name after you create the rule group), and optionally a **Description**, a AWS Key Management Service customer managed key under **Customer managed key** to encrypt your resources instead of using an AWS owned key (see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md)), and tags under **Add tags** (see [Tagging AWS Network Firewall resources](tagging.md)). Then choose **Next**.

1. On the **Choose rule group type** page, for **Rule group version**, leave **Next Generation** selected (to create a Classic Network Firewall rule group instead, select **Classic** and follow the procedure in [Creating a stateful rule group](rule-group-stateful-creating.md)). Under **Rule group type**, select the inspection engine—**Firewall rule group** (the default) for the firewall engine or **IPS rule group** for the IPS engine. For **Rule group format**, select how to author the rules: a firewall rule group supports **Visual rule builder** (the default), **Text rule builder**, or **Domain list**, and an IPS rule group supports only **Text rule builder**. For information about the rule formats, see [Authoring firewall rules](firewall-rule-groups-authoring.md) and [Generating firewall rules from domain names](firewall-rule-groups-fqdn.md). Then choose **Next**.

1. (Optional) On the **Rule group variables** page, define the rule variables that your rules reference. For an IPS rule group, you can also define IP set references. Then choose **Next**. This page appears for the **Visual rule builder** and **Text rule builder** formats; it doesn't appear for the **Domain list** format.

1. On the **Configure rules** page, provide the rules for the rule group. For the **Visual rule builder**, build each rule from structured fields—choosing a rule template, action, protocol and connection state, action scope, source and destination, and rule options—and choose **Add rule** to add it to the **Firewall rules** table; for the **Text rule builder**, enter your rules under **Suricata compatible rule string**; and for a **Domain list**, enter the domain names and matching options. Then, in the **Capacity** section, set the capacity with **Allow room to grow** (recommended), **Match current rules**, or **Custom capacity** (a value from 1 to 30,000); you can't change the capacity after you create the rule group. For information about authoring rules, templates, and capacity, see [Authoring firewall rules](firewall-rule-groups-authoring.md), [Generating firewall rules from domain names](firewall-rule-groups-fqdn.md), [Setting rule group capacity in AWS Network Firewall](rule-group-capacity-v2.md), and [AWS Network Firewall quotas](quotas.md). Then choose **Next**.

1. On the **Review and create** page, review the rule group, then choose **Create**.

You can also create a rule group with the AWS CLI. Both rule group types use the `create-rule-group` command with the `--type` parameter: `FIREWALL` for a firewall rule group and `IPS` for an IPS rule group. The `describe-rule-group`, `update-rule-group`, and `delete-rule-group` commands require the matching `--type`.

The following example creates a firewall rule group from a rule string. The rule group definition is in a local file named `firewall-rules.json`:

```
{ "RulesSource": { "RulesString": "accept:flow tcp:all any any -> any 443 (sid:1001;)\n" } }
```

```
aws network-firewall create-rule-group \
--type FIREWALL --capacity 100 \
--rule-group-name example-firewall-rule-group \
--firewall-rule-group file://firewall-rules.json \
--region us-west-2
```

The following example creates an IPS rule group. The rules use the same Suricata-compatible syntax as a Classic Network Firewall stateful rule group, and the definition is in a local file named `ips-rules.json`:

```
{ "RulesSource": { "RulesString": "drop http any any -> any any (msg:\"block evil host\"; http.host; content:\"evil.example.com\"; sid:2001; rev:1;)\n" } }
```

```
aws network-firewall create-rule-group \
--type IPS --capacity 100 \
--rule-group-name example-ips-rule-group \
--ips-rule-group file://ips-rules.json \
--region us-west-2
```

Each create call returns an `UpdateToken` that you provide on a subsequent `update-rule-group` or `delete-rule-group` call for the rule group. The token changes with every update.