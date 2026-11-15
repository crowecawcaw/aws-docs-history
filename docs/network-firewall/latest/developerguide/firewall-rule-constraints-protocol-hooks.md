

# Common hooks for common protocols
<a name="firewall-rule-constraints-protocol-hooks"></a>

The following table lists, for the protocols that customers most commonly filter, a common hook to use for a simple allow or deny rule and the keywords that become available at that hook. These are common choices, not the only valid ones—each protocol exposes more hooks than are listed here. For a rule that matches one of the listed keywords, use the hook shown. For a rule that matches no protocol field, you can use any valid hook for the protocol; the hook shown is a reliable default. For the full set of hooks each protocol exposes and the complete keyword reference, see the [Firewall design](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html) documentation.


| Protocol | Hook type | Common hook | Example keywords at that hook | 
| --- | --- | --- | --- | 
| TLS | Application | tls:client\_hello | tls.sni, tls.version (the version the client offered; to match the negotiated version, match tls.version on the server-to-client direction, such as in an IPS rule), ja3.hash, aws\_domain\_category (certificate keywords such as tls.cert\_subject are at tls:client\_cert and tls:server\_cert) | 
| HTTP/1.1 | Application | http1:request\_headers | http.host, http.header, http.user\_agent, aws\_url\_category (method and URI are at http1:request\_line) | 
| HTTP/2 | Application substate | http2:stream:request\_headers | http.host, http.method, http.uri, http.header | 
| DNS | Application (UDP) | dns:request\_complete | Query-name buffers such as dns.query (header fields such as dns.opcode are at dns:request\_started) | 
| SSH | Application | ssh:request\_banner\_done | ssh.proto, ssh.software, ssh.hassh | 
| TCP, UDP, SCTP | Packet | tcp:all, udp:all, sctp:all | Header and flow keywords such as tcp.flags, dsize, flow, geoip (no application-layer keywords) | 
| IP, ICMP | Packet | ip:all, icmp:all | ttl, ipopts, fragbits, itype, icode, geoip | 

**Note**  
HTTP/2 carries each request in a separate *stream*, so its hooks have an extra level in the token: `http2:stream:{{hook}}` for per-request matching. A `http2:global:{{hook}}` form also exists for whole-connection rules that don't match per-request content. Use the `stream` form to match request fields such as the host.

The rule-header token for HTTP/1.1 is `http1`, not `http`. A rule string that uses `http:{{hook}}` is rejected. In a modeled rule, you select the protocol `HTTP`, which is the modeled alias for `http1`; Network Firewall compiles it to the `http1` token in the rule string. (HTTP/2 is a separate protocol, `http2`.)