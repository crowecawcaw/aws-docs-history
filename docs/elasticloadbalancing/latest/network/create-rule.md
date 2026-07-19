# Listener rules for your Network Load Balancer

You can create listener rules to route traffic to different target groups
based on the source IP address type of incoming traffic. This is useful for
dual-stack Network Load Balancers that need to route IPv4 and IPv6 traffic to separate target
groups. You can modify, reorder, describe, and delete listener rules at any time.
Changes to listener rules take effect immediately.

## Prerequisites

- You must have a dual-stack Network Load Balancer with an existing listener.
- You must have one or more target groups to route traffic to. For more
  information, see [Create a target group for your Network Load Balancer](create-target-group.md "create-target-group.md").

###### Contents

- [Add a rule](add-rule.md "add-rule.md")
- [Edit a rule](modify-rule.md "modify-rule.md")
- [Delete a rule](delete-rule.md "delete-rule.md")
