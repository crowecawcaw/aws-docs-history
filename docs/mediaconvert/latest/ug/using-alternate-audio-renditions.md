# Alternate HLS audio

rendition requirements

With HLS rendition groups, you can use the audio selector settings to indicate
which alternate audio rendition you want MediaConvert to use. To be eligible for
selection, your alternate audio renditions must conform to the following
requirements:

- The renditions must be included in `EXT-X-MEDIA` tags in the
  input multivariant playlist.
- The `EXT-X-MEDIA` tags must contain a unique combination of
  GROUP-ID, NAME, and LANGUAGE values..
- Audio must be in one of the following supported audio codecs:
  AAC, Dolby Digital (AC3), Dolby Digital
  Plus (EAC3), or MP3.
- The variant playlist for your alternate audio rendition must be included in
  the multivariant playlist that you used for your Input file URL (FileInput)
  When you specify audio selector settings to identify an alternate audio
  rendition, the audio selector looks for a matching `EXT-X-MEDIA` tag in
  the multivariant playlist.

You can use one or more selector settings at a time. For example, given the
following `EXT-X-MEDIA` tags, you can identify the audio rendition by the
name (RenditionName) or language (RenditionLangageCode) because these are both
unique values across the tags.

`#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",CHANNELS="2",NAME="English",LANGUAGE="eng",DEFAULT=YES,AUTOSELECT=YES,URI="english_audio.m3u8"`

`#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",CHANNELS="2",NAME="Japanese",LANGUAGE="jpn",DEFAULT=NO,AUTOSELECT=NO,URI="japanese_audio.m3u8"`

However, because the group ID (RenditionGroupID) is the same for both tags, you
can't use that alone to identify an audio rendition. You must use the group ID in
combination with another value from the `EXT-X-MEDIA` tag to identify the
audio rendition that you want MediaConvert to use.

If you don't specify audio selector settings, the audio selector looks for audio
that's muxed into the video segments. If the video segments don't contain audio, the
audio selector uses the first alternate audio rendition from the input parent
manifest.
