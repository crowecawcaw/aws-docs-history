# Working with SMPTE 2022-6

Elemental Live supports sources that are compliant with the SMPTE
2022-6 standard. The Elemental Live implementation of SMPTE 2022-6
provides an effective way to handle uncompressed video content. SMPTE
2022-6 uses standard IP networking to receive content, which means it uses
a cheaper and more readily available network infrastructure than the
traditional SDI protocol.

Elemental Live supports redundant inputs using SMPTE 20227, and
non-redundant inputs.

With SMPTE 2022-6, the video, audio, and ancillary data are muxed into
one feed. Compare this design to SMPTE 2110, where the content is each in
a separate essence.

To work with SMPTE ST 2022-6 in Elemental Live, see [Ingesting SMPTE 2022-6 content](input-2022-6.md "input-2022-6.md").
