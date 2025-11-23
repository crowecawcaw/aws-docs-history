# Origin settings

When you use the CloudFront console to create or update a distribution, you provide information
about one or more locations, known as _origins_, where you
store the original versions of your web content. CloudFront gets your web content from your
origins and serves it to viewers via a worldwide network of edge servers.

For the current maximum number of origins that you can create for a distribution, or to
request a higher quota, see [General quotas on distributions](cloudfront-limits.md#limits-web-distributions "cloudfront-limits.md#limits-web-distributions").

If you want to delete an origin, you must first edit or delete the cache behaviors that
are associated with that origin.

###### Important

If you delete an origin, confirm that files that were previously served by that origin
are available in another origin and that your cache behaviors are now routing requests
for those files to the new origin.

When you create or update a distribution, you specify the following values for each
origin.

###### Topics

- [Origin domain](#DownloadDistValuesDomainName "#DownloadDistValuesDomainName")
- [Protocol (custom origins
  only)](#DownloadDistValuesOriginProtocolPolicy "#DownloadDistValuesOriginProtocolPolicy")
- [Origin path](#DownloadDistValuesOriginPath "#DownloadDistValuesOriginPath")
- [Name](#DownloadDistValuesId "#DownloadDistValuesId")
- [Origin access (Amazon S3 origins
  only)](#DownloadDistValuesOAIRestrictBucketAccess "#DownloadDistValuesOAIRestrictBucketAccess")
- [Add custom header](#DownloadDistValuesOriginCustomHeaders "#DownloadDistValuesOriginCustomHeaders")
- [Enable Origin Shield](#create-update-fields-origin-shield "#create-update-fields-origin-shield")
- [Connection attempts](#origin-connection-attempts "#origin-connection-attempts")
- [Connection timeout](#origin-connection-timeout "#origin-connection-timeout")
- [Response timeout](#DownloadDistValuesOriginResponseTimeout "#DownloadDistValuesOriginResponseTimeout")
- [Response completion timeout](#response-completion-timeout "#response-completion-timeout")
- [Keep-alive timeout (custom
  and VPC origins only)](#DownloadDistValuesOriginKeepaliveTimeout "#DownloadDistValuesOriginKeepaliveTimeout")
- [Response and keep-alive timeout
  quotas](#response-keep-alive-timeout-quota "#response-keep-alive-timeout-quota")

## Origin domain

The origin domain is the DNS domain name of the resource where CloudFront will get objects
for your origin, such as an Amazon S3 bucket or HTTP server. For example:

- **Amazon S3 bucket** –
  ``amzn-s3-demo-bucket`.s3.`us-west-2`.amazonaws.com`

###### Note

If you recently created the S3 bucket, the CloudFront distribution might return
`HTTP 307 Temporary Redirect` responses for up to 24 hours.
It can take up to 24 hours for the S3 bucket name to propagate to all AWS
Regions. When the propagation is complete, the distribution automatically
stops sending these redirect responses; you don't need to take any action.
For more information, see [Why am I
getting an HTTP 307 Temporary Redirect response from Amazon S3?](https://repost.aws/knowledge-center/s3-http-307-response "https://repost.aws/knowledge-center/s3-http-307-response") and
[Temporary
Request Redirection](../../../AmazonS3/latest/dev/Redirects.md#TemporaryRedirection "../../../AmazonS3/latest/dev/Redirects.md#TemporaryRedirection").

- **Amazon S3 bucket configured as a website** –
  ``amzn-s3-demo-bucket`.s3-website.`us-west-2`.amazonaws.com`
- **MediaStore container** –
  ``examplemediastore`.data.mediastore.`us-west-1`.amazonaws.com`
- **MediaPackage endpoint** –
  ``examplemediapackage`.mediapackage.`us-west-1`.amazonaws.com`
- **Amazon EC2 instance** –
  ``ec2-203-0-113-25`.compute-1.amazonaws.com`
- **ELB load balancer** –
  ``example-load-balancer-1234567890`.`us-west-2`.elb.amazonaws.com`
- **Your own web server** –
  `www.example.com`

Choose the domain name in the **Origin domain** field, or type the
name. Resources from opt-in Regions must be entered manually. The domain name is not
case-sensitive. Your origin domain must have a publicly resolvable DNS name that routes
requests from clients to targets over the internet.

If you configure CloudFront to connect to your origin over HTTPS, one of the domain names in
the certificate must match the domain name that you specify for **Origin Domain
Name**. If no domain name matches, CloudFront returns HTTP status code 502 (Bad
Gateway) to the viewer. For more information, see [Domain names in the CloudFront distribution
and in the certificate](cnames-and-https-requirements.md#https-requirements-domain-names-in-cert "cnames-and-https-requirements.md#https-requirements-domain-names-in-cert") and [SSL/TLS negotiation failure between
CloudFront and a custom origin server](http-502-bad-gateway.md#ssl-negotitation-failure "http-502-bad-gateway.md#ssl-negotitation-failure").

###### Note

If you are using an origin request policy that forwards the viewer host header to
the origin, the origin must respond with a certificate that matches the viewer host
header. For more information, see [Add CloudFront request headers](adding-cloudfront-headers.md "adding-cloudfront-headers.md").

If your origin is an Amazon S3 bucket, note the following:

- If the bucket is configured as a website, enter the Amazon S3 static website
  hosting endpoint for your bucket; don’t select the bucket name from the list in
  the **Origin domain** field. The static website hosting
  endpoint appears in the Amazon S3 console, on the **Properties**
  page under **Static website hosting**. For more information,
  see [Use an Amazon S3 bucket that's
  configured as a website endpoint](DownloadDistS3AndCustomOrigins.md#concept_S3Origin_website "DownloadDistS3AndCustomOrigins.md#concept_S3Origin_website").
- If you configured Amazon S3 Transfer Acceleration for your bucket, do not specify
  the `s3-accelerate` endpoint for **Origin
  domain**.
- If you're using a bucket from a different AWS account and if the bucket is
  not configured as a website, enter the name, using the following format:

``bucket-name`.s3.`region`.amazonaws.com`

If your bucket reside in a US Region, and you want Amazon S3 to route requests to a
facility in northern Virginia, use the following format:

``bucket-name`.s3.us-east-1.amazonaws.com`

- The files must be publicly readable unless you secure your content in Amazon S3 by
  using a CloudFront origin access control. For more information about access control,
  see [Restrict access to an Amazon S3
  origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").

###### Important

If the origin is an Amazon S3 bucket, the bucket name must conform to DNS naming
requirements. For more information, go to [Bucket restrictions and limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the
_Amazon Simple Storage Service User Guide_.

When you change the value of **Origin domain** for an origin, CloudFront
immediately begins replicating the change to CloudFront edge locations. Until the distribution
configuration is updated in a given edge location, CloudFront continues to forward requests to
the previous origin. As soon as the distribution configuration is updated in that edge
location, CloudFront begins to forward requests to the new origin.

Changing the origin does not require CloudFront to repopulate edge caches with objects from
the new origin. As long as the viewer requests in your application have not changed,
CloudFront continues to serve objects that are already in an edge cache until the TTL on each
object expires or until seldom-requested objects are evicted.

## Protocol (custom origins

only)

###### Note

This applies only to custom origins.

The protocol policy that you want CloudFront to use when fetching objects from your origin.

Choose one of the following values:

- **HTTP only:** CloudFront uses only HTTP to access the
  origin.

###### Important

**HTTP only** is the default setting when the origin is
an Amazon S3 static website hosting endpoint, because Amazon S3 doesn’t support HTTPS
connections for static website hosting endpoints. The CloudFront console does not
support changing this setting for Amazon S3 static website hosting
endpoints.

- **HTTPS only:** CloudFront uses only HTTPS to access the
  origin.
- **Match viewer:** CloudFront communicates with your origin using
  HTTP or HTTPS, depending on the protocol of the viewer request. CloudFront caches the
  object only once even if viewers make requests using both HTTP and HTTPS
  protocols.

###### Important

For HTTPS viewer requests that CloudFront forwards to this origin, one of the
domain names in the SSL/TLS certificate on your origin server must match the
domain name that you specify for **Origin domain**.
Otherwise, CloudFront responds to the viewer requests with an HTTP status code 502
(Bad Gateway) instead of returning the requested object. For more
information, see [Requirements for using SSL/TLS certificates with
CloudFront](cnames-and-https-requirements.md "cnames-and-https-requirements.md").

###### Topics

- [HTTP port](#DownloadDistValuesHTTPPort "#DownloadDistValuesHTTPPort")
- [HTTPS port](#DownloadDistValuesHTTPSPort "#DownloadDistValuesHTTPSPort")
- [Minimum origin SSL
  protocol](#DownloadDistValuesOriginSSLProtocols "#DownloadDistValuesOriginSSLProtocols")

### HTTP port

###### Note

This applies only to custom origins.

(Optional) You can specify the HTTP port on which the custom origin listens. Valid
values include ports 80, 443, and 1024 to 65535. The default value is port 80.

###### Important

Port 80 is the default setting when the origin is an Amazon S3 static website
hosting endpoint, because Amazon S3 only supports port 80 for static website hosting
endpoints. The CloudFront console does not support changing this setting for Amazon S3
static website hosting endpoints.

### HTTPS port

###### Note

This applies only to custom origins.

(Optional) You can specify the HTTPS port on which the custom origin listens.
Valid values include ports 80, 443, and 1024 to 65535. The default value is port 443. When **Protocol** is set to **HTTP only**,
you cannot specify a value for **HTTPS port**.

### Minimum origin SSL

protocol

###### Note

This applies only to custom origins.

Choose the minimum TLS/SSL protocol that CloudFront can use when it establishes an HTTPS
connection to your origin. Lower TLS protocols are less secure, so we recommend that
you choose the latest TLS protocol that your origin supports. When
**Protocol** is set to **HTTP only**, you
cannot specify a value for **Minimum origin SSL protocol**.

If you use the CloudFront API to set the TLS/SSL protocol for CloudFront to use, you cannot
set a minimum protocol. Instead, you specify all of the TLS/SSL protocols that CloudFront
can use with your origin. For more information, see [OriginSslProtocols](../../../cloudfront/latest/APIReference/API_OriginSslProtocols.md "../../../cloudfront/latest/APIReference/API_OriginSslProtocols.md") in the
_Amazon CloudFront API Reference_.

## Origin path

If you want CloudFront to request your content from a directory in your origin, enter the
directory path, beginning with a slash (/). CloudFront appends the directory path to the value
of **Origin domain**, for example,
`cf-origin.example.com/production/images`. Do not add a slash
(/) at the end of the path.

For example, suppose you’ve specified the following values for your
distribution:

- **Origin domain** – An Amazon S3 bucket named
  `amzn-s3-demo-bucket`
- **Origin path** –
  `/production`
- **Alternate domain names (CNAME)** –
  `example.com`

When a user enters `example.com/index.html` in a browser, CloudFront sends a
request to Amazon S3 for `amzn-s3-demo-bucket/production/index.html`.

When a user enters `example.com/acme/index.html` in a browser, CloudFront sends a
request to Amazon S3 for `amzn-s3-demo-bucket/production/acme/index.html`.

## Name

A name is a string that uniquely identifies this origin in this distribution. If you
create cache behaviors in addition to the default cache behavior, you use the name that
you specify here to identify the origin that you want CloudFront to route a request to when
the request matches the path pattern for that cache behavior.

## Origin access (Amazon S3 origins

only)

###### Note

This applies only to Amazon S3 bucket origins (those that are
_not_ using the S3 static website endpoint).

Choose **Origin access control settings (recommended)** if you want
to make it possible to restrict access to an Amazon S3 bucket origin to only specific CloudFront
distributions.

Choose **Public** if the Amazon S3 bucket origin is publicly
accessible.

For more information, see [Restrict access to an Amazon S3
origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").

For information about how to require users to access objects on a custom origin by
using only CloudFront URLs, see [Restrict access to files on custom
origins](private-content-overview.md#forward-custom-headers-restrict-access "private-content-overview.md#forward-custom-headers-restrict-access").

## Add custom header

If you want CloudFront to add custom headers whenever it sends a request to your origin,
specify the header name and its value. For more information, see [Add custom headers to origin requests](add-origin-custom-headers.md "add-origin-custom-headers.md").

For the current maximum number of custom headers that you can add, the maximum length
of a custom header name and value, and the maximum total length of all header names and
values, see [Quotas](cloudfront-limits.md "cloudfront-limits.md").

## Enable Origin Shield

Choose **Yes** to enable CloudFront Origin Shield. For more information
about Origin Shield, see [Use Amazon CloudFront Origin Shield](origin-shield.md "origin-shield.md").

## Connection attempts

You can set the number of times that CloudFront attempts to connect to the origin. You can
specify 1, 2, or 3 as the number of attempts. The default number (if you don’t specify
otherwise) is 3.

Use this setting together with **Connection timeout** to specify how
long CloudFront waits before attempting to connect to the secondary origin or returning an
error response to the viewer. By default, CloudFront waits as long as 30 seconds (3 attempts
of 10 seconds each) before attempting to connect to the secondary origin or returning an
error response. You can reduce this time by specifying fewer attempts, a shorter
connection timeout, or both.

If the specified number of connection attempts fail, CloudFront does one of the
following:

- If the origin is part of an origin group, CloudFront attempts to connect to the
  secondary origin. If the specified number of connection attempts to the
  secondary origin fail, then CloudFront returns an error response to the viewer.
- If the origin is not part of an origin group, CloudFront returns an error response
  to the viewer.

For a custom origin (including an Amazon S3 bucket that’s configured with static website
hosting), this setting also specifies the number of times that CloudFront attempts to get a
response from the origin. For more information, see [Response timeout](#DownloadDistValuesOriginResponseTimeout "#DownloadDistValuesOriginResponseTimeout").

## Connection timeout

The connection timeout is the number of seconds that CloudFront waits when trying to
establish a connection to the origin. You can specify a number of seconds between 1 and
10 (inclusive). The default timeout (if you don’t specify otherwise) is 10
seconds.

Use this setting together with **Connection attempts** to specify how
long CloudFront waits before attempting to connect to the secondary origin or before returning
an error response to the viewer. By default, CloudFront waits as long as 30 seconds (3
attempts of 10 seconds each) before attempting to connect to the secondary origin or
returning an error response. You can reduce this time by specifying fewer attempts, a
shorter connection timeout, or both.

If CloudFront doesn’t establish a connection to the origin within the specified number of
seconds, CloudFront does one of the following:

- If the specified number of **Connection attempts** is more
  than 1, CloudFront tries again to establish a connection. CloudFront tries up to 3 times, as
  determined by the value of **Connection attempts**.
- If all the connection attempts fail and the origin is part of an origin group,
  CloudFront attempts to connect to the secondary origin. If the specified number of
  connection attempts to the secondary origin fail, then CloudFront returns an error
  response to the viewer.
- If all the connection attempts fail and the origin is not part of an origin
  group, CloudFront returns an error response to the viewer.

## Response timeout

The origin response timeout, also known as the _origin read
timeout_ or _origin request timeout_, applies to both
of the following values:

- How long (in seconds) CloudFront waits for a response after forwarding a request to
  the origin.
- How long (in seconds) CloudFront waits after receiving a packet of a response from
  the origin and before receiving the next packet.

###### Tip

If you want to increase the timeout value because viewers are experiencing HTTP
504 status code errors, consider exploring other ways to eliminate those errors
before changing the timeout value. See the troubleshooting suggestions in [HTTP 504 status code (Gateway
Timeout)](http-504-gateway-timeout.md "http-504-gateway-timeout.md").

CloudFront behavior depends on the HTTP method in the viewer request:

- `GET` and `HEAD` requests – If the origin doesn’t
  respond or stops responding within the duration of the response timeout, CloudFront
  drops the connection. CloudFront tries again to connect according to the value of
  [Connection attempts](#origin-connection-attempts "#origin-connection-attempts").
- `DELETE`, `OPTIONS`, `PATCH`,
  `PUT`, and `POST` requests – If the origin
  doesn’t respond for the duration of the read timeout, CloudFront drops the connection
  and doesn’t try again to contact the origin. The client can resubmit the request
  if necessary.

## Response completion timeout

###### Note

Response completion timeout doesn't support the [continuous deployment](continuous-deployment.md "continuous-deployment.md") feature.

The time (in seconds) that a request from CloudFront to the origin can stay open and wait
for a response. If the complete response isn't received from the origin by this time,
CloudFront ends the connection.

Unlike **Response timeout**, which is the wait time for
_individual_ response packets, **Response completion
timeout** is the _maximum_ allowed amount of time that
CloudFront waits for the response to complete. You can use this setting to ensure that CloudFront
doesn't wait indefinitely for a slow or unresponsive origin, even if other timeout
settings allow for a longer wait.

This maximum timeout includes what you specified for other timeout settings and the
number of **Connection attempts** for each retry. You can use these
settings together to specify how long CloudFront waits for the full request and when to end
the request, regardless if it's complete or not.

For example, if you set the following settings:

- **Connection attempts** is 3
- **Connection timeout** is 10 seconds
- **Response timeout** is 30 seconds
- **Response completion timeout** is 60 seconds

This means CloudFront will try to connect to the origin (up to 3 total attempts), with each
connection attempt timing out at 10 seconds. Once connected, CloudFront will wait up to 30
seconds for the origin to respond to the request until it receives the last packet of
the response.

Regardless of the number of connection attempts or the response timeout, CloudFront will end
the connection if the complete response from the origin takes longer than 60 seconds to
complete. CloudFront will then return to the viewer a [HTTP 504 status code (Gateway
Timeout)](http-504-gateway-timeout.md "http-504-gateway-timeout.md") error response or a custom error response if you specified one.

###### Notes

- If you set a value for response completion timeout, the value must be
  equal to or greater than the value for the [response timeout
  (origin read timeout)](#DownloadDistValuesOriginResponseTimeout "#DownloadDistValuesOriginResponseTimeout").
- If you don't set a value for the response completion timeout, CloudFront doesn't
  enforce a maximum value.

## Keep-alive timeout (custom

and VPC origins only)

The keep-alive timeout is how long (in seconds) CloudFront tries to maintain a connection to
your custom origin after it gets the last packet of a response. Maintaining a persistent
connection saves the time that is required to re-establish the TCP connection and
perform another TLS handshake for subsequent requests. Increasing the keep-alive timeout
helps improve the request-per-connection metric for distributions.

###### Note

For the **Keep-alive timeout** value to have an effect, your
origin must be configured to allow persistent connections.

## Response and keep-alive timeout

quotas

- For [response
  timeout,](#DownloadDistValuesOriginResponseTimeout "#DownloadDistValuesOriginResponseTimeout") the default is 30 seconds.
- For [keep-alive
  timeout](#DownloadDistValuesOriginKeepaliveTimeout "#DownloadDistValuesOriginKeepaliveTimeout"), the default is 5 seconds.

If you request a timeout increase for your AWS account, update your distribution
origins so that they have the response timeout and keep-alive timeout values that you
want. A quota increase for your account doesn't automatically update your origins. For
example, if you're using a Lambda@Edge function to set a keep-alive timeout of 90
seconds, your origin must already have a keep-alive timeout of 90 seconds or more.
Otherwise, your Lambda@Edge function might fail to execute.

For more information about distribution quotas, including how to request an increase,
see [General quotas on distributions](cloudfront-limits.md#limits-web-distributions "cloudfront-limits.md#limits-web-distributions").
