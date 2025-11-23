# Helper methods for origin

modification

This section applies if you dynamically update or change the origin used on the
request inside your CloudFront Functions code. You can update the origin on _viewer
request_ CloudFront Functions only. CloudFront Functions has a module that provides
helper methods to dynamically update or change the origin.

To use this module, create a CloudFront function using JavaScript runtime 2.0 and include
the following statement in the first line of the function code:

```
import cf from 'cloudfront';
```

For more information, see [JavaScript runtime 2.0 features for
CloudFront Functions](functions-javascript-runtime-20.md "functions-javascript-runtime-20.md").

###### Note

The Test API and Test console pages don't test whether an origin modification has
occurred. However, testing ensures that the function code executes without
error.

## Choose between CloudFront Functions

and Lambda@Edge

You can update your origins by using either CloudFront Functions or Lambda@Edge.

When using CloudFront Functions to update origins, you use the _viewer
request_ event trigger, which means this logic will run on every
request when this function is used. When using Lambda@Edge, the origin updating
capabilities are on the _origin request_ event trigger, which
means this logic only runs on cache misses.

Your choice depends largely on your workload and any existing usage of
CloudFront Functions and Lambda@Edge on your distributions. The following considerations
can help you decide whether to use CloudFront Functions or Lambda@Edge to update your
origins.

CloudFront Functions is most useful in the following situations:

- When your requests are dynamic (meaning they cannot be cached) and will
  always go to origin. CloudFront Functions provides better performance and lower
  overall cost.
- When you already have an existing viewer request CloudFront function that will
  run on every request, you can add the origin updating logic into the
  existing function.

To use CloudFront Functions to update origins, see the helper methods in the following
topics.

Lambda@Edge is most useful in the following situations:

- When you have highly cacheable content, Lambda@Edge can be more
  cost-efficient because it runs only on cache misses, while CloudFront Functions
  runs on every request.
- When you already have an existing origin request Lambda@Edge function, you
  can add the origin updating logic into the existing function.
- When your origin update logic requires fetching data from third-party data
  sources, such as Amazon DynamoDB or Amazon S3.

For more information about Lambda@Edge, see [Customize at the edge with Lambda@Edge](lambda-at-the-edge.md "lambda-at-the-edge.md").

## updateRequestOrigin()

method

Use the `updateRequestOrigin()` method to update the origin settings
for a request. You can use this method to update existing origin properties for
origins that are already defined in your distribution, or to define a new origin for
the request. To do so, specify the properties that you want to change.

###### Important

Any settings that you don't specify in the `updateRequestOrigin()`
will inherit the _same settings_ from the
existing origin's configuration.

The origin set by the `updateRequestOrigin()` method can be any HTTP
endpoint and doesn't need to be an existing origin within your CloudFront
distribution.

###### Notes

- If you're updating an origin that is part of an origin group, only the
  _primary origin_ of the origin group is updated.
  The secondary origin remains unchanged. Any response code from the
  modified origin that matches the failover criteria will trigger a
  failover to the secondary origin.
- If you are changing the origin type and have OAC enabled, make sure
  that the origin type in `originAccessControlConfig` matches
  the new origin type.
- You can't use the `updateRequestOrigin()` method to update
  [VPC origins](private-content-vpc-origins.md "private-content-vpc-origins.md"). The
  request will fail.

**Request**

```
updateRequestOrigin({origin properties})
```

The `origin properties` can contain the following:

**domainName (optional)**

The domain name of the origin. If this is not provided, the domain
name from the assigned origin is used instead.

**For custom origins**

Specify a DNS domain name, such as
`www.example.com`. The domain name can't
include a colon (`:`) and can't be an IP address.
The domain name can be up to 253 characters.

**For S3 origins**

Specify the DNS domain name of the Amazon S3 bucket, such as
`amzn-s3-demo-bucket.s3.eu-west-1.amazonaws.com`.
The name can be up to 128 characters, and must be all
lowercase.

