# Time-shifted query parameters in AWS Elemental MediaPackage

To use time-shifted viewing query parameters, append `aws.manifestsettings`
to your playback request to MediaPackage. MediaPackage evaluates the query, and serves a client manifest
based on those query parameters.

The following sections describe how to configure time-shift viewing query
parameters.

## Query parameter formatting

Use the following guidelines when constructing query parameters:

- Queries are not case sensitive.
- Queries can be up to 1,024 characters.
- Reserved characters in the queries must be URL encoded as indicated in the
  [URI: General
  Syntax](https://datatracker.ietf.org/doc/html/rfc3986 "https://datatracker.ietf.org/doc/html/rfc3986") standard.

###### Important

At a minimum, if your query includes multiple parameters, the following
characters in the query must be URL encoded. If they're not, MediaPackage processes
just the first query parameter in the string.

| Character     | Encoded value |
| ------------- | ------------- |
| : (colon)     | %3A           |
| ; (semicolon) | %3B           |
| , (comma)     | %2C           |
| + (plus)      | %2B           |

If the query is malformed, MediaPackage returns an incomplete or empty manifest. For query
syntax, see the following section.

## Query syntax

The base query parameter for time-shifted viewing is
`aws.manifestsettings`, which is followed by optional parameter name and
value pairs. To construct the query, append `?aws.manifestsettings=` to the
end of the MediaPackage endpoint URL, followed by parameter names and values. For a list of all
of the available parameters, see [Query parameters](#msettings-parameters "#msettings-parameters").

An Apple HLS filter query might look like this:

`https://example-mediapackage-endpoint.mediapackage.us-west-2.amazonaws.com/out/v1/examplemediapackage/index.m3u8`?aws.manifestsettings=``

The query syntax is listed in the following table.

###### Note

If you use Amazon CloudFront as your CDN, you might need to set additional configurations.
For more information, see [Configure cache behavior for all endpoints](../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#live-streaming-with-mediapackage-create-cache-behavior "../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#live-streaming-with-mediapackage-create-cache-behavior").

| Query string component  | Description                                                                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `?`                     | A restricted character that marks the beginning of a<br>query.                                                                                                                                                                               |
| `aws.manifestsettings=` | The base query, which is followed by parameters constructed of<br>name and value pairs. For a list of all of the available parameters,<br>see [Query parameters](#msettings-parameters "#msettings-parameters").                             |
| `:`                     | Used to associate the parameter name with a value. For example,<br>``parameter_name`:`value``.                                                                                                                                               |
| `;`                     | Separates parameters in a query that contains multiple<br>parameters. For example,<br>``parameter1_name:value`;`parameter2_name:minValue-maxValue``.<br>When used in a list of parameters for the same query, implies an<br>`AND` operation. |

###### Date and time format requirements

In all cases, the date and time must be notated in one of the following formats:

- ISO 8601 dates, such as 2017-08-18T21:18:54%2B08:00, where **%2B08:00** is the timezone UTC+08:00. The plus (+) must
  be URL-encoded.
- POSIX (or Epoch) time, such as 1503091134

###### DASH parameter rules

Start and end parameters in the URL request for DASH content can use standard
parameter notation, or can be included as path elements in the URL.

- Query parameter notation – start and end parameters are included at the
  end of the request URL

```
https://cf98fa7b2ee4450e.mediapackagev2.us-east-1.amazonaws.com/out/v1/997cbb27697d4863bb65488133bff26f/sports.mpd?`start=1513717228&end=1513720828`
```

- Path elements – start and end parameters are included in the path of
  the request URL

```
https://cf98fa7b2ee4450e.mediapackagev2.us-east-1.amazonaws.com/out/v1/997cbb27697d4863bb65488133bff26f/`start`/`2017-12-19T13:00:28-08:00`/`end`/`2017-12-19T14:00:28-08:00`/sports.mpd
```

###### TS and CMAF parameter rules

Start and end parameters in the URL request for TS content can use standard parameter
notation.

- Query parameter notation – start and end parameters are included at the
  end of the request URL

###### Example TS

```
https://cf98fa7b2ee4450e.mediapackagev2.us-east-1.amazonaws.com/out/v1/064134724fd74667ba294657a674ae72/comedy.m3u8?`start=2017-12-19T13:00:28-08:00&end=2017-12-19T14:00:28-08:00`
```

###### Example CMAF

```
https://cf98fa7b2ee4450e.mediapackagev2.us-east-1.amazonaws.com/out/v1/064134724fd74667ba294657a674ae72/manifest_id/news.m3u8?`start=2018-04-04T01:14:00-08:00&end=2018-04-04T02:15:00-08:00`
```

## Query parameters

Playback devices can append the following time-shifted viewing query parameters to
their requests to MediaPackage. Responses to requests with one or more of these parameters will
include manifests that adhere to the specified time-shifted query parameters.

If you want all manifests served from this origin endpoint to be time shifted, enable the
settings on the endpoint, as described in [Creating an origin endpoint in AWS Elemental MediaPackage](endpoints-create.md "endpoints-create.md").

###### Note

The `manifest_window_seconds` option is available only as a query
parameter on a session initialization URL, and not as a setting on the endpoint.
This is because the `manifest_window_seconds` query parameter modifies
the standard length of the manifest that's configured through the **Manifest
window** setting on the endpoint. For more information about manifest
window relationships, see [Window duration](window-seconds.md "window-seconds.md").

| Name                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `clip_start_time`         | • With a time delay manifest, defines the earliest content that should be<br>available in this manifest.<br>• **Accepted values**: Epoch or ISO 8601<br>timestamp that represents the earliest date and time that<br>live content is available in the manifest.<br>+ `clip_start_time` can't be combined<br>with `start` or `end`<br>parameters.<br>+ `clip_start_time` query parameters<br>can't be combined with \*_Clip start<br>time_<br>• settings on the origin<br>endpoint.                                                | `stream.mpd?aws.manifestsettings=subtitle_language:en-US,<br>hi;clip_start_time:1720246778` |
| `manifest_window_seconds` | • Used to request a manifest that's shorter than manifest<br>window for this request.<br>• **Accepted values**: Integer<br>that represents the desired manifest window in seconds.<br>+ At minimum, the value provided must be greater<br>than or equal to double the length of the segment<br>target duration. This is to ensure that the window<br>includes at least two segments.<br>+ At maximum, the value provided must be less than the configured<br>manifest window in the manifest settings for the<br>origin endpoint. | `stream.mpd?aws.manifestsettings=manifest_window_seconds:30`                                |
| `start`                   | • Used to denote the beginning of a time-shifted manifest.<br>For more information, see [Define manifest start and end times from<br>AWS Elemental MediaPackage](start-and-end-parameters-rules.md "start-and-end-parameters-rules.md").<br>• **Accepted values**: Epoch or<br>ISO 8601 timestamp that represents the start date and time<br>for content in the manifest.                                                                                                                                                         | `stream.mpd?aws.manifestsettings=start:1732285823`                                          |
| `end`                     | • Used to denote the end of a time-shifted manifest. For<br>more information, see [Define manifest start and end times from<br>AWS Elemental MediaPackage](start-and-end-parameters-rules.md "start-and-end-parameters-rules.md").<br>• **Accepted values**: Epoch or<br>ISO 8601 timestamp that represents the start date and time<br>for content in the manifest.                                                                                                                                                               | `stream.mpd?aws.manifestsettings=end:1732300175`                                            |
| `time_delay`              | • Used to redefine the live point for this request. For more<br>information, see [Define manifest start and end times from<br>AWS Elemental MediaPackage](start-and-end-parameters-rules.md "start-and-end-parameters-rules.md").                                                                                                                                                                                                                                                                                                 | `stream.mpd?aws.manifestsettings=time_delay:320`                                            |

## URL encoding query parameters

When you add query parameters to your HLS and LL-HLS playback requests, MediaPackage appends
the parameters in alphabetical order to the child manifest URLs. For instance, the
`end` parameter is listed before the `start` parameter.

To [create a signed API request](../../../IAM/latest/UserGuide/reference_sigv-create-signed-request.md#create-canonical-request "../../../IAM/latest/UserGuide/reference_sigv-create-signed-request.md#create-canonical-request") for AWS Signature Version 4 (SigV4) signing, your query
strings must be URL encoded. By default, MediaPackage doesn't encode query parameters. To be a
valid SigV4 signature, choose **URL-encode HLS child manifest query
parameters** on your HLS or LL-HLS origin endpoint, as described in [Manifest fields](endpoints-create.md#endpoints-manifest "endpoints-create.md#endpoints-manifest").

For more information about SigV4 and its requirements, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in _AWS Identity and Access Management User Guide_.

###### Example unencoded query strings

```
hls_video-1080.m3u8?aws.manifestsettings=time_delay:10&end=2025-02-03T17:09:49Z&start=2025-02-03T17:08:49Z
```

###### Example URL-encoded query strings

```
hls_video-1080.m3u8?aws.manifestsettings=time_delay%3A10&end=2025-02-03T17%3A09%3A49Z&start=2025-02-03T17%3A08%3A49Z
```
