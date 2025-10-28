# Require HTTPS for communication between CloudFront

and your Amazon S3 origin

When your origin is an Amazon S3 bucket, your options for using HTTPS for communications with CloudFront depend on how you're using the
bucket. If your Amazon S3 bucket is configured as a website endpoint, you can't configure CloudFront to use HTTPS to communicate with your origin
because Amazon S3 doesn't support HTTPS connections in that configuration.

When your origin is an Amazon S3 bucket that supports HTTPS communication, CloudFront forwards requests
to S3 by using the protocol that viewers used to submit the requests. The default
setting for the [Protocol (custom origins
only)](DownloadDistValuesOrigin.md#DownloadDistValuesOriginProtocolPolicy "DownloadDistValuesOrigin.md#DownloadDistValuesOriginProtocolPolicy") setting is **Match
Viewer** and can't be changed. However, if you enable origin access control
(OAC) for your Amazon S3 origin, the communication used between CloudFront and Amazon S3 depends on your
settings. For more information, see [Create a new origin access control](private-content-restricting-access-to-s3.md#create-oac-overview-s3 "private-content-restricting-access-to-s3.md#create-oac-overview-s3").

If you want to require HTTPS for communication between CloudFront and Amazon S3, you must change the
value of **Viewer Protocol Policy** to **Redirect HTTP to
HTTPS** or **HTTPS Only**. The procedure later in this section
explains how to use the CloudFront console to change **Viewer Protocol
Policy**. For information about using the CloudFront API to update the
`ViewerProtocolPolicy` element for a distribution, see [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") in the
_Amazon CloudFront API Reference_.

When you use HTTPS with an Amazon S3 bucket that supports HTTPS communication, Amazon S3 provides the SSL/TLS certificate, so you don't have to.

## Require HTTPS for an Amazon S3 origin

The following procedure shows you how to configure CloudFront to require HTTPS to your Amazon S3 origin.

###### To configure CloudFront to require

HTTPS to your Amazon S3 origin

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the top pane of the CloudFront console, choose the ID for the distribution that you want
   to update.
3. On the **Behaviors** tab, choose the cache behavior that you want to
   update, and then choose **Edit**.
4. Specify one of the following values for **Viewer Protocol
   Policy**:

**Redirect HTTP to HTTPS**

Viewers can use both protocols, but HTTP requests are automatically redirected
to HTTPS requests. CloudFront returns HTTP status code 301 (Moved Permanently) along with
the new HTTPS URL. The viewer then resubmits the request to CloudFront using the HTTPS
URL.

###### Important

CloudFront doesn't redirect `DELETE`, `OPTIONS`,
`PATCH`, `POST`, or `PUT` requests from HTTP to
HTTPS. If you configure a cache behavior to redirect to HTTPS, CloudFront responds to
HTTP `DELETE`, `OPTIONS`, `PATCH`,
`POST`, or `PUT` requests for that cache behavior with
HTTP status code 403 (Forbidden).

When a viewer makes an HTTP request that is redirected to an HTTPS request, CloudFront
charges for both requests. For the HTTP request, the charge is only for the request
and for the headers that CloudFront returns to the viewer. For the HTTPS request, the
charge is for the request, and for the headers and the object returned by your
origin.

**HTTPS Only**

Viewers can access your content only if they're using HTTPS. If a viewer sends
an HTTP request instead of an HTTPS request, CloudFront returns HTTP status code 403
(Forbidden) and does not return the object. 5. Choose **Yes, Edit**. 6. Repeat steps 3 through 5 for each additional cache behavior that you want to require
HTTPS for between viewers and CloudFront, and between CloudFront and S3. 7. Confirm the following before you use the updated configuration in a production
environment:

    * The path pattern in each cache behavior applies only to the requests that you want
     viewers to use HTTPS for.
    * The cache behaviors are listed in the order that you want CloudFront to evaluate them
     in. For more information, see [Path pattern](DownloadDistValuesCacheBehavior.md#DownloadDistValuesPathPattern "DownloadDistValuesCacheBehavior.md#DownloadDistValuesPathPattern").
    * The cache behaviors are routing requests to the correct origins.
