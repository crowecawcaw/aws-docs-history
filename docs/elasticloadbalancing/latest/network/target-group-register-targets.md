# Register targets for your Network Load Balancer

When your target is ready to handle requests, you register it with one or more target
groups. The target type of the target group determines how you register targets. For
example, you can register instance IDs, IP addresses, or an Application Load Balancer. Your Network Load Balancer starts
routing requests to targets as soon as the registration process completes and the
targets pass the initial health checks. It can take a few minutes for the registration
process to complete and health checks to start. For more information, see [Health checks for Network Load Balancer target groups](target-group-health-checks.md "target-group-health-checks.md").

If demand on your currently registered targets increases, you can register additional
targets in order to handle the demand. If demand on your registered targets decreases,
you can deregister targets from your target group. It can take a few minutes for the
deregistration process to complete and for the load balancer to stop routing requests to
the target. If demand increases subsequently, you can register targets that you
deregistered with the target group again. If you need to service a target, you can
deregister it and then register it again when servicing is complete.

When you deregister a target, ELB waits until in-flight requests have completed.
This is known as _connection draining_. The status of a target is
`draining` while connection draining is in progress. After deregistration
is complete, status of the target changes to `unused`. For more information,
see [Deregistration delay](edit-target-group-attributes.md#deregistration-delay "edit-target-group-attributes.md#deregistration-delay").

If you are registering targets by instance ID, you can use your load balancer with an
Amazon EC2 Auto Scaling group. After you attach a target group to an Amazon EC2 Auto Scaling group and the group scales out,
the instances launched by the Amazon EC2 Auto Scaling group are automatically registered with the target
group. If you detach the load balancer from the Amazon EC2 Auto Scaling group, the instances are
automatically deregistered from the target group. For more information, see [Attaching a load balancer to your
Amazon EC2 Auto Scaling group](../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md "../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md") in the _Amazon EC2 Auto Scaling User Guide_.

###### Contents

- [Target security groups](#target-security-groups "#target-security-groups")
- [Network ACLs](#network-acls "#network-acls")
- [Shared subnets](#register-targets-shared-subnets "#register-targets-shared-subnets")
- [Register targets](#register-targets "#register-targets")
- [Deregister targets](#deregister-targets "#deregister-targets")

## Target security groups

Before adding targets to your target group, configure the security groups
associated with the targets to accept traffic from your Network Load Balancer.

###### Recommendations for target security groups if the load balancer has an

associated security group

- To allow client traffic: Add a rule that
  references the security group associated with the load balancer.
- To allow PrivateLink traffic: If you
  configured the load balancer to evaluate inbound rules for traffic sent
  through AWS PrivateLink, add a rule that accepts traffic from the load
  balancer security group on the traffic port. Otherwise, add a rule that
  accepts traffic from the load balancer private IP addresses on the traffic
  port.
- To accept load balancer health checks: Add
  a rule that accepts health check traffic from the load balancer security
  groups on the health check port.

###### Recommendations for target security groups if the load balancer is not

associated with a security group

- To allow client traffic: If your load
  balancer preserves client IP addresses, add a rule that accepts traffic from
  the IP addresses of approved clients on the traffic port. Otherwise, add a
  rule that accepts traffic from the load balancer private IP addresses on the
  traffic port.
- To allow PrivateLink traffic: Add a rule
  that accepts traffic from the load balancer private IP addresses on the
  traffic port.
- To accept load balancer health checks: Add
  a rule that accepts health check traffic from the load balancer private IP
  addresses on the health check port.

###### How client IP preservation works

Network Load Balancers don't preserve client IP addresses unless you set the
`preserve_client_ip.enabled` attribute to
`true`. Also, with dualstack Network Load Balancers, client IP address
preservation does not work when translating IPv4 addresses to
IPv6, or IPv6 to IPv4 addresses. Client IP address preservation
only works when client and target IP addresses are both IPv4 or
both IPv6.

###### To find the load balancer private IP addresses using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network
   Interfaces**.
3. In the search field, enter the name of your Network Load Balancer. There is one network
   interface per load balancer subnet.
4. On the **Details** tab for each network interface, copy
   the address from **Private IPv4 address**.

For more information, see [Update the security groups for your Network Load Balancer](load-balancer-security-groups.md "load-balancer-security-groups.md").

## Network ACLs

When you register EC2 instances as targets, you must ensure that the network ACLs
for the subnets for your instances allow traffic on both the listener port and the
health check port. The default network access control list (ACL) for a VPC allows
all inbound and outbound traffic. If you create custom network ACLs, verify that
they allow the appropriate traffic.

The network ACLs associated with the subnets for your instances must allow the
following traffic for an internet-facing load balancer.

Recommended rules for instance subnets| **Inbound** |
| **Source** | **Protocol** | **Port Range** | **Comment** |
| `Client IP addresses` | `listener` | `target port` | Allow client traffic (IP Preservation: `ON`) |
| `VPC CIDR` | `listener` | `target port` | Allow client traffic (IP Preservation: `OFF`) |
| `VPC CIDR` | `health check` | `health check` | Allow health check traffic |
| **Outbound** |
| **Destination** | **Protocol** | **Port Range** | **Comment** |
| `Client IP addresses` | `listener` | 1024-65535 | Allow return traffic to client (IP Preservation: `ON`) |
| `VPC CIDR` | `listener` | 1024-65535 | Allow return traffic to client (IP Preservation: `OFF`) |
| `VPC CIDR` | `health check` | 1024-65535 | Allow health check traffic |

The network ACLs associated with the subnets for your load balancer must allow the
following traffic for an internet-facing load balancer.

Recommended rules for load balancer subnets| **Inbound** |
| **Source** | **Protocol** | **Port Range** | **Comment** |
| `Client IP addresses` | `listener` | `listener` | Allow client traffic |
| `VPC CIDR` | `listener` | 1024-65535 | Allow response from target |
| `VPC CIDR` | `health check` | 1024-65535 | Allow health check traffic |
| **Outbound** |
| **Destination** | **Protocol** | **Port Range** | **Comment** |
| `Client IP addresses` | `listener` | 1024-65535 | Allow responses to clients |
| `VPC CIDR` | `listener` | `target port` | Allow requests to targets |
| `VPC CIDR` | `health check` | `health check` | Allow health check to targets |

For an internal load balancer, the network ACLs for the subnets for your instances
and load balancer nodes must allow both inbound and outbound traffic to and from the
VPC CIDR, on the listener port and ephemeral ports.

## Shared subnets

Participants can create a Network Load Balancer in a shared VPC. Participants can't register
a target that runs in a subnet that is not shared with them.

Shared subnets for Network Load Balancers is supported in all AWS Regions, excluding:

- Asia Pacific (Osaka) `ap-northeast-3`
- Asia Pacific (Hong Kong) `ap-east-1`
- Middle East (Bahrain) `me-south-1`
- AWS China (Beijing) `cn-north-1`
- AWS China (Ningxia) `cn-northwest-1`

## Register targets

Each target group must have at least one registered target in each Availability
Zone that is enabled for the load balancer.

The target type of your target group determines which targets you can register.
For more information, see [Target type](load-balancer-target-groups.md#target-type "load-balancer-target-groups.md#target-type").
Use the information below to register targets with a target group of type
`instance` or `ip`. If the target type is `alb`,
see [Use Application Load Balancers as targets](application-load-balancer-target.md "application-load-balancer-target.md").

###### Requirements and considerations

- An instance must be in the `running` state when you register
  it.
- You can't register instances by instance ID if they use one of the
  following instance types: C1, CC1, CC2, CG1, CG2, CR1, G1, G2, HI1, HS1, M1,
  M2, M3, or T1.
- When registering targets by instance ID, instances must be in the same VPC
  as the Network Load Balancer. You can't register instances by instance ID if they are in an VPC
  that is peered to the load balancer VPC (same Region or different Region). You
  can register these instances by IP address.
- When registering targets by instance ID for a IPv6 target group, the targets
  must have an assigned primary IPv6 address. To learn more, see [IPv6 addresses](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#ipv6-addressing "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#ipv6-addressing") in the _Amazon EC2 User Guide_
- When registering targets by IP address for an IPv4 target group, the IP
  addresses that you register must be from one of the following CIDR blocks:
  - The subnets of the target group VPC
  - 10.0.0.0/8 (RFC 1918)
  - 100.64.0.0/10 (RFC 6598)
  - 172.16.0.0/12 (RFC 1918)
  - 192.168.0.0/16 (RFC 1918)

- When registering targets by IP address for an IPv6 target group, the IP
  addresses that you register must be within the VPC IPv6 CIDR block or
  within the IPv6 CIDR block of a peered VPC.
- If you register a target by IP address and the IP address is in the same
  VPC as the load balancer, the load balancer verifies that it is from a
  subnet that it can reach.
- For UDP, TCP_UDP, QUIC, and TCP_QUIC target groups, do not register instances by IP address
  if they reside outside of the load balancer VPC or if they use one of the
  following instance types: C1, CC1, CC2, CG1, CG2, CR1, G1, G2, HI1, HS1, M1,
  M2, M3, or T1. Targets that reside outside the load balancer VPC or use an
  unsupported instance type might be able to receive traffic from the load
  balancer but then be unable to respond.

###### QUIC specific requirements and considerations

- All targets registered to a QUIC or TCP_QUIC target group must have a server ID specified.
- Server IDs must be unique for all targets that exist within an Network Load Balancer listener.
- QUIC server IDs are always 8 bytes. When registering the target, the server ID must be in the form `0x` followed by 16 hexadecimal
  characters.
- Once a target is registered with a server ID, the ID is immuatable. To change a target server ID, it must be deregistered first
  and then registered with the new server ID.
- A target identifier and port combination must have one server ID. Using a different server ID for the same IP or instance ID and port
  combination within the same VPC is not supported.
- Avoid re-using the same server ID for a different target within 6 hours.

Console

###### To register targets

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. Choose the **Targets** tab.
5. Choose **Register targets**.
6. If the target type of the target group is `instance`,
   select available instances, override the default port if needed,
   and then choose **Include as pending below**.
7. If the target type of the target group is `ip`, for
   each IP address, select the network, enter the IP address and ports,
   and choose **Include as pending below**.
8. If the target type of the target group is `alb`, override
   the default port if needed and select the Application Load Balancer. For more information,
   see [Use Application Load Balancers as targets](application-load-balancer-target.md "application-load-balancer-target.md").
9. If the protocol of the target group is QUIC or TCP_QUIC, ensure a
   server ID is specified.
10. Choose **Register pending targets**.

AWS CLI

###### To register targets

Use the [register-targets](../../../cli/latest/reference/elbv2/register-targets.md "../../../cli/latest/reference/elbv2/register-targets.md") command. The following example
registers targets by instance ID. Because the port is not
specified, the load balancer uses the target group port.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`i-1234567890abcdef0` Id=`i-0abcdef1234567890`
```

The following example registers targets by IP address. Because
the port is not specified, the load balancer uses the target
group port.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`10.0.50.10` Id=`10.0.50.20`
```

The following example registers an Application Load Balancer as a target.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`application-load-balancer-arn`
```

The following example registers targets into a QUIC or TCP_QUIC target group.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`10.0.50.10`,QuicServerId=`0xa1b2c3d4e5f65890` Id=`10.0.50.20`,QuicServerId=`0xa1b2c3d4e5f65999`
```

CloudFormation

###### To register targets

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the new targets. The following example registers
two targets by instance ID.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: instance
      VpcId: !Ref myVPC
      Targets:
        - Id: !GetAtt Instance1.InstanceId
          Port: 80
        - Id: !GetAtt Instance2.InstanceId
          Port: 80
```

The following example registers two targets by instance ID into a QUIC or TCP_QUIC protocol target group.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: instance
      VpcId: !Ref myVPC
      Targets:
        - Id: !GetAtt Instance1.InstanceId
          Port: 80
          QuicServerId: 0xa1b2c3d4e5f65999
        - Id: !GetAtt Instance2.InstanceId
          Port: 80
          QuicServerId: 0xa1b2c3d4e5f65000

```

## Deregister targets

If demand on your application decreases, or if you need to service your targets, you
can deregister targets from your target groups. Deregistering a target removes it from
your target group, but does not affect the target otherwise. The load balancer stops
routing traffic to a target as soon as it is deregistered. The target enters the
`draining` state until in-flight requests have completed.

Console

###### To deregister targets

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Targets** tab, select
   the targets to remove.
5. Choose **Deregister**.

AWS CLI

###### To deregister targets

Use the [deregister-targets](../../../cli/latest/reference/elbv2/deregister-targets.md "../../../cli/latest/reference/elbv2/deregister-targets.md") command. The following example
deregisters two targets that were registered by instance ID.

```
aws elbv2 deregister-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`i-1234567890abcdef0` Id=`i-0abcdef1234567890`
```
