# Assess the upstream system

As part of the planning of the MediaLive workflow, you must assess the upstream system that is
the source of the content, to ensure that it is compatible with MediaLive. Then you must assess the
source content to ensure that it contains formats that MediaLive can ingest and that MediaLive can include
in the outputs you want.

You obtain the _source content_ from a _content provider_. The source content is provided to you from an
_upstream system_ that the content provider controls. Typically,
you have already identified the content provider. For more information about source content and
upstream systems, see [How MediaLive works](how-medialive-works-channels.md "how-medialive-works-channels.md").

###### To assess the upstream system

1. Speak to the content provider to obtain information about the upstream system. You use this
   information to assess the ability of MediaLive to connect to the upstream system, and to assess the
   ability of MediaLive to use the source content from that upstream system.

For details about the information to obtain and assess, see the sections that
follow: 2. Make a note of the MediaLive input type that you identify for the source content. 3. Make a note of the following three characteristics of the source stream. You will need this
information [when you set up the channel](input-specification.md "input-specification.md"):

    * The video codec
    * The resolution of the video—SD, HD, or UHD
    * The maximum input bitrate

**Result of this step**

At the end of this step, you will be confident that MediaLive can ingest the content. In addition
you will have identified the following:

- The type of MediaLive input you will create to ingest the source content.
- The information that you need to extract the video, audio, and captions from the source
  (from the MediaLive input). For example:

| Information                                         | Format                           | Characteristics                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source formats and packaging                        | RTP                              | with FEC                                                                                                                                                                                                                                                                                                                      |
| Supported video codecs                              | HEVC                             | 1920x1080 5 Mbps maximum                                                                                                                                                                                                                                                                                                      |
| Supported audio codecs, coding modes, and languages | Dolby Digital 5.1                | English, Spanish                                                                                                                                                                                                                                                                                                              |
| AAC 2.0                                             | English, Spanish, French, German |
| Supported captions formats                          | Embedded                         | English, Spanish, French, German                                                                                                                                                                                                                                                                                              |
| Teletext                                            | 10 languages                     | ###### Topics <br>• [Assess source formats and packaging](uss-obtain-info.md "uss-obtain-info.md") <br>• [Assess video content](assess-uss-source.md "assess-uss-source.md") <br>• [Assess audio content](assess-uss-audio.md "assess-uss-audio.md") <br>• [Assess captions](assess-uss-captions.md "assess-uss-captions.md") |
