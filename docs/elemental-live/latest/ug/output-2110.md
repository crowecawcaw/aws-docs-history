# Configuring SMPTE 2110 outputs

You can include one or more SMPTE 2110 outputs in an AWS Elemental Live event. You can
optionally configure the output to implement SMPTE 2022-7, so that the output delivers
identical content to two destinations, which improves resiliency for the downstream
system.

For general information about SMPTE 2110 video content, SMPTE 2022-7, NMOS, and SDP files,
see [Working with SMPTE 2110](SMPTE-ST-2110.md "SMPTE-ST-2110.md").

###### Note

You can't use AWS Elemental Conductor Live to produce SMPTE 2110 outputs that use NMOS. You can use AWS Elemental Conductor Live
to if you're not using NMOS.

###### Topics

- [Step 1: Get ready](s2110-output-get-ready.md "s2110-output-get-ready.md")
- [Step 2: Design the workflow](s2110-out-design-workflow.md "s2110-out-design-workflow.md")
- [Step 3: Create SMPTE 2110 output group](config-output-2110.md "config-output-2110.md")
- [Step 4: Download and post the SDP file](locate-sdp.md "locate-sdp.md")
