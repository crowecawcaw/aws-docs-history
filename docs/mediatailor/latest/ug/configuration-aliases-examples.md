# Configuration alias with MediaTailor use

example

The following examples show how a complete MediaTailor configuration with configuration aliases, a session initialization request with aliases, and the processing flow for aliases.

###### Example Complete configuration with aliases

The following example shows a complete configuration that includes configuration
aliases and dynamic domain variables:

```
PUT /playbackConfiguration
{
    "Name": "aliasedConfig",
    "AdDecisionServerUrl": "https://abc.execute-api.us-west-2.amazonaws.com/ads?sid=[session.id]&ad_type=[player_params.ad_type]",
    "VideoContentSourceUrl": "https://[player_params.origin_domain].mediapackage.[player_params.region].amazonaws.com/out/v1/[player_params.endpoint_id]",

    "AdSegmentUrlPrefix": "https://[player_params.ad_cdn_domain]/ads/",
    "ContentSegmentUrlPrefix": "https://[player_params.content_cdn_domain]/content/",
    "TranscodeProfileName": "[player_params.transcode_profile]",
    "SlateAdUrl": "https://[player_params.slate_domain]/slate/[player_params.slate_type].mp4",
    "StartUrl": "https://[player_params.tracking_domain]/start?session=[session.id]",
    "EndUrl": "https://[player_params.tracking_domain]/end?session=[session.id]",

    "ConfigurationAliases": {
        "player_params.origin_domain": {
            "pdx": "abc",
            "iad": "xyz"
        },
        "player_params.region": {
            "pdx": "us-west-2",
            "iad": "us-east-1"
        },
        "player_params.endpoint_id": {
            "pdx": "abcd",
            "iad": "wxyz"
        },
        "player_params.ad_type": {
            "customized": "abc12345",
            "default": "defaultAdType"
        },
        "player_params.ad_cdn_domain": {
            "pdx": "ads-west.cdn.example.com",
            "iad": "ads-east.cdn.example.com"
        },
        "player_params.content_cdn_domain": {
            "pdx": "content-west.cdn.example.com",
            "iad": "content-east.cdn.example.com"
        },
        "player_params.transcode_profile": {
            "mobile": "mobile_optimized",
            "desktop": "high_quality",
            "tv": "4k_profile"
        },
        "player_params.slate_domain": {
            "pdx": "slate-west.example.com",
            "iad": "slate-east.example.com"
        },
        "player_params.slate_type": {
            "standard": "default_slate",
            "branded": "brand_slate"
        },
        "player_params.tracking_domain": {
            "pdx": "tracking-west.example.com",
            "iad": "tracking-east.example.com"
        }
    }
}
```

###### Example Session initialization with aliases

The following example shows a session initialization request that specifies the player variables and aliases:

```
POST master.m3u8
{
    "playerParams": {
        "origin_domain": "pdx",
        "region": "pdx",
        "endpoint_id": "pdx",
        "ad_type": "customized",
        "ad_cdn_domain": "pdx",
        "content_cdn_domain": "pdx",
        "transcode_profile": "mobile",
        "slate_domain": "pdx",
        "slate_type": "branded",
        "tracking_domain": "pdx"
    }
}
```

###### Example Parameter processing flow

In the following example, MediaTailor replaces the alias strings with the mapped values in the configuration
aliases. The processing results in the following requests:

- ADS request:

```
https://abc.execute-api.us-west-2.amazonaws.com/ads?sid=[session.id]&ad_type=abc12345
```

- VideoContentSource request:

```
https://abc.mediapackage.us-west-2.amazonaws.com/out/v1/abcd
```

- AdSegmentUrlPrefix:

```
https://ads-west.cdn.example.com/ads/
```

- ContentSegmentUrlPrefix:

```
https://content-west.cdn.example.com/content/
```

- TranscodeProfileName:

```
mobile_optimized
```

- SlateAdUrl:

```
https://slate-west.example.com/slate/brand_slate.mp4
```

- StartUrl:

```
https://tracking-west.example.com/start?session=[session.id]
```

- EndUrl:

```
https://tracking-west.example.com/end?session=[session.id]
```
