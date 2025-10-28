# Design the encodes

In the first step of planning the channel, you [identified](planning-encodes.md "planning-encodes.md") the video, audio, and captions encodes to include in each output group. In the
second step, you organized these encodes into outputs in each output group.

Now in this third step, you must plan the configuration parameters for each encode. As part
of this plan, you identify opportunities for sharing encodes among outputs in the same output
group in the channel, and among outputs in different output groups in the channel.

###### Result of this procedure

After you have performed this procedure, you will have a list of video,
audio, and captions encodes to create.

###### Topics

- [Plan the encodes](plan-encodes.md "plan-encodes.md")
- [Identify encode sharing
  opportunities](plan-encode-sharing.md "plan-encode-sharing.md")

| Encode nickname | Characteristics of the encode                                   | Source            | Opportunity | Action                                                                                                                                                                                                                                                          |
| --------------- | --------------------------------------------------------------- | ----------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VideoA          | AVC 1920x1080, 5 Mbps                                           | HEVC              |             | Create this encode from scratch.                                                                                                                                                                                                                                |
| VideoB          | AVC 1280x720, 3 Mbps                                            | HEVC              | Clone       | Clone VideoA and change the bitrate. Perhaps also other fields.                                                                                                                                                                                                 |
| VideoC          | AVC 320x240, 750 Kbps                                           | HEVC              | Clone       | Clone VideoA and change the bitrate and perhaps other fields.                                                                                                                                                                                                   |
| AudioA          | AAC 2.0 in English at 192000 bps                                | AAC 2.0           |             | Create this encode from scratch.                                                                                                                                                                                                                                |
| AudioB          | AAC 2.0 in French at 192000 bps                                 | AAC 2.0           | Clone       | Clone AudioA and change the audio selector (the reference to the source) to the selector for French. Perhaps also change other fields.                                                                                                                          |
| CaptionsA       | WebVTT (object-style) converted from embedded, in English       | Embedded          |             | Create this encode from scratch.                                                                                                                                                                                                                                |
| CaptionsB       | WebVTT (object-style) converted from embedded, in French        | Embedded          | Clone       | Clone CaptionsC and change the captions selector (the reference to the source) to the selector for French. Perhaps also change other fields.                                                                                                                    |
| VideoD          | AVC 1920x1080, 5Mbps                                            | HEVC              | Share       | Share VideoA                                                                                                                                                                                                                                                    |
| AudioC          | Dolby Digital 5.1 in Spanish                                    | Dolby Digital 5.1 |             | Create this encode from scratch.                                                                                                                                                                                                                                |
| CaptionsC       | RTMP CaptionInfo (converted from embedded) in Spanish           | Embedded          | Clone       | Clone CaptionsA and change the captions selector (the reference to the source) to the selector for Spanish. Perhaps also change other fields.                                                                                                                   |
| VideoE          | AVC, 1920x1080, 5 Mbps                                          | HEVC              | Share       | Share VideoA                                                                                                                                                                                                                                                    |
| AudioD          | Dolby Digital 2.0 in Spanish                                    | AAC 2.0           |             | Create this encode from scratach. Although its source is the same as Aa, its output codec is different, which means all its configuration fields are different. Therefore, there is no advantage to cloning.                                                    |
| AudioE          | Dolby Digital 2.0 in French                                     | AAC 2.0           | Clone       | Clone AudioD and change the audio selector (the reference to the source) to the selector for French. Perhaps also change other fields.Don't clone AuduioB because AudioB and AudioA have different output codecs. Therefore, there is no advantage to cloning.  |
| AudioF          | Dolby Digital 2.0 in English                                    | AAC 2.0           | Clone       | Clone AuduioD and change the audio selector (the reference to the source) to the selector for English. Perhaps also change other fields.Don't clone AudioB because AudioB and AudioF have different output codecs. Therefore, there is no advantage to cloning. |
| CaptionsD       | DVB-Sub (object-style) converted from Teletext, in 6 languages. | Teletext          |             | Create this encode from scratch.                                                                                                                                                                                                                                |
