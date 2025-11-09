# Including accessibility data in audio encodes

In the audio in CMAF Ingest or Microsoft Smooth output groups, you can include accessibility
data. This data describes the type of accessibility that the encode represents. For example, an
audio track might actually be a spoken description of what's happening in the video.
Accessibility data is also known as accessibility signaling.

MediaLive also includes a feature for including accessibility data in captions. For more
information, see [Including accessibility data in captions in
MediaLive](captions-accessibility.md "captions-accessibility.md").

## Supported accessibility data standards

MediaLive supports the following styles of accessibility data.

| Accessibility data style | Specification                                                  | CMAF Ingest | Microsoft Smooth |
| ------------------------ | -------------------------------------------------------------- | ----------- | ---------------- |
| DASH role audio          | DASH role scheme (_ISO/IEC 23009-1:2022(E))_                   | Yes         | Yes              |
| DVB DASH accessibility   | _ETSI TS 103 285 Technical Specification, V1.3.1<br>(2020-02)_ | Yes         | Yes              |

## Specifying accessibility data

###### Note

The information in this section assumes that you are familiar with the general steps for
creating or editing a channel.

1.  In the **Create channel** or **Edit channel** page for
    the channel, in the **Channel** panel, find the output group that you want to
    set up. Then find the audio output where you want to configure accessibility data.
2.  Select the output by its name. The details appear on the right. Go to the
    **Stream** settings section and choose the **Audio**
    section.
3.  Open the **Additional settings** and set the accessibility data
    fields.

        * To include DASH Roles, choose **Add dash roles** as many times as you
         want. In **DASH Role Audio**, choose the style in each role.
        * To include DVB DASH accessibility style, in **DVB DASH accessibility**,
         choose the applicable description. You can add only one instance of this accessibility
         style.

    You can add more than one style of acessibility data to each encode. For example, you can
    add Dash Roles and DVB DASH accessibility style. You might want to do this because different
    downstream systems for these outputs implement different styles.

## Handling of accessibility data

The fields for accessibility data appear in the encode fields in all output group types,
including types that don't support this data.

###### Note

When you set up audio encodes and you plan to include accessibility data, proceed as
follows. First create the audio encodes in the CMAF Ingest and/or Microsoft Smooth output
groups, and set up the accessibility data. Then create the audio encodes in the other output
groups.

**Handling in supported output groups**

If you aren't implementing shared audio encodes, MediaLive includes the data only in the audio
outputs of the CMAF Ingest and Microsoft Smooth output groups that you set up for audio
accessibility data.

**Handling in shared encodes**

You might plan to share audio encodes among several output groups. For example, you might
share an audio encode among at least one CMAF Ingest or Microsoft output group, and with other
output groups.

If you set up accessibility data in a shared audio encode, MediaLive will handle the data as
follows:

- It will include the data in the CMAF Ingest and Microsoft Smooth output groups that share
  the encode.
- It won't include the data in other output groups, because those output groups don't
  support this data. Even though the output group is sharing the encode, MediaLive won't include the
  data.

**Handling in other output groups**

You might try to set up accessibility fields in an output that doesn't support accessibility
data. If you're not implementing encode sharing with a CMAF Ingest or Microsoft Smooth output
group, you will get an error message when you save the channel.
