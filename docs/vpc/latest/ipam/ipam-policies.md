

# IPAM policies
<a name="ipam-policies"></a>

An IPAM policy is a set of rules that IPAM applies to AWS resources when they are created in the accounts that the policy targets. You define the rules once, enable the policy for your organization, for organizational units, or for individual accounts, and IPAM applies the rules without any action in the member accounts.

This topic describes the concepts and procedures that are common to all IPAM policies: prerequisites, how IPAM decides which policy applies to an account, and how to create and enable a policy. The kinds of rules that you can define in a policy are described in the following topics.

**Topics**
+ [Prerequisites](#ipam-policies-prerequisites)
+ [Terminology](#ipam-policies-terminology)
+ [Which policy applies to an account](#ipam-policies-precedence)
+ [Create an IPAM policy](#ipam-policies-create)
+ [Enable an IPAM policy](#ipam-policies-enable)
+ [Define public IPv4 allocation strategy with IPAM policies](define-public-ipv4-allocation-strategy-with-ipam-policies.md)

## Prerequisites
<a name="ipam-policies-prerequisites"></a>
+ An [IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) with [advanced tier](https://docs.aws.amazon.com/vpc/latest/ipam/mod-ipam-tier.html) enabled. To apply policies to accounts across your organization, the IPAM must be in the [delegated administrator account](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam.html). An IPAM in an account that is not the delegated administrator can apply policies to that account only.
+ [IAM permissions](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam.html) for the IPAM policy operations and for the EC2 operations that create the governed resources.

## Terminology
<a name="ipam-policies-terminology"></a>

**IPAM policy**  
A set of rules that IPAM applies to resources created in the accounts that the policy targets. A policy can contain rules of more than one kind, and a policy's targets apply to all of its rules. Only one policy can be enabled for a given target, so rules of different kinds that should apply to the same target must be in the same policy. Use separate policies only when the rules should apply to different targets.

**Rule**  
An entry in a policy that maps matching resources to an outcome, such as the IPAM pool that a resource gets its IP address from. Each kind of rule has its own matching model, described in the topic for that rule kind.

**Target**  
An AWS account, an organizational unit (OU), or the root of an AWS Organization to which a policy is applied.

## Which policy applies to an account
<a name="ipam-policies-precedence"></a>

An account can be in the scope of more than one enabled policy. The delegated administrator can target the organization root, an OU, or a member account directly, and an account that has its own IPAM can enable a policy for itself. When more than one policy applies to an account, IPAM uses the policy with the highest precedence, in this order:

1. **Member account target**: A policy that the delegated administrator enabled for the account directly.

1. **OU target**: A policy that the delegated administrator enabled for an OU that contains the account. If more than one OU in the account's path has a policy, the policy on the OU nearest to the account applies.

1. **Organization root target**: A policy that the delegated administrator enabled for the whole organization.

1. **Self-activation**: A policy that the account enabled for itself from its own IPAM.

Only the rules from that one policy are evaluated. Rules from lower-precedence policies are not merged in, even if they are of a kind that the higher-precedence policy does not contain.

For example, suppose that you enable a policy with two kinds of rules for the organization root, and a second policy with only one kind of rule for an OU. Accounts in that OU use only the OU policy, so the other kind of rule from the organization-wide policy does not apply to them. To apply both kinds of rules to the OU, include both kinds in the OU policy.

**Important**  
A policy that a member account enables for itself never overrides a policy that the delegated administrator has applied to it, whether directly, through an OU, or at the organization root. The account's own policy applies only when no delegated administrator policy covers the account.

## Create an IPAM policy
<a name="ipam-policies-create"></a>

**Using the AWS Console:**  
Follow these steps to create an IPAM policy by using the AWS Console:

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the left navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. Enter a **Name** for your policy (optional).

1. Select the **IPAM** to associate with this policy.

1. (Optional) Add tags.

1. Choose **Create policy**.

**Using the AWS CLI:**  
Use the [create-ipam-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-ipam-policy.html) command.

After you create the policy, add rules to it. See the topic for the kind of rule that you want to add.

## Enable an IPAM policy
<a name="ipam-policies-enable"></a>

Specify which accounts should use the policy. A policy's targets apply to all of the rules in the policy, and only one policy can be enabled for a given target.

**Using the AWS Console:**  
Follow these steps to enable the policy by using the AWS Console:

1. In your policy details page, choose the **Targets** tab.

1. Choose **Manage policy targets**.

1. Do one of the following:
   + For single account usage (IPAM not integrated with AWS Organizations, or an account applying a policy to itself), choose **Enable for your account**.
   + For IPAM integrated with AWS Organizations (when you're the delegated admin):
     + In the **Organizational structure** section, select the accounts or organizational units where you want to apply this policy.
     + Check the **Enabled** checkbox for each target.
     + Choose **Save Changes**.

**Using the AWS CLI:**  
Use the [enable-ipam-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-ipam-policy.html) command based on your setup:

For single account usage (IPAM not integrated with AWS Organizations, or an account applying a policy to itself):

```
aws ec2 enable-ipam-policy \
    --ipam-policy-id ipam-policy-12345678
```

For IPAM integrated with AWS Organizations (when you're the delegated admin), set a policy to target an account in the AWS Organization:

```
aws ec2 enable-ipam-policy \
    --ipam-policy-id ipam-policy-12345678 \
    --organization-target-id 123456789012
```

For IPAM integrated with AWS Organizations (when you're the delegated admin), set a policy to target an organizational unit:

```
aws ec2 enable-ipam-policy \
    --ipam-policy-id ipam-policy-12345678 \
    --organization-target-id ou-123
```

**Important**  
Enabling a policy for a target replaces any policy that is already enabled for that same target. Policies enabled for different targets coexist; see [Which policy applies to an account](#ipam-policies-precedence).