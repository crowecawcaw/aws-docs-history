

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

## Common issues to watch for
<a name="smsec04-issues"></a>
+ Ingest endpoints accepting connections from any IP address.
+ Unencrypted RTMP or HTTP contribution without TLS.
+ Source content sent over public internet without dedicated connectivity.
+ Stale ACL entries for former providers never removed.