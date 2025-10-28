This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Sample HLS Output Group with Audio

Rendition Group Event Manifest

## Video Information for

an HLS Output Group with Audio Rendition Group Event

- There are two video streams, as indicated by the presence of two EXT-STREAM-INF
  lines.
  - The first video stream has a low bandwidth. As indicated by the AUDIO parameter, it is
    associated with “audio1.”
  - The second video stream has a higher bandwidth. As indicated by the AUDIO parameter, it
    is associated with “audio2.”

## Audio Information for

an HLS Output Group with Audio Rendition Group Event

- There are four audio streams as indicated by the presence of four EXT-X-MEDIA lines with
  TYPE=AUDIO.
- There are two audio rendition groups, as indicated by the values for the GROUP-ID in each
  line. The first two lines belong to audio1, the second two to audio2.
- In each audio stream, the values for the various parameters come from these fields in the
  web interface:
  - TYPE: Always Audio.
  - GROUP-ID: from Audio Group ID field in Output > Advanced.
  - LANGUAGE: from the Language Code field in Stream > Advanced.
  - NAME: from the Stream Name field in Stream > Advanced.
  - AUTOSELECT: from the Alternate Audio Track Type field (named Audio Track Selection
    in earlier versions) in Output > Advanced.
  - DEFAULT: from the Alternate Audio Track Selection field in Output > Advanced.
  - URI: from the combined Destination field (in Output Group) and Name Modifier field (in
    Stream).

## Captions Information

for an HLS Output Group with Audio Rendition Group Event

- There are two captions streams, as indicated by the presence of two EXT-X-MEDIA lines
  with TYPE=SUBTITLES.

```
#EXTM3U
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio1",LANGUAGE="eng",NAME="English",AUTOSELECT=YES, \
DEFAULT=YES,URI="eng1/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio1",LANGUAGE="fre",NAME="français",AUTOSELECT=YES, \
DEFAULT=NO,URI="fr1/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio2",LANGUAGE="eng",NAME="English",AUTOSELECT=YES, \
DEFAULT=YES,URI="eng2/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio2",LANGUAGE="fr",NAME="français",AUTOSELECT=YES, \
DEFAULT=NO,URI="fr2/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",LANGUAGE="eng",NAME="English",
DEFAULT=YES,AUTOSELECT=YES,FORCED=NO,URI="1c1.m3u8"
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",LANGUAGE="fra",NAME="French",
DEFAULT=YES,AUTOSELECT=YES,FORCED=NO,URI="1c2.m3u8"

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=195023,CODECS="avc1.42e00a,mp4a.40.2",AUDIO="audio1"
lo/prog_index.m3u8,SUBTITLES="subs",URI="1c2.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=591680,CODECS="avc1.42e01e,mp4a.40.2",AUDIO="audio2"
hi/prog_index.m3u8,URI="1c2.m3u8"
```
