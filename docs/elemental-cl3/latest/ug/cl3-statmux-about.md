# Working with AWS Elemental Statmux

Include AWS Elemental Statmux nodes in your AWS Elemental Conductor Live cluster if you want to create MPTS outputs. A
multi-program transport stream (MPTS) is a UDP transport stream (TS) that carries multiple
programs. Conductor Live lets you create an MPTS that contains all variable bitrate programs, a mix of
variable and constant bitrate programs, or all constant bitrate programs.

You use AWS Elemental Statmux to ingest SPTS outputs from AWS Elemental Live and produce
MPTSes.

For Elemental Statmux, Conductor Live is a requirement. You can't run MPTSes without
Conductor Live.

###### Topics

- [Components of
  AWS Elemental Statmux in a cluster](smux-cluster-usage-components.md "smux-cluster-usage-components.md")
- [Features of AWS Elemental Statmux](cl3-statmux-features.md "cl3-statmux-features.md")
