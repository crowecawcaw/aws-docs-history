

# Matching on destination context

**Note**  
Destination context matching works only for TCP and TCP-based application protocols. Network Firewall rejects destination context rules for other protocols, such as UDP and ICMP, when you create or update the rule group.

On the network path, the transit gateway stamps each packet with the context of that packet's *source*. It does this in both directions of the flow. It never provides a destination context.

To learn the destination, the network firewall uses the first packet that travels in the opposite direction, such as the server's response. That packet's source context is the flow's destination, so the firewall saves it as the flow's destination context. From then on, the firewall matches destination rules against all later packets in the flow, in both directions. Every resource type that works in the source position also works in the destination position.

A rule with a context ID in the destination position must use `tcp` or a TCP-based application protocol, such as `http` or `tls`. In a firewall rule, use the `tcp:all` hook or an application-layer protocol. Hooks that evaluate only at the start of a flow, such as `tcp:flow_start`, run before the firewall learns the destination, so they never match.

A rule with a context ID in the destination position doesn't match a flow's handshake packets, because the firewall hasn't learned the destination yet. The rule takes no action on those packets, whatever its action is: pass, drop, alert, or, in Next Generation Firewall rules, accept or reject. Your other rules and the policy's default action decide what happens to the handshake, so make sure they allow or block it as you intend.
+ The first packet a destination rule can match is the first client-to-server packet after the handshake. A drop or reject rule takes effect from that packet.
+ In a policy that drops traffic by default, a destination rule that accepts or passes traffic isn't enough on its own. Another rule must allow the handshake, or the connection never completes and the destination rule never matches.
+ Application-layer rules for protocols such as HTTP, TLS, and SSH run after the handshake. By then the firewall has learned the destination, so these rules evaluate every application-layer packet with the destination context in place.

Flow logs record the destination context after the firewall learns it. See [Context in your network firewall logs](context-aware-rules-logging.md).

The following examples show destination context rules:

The following firewall rule blocks connections from anywhere outside your home networks to your production database VPCs:

```
drop:flow tcp:all $EXTERNAL_NET any -> $PROD_DB_VPCS 3306 (msg:"Block external access to production databases"; sid:3001;)
```

Combine source and destination context in one firewall rule to segment tiers. Both conditions must hold:

```
accept:flow tcp:all $APP_SUBNETS any -> $DB_SUBNETS [3306,5432] (msg:"Allow application to database"; sid:3002;)
```

In an IPS rule, combine destination context with application-layer matching:

```
drop http any any -> $DEV_VPCS any (http.uri; content:"/admin"; msg:"Block admin paths into development VPCs"; sid:3003;)
```