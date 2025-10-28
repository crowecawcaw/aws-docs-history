# SCTE-35 and SCTE-104 message

processing in Elemental Live

You can use Elemental Live to manipulate the SCTE-35 messages in a TS input and to
manipulate the SCTE-104 messages in an HD-SDI input. You can also use Elemental Live to remove

or include the cueing information conveyed by SCTE messages in the output streams (video,
audio, closed captioning, data) and any associated manifests.

You set up SCTE message processing instructions in the Elemental Live event. This
guide describes how to perform this set up.

Note that Elemental Live does not support processing of manifests that are present in
the input. The information in these manifests is not ingested by Elemental Live and
is not included in the output or the output manifest.

###### About this guide

SCTE messages might convey DPI cueing information for ad avails and
for other non-ad-avail messages such as programs and chapters.

This guide covers both Event Signaling and Management (ESAM) and non-ESAM processing of
messages.

###### Assumptions

You should be familiar with the SCTE-35 and SCTE-104 standards and optionally with the
SCTE-67 standards and how the input you encode implements these standards. You should be
familiar with profiles and with managing Elemental Live events. To use the REST API
features, you should be familiar with interacting with Elemental Live through the
API.

###### Topics

- [Eligible messages and
  streams](eligible-messages-and-streams.md "eligible-messages-and-streams.md")
- [Getting
  ready: Setting the ad avail mode](getting-ready-setting-the-ad-avail-mode.md "getting-ready-setting-the-ad-avail-mode.md")
- [Manifest decoration](manifest-decoration.md "manifest-decoration.md")
- [Ad avail blanking and
  blackout](ad-avail-blanking-and-blackout.md "ad-avail-blanking-and-blackout.md")
- [Passthrough or removal of
  SCTE messages](pass-through-or-removal.md "pass-through-or-removal.md")
- [SCTE-35 message insertion
  into currently running events](scte-35-message-insertion.md "scte-35-message-insertion.md")
- [POIS conditioning](pois-conditioning.md "pois-conditioning.md")
- [Setting up using the REST
  API](setting-up-via-the-rest-api.md "setting-up-via-the-rest-api.md")
- [Example manifests for Apple
  HLS](example-manifests-hls.md "example-manifests-hls.md")
