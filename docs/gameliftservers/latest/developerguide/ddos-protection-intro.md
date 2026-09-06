

# DDoS protection with Amazon GameLift Servers
<a name="ddos-protection-intro"></a>

Amazon GameLift Servers provides multiple layers of DDoS protection to defend your game servers from DDoS attacks. All layers of protection are provided at no additional cost when you use Amazon GameLift Servers.

## AWS Shield Standard
<a name="ddos-protection-intro-shield-standard"></a>

AWS Shield Standard provides baseline network-level DDoS detection and mitigation for all AWS services, including Amazon GameLift Servers. Shield Standard delivers detection and reactive mitigation that minimizes application downtime and latency from common, frequently occurring network and transport layer DDoS attacks.

Shield Standard is the protection historically provided on Amazon GameLift Servers prior to the launch of Amazon GameLift Servers Enhanced DDoS Protection and Amazon GameLift Servers player gateway. Although Shield Standard provides foundational protection against common DDoS attack vectors, Amazon GameLift Servers now offers enhanced protections specifically designed for gaming workloads.

## Amazon GameLift Servers Enhanced DDoS Protection
<a name="ddos-protection-intro-enhanced"></a>

We operate some of the largest games in the world using Amazon GameLift Servers, and we have developed, tested, and proven effective an enhanced level of zero-touch, on by default DDoS protections. We have made these protections automatically enabled for games of all sizes with no configuration required and at no additional cost.

Amazon GameLift Servers Enhanced DDoS Protection leverages the resiliency of the AWS network and provides automatic protections that have been tuned and proven effective for protecting gaming workloads from common network and transport layer attacks. This significantly enhances baseline protections by providing proactive traffic shaping mitigations specifically designed for the unique traffic patterns of multiplayer games.

Amazon GameLift Servers Enhanced DDoS Protection is active from the moment you start running game servers on Amazon GameLift Servers. This protection is automatically enabled for all fleets except in the China (Beijing) and China (Ningxia) Regions. Coverage applies to fleets using Amazon GameLift Servers Server SDK 5 (SDKv5).

### Key benefits
<a name="ddos-protection-intro-enhanced-benefits"></a>
+ **Enabled automatically** – No action required to receive protection.
+ **Zero-touch** – No configuration necessary.
+ **Offered at no additional cost**
+ **Gaming-optimized mitigations** – Traffic shaping rules are specifically designed for gaming workloads, tuned from experience protecting some of the world's largest games.
+ **Network and transport layer defense** – Protects against common volumetric attacks at layers 3 and 4, including UDP reflection, SYN floods, and other common DDoS attack vectors.
+ **Enhanced protection** – Provides proactive, gaming-specific protections that go significantly beyond baseline DDoS protections.

## Amazon GameLift Servers player gateway
<a name="ddos-protection-intro-advanced"></a>

With Amazon GameLift Servers player gateway, you get our highest level of protection against sophisticated or targeted attacks using a relay-based network architecture. Player gateway validates and routes player traffic through relay endpoints, hiding your game server IP addresses from the public, rate limiting traffic for each player, and ensuring that only authenticated player traffic reaches your servers.

Player gateway requires integration steps—you must enable it during fleet creation and update your game client and game backend—but provides maximum protection for games facing persistent or targeted DDoS threats. Like Amazon GameLift Servers Enhanced DDoS Protection, player gateway is provided at no additional cost with Amazon GameLift Servers.

### Key benefits
<a name="ddos-protection-intro-advanced-benefits"></a>
+ **Hide game server IP addresses** – Game clients connect through relay endpoints instead of directly to game servers, hiding your game server addresses from the public.
+ **Traffic validation** – All traffic through player gateway requires a valid token, allowing only traffic from authenticated players to reach your game servers.
+ **Rate limiting for each player** – Traffic is rate limited for each player, preventing any single player or attacker from overwhelming your game servers.
+ **Improved observability** – Gain visibility into traffic patterns and potential threats through player gateway metrics and monitoring.

For details on how player gateway works and how to integrate it, see [Amazon GameLift Servers player gateway](ddos-protection-player-gateway.md).

## Choosing the right level of protection
<a name="ddos-protection-intro-comparison"></a>

Amazon GameLift Servers provides three tiers of DDoS protection, all included at no additional cost. Each tier builds upon the previous, providing progressively stronger defense:

AWS Shield Standard is the foundational network-level DDoS protection provided to all AWS services. It offers detection and reactive mitigation for common DDoS attacks. Prior to the launch of Amazon GameLift Servers Enhanced DDoS Protection, this was the only automatic protection available on Amazon GameLift Servers. Although Shield Standard remains active, the protections described below provide significantly greater defense for gaming workloads.


| Feature | AWS Shield Standard | Amazon GameLift Servers Enhanced DDoS Protection | Amazon GameLift Servers player gateway | 
| --- | --- | --- | --- | 
| Enabled by default | Yes – SDKv4 | Yes – SDKv5\* | No – Opt-In Required | 
| Configuration required | None | None | Fleet and client integration | 
| Additional cost | None | None | None | 
| Network layer (L3/L4) mitigation | Reactive | Proactive, gaming-optimized | Proactive, gaming-optimized | 
| Gaming-specific traffic shaping | No | Yes | Yes | 
| Game server IP obfuscation | No | No | Yes | 
| Traffic validation for each player | No | No | Yes | 
| Rate limiting for each player | No | No | Yes | 
| Traffic distribution across relay endpoints | No | No | Yes | 

\* For instances launched following the release of Amazon GameLift Servers Enhanced DDoS Protection.

Consider the following when deciding which level of protection is right for your game:
+ **Amazon GameLift Servers Enhanced DDoS Protection** is appropriate for all games running on Amazon GameLift Servers. It provides substantial, proven protection against network and transport layer attacks with zero integration effort and no changes to your game client or backend.
+ **Amazon GameLift Servers player gateway** is recommended for games that are high-profile targets for DDoS attacks, require hidden server IP addresses, or need traffic validation for each player. It requires integration work but provides the strongest level of protection available on Amazon GameLift Servers.

The enhanced DDoS protection features offered by Amazon GameLift Servers give you the flexibility to select the level of protection your game requires while working within the often rigorous timelines faced by game developers. Both options have been proven effective at protecting games of all sizes.