# Sharing Resolver query logging configurations with other AWS accounts

You can share the query logging configurations that you created using one AWS account with other AWS accounts. To share configurations, the
Route 53 Resolver console integrates with AWS Resource Access Manager. For more information about Resource Access Manager, see the [Resource Access Manager User Guide](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

Note the following:

**Associating VPCs with shared query logging configurations**

If another AWS account has shared one or more configurations with your account, you can associate VPCs with the configuration the
same way that you associate VPCs with configurations that you created.

**Deleting or unsharing a configuration**

If you share a configuration with other accounts and then either delete the configuration or stop sharing it, and if one or more
VPCs were associated with the configuration, Route 53 Resolver stops logging DNS queries that originate in those VPCs.

**Maximum number of query logging configurations and VPCs that can be associated with a config**

When an account creates a configuration and shares it with one or more
other accounts, the maximum number of VPCs that can be associated
with the configuration are applied per account. For example, if you
have 10,000 accounts in your organization, you can create the query
logging configuration in the central account and share it via AWS RAM to
share it to the organization accounts. The organization accounts
will then associate the configuration with their VPCs counting them
against their account’s query log configuration VPC associations per
AWS Region limit of 100. However, if all the VPCs are in a single
account, then the account’s service limits might be needed to
increased.

For current Resolver quotas, see [Quotas on Route 53 Resolver](DNSLimitations.md#limits-api-entities-resolver "DNSLimitations.md#limits-api-entities-resolver").

**Permissions**

To share a rule with another AWS account, you must have permission to use the [PutResolverQueryLogConfigPolicy](../APIReference/API_route53resolver_PutResolverQueryLogConfigPolicy.md "../APIReference/API_route53resolver_PutResolverQueryLogConfigPolicy.md")
action.

**Restrictions on the AWS account that a rule is shared with**

The account that a rule is shared with can't change or delete the rule.

**Tagging**

Only the account that created a rule can add, delete, or see tags on the rule.

To view the current sharing status of a rule (including the account that shared the rule or the account that a rule is shared with), and to
share rules with another account, perform the following procedure.

###### To view sharing status and share query logging configurations with another AWS

account

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Query Logging**.
3. On the navigation bar, choose the Region where you created the rule.

The **Sharing status** column shows the current sharing status of rules that were created by the current account or
that are shared with the current account:

    * **Not shared**: The current AWS account created the rule, and the rule is not shared with any
     other accounts.
    * **Shared by me**: The current account created the rule and shared it with one or more
     accounts.
    * **Shared with me**: Another account created the rule and shared it with the current
     account.

4. Choose the name of the rule that you want to display sharing information for or that you want to share with another account.

On the **Rule: `rule name`** page, the value under **Owner** displays ID of
the account that created the rule. That's the current account unless the value of **Sharing status** is
**Shared with me**. In that case, **Owner** is the account that created the rule and shared it
with the current account.

The sharing status is also displayed. 5. Choose **Share configuration** to open the AWS RAM console 6. To create a resource share, follow the steps in
[Creating a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM user guide_.

###### Note

You can't update sharing settings. If you want to change any of the following settings, you must reshare a rule with the new
settings and then remove the old sharing settings.
