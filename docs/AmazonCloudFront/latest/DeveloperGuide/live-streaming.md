# Deliver video streaming with CloudFront and AWS Media

Services

To use AWS Media Services with CloudFront to deliver live content to a global audience,
see the following guidance.

Use [AWS Elemental MediaLive](../../../medialive/latest/ug/getting-started.md "../../../medialive/latest/ug/getting-started.md") to encode live
video streams in real time. To encode a large video stream, MediaLive compresses it into
smaller versions (_encodes_) that can be distributed to
your viewers.

After you compress a live video stream, you can use either of the following two main
options to prepare and serve the content:

- **Convert your content into required formats, and then
  serve it** – If you require content in multiple formats, use
  [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/ "https://aws.amazon.com/mediapackage/") to package the
  content for different device types. When you package the content, you can also
  implement extra features and add digital rights management (DRM) to prevent
  unauthorized use of your content. For step-by-step instructions for using CloudFront
  to serve content that MediaPackage formatted, see [Serve live video formatted with
  AWS Elemental MediaPackage](#live-streaming-with-mediapackage "#live-streaming-with-mediapackage").
- **Store and serve your content using scalable
  origin** – If MediaLive encoded content in the formats required
  by all of the devices that your viewers use, use a highly scalable origin like
  [AWS Elemental MediaStore](../../../mediastore/latest/ug/getting-started.md "../../../mediastore/latest/ug/getting-started.md") to serve the
  content. For step-by-step instructions for using CloudFront to serve content that is
  stored in a MediaStore container, see [Serve video by using AWS Elemental MediaStore as the
  origin](#video-streaming-mediastore "#video-streaming-mediastore").
  After you’ve set up your origin by using one of these options, you can distribute live
  streaming video to viewers by using CloudFront.

###### Tip

You can learn about an AWS solution that automatically deploys services for
building a highly available real-time viewing experience. To see the steps to
automatically deploy this solution, see [Live
Streaming Automated Deployment](../../../solutions/latest/live-streaming/deployment.md "../../../solutions/latest/live-streaming/deployment.md").

###### Topics

- [Serve video by using AWS Elemental MediaStore as the
  origin](#video-streaming-mediastore "#video-streaming-mediastore")
- [Serve live video formatted with
  AWS Elemental MediaPackage](#live-streaming-with-mediapackage "#live-streaming-with-mediapackage")
- [Serve video-on-demand content with
  AWS Elemental MediaPackage](#live-streaming-mediapackage-vod "#live-streaming-mediapackage-vod")

## Serve video by using AWS Elemental MediaStore as the

origin

If you have video stored in an [AWS Elemental MediaStore](../../../mediastore/latest/ug/getting-started.md "../../../mediastore/latest/ug/getting-started.md") container, you can create a CloudFront distribution to serve the
content.

To get started, you grant CloudFront access to your MediaStore container. Then you create a
CloudFront distribution and configure it to work with MediaStore.

###### To serve content from an AWS Elemental MediaStore container

1.  Follow the procedure at [Allowing Amazon CloudFront to access your AWS Elemental MediaStore
    container](../../../mediastore/latest/ug/cdns-allowing-cloudfront-to-access-mediastore.md "../../../mediastore/latest/ug/cdns-allowing-cloudfront-to-access-mediastore.md"), and then return to these steps to create your
    distribution.
2.  Create a distribution with the following settings:
    1.  **Origin domain** – The data endpoint that
        is assigned to your MediaStore container. From the dropdown list, choose
        the MediaStore container for your live video.
    2.  **Origin path** – The folder structure in
        the MediaStore container where your objects are stored. For more
        information, see [Origin path](DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath "DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath").
    3.  **Add custom header** – Add header names
        and values if you want CloudFront to add custom headers when it forwards
        requests to your origin.
    4.  **Viewer protocol policy** – Choose
        **Redirect HTTP to HTTPS**. For more
        information, see [Viewer protocol
        policy](DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy "DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy").
    5.  **Cache policy** and **Origin request
        policy**

            * For **Cache policy**, choose
             **Create policy**, and then create a
             cache policy that’s appropriate for your caching needs and
             segment durations. After you create the policy, refresh the
             list of cache policies and choose the policy that you just
             created.
            * For **Origin request policy**, choose
             **CORS-CustomOrigin** from the dropdown
             list.For the other settings, you can set specific values based on other

        technical requirements or the needs of your business. For a list of all the
        options for distributions and information about setting them, see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

3.  For links in your application (for example, a media player), specify the
    name of the media file in the same format that you use for other objects
    that you’re distributing using CloudFront.

## Serve live video formatted with

AWS Elemental MediaPackage

If you formatted a live stream by using AWS Elemental MediaPackage, you can create a CloudFront
distribution and configure cache behaviors to serve the live stream. The following
process assumes that you have already [created
a channel](../../../mediapackage/latest/ug/channels-create.md "../../../mediapackage/latest/ug/channels-create.md") and [added endpoints](../../../mediapackage/latest/ug/channels-add-endpoint.md "../../../mediapackage/latest/ug/channels-add-endpoint.md") for your live video using MediaPackage.

To create a CloudFront distribution for MediaPackage manually, follow these steps:

###### Steps

Complete the following procedure to set up a CloudFront distribution for the live
video channel that you created with MediaPackage.

###### To

create a distribution for your live video channel

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose **Create distribution**.
3. Choose the settings for the distribution, including the
   following:

**Origin domain**

The origin where your MediaPackage live video channel and
endpoints are. Choose the text field, then from the dropdown
list, choose the MediaPackage origin domain for your live video.
You can map one domain to several origin endpoints.

If you created your origin domain using another AWS
account, type the origin URL value into the field. The
origin must be an HTTPS URL.

For example, for an HLS endpoint like
`https://3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com/out/v1/abc123/index.m3u8`,
the origin domain is
`3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com`.

For more information, see [Origin domain](DownloadDistValuesOrigin.md#DownloadDistValuesDomainName "DownloadDistValuesOrigin.md#DownloadDistValuesDomainName").

**Origin path**

The path to the MediaPackage endpoint from where the content is
served.

For more information about how an origin path works, see
[Origin path](DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath "DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath").

###### Important

The wildcard path `*` is required to route somewhere in
the CloudFront distribution. To prevent requests not matching an explicit
path from routing to the real origin, create a "dummy"
origin for that wildcard path.

###### Example: Creating a "dummy" origin

In the following example, the endpoints `abc123` and
`def456` route to the "real" origin, but
requests for any other endpoint's video content route to
`mediapackage.us-west-2.amazonaws.com` without the
proper subdomain, which results in an HTTP `404`
error.

MediaPackage endpoints:

```
https://3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com/out/v1/abc123/index.m3u8
https://3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com/out/v1/def456/index.m3u8
```

CloudFront Origin A:

```
Domain: 3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com
Path: None
```

CloudFront Origin B:

```
Domain: mediapackage.us-west-2.amazonaws.com
Path: None
```

CloudFront cache behavior:

```
1. Path: /out/v1/abc123/* forward to Origin A
2. Path: /out/v1/def456/* forward to Origin A
3. Path: * forward to Origin B
```

For the other distribution settings, set specific values based on
other technical requirements or the needs of your business. For a list
of all the options for distributions and information about setting them,
see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

When you finish choosing the other distribution settings, choose
**Create distribution**. 4. Choose the distribution that you just created, then choose
**Behaviors**. 5. Select the default cache behavior, then choose
**Edit**. Specify the correct cache behavior
settings for the channel that you chose for the origin. Later, you’ll
add one or more additional origins and edit cache behavior settings for
them. 6. Go to the [CloudFront distributions
page](https://console.aws.amazon.com/cloudfront/v4/home#/distributions "https://console.aws.amazon.com/cloudfront/v4/home#/distributions"). 7. Wait until the value of the **Last modified** column
for your distribution has changed from **Deploying** to
a date and time, indicating that CloudFront has created your
distribution.

Repeat the steps here to add each of your MediaPackage channel endpoints to your
distribution, keeping in mind the need to create a "dummy"
origin.

###### To

add other endpoints as origins

1. On the CloudFront console, choose the distribution that you created for your
   channel.
2. Choose **Origins**, then choose **Create
   origin**.
3. For **Origin domain**, in the dropdown list, choose a
   MediaPackage endpoint for your channel.
4. For the other settings, set the values based on other technical
   requirements or the needs of your business. For more information, see
   [Origin settings](DownloadDistValuesOrigin.md "DownloadDistValuesOrigin.md").
5. Choose **Create origin**.

For each endpoint, you must configure cache behaviors to add path patterns
that route requests correctly. The path patterns that you specify depend on the
video format that you’re serving. The following procedure includes the path
pattern information to use for Apple HLS, CMAF, DASH, and Microsoft Smooth
Streaming formats.

You typically set up two cache behaviors for each endpoint:

- The parent manifest, which is the index to your files.
- The segments, which are the files of the video content.

###### To create a cache behavior for an endpoint

1. On the CloudFront console, choose the distribution that you created for your
   channel.
2. Choose **Behaviors**, then choose **Create
   behavior**.
3. For **Path pattern**, use a specific MediaPackage
   `OriginEndpoint` GUID as a path prefix.

**Path patterns**

For an HLS endpoint like
`https://3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com/out/v1/abc123/index.m3u8`,
create the following two cache behaviors:

    * For parent and child manifests, use
     `/out/v1/abc123/*.m3u8`.
    * For the content segments, use
     `/out/v1/abc123/*.ts`.

For a CMAF endpoint like
`https://3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com/out/v1/abc123/index.m3u8`,
create the following two cache behaviors:

    * For parent and child manifests, use
     `/out/v1/abc123/*.m3u8`.
    * For the content segments, use
     `/out/v1/abc123/*.mp4`.

For a DASH endpoint like
`https://3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com/out/v1/abc123/index.mpd`,
create the following two cache behaviors:

    * For the parent manifest, use
     `/out/v1/abc123/*.mpd`.
    * For the content segments, use
     `/out/v1/abc123/*.mp4`.

For a Microsoft Smooth Streaming endpoint like
`https://3ae97e9482b0d011.mediapackage.us-west-2.amazonaws.com/out/v1/abc123/index.ism`,
only a manifest is served, so you create only one cache
behavior: `out/v1/abc123/index.ism/*`. 4. For each cache behavior, specify values for the following
settings:

**Viewer protocol policy**

Choose **Redirect HTTP to HTTPS**.

**Cache policy and origin request policy**

For **Cache policy**, choose
**Create policy**. For your new cache
policy, specify the following settings:

**Minimum TTL**

Set to 5 seconds or less, to help prevent
serving stale content.

**Query strings**

For **Query strings** (in
**Cache key settings**), choose
**Include specified query
strings**. For
**Allow**, add the following
values by typing them and then choosing
**Add item**:

    * Add `m` as a query string
     parameter that you want CloudFront to use as the basis
     for caching. The MediaPackage response always includes
     the tag `?m=###` to capture the
     modified time of the endpoint. If content is
     already cached with a different value for this
     tag, CloudFront requests a new manifest instead of
     serving the cached version.
    * If you’re using the time-shifted viewing
     functionality in MediaPackage, specify `start`
     and `end` as additional query string
     parameters on the cache behavior for manifest
     requests (`*.m3u8`, `*.mpd`,
     and `index.ism/*`). This way, content
     is served that’s specific to the requested time
     period in the manifest request. For more
     information about time-shifted viewing and
     formatting content start and end request
     parameters, see [Time-shifted viewing](../../../mediapackage/latest/ug/time-shifted.md "../../../mediapackage/latest/ug/time-shifted.md")
     in the *AWS Elemental MediaPackage User Guide*.
    * If you’re using the manifest filtering
     feature in MediaPackage, specify
     `aws.manifestfilter` as an additional
     query string parameter for the cache policy that
     you use with the cache behavior for manifest
     requests (`*.m3u8`, `*.mpd`,
     and `index.ism/*`). This configures
     your distribution to forward the
     `aws.manifestfilter` query string to
     your MediaPackage origin, which is required for the
     manifest filtering feature to work. For more
     information, see [Manifest filtering](../../../mediapackage/latest/ug/manifest-filtering.md "../../../mediapackage/latest/ug/manifest-filtering.md") in the *AWS Elemental MediaPackage User Guide*.
    * If you're using low-latency HLS (LL-HLS),
     specify `_HLS_msn` and
     `_HLS_part` as additional query string
     parameters for the cache policy that you use with
     the cache behavior for manifest requests
     (`*.m3u8`). This configures your
     distribution to forward the `_HLS_msn`
     and `_HLS_part` query strings to your
     MediaPackage origin, which is required for the
     LL-HLS blocking playlist request feature to
     work.

5. Choose **Create**.
6. After you create the cache policy, go back to the cache behavior
   creation workflow. Refresh the list of cache policies, and choose the
   policy that you just created.
7. Choose **Create behavior**.
8. If your endpoint is not a Microsoft Smooth Streaming endpoint, repeat
   these steps to create a second cache behavior.

We recommend enabling header-based MediaPackage CDN Authorization between MediaPackage
endpoints and the CloudFront distribution. For more information, see [Enable CDN authorization in MediaPackage](../../../mediapackage/latest/ug/cdn-auth-setup.md#cdn-aut-setup-endpoint "../../../mediapackage/latest/ug/cdn-auth-setup.md#cdn-aut-setup-endpoint") in the
_AWS Elemental MediaPackage User Guide_.

After you create the distribution, add the origins, create the cache
behaviors, and enable header-based CDN authorization, you can serve the live
stream channel using CloudFront. CloudFront routes requests from viewers to the correct
MediaPackage endpoints based on the settings that you configured for the cache
behaviors.

For links in your application (for example, a media player), specify the URL
for the media file in the standard format for CloudFront URLs. For more information,
see [Customize the URL format for files in CloudFront](LinkFormat.md "LinkFormat.md").

## Serve video-on-demand content with

AWS Elemental MediaPackage

If you originate your video-on-demand (VOD) content from an AWS Elemental MediaPackage origin, you can create a CloudFront distribution and configure optimized cache behaviors to serve the VOD content to viewers. The following
process assumes that you have already [created
a packaging group](../../../mediapackage/latest/ug/pkg-group-create.md "../../../mediapackage/latest/ug/pkg-group-create.md") with a [packaging configuration](../../../mediapackage/latest/ug/pkg-cfig-create.md "../../../mediapackage/latest/ug/pkg-cfig-create.md") and [ingested an asset](../../../mediapackage/latest/ug/asset-create.md "../../../mediapackage/latest/ug/asset-create.md") with MediaPackage.

To create a CloudFront distribution for MediaPackage manually, follow these steps:

###### Steps

Complete the following procedure to set up a CloudFront distribution for the packaging group that you created with MediaPackage.

###### To

create a distribution for your VOD content

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose **Create distribution**.
3. Choose the settings for the distribution, including the
   following:

**Origin domain**

The origin for your MediaPackage packaging group. Type the origin URL value into the text field. The origin must be an HTTPS URL.

For example, for an HLS endpoint like
`https://3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/abc123/def456/ghi789/index.m3u8`,
the origin domain is
`3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com`.

For more information, see [Origin domain](DownloadDistValuesOrigin.md#DownloadDistValuesDomainName "DownloadDistValuesOrigin.md#DownloadDistValuesDomainName").

**Origin path**

The path from where the content is
served.

For more information about how an origin path works, see
[Origin path](DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath "DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath").

###### Important

The wildcard path `*` is required to route somewhere in
the CloudFront distribution. To prevent requests not matching an explicit
path from routing to the real origin, create a "dummy"
origin for that wildcard path.

###### Example: Creating a "dummy" origin

In the following example, the packaging configurations `def456` and
`321xyz` route to the "real" origin, but
requests for any other video content route to
`mediapackage-vod.us-west-2.amazonaws.com` without the
proper subdomain, which results in an HTTP `404`
error.

MediaPackage content URLs for a single asset for a packaging group with two packaging configurations:

```
https://3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/abc123/def456/ghi789/index.m3u8
https://3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/abc123/321xyz/654uvw/index.m3u8
```

CloudFront Origin A:

```
Domain: 3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com
Path: None
```

CloudFront Origin B:

```
Domain: mediapackage-vod.us-west-2.amazonaws.com
Path: None
```

CloudFront cache behavior:

```
1. Path: /out/v1/*/def456/* forward to Origin A
2. Path: /out/v1/*/321xyz/* forward to Origin A
3. Path: * forward to Origin B
```

For the other distribution settings, set specific values based on
other technical requirements or the needs of your business. For a list
of all the options for distributions and information about setting them,
see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

When you finish choosing the other distribution settings, choose
**Create distribution**. 4. Choose the distribution that you just created, then choose
**Behaviors**. 5. Select the default cache behavior, then choose
**Edit**. Specify the correct cache behavior
settings for the packaging configuration that you chose for the origin. Later, you'll
add one or more additional origins and edit cache behavior settings for
them. 6. Go to the [CloudFront distributions
page](https://console.aws.amazon.com/cloudfront/v4/home#/distributions "https://console.aws.amazon.com/cloudfront/v4/home#/distributions"). 7. Wait until the value of the **Last modified** column
for your distribution has changed from **Deploying** to
a date and time, indicating that CloudFront has created your
distribution.

Repeat the steps here to add each of your MediaPackage packaging groups to your
distribution, keeping in mind the need to create a "dummy"
origin.

###### To

add other packaging groups as origins

1. On the CloudFront console, choose the distribution that you created for your
   channel.
2. Choose **Origins**, then choose **Create
   origin**.
3. For **Origin domain**, type in the URL for the MediaPackage packaging group.
4. For the other settings, set the values based on other technical
   requirements or the needs of your business. For more information, see
   [Origin settings](DownloadDistValuesOrigin.md "DownloadDistValuesOrigin.md").
5. Choose **Create origin**.

For each packaging configuration, you must configure cache behaviors to add path patterns
that route requests correctly. The path patterns that you specify depend on the
video format that you’re serving. The following procedure includes the path
pattern information to use for Apple HLS, CMAF, DASH, and Microsoft Smooth
Streaming formats.

You typically set up multiple cache behaviors for each packaging configuration:

- The parent manifest, which is the index to your files.
- The segments, which are the files of the video content. A format might use more than one extension for content, depending on your configuration. A cache behavior is needed for each extension.

###### To create a cache behavior for a packaging configuration

1. On the CloudFront console, choose the distribution that you created for your
   channel.
2. Choose **Behaviors**, then choose **Create
   behavior**.
3. For **Path pattern**, use a specific MediaPackage
   VOD packaging configuration GUID as a path prefix. This is the second GUID in a MediaPackage VOD path.

**Path patterns**

For HLS content like
`https://3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/abc123/def456/ghi789/index.m3u8`,
create the following cache behaviors:

    * For parent and child manifests, use
     `/out/v1/*/def456/*.m3u8`.
    * For the content segments, use
     `/out/v1/*/def456/*.ts` and repeat for all needed segment extensions.

For CMAF content like
`https://3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/abc123/def456/ghi789/index.m3u8`,
create the following cache behaviors:

    * For parent and child manifests, use
     `/out/v1/*/def456/*.m3u8`.
    * For the content segments, use
     `/out/v1/*/def456/*.mp4` and repeat for all needed segment extensions.

For DASH content like
`https://3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/abc123/def456/ghi789/index.mpd`,
create the following cache behaviors:

    * For the parent manifest, use
     `/out/v1/*/def456/*.mpd`.
    * For the content segments, use
     `/out/v1/*/def456/*.mp4`.

For a Microsoft Smooth Streaming endpoint like
`https://3ae97e9482b0d011.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/abc123/def456/ghi789/index.ism/Manifest`,
only a manifest is served, so you create only one cache
behavior: `out/v1/*/def456/*/index.ism/*`. 4. For each cache behavior, specify values for the following
settings:

**Viewer protocol policy**

Choose **Redirect HTTP to HTTPS**.

**Cache policy and origin request policy**

For **Cache policy**, choose
**Create policy**. For your new cache
policy, specify the following settings:

**Minimum TTL**

Set to 5 seconds or less, to help prevent
serving stale content.

**Query strings**

For **Query strings** (in
**Cache key settings**), choose
**Include specified query
strings**. For
**Allow**, add the following
values by typing them and then choosing
**Add item**:

    * If you’re using the manifest filtering
     feature in MediaPackage, specify
     `aws.manifestfilter` as an additional
     query string parameter for the cache policy that
     you use with the cache behavior for manifest
     requests (`*.m3u8`, `*.mpd`,
     and `index.ism/*`). This configures
     your distribution to forward the
     `aws.manifestfilter` query string to
     your MediaPackage origin, which is required for the
     manifest filtering feature to work. For more
     information, see [Manifest filtering](../../../mediapackage/latest/ug/manifest-filtering.md "../../../mediapackage/latest/ug/manifest-filtering.md") in the *AWS Elemental MediaPackage User Guide*.

5. Choose **Create**.
6. After you create the cache policy, go back to the cache behavior
   creation workflow. Refresh the list of cache policies, and choose the
   policy that you just created.
7. Choose **Create behavior**.
8. If your endpoint is not a Microsoft Smooth Streaming endpoint, repeat
   these steps to create a second cache behavior.

We recommend enabling header-based MediaPackage CDN Authorization between MediaPackage
VOD content and the CloudFront distribution. For more information, see [Enable CDN authorization in MediaPackage](../../../mediapackage/latest/ug/cdn-auth-setup.md#cdn-aut-setup-endpoint "../../../mediapackage/latest/ug/cdn-auth-setup.md#cdn-aut-setup-endpoint") in the
_AWS Elemental MediaPackage User Guide_.

After you create the distribution, add the origins, create the cache
behaviors, and enable header-based CDN authorization, you can serve the VOD content using CloudFront. CloudFront routes requests from viewers to the correct
MediaPackage VOD content based on the settings that you configured for the cache
behaviors.

For links in your application (for example, a media player), specify the URL
for the media file in the standard format for CloudFront URLs. For more information,
see [Customize the URL format for files in CloudFront](LinkFormat.md "LinkFormat.md").
