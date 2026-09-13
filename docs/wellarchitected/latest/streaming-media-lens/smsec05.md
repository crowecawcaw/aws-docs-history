

# Infrastructure protection
<a name="smsec05"></a>

Content origins need protection from DDoS attacks at both network and application layers, unauthorized direct access bypassing the CDN, and application-level exploits.


| SMSEC05: How do you protect content origin from unauthorized access and malicious attacks? | 
| --- | 
| [SMSEC05-BP01 Use distributed denial of service (DDoS) protection service to maintain content availability](smsec05-bp01.md) | 
| [SMSEC05-BP02 Restrict content origin access to only allow known entities](smsec05-bp02.md) | 
| [SMSEC05-BP03 Use a web application firewall to monitor and control content access](smsec05-bp03.md) | 

## Capability intent
<a name="smsec05-intent"></a>
+ Origins are shielded behind CDN and DDoS protection.
+ Direct access to origins is blocked for all external traffic.
+ Application-layer attacks are filtered by AWS WAF rules tuned to streaming patterns.
+ Traffic anomalies trigger alerts and automated response.

## Maturity levels
<a name="smsec05-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Origins are directly exposed to the internet with no CDN or DDoS protection layer. | 
| 2 | Emerging | A CDN fronts the origin but security groups still allow broad access. AWS WAF is deployed in count-only mode. | 
| 3 | Defined | DDoS protection is active, origins accept traffic only from CDN IPs, and AWS WAF rules block known attack patterns. | 
| 4 | Proactive | Streaming-specific AWS WAF rules (manifest rate limiting, bot detection) are in place. Traffic anomalies trigger automated mitigation. | 
| 5 | Optimized | AWS WAF rules and DDoS thresholds are continuously tuned from traffic analysis. Origin shielding consolidates requests and automated responses adapt to emerging attack patterns. | 

## Common issues to watch for
<a name="smsec05-issues"></a>
+ Origins exposed without DDoS protection or CDN in front.
+ Security groups allowing all sources rather than restricting to CDN IPs.
+ AWS WAF deployed in count-only mode indefinitely without moving to block.
+ No streaming-specific AWS WAF rules (rate limiting on manifest requests, bot detection).