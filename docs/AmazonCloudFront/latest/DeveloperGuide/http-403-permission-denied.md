# HTTP 403 status code (Permission
 Denied)

An HTTP 403 error means the client isn't authorized to access the requested
 resource. The client understands the request, but can't authorize viewer access. The
 following are common causes when CloudFront returns this status code:

###### Topics

* [Alternate CNAME is
 incorrectly configured](#alternate-cname-incorrectly-configured "#alternate-cname-incorrectly-configured")
* [AWS WAF is configured
 on CloudFront distribution or at the origin](#aws-waf-configured-on-distribution-origin "#aws-waf-configured-on-distribution-origin")
* [Custom origin returns a 403
 error](#custom-origin-returning-403 "#custom-origin-returning-403")
* [Amazon S3 origin returns a 403 error](#s3-origin-403-error "#s3-origin-403-error")
* [Geographic restrictions return a 403
 error](#geolocation-403 "#geolocation-403")
* [Signed URL or signed cookie
 configuration returns a 403 error](#signed-URLs-cookies-403 "#signed-URLs-cookies-403")
* [Stacked distributions cause a 403
 error](#stacked-distributions-403 "#stacked-distributions-403")

## Alternate CNAME is
 incorrectly configured


Verify that you specified the correct CNAME for our distribution. To use an
 alternate CNAME instead of the default CloudFront URL:



1. Create a CNAME record in your DNS to point the CNAME to CloudFront
 distribution URL.
2. Add the CNAME in your CloudFront distribution configuration.

If you create the DNS record but don't add the CNAME in your CloudFront distribution
 configuration, then the request returns a 403 error. For more information about
 configuring a custom CNAME, see [Use custom URLs by adding alternate domain names (CNAMEs)](CNAMEs.md "CNAMEs.md").


## AWS WAF is configured
 on CloudFront distribution or at the origin


When AWS WAF sits between the client and CloudFront, CloudFront can't distinguish between a
 403 error code that’s returned by your origin and a 403 error code that's
 returned by AWS WAF when a request is blocked.


To find the source of the 403 status code, check your AWS WAF web access control
 list (ACL) rule for a blocked request. For more information, see the following
 topics:



* [AWS WAF web access control lists (web
 ACLs)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html "https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html")
* [Testing and tuning your AWS WAF
 protections](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html "https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html")

## Custom origin returns a 403
 error


If you're using a custom origin, you might see a 403 error if you have a
 custom firewall configuration at the origin. To troubleshoot, make the request
 directly to the origin. If you can replicate the error without CloudFront, then the
 origin is causing the 403 error. 


If the custom origin is causing the error, check the origin logs to identify
 what might be causing the error. For more information, see the following
 troubleshooting topics:



* [How do I troubleshoot HTTP 403 errors from
 API Gateway?](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-troubleshoot-403-forbidden/  "https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-troubleshoot-403-forbidden/ ")
* [How do I troubleshoot Application Load Balancer HTTP 403 forbidden
 errors?](https://repost.aws/knowledge-center/alb-http-403-error "https://repost.aws/knowledge-center/alb-http-403-error")

## Amazon S3 origin returns a 403 error


You might see a 403 error for the following reasons:



* CloudFront doesn't have access to the Amazon S3 bucket. This can happen if origin
 access identity (OAI) or origin access control (OAC) isn't enabled for
 your distribution and the bucket is private.
* The specified path in the requested URL isn't correct.
* The requested object doesn't exist.
* The host header was forwarded with the REST API endpoint. For more
 information, see [HTTP Host header bucket specification](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#VirtualHostingSpecifyBucket "https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#VirtualHostingSpecifyBucket") in the
 *Amazon Simple Storage Service User Guide*.
* You configured custom error pages. For more information, see [How CloudFront processes errors when
 you have configured custom error pages](HTTPStatusCodes.md#HTTPStatusCodes-custom-error-pages "HTTPStatusCodes.md#HTTPStatusCodes-custom-error-pages").

## Geographic restrictions return a 403
 error


If you enabled geographic restrictions (also known as geoblocking) to prevent
 users in specific geographic locations from accessing content that you're
 distributing through a CloudFront distribution, blocked users receive a 403
 error.


For more information, see [Restrict the geographic distribution of your content](georestrictions.md "georestrictions.md").


## Signed URL or signed cookie
 configuration returns a 403 error


If you enabled **Restrict viewer access** for your
 distribution's behavior configuration, then requests that don't use signed
 cookies or signed URLs result in a 403 error. For more information, see the
 following topics:



* [Serve private content with signed URLs and signed
 cookies](PrivateContent.md "PrivateContent.md")
* [How do I troubleshoot issues related to a signed
 URL or signed cookies in CloudFront?](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-troubleshoot-signed-url-cookies/ "https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-troubleshoot-signed-url-cookies/")

## Stacked distributions cause a 403
 error


If you have two or more distributions within a chain of requests to the origin
 endpoint, CloudFront returns a 403 error. We don't recommend placing one distribution
 in front of another.
