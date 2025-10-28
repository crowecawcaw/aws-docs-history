# Working with SMPTE 2110

Elemental Live supports both inputs and outputs that are compliant with the SMPTE 2110 suite of
standards.

The Elemental Live implementation of SMPTE 2110 provides an effective way to handle uncompressed and
lightly compressed video content. SMPTE 2110 uses standard IP networking to send and receive
content, which means it uses a cheaper and more readily available network infrastructure than
the traditional SDI protocol.

This section provides general information about the capabilities that SMPTE 2110 offers.
For detailed information about setting up SMPTE 2110 inputs, see [Ingesting SMPTE 2110 content](input-2110.md "input-2110.md").
For detailed information about setting up SMPTE 2110 outputs, see [Configuring SMPTE 2110 outputs](output-2110.md "output-2110.md").

**Separate streams**

SMPTE 2110 separates the key media—video, audio, and ancillary data—into separate streams,
or _essences_. This architecture cuts down on the
transmission costs compared to a transport stream, for example. This architecture also means
that there is less wasted processing (unnecessary demuxing) when ingesting the content. Elemental Live
only receives the specific video, audio, and ancillary data required for a specific
event.

**Uncompressed and lightly compressed content**

Elemental Live supports both video that is uncompressed, and video that is lightly compressed using
the JPEG XS codec. The JPEG XS codec reduces the bitrate of the video content, typically
without visible loss of video quality after multiple transcodes.

**SMPTE 2110 and SDP files**

The SMPTE 2110 specification relies on SDP files to describe the contents of the SMPTE 2110
streams. There is one file for each individual SMPTE 2110 stream. For more information about
SDP files, see [About SDP files](2110-sdp-about.md "2110-sdp-about.md").

**Support for NMOS**

Elemental Live supports NMOS IS-04 and IS-05 with both SMPTE 2110 inputs and outputs.

You can use NMOS to manage SMPTE 2110 streams. You can't use NMOS to manage other types of
streams. For more information about NMOS, see [Support for NMOS IS-04
stream
discovery](2110-and-nmos.md "2110-and-nmos.md").

**Conductor Live and SMPTE 2110 inputs with NMOS**

You can use Conductor Live to set up SMPTE 2110 inputs either with or without NMOS. If you're using
NMOS, the recommended procedure is to create a profile that includes a parameter for a device
input. Then when you create the channel, you set the parameter to either an SDI device (for an
SDI input) or to a SMPTE 2110 Receiver Group.

**Conductor Live and SMPTE 2110 outputs**

You can't use Conductor Live to produce SMPTE 2110 outputs that use NMOS. You can use AWS Elemental Conductor Live if
you're not including NMOS.

**Support for SMPTE 2022-7 – seamless protection
switching**

Elemental Live supports seamless protection switching (conforming with SMPTE 2022-7) for both SMPTE
2110 inputs and SMPTE 2110 outputs. Elemental Live uses SMPTE 2022-7 to implement resiliency via
redundant streams.

For more information about SMPTE 2022-7, see [Support for SMPTE 2022-7 – seamless protection
switching](2110-options.md "2110-options.md").

###### Topics

- [Requirements for the appliance and network](2110-appliance-reqs.md "2110-appliance-reqs.md")
- [Supported content](2110-supported-content.md "2110-supported-content.md")
- [About SDP files](2110-sdp-about.md "2110-sdp-about.md")
- [Support for SMPTE 2022-7 – seamless protection
  switching](2110-options.md "2110-options.md")
- [Support for NMOS IS-04
  stream
  discovery](2110-and-nmos.md "2110-and-nmos.md")
- [Setup: Remove bonded
  interfaces](s2110-setup-bonded-if.md "s2110-setup-bonded-if.md")
- [Setup: Reserve cores for SMPTE 2110](enable-2110.md "enable-2110.md")
- [Setup: Enable precision time protocol (PTP)](enable-ptp.md "enable-ptp.md")
