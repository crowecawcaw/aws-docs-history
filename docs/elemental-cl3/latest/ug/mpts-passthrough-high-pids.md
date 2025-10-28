# Passing through custom

streams

You can passthrough any stream from a source TS to the output
MPTS. You can pass through any number of streams.

This section describes the procedure for passing through a stream
whose PID isn't reserved for an SI/PSI table. For example, you might
want to pass through a stream that isn't part of any program because
your downstream system can use the data.

If you want to pass through an SI/PSI table rather than a custom
stream, see the next section.

**Setting up**

You include the stream by setting it up in the MPTS as a _passthrough stream_. The source of the
stream can be any well-formed transport stream.

To include a passthrough stream, design the workflow in the
regular way. When you create the MPTS, add the passthrough stream.
You must specify the following information for the stream:

- The location where the upstream system is sending the
  source transport stream. Elemental Statmux listens for the stream at that
  location.
- The PID to assign to this stream in the output MPTS.
  For detailed instructions about passing through a stream, see
  [Including passthrough
  streams in an MPTS](crud-mpts-pasthrough-streams.md "crud-mpts-pasthrough-streams.md").

**Handling by Elemental Statmux**

When the MPTS starts, Elemental Statmux connects to the location where the
upstream system is publishing the transport stream, and extracts the
packets for the specified PID.

- Elemental Statmux ignores and discards any SI/PSI tables that are in
  the transport stream. It extracts only the specified
  stream.
- Elemental Statmux includes the stream in the MPTS.
- Elemental Statmux doesn't include the stream PID in any of the SI/PSI
  tables for the MPTS.