**hostHeader (optional, for non-S3 custom origins)**

The host header to use when making the request to the origin. If this
is not provided, the value from the domainName parameter is used. If
neither host header or domain name parameter are provided, the domain
name from the assigned origin is used or the host header from the
incoming request if the forward to origin (FTO) policy includes the
host. The host header can't include a colon (`:`) and can't
be an IP address. The host header can be up to 253 characters.

**originPath (optional)**

The directory path at the origin where the request should locate
content. The path should start with a forward slash (/) but shouldn't
end with one. For example, it shouldn't end with
`example-path/`. If this is not provided, then the origin
path from the assigned origin is used.

**For custom origins**

The path should be URL encoded and have a maximum length
of 255 characters.

**customHeaders (optional)**

You can include custom headers with the request by specifying a header
name and value pair for each custom header. The format is different than
that of the request and response headers in the event structure. Use the
following key-value pair syntax:

```
{"key1": "value1", "key2": "value2", ...}
```

You can't add headers that are disallowed, and a header with the same
name can't also be present in the incoming request `headers`.
Header name must be lowercase in your function code. When CloudFront Functions
converts the event object back into an HTTP request, the first letter of
each word in header names is capitalized, and words are separated by a
hyphen.

For example, if you function code adds a header named
`example-header-name`, CloudFront converts this to
`Example-Header-Name` in the HTTP request. For more
information, see [Custom headers that CloudFront can’t add
to origin requests](add-origin-custom-headers.md#add-origin-custom-headers-denylist "add-origin-custom-headers.md#add-origin-custom-headers-denylist") and [Restrictions on edge functions](edge-functions-restrictions.md "edge-functions-restrictions.md").

If this is not provided, then any custom headers from the assigned
origin are used.

**connectionAttempts (optional)**

The number of times that CloudFront attempts to connect to the origin. The
minimum is 1 and the maximum is 3. If this is not provided, the
connection attempts from the assigned origin are used.

**originShield (optional)**

This enables or updates CloudFront Origin Shield. Using Origin Shield can
help reduce the load on your origin. For more information, see [Use Amazon CloudFront Origin Shield](origin-shield.md "origin-shield.md"). If this is
not provided, the Origin Shield settings from the assigned origin are
used.

**enabled (required)**

Boolean expression to enable or disable Origin Shield.
Accepts a `true` or `false`
value.

**region (required when enabled)**

The AWS Region for Origin Shield. Specify the
AWS Region that has the lowest latency to your origin. Use
the Region code, not the Region name. For example, use
`us-east-2` to specify the US East (Ohio)
Region.

When you enable CloudFront Origin Shield, you must specify the
AWS Region for it. For a list of available AWS Regions
and help choosing the best Region for your origin, see [Choose the AWS Region for Origin
Shield](origin-shield.md#choose-origin-shield-region "origin-shield.md#choose-origin-shield-region").

**originAccessControlConfig (optional)**

The unique identifier of an origin access control (OAC) for this
origin. This is only used when the origin supports a CloudFront OAC, such as
Amazon S3, Lambda function URLs, MediaStore, and MediaPackage V2. If this is not provided,
then the OAC settings from the assigned origin are used.

This does not support the legacy origin access identity (OAI). For
more information, see [Restrict access to an AWS
origin](private-content-restricting-access-to-origin.md "private-content-restricting-access-to-origin.md").

**enabled (required)**

Boolean expression to enable or disable OAC. Accepts a
`true` or `false` value.

**signingBehavior (required when enabled)**

Specifies which requests CloudFront signs (adds authentication
information to). Specify `always` for the most
common use case. For more information, see [Advanced settings for origin access
control](private-content-restricting-access-to-s3.md#oac-advanced-settings-s3 "private-content-restricting-access-to-s3.md#oac-advanced-settings-s3").

This field can have one of the following values:

- `always` – CloudFront signs all origin
  requests, overwriting the `Authorization`
  header from the viewer request if one exists.
- `never` – CloudFront doesn’t sign any
  origin requests. This value turns off origin access
  control for the origin.
- `no-override` – If the viewer
  request doesn’t contain the
  `Authorization` header, then CloudFront signs
  the origin request. If the viewer request contains
  the `Authorization` header, then CloudFront
  doesn’t sign the origin request and instead passes
  along the `Authorization` header from the
  viewer request.

###### Warning

To pass along the `Authorization`
header from the viewer request, you must add it to
an origin request policy for all cache behaviors
that use origins associated with this origin
access control. For more information, see [Control origin requests with a policy](controlling-origin-requests.md "controlling-origin-requests.md").

**signingProtocol (required when enabled)**

The signing protocol of the OAC, which determines how CloudFront
signs (authenticates) requests. The only valid value is
`sigv4`.

**originType (required when enabled)**

The type of origin for this OAC. Valid values include
`s3`, `mediapackagev2`,
`mediastore`, and `lambda`.

**timeouts (optional)**

Timeouts that you can specify for how long CloudFront should attempt to wait
for origins to respond or send data. If this is not provided, then the
timeout settings from the assigned origin are used.

###### Note

Unless specified, these timeouts support both custom origins and
Amazon S3 origins.

**readTimeout (optional)**

The `readTimeout` applies to both of the
following values:

- How long (in seconds) CloudFront waits for a response
  after forwarding a request to the origin.
- How long (in seconds) CloudFront waits after receiving a
  packet of a response from the origin and before
  receiving the next packet.

The minimum timeout is 1 second and the maximum is 120
seconds. For more information, see [Response timeout](DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout "DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout").

**responseCompletionTimeout (optional)**

The time (in seconds) that a request from CloudFront to the
origin can stay open and wait for a response. If the
complete response isn't received from the origin by this
time, CloudFront ends the connection.

The value for `responseCompletionTimeout` must
be equal to or greater than the value for the
`readTimeout`. For more information, see
[Response completion timeout](DownloadDistValuesOrigin.md#response-completion-timeout "DownloadDistValuesOrigin.md#response-completion-timeout").

**keepAliveTimeout (optional)**

This timeout only applies to custom origins, not Amazon S3
origins. (S3 origin configurations will ignore these
settings.)

The `keepAliveTimeout` specifies how long CloudFront
should try to maintain the connection to the origin after
receiving the last packet of the response. The minimum
timeout is 1 second and the maximum is 120 seconds. For more
information, see [Keep-alive timeout (custom
and VPC origins only)](DownloadDistValuesOrigin.md#DownloadDistValuesOriginKeepaliveTimeout "DownloadDistValuesOrigin.md#DownloadDistValuesOriginKeepaliveTimeout").

**connectionTimeout (optional)**

The number of seconds that CloudFront waits when trying to
establish a connection to the origin. The minimum timeout is
1 second and the maximum is 10 seconds. For more
information, see [Connection timeout](DownloadDistValuesOrigin.md#origin-connection-timeout "DownloadDistValuesOrigin.md#origin-connection-timeout").

**customOriginConfig (optional)**

Use `customOriginConfig` to specify connection settings for
origins that are _not_ an Amazon S3 bucket. There is one
exception: you can specify these settings if the S3 bucket is configured
with static website hosting. (Other types of S3 bucket configurations
will ignore these settings.) If `customOriginConfig` is not
provided, then the settings from the assigned origin are used.

**port (required)**

The HTTP port that CloudFront uses to connect to the origin.
Specify the HTTP port that the origin listens on.

**protocol (required)**

Specifies the protocol (HTTP or HTTPS) that CloudFront uses to
connect to the origin. Valid values are as follows:

- `http` – CloudFront always uses HTTP
  to connect to the origin
- `https` – CloudFront always uses HTTPS
  to connect to the origin

**sslProtocols (required)**

A list that specifies the minimum SSL/TLS protocol that
CloudFront uses when connecting to your origin over HTTPS. Valid
values include `SSLv3`, `TLSv1`,
`TLSv1.1`, and `TLSv1.2`. For more
information, see [Minimum origin SSL
protocol](DownloadDistValuesOrigin.md#DownloadDistValuesOriginSSLProtocols "DownloadDistValuesOrigin.md#DownloadDistValuesOriginSSLProtocols").

**ipAddressType (optional)**

Specifies the IP address type that CloudFront uses to connect to
the origin. Valid values include `ipv4`,
`ipv6`, and `dualstack`. Changing
`ipAddressType` is only supported when the
`domainName` property is also being
changed.

**sni (optional, for non-S3 custom origins)**

The Server Name Indication (SNI) is an extension to the Transport
Layer Security (TLS) protocol by which a client indicates which hostname
it's attempting to connect to at the start of the TLS handshake process.
This value should match a common name on a TLS certificate on your
origin server. Otherwise, your origin server may throw an error.

If this is not provided, the value from the `hostHeader`
parameter is used. If the host header not provided, the value from the
`domainName` parameter is used.

If neither host header or domain name parameter are provided, the
domain name from the assigned origin is used or the host header from the
incoming request if the forward to origin (FTO) policy includes the
host. The SNI can't include a colon (`:`) and can't be an IP
address. The SNI can be up to 253 characters.

**allowedCertificateNames (optional, for non-S3 custom origins)**

You can include a list of valid certificate names to be used by CloudFront
to validate the domain matching from your origin server TLS certificate
during the TLS handshake with your origin server. This field expects an
array of valid domain names and can include wildcard domains, such as
`*.example.com`.

You can specify up to 20 allowed certificate names. Each certificate
name can have up to 64 characters.

###### Example – Update to Amazon S3 request origin

The following example changes the viewer request’s origin to an S3 bucket,
enables OAC, and resets custom headers sent to the origin.

```
cf.updateRequestOrigin({
    "domainName" : "amzn-s3-demo-bucket-in-us-east-1.s3.us-east-1.amazonaws.com",
    "originAccessControlConfig": {
        "enabled": true,
        "signingBehavior": "always",
        "signingProtocol": "sigv4",
        "originType": "s3"
    },
    // Empty object resets any header configured on the assigned origin
    "customHeaders": {}
});
```

###### Example – Update to Application Load Balancer request origin

The following example changes the viewer request’s origin to an Application Load Balancer origin
and sets a custom header and timeouts.

```
cf.updateRequestOrigin({
    "domainName" : "example-1234567890.us-east-1.elb.amazonaws.com",
    "timeouts": {
        "readTimeout": 30,
        "connectionTimeout": 5
    },
    "customHeaders": {
        "x-stage": "production",
        "x-region": "us-east-1"
    }
});
```

###### Example – Update to origin with Origin Shield enabled

In the following example, the origin in the distribution has Origin Shield
enabled. The function code updates only the domain name used for the origin and
omits all the other optional parameters. In this case, Origin Shield will still
be used with the modified origin domain name because the Origin Shield
parameters were not updated.

```
cf.updateRequestOrigin({
    "domainName" : "www.example.com"
});
```

###### Example – Update the host header, SNI, and allowed certificate names

###### Warning

For most use cases, you won't need to use this type of modification to
requests going to your origin. These parameters shouldn't be used unless you
understand the impact of changing these values.

The following example changes the domain name, the host header, SNI, and
allowed certificates on the request to the origin.

```
cf.updateRequestOrigin({
    "domainName": "www.example.com",
    "hostHeader": "test.example.com",
    "sni": "test.example.net",
    "allowedCertificateNames": ["*.example.com", "*.example.net"],
});
```

## selectRequestOriginById()

method

Use `selectRequestOriginById()` to update an existing origin by
selecting a different origin that's already configured in your distribution. This
method uses all the same settings that are defined by the updated origin.

This method only accepts origins that are already defined in the same distribution
used when running the function. Origins are referenced by the origin ID, which is
the origin name that you defined when setting up the origin.

If you have a VPC origin configured in your distribution, you can use this method
to update your origin to your VPC origin. For more information, see [Restrict access with VPC origins](private-content-vpc-origins.md "private-content-vpc-origins.md").

**Request**

```
cf.selectRequestOriginById(origin_id, {origin_overrides})
```

In the previous example, `origin_id` is a string that points to the
origin name of an origin in the distribution that's running the function. The
`origin_overrides` parameter can contain the following:

**hostHeader (optional, for non-S3 custom origins)**

The host header to use when making the request to the origin. If this
is not provided, the value from the `domainName` parameter is
used.

If neither host header or domain name parameter are provided, the
domain name from the assigned origin is used or the host header from the
incoming request if the forward to origin (FTO) policy includes the
host. The host header can't include a colon (`:`) and can't
be an IP address. The host header can be up to 253 characters.

**sni (optional, for non-S3 custom origins)**

The Server Name Indication (SNI) is an extension to the Transport
Layer Security (TLS) protocol by which a client indicates which hostname
it's attempting to connect to at the start of the TLS handshake process.
This value should match a common name on a TLS certificate on your
origin server. Otherwise, your origin server may throw an error.

If this is not provided, the value from the `hostHeader`
parameter is used. If the host header not provided, the value from the
`domainName` parameter is used.

If neither host header or domain name parameter are provided, the
domain name from the assigned origin is used or the host header from the
incoming request if the forward to origin (FTO) policy includes the
host. The SNI can't include a colon (`:`) and can't be an IP
address. The SNI can be up to 253 characters.

**allowedCertificateNames (optional, for non-S3 custom origins)**

You can include a list of valid certificate names to be used by CloudFront
to validate the domain matching from your origin server TLS certificate
during the TLS handshake with your origin server. This field expects an
array of valid domain names and can include wildcard domains, such as
`*.example.com`.

You can specify up to 20 allowed certificate names. Each certificate
name can have up to 64 characters.

**Request**

```
selectRequestOriginById(origin_id)
```

In the preceding example, `origin_id` is a string that points to the
origin name of an origin in the distribution that's running the function.

###### Example – Select Amazon S3 request origin

The following example selects the origin named
`amzn-s3-demo-bucket-in-us-east-1` from the list of origins
associated with the distribution, and applies the configuration settings of the
`amzn-s3-demo-bucket-in-us-east-1` origin to the request.

```
cf.selectRequestOriginById("amzn-s3-demo-bucket-in-us-east-1");
```

###### Example – Select Application Load Balancer request origin

The following example selects an Application Load Balancer origin named `myALB-prod`
from the list of origins associated with the distribution, and applies the
configuration settings of `myALB-prod` to the request.

```
cf.selectRequestOriginById("myALB-prod");
```

###### Example – Select Application Load Balancer request origin and override the host header

Like the previous example, the following example selects an Application Load Balancer origin named
`myALB-prod` from the list of origins associated with the
distribution, and applies the configuration settings of `myALB-prod`
to the request. However, this example overrides the host header value using
`origin_overrides`.

```
cf.overrideRequestOrigin("myALB-prod",{
        "hostHeader" : "test.example.com"
});
```

## createRequestOriginGroup() method

Use `createRequestOriginGroup()` to define two origins to use as an
[origin group](high_availability_origin_failover.md#concept_origin_groups.creating "high_availability_origin_failover.md#concept_origin_groups.creating") for failover
in scenarios that require high availability.

An origin group includes two origins (a primary and a secondary) and a failover
criteria that you specify. You create an origin group to support origin failover in
CloudFront. When you create or update an origin group using this method, you can specify
the origin group instead of a single origin. CloudFront will failover from the primary
origin to the secondary origin, using the failover criteria.

If you have a VPC origin configured in your distribution, you can use this method
to create an origin group using a VPC origin. For more information, see [Restrict access with VPC origins](private-content-vpc-origins.md "private-content-vpc-origins.md").

### Request

```
createRequestOriginGroup({origin_group_properties})
```

In the preceding example, the `origin_group_properties` can contain
the following:

**originIds (required)**

Array of `origin_ids`, where the `origin_id`
is a string that points to the origin name of an origin in the
distribution running the function. You must provide two origins as
part of the array. The first origin in the list is the primary
origin and the second serves as the second origin for failover
purposes.

**originOverrides (optional)**

A few advanced settings are allowed to be overwritten by using
the `{origin_overrides}` parameter. The `origin
 overrides` can contain the following:

**hostHeader (optional, for non-S3 custom origins)**

The host header to use when making the request to the
origin. If this is not provided, the value from the
`domainName` parameter is used.

If neither host header or domain name parameter are
provided, the domain name from the assigned origin is
used or the host header from the incoming request if the
forward to origin (FTO) policy includes the host. The
host header can't include a colon (`:`) and
can't be an IP address. The host header can be up to 253
characters.

**sni (optional, for non-S3 custom origins)**

The Server Name Indication (SNI) is an extension to
the Transport Layer Security (TLS) protocol by which a
client indicates which hostname it is attempting to
connect to at the start of the TLS handshaking process.
This value should match a common name on a TLS
certificate on your origin server, otherwise your origin
server may throw an error.

If this is not provided, the value from the
`hostHeader` parameter is used. If the
host header not provided, the value from the
`domainName` parameter is used.

If neither host header or domain name parameter are
provided, the domain name from the assigned origin is
used or the host header from the incoming request if the
forward to origin (FTO) policy includes the host. The
SNI can't include a colon (`:`) and can't be
an IP address. The SNI can be up to 253
characters.

**allowedCertificateNames (optional, for non-S3 custom
origins)**

You can include a list of valid certificate names to
be used by CloudFront to validate the domain matching from
your origin server TLS certificate during the TLS
handshake with your origin server. This field expects an
array of valid domain names and can include wildcard
domains, such as `*.example.com`.

You can specify up to 20 allowed certificate names.
Each certificate name can have up to 64
characters.

**selectionCriteria (optional)**

Select whether to use the `default` origin failover
criteria or to use the `media-quality-score` based
failover logic. Valid values are as follows:

- `default` uses the failover criteria, based on
  the status codes that are specified in the
  `failoverCriteria`. If you don't set
  `selectionCriteria` in the function,
  `default` will be used.
- `media-quality-score` is used when the media
  aware routing capability is being used.

**failoverCriteria (required)**

An array of status codes that, when returned from the primary
origin, will trigger CloudFront to failover to the secondary origin. If
you overwrite an existing origin group, this array will overwrite
all failover status codes that are set in the origin group's
original configuration.

When you use `media-quality-score`
`selectionCriteria`, CloudFront will attempt to route requests
based on the media quality score. If the selected origin returns an
error code set in this array, CloudFront will failover to the other
origin.

###### Example – Create request origin group

The following example creates an origin group for a request using the
origin IDs. These origin IDs come from the origin group configuration for
the distribution used to run this function.

Optionally, you can use `originOverrides` to override the
origin group configurations for `sni`, `hostHeader`,
and `allowedCertificateNames`.

```
import cf from 'cloudfront';

function handler(event) {
    cf.createRequestOriginGroup({
        "originIds": [
            {
                "originId": "origin-1",
                "originOverrides": {
                    "hostHeader": "hostHeader.example.com",
                    "sni": "sni.example.com",
                    "allowedCertificateNames": ["cert1.example.com", "cert2.example.com", "cert3.example.com"]
                }
            },
            {
                "originId": "origin-2",
                "originOverrides": {
                    "hostHeader": "hostHeader2.example.com",
                    "sni": "sni2.example.com",
                    "allowedCertificateNames": ["cert4.example.com", "cert5.example.com"]
                }
            }
        ],
        "failoverCriteria": {
            "statusCodes": [500]
        }
    });

    event.request.headers['x-hookx'] = { value: 'origin-overrides' };
    return event.request;
}
```
