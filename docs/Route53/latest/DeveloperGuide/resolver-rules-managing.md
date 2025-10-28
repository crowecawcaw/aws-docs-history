# Managing forwarding rules

If you want Resolver to forward queries for specified domain names to your network, you create one forwarding rule
for each domain name and specify the name of the domain for which you want to forward queries.

###### Topics

- [Viewing and editing forwarding rules](#resolver-rules-managing-viewing "#resolver-rules-managing-viewing")
- [Creating forwarding rules](#resolver-rules-managing-creating-rules "#resolver-rules-managing-creating-rules")
- [Adding rules for reverse lookup](#add-reverse-lookup "#add-reverse-lookup")
- [Associating forwarding rules with a VPC](#resolver-rules-managing-associating-rules "#resolver-rules-managing-associating-rules")
- [Disassociating forwarding rules from a VPC](#resolver-rules-managing-disassociating-rules "#resolver-rules-managing-disassociating-rules")
- [Sharing Resolver rules with other AWS accounts and using shared rules](#resolver-rules-managing-sharing "#resolver-rules-managing-sharing")
- [Deleting forwarding rules](#resolver-rules-managing-deleting "#resolver-rules-managing-deleting")
- [Forwarding rules for
  reverse DNS queries in Resolver](#resolver-automatic-forwarding-rules-reverse-dns "#resolver-automatic-forwarding-rules-reverse-dns")

## Viewing and editing forwarding rules

To view and edit settings for a forwarding rule, perform the following procedure.

###### To view and edit settings for a forwarding rule

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Rules**.
3. On the navigation bar, choose the Region where you created the rule.
4. Choose the option for the rule that you want to view settings for or want to edit.
5. Choose **View details** or **Edit**.

For information about the values for forwarding rules, see
[Values that you specify when you create or edit rules](resolver-forwarding-outbound-queries-rule-values.md "resolver-forwarding-outbound-queries-rule-values.md"). 6. If you chose **Edit**, enter the applicable values, and then choose **Save**.

## Creating forwarding rules

To create one or more forwarding rules, perform the following procedure.

###### To create forwarding rules and

associate the rules with one or more VPCs

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Rules**.
3. On the navigation bar, choose the Region where you want to create the rule.
4. Choose **Create rule**.
5. Enter the applicable values. For more information, see
   [Values that you specify when you create or edit rules](resolver-forwarding-outbound-queries-rule-values.md "resolver-forwarding-outbound-queries-rule-values.md").
6. Choose **Save**.
7. To add another rule, repeat steps 4 through 6.

## Adding rules for reverse lookup

If you need to control reverse lookups in your VPC, you can add rules to your outbound
resolver endpoint.

###### To create the reverse lookup rule

1. Follow the steps in the previous procedure, up to step 5.
2. When you specify your rule, enter the PTR record for the IP address or addresses that you
   want a reverse lookup forwarding rule for.

For example, if you need to forward lookups for addresses in the
10.0.0.0/23 range, enter two rules:

    * 0.0.10.in-addr.arpa
    * 1.0.10.in-addr.arpa

Any IP address in those subnets will be referenced as a subdomain of those
PTR records—for example, 10.0.1.161 will have a reverse lookup
address of 161.1.0.10.in-addr.arpa, which is a subdomain of
1.0.10.in-addra.arpa. 3. Specify the server to forward these lookups to. 4. Add these rules to your outbound resolver endpoint.

Note that turning on `enableDNSHostNames` for your VPC automatically adds PTR records. See [What is Amazon Route 53 Resolver?](resolver.md "resolver.md"). The previous procedure is required only if you want to explicitly specify a resolver for given IP ranges—for example, when forwarding
queries to an Active Directory server.

## Associating forwarding rules with a VPC

After you create a forwarding rule, you must associate the rule with one or more VPCs. The rules will only work after they are
associated with a VPC. When you associate a rule with
a VPC, Resolver starts to forward DNS queries for the domain name that's specified in the rule to the DNS resolvers
that you specified in the rule. The queries pass through the outbound endpoint that you specified when you created
the rule.

###### To associate a forwarding rule with one or more VPCs

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Rules**.
3. On the navigation bar, choose the Region where you created the rule.
4. Choose the name of the rule that you want to associate with one or more VPCs.
5. Choose **Associate VPC**.
6. Under **VPCs that use this rule**, choose the VPCs that you want to associate the rule with.
7. Choose **Add**.

## Disassociating forwarding rules from a VPC

You disassociate a forwarding rule from a VPC in the following circumstances:

- For DNS queries that originate in this VPC, you want Resolver to stop forwarding queries
  for the domain name specified in the rule to your network.
- You want to delete the forwarding rule. If a rule is currently associated with one or more VPCs, you must
  disassociate the rule from all VPCs before you can delete it.

If you want to disassociate a forwarding rule from one or more VPCs, perform the following procedure.

###### To disassociate a forwarding rule from a VPC

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Rules**.
3. On the navigation bar, choose the Region where you created the rule.
4. Choose the name of the rule that you want to disassociate from one or more VPCs.
5. Choose the option for the VPC that you want to disassociate the rule from.
6. Choose **Disassociate**.
7. Type **disassociate** to confirm.
8. Choose **Submit**.

## Sharing Resolver rules with other AWS accounts and using shared rules

You can share the Resolver rules that you created using one AWS account with other AWS accounts. To share rules,
the Route 53 Resolver console integrates with AWS Resource Access Manager. For more information about Resource Access Manager, see the
[Resource Access Manager User Guide](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

Note the following:

**Associating shared rules with VPCs**
If another AWS account has shared one or more rules with your account, you can associate the rules
with your VPCs the same way that you associate rules that you created with your VPCs. For more information, see
[Associating forwarding rules with a VPC](#resolver-rules-managing-associating-rules "#resolver-rules-managing-associating-rules").

**Deleting or unsharing a rule**
If you share a rule with other accounts and then either delete the rule or stop sharing it,
and if the rule was associated with one or more VPCs, Route 53 Resolver starts to process DNS queries for those VPCs
based on the remaining rules. The behavior is the same as if you disassociate the rule from the VPC.

If a rule is shared to an Organizational Unit (OU) and an account in the OU is moved to a different OU,
all associations with the shared rule to any VPC in the account will be deleted.
However, if the Resolver rule was already shared with destination OU, then the VPC association will stay intact and will not be dissociated.

**Maximum number of rules and associations**
When an account creates a rule and shares it with one or more other accounts, the maximum
number of rules per AWS Region applies to the account that created the rule.

When an account that a rule is shared with associates the rule with one or more VPCs, the maximum
number of associations between rules and VPCs per Region applies to the account that the rule is shared with.

For current Resolver quotas, see
[Quotas on Route 53 Resolver](DNSLimitations.md#limits-api-entities-resolver "DNSLimitations.md#limits-api-entities-resolver").

**Permissions**
To share a rule with another AWS account, you must have permission to use the
[PutResolverRulePolicy](../APIReference/API_route53resolver_PutResolverRulePolicy.md "../APIReference/API_route53resolver_PutResolverRulePolicy.md") action.

**Restrictions on the AWS account that a rule is shared with**
The account that a rule is shared with can't change or delete the rule.

**Tagging**
Only the account that created a rule can add, delete, or see tags on the rule.

To view the current sharing status of a rule (including the account that shared the rule or
the account that a rule is shared with), and to share rules with another
account, perform the following procedure.

###### To view sharing status and share rules with another AWS account

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Rules**.
3. On the navigation bar, choose the Region where you created the rule.

The **Sharing status** column shows the current sharing status of rules that were created by the
current account or that are shared with the current account:

    * **Not shared**: The current AWS account created the rule, and the rule
     is not shared with any other accounts.
    * **Shared by me**: The current account created the rule and shared it with
     one or more accounts.
    * **Shared with me**: Another account created the rule and shared it with
     the current account.

4. Choose the name of the rule that you want to display sharing information for or that you want to share with
   another account.

On the **Rule: `rule name`** page, the value under **Owner**
displays ID of the account that created the rule. That's the current account unless the value of **Sharing status**
is **Shared with me**. In that case, **Owner** is the account that created the rule and
shared it with the current account. 5. Choose **Share** to view additional information or to share the rule with another account.
A page in the Resource Access Manager console appears, depending on the value of **Sharing status**:

    * **Not shared**: The **Create resource share** page
     appears. For information about how to share the rule with another account, OU, or organization, skip to step 6.
    * **Shared by me**: The **Shared resources** page shows
     the rules and other resources that are owned by the current account and shared with other accounts.
    * **Shared with me**: The **Shared resources** page shows
     the rules and other resources that are owned by other accounts and shared with the current account.

6. To share a rule with another AWS account, OU, or organization, specify the following values.

###### Note

You can't update sharing settings. If you want to change any of the following settings, you must
reshare a rule with the new settings and then remove the old sharing settings.

**Description**
Enter a short description that helps you remember why you shared the rule.

**Resources**
Choose the check box for the rule that you want to share.

**Principals**
Enter the AWS account number, OU name, or organization name.

**Tags**
Specify one or more keys and the corresponding values. For example, you might specify
**Cost center** for **Key** and specify **456** for **Value**.

These are the tags that AWS Billing and Cost Management provides for organizing your AWS bill; you can use also tags for other purposes.
For more information about using tags for cost allocation, see
[Using cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
in the _AWS Billing User Guide_.

## Deleting forwarding rules

To delete a forwarding rule, perform the following procedure.

Note the following:

- If the forwarding rule is associated with any VPCs, you must disassociate the rule from the VPCs
  before you can delete the rule. For more information, see
  [Disassociating forwarding rules from a VPC](#resolver-rules-managing-disassociating-rules "#resolver-rules-managing-disassociating-rules").
- You can't delete the default **Internet Resolver** rule, which has a value of **Recursive**
  for **Type**. This rule causes Route 53 Resolver to act as a recursive resolver for any domain names that you didn't
  create custom rules for and that Resolver didn't create autodefined rules for. For more information about how rules are categorized, see
  [Using rules to control which queries are forwarded
  to your network](resolver-overview-forward-vpc-to-network-using-rules.md "resolver-overview-forward-vpc-to-network-using-rules.md").

###### To delete a forwarding rule

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Rules**.
3. On the navigation bar, choose the Region where you created the rule.
4. Choose the option for the rule that you want to delete.
5. Choose **Delete**.
6. To confirm that you want to delete the rule, enter the name of the rule and choose **Submit**.

## Forwarding rules for

reverse DNS queries in Resolver

When the `enableDnsHostnames` and `enableDnsSupport` are set to
`true` for a virtual private cloud (VPC) from Amazon VPC, Resolver
automatically creates auto-defined system rules for reverse DNS queries. For more
information about these settings, see [DNS attributes in your
VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support") in the _Amazon VPC Developer Guide_.

Forwarding rules for reverse DNS queries are particularly useful for services like SSH
or Active Directory, which have an option to authenticate users by performing a reverse
DNS lookup for the IP address from which a customer is attempting to connect to a
resource. For more information about auto-defined system rules, see [Domain names that Resolver creates autodefined system rules for](resolver-overview-forward-vpc-to-network-autodefined-rules.md "resolver-overview-forward-vpc-to-network-autodefined-rules.md").

You can turn off these rules and modify all reverse DNS queries so that they are, for
example, forwarded to your on-premises name servers for resolution.

After you turn off the automatic rules, create rules to forward the queries as needed to
your on-premises resources. For more information about how to manage forwarding
rules, see [Managing forwarding rules](resolver-rules-managing.md "resolver-rules-managing.md").

###### To turn off auto-defined

rules

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, under **Resolver** choose
   **VPCs**, and then choose a VPC ID.
3. Under **Autodefined rules for reverse DNS resolution**, deselect the
   check box. If the check box is already deselected, you can select it to turn
   on auto-defined reverse DNS resolution.

For the related APIs, see [Resolver configuration APIs](../APIReference/API-actions-by-function.md#actions-by-function-resolver-configuration "../APIReference/API-actions-by-function.md#actions-by-function-resolver-configuration").
