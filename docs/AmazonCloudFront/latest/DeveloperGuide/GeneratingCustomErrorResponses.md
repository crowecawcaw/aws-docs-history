# Generate custom error responses

If an object that you’re serving through CloudFront is unavailable for some reason, your web
server typically returns a relevant HTTP status code to CloudFront to indicate this. For example,
if a viewer requests an invalid URL, your web server returns an HTTP 404 (Not Found) status
code to CloudFront, and then CloudFront returns that status code to the viewer. Instead of using this
default error response, you can create a custom one that CloudFront returns to the viewer.

If you configure CloudFront to return a custom error page for an HTTP status code but the custom
error page isn’t available, CloudFront returns to the viewer the status code that CloudFront received
from the origin that contains the custom error pages. For example, suppose your custom
origin returns a 500 status code and you have configured CloudFront to get a custom error page for
a 500 status code from an Amazon S3 bucket. However, someone accidentally deleted the custom
error page from your Amazon S3 bucket. CloudFront returns an HTTP 404 status code (Not Found) to the
viewer that requested the object.

When CloudFront returns a custom error page to a viewer, you pay the standard CloudFront charges for
the custom error page, not the charges for the requested object. For more information about
CloudFront charges, see [Amazon CloudFront
Pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").

###### Topics

- [Configure error response behavior](custom-error-pages-procedure.md "custom-error-pages-procedure.md")
- [Create a custom error page for specific HTTP status codes](creating-custom-error-pages.md "creating-custom-error-pages.md")
- [Store objects and custom error pages in different locations](custom-error-pages-different-locations.md "custom-error-pages-different-locations.md")
- [Change response codes returned by CloudFront](custom-error-pages-response-code.md "custom-error-pages-response-code.md")
- [Control how long CloudFront caches errors](custom-error-pages-expiration.md "custom-error-pages-expiration.md")
