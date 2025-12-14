**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How Firewall Manager manages your Network Firewall resources

This section describes how you manage your Network Firewall resources in Firewall Manager.

When you define the policy in Firewall Manager, you provide the network traffic filtering
behavior of a standard AWS Network Firewall firewall policy. You add stateless
and stateful Network Firewall rule groups and specify default actions for packets
that don’t match any stateless rules. For information on working with firewall
policies in AWS Network Firewall, see the [AWS Network Firewall firewall policies](../../../network-firewall/latest/developerguide/firewall-policies.md "../../../network-firewall/latest/developerguide/firewall-policies.md").

For distributed and centralized policies, when you save the Network Firewall policy, Firewall Manager creates a firewall and firewall
policy in each VPC that's within scope of the policy. Firewall Manager names these
Network Firewall resources by concatenating the following values:

- A fixed string, either `FMManagedNetworkFirewall` or
  `FMManagedNetworkFirewallPolicy`, depending on the resource
  type.
- Firewall Manager policy name. This is the name you assign when you create the
  policy.
- Firewall Manager policy ID. This is the AWS resource ID for the Firewall Manager policy.
- Amazon VPC ID. This is the AWS resource ID for the VPC where Firewall Manager creates the
  firewall and firewall policy.
  The following shows an example name for a firewall that's managed by Firewall Manager:

```
FMManagedNetworkFirewallEXAMPLENameEXAMPLEFirewallManagerPolicyIdEXAMPLEVPCId
```

The following shows an example firewall policy name:

```
FMManagedNetworkFirewallPolicyEXAMPLENameEXAMPLEFirewallManagerPolicyIdEXAMPLEVPCId
```

After you create the policy, member accounts in the VPCs can't override your firewall
policy settings or your rule groups, but they can add rule groups to the firewall policy
that Firewall Manager has created.
