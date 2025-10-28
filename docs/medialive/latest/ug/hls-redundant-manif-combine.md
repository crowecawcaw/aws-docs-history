# Combining redundant manifests with other

features

## Combining redundant manifests and

custom path feature

When you set up redundant manifests in a MediaLive HLS output group, you can also set up
custom paths. Make sure that you follow the rules [for
custom paths](hls-custom-paths-rules.md "hls-custom-paths-rules.md") and for redundant manifests for your downstream system—either an
[Akamai CDN](hls-redundant-manif-akamai.md "hls-redundant-manif-akamai.md") or [another downstream system](hls-redundant-manif-most-systems.md "hls-redundant-manif-most-systems.md").

## Combining redundant manifests with audio

rendition groups

###### Note

The information in this section assumes that you are familiar with the manifests for
audio rendition groups. For more information, see [Sample manifest](sample-manifest.md "sample-manifest.md").

Following is information about the processing that MediaLive performs when you set up
redundant manifests in an HLS output group that includes an audio rendition group.

MediaLive automatically adjusts the references to the audio rendition groups in the parent
manifests.

In each pair of lines (for example, the `#EXT-X-STREAM-INF` for the
high-resolution video), MediaLive adjusts the name of the rendition groups. In this way, the
references to the rendition groups are different for each pipeline, which ensures that when
the client player reads the manifest, it chooses the video and the audio from the same
pipeline.

The `#EXT-X-STREAM` for the video for pipeline 0. Note the value for
_AUDIO_:

```
#EXT-X-STREAM-INF:BANDWIDTH=541107,...AUDIO="aac-audio-0", ...
```

The `#EXT-X-STREAM` for the video for pipeline 1. Note the value for
_AUDIO_:

```
#EXT-X-STREAM-INF:BANDWIDTH =541107, ...AUDIO="aac-audio-1",...
```
