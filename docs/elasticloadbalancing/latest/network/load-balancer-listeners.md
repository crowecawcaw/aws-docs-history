

# Listeners for your Network Load Balancers
<a name="load-balancer-listeners"></a>

A *listener* is a process that checks for connection requests, using the protocol and port that you configure. Before you start using your Network Load Balancer, you must add at least one listener. If your load balancer has no listeners, it can't receive traffic from clients. The rule that you define for a listener determines how the load balancer routes requests to the targets that you register, such as EC2 instances.

**Topics**
+ [Listener configuration](#listener-configuration)
+ [Default actions](#default-actions)
+ [Listener attributes](#listener-attributes)
+ [Listener rules](#listener-rules)
+ [Secure listeners](#secure-listeners)
+ [ALPN policies](#alpn-policies)
+ [Create a listener](create-listener.md)
+ [Server certificates](tls-listener-certificates.md)
+ [Security policies](describe-ssl-policies.md)
+ [Update a listener](listener-update-rules.md)
+ [Listener rules](create-rule.md)
+ [Update idle timeout](update-idle-timeout.md)
+ [Update a TLS listener](listener-update-certificates.md)
+ [Delete a listener](delete-listener.md)

## Listener configuration
<a name="listener-configuration"></a>

Listeners support the following protocols and ports:
+ **Protocols**: TCP, TLS, UDP, TCP\_UDP, QUIC, TCP\_QUIC 
+ **Ports**: 1-65535

You can use a TLS listener to offload the work of encryption and decryption to your load balancer so that your applications can focus on their business logic. If the listener protocol is TLS, you must deploy at least one SSL server certificate on the listener. For more information, see [Server certificates](tls-listener-certificates.md).

If you must ensure that the targets decrypt TLS traffic instead of the load balancer, you can create a TCP listener on port 443 instead of creating a TLS listener. With a TCP listener, the load balancer passes encrypted traffic through to the targets without decrypting it.

You can use a QUIC listener to accept QUIC traffic. The Network Load Balancer acts as a pass through load balancer in accordance with [RFC9000](https://tools.ietf.org/html/rfc9000). Utilize a QUIC listener and QUIC enabled backends to enable seamless connection migration for mobile devices.

To support both TCP and UDP on the same port, create a TCP\_UDP listener. The target groups for a TCP\_UDP listener must use the TCP\_UDP protocol. 

To support both TCP and QUIC on the same port, create a TCP\_QUIC listener. The target groups for a TCP\_QUIC listener must use the TCP\_QUIC protocol.

A UDP listener for a dualstack load balancer requires IPv6 target groups.

WebSockets is supported only on TCP, TLS, TCP\_UDP, and TCP\_QUIC listeners.

QUIC traffic does not support version negotiation. QUIC v1 is the only supported QUIC version.

All network traffic sent to a configured listener is classified as intended traffic. Network traffic that does not match a configured listener is classified as unintended traffic. ICMP requests other than Type 3 are also considered unintended traffic. Network Load Balancers drop unintended traffic without forwarding it to any targets. TCP data packets sent to the listener port for a configured listeners that are not new connections or part of an active TCP connection are rejected with a TCP reset (RST).

For more information, see [Request routing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#request-routing) in the *Elastic Load Balancing User Guide*.

## Default actions
<a name="default-actions"></a>

When you create a listener, you specify a default action for routing requests. The default action forwards requests to the target groups that you specify.

**Distribute traffic to multiple target groups**  
If you specify multiple target groups for a default action, requests are distributed to these target groups based on their relative weights. You must specify a weight from 0 to 999 for each target group. A target group with a weight of 0 receives no traffic. After you add a target group or update the target group weights, new connections are routed based on the new target group weights. Existing connections are not affected and continue until they are closed as usual.

As an example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the target group with a weight of 10.

A common use case is migrating traffic from one target group to another. Meaning that you gradually increase the weight of the new target group while decreasing the weight of the original target group until it is 0. If you update the weight of a target group to 0, after a short period of time, it receives no new connections and existing connections are closed.

**Sticky sessions and weighted target groups**  
Forward actions on listeners can specify whether to enable target group stickiness. When enabled, target group stickiness causes subsequent connections from the same source IP address to prefer the previously chosen target group.

**Considerations**
+ For TLS listeners, you can't add both TCP target groups and TLS target groups to the listener rule. All target groups must use the same protocol.
+ For TLS listeners, target group stickiness is not supported.
+ For dualstack load balancers, you can't add both IPv4 target groups and IPv6 target groups to the same default action. All target groups in the default action must use the same IP address type.
+ For listeners, if a forward action contains multiple target groups and any of them have stickiness enabled, then the forward action must also have target group stickiness enabled.

## Listener attributes
<a name="listener-attributes"></a>

The following are the listener attributes for Network Load Balancers:

`tcp.idle_timeout.seconds`  
The tcp idle timeout value, in seconds. The valid range is 60-6000 seconds. The default is 350 seconds.

For more information, see [Update idle timeout](update-idle-timeout.md).

## Listener rules
<a name="listener-rules"></a>

The listener rules for your Network Load Balancer determine how it routes requests to targets. Each listener has a default action that forwards requests to a specified target group. You can add custom rules that evaluate conditions and route traffic to different target groups based on the source IP address type of incoming traffic. This enables you to route IPv4 and IPv6 traffic to separate target groups using a single dual-stack load balancer, eliminating the need for IPv4/IPv6 protocol translation and preserving end-to-end source IP connectivity.

**Rule basics**
+ Each rule consists of the following components: a priority, actions, and condition.
+ When you create a listener, you define the action for the default rule. The default rule can't have conditions. If none of the conditions for any other rules are met, the action for the default rule is performed.
+ Rules are evaluated in priority order, from the lowest value to the highest value. The default rule is evaluated last. You can't change the priority of the default rule.
+ Each rule must include exactly one `forward` action, which routes requests to one or more target groups.
+ Listener rules are only available on dual-stack Network Load Balancers.

**Topics**
+ [Rule conditions](#rule-conditions)
+ [Rule actions](#rule-actions)
+ [Rule priority](#rule-priority)
+ [Rule evaluation](#rule-evaluation)
+ [Considerations](#listener-rules-considerations)

### Rule conditions
<a name="rule-conditions"></a>

Each rule condition has a type and configuration information. When the conditions for a rule are met, the rule's action is performed.

The following is the supported condition type for Network Load Balancer listener rules:

`source-ip`  
Route based on the IP address type of the source traffic. You specify an `IpAddressType` value of `ipv4` or `ipv6`. When the source IP version of an incoming request matches the condition, the rule action is performed.  
The following is an example of a source-ip condition:  

```
{
  "Field": "source-ip",
  "SourceIpConfig": {
    "IpAddressType": "ipv4"
  }
}
```

**Note**  
The `source-ip` condition for Network Load Balancers uses `IpAddressType` to match traffic by IP version (IPv4 or IPv6). This differs from the Application Load Balancer `source-ip` condition, which uses CIDR ranges to match specific source IP addresses.

### Rule actions
<a name="rule-actions"></a>

Each rule action has a type and configuration information. The following is the supported action type for Network Load Balancer listener rules:

`forward`  
Forward requests to one or more specified target groups. If you specify multiple target groups for a `forward` action, you must specify a weight for each target group. Each target group weight is a value from 0 to 999. Requests that match a listener rule with weighted target groups are distributed to these target groups based on their weights. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group.

The following is an example of a forward action that routes to a single target group:

```
{
  "Type": "forward",
  "TargetGroupArn": "arn:aws:elasticloadbalancing:{{region}}:{{account-id}}:targetgroup/{{my-ipv4-tg}}/{{target-group-id}}"
}
```

The following is an example of a forward action that routes to two weighted target groups:

```
{
  "Type": "forward",
  "ForwardConfig": {
    "TargetGroups": [
      {
        "TargetGroupArn": "arn:aws:elasticloadbalancing:{{region}}:{{account-id}}:targetgroup/{{my-tg-1}}/{{target-group-id}}",
        "Weight": 70
      },
      {
        "TargetGroupArn": "arn:aws:elasticloadbalancing:{{region}}:{{account-id}}:targetgroup/{{my-tg-2}}/{{target-group-id}}",
        "Weight": 30
      }
    ]
  }
}
```

### Rule priority
<a name="rule-priority"></a>

Each rule has a priority. Rules are evaluated in priority order, from the lowest value to the highest value. The default rule is evaluated last. You can change the priority of a non-default rule at any time using the [set-rule-priorities](https://docs.aws.amazon.com/cli/latest/reference/elbv2/set-rule-priorities.html) command.

Each rule must have a unique priority value. You cannot create multiple rules with the same priority. If multiple rules match the incoming traffic, the rule with the highest priority (lowest numeric value) takes precedence.

### Rule evaluation
<a name="rule-evaluation"></a>

When traffic arrives at the Network Load Balancer listener, rules are evaluated in the following order:

1. Non-default rules are evaluated in priority order (lowest value first).

1. When the conditions for a rule are met, the rule's action is performed.

1. If no rule conditions are met, the default action is performed.

If listener rules cover all traffic scenarios (both IPv4 and IPv6), the default action may never be used. However, a default action is always required.

### Considerations
<a name="listener-rules-considerations"></a>

Prerequisites  
Listener rules require a dual-stack Network Load Balancer. The VPC and subnets must have IPv6 CIDR blocks associated, and the subnet route tables must route IPv6 traffic.

Rule evaluation and the default action  
Rules evaluate in priority order, where a lower priority number is evaluated first. Traffic that matches no rule falls through to the default action. Set the default action to the IP address family you want as the fallback.

Protocols and target groups  
Listener rules apply to TCP, UDP, TCP\_UDP, and TLS listeners. A UDP listener on a dual-stack Network Load Balancer requires an IPv6 target group, so make sure the IPv6 target group exists before you split UDP traffic.

Health checks  
Each target group health-checks its targets over its own IP address family. Confirm that target security groups allow health check traffic from the load balancer over both IPv4 and IPv6.

Performance and availability  
A consolidated dual-stack Network Load Balancer carries the combined traffic of both IPv4 and IPv6 address families, potentially doubling the load compared to two individual Network Load Balancers. While one Network Load Balancer provides simplification, two separate Network Load Balancers provide natural fault isolation per address family. Evaluate your scale and availability requirements before consolidating.

Compatibility with existing Network Load Balancer features  
Listener rules work alongside the existing Network Load Balancer feature set: connection draining (deregistration delay), target group stickiness (sticky sessions), cross-zone load balancing, client IP preservation (`preserve_client_ip`), and TLS termination on TLS listeners. Each target group maintains its own configuration.

Source IP preservation  
When client and target IP versions match (enabled by listener rules), traffic flows directly without protocol translation, maintaining end-to-end source IP preservation. This requires `preserve_client_ip` to be enabled on the target group.

Weighted target groups  
Listener rules support `ForwardConfig` with multiple weighted target groups, which is useful for canary rollouts or gradual migrations. Each target group takes a weight from 0 to 999, and a group with weight 0 receives no new connections.

Relationship to Application Load Balancer listener rules  
Both Network Load Balancers and Application Load Balancers use a `source-ip` condition, but they match on different attributes. Application Load Balancer matches the source address against one or more CIDR blocks (`SourceIpConfig.Values`), while Network Load Balancer matches on the IP address type of the source connection (`SourceIpConfig.IpAddressType`). In short, Application Load Balancer routes by specific address range, and Network Load Balancer routes by IP version.

Pricing and availability  
Listener rules are available in all AWS commercial Regions and the AWS GovCloud (US) Regions. There is no additional charge for the feature. You pay standard Network Load Balancer pricing for load balancer hours and LCUs. Consolidating separate IPv4 and IPv6 Network Load Balancers onto a single dual-stack Network Load Balancer removes the hours and LCU charges of the second load balancer.

For more information, see [Listener rules for your Network Load Balancer](create-rule.md).

## Secure listeners
<a name="secure-listeners"></a>

To use a TLS listener, you must deploy at least one server certificate on your load balancer. The load balancer uses a server certificate to terminate the front-end connection and then to decrypt requests from clients before sending them to the targets. Note that if you need to pass encrypted traffic to the targets without the load balancer decrypting it, create a TCP listener on port 443 instead of creating a TLS listener. The load balancer passes the request to the target as is, without decrypting it.

Elastic Load Balancing uses a TLS negotiation configuration, known as a security policy, to negotiate TLS connections between a client and the load balancer. A security policy is a combination of protocols and ciphers. The protocol establishes a secure connection between a client and a server and ensures that all data passed between the client and your load balancer is private. A cipher is an encryption algorithm that uses encryption keys to create a coded message. Protocols use several ciphers to encrypt data over the internet. During the connection negotiation process, the client and the load balancer present a list of ciphers and protocols that they each support, in order of preference. The first cipher on the server's list that matches any one of the client's ciphers is selected for the secure connection.

Network Load Balancers do not support mutual TLS authentication (mTLS). For mTLS support, create a TCP listener instead of a TLS listener. The load balancer passes the request through as is, so you can implement mTLS on the target.

Network Load Balancers support TLS resumption using PSK for TLS 1.3, and session tickets for TLS 1.2 and older. Resumptions with session ID, or when multiple certificates are configured in the listener using SNI, are not supported. The 0-RTT data feature and early\_data extension are not implemented.

For related demos, see [TLS Support on Network Load Balancer](https://exampleloadbalancer.com/nlbtls_demo.html) and [SNI Support on Network Load Balancer](https://exampleloadbalancer.com/nlbsni_demo.html).

## ALPN policies
<a name="alpn-policies"></a>

Application-Layer Protocol Negotiation (ALPN) is a TLS extension that is sent on the initial TLS handshake hello messages. ALPN enables the application layer to negotiate which protocols should be used over a secure connection, such as HTTP/1 and HTTP/2.

When the client initiates an ALPN connection, the load balancer compares the client ALPN preference list with its ALPN policy. If the client supports a protocol from the ALPN policy, the load balancer establishes the connection based on the preference list of the ALPN policy. Otherwise, the load balancer does not use ALPN.Supported ALPN Policies

The following are the supported ALPN policies:

`HTTP1Only`  
Negotiate only HTTP/1.\*. The ALPN preference list is http/1.1, http/1.0.

`HTTP2Only`  
Negotiate only HTTP/2. The ALPN preference list is h2.

`HTTP2Optional`  
Prefer HTTP/1.\* over HTTP/2 (which can be useful for HTTP/2 testing). The ALPN preference list is http/1.1, http/1.0, h2.

`HTTP2Preferred`  
Prefer HTTP/2 over HTTP/1.\*. The ALPN preference list is h2, http/1.1, http/1.0.

`None`  
Do not negotiate ALPN. This is the default.

**Enable ALPN Connections**  
You can enable ALPN connections when you create or modify a TLS listener. For more information, see [Add a listener](create-listener.md#add-listener) and [Update the ALPN policy](listener-update-certificates.md#update-alpn-policy).