# Including passthrough

programs

In any MPTS, you can include any number of *passthrough program*s. A passthrough program is a
source program that doesn't come from an Elemental Live node that is in the
Conductor Live cluster. The program could be either of the following:

- An MPTS produced by another encoder. That MPTS could
  include one or more SPTSes. Elemental Statmux lets you extract only the
  SPTSes that you want.
- An MPTS produced by an Elemental Live node that is not in the Conductor Live
  cluster. In this case, the MPTS is an output from a UPD/TS
  output group, where the MPTS Membership of the output hasn't
  been set up as remote.
  **Setting up**

You include the program by setting it up in the MPTS as a
_passthrough program_. These
rules apply:

- The source programs must be well-formed MPTSes. They must
  contain all the tables that Elemental Statmux expects, so that Elemental Statmux
  can process the program in the same way as it processes
  standard Elemental Live SPTSes.
- The source programs must have CBR video streams. They
  can't have VBR streams.
  To include passthrough programs, design the workflow in the
  regular way. When you create the MPTS, add passthrough programs. For
  each program, you must specify the following information:

- The location where the upstream system is sending the
  source program. Elemental Statmux listens for the stream at that
  location.
- The specific program to extract from the source
  MPTS.
- Data to use in the SI/PSI tables in the output
  MPTS.
- PIDs to assign to this program in the output MPTS.
  For much of this information, if you don't specify values, Elemental Statmux
  automatically assigns values when you save the MPTS. Elemental Statmux ensures
  that valid PIDs are assigned throughout the MPTS.

For detailed instructions about adding a passthrough program, see
[Including passthrough
programs in an MPTS](crud-mpts-passthrough-programs.md "crud-mpts-passthrough-programs.md").

**Handling by Elemental Statmux**

When the MPTS starts, Elemental Statmux connects to the source transport
stream that you specified and extracts the program that you
specified.

- Elemental Statmux uses the PAT and SDT to identify the PMT, then uses
  the PMT to identify the streams (the video, audio, and
  data).
- It then discards all the SI/PSI tables from the
  source.
- It assigns new output PIDs to the streams. You could
  specify the output PIDs that you want Elemental Statmux to use, but
  that step is optional.
- It restamps the PCR in each program as it inserts the
  packets.
- It creates a new PMT for the program, and includes that
  PMT in the PAT and SDT for the MPTS.
