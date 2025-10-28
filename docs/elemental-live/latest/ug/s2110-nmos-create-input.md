# Create a receiver group input

You must create a receiver group input that connects to the appropriate SMPTE 2110
receiver streams.

###### Note

The information in this section assumes that you are familiar with the general
steps for creating a Elemental Live event or Conductor Live channel.

1.  In the Elemental Live event or in the AWS Elemental Conductor Live profile, go to the Inputs section.
2.  Click **Add Input**. A row for the new input appears.
3.  Click the **Select Type** field to display a list of types.
    Select the receiver group that applies to this input. (Don't select
    **SMPTE 2110 Input**, which is an option that appears at the
    bottom of the list of types.) Optionally, enter a name for the input.
4.  Click **Advanced** to show more fields for this input. Scroll
    down to the selectors section of this input. Complete the selectors as
    follows:
    - **Video Selector**: Leave the single selector that
      appears by default. Ignore the **Program** and
      **PID** fields, which don't apply to SMPTE 2110 NMOS
      inputs. Complete the other fields as applicable.
    - **Audio Selector**: Click **Add Audio
      Selector** to display as many selectors as you need. For
      example, following the examples in [Create the receiver group](s2110-nmos-create-receiver-group.md "s2110-nmos-create-receiver-group.md"), you need three
      selectors.

    If the receiver group has more than one audio SDP, you must complete
    these fields:

        + **Selector Type**: Choose
         **Track**.
        + **Track**: Enter the track. Following the first
         example in [Create the receiver group](s2110-nmos-create-receiver-group.md "s2110-nmos-create-receiver-group.md"), enter
         `1` to identify the English audio,
         `2` to identify the French audio, and
         `3` to enter the Spanish audio. It doesn't
         matter if the audios are all in the same SDP or different SDPs, the
         audio streams are always numbered in SDP order, starting from 1.

5.  Click **Add Caption Selector** once. Make sure
    **Source** specifies **Embedded**. Ignore the
    other fields on this line, they don't apply to passing through embedded captions.
