**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How Firewall Manager creates firewall endpoints

This section explains how Firewall Manager creates firewall endpoints.

The _Firewall management type_ in your policy determines how Firewall Manager
creates firewalls. Your policy can create _distributed_ firewalls, a _centralized_ firewall, or you can **import existing firewalls**:

- **Distributed** - With the distributed
  deployment model, Firewall Manager creates endpoints for each VPC that's within policy
  scope. You can either customize the endpoint location by specifying which
  Availability Zones to create firewall endpoints in, or Firewall Manager can automatically
  create endpoints in the Availability Zones with public subnets. If you manually
  choose the Availability Zones, you have the option to restrict the set of
  allowed CIDRs per Availability Zone. If you decide to let Firewall Manager automatically
  create the endpoints, you must also specify whether the service will create a
  single endpoint or multiple firewall endpoints within your VPCs.
  - For multiple firewall endpoints, Firewall Manager deploys a firewall endpoint in
    each Availability Zone where you have a subnet with an internet gateway
    or a Firewall Manager-created firewall endpoint route in the route table. This is
    the default option for a Network Firewall policy.
  - For a single firewall endpoint, Firewall Manager deploys a firewall endpoint in a single
    Availability Zone in any subnet that has an internet gateway route. With
    this option, traffic in other zones needs to cross zone boundaries in
    order to be filtered by the firewall.

  ###### Note

  For both of these options, there must be a subnet associated to a route table that has an
  IPv4/prefixlist route in it. Firewall Manager does not check for any other resources.

- **Centralized** - With the centralized
  deployment model, Firewall Manager creates one or more firewall endpoints within an
  _inspection VPC_. An inspection VPC is a
  central VPC where Firewall Manager launches your endpoints. When you use the centralized deployment model, you also specify which Availability Zones to create firewall endpoints in. You can't change the inspection VPC after you create your policy. To use a different inspection VPC, you must create a new policy.
- **Import existing firewalls** - When you import existing firewalls, you choose the firewalls to manage in your policy by adding one or more _resource sets_ to your policy. A resource set is a collection of resources, in this case existing firewalls in Network Firewall, that are managed by an account in your organization. Before you use resource sets in your policy, you must first create a resource set. For information about Firewall Manager resource sets, see [Grouping your resources in Firewall Manager](fms-resource-sets.md "fms-resource-sets.md").

Keep in mind the following considerations when working with imported firewalls:

    + If an imported firewall become non-compliant, Firewall Manager will try to automatically resolve the violation, except for under the following circumstances:




    	- If there's a mismatch between the Firewall Manager and Network Firewall policy's stateful or stateless default actions.
    	- If a rule group in an imported firewall's firewall policy has the same priority as a rule group in the Firewall Manager policy.
    	- If an imported firewall uses a firewall policy that's associated with a firewall that's not part of the policy's resource set. This can happen because a firewall can have exactly one firewall policy, but a single firewall policy can be associated with multiple firewalls.
    	- If a pre-existing rule group belonging to an imported firewall's firewall policy that is also specified in the Firewall Manager policy is given a different priority.
    + If you enable resource cleanup in the policy, Firewall Manager removes the rule groups which have been in FMS import policy from the firewalls in scope of the resource set.
    + Firewalls managed by that are managed by a Firewall Manager import existing firewall management type can only be managed by one policy at a time. If the same resource set is added to multiple import network firewall policies, the firewalls in the resource set will be managed by the first policy the resource set was added to and will be ignored by the second policy.
    + Firewall Manager doesn't currently stream exception policy configurations. For information about stream exception policies, see [Stream exception policy](../../../network-firewall/latest/developerguide/firewall-policy-settings.md#:~:text=Stream%20exception%20policy "../../../network-firewall/latest/developerguide/firewall-policy-settings.md#:~:text=Stream%20exception%20policy") in
     the *AWS Network Firewall Developer Guide*.

If you change the list of Availability Zones for policies using distributed or centralized firewall management, Firewall Manager will try to clean up any endpoints that were created in the past, but that aren't currently in policy scope. Firewall Manager will remove the endpoint only if there are no route table routes that reference the out of scope endpoint. If Firewall Manager finds that it is unable to delete these endpoints, it will mark the firewall subnet as being non-compliant and will continue attempting to remove the endpoint until such time as it is safe to delete.
