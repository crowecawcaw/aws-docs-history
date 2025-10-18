# Optimize high availability with CloudFront
 origin failover

You can set up CloudFront with origin failover for scenarios that require high availability.
 To get started, you create an *origin group* with two origins: a
 primary and a secondary. If the primary origin is unavailable, or returns specific HTTP
 response status codes that indicate a failure, CloudFront automatically switches to the
 secondary origin.

To set up origin failover, you must have a distribution with at least two origins.
 Next, you create an origin group for your distribution that includes two origins,
 setting one as the primary. Finally, you create or update a cache behavior to use the
 origin group.

To see the steps for setting up origin groups and configuring specific origin failover
 options, see [Create an origin group](#concept_origin_groups.creating "#concept_origin_groups.creating").

After you configure origin failover for a cache behavior, CloudFront does the following for
 viewer requests:


* When there’s a cache hit, CloudFront returns the requested object.
* When there’s a cache miss, CloudFront routes the request to the primary origin in
 the origin group.
* When the primary origin returns a status code that is not configured for
 failover, such as an HTTP 2xx or 3xx status code, CloudFront serves the requested
 object to the viewer.
* When any of the following occur:




	+ The primary origin returns an HTTP status code that you’ve configured
	 for failover
	+ CloudFront fails to connect to the primary origin (when 503 is set as a failover code)
	+ The response from the primary origin takes too long (times out) (when 504 is set as a failover code)
Then CloudFront routes the request to the secondary origin in the origin
 group.


###### Note

For some use cases, like streaming video content, you might want CloudFront to
 fail over to the secondary origin quickly. To adjust how quickly CloudFront fails
 over to the secondary origin, see [Control origin timeouts and
 attempts](#controlling-attempts-and-timeouts "#controlling-attempts-and-timeouts").
CloudFront routes all incoming requests to the primary origin, even when a previous request
 failed over to the secondary origin. CloudFront only sends requests to the secondary origin
 after a request to the primary origin fails.

CloudFront fails over to the secondary origin only when the HTTP method of the viewer
 request is `GET`, `HEAD`, or `OPTIONS`. CloudFront does not
 fail over when the viewer sends a different HTTP method (for example `POST`,
 `PUT`, and so on).

The following diagram illustrates how origin failover works.


![How origin failover works](images/origingroups-overview.png)
###### Topics

* [Create an origin group](#concept_origin_groups.creating "#concept_origin_groups.creating")
* [Control origin timeouts and
 attempts](#controlling-attempts-and-timeouts "#controlling-attempts-and-timeouts")
* [Use origin failover with Lambda@Edge
 functions](#concept_origin_groups.lambda "#concept_origin_groups.lambda")
* [Use custom error pages with
 origin failover](#concept_origin_groups.custom-error "#concept_origin_groups.custom-error")

## Create an origin group


###### To create an origin group

1. Sign in to the AWS Management Console and open the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose the distribution that you want to create the origin group
 for.
3. Choose the **Origins** tab.
4. Make sure the distribution has more than one origin. If it doesn’t, add a
 second origin.
5. On the **Origins** tab, in the **Origin
 groups** pane, choose **Create origin
 group**.
6. Choose the origins for the origin group. After you add origins, use the
 arrows to set the priority—that is, which origin is primary and which is
 secondary.
7. Enter a name for the origin group.
8. Choose the HTTP status codes to use as failover criteria. You can choose
 any combination of the following status codes: 400, 403, 404, 416, 500, 502,
 503, or 504. When CloudFront receives a response with one of the status codes that
 you specify, it fails over to the secondary origin.


###### Note

CloudFront fails over to the secondary origin only when the HTTP method of
 the viewer request is `GET`, `HEAD`, or
 `OPTIONS`. CloudFront does not fail over when the viewer sends
 a different HTTP method (for example `POST`,
 `PUT`, and so on).
9. Under **Origin selection criteria**, specify how your
 origins are selected when your distribution routes viewer requests. You can
 choose the following options.




**Default**

CloudFront will use the default origin priority that you specify on
 the **Settings** page.



**Media quality score**

CloudFront tracks and uses this score to determine the first origin
 to forward the request to. This also authorizes CloudFront to make
 asynchronous `HEAD` requests to the alternate origin
 in the origin group to determine its media quality score. You
 can only choose this option for AWS Elemental MediaPackage v2 origins. For more
 information, see [Media quality-aware resiliency](media-quality-score.md "media-quality-score.md").
10. Choose **Create origin group**.

Make sure to assign your origin group as the origin for your distribution's cache
 behavior. For more information, see [Name](DownloadDistValuesOrigin.md#DownloadDistValuesId "DownloadDistValuesOrigin.md#DownloadDistValuesId").


## Control origin timeouts and
 attempts


By default, CloudFront tries to connect to the primary origin in an origin group for as
 long as 30 seconds (3 connection attempts of 10 seconds each) before failing over to
 the secondary origin. For some use cases, like streaming video content, you might
 want CloudFront to fail over to the secondary origin more quickly. You can adjust the
 following settings to affect how quickly CloudFront fails over to the secondary origin. If
 the origin is a secondary origin, or an origin that is not part of an origin group,
 these settings affect how quickly CloudFront returns an HTTP 504 response to the
 viewer.


To fail over more quickly, specify a shorter connection timeout, fewer connection
 attempts, or both. For custom origins (including Amazon S3 bucket origins that *are* configured with static website hosting), you can
 also adjust the origin response timeout.




**Origin connection timeout**

The origin connection timeout setting affects how long CloudFront waits when
 trying to establish a connection to the origin. By default, CloudFront waits
 10 seconds to establish a connection, but you can specify 1–10
 seconds (inclusive). For more information, see [Connection timeout](DownloadDistValuesOrigin.md#origin-connection-timeout "DownloadDistValuesOrigin.md#origin-connection-timeout").



**Origin connection attempts**

The origin connection attempts setting affects the number of times
 that CloudFront attempts to connect to the origin. By default, CloudFront tries 3
 times to connect, but you can specify 1–3 (inclusive). For more
 information, see [Connection attempts](DownloadDistValuesOrigin.md#origin-connection-attempts "DownloadDistValuesOrigin.md#origin-connection-attempts").


For a custom origin (including an Amazon S3 bucket that’s configured with
 static website hosting), this setting also affects the number of times
 that CloudFront attempts to get a response from the origin in the case of an
 origin response timeout.



**Origin response timeout**

The origin response
 timeout,
 also known as the origin read timeout,
 
 affects how long CloudFront waits to receive a response (or to receive the
 complete response) from the origin. By default, CloudFront waits for 30
 seconds, but you can specify 1–120 seconds (inclusive). For more
 information, see [Response timeout](DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout "DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout").




### How to change these
 settings


**To change these settings in the [CloudFront
 console](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home")**



* For a new origin or a new distribution, you specify these values when you
 create the resource.
* For an existing origin in an existing distribution, you specify these
 values when you edit the origin.

For more information, see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").


## Use origin failover with Lambda@Edge
 functions


You can use Lambda@Edge functions with CloudFront distributions that you’ve set up with
 origin groups. To use a Lambda function, specify it in an [origin request or origin response
 trigger](lambda-cloudfront-trigger-events.md "lambda-cloudfront-trigger-events.md") for an origin group when you create the cache behavior. When you
 use a Lambda@Edge function with an origin group, the function can be triggered twice
 for a single viewer request. For example, consider this scenario:



1. You create a Lambda@Edge function with an origin request trigger.
2. The Lambda function is triggered once when CloudFront sends a request to the
 primary origin (on a cache miss).
3. The primary origin responds with an HTTP status code that’s configured for
 failover.
4. The Lambda function is triggered again when CloudFront sends the same request to
 the secondary origin.

The following diagram illustrates how origin failover works when you include a
 Lambda@Edge function in an origin request or response trigger.



![How origin failover works with Lambda@Edge functions](images/origingroups-with-lambda-edge.png)

For more information about using Lambda@Edge triggers, see [Add triggers for a Lambda@Edge
 function](lambda-edge-add-triggers.md "lambda-edge-add-triggers.md").


For more information about managing DNS failover, see [Configuring
 DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html") in the *Amazon Route 53 Developer
 Guide*.


## Use custom error pages with
 origin failover


You can use custom error pages with origin groups similarly to how you use them
 with origins that are not set up for origin failover. 


When you use origin failover, you can configure CloudFront to return a custom error page
 for the primary or secondary origin (or both):



* **Return a custom error page for the primary
 origin** – If the primary origin returns an HTTP status code
 that’s not configured for failover, CloudFront returns the custom error page to
 viewers.
* **Return a custom error page for the secondary
 origin** – If CloudFront receives a failure status code from the
 secondary origin, CloudFront returns the custom error page.

For more information about using custom error pages with CloudFront, see [Generate custom error responses](GeneratingCustomErrorResponses.md "GeneratingCustomErrorResponses.md").
