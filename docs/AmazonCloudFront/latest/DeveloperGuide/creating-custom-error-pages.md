# Create a custom error page for specific
 HTTP status codes

If you’d rather display a custom error message instead of the default
 message—for example, a page that uses the same formatting as the rest of your
 website—you can have CloudFront return to the viewer an object (such as an HTML file)
 that contains your custom error message.

To specify the file that you want to return and the errors for which the file should
 be returned, you update your CloudFront distribution to specify those values. For more
 information, see [Configure error response
 behavior](custom-error-pages-procedure.md "custom-error-pages-procedure.md").

For example, the following is a custom error page:


![Screenshot of an example custom AWS 404 page.](images/custom-error-page-aws-404-example.png)
You can specify a different object for each supported HTTP status code, or you can use
 the same object for all of the supported status codes. You can choose to specify custom
 error pages for some status codes and not for others.

The objects that you’re serving through CloudFront can be unavailable for a variety of
 reasons. These fall into two broad categories:


* *Client errors* indicate a problem with the
 request. For example, an object with the specified name isn’t available, or the
 user doesn’t have the permissions required to get an object in your Amazon S3 bucket.
 When a client error occurs, the origin returns an HTTP status code in the 4xx
 range to CloudFront.
* *Server errors* indicate a problem with the
 origin server. For example, the HTTP server is busy or unavailable. When a
 server error occurs, either your origin server returns an HTTP status code in
 the 5xx range to CloudFront, or CloudFront doesn’t get a response from your origin server
 for a certain period of time and assumes a 504 status code (Gateway
 Timeout).
The HTTP status codes for which CloudFront can return a custom error page include the
 following:


* 400, 403, 404, 405, 414, 416
* 500, 501, 502, 503, 504


###### Notes



	+ If CloudFront detects that the request might be unsafe, CloudFront returns a
	 400 (Bad Request) error instead of a custom error page.
	+ You can create a custom error page for HTTP status code 416
	 (Requested Range Not Satisfiable), and you can change the HTTP
	 status code that CloudFront returns to viewers when your origin returns a
	 status code 416 to CloudFront. For more information, see [Change response codes returned by
	 CloudFront](custom-error-pages-response-code.md "custom-error-pages-response-code.md"). However,
	 CloudFront doesn't cache status code 416 responses, so even if you
	 specify a value for **Error Caching Minimum TTL**
	 for status code 416, CloudFront doesn't use it.
	+ In some cases, CloudFront doesn’t return a custom error page for the
	 HTTP 503 status code even if you configure CloudFront to do so. If the
	 CloudFront error code is `Capacity Exceeded` or `Limit
	 Exceeded`, CloudFront returns a 503 status code to the viewer
	 without using your custom error page.
	+ If you created a custom error page, CloudFront will return
	 `Connection: close` or `Connection:
	 keep-alive` for the following response codes:
	
	
	
	
		- CloudFront returns `Connection: close` for status
		 codes: 400, 405, 414, 416, 500, 501
		- CloudFront returns `Connection: keep-alive` for
		 status codes: 403, 404, 502, 503, 504
For a detailed explanation of how CloudFront handles error responses from your origin, see
 [How CloudFront processes HTTP 4xx and 5xx status codes from
 your origin](HTTPStatusCodes.md "HTTPStatusCodes.md").
