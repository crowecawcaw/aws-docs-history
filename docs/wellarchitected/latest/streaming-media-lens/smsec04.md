

# Content ingest protection
<a name="smsec04"></a>

Ingest endpoints accept content from providers and encoding devices. They need to be restricted to trusted sources and protected in transit to reduce the risk of injection, interception, or degradation.


| SMSEC04: How do you protect content ingest endpoints? | 
| --- | 
| [SMSEC04-BP01 Use Access Control Lists to restrict content to trusted providers only](smsec04-bp01.md) | 
| [SMSEC04-BP02 Encrypt content ingest traffic using TLS](smsec04-bp02.md) | 
| [SMSEC04-BP03 Use private connectivity when working with partners](smsec04-bp03.md) | 
| [SMSEC04-BP04 Encrypt content at rest when delivering via physical medium](smsec04-bp04.md) | 

## Capability intent
<a name="smsec04-intent"></a>
+ Only authorized sources can send content into workflows.
+ All ingest traffic is encrypted with current TLS versions.
+ High-value content travels over private connectivity rather than the public internet.
+ Physical media transfers use hardware encryption with chain-of-custody controls.

## Maturity levels
<a name="smsec04-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Ingest endpoints are open to any source with no IP restriction or encryption requirement. | 
| 2 | Emerging | Basic IP allowlists exist but are not regularly audited. TLS is used inconsistently across ingest paths. | 
| 3 | Defined | All ingest traffic is encrypted with current TLS versions. ACLs restrict access to known providers and are reviewed on a schedule. | 
| 4 | Proactive | High-value content uses private connectivity. ACL changes are automated through provider onboarding and offboarding workflows. | 
| 5 | Optimized | Physical media transfers use hardware encryption with chain-of-custody verification. Stale ACL entries are detected and removed automatically. | 

## Common issues to watch for
<a name="smsec04-issues"></a>
+ Ingest endpoints accepting connections from any IP address.
+ Unencrypted RTMP or HTTP contribution without TLS.
+ Source content sent over public internet without dedicated connectivity.
+ Stale ACL entries for former providers never removed.