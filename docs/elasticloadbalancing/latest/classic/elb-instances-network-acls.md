# Network ACLs for the instances for your Classic Load Balancer

A _network access control list_ (ACL) allows or denies specific inbound or
outbound traffic at the subnet level. You can use the default network ACL for your VPC, or you
can create a custom network ACL for your VPC with rules that are similar to the rules for your
security groups in order to add an additional layer of security to your VPC.

The default network access control list (ACL) for the VPC allows all inbound and outbound traffic.
If you create custom network ACLs, you must add rules that allow the load balancer
and instances to communicate.

The recommended rules for the subnet for your instances depend on whether
the subnet is private or public. The following rules are for a private subnet.
If your instances are in a public subnet, change the source and destination
from the CIDR of the VPC to `0.0.0.0/0`.

The following are the recommended inbound rules.

| Source     | Protocol | Port Range          | Comment                                                                  |
| ---------- | -------- | ------------------- | ------------------------------------------------------------------------ |
| `VPC CIDR` | TCP      | `instance listener` | Allow inbound traffic from the VPC CIDR on the instance listener<br>port |
| `VPC CIDR` | TCP      | `health check`      | Allow inbound traffic from the VPC CIDR on the health check port         |

The following are the recommended outbound rules.

| Destination | Protocol | Port Range | Comment                                                       |
| ----------- | -------- | ---------- | ------------------------------------------------------------- |
| `VPC CIDR`  | TCP      | 1024-65535 | Allow outbound traffic to the VPC CIDR on the ephemeral ports |
