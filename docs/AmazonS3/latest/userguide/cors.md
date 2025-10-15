# Using cross-origin resource sharing (CORS)

Cross-origin resource sharing (CORS) defines a way for client web applications that are
 loaded in one domain to interact with resources in a different domain. With CORS support, you can build rich client-side web applications with Amazon S3 and selectively allow
 cross-origin access to your Amazon S3 resources. 

This section provides an overview of CORS. The subtopics describe how you can enable CORS
 using the Amazon S3 console, or programmatically by using the Amazon S3 REST API and the AWS SDKs. 

## Cross-origin resource sharing: Use-case
 scenarios


The following are example scenarios for using CORS.


###### Scenario 1


Suppose that you are hosting a website in an Amazon S3 bucket named `website` as
 described in [Hosting a static website using Amazon S3](WebsiteHosting.md "WebsiteHosting.md"). Your users
 load the website endpoint:



```
http://website.s3-website.us-east-1.amazonaws.com
```

Now you want to use JavaScript on the webpages that are stored in this bucket to be able
 to make authenticated GET and PUT requests against the same bucket by using the Amazon S3 API
 endpoint for the bucket, `website.s3.us-east-1.amazonaws.com`. A browser would
 normally block JavaScript from allowing those requests, but with CORS you can configure your
 bucket to explicitly enable cross-origin requests from `website.s3-website.us-east-1.amazonaws.com`.


###### Scenario 2


Suppose that you want to host a web font
 from your S3 bucket. Again, browsers require a CORS check (also called a preflight check)
 for loading web fonts. You would configure the bucket that is hosting the web font to
 allow any origin to make these requests.


## How does Amazon S3 evaluate the CORS configuration on a
 bucket?


When Amazon S3 receives a preflight request from a browser, it evaluates the CORS configuration
 for the bucket and uses the first `CORSRule` rule that matches the incoming browser
 request to enable a cross-origin request. For a rule to match, the following conditions must
 be met:



* The `Origin` header in a CORS request to your bucket must match the origins in the
 `AllowedOrigins` element in your CORS configuration.
* The HTTP methods that are specified in the
 `Access-Control-Request-Method` in a CORS request to your bucket must
 match the method or methods listed in the `AllowedMethods` element in
 your CORS configuration.
* The headers listed in the `Access-Control-Request-Headers` header in a
 pre-flight request must match the headers in the `AllowedHeaders` element
 in your CORS configuration.

###### Note

The ACLs and policies continue to apply when you enable CORS on your bucket.


## How Object Lambda Access Point supports CORS


When S3 Object Lambda receives a request from a browser or the request includes an `Origin` header, S3 Object Lambda always adds an `"AllowedOrigins":"*"` header field.


For more information about using CORS, see the following topics.

###### Topics

* [Elements of a CORS configuration](ManageCorsUsing.md "ManageCorsUsing.md")
* [Configuring cross-origin resource sharing (CORS)](enabling-cors-examples.md "enabling-cors-examples.md")
* [Testing CORS](testing-cors.md "testing-cors.md")
* [Troubleshooting CORS](cors-troubleshooting.md "cors-troubleshooting.md")
