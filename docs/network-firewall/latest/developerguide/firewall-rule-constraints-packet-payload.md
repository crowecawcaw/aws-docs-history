

# Payload matching and packet hooks

Payload-matching keywords—`content`, `pcre`, `byte_test`, `byte_jump`, and `isdataat`—search the contents of traffic. In a firewall rule, these keywords are valid only at an application-layer hook, where the match binds to a specific protocol buffer such as the TLS SNI or the HTTP host. They aren't valid at a packet hook (such as `tcp:all` or `udp:all`). If you put a payload-matching keyword on a packet hook, Network Firewall rejects the rule with a message that payload matches aren't supported on a packet hook.

To match content, choose the application-layer hook where that content appears (see [Common hooks for common protocols](firewall-rule-constraints-protocol-hooks.md)), and pair the payload keyword with the protocol buffer keyword for that field. For example, match a TLS SNI by pairing `content` with `tls.sni` at the `tls:client_hello` hook:

```
accept:flow tls:client_hello $HOME_NET any -> $EXTERNAL_NET any (tls.sni; content:"example.com"; sid:1;)
```

At a packet hook, use only header and flow keywords—such as `dsize`, `ttl`, `tcp.flags`, `itype`, `icode`, `fragbits`, and `flow`—which match packet and connection metadata rather than payload contents. To key a packet rule off a detected application protocol without matching payload, use the `app-layer-protocol` keyword, for example `app-layer-protocol:tls`. For more about packet-layer and application-layer rule tables and how payload matching binds to protocol buffers, see [Firewall design](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html) in the [Suricata User Guide](https://docs.suricata.io/en/suricata-8.0.3/index.html).