# Managing IP/VPC restrictions

## Turning on Internet Protocol

(IP) and VPC endpoint restrictions in Amazon Quick Suite

You can limit access to your organization's Amazon Quick Suite account to a predefined list
of IP ranges, VPC IDs, and VPC endpoint IDs. For example, you can create an IP rule that
allows users to access your Quick Suite account only from IP addresses associated
with your company's office or remote virtual private network (VPN). You can also
create a VPC endpoint rule that allows users access to your Quick Suite account
only from the VPC that is used for AWS Direct Connect.

For more information about setting up VPC endpoints in Quick Suite, see [Quick Suite Interface VPC endpoints (AWS PrivateLink)](../../../quicksight/latest/developerguide/vpc-interface-endpoints.md "../../../quicksight/latest/developerguide/vpc-interface-endpoints.md") for more
information about how to setup VPC endpoints.

Only admins with AWS Identity and Access Management (IAM) credentials who have access to the
Quick Suite console pages can access the IP and VPC endpoint restrictions
table.

###### Topics

- [Adding an IP or VPC endpoint rule](#adding-a-rule "#adding-a-rule")
- [Update an existing rule](#update-a-rule "#update-a-rule")
- [Delete a rule](#delete-a-rule "#delete-a-rule")
- [Turning on your IP and VPC endpoint
  rules](#enabling-ip-rules "#enabling-ip-rules")

### Adding an IP or VPC endpoint rule

An _IP rule_ is created when you add a CIDR
address with a public IP version 4 address to the restrictions table. A VPC endpoint
rule is created when you add either a VPC ID or a VPC endpoint ID to the
restrictions table.
You
can add up to IP or VPC endpoint rules to the restrictions table.
You can only add rules from the AWS Region where your account is. All traffic that
is not allowed by either the IP rule or the VPC endpoint rule is blocked when the
restriction is turned on.

A _CIDR address_ is composed of two parts: the
prefix and the suffix. The prefix is the CIDR's network address and is written like
a normal IP address. The suffix shows how many bits are in the address. An example
of a complete CIDR address is `10.24.34.0/23`.

IP and VPC endpoint rules apply only to Quick Suite web, embedded, and
mobile access and don't restrict access to the public API. Your users can still call
all API operations from restricted IP ranges. For information on restricting calls
to the public API from specific IP addresses, see [AWS: Denies access to AWS based on the source
IP](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md") in the _IAM User Guide_.

Before you save any rule changes or turn on other rules, make sure that you have a
rule that includes your IP address or VPC endpoint ID. If there isn’t a rule that
includes allows your traffic, you can't save your changes.

###### To add an IP or VPC endpoint rule

1. On the Quick Suite start page, choose **Manage
   QuickSight**, and then choose **Security and
   Permissions**.
2. Choose **IP and VPC endpoint restrictions**.
3. Perform one of the following actions.
   1. For **IP restriction**, enter the CIDR address
      that defines the IP range that you want to create a rule for.
   2. For **VPC endpoint restriction**, enter either
      the VPC ID or the VPC endpoint ID of the endpoint that you want to
      create a rule for.

4. (Optional) For **Description**, enter a description for
   the rule. Doing this can help you differentiate your rules.
5. Choose **Add**.
6. Choose **Save changes** in the box that appears to apply
   the rule.

It can take up to 10 minutes for a rule to be fully implemented.

### Update an existing rule

After you create an IP pr VPC endpoint rule, use the IP and VPC restrictions table
to make changes to the rule. Use the procedure bwloe to update an existing IP or VPC
endpoint rule in the IP and VPC restrictions table.

###### To update an existing IP or VPC endpoint rule

1. On the Quick Suite start page, choose **Manage
   QuickSight**, and then choose **Security and
   Permissions**.
2. Choose **IP and VPC endpoint restrictions**.
3. Choose the edit icon to the right of the rule that you want to
   change.
4. Make your changes and choose **Update**.
5. Choose **Save changes** in the box that appears to update
   the rule.

It can take up to 10 minutes for an updated rule to be fully implemented.

### Delete a rule

Use the procedure below to delete an IP or VPC endpoint rule from the IP and VPC
endpoint restrictions table.

###### To delete an IP rule

1. On the Quick Suite start page, choose **Manage
   QuickSight**, and then choose **Security and
   Permissions**.
2. Choose **IP and VPC endpoint restrictions**.
3. Make your changes and choose **Update**. A rule marked
   for deletion appears with a strike through it.
4. Choose **Save changes** in the box that appears to delete
   the rule.

It can take up to 10 minutes for an updated rule to be deleted.

### Turning on your IP and VPC endpoint

rules

You can turn on or turn off your account's IP and VPC endpoint restrictions by
using the **Rules** option at the top of the IP and VPC
restrictions page. When rules are turned on, users from sources that are not on the
restrictions table can't access Quick Suite mobile, embedded, and website
pages. IP and VPC endpoint rules are global and apply to all AWS Regions.

If a user is accessing the Quick Suite account from a source that is not on
the rule list when you turn on restrictions, they lose access to the account.

Account holders can audit users who make changes to the IP and VPC endpoint
restrictions table by using AWS CloudTrail. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").
