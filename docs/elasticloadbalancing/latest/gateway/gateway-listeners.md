

# Listeners for your Gateway Load Balancers
<a name="gateway-listeners"></a>

When you create your Gateway Load Balancer, you add a *listener*. A listener is a process that checks for connection requests.

Listeners for Gateway Load Balancers listen for all IP packets across all ports. You cannot specify a protocol or port when you create a listener for a Gateway Load Balancer.

When you create a listener, you specify a rule for routing requests. This rule forwards requests to the specified target group. You can update the listener rule to forward requests to a different target group.

## Listener attributes
<a name="listener-attributes"></a>

The following are the listener attributes for Gateway Load Balancers:

`tcp.idle_timeout.seconds`  
The tcp idle timeout value, in seconds. The valid range is 60-6000 seconds. The default is 350 seconds.

`send_tcp_reset.on_idle_timeout.enabled`  
Indicates whether the Gateway Load Balancer sends a TCP reset (RST) to the sender of traffic. If enabled, the Gateway Load Balancer sends the RST when a TCP flow's idle timeout expires, or when it receives a non-SYN TCP packet for a flow that is not in the flow table. The possible values are `true` and `false`. The default is `false`. After sending the RST, the Gateway Load Balancer removes the flow entry from its flow table.

For more information, see [Update idle timeout](update-idle-timeout.md).