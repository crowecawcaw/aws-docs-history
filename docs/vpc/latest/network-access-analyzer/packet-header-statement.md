# Packet header statements in Network Access Analyzer

A packet header statement defines the traffic types for a match or exclude condition. If
you omit the packet header statement, all traffic types match. All fields are optional, but if
you use a packet header statement, you must use at least one of its fields.

You can specify the following fields:

- `Protocols` –
  The protocol strings to match. The possible values are `tcp`
  and `udp`. You can specify one of the values or both of the values.
  If you omit this field, packets with either the `tcp` or
  `udp` protocol are admitted.
- `SourceAddress` –
  The IP addresses or CIDR ranges. You can't specify this option with
  `SourcePrefixLists`. If specified, only packets with matching source addresses are admitted.
  If you don't specify `SourcePrefixLists` or
  `SourceAddresses`, packets with any source address are admitted.
- `SourcePrefixLists` –
  The IDs or ARNs of the prefix lists. You can't specify this option with
  `SourceAddresses`. If specified, only packets with matching source addresses are admitted.
  If you don't specify `SourcePrefixLists` or
  `SourceAddresses`, packets with any source address are admitted.
- `DestinationAddress` –
  The IP addresses or CIDR ranges. This option is mutually exclusive with
  `DestinationPrefixLists`. If specified, only packets with matching destination addresses are
  admitted. If you don't specify `DestinationPrefixLists` or `DestinationAddress`,
  packets with any destination address are admitted.
- `DestinationPrefixLists` –
  The IDs or ARNs of the prefix lists. This option is mutually exclusive with
  `DestinationAddress`. If specified, only packets with matching destination addresses are
  admitted. If you don't specify `DestinationPrefixLists` or `DestinationAddress`,
  packets with any destination address are admitted.
- `SourcePorts` –
  The ports or port ranges. If specified, only packets with source
  ports that match one of the ports or port ranges are admitted. If omitted, packets with any
  source port are admitted.
- `DestinationPorts` –
  The ports or port ranges. If specified, only packets
  with destination ports that match one of the ports or ranges are admitted. If omitted,
  packets with any destination port are admitted.
