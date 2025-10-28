This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Calling ingress settings

Wickr supports a calling ingress setting, allowing a client to connect to any calling node
within the cluster and have the call route to the correct calling server. Wickr supports four
calling ingress types:

- LoadBalancer (default)
  - The LoadBalancer will be provisioned by the cloud provider (fully on-premise
    installations will require additional configuration). After the LoadBalancer has been
    provisioned, the KOTS config must be updated again to provide the load balancer's hostname or
    IP addresses.

- NodePort
  - Exposes a NodePort service on each calling node that will serve as the entry point for
    calling traffic. A hostname resolving to one or more nodes or an IP address of one or more
    nodes must be provided. You can choose a port range from 30000-32767 for UDP and optionally
    TCP traffic.

- Existing NLB
  - Attaches the calling ingress service to an existing NLB. You will need to supply the
    target group ARN for UDP and optionally, TCP traffic.

- No Service
  - Select this if you don't need an additional Kubernetes service to allow ingress traffic.
    This will typically be used with the host network setting to route calling ingress traffic
    directly to your calling nodes.

## Considerations

- To ensure backwards compatibility with older clients and federated networks without
  calling ingress, when calling ingress is enabled, the legacy calling mode is still available
  (direct connection to the calling servers). If changing any default ports, ensure that you do
  not have any port collisions on the calling nodes.
- Dual-stack NLBs serving UDP traffic must have IPv6 backend targets. For more information,
  see [Network Load Balancer Target Groups](../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md#target-group-ip-address-type "../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md#target-group-ip-address-type").
- If you require STIG compliance, you must disable the host network option for calling. If
  the nodes are configured in dual-stack mode, but the cluster is not, you may lose IPv6
  connectivity (assuming an IPv4 cluster).
- Calling ingress requires pre-defined host names or IP Addresses. Scaling nodes or
  providing custom routing may require modifying configuration.
- Default calling ingress ports are 8443 for TCP and 16384 for UDP. Make sure firewalls and
  security groups allow traffic for these ports, or alternative ports if the defaults are
  overridden.

## Reference architectures

**Ingress with load balancer**

This option exposes a single load balancer as the entry point for all calling
traffic.

1.  For **Calling Ingress Type**, choose either **Load
    Balancer** or **Existing NLB**. For more information about
    **Existing NLB**, reference the NLB stack in the [Wickr Enterprise CDK Sample](https://github.com/aws-samples/sample-packages-for-aws-wickr/tree/main/enterprise-infrastructure-examples/aws-cdk "https://github.com/aws-samples/sample-packages-for-aws-wickr/tree/main/enterprise-infrastructure-examples/aws-cdk") on GitHub.
2.  Do one of the following, depending on the **Calling Ingress
    Type**:

        * For **Existing NLB**, provide the target group ARNs for UDP and TCP
         traffic and the hostname of the NLB.
        * For **Load Balancer**, provide the hostname after it is provisioned by
         Kubernetes.

    Alternatively, for either **Calling Ingress Type**, you can provide the
    IP addresses of the load balancer or a custom hostname that points to the load
    balancer.

3.  (Optional) To combine messaging and calling traffic under a single NLB, choose
    **Existing NLB** in the **Ingress** section, and provide an
    HTTPS target group.

**Ingress with NodePort**

This option is useful if host networking is disabled and you don’t want to expose an
additional load balancer.

###### Note

Make sure your firewalls and security groups allow traffic for the NodePorts.

1. For **Calling Ingress Type**, choose
   **NodePort**.
2. Add the calling node hostnames or IP addresses.
3. Disable **Calling Host Network**.

**Direct ingress with HostNetwork**

This option does not expose any additional Kubernetes service and allows calling ingress
traffic to connect directly over the calling nodes’ host network. This approach is preferred if
IPv6 connectivity is required.

1. For **Calling Ingress Type**, select **No
   Service**.
2. Add the calling node hostnames or IP addresses.
3. Enable **Calling Host Network**.
