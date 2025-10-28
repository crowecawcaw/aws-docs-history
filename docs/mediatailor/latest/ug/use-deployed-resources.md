# Use the AWS CloudFormation deployed resources for CDN and MediaTailor integration

AWS Elemental MediaTailor resources deployed by the AWS CloudFormation stack provide several important outputs that you'll use to access your content with ad insertion. After the AWS CloudFormation stack is created successfully, you'll need to understand how to use
the outputs to access your content with ads inserted. This is similar to how you would
use MediaTailor URLs in a manual setup, but the AWS CloudFormation deployment provides these URLs
automatically.

After successful deployment, the AWS CloudFormation stack provides several important outputs that
you'll use to access your content with ad insertion:

`CloudFrontDomainName`

The domain name of your CloudFront distribution (e.g.,
`d1234abcdef.CloudFront.net`)

`HlsManifestUrl`

Base URL for HLS manifests with ad insertion (e.g.,
https://`d1234abcdef.CloudFront.net`/v1/master/`12345`/`my-playback-config`/)

`DashManifestUrl`

Base URL for DASH manifests with ad insertion (e.g.,
https://`d1234abcdef.CloudFront.net`/v1/dash/`12345`/`my-playback-config`/)

`MediaTailorPlaybackConfigName`

Name of the created MediaTailor playback configuration (such as
`my-stack-PlaybackConfig`)

## Construct playback URLs

To create the complete playback URL for your content with ads, you'll need to
combine the base URL from the AWS CloudFormation outputs with your specific manifest path. This
is a critical step for broadcast professionals to understand, as it connects your
existing content with the ad insertion system.

1. Start with the appropriate manifest URL from the outputs:

```
HlsManifestUrl: https://`d1234abcdef.CloudFront.net`/v1/master/`12345`/`my-playback-config`/
```

2. Append your specific manifest path:

```
Your manifest path: `channel/index.m3u8`
```

3. The complete playback URL becomes:

```
https://`d1234abcdef.CloudFront.net`/v1/master/`12345`/`my-playback-config`/`channel/index.m3u8`
```

Use this URL in your video player to play content with dynamically inserted
ads.

###### Tip

If you're not sure what your manifest path should be, check your origin
server. For MediaPackage origins, this is the path to your endpoint's HLS or DASH
manifest. For Amazon S3 origins, this is the path to your manifest file within the
bucket.

For more information about MediaTailor URL structure, see [Set up CDN integration with MediaTailor](cdn-configuration.md "cdn-configuration.md").

## Configure a video player

After you have your playback URL, you need to configure a video player to use it.
For broadcast professionals, this is similar to configuring a player for any HLS or
DASH stream, but now the stream will include personalized ads. Here's a simple
example using the popular HLS.js player:

```
<!DOCTYPE html>
<html>
<head>
    <title>MediaTailor Playback Example</title>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
</head>
<body>
    <video id="video" controls style="width: 640px; height: 360px;"></video>

    <script>
        const video = document.getElementById('video');
        const mediaUrl = 'https://<replaceable>d1234abcdef.CloudFront.net</replaceable>/v1/master/<replaceable>12345</replaceable>/<replaceable>my-playback-config</replaceable>/<replaceable>channel/index.m3u8</replaceable>';

        if (Hls.isSupported()) {
            const hls = new Hls();
            hls.loadSource(mediaUrl);
            hls.attachMedia(video);
        } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
            video.src = mediaUrl;
        }
    </script>
</body>
</html>
```

You can also use professional broadcast players like:

- JW Player
- Bitmovin Player
- THEOplayer
- Video.js

For more information about player integration with MediaTailor, see [MediaTailor ad server integration requirements](vast.md "vast.md").
