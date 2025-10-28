# Edit attributes for your Network Load Balancer

After you create a Network Load Balancer, you can edit its attributes.

###### Load balancer attributes

- [Deletion protection](#deletion-protection "#deletion-protection")
- [Cross-zone load balancing](#load-balancer-cross-zone "#load-balancer-cross-zone")
- [Availability Zone DNS affinity](#zonal-dns-affinity "#zonal-dns-affinity")
- [Secondary IP addresses](#secondary-ip-addresses "#secondary-ip-addresses")

## Deletion protection

To prevent your Network Load Balancer from being deleted accidentally, you can enable deletion
protection. By default, deletion protection is disabled for your Network Load Balancer.

If you enable deletion protection for your Network Load Balancer, you must disable it before
you can delete the Network Load Balancer.

Console

###### To enable or disable deletion protection

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the name of the Network Load Balancer to open its details page.
4. On the **Attributes** tab, choose **Edit**.
5. Under **Protection**, enable or disable
   **Deletion protection**.
6. Choose **Save changes**.

AWS CLI

###### To enable or disable deletion protection

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`deletion_protection.enabled` attribute.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=deletion_protection.enabled,Value=`true`"
```

CloudFormation

###### To enable or disable deletion protection

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `deletion_protection.enabled` attribute.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "deletion_protection.enabled"
          Value: "`true`"
```

## Cross-zone load balancing

With Network Load Balancers, cross-zone load balancing is off by default at the load balancer level, but
you can turn it on at any time. For target groups, the default is to use the load
balancer setting, but you can override the default by explicitly turning cross-zone load
balancing on or off at the target group level. For more information, see
[Cross-zone load balancing for target groups](edit-target-group-attributes.md#target-group-cross-zone "edit-target-group-attributes.md#target-group-cross-zone").

Console

###### To enable or disable cross-zone load balancing for a load balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the name of the load balancer to open its details page.
4. On the **Attributes** tab, choose **Edit**.
5. On the **Edit load balancer attributes** page, turn
   **Cross-zone load balancing** on or off.
6. Choose **Save changes**.

AWS CLI

###### To enable or disable cross-zone load balancing for a load balancer

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`load_balancing.cross_zone.enabled` attribute.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=load_balancing.cross_zone.enabled,Value=`true`"
```

CloudFormation

###### To enable or disable cross-zone load balancing for a load balancer

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `load_balancing.cross_zone.enabled` attribute.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "load_balancing.cross_zone.enabled"
          Value: "`true`"
```

## Availability Zone DNS affinity

When using the default client routing policy, requests sent to your Network Load Balancers DNS name will receive any
healthy Network Load Balancer IP addresses. This leads to the distribution of client
connections across the Network Load Balancer's Availability Zones. With the Availability Zone
affinity routing policies, client DNS queries favor Network Load Balancer IP addresses in their own Availability
Zone. This helps improve both latency and resiliency, as clients do not need to cross
Availability Zone boundaries when connecting to targets.

Availability Zone affinity routing policies only apply to clients resolving the Network Load Balancers
DNS name using Route 53 Resolver. For more information, see
[What is Amazon Route 53 Resolver?](../../../Route53/latest/DeveloperGuide/resolver.md "../../../Route53/latest/DeveloperGuide/resolver.md") in the _Amazon Route 53 Developer Guide_

###### Client routing policies available to Network Load Balancers using Route 53 resolver:

- **Availability Zone affinity** – _100
  percent zonal affinity_

Client DNS queries will favor Network Load Balancer IP address in their own Availability
Zone. Queries may resolve to other zones if there are no healthy Network Load Balancer IP
addresses in their own zone.

- **Partial Availability Zone affinity** –
  _85 percent zonal affinity_

85 percent of client DNS queries will favor Network Load Balancer IP addresses in their own
Availability Zone, while the remaining queries resolve to any healthy zone. Queries
may resolve to other healthy zones if there are no healthy IP addresses in their
zone. When there are no healthy IP addresses in any zone, queries resolve to any
zone.

- **Any Availability Zone** (default) –
  _0 percent zonal affinity_

Client DNS queries are resolved among healthy Network Load Balancer IP addresses across
all Network Load Balancer Availability Zones.

Availability Zone affinity helps route requests from the client to the Network Load Balancer, while
cross-zone load balancing is used to help route requests from the Network Load Balancer to the targets.
When using Availability Zone affinity, cross-zone load balancing should be turned off, this
ensures the Network Load Balancer traffic from clients to targets remains within the same Availability
Zone. With this configuration, client traffic is sent to the same Network Load Balancer Availability
Zone, so it's recommended to configure your application to scale independently in each Availability
Zone. This is an important consideration when the number of clients per Availability zone, or the
traffic per Availability Zone are not the same. For more information, see
[Cross-zone load balancing for target groups](edit-target-group-attributes.md#target-group-cross-zone "edit-target-group-attributes.md#target-group-cross-zone").

When an Availability Zone is considered unhealthy, or when a zonal shift is
started, the zonal IP address will be considered unhealthy and not returned to
clients unless fail open is in effect. Availability Zone affinity is maintained when the
DNS record fails open. This helps keep Availability Zones independent and prevent
potential cross zone failures.

When using Availability Zone affinity, times of imbalance between Availability
Zones are expected. It's recommended ensuring your targets are scaling
at the zonal level, to support each Availability Zones workload. In cases
where these imbalances are significant, it's recommended turning off Availability Zone affinity. This allows even distribution of client connections between
all the Network Load Balancer's Availability Zones within 60 seconds, or the DNS TTL.

###### Before using Availability Zone affinity, consider the following:

- Availability Zone affinity causes changes on all of the Network Load Balancers clients who are using
  Route 53 Resolver.
  - Clients aren't able to decide between zonal-local and multi-zone DNS resolutions.
    Availability Zone affinity decides for them.
  - Clients aren't provided with a reliable method to determine when
    they're being impacted by Availability Zone affinity, or how to know which IP
    address is in which Availability Zone.

- When using Availability Zone affinity with Network Load Balancers and Route 53 Resolver,
  we recommend clients use the Route 53 Resolver inbound endpoint in their own
  Availability Zone.
- Clients will remain assigned to their zone-local IP address until it is
  deemed fully unhealthy according to DNS health checks, and is removed
  from DNS.
- Using Availability Zone affinity with cross-zone load balancing on can
  lead to unbalanced distribution of client connections between
  Availability Zones. It's recommended to configure your application
  stack to scale independently in each Availability Zone, ensuring it
  can support zonal clients traffic.
- If cross-zone load balancing is on, the Network Load Balancer is subject to cross zone
  impact.
- The load on each of the Network Load Balancers Availability Zones will be proportional to
  the zonal locations of clients requests. If you don't configure how many
  clients are running in which Availability Zone, you will have to independently scale
  each Availability Zone reactively.

### Monitoring

It is recommended to track the distribution of connections between
Availability Zones, using the zonal Network Load Balancer metrics. You can use
metrics to view the number of new and active connections per zone.

We recommend tracking the following:

- `ActiveFlowCount` – The
  total number of concurrent flows (or connections) from clients
  to targets.
- `NewFlowCount` – The
  total number of new flows (or connections) established from
  clients to targets in the time period.
- `HealthyHostCount` – The
  number of targets that are considered healthy.
- `UnHealthyHostCount` – The
  number of targets that are considered unhealthy.

For more information, see [CloudWatch metrics for your Network Load Balancer](load-balancer-cloudwatch-metrics.md "load-balancer-cloudwatch-metrics.md")

### Enable Availability Zone affinity

Console

###### To enable Availability Zone affinity

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the name of the Network Load Balancer to open its details page.
4. On the **Attributes** tab, choose **Edit**.
5. Under **Availability Zone routing configuration**, **Client routing policy (DNS record)**, select **Availability Zone affinity** or **Partial Availability Zone affinity**.
6. Choose **Save changes**.

AWS CLI

###### To enable Availability Zone affinity

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`dns_record.client_routing_policy` attribute.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=dns_record.client_routing_policy,Value=`partial_availability_zone_affinity`"
```

CloudFormation

###### To enable Availability Zone affinity

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `dns_record.client_routing_policy` attribute.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "dns_record.client_routing_policy"
          Value: "`partial_availability_zone_affinity`"
```

## Secondary IP addresses

If you experience [port
allocation errors](load-balancer-troubleshooting.md#port-allocation-errors-privatelink "load-balancer-troubleshooting.md#port-allocation-errors-privatelink") and you can't add targets to the target group to
resolve them, you can add secondary IP addresses to the load balancer network
interfaces. For each zone where the load balancer is enabled, we select IPv4
addresses from the load balancer subnet and assign them to the corresponding network
interface. These secondary IP addresses are used to establish connections with
targets. They are also used for health check traffic. We recommend that you add one
secondary IP address to start with, monitor the `PortAllocationErrors`
metric, and add another secondary IP address only if the port allocation errors are
not resolved.

###### Warning

After you add secondary IP addresses, you can't remove them. The only way to
release the secondary IP addresses is to delete the load balancer. Before you
add secondary IP addresses, verify that there are enough available IPv4
addresses in the load balancer subnets.

Console

###### To add a secondary IP address

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the name of the Network Load Balancer to open its details page.
4. On the **Attributes** tab, choose **Edit**.
5. Expand **Special case attributes**, unlock the
   **Secondary IP addresses auto assigned per subnet**
   attribute, and choose the number of secondary IP addresses.
6. Choose **Save changes**.

AWS CLI

###### To add a secondary IP address

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`secondary_ips.auto_assigned.per_subnet` attribute.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=secondary_ips.auto_assigned.per_subnet,Value=`1`"
```

You can use the [describe-network-interfaces](../../../cli/latest/reference/elbv2/describe-network-interfaces.md "../../../cli/latest/reference/elbv2/describe-network-interfaces.md") command to get the IPv4
addresses for the load balancer network interfaces. The
`--filters` parameter scopes the results to the network
interfaces for Network Load Balancers and the `--query` parameter further
scopes the results to the load balancer with the specified name and
displays only the specified fields. You can include additional fields
as needed.

```
aws elbv2 describe-network-interfaces \
    --filters "Name=interface-type,Values=network_load_balancer" \
    --query "NetworkInterfaces[?contains(Description,'`my-nlb`')].{ID:NetworkInterfaceId,AZ:AvailabilityZone,Addresses:PrivateIpAddresses[*]}"
```

CloudFormation

###### To add a secondary IP address

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `secondary_ips.auto_assigned.per_subnet`
attribute.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "secondary_ips.auto_assigned.per_subnet"
          Value: "`1`"
```
