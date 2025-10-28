# Rules for ingesting Apple

HLS TS sources

For video, each AWS Elemental Live event can extract only one video from
only one rendition. Elemental Live will not reject inputs that contain
multiple renditions, but it will handle only one of the renditions. There
are fields in the event for specifying which video to extract.

For audio, each Elemental Live event can extract audio from the same
rendition as the selected video. It can extract more than one audio from
that rendition. It cannot extract audio from two different renditions.
There are fields in the event for specifying which audio or audios to
extract.

Elemental Live cannot extract audio from a rendition that contains only
audio; it does not support ingest of audio rendition groups.

In all cases, the incoming HLS stream must include a manifest.
