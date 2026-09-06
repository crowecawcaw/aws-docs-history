

# Dual-stack (IPv6) endpoints for AWS Elemental MediaTailor
<a name="dualstack-endpoints"></a>

AWS Elemental MediaTailor supports dual-stack endpoints that you can use to connect over either IPv4 or IPv6. These endpoints are functionally equivalent to the standard IPv4-only endpoints. The service behavior is identical, and only the network transport layer differs.

## What are dual-stack endpoints?
<a name="dualstack-what-is"></a>

Dual-stack endpoints advertise both IPv4 and IPv6 addresses. When you use a dual-stack endpoint, DNS resolves to either an IPv4 or IPv6 address based on your network configuration and client preferences. You don't need to change your MediaTailor resources, playback configurations, or ad insertion behavior.

## Supported features
<a name="dualstack-supported-features"></a>

The following table lists MediaTailor feature support for dual-stack endpoints.


| Feature | Dual-stack support | 
| --- | --- | 
| Control plane APIs (all regions) | Supported | 
| SSAI data plane (session initialization, manifest, segment) | Supported | 
| Channel assembly data plane | Supported | 
| AWS Management Console | Supported | 
| AWS SDK | Coming soon | 

## Dual-stack endpoint format
<a name="dualstack-endpoint-format"></a>

MediaTailor dual-stack endpoints use the `.api.aws` domain:
+ **Control plane**: `mediatailor.{{region}}.api.aws`
+ **SSAI data plane**: Displayed in the **Dualstack endpoints** section of your playback configuration details in the AWS Management Console.
+ **Channel assembly data plane**: Displayed in your channel's output details in the AWS Management Console.

Your existing applications continue to work with the original IPv4-only endpoints (`api.mediatailor.{{region}}.amazonaws.com` for control plane, `{{unique-id}}.mediatailor.{{region}}.amazonaws.com` for data plane). For a complete list of available endpoints, see [MediaTailor endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/mediatailor.html) in the *AWS General Reference*.

## Using dual-stack endpoints
<a name="dualstack-using"></a>

### AWS Management Console
<a name="dualstack-using-console"></a>

Dual-stack endpoints appear in the **Playback configuration details** page under the **Dualstack endpoints** section. You can copy these URLs directly for use in your player or CDN configuration.

### AWS Command Line Interface
<a name="dualstack-using-cli"></a>

Specify the dual-stack endpoint URL when you make API calls:

```
aws mediatailor get-playback-configuration \
    --name {{my-config}} \
    --endpoint-url https://mediatailor.{{us-east-1}}.api.aws
```

Replace {{my-config}} with the name of your playback configuration and {{us-east-1}} with your AWS Region.

### AWS SDK
<a name="dualstack-using-sdk"></a>

Enable dual-stack in your SDK configuration.

**Python (boto3)**:

```
import boto3

client = boto3.client(
    'mediatailor',
    endpoint_url='https://mediatailor.{{us-east-1}}.api.aws'
)
```

**JavaScript (AWS SDK v3)**:

```
import { MediaTailorClient } from "@aws-sdk/client-mediatailor";

const client = new MediaTailorClient({
    useDualstackEndpoint: true
});
```

## Considerations
<a name="dualstack-considerations"></a>

Keep the following in mind when you use dual-stack endpoints:
+ Dual-stack endpoints are available in all AWS Regions where MediaTailor is available.
+ You don't need to change your playback configurations, ad decision server settings, or CDN configuration to use dual-stack endpoints.
+ If your CDN uses hostname-pattern-based routing, verify that your rules accommodate the `.api.aws` domain format.
+ Standard AWS guidance for dual-stack endpoints applies. For more information, see [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#dual-stack-endpoints) in the *AWS General Reference*.