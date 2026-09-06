

# IPv6 support for AWS Elemental MediaPackage V2 control plane
<a name="mediapackagev2-ipv6-support"></a>

AWS Elemental MediaPackage V2 control plane APIs support dual-stack (IPv4 and IPv6) endpoints. This enables you to make API requests using either IPv4 or IPv6 protocols for management operations such as creating channel groups, channels, and origin endpoints.

**Note**  
IPv6 support applies to control plane operations only. Content ingest and delivery endpoints continue to use IPv4. IPv6 support for the data plane is planned for a future release.

## IPv6 endpoints
<a name="mediapackagev2-ipv6-endpoints"></a>

MediaPackage V2 provides the following dual-stack endpoints:
+ **Standard endpoint**: `mediapackagev2.{{region}}.api.aws`
+ **FIPS endpoint** (FIPS-enabled regions): `mediapackagev2-fips.{{region}}.api.aws`

Your existing applications continue to work with the original IPv4-only endpoints (`mediapackagev2.{{region}}.amazonaws.com`). For a complete list of available endpoints, see [MediaPackage endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/mediapackage.html) in the *AWS General Reference*.

## Using IPv6 endpoints
<a name="mediapackagev2-ipv6-usage"></a>

To use the IPv6 endpoints, specify the dual-stack endpoint URL when making API calls.

**AWS CLI example**:

```
aws mediapackagev2 list-channel-groups \
    --endpoint-url https://mediapackagev2.us-east-1.api.aws
```

**SDK example (Python)**:

```
import boto3

client = boto3.client(
    'mediapackagev2',
    endpoint_url='https://mediapackagev2.us-east-1.api.aws'
)
```