# IPv6 support in Amazon Keyspaces

IPv6 support in Amazon Keyspaces allows applications to establish connections using Internet Protocol
version 6, the next-generation internet protocol that provides a vastly expanded address
space compared to IPv4. The implementation uses dual-stack endpoints that support both IPv4
and IPv6 simultaneously, ensuring backward compatibility while enabling future-ready
connectivity. For a list of endpoints, see [Global endpoints](programmatic.md#global_endpoints "programmatic.md#global_endpoints").

Amazon Keyspaces implements IPv6 support through a dual-stack architecture that maintains complete backward
compatibility while enabling IPv6 connectivity.

## DNS resolution in Amazon Keyspaces

When applications connect to dual-stack endpoints, the DNS resolution process returns both address types:

A Records (IPv4)

Traditional IPv4 addresses for backward compatibility

AAAA Records (IPv6)

New IPv6 addresses for modern connectivity

The client's operating system and network stack automatically select the most appropriate protocol
based on local configuration, network availability, and system preferences.

The Cassandra Query Language (CQL) protocol seamlessly supports IPv6 connectivity without requiring
application code changes.

Automatic protocol selection

- Applications specify the dual-stack endpoint
- Network stack chooses IPv4 or IPv6 based on availability
- No code modifications required for existing CQL applications

Driver compatibility

- All major CQL drivers support IPv6 transparently
- DataStax drivers handle IPv6 addresses natively
- Open-source drivers work without modification

Connection consistency

- System tables reflect the connection protocol used
- IPv6 connections show IPv6 addresses in `system.peers`
- IPv4 connections continue showing IPv4 addresses
