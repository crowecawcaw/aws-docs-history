

# IPv6 support for AWS Elemental MediaPackage control plane
<a name="mediapackage-ipv6-support"></a>

AWS Elemental MediaPackage control plane APIs support dual-stack (IPv4 and IPv6) endpoints for both Live and VOD services. This enables you to make API requests using either IPv4 or IPv6 protocols for management operations such as creating channels, endpoints, packaging groups, packaging configurations, and assets.

**Note**  
IPv6 support applies to control plane operations only. Content ingest and delivery endpoints continue to use IPv4.

## IPv6 endpoints
<a name="mediapackage-ipv6-endpoints"></a>

MediaPackage provides the following dual-stack endpoints:
+ **Live**: `mediapackage.{{region}}.api.aws`
+ **VOD**: `mediapackage-vod.{{region}}.api.aws`

Your existing applications continue to work with the original IPv4-only endpoints (`mediapackage.{{region}}.amazonaws.com` and `mediapackage-vod.{{region}}.amazonaws.com`). For a complete list of available endpoints, see [MediaPackage endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/mediapackage.html) in the *AWS General Reference*.

## Using IPv6 endpoints
<a name="mediapackage-ipv6-usage"></a>

To use the IPv6 endpoints, specify the dual-stack endpoint URL when making API calls.

**AWS CLI example (Live)**:

```
aws mediapackage list-channels \
    --endpoint-url https://mediapackage.us-east-1.api.aws
```

**AWS CLI example (VOD)**:

```
aws mediapackage-vod list-packaging-groups \
    --endpoint-url https://mediapackage-vod.us-east-1.api.aws
```

**SDK example (Python)**:

```
import boto3

# Live
live_client = boto3.client(
    'mediapackage',
    endpoint_url='https://mediapackage.us-east-1.api.aws'
)

# VOD
vod_client = boto3.client(
    'mediapackage-vod',
    endpoint_url='https://mediapackage-vod.us-east-1.api.aws'
)
```