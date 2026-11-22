

# Automated Allowlists

With Automated Allowlists, DNS Firewall helps you build an allowlist of domains from the DNS query traffic of your VPCs. An Automated Allowlist rule is a rule type with the `ALLOW` action. DNS Firewall creates a domain list for the rule and shows you the domains that it observes in your DNS query traffic. You review the observed domains and add the domains that you want to allow.

Use Automated Allowlists when you want to allow only known domains and block all others (a *walled garden*), but you don't know in advance every domain that your workloads need.

## How Automated Allowlists work
<a name="firewall-advanced-automated-allowlists-how-it-works"></a>

DNS Firewall observes DNS queries from every VPC that the rule group is associated with. This includes VPCs that use the rule group through Route 53 Profiles, and VPCs in other accounts that you share the rule group with through AWS Firewall Manager or AWS Resource Access Manager (AWS RAM).

When you create the rule, DNS Firewall lists the domains that your VPC clients queried during the look-back period that you choose, including queries that were allowed. After that, DNS Firewall adds a domain to the list of observed domains when any DNS Firewall rule blocks a query for it from an associated VPC. This includes rules in other rule groups, such as rules that block known threats. Review these domains before you allow them. You can then add an observed domain to the rule's domain list so that DNS Firewall allows queries for it. If the answer for a domain includes a redirection chain, such as a CNAME record, you also need to allow the redirection targets. For more information, see [Considerations for Automated Allowlists](#firewall-advanced-automated-allowlists-considerations).

A typical walled-garden rule group contains the following rules:

1. (Optional) Rules that block known threats, with the highest priority (the lowest numeric priority settings), so that adding an observed domain to the allowlist can't override a threat block.

1. An Automated Allowlist rule with a higher priority (a lower numeric priority setting) than the rule that blocks all other domains.

1. A rule with a lower priority that blocks all other domains, using a domain list that contains the wildcard `*`.

Each domain that DNS Firewall tracks for an Automated Allowlist rule has one of the following statuses:
+ `OBSERVED` – Domains that DNS Firewall observed in your DNS query traffic. When you create the rule, DNS Firewall adds the domains that your VPCs queried during the look-back period that you specify, including queries that were allowed. After that, DNS Firewall adds domains when a DNS Firewall rule blocks a query for them. Review these domains to decide which ones to allow. Domains from the look-back period that your VPCs keep querying, and that no rule blocks, move to `ALLOWED` within about a day after you create the rule, so review the observed domains soon after the rule is created.
+ `ALLOWED` – Domains that DNS Firewall allowed queries for, whether or not they're in the rule's domain list.
+ `DENIED` (**Rejected** in the console) – Domains that you chose not to add to the allowlist. If your VPCs still query a rejected domain and no rule blocks it, the domain can move to `ALLOWED`. If a rule later blocks it, it can appear in the observed domains again.

The `ALLOWED` status isn't the allowlist itself. In the console, the **Analysis** tab shows the domains that DNS Firewall allowed queries for, with their request counts, and DNS Firewall updates this information every hour. The **Allowed domains** view on the **Domain list** tab shows the rule's domain list, which is the allowlist that DNS Firewall enforces.

## Considerations for Automated Allowlists
<a name="firewall-advanced-automated-allowlists-considerations"></a>

