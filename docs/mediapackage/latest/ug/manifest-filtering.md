# Manifest filtering

With manifest filtering, AWS Elemental MediaPackage dynamically produces client manifests based on parameters that you specify in a query appended to your playback request. This enables you to do things such as restrict viewer access to premium 4K HEVC content, or target specific device types and audio sample rate ranges, all from a single endpoint. Previously, you would have to configure multiple endpoints to accomplish this behavior. MediaPackage now provides a cost-effective way to dynamically produce different client manifests on the same endpoint.

## Working with manifest filters

When you use a manifest filter, the resulting manifest includes only the audio and
video streams that match the characteristics that you specify in your query. If no
manifest filter is used, then all of the ingested streams are present in the endpoint
output stream. The exception to this is if you have set stream filters for the endpoint,
such as minimum video bitrate. In that case, the manifest filter is applied after the
stream filter, which could skew your output, and is not recommended.

Manifest filtering can be used on all endpoint types supported by MediaPackage:

- Apple HLS
- DASH-ISO
- Microsoft Smooth Streaming
- CMAF

To use manifest filtering, append `aws.manifestfilter` query parameters to
your playback request to MediaPackage. MediaPackage evaluates the query, and serves a
client manifest based on those query parameters. Manifest queries are _not_ case-sensitive and can be up to 1024 characters long. If
the query is malformed, or if it there aren't streams that match the query parameters,
MediaPackage returns an incomplete or empty manifest. For query syntax, see the following
section.

###### Note

