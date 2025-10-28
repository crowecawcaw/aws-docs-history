# Modify IPAM tier

IPAM offers two tiers: Free
Tier and Advanced Tier. Switching to the Advanced Tier of Amazon VPC IP Address Manager provides more granular control over your IP address management. This can be beneficial as your network complexity grows, allowing you to better optimize and manage your IP address space. For more information about the features available in the Free
Tier and the costs associated with the Advanced Tier, see the IPAM tab in the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

###### Note

Before you can switch from the Advanced Tier to the Free Tier, you must:

- Delete private scope pools.
- Delete non-default private scopes.
- Delete pools with locales different than the IPAM home Region.
- Delete non-default resource discovery associations.
- Delete pool allocations to accounts that are not the IPAM owner.

AWS Management Console

###### To modify the IPAM tier

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **IPAMs**.
3. In the content pane, select your IPAM.
4. Choose **Actions** >
   **Edit**.

###### Note

If you are in the Free Tier, you will see **Your estimated IPAM total active IP count
is...**.

The total active IP count is the number of active IP
addresses in your IPAM that you would be charged if you switched from the Free Tier
to the Advanced Tier. An active IP address is defined as an IP address or a prefix associated with an Elastic Network Interface (ENI) that is attached to a resource such as an EC2 Instance.

    * This metric is only available to customers in the Free Tier.
    * If your IPAM is [integrated with AWS Organizations](enable-integ-ipam.md "enable-integ-ipam.md"), the active IP count covers all the Organization accounts.
    * You cannot view a breakdown of the active IP count by IP type (public/private) or class (IPv4/IPv6).
    * IPAM only counts IPs from ENIs owned by monitored accounts. The count may be inaccurate for shared subnets. IP addresses are excluded if the subnet owner or ENI owner is not covered by IPAM.

5. Choose the **IPAM tier** you want to use for the IPAM.
6. Choose **Save changes**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to view and modify an IPAM tier:

1. View current IPAMs: [describe-ipams](../../../cli/latest/reference/ec2/describe-ipams.md "../../../cli/latest/reference/ec2/describe-ipams.md")
2. Modify the IPAM tier: [modify-ipam](../../../cli/latest/reference/ec2/modify-ipam.md "../../../cli/latest/reference/ec2/modify-ipam.md")
3. View your updated IPAMs: [describe-ipams](../../../cli/latest/reference/ec2/describe-ipams.md "../../../cli/latest/reference/ec2/describe-ipams.md")
