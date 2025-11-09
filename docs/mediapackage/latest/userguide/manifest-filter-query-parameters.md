# Manifest filtering query parameters

in AWS Elemental MediaPackage

To use manifest filtering query parameters, append `aws.manifestfilter` to
your playback request to MediaPackage. MediaPackage evaluates the query, and serves a client manifest
based on those query parameters.

The following sections describe how to configure manifest filtering query
parameters.

###### Note

If you are using TS or CMAF origin endpoints, special conditions apply. For
information about these conditions, see [Special conditions for TS and
CMAF manifests in MediaPackage](special-conditions-TS-CMAF-manifests.md "special-conditions-TS-CMAF-manifests.md").

## Query parameter formatting

Use the following guidelines when constructing query parameters:

- Queries are not case sensitive.
- Queries can be up to 1,024 characters.
- Reserved characters in the queries must be URL encoded as indicated in the
  [URI: General Syntax](https://datatracker.ietf.org/doc/html/rfc3986 "https://datatracker.ietf.org/doc/html/rfc3986") standard.

###### Important

At a minimum, if your query includes multiple parameters, the
following characters in the query must be URL encoded. If they're not,
MediaPackage processes just the first query parameter in the string.

| Character     | Encoded value |
| ------------- | ------------- |
| : (colon)     | %3A           |
| ; (semicolon) | %3B           |
| , (comma)     | %2C           |
| + (plus)      | %2B           |

If the query is malformed, or if it there aren't streams that match the query
parameters, MediaPackage returns an incomplete or empty manifest. For query syntax, see the
following section.

## Query syntax

The base query parameter is `aws.manifestfilter`, which is followed by
optional parameter name and value pairs. To construct the query, append
`?aws.manifestfilter=` to the end of the MediaPackage endpoint URL, followed
by parameter names and values. For a list of all of the available parameters, see
[Manifest filtering query parameters
in AWS Elemental MediaPackage](manifest-filter-query-parameters.md "manifest-filter-query-parameters.md").

###### Example HLS filter query

The following example query includes filters for audio sample rate, video
bitrate, video codec, and audio language. Note that the reserved characters use
URL-encoded values.

`https://example-mediapackage-endpoint.mediapackage.us-west-2.amazonaws.com/out/v1/examplemediapackage/index.m3u8`?aws.manifestfilter=audio_sample_rate%3A0-44100%3Bvideo_bitrate%3A0-2147483647%3Bvideo_codec%3Ah265%3Baudio_language%3Afr%2Cen-US%2Cde``

The query syntax is described in the following table.

###### Note

If you use Amazon CloudFront as your CDN, you might need to set additional
configurations. For more information, see [Configure cache behavior for all endpoints](../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#live-streaming-with-mediapackage-create-cache-behavior "../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#live-streaming-with-mediapackage-create-cache-behavior").

| Query string component | Description                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `?`                    | A restricted character that marks the beginning of a<br>query.                                                                                                                                                                                                                                                                                                                                                                                          |
| `aws.manifestfilter=`  | The base query, which is followed by parameters constructed of<br>name and value pairs. For a list of all of the available parameters,<br>see [Manifest filtering query parameters<br>in AWS Elemental MediaPackage](manifest-filter-query-parameters.md "manifest-filter-query-parameters.md").                                                                                                                                                        |
| `:`                    | Used to associate the parameter name with a value. For example,<br>``parameter_name`:`value``.<br>When using multiple query parameters, this character must<br>be URL encoded (%3A).                                                                                                                                                                                                                                                                    |
| `;`                    | Separates parameters in a query that contains multiple<br>parameters. For example,<br>``parameter1_name:value`;`parameter2_name:minValue-maxValue``.<br>When used in a list of parameters for the same query, implies an<br>`AND` operation.When using multiple query<br>parameters, this character must be URL encoded<br>(%3B).                                                                                                                       |
| `,`                    | Separates a list of values. For example,<br>`parameter_name:`value1`,`value2`,`value3``.<br>Comma-separated values in a list imply an `OR`<br>relationship.When using multiple query parameters, this<br>character must be URL encoded (%2C).                                                                                                                                                                                                           |
| `-`                    | Used to define a parameter's minimum<br>• maximum value range. For<br>example, `audio_sample_rate:0-44100`. When a numerical<br>value is used in a range, it is included in the range definition.<br>This means that streams must be greater than or equal to the minimum<br>value, and less than or equal to the maximum value. With ranges, the<br>minimum and maximum values are mandatory. The supported range values<br>are `0`<br>• `2147483647`. |

## Query value formats

The following query parameters support expanded value formats:

- `audio_bitrate`
- `audio_channels`
- `audio_sample_rate`
- `trickplay_height`
- `video_bitrate`
- `video_framerate`
- `video_height`

For all of these parameters, you can format your values as single values or
ranges, one or more ranges, or a combination of both.

**Individual values and ranges**

Filter manifests by single values or ranges.

**Syntax**

- Individual single values:
  `aws.manifestfilter=`parameter`:`value``
- Individual range:
  `aws.manifestfilter=`parameter`:`min1-max1``

###### Example individual value

The following example filters for videos with a bitrate of 8000000
bps.

```
stream.mpd?aws.manifestfilter=video_bitrate:8000000
```

###### Note

When you filter for a single `video_framerate` value,
MediaPackage uses an approximate equals comparison with an epsilon
tolerance of 0.0005. MediaPackage uses this tolerance because the query
allows only up to three decimal places, and there could be a small
difference in accuracy between the stored framerates and the
specified framerate.

For example, if your filter is
`video_framerate:30.000`, MediaPackage matches framerates in the
range of 29.9995 to 30.0005.

**Multiple values and ranges**

Filter manifests by multiple single values or multiple ranges.

**Syntax**

- Multiple single values:
  `aws.manifestfilter=`parameter`:`value`,`value``
- Multiple ranges:
  `aws.manifestfilter=`parameter`:`min1-max1`,`min2-max2``

###### Example multiple ranges

The following example filters for videos that are either 240p-360p
OR 720p-1080p. It uses URL encoding for reserved characters.

```
stream.mpd?aws.manifestfilter=video_height%3A240-360%2C720-1080
```

**Combination**

Filter manifests by a combination of ranges and values.

**Syntax**

- Multiple ranges and single values:
  `aws.manifestfilter=`parameter`:`min1-max1`,`min2-max2`,`value1`,`value2``

###### Example multiple ranges and values

The following example filters for videos that are either
240p-360p, 720p-1080p, 1440p, OR 2160p. It uses URL encoding for
reserved characters.

```
stream.mpd?aws.manifestfilter=video_height%3A240-360%2C720-1080%2C1440%2C2160
```

## Query parameters

MediaPackage supports the following query parameters.

You can set one or more filters. For example, to restrict all manifests from this
endpoint to 0 to 44000 Hz audio sample rate, 0 to 2147483647 video bitrate, H265
video codec, and French and English languages, enter the following key and value
pairs on the origin endpoint:

**Filter key**
`audio_sample_rate` | **Filter value**:
`0-44100`

**Filter key**
`video_bitrate` | **Filter value**:
`0-2147483647`

**Filter key**
`video_codec` | **Filter value**: `H265`

**Filter key**
`audio_language` | **Filter value**:
`fr,en-US`

| Category | Name                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Example                                                     |
| -------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Audio    | `audio_bitrate`       | • The audio bitrate in bits per second.<br>• **Accepted values**: Two<br>integers aggregated with a dash that define an inclusive<br>range. The supported range values are `0` -<br>`2147483647`. Individual integers within<br>that range are also allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `stream.mpd?aws.manifestfilter=audio_bitrate:0-2147483647`  |
| Audio    | `audio_channels`      | • The number of audio channels.<br>• **Accepted values**: Two<br>integers aggregated with a dash that define an inclusive<br>range. The supported range values are `1` -<br>`32767`. Individual integers within that<br>range are also allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `stream.mpd?aws.manifestfilter=audio_channels:1-8`          |
| Audio    | `audio_codec`         | • The audio codec type.<br>• **Accepted values**:<br>`AACL`, `AACH`, `AC-3`, `EC-3`. You must include the `-` for `AC-3` and `EC-3`.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `stream.mpd?aws.manifestfilter=audio_codec:AACL,AC-3`       |
| Audio    | `audio_language`      | • Audio languages or functional codes derived from encoder passthrough.<br>• **Accepted values**:<br>Arbitrary strings, such as two or four character [ISO-639-1](https://www.andiamo.co.uk/resources/iso-language-codes/ "https://www.andiamo.co.uk/resources/iso-language-codes/") language codes. You must use the same<br>language strings that are set for your encoder.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                            | `stream.mpd?aws.manifestfilter=audio_language:fr,en-US,de`  |
| Audio    | `audio_sample_rate`   | • The audio sample rate in Hz.<br>• **Accepted values**: Two<br>integers aggregated with a dash that define an inclusive<br>range. The supported range values are `0` -<br>`2147483647`. Individual integers within<br>that range are also allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `stream.mpd?aws.manifestfilter=audio_sample_rate:0-44100`   |
| Subtitle | `subtitle_language`   | • The subtitle language or functional codes derived from<br>encoder passthrough.<br>• **Accepted values**:<br>Arbitrary strings, such as two or four character [ISO-639-1](https://www.andiamo.co.uk/resources/iso-language-codes/ "https://www.andiamo.co.uk/resources/iso-language-codes/") language codes. You must use the same<br>language strings that are set for your encoder.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                   | `stream.mpd?aws.manifestfilter=subtitle_language:en-US, hi` |
| Video    | `trickplay_height`    | • The height of the trick-play image in pixels. This applies<br>to both I-frame only and image-based trick-play.<br>NoteIf you're using this parameter with I-frame only<br>trick-play, `trickplay_height` and<br>`video_height` should have similar<br>values. If the values are not the same, I-frame only<br>tracks might be removed from a manifest.<br>• **Accepted values**: Two<br>integers aggregated with a dash that define an inclusive<br>range. The supported range values are `1` -<br>`2147483647`. Individual integers within<br>that range are also allowed.                                                                                                                                                                                                         | `stream.mpd?aws.manifestfilter=trickplay_height:200-1200`   |
| Video    | `trickplay_type`      | • The trickplay track type.<br>• **Accepted values**:<br>`iframe`, `image`, `none`.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `stream.mpd?aws.manifestfilter=trickplay_type:iframe`       |
| Video    | `video_bitrate`       | • The video bitrate in bits per second.<br>NoteIf you're using this parameter, we recommend that you<br>use only the `video_bitrate` filter parameter<br>to set the video bitrate. Don't also set the minimum and<br>maximum video bitrate via the MediaPackage console or<br>AWS CLI. The `video_bitrate` filter applies to<br>the video bitrate settings created at the endpoint. If<br>you use the parameter and set the bitrate in the console<br>or AWS CLI, your output might be skewed.<br>• **Accepted values**: Two<br>integers aggregated with a dash that define an inclusive<br>range. The supported range values are `0` -<br>`2147483647`. Individual integers within<br>that range are also allowed.<br>• NoteYou can't use this parameter with trick-play<br>streams. | `stream.mpd?aws.manifestfilter=video_bitrate:0-2147483647`  |
| Video    | `video_codec`         | • The video codec type.<br>• **Accepted values**:<br>`H264`, `H265`,<br>`AV1`.<br>The values are \*not<br>• case-sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `stream.mpd?aws.manifestfilter=video_codec:h264`            |
| Video    | `video_dynamic_range` | • The video dynamic range.<br>• **Accepted values**:<br>`dv`, `hdr10`, `hlg`,<br>`sdr`.<br>The values are \*not<br>• case-sensitive.<br>You can use the `dv` value to filter for Dolby<br>Vision streams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `stream.mpd?aws.manifestfilter=video_dynamic_range:hdr10`   |
| Video    | `video_framerate`     | • The video frame rate range in the NTSC format.<br>• **Accepted values**: Two<br>floating-point numbers aggregated with a dash that<br>define an inclusive range. Each number can have up to<br>three optional fractional values. For example,<br>`29.97` or `29.764`. The<br>supported range values are `1` -<br>`999.999`. Individual integers within<br>that range are also allowed.                                                                                                                                                                                                                                                                                                                                                                                              | `stream.mpd?aws.manifestfilter=video_framerate:23.976-30`   |
| Video    | `video_height`        | • The height of the video in pixels.<br>NoteIf you're using this parameter with I-frame only trick-play, `trickplay_height` and `video_height` should have similar values.<br>If the values are not the same, I-frame only tracks might be removed from a manifest.<br>• **Accepted values**: Two<br>integers aggregated with a dash that define an inclusive<br>range. The supported range values are `1` -<br>`32767`. Individual integers within that<br>range are also allowed.                                                                                                                                                                                                                                                                                                   | `stream.mpd?aws.manifestfilter=video_height:720-1080`       |
