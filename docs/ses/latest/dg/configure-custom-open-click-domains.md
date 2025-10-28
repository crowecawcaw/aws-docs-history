# Configuring custom domains to handle

open and click tracking

When you use [event publishing](monitor-using-event-publishing.md "monitor-using-event-publishing.md") to
capture open and click events, Amazon SES makes minor changes to the emails you send. To capture
open events, SES adds a 1 pixel by 1 pixel transparent GIF image in each email sent
through SES which includes a unique file name for each email, and is hosted on a
server operated by SES; when the image is downloaded, SES can tell exactly
which message was opened and by whom.

By default, this pixel is inserted at the bottom of the email; however, some email
providers’ applications truncate the preview of an email when it exceeds a certain size and
may provide a link to view the remainder of the message. In this scenario, the SES pixel
tracking image does not load and will throw off the open rates you’re trying to track. To
get around this, you can optionally place the pixel at the beginning of the email, or
anywhere else, by inserting the `{{ses:openTracker}}` placeholder into the email
body. Once SES receives the message with the placeholder, it will be replaced with
open tracking pixel image.

###### Important

- Any `{{ses:openTracker}}` placeholders in excess of one will be
  removed at sending by SES.
- Only add one `{{ses:openTracker}}` placeholder if you're using them
  in an email template, as more than one will result in a `400
 BadRequestException` error code being returned.
  To capture link click events, SES replaces the links in your emails with links to a
  server operated by SES. This immediately redirects the recipient to his or her
  intended destination. The total size of headers, including cookies, of requests made to this
  server must not exceed 8192 bytes, else a `400 BadRequestException` error code is
  returned.

You also have the option to use your own domains, rather than domains owned and operated
by SES, to create a more cohesive experience for your recipients, meaning all
SES indicators are removed. You can configure multiple custom domains to handle open
and click tracking events. These custom domains are associated with configuration sets. When
you send an email using a configuration set, if that configuration set is configured to use
a custom domain, then the open and click links in that email automatically use the custom
domain specified in that configuration set.

This section contains procedures for setting up a subdomain on a server you own to
automatically redirect users to the open and click tracking servers operated by SES.
There are three steps involved in setting up these domains. First, you configure the
subdomain itself, then set a configuration set to use the custom domain, and then set its
event destination to publish open and click events. This topic contains procedures for
completing all of these steps.

However, if you simply want to enable open or click tracking without setting up a custom
domain, you can proceed directly to defining event destinations for your configuration set
which enables event publishing that is triggered on the event types you specify, including
open and click events. A configuration set can have multiple event destinations with
multiple event types defined. See [Creating Amazon SES event destinations](event-destinations-manage.md "event-destinations-manage.md").

## Part 1: Setting up a domain for

handling open and click link redirects

The specific procedures for setting up a redirect domain vary depending on your web
hosting provider (and your Content Delivery Network, if you use an HTTPS server). The
procedures in the following sections provide general guidance rather than specific
steps.

### Option 1:

Configuring an HTTP domain

If you plan to use an HTTP domain to handle open and click links (as opposed to an
HTTPS domain), the process for configuring the subdomain involves only a few
steps.

###### Note

If you set up a custom domain that uses the HTTP protocol, and you send an
email that contains links that use the HTTPS protocol, your customers may see a
warning message when they click the links in your email. If you plan to send
emails that contain links that use the HTTPS protocol, you should use an HTTPS
domain for handling click tracking events.

###### To set up an HTTP subdomain for handling open and click links

1. Create a subdomain to use for open and click tracking links. SES
   recommends that this subdomain is specifically dedicated to handling these
   links, and that a subdomain is created for each AWS Region you send email
   in that you want to track.
