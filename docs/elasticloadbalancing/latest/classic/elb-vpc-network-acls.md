# Configure network ACLs for your Classic Load Balancer

The default network access control list (ACL) for a VPC allows all inbound and outbound traffic.
If you create custom network ACLs, you must add rules that allow the load balancer
and instances to communicate.

The recommended rules for the subnet for your load balancer depend on the type of load
balancer, internet-facing or internal.

###### Internet-facing load balancer

The following are the recommended inbound rules for an internet-facing load balancer.

| Source     | Protocol | Port Range | Comment                                                        |
| ---------- | -------- | ---------- | -------------------------------------------------------------- |
| 0.0.0.0/0  | TCP      | `listener` | Allow all inbound traffic on the load balancer listener port   |
| `VPC CIDR` | TCP      | 1024-65535 | Allow inbound traffic from the VPC CIDR on the ephemeral ports |

The following are the recommended outbound rules for an internet-facing load balancer.

| Destination | Protocol | Port Range          | Comment                                                  |
| ----------- | -------- | ------------------- | -------------------------------------------------------- |
| `VPC CIDR`  | TCP      | `instance listener` | Allow all outbound traffic on the instance listener port |
| `VPC CIDR`  | TCP      | `health check`      | Allow all outbound traffic on the health check port      |
| 0.0.0.0/0   | TCP      | 1024-65535          | Allow all outbound traffic on the ephemeral ports        |

###### Internal load balancer

The following are the recommended inbound rules for an internal load balancer.

| Source     | Protocol | Port Range | Comment                                                                    |
| ---------- | -------- | ---------- | -------------------------------------------------------------------------- |
| `VPC CIDR` | TCP      | `listener` | Allow inbound traffic from the VPC CIDR on the load balancer listener port |
| `VPC CIDR` | TCP      | 1024-65535 | Allow inbound traffic from the VPC CIDR on the ephemeral ports             |

The following are the recommended outbound rules for an internal load balancer.

| Destination | Protocol | Port Range          | Comment                                                                 |
| ----------- | -------- | ------------------- | ----------------------------------------------------------------------- |
| `VPC CIDR`  | TCP      | `instance listener` | Allow outbound traffic to the VPC CIDR on the instance listener<br>port |
| `VPC CIDR`  | TCP      | `health check`      | Allow outbound traffic to the VPC CIDR on the health check port         |
| `VPC CIDR`  | TCP      | 1024-65535          | Allow outbound traffic to the VPC CIDR on the ephemeral ports           |