Note the following when you use Automated Allowlists:
+ A rule group can contain only one Automated Allowlist rule.
+ The rule action is always `ALLOW`, and the rule applies to all DNS query types.
+ Automated Allowlist rules are Regional.
+ DNS Firewall keeps up to 10,000 domains in each status for a rule. When a status is full, DNS Firewall doesn't add new domains to it, even domains with a lot of traffic, until existing domains in that status stop receiving queries.
+ Domains in the `OBSERVED`, `ALLOWED`, and `DENIED` statuses are always fully qualified domain names. In the rule's domain list, you can also add wildcard domains, such as `*.example.com`, to allow all subdomains of a domain. DNS Firewall doesn't expand a wildcard domain into separate entries. Traffic for each matching subdomain still appears on the **Analysis** tab in the console. An observed domain that matches a wildcard domain that you just added can remain in the `OBSERVED` status for up to an hour.
+ The rule's domain list counts toward your domain list and domain quotas. You can't delete the list directly, use it in another rule, replace its contents, or import domains into it.
+ Only the owner of the rule group can view the observed domains. For shared rule groups, DNS Firewall combines the traffic from all VPCs and doesn't show which VPC or account queried a domain.
+ If you associate a VPC with the rule group after you create the rule, DNS Firewall doesn't analyze that VPC's past DNS query traffic. It adds only domains from queries that the VPC makes after the association.
+ When you delete the rule, DNS Firewall also deletes the rule's domain list. If you create a new Automated Allowlist rule, it gets a new domain list and doesn't keep the previous rule's observed or rejected domains.
+ Observed domains can include domains that other rules blocked, including rules in other rule groups that block known threats. When a rule matches a query, DNS Firewall stops evaluating, so if the Automated Allowlist rule runs before a threat rule, adding such a domain lets queries for it resolve. To prevent this, put rules that block known threats in the same rule group as the Automated Allowlist rule, with a higher priority (a lower numeric priority setting). For threat rules in another rule group, associate that rule group with your VPCs at a lower priority number than the Automated Allowlist rule's rule group. You can't move a rule group that Firewall Manager associates as a last rule group ahead of your other rule groups. For more information, see [Managing associations between your VPC and Resolver DNS Firewall rule group](resolver-dns-firewall-vpc-associating-rule-group.md).

  If the threat rules reach your VPCs through a different Route 53 Profile than the Automated Allowlist rule, a rule group's priority in one Profile doesn't order it against a rule group in the other Profile. Instead, put the threat rules in the same Profile at a lower priority number than the Automated Allowlist rule's rule group, associate them directly with your VPCs at a lower priority number, or use a Profile with a lower priority number. Changing a Profile's priority also changes which Profile's Resolver rules and private hosted zones apply to your VPCs. For more information, see [How Route 53 Profile settings are prioritized](profiles.md#profiles-priority).
+ The Automated Allowlist rule always inspects the domains in a DNS redirection chain, such as the targets of CNAME records. Observed domains and the **Analysis** tab show only the domain names that your VPCs queried, not the targets in the answers. Before you add a rule that blocks all other domains, check the answers in the Resolver query logs for the VPCs that use the rule group, and add the redirection targets, or a wildcard domain that covers them, to the allowlist. Otherwise, queries for those domains are blocked. For VPCs in other accounts, the answers are in the query logs of the query logging configurations that those VPCs use, for example a configuration that you share with those accounts through AWS RAM. Query logs contain only queries that VPCs make after you configure logging. For more information, see [Resolver query logging](resolver-query-logs.md) and [Rule settings in DNS Firewall](resolver-dns-firewall-rule-settings.md).

## Creating an Automated Allowlist rule
<a name="firewall-advanced-automated-allowlists-create"></a>

When you create the rule, you choose the look-back period for the DNS query traffic that DNS Firewall uses to build the first set of observed domains, from 1 hour to 1 week. You can't change this setting after you create the rule.

If you already use a walled-garden setup with your own allowlist, you can optionally start the Automated Allowlist rule with the domains from that domain list. This is a one-time copy, and afterward the two lists are independent. The source must be a completed, Regional domain list that you own, not an AWS managed domain list or another Automated Allowlist domain list. Imported domains are added to the rule's domain list. While the import runs, the status of the rule's domain list is `IMPORTING`, and then it changes to `COMPLETE`, or to `COMPLETE_IMPORT_FAILED` if the import fails. You can't add, remove, or reject domains until the import finishes.

DNS Firewall creates a domain list for the rule, named `AutoAllowlist - {{rule-name}}`. The rule status is `CREATING` while DNS Firewall builds the first set of observed domains, and changes to `COMPLETE` (**Created** in the console) when they're ready.

For general information about rules, see [Creating a rule group and rules](resolver-dns-firewall-rule-group-adding.md) and [Rule settings in DNS Firewall](resolver-dns-firewall-rule-settings.md).

------
#### [ Console ]

Before you start, you need a rule group that's associated with one or more VPCs. The rule group can be empty or can already contain rules. For more information, see [Creating a rule group and rules](resolver-dns-firewall-rule-group-adding.md) and [Managing associations between your VPC and Resolver DNS Firewall rule group](resolver-dns-firewall-vpc-associating-rule-group.md).

**To add an Automated Allowlist rule**

