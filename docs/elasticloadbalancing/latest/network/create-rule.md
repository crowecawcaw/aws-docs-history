

# Listener rules for your Network Load Balancer
<a name="create-rule"></a>

You can create listener rules to route traffic to different target groups based on the source IP address type of incoming traffic. This is useful for dual-stack Network Load Balancers that need to route IPv4 and IPv6 traffic to separate target groups. You can modify, reorder, describe, and delete listener rules at any time. Changes to listener rules take effect immediately.

## Prerequisites
<a name="create-rule-prereqs"></a>
+ You must have a dual-stack Network Load Balancer with an existing listener.
+ You must have one or more target groups to route traffic to. For more information, see [Create a target group for your Network Load Balancer](create-target-group.md).

**Topics**
+ [Prerequisites](#create-rule-prereqs)
+ [Add a rule](add-rule.md)
+ [Edit a rule](modify-rule.md)
+ [Delete a rule](delete-rule.md)