2. Verify the subdomain for use with SES. For more information, see
   [Creating a domain identity](creating-identities.md#verify-domain-procedure "creating-identities.md#verify-domain-procedure").
3. Add a new CNAME record to your subdomain’s DNS settings that redirects
   requests to the SES tracking domain. The address that you redirect to
   must be the in the same AWS Region as your custom subdomain.
   - Use the [Tracking domains table](../../../general/latest/gr/ses.md#ses_tracking_domains "../../../general/latest/gr/ses.md#ses_tracking_domains") in the AWS General Reference to select
     the tracking domain that's in the same region as your custom
     domain.

###### Note

Depending on your web hosting provider, it may take several minutes
for the changes you make to the subdomain's DNS record to take effect.
Your web hosting provider or IT organization can provide additional
information about these delays.

### Option 2:

Configuring an HTTPS domain

You can also use an HTTPS domain for tracking open and link clicks. To set up an
HTTPS domain for tracking open and link clicks, you have to perform some additional
steps, beyond those required for [setting up an HTTP
domain](#configure-custom-open-click-domain-http "#configure-custom-open-click-domain-http").

###### To set up an HTTPS subdomain for handling open and click links

1. Create a subdomain to use for open and click tracking links. SES
   recommends that this subdomain is specifically dedicated to handling these
   links, and that a subdomain is created for each AWS Region you send email
   in that you want to track.
2. Verify the subdomain for use with SES. For more information, see
   [Creating a domain identity](creating-identities.md#verify-domain-procedure "creating-identities.md#verify-domain-procedure").
3. Create a new account with a Content Delivery Network (CDN), such as [Amazon CloudFront](https://aws.amazon.com/cloudfront "https://aws.amazon.com/cloudfront"), see [Get started
   with a basic CloudFront distribution](../../../AmazonCloudFront/latest/DeveloperGuide/GettingStarted.md "../../../AmazonCloudFront/latest/DeveloperGuide/GettingStarted.md").
4. Configure the CDN to the origin which is the SES tracking domain,
   such as `r.us-east-1.awstrack.me` for example. The CDN must point
   to the AWS tracking domain that's in the same region as your custom
   domain. The CDN must pass the `Host` header supplied by the
   requester to the origin, see this [AWS re:Post article](https://repost.aws/knowledge-center/configure-cloudfront-to-forward-headers "https://repost.aws/knowledge-center/configure-cloudfront-to-forward-headers") for more information.
   - Use the [Tracking domains table](../../../general/latest/gr/ses.md#ses_tracking_domains "../../../general/latest/gr/ses.md#ses_tracking_domains") in the AWS General Reference to select
     the tracking domain that's in the same region as your custom
     domain.

5. If you use Route 53 to manage the DNS configuration for your domain and CloudFront
   as your CDN, create an Alias record in Route 53 that refers to your CloudFront
   distribution (such as _d111111abcdef8.cloudfront.net_).
   For more information, see [Creating Records
   by Using the Amazon Route 53 Console](../../../Route53/latest/DeveloperGuide/resource-record-sets-creating.md "../../../Route53/latest/DeveloperGuide/resource-record-sets-creating.md") in the
   _Amazon Route 53 Developer Guide_.

Otherwise, in the DNS configuration for your subdomain, add a CNAME record
that refers to the address of your CDN. 6. Acquire an SSL certificate from a trusted Certificate Authority. The
certificate should cover both the subdomain you created in step 1 as well as
the CDN you configured in steps 3–5. Upload the certificate to the
CDN. 7. You can use the following curl command to validate that your newly created
custom domain is using the correct region and HTTPS protocol. In the
following example, everything is a literal except for the name of your
domain:

```
curl --head https://`custom.domain.com`/favicon.ico
```

A response is returned as in the following example:

```
(python-sdk-test) jdoe@12a34567b89c BaconRedirectService % curl --head https://custom.domain.com/favicon.ico
HTTPS/1.1 200 OK
x-amz-ses-region: us-east-1
x-amz-ses-request-protocol: https
Content-Type: image/x-icon
Transfer-Encoding: chunked
Date: Fri, 30 Aug 2024 13:50:14 GMT
```

This response contains the following properties:

    * The `x-amz-ses-region` header value is the SES
     region which received the request.
    * The `x-amz-ses-request-protocol` header value is the
     protocol used for the request between the CDN and SES in the
     header.

If your setup is correct, the region should reflect the region your domain
was created in and the protocol should be HTTPS.

## Part 2: Specifying your

custom redirect domain and HTTPS policy through a configuration
set

After you configure your domain to handle open and click tracking redirects, you must
specify your custom domain and HTTPS policy in a configuration set.

When you send an email using a configuration set, if that configuration set is
configured to use a custom redirect domain, the open and click links in that email
automatically use the custom domain and HTTPS policy options specified in the
configuration set.

You can complete this using the SES console or the [`CreateConfigurationSet`](../APIReference-V2/API_CreateConfigurationSet.md "../APIReference-V2/API_CreateConfigurationSet.md") v2 API operation.

###### To specify a custom redirect domain and HTTPS policy using the console

- While creating or editing a configuration set, use the [Tracking options](creating-configuration-sets.md#create-config-set-step-4 "creating-configuration-sets.md#create-config-set-step-4") in Step 4 of
  [Create configuration
  sets](creating-configuration-sets.md "creating-configuration-sets.md") to specify your custom
  redirect domain and HTTPS policy options.

###### To specify a custom redirect domain and HTTPS policy using the AWS CLI

You can use the [`CreateConfigurationSet`](../APIReference-V2/API_CreateConfigurationSet.md "../APIReference-V2/API_CreateConfigurationSet.md") operation in the SES API
v2 and use the `TrackingOptions` property to specify your custom redirect
domain and the HTTPS policy. You can call this operation from the AWS CLI as shown in
the following example.

- Create the configuration set in the AWS Region where you want to send and
  track email:

```
aws sesv2 create-configuration-set --cli-input-json file://create.json
```

- In this example, the input file is using parameters of the [`TrackingOptions`](../APIReference-V2/API_TrackingOptions.md "../APIReference-V2/API_TrackingOptions.md")
  property—`CustomRedirectDomain` specifies the custom
  domain to use for tracking open and click links, and `HttpsPolicy`
  specifies an HTTPS policy option:

```
{
    "ConfigurationSetName": "my-config-set",
    "TrackingOptions": {
        "CustomRedirectDomain": "marketing.example.com",
        "HttpsPolicy": "REQUIRE"
    },
    "SendingOptions": {
        "SendingEnabled": true
    }
}
```

For the `HttpsPolicy` parameter, the following values can be
specified to set the protocol of the open and click tracking links for your
custom redirect domain:

    + `OPTIONAL` – (Default behavior) Open tracking links
     will be wrapped using HTTP. Click tracking links will be wrapped using
     the original protocol of the link.
    + `REQUIRE` – Open and Click tracking links will both
     be wrapped using HTTPS.
    + `REQUIRE_OPEN_ONLY` – Open tracking links will be
     wrapped using HTTPS. Click tracking links will be wrapped using the
     original protocol of the link.

## Part 3: Specifying open and click

event types through a configuration set

After specifying your custom domain and HTTPS policy in the configuration set in the
previous step, you must specify open and/or click event types to track in an event
destination through a configuration set.

You can complete this using the SES console or the [`CreateConfigurationSetEventDestination`](../APIReference-V2/API_CreateConfigurationSetEventDestination.md "../APIReference-V2/API_CreateConfigurationSetEventDestination.md") v2 API
operation.

###### To select open and/or click event types using the console

- While creating or modifying an event destination, use [Open and click tracking](event-destinations-manage.md#select-event-types-step "event-destinations-manage.md#select-event-types-step") in Step 6
  of [Creating an event destination](event-destinations-manage.md#event-destination-add "event-destinations-manage.md#event-destination-add") to specify the event types.
