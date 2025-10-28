# Passing through SI/PSI

tables

You can pass through any stream from a source TS to the output
MPTS. You can pass through any number of streams.

This section describes the procedure for passing through one or
more SI/PSI tables that have been created outside of Elemental Statmux. If you
want to pass through a custom stream rather than an SI/PSI table,
see the previous section.

You can pass through the following:

- An SI/PSI table that Elemental Statmux doesn't implement. For
  example, an EIT.
- An SI/PSI table that Elemental Statmux does implement. For example, a
  PAT.
  You include the table by setting it up in the MPTS as a _passthrough stream_.

You can combine SI/PSI table passthrough with custom stream
passthrough and program passthrough.

**Setting up**

You pass through one or more SI/PSI tables by setting it up in the
MPTS as a _passthrough stream_.

To include passthrough streams, follow these steps:

- Design the MPTS workflow in the [regular
  way](setting-up-mpts-outputs.md "setting-up-mpts-outputs.md").
- When you create the MPTS, add the passthrough streams.

You must specify the following information for the
stream:

    + The location where the upstream system is sending
     the source program. Elemental Statmux listens for the stream at
     that location.
    + The PID to assign to this stream in the output
     MPTS.

For detailed instructions about passing through a stream,
see [Including passthrough
streams in an MPTS](crud-mpts-pasthrough-streams.md "crud-mpts-pasthrough-streams.md").

- You might want to suppress some or all of the tables that
  Elemental Statmux usually generates.

      + You must suppress table generation for a specific
       table if you are also passing through that table.
       Elemental Statmux won't allow two tables with the same
       PID.
      + You can optionally suppress table generation even
       if you aren't passing through the table. For
       example, you can suppress the PAT, even if you
       aren't passing it through. The MPTS won't include a
       PAT.

  For detailed instructions about suppressing table
  generation, see [Advanced tab –
  Suppressing generation of SI/PSI tables](step-create-mpts-tab-advanced.md "step-create-mpts-tab-advanced.md").
  **Handling by Elemental Statmux**

When passing through this type of stream, Elemental Statmux reads the PID of
a passthrough table, to ensure that it doesn't conflict with other
PIDs. But it treats the contents as a _black
box_. Elemental Statmux doesn't perform any validation on the
contents.

It is your responsibility to make sure that all the SI/PSI tables
are acceptable to the downstream system. It is your responsibility
to ensure that the SI/PSI tables correctly reference the program and
stream PIDs.