If you are using Apple HLS or CMAF endpoints, special conditions apply. For information
about these conditions, see [Special conditions for HLS and CMAF manifests](#special-conditions-HLS-CMAF-manifests "#special-conditions-HLS-CMAF-manifests").

###### Query syntax

The base query parameter is `aws.manifestfilter`, which is followed by
optional parameter name and value pairs. To construct the query, append
`?aws.manifestfilter=` to the end of the MediaPackage endpoint URL,
followed by parameter names and values. For a list of all of the available
parameters, see [Manifest filter query
parameters](#manifest-filter-query-parameters "#manifest-filter-query-parameters").

An Apple HLS filter query might look like this:

`https://example-mediapackage-endpoint.mediapackage.us-west-2.amazonaws.com/out/v1/examplemediapackage/index.m3u8`?aws.manifestfilter=audio_sample_rate:0-44100;video_bitrate:0-2147483647;video_codec:h265;audio_language:fr,en-US,de``

The query syntax is listed in the following table.

| Query string component | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `?`                    | A restricted character that marks the beginning of a query.                                                                                                                                                                                                                                                                                                                                                                                          |
| `aws.manifestfilter=`  | The base query, which is followed by parameters constructed of name<br>and value pairs. For a list of all of the available parameters, see<br>[Manifest filter query<br>parameters](#manifest-filter-query-parameters "#manifest-filter-query-parameters").                                                                                                                                                                                          |
| `:`                    | Used to associate the parameter name with a value. For example,<br>``parameter_name`:`value``.                                                                                                                                                                                                                                                                                                                                                       |
| `;`                    | Separates parameters in a query that contains multiple parameters.<br>For example,<br>``parameter1_name:value`;`parameter2_name:minValue-maxValue``.                                                                                                                                                                                                                                                                                                 |
| `,`                    | Separates a list of values. For example,<br>`parameter_name:`value1`,`value2`,`value3``.<br>Comma-separated values in a list imply an `OR`<br>relationship.                                                                                                                                                                                                                                                                                          |
| `-`                    | Used to define a parameter's minimum<br>• maximum value range. For example,<br>`audio_sample_rate:0-44100`. When a numerical value is<br>used in a range, it is included in the range definition. This means that<br>streams must be greater than or equal to the minimum value, and less<br>than or equal to the maximum value. With ranges, the minimum and maximum<br>values are mandatory. The supported range values are `0` -<br>`2147483647`. |

###### Note

If you use Amazon CloudFront as your CDN, you might need to set additional configurations.
For more information, see [Configure cache behavior for all endpoints.](../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#live-streaming-with-mediapackage-create-cache-behavior "../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#live-streaming-with-mediapackage-create-cache-behavior").

## Manifest filter query

parameters

MediaPackage supports the following query parameters.

| Category | Name                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                     |
| -------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Audio    | `audio_bitrate`       | • The audio bitrate in bits per second.<br>• **Accepted values**:<br>Two integers aggregated with a dash that define an inclusive range. The<br>supported range values are `0` -<br>`2147483647`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `stream.mpd?aws.manifestfilter=audio_bitrate:0-2147483647`  |
| Audio    | `audio_channels`      | • The number of audio channels.<br>• **Accepted values**:<br>Two integers aggregated with a dash that define an inclusive range. The<br>supported range values are `1` -<br>`32767`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `stream.mpd?aws.manifestfilter=audio_channels:1-8`          |
| Audio    | `audio_codec`         | • The audio codec type.<br>• **Accepted values**:<br>`AACL`, `AACH`, `AC-3`, `EC-3`. You must include the `-` for `AC-3` and `EC-3`.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `stream.mpd?aws.manifestfilter=audio_codec:AACL,AC-3`       |
| Audio    | `audio_language`      | • Audio languages or functional codes derived from encoder passthrough.<br>• **Accepted values**:<br>Arbitrary strings, such as two or four character [ISO-639-1](https://www.andiamo.co.uk/resources/iso-language-codes/ "https://www.andiamo.co.uk/resources/iso-language-codes/") language codes. You must use the same<br>language strings that are set for your encoder.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                 | `stream.mpd?aws.manifestfilter=audio_language:fr,en-US,de`  |
| Audio    | `audio_sample_rate`   | • The audio sample rate in Hz.<br>• **Accepted values**: Two<br>integers aggregated with a dash that define an inclusive range. The<br>supported range values are `0` -<br>`2147483647`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `stream.mpd?aws.manifestfilter=audio_sample_rate:0-44100`   |
| Subtitle | `subtitle_language`   | • The subtitle language or functional codes derived from<br>encoder passthrough.<br>• **Accepted values**:<br>Arbitrary strings, such as two or four character [ISO-639-1](https://www.andiamo.co.uk/resources/iso-language-codes/ "https://www.andiamo.co.uk/resources/iso-language-codes/") language codes. You must use the same<br>language strings that are set for your encoder.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                        | `stream.mpd?aws.manifestfilter=subtitle_language:en-US, hi` |
| Video    | `trickplay_height`    | • The height of the trick-play image in pixels. This applies<br>to both I-frame only and image-based trick-play.<br>NoteIf you're using this parameter with I-frame only<br>trick-play, `trickplay_height` and<br>`video_height` should have similar<br>values. If the values are not the same, I-frame only<br>tracks might be removed from a manifest.<br>• The `trickplay_height` filter is applied before tiling for DASH on VOD.<br>• **Accepted values**:<br>Two integers aggregated with a dash that define an inclusive range. The<br>supported range values are `1` -<br>`2147483647`.                                                                                                                            | `stream.mpd?aws.manifestfilter=trickplay_height:200-1200`   |
| Video    | `trickplay_type`      | • The trickplay track type. You can filter on iframe or image trickplay tracks or use the<br>value `none` to filter out all trickplay tracks (both iframe and image).<br>• **Accepted values**:<br>`iframe`, `image`, `none`.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `stream.mpd?aws.manifestfilter=trickplay_type:iframe`       |
| Video    | `video_bitrate`       | • The video bitrate in bits per second.<br>NoteIf you're using this parameter, we recommend that you<br>use only the `video_bitrate` filter parameter<br>to set the video bitrate. Don't also set the minimum and<br>maximum video bitrate via the MediaPackage console or<br>AWS CLI. The `video_bitrate` filter applies to<br>the video bitrate settings created at the endpoint. If<br>you use the parameter and set the bitrate in the console<br>or AWS CLI, your output might be skewed.<br>• **Accepted values**: Two<br>integers aggregated with a dash that define an inclusive range. The<br>supported range values are `0` -<br>`2147483647`.<br>• NoteYou can't use this parameter with trick-play<br>streams. | `stream.mpd?aws.manifestfilter=video_bitrate:0-2147483647`  |
| Video    | `video_codec`         | • The video codec type.<br>• **Accepted values**:<br>`H264`, `H265`.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `stream.mpd?aws.manifestfilter=video_codec:h264`            |
| Video    | `video_dynamic_range` | • The video dynamic range.<br>• **Accepted values**:<br>`hdr10`, `hlg`, `sdr`.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `stream.mpd?aws.manifestfilter=video_dynamic_range:hdr10`   |
| Video    | `video_framerate`     | • The video frame rate range in the NTSC format.<br>• **Accepted values**:<br>Two floating-point numbers aggregated with a dash that define an inclusive range. Each number can have up to three optional fractional values. For example, `29.97` or `29.764`. The<br>supported range values are `1` -<br>`999.999`.                                                                                                                                                                                                                                                                                                                                                                                                       | `stream.mpd?aws.manifestfilter=video_framerate:23.976-30`   |
| Video    | `video_height`        | • The height of the video in pixels.<br>NoteIf you're using this parameter with I-frame only trick-play, `trickplay_height` and `video_height` should have similar values.<br>If the values are not the same, I-frame only tracks might be removed from a manifest.<br>• **Accepted values**:<br>Two integers aggregated with a dash that define an inclusive range. The<br>supported range values are `1` -<br>`32767`.                                                                                                                                                                                                                                                                                                   | `stream.mpd?aws.manifestfilter=video_height:720-1080`       |

## Manifest filtering examples

These are manifest filtering examples.

###### Example 1: Target a player that supports AVC and a 44.1k audio sample rate

The viewer is playing content on a device that can only support AVC and a 44.1k
audio sample rate. You set the `video_codec` and
`audio_sample_rate` to filter out streams that don't fit these
requirements.

`?aws.manifestfilter=audio_sample_rate:0-44100;video_codec:h264`

###### Example 2: Restrict 4k HEVC content

Your 4K HEVC stream is 15 Mbps, and all your other streams are less than 9 Mbps. To
exclude the 4K stream from the stream set, you set a threshold of 9,000,000 bits per second to
filter out the higher bitrate.

`?aws.manifestfilter=video_bitrate:0-9000000`

###### Example 3: Include video between 23.976 and 30 frames per second

To only include video within a certain frame rate range, use `video_framerate`. This parameter accepts floating-point numbers with up to three optional decimal values.

`?aws.manifestfilter=video_framerate:23.976-30`

## Special conditions for HLS and CMAF manifests

If you are using HLS or CMAF manifests, these special conditions apply.

- For HLS manifests, we strongly recommend that you use audio rendition
  groups to avoid removing the video streams that are multiplexed with the audio
  streams that are filtered out. For more information about rendition groups, see
  [Rendition groups reference in AWS Elemental MediaPackage](rendition-groups.md "rendition-groups.md").
- In HLS and CMAF manifests, the audio sample rate is not signaled, so it's
  not easy to visually check the original or filtered manifests for this setting.
  To verify the audio sample rate, check the audio sample rate at the encoder
  level and output level.
- In HLS and CMAF manifests, the `BANDWIDTH` attribute for a
  variant associates the bandwidth of the audio track with the video track,
  whether it is multiplexed with the video track, or if it is an audio rendition
  track referenced by the video track. Therefore, you can't visually inspect the
  original and filtered manifests to confirm the `video_bitrate` filter
  has worked. To verify the filter, check the video bitrate at the encoder level
  and output level.
- For HLS and CMAF manifests, request parameters appended to bitrate playlists
  or segments result in an HTTP 400 error.

## Error conditions

Some playback devices will return errors if the manifest or segments include invalid
or unknown query parameters. The following are query parameters that MediaPackage can
process:

- `m`
- `start`
- `end`
- `aws.manifestfilter`
- `aws.drmsettings`

If you have query parameters other than those listed, use a CDN such as Amazon CloudFront to
remove the unnecessary parameters. For more information, see [Cache
content based on query string parameters](../../../AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.md "../../../AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.md") in the _Amazon CloudFront Developer Guide_.

The following table contains additional common error conditions.

| Error condition                                                                                                                         | Example                                                                                      | HTTP status code |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------- | --- |
| A list parameter is not found and is not part of a constrained<br>list                                                                  | `?aws.manifestfilter=audio_language:dahlia`                                                  | 200              |
| Only subtitle streams are present in the stream                                                                                         | `?aws.manifestfilter=audio_sample_rate:0-1;video_bitrate=0-1`                                | 200              |
| Duplicate filter parameter                                                                                                              | `?aws.manifestfilter=audio_sample_rate:0-48000;aws.manifestfilter=audio_sample_rate:0-48000` | 400              |
| Invalid parameter                                                                                                                       | `?aws.manifestfilter=donut_type:rhododendron`                                                | 400              |
| Invalid range parameter                                                                                                                 | `?aws.manifestfilter=audio_sample_rate:300-0`                                                | 400              |
| Invalid range value (more than `INT_MAX`)                                                                                               | `?aws.manifestfilter=audio_sample_rate:0-2147483648`                                         | 400              |
| Malformed query string                                                                                                                  | `?aws.manifestfilter=audio_sample_rate:is:0-44100`                                           | 400              |
| Parameter string is greater than 1024 characters                                                                                        | `?aws.manifestfilter=audio_language:abcdef....`                                              | 400              |
| Query parameters on an HLS or CMAF bitrate manifest                                                                                     | `index_1.m3u8?aws.manifestfilter=video_codec:h264`                                           | 400              |
| Query parameters on a segment request                                                                                                   | `...\_1.[ts                                                                                  | mp4              | vtt..]?aws.manifestfilter=video_codec:h264` | 400 |
| Repeated query parameter                                                                                                                | `?aws.manifestfilter=audio_sample_rate:0-48000;aws.manifestfilter=video_bitrate:0-1`         | 400              |
| Application of the filter results in an empty manifest (content has<br>no streams that meet the conditions defined in the query string) | `?aws.manifestfilter=audio_sample_rate:0-1;video_bitrate=0-1`                                | 400              |
