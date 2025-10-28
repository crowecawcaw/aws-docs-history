# POIS conditioning

Elemental Live events can be configured to communicate with a POIS
server. During processing of the input, each time a SCTE-35 message is
encountered, Elemental Live sends the message contents to the server.
The POIS responds with SCTE-35 content that might be identical to the
original, slightly different from, or completely different from the
original.

Elemental Live also supports handling of “out-of-band” SCTE-35 messages from
the POIS – messages that are not a response to a message originally sent by Elemental Live. If such a message is received, Elemental Live accepts and
processes it.

## POIS conditioning and

other SCTE 35 features

This section describes how POIS conditioning interacts with other
SCTE 35 features that you can set up.

###### Ad avail mode

When POIS conditioning is enabled, the ad avail mode is always
set to _splice insert_. For
information about how this value affects the behavior of manifest
decoration and ad avail blanking see [Getting
ready: Setting the ad avail mode](getting-ready-setting-the-ad-avail-mode.md "getting-ready-setting-the-ad-avail-mode.md").

###### SCTE-35 messages inserted by REST API

All these messages are sent to the POIS along with messages that are already in the
input.

###### Manifest decoration

The effect of POIS conditioning on [manifest decoration](manifest-decoration.md "manifest-decoration.md") is as
follows:

- **HLS Outputs** – A
  message received from the POIS might include instructions to
  decorate an HLS manifest (not other types of manifests). This
  information is used to decorate the HLS manifest.

How Elemental Live processes the decoration information depends on how
the event or event has been configured:

    + If the event or event does not have manifest decoration enabled for HLS
     outputs, then the information is ignored.
    + If the event does have it enabled, then the decoration information is
     inserted in the manifest.
    + The information is inserted into the manifest “as is.”
     The style of the information might not match the styles (ad
     marker styles) specified in the event. Elemental Live
     doesn't check for format inconsistencies between these
     instructions and the ad marker style.

- **Other Outputs** – Decoration of other
  manifest types is according to the information in the SCTE-35 message and how the Elemental Live event is set up for manifest decoration and which ad avail
  mode is enabled. The POIS conditioning has no effect on these manifest types.

###### Blanking and blackout

The effect of POIS conditioning on blanking and blackout is as follows:

- **Extra Blackout Instructions**
  – A message received from the POIS might include explicit
  “blank the content corresponding to this SCTE-35 message”
  instructions for any SCTE-35 message.
- **Blanking Image** – A
  POIS response might include reference to a blanking .png or .bmp
  file. Elemental Live uses this file for any blanking/blackout if
  it can find the file at `/data/server/esam/`
  on the Elemental Live node.

If Elemental Live cannot find the file, it uses a black slate.

- **Restriction Flags** – In
  ESAM mode, the Override restriction flags in the Elemental Live
  event (**Ignore Web Delivery Allowed** flag and **Ignore No Regional
  Blackout** flag) are always cleared (not selected).
  See [Ad avail blanking and
  blackout](ad-avail-blanking-and-blackout.md "ad-avail-blanking-and-blackout.md").
- **Passthrough or Removal**
  – Without POIS conditoin, if passthrough is enabled in the
  Elemental Live event, then the rule is that all SCTE-35 message
  are passed through.

But when POIS conditioning is enabled, the POIS can override
this rule: if the POIS instruction is to remove a given SCTE-35
message, then that message is removed and is not passed through,
even though passthrough is enabled in Elemental Live.

## Procedure to

enable POIS conditioning

1. In the **Profile** or **Event** screen, select **Advanced Avail
   Controls** (in the Input section towards the top
   of the screen):
2. In **Ad Avail Trigger**, choose
   **ESAM**. More fields appear.
3. Complete the fields as follows:
   - Complete the first 6 fields to identify the endpoints on the POIS.
   - For **Response Signal Preroll**, change the
     value as desired to set the distance (in milliseconds) between the time that
     the SCTE-35 message is inserted and the start time of that ad avail.
