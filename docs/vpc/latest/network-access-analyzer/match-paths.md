# Match conditions in Network Access Analyzer

A match condition defines the types of network paths that should be produced as findings.
A Network Access Scope must specify at least one match condition. A match condition can
contain a source and a destination. Each source and destination can include a resource
statement, a packet header statement, or both.

If a match condition has a source but no destination, it produces findings for the
following:

- Network paths that end at any supported resource
- Network paths that start at a network component specified in the resource statement of
  the source (if defined)
- Network paths with a packet header that matches the packet header statement of the
  source (if defined)

If a match condition has a destination but no source, it produces findings for the
following:

- Network paths that start at any supported resource and end at a network component
  specified in the resource statement of the destination (if defined)
- Network paths with a packet header that matches the packet header statement of the
  destination (if defined)
  If a match condition has both a source and destination, the network path must at the
  source entry and end at the destination.

If a Network Access Scope has multiple match conditions, it produces findings for any path
that satisfies at least one of the match conditions.
