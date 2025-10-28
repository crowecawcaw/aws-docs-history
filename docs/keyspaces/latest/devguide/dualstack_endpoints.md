# Connecting to dual-stack endpoints

Amazon Keyspaces global endpoints are dual-stack endpoints that accept IPv4 and IPv6 requests.

When connecting to Amazon Keyspaces using IPv6, the service automatically adapts system table responses to match your
connection protocol. This ensures that your applications receive consistent network address information matching
their connection type. This provides accurate network topology information to the client while maintaining backward
compatibility for existing CQL applications.

Amazon Keyspaces detects the network protocol (IPv4 or IPv6) used by your client connection automatically
and adjusts the system table responses accordingly. This detection happens transparently during the initial
connection handshake, requiring no additional configuration from the client application.

Amazon Keyspaces returns IP addresses based on your connection protocol. For example,
a request from an IPv4 network returns the following response.

```
SELECT * FROM system.peers;
-- Returns IPv4 addresses in peer column
-- Example: 172.31.1.1, 172.31.1.2, etc.
```

A connection from an IPv6 network to a dual-stack endpoint,
for example `cassandra.us-east-1.api.aws`, returns the following response.

```
SELECT * FROM system.peers;
-- Returns IPv6 addresses in peer column
-- Example: 2001:db8::1, 2001:db8::2, etc.
```

For more information about IPv6 support in Amazon Keyspaces, see [IPv6 support in Amazon Keyspaces](ipv6-support.md "ipv6-support.md").
