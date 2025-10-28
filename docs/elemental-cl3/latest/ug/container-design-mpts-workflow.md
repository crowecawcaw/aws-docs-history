# Designing an MPTS

workflow

This section describes how to design a standard MPTS, and how to
augment that standard MPTS by including passthrough elements.

You can configure the MPTS to include multiple programs.

You can configure the MPTS to generate the following SI/PSI
tables:

- PAT. Required if you want to create a compliant MPTS.

- PMT for each program. Required if you want to create a
  compliant MPTS.
- NIT. Always optional.
- SDT. Always optional.
- TDT. Always optional.
  You can also configure the MPTS to pass through any SI/PSI tables that
  you pass in, both the tables the Elemental Statmux can generate, and those that it
  never generates.

###### Topics

- [Creating a standard
  MPTS](mpts-design-step-channels.md "mpts-design-step-channels.md")
- [Including passthrough
  programs](mpts-passthrough-program.md "mpts-passthrough-program.md")
- [Passing through custom
  streams](mpts-passthrough-high-pids.md "mpts-passthrough-high-pids.md")
- [Passing through SI/PSI
  tables](mpts-passthrough-PSI-pids.md "mpts-passthrough-PSI-pids.md")
