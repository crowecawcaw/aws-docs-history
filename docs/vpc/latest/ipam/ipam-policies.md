

# Understanding IPAM policies
<a name="ipam-policies"></a>

An Amazon VPC IP Address Manager (IPAM) policy is a set of rules that IPAM applies to AWS resources when they are created in the accounts that the policy targets. You define the rules once, enable the policy for your organization, for organizational units, or for individual accounts, and IPAM applies the rules without any action in the member accounts.

This section describes the concepts and procedures that are common to all IPAM policies: prerequisites, how IPAM decides which policy applies to an account, and how to create and enable a policy. The kinds of rules that you can define in a policy are described in the following topics.

**Topics**
+ [Terminology](#ipam-policies-terminology)
+ [Where a policy applies](#ipam-policies-scope)
+ [Which policy applies to an account](#ipam-policies-precedence)
+ [Managing IPAM policies](managing-ipam-policies.md)
+ [Defining a public IPv4 allocation strategy with IPAM policies](define-public-ipv4-allocation-strategy-with-ipam-policies.md)

## Terminology
<a name="ipam-policies-terminology"></a>

The following terms apply to IPAM policies:

**Allocation rules**  
Optional configurations within an IPAM policy that map AWS resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.

**IPAM policy**  
A set of rules that IPAM applies to resources created in the accounts that the policy targets. A policy can contain rules of more than one kind, and a policy's targets apply to all of its rules. Only one policy can be enabled for a given target, so rules of different kinds that should apply to the same target must be in the same policy. Use separate policies only when the rules should apply to different targets.

**Rule**  
An entry in a policy that maps matching resources to an outcome, such as the IPAM pool that a resource gets its IP address from. Each kind of rule has its own matching model, described in the topic for that rule kind.

**Target**  
An AWS account, [organizational unit](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organization-structure) (OU), or [organization root](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organization-structure) to which a policy is applied. The targets that take effect depend on the IPAM owner and tier. For more information, see [Where a policy applies](#ipam-policies-scope).

## Where a policy applies
<a name="ipam-policies-scope"></a>

A policy applies only in the IPAM's operating AWS Regions. For more information, see [Modify IPAM operating Regions](mod-ipam-region.md). The accounts that a policy applies to depend on which account owns the IPAM and on the IPAM's [tier](https://docs.aws.amazon.com/vpc/latest/ipam/mod-ipam-tier.html).

The following table shows which accounts a policy applies to, based on the IPAM owner and tier.


| IPAM owner | Tier | Accounts the policy applies to | 
| --- | --- | --- | 
| Delegated administrator account | Advanced Tier | The targets that you choose. Target the organization root to apply the policy to every account in the organization, or target an organizational unit (OU) or individual member accounts to apply it to some accounts. | 
| Delegated administrator account | Free Tier | Only the delegated administrator account. If you target the organization root, an OU, or member accounts, the policy rules still apply only to the delegated administrator account. | 
| Any other account | Free Tier or Advanced Tier | Only the account that owns the IPAM. | 

To apply a policy to accounts across your organization, the IPAM must be in the delegated administrator account and use the Advanced Tier.

**Note**  
A policy applies only to accounts in the delegated administrator's own organization. If your IPAM manages accounts in other organizations through shared resource discoveries, the policy does not apply to those accounts. For more information, see [Integrate IPAM with accounts outside of your organization](enable-integ-ipam-outside-org.md).  
Organizational unit (OU) exclusions also apply to IPAM policies. A policy doesn't apply to accounts that an OU exclusion covers, even if the policy specifies those accounts as targets. Before you choose policy targets, review your OU exclusions. For more information, see [Exclude organizational units from IPAM](exclude-ous.md).

## Which policy applies to an account
<a name="ipam-policies-precedence"></a>

An account can be in the scope of more than one enabled policy. The delegated administrator can target the organization root, an OU, or a member account directly, and an account that has its own IPAM can enable a policy for itself. When more than one policy applies to an account, IPAM uses the policy with the highest precedence, in this order:

1. **Member account target** – A policy that the delegated administrator enabled for the account directly.

1. **OU target** – A policy that the delegated administrator enabled for an OU that contains the account. If more than one OU in the account's path has a policy, the policy on the OU nearest to the account applies.

1. **Organization root target** – A policy that the delegated administrator enabled for the whole organization.

1. **Self-activation** – A policy that the account enabled for itself from its own IPAM.

Only the rules from that one policy are evaluated. Rules from lower-precedence policies are not merged in, even if they are of a kind that the higher-precedence policy does not contain.

For example, suppose that you enable a policy with two kinds of rules for the organization root, and a second policy with only one kind of rule for an OU. Accounts in that OU use only the OU policy, so the other kind of rule from the organization-wide policy does not apply to them. To apply both kinds of rules to the OU, include both kinds in the OU policy.

**Note**  
A policy that a member account enables for itself never overrides a policy that the delegated administrator has applied to it, whether directly, through an OU, or at the organization root. The account's own policy applies only when no delegated administrator policy covers the account.