1. Open the Amazon VPC console. In the navigation pane, under **DNS Firewall**, choose **Rule groups**. Choose the name of your rule group, and then on the **Rules** tab, choose **Add rule**.

1. Under **Rule details**, enter a **Name** for the rule. For **Tier option**, choose **Advanced**.

1. Under **Rule configurations**, for **Rule type**, choose **Automated allow list**.

1. For **Analysis timeframe**, choose the look-back period for the DNS query traffic that DNS Firewall analyzes to find observed domains, from 1 hour to 1 week. You can't change the timeframe after you create the rule.

1. (Optional) For **Import a domain list**, choose an existing domain list to copy into the allowlist. This is a one-time copy. Afterward, the two lists are independent.

1. Under **Action**, the action is always **ALLOW**. Choose **Add rule**.

   The rule appears on the **Rules** tab with the rule type **Automated allow list** and the status **Creating**. The console gives the rule the next available priority, after any existing rules in the rule group. If the rule group already has a rule that blocks all other domains, change the priority of that rule to a higher number than the Automated Allowlist rule's priority, so that the Automated Allowlist rule runs first. You can't change the Automated Allowlist rule until its status is **Created**.

1. (Optional) After you review the observed domains and add the ones that your workloads need to the allowlist, add a rule that blocks all other domains. Before you add it, compare the **Analysis** tab with **Allowed domains** to find domains that your workloads need that aren't in the allowlist yet. Also add the redirection targets from the Resolver query logs for the VPCs that use the rule group. The **Analysis** tab might not show every domain if a status is full, so also check the query names in those query logs for domains that the allowlist and its wildcard domains don't cover yet. Use a domain list that contains the wildcard `*`, set the action to **BLOCK**, and give the rule a higher priority number than the Automated Allowlist rule. For an example, see [Resolver DNS Firewall walled garden example](resolver-dns-firewall-getting-started.md#dns-firewall-walled-garden-example).

To review the observed domains, choose **View domain list** in the success message, or choose the rule's **Resource value**.

------
#### [ CLI ]

You can create an Automated Allowlist rule by running a AWS CLI command like the following and using your own values. Use `--priority` to set the rule's priority. To start the allowlist with the domains from an existing domain list, add `"ImportFromFirewallDomainListId":"{{domain-list-id}}"` to `AutoAllowlist`.

```bash
aws route53resolver create-firewall-rule \
    --creator-request-id my-request-id \
    --firewall-rule-group-id rslvr-frg-0123456789example \
    --name my-automated-allowlist \
    --priority 100 \
    --action ALLOW \
    --firewall-rule-type '{"AutoAllowlist":{"InitialDataTimeframeHours":24}}'
```

The response includes the rule's `FirewallThreatProtectionId` and, in `FirewallRuleType`, the `AutoAllowlistFirewallDomainListId` of the rule's domain list. You use these IDs to review and update domains. For more information, see [create-firewall-rule](https://docs.aws.amazon.com/cli/latest/reference/route53resolver/create-firewall-rule.html) in the *AWS CLI Command Reference*.

------

## Reviewing and approving domains
<a name="firewall-advanced-automated-allowlists-review"></a>

You can view the domains for a rule by status. You can filter them by part of a domain name, and sort them by the time the domain was added, by requests in the last 24 hours, or by total requests.

DNS Firewall keeps up to 10,000 domains in each status for a rule. When a status is full, DNS Firewall doesn't add new domains to it until existing domains stop receiving queries, so the list and the **Analysis** tab might not include every domain that your VPCs query. For more information, see [Considerations for Automated Allowlists](#firewall-advanced-automated-allowlists-considerations).

------
#### [ Console ]

**To review and approve domains**

1. On the rule group's **Rules** tab, find the Automated Allowlist rule. When its **Status** is **Created**, choose the domain list ID in the **Resource value** column.

1. On the domain list page, on the **Domain list** tab, choose **Observed domains**.

1. Review the observed domains. For each domain, the table shows **Total requests**, **Daily frequency**, and **Date first observed**. To find specific domains, use **Filter resources** or sort by a column.

1. To allow domains, select them, and then choose **Add to allow list**. Allowing a domain can take up to 1 hour to take effect. While DNS Firewall applies the change, the **Domain list status** is **Updating**.

1. To reject domains, select them, and then choose **Reject**. Rejected domains appear under **Rejected domains**. To allow a rejected domain later, select it there, and then choose **Add to allow list**.

1. To see the domains that DNS Firewall allowed queries for, choose the **Analysis** tab. For each allowed domain, the table shows **Total requests**, **Daily frequency**, and **Date first observed**.

------
#### [ CLI ]

You can list the observed domains for a rule, with the most requested domains first, by running a AWS CLI command like the following and using your own values. To list allowed or denied domains, set `DomainStatus` to `ALLOWED` or `DENIED`. `ALLOWED` lists the domains that DNS Firewall allowed queries for, whether or not they're in the rule's domain list.

```bash
aws route53resolver list-firewall-rule-domains \
    --firewall-rule-group-id rslvr-frg-0123456789example \
    --firewall-threat-protection-id 0123456789example \
    --query-options DomainStatus=OBSERVED,SortBy=TOTAL_REQUESTS,SortOrder=DESC
```

The following is an example output after you run the command:

```json
{
    "Domains": [
        {
            "DomainName": "example.com",
            "DomainStatus": "OBSERVED",
            "Last24HourRequests": 2000,
            "TotalRequests": 15000,
            "AddedTime": "2026-11-16T10:00:00Z"
        }
    ]
}
```

For more information, see [list-firewall-rule-domains](https://docs.aws.amazon.com/cli/latest/reference/route53resolver/list-firewall-rule-domains.html) in the *AWS CLI Command Reference*.

To list the domains in the allowlist itself, specify the rule's domain list instead:

```bash
aws route53resolver list-firewall-rule-domains \
    --firewall-rule-group-id rslvr-frg-0123456789example \
    --firewall-domain-list-id rslvr-fdl-0123456789example
```

------

## Updating domains in an allowlist
<a name="firewall-advanced-automated-allowlists-update"></a>

You can make the following updates to the rule's domain list:
+ `ADD` – Approves a domain. You can also add domains that DNS Firewall hasn't observed, including wildcard domains.
+ `REMOVE` – Removes a domain from the allowlist.
+ `DENY` – Rejects an observed domain. If the domain is in the allowlist, DNS Firewall also removes it. `DENY` accepts exact domain names only, not wildcards.

------
#### [ Console ]

**To add domains to an allowlist**

1. On the domain list page, on the **Domain list** tab, choose **Allowed domains**, and then choose **Add domains**.

1. Under **Enter one domain per line**, enter up to 1,000 domains. You can add domains that DNS Firewall hasn't observed. To allow all subdomains of a domain, start the name with an asterisk, for example `*.example.com`.

1. Choose **Add**. The domains appear under **Allowed domains**. Allowing a domain can take up to 1 hour to take effect.

1. (Optional) After you add the domains that your workloads need, add a rule that blocks all other domains, if the rule group doesn't already have one. Before you add it, compare the **Analysis** tab with **Allowed domains** to find domains that your workloads need that aren't in the allowlist yet. Also add the redirection targets from the Resolver query logs for the VPCs that use the rule group. The **Analysis** tab might not show every domain if a status is full, so also check the query names in those query logs for domains that the allowlist and its wildcard domains don't cover yet. Use a domain list that contains the wildcard `*`, set the action to **BLOCK**, and give the rule a higher priority number than the Automated Allowlist rule. For an example, see [Resolver DNS Firewall walled garden example](resolver-dns-firewall-getting-started.md#dns-firewall-walled-garden-example).

To change or remove a domain, select it under **Allowed domains**, and then choose **Edit** or **Delete**.

------
#### [ CLI ]

You can approve observed domains by running a AWS CLI command like the following and using your own values. To remove or reject domains, set `--operation` to `REMOVE` or `DENY`.

```bash
aws route53resolver update-firewall-domains \
    --firewall-domain-list-id rslvr-fdl-0123456789example \
    --operation ADD \
    --domains example.com "*.example.org"
```

For more information, see [update-firewall-domains](https://docs.aws.amazon.com/cli/latest/reference/route53resolver/update-firewall-domains.html) in the *AWS CLI Command Reference*.

------

## Pricing
<a name="firewall-advanced-automated-allowlists-pricing"></a>

Automated Allowlist rules are billed as DNS Firewall Advanced rules. For more information, see [Amazon Route 53 Pricing](https://aws.amazon.com/route53/pricing/).