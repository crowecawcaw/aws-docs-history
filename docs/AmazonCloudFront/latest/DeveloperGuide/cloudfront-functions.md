# Customize at the edge with CloudFront Functions

With CloudFront Functions, you can write lightweight functions in JavaScript for high-scale,
latency-sensitive CDN customizations. Your functions can manipulate the requests and
responses that flow through CloudFront, perform basic authentication and authorization, generate
HTTP responses at the edge, and more. The CloudFront Functions runtime environment offers
submillisecond startup times, scales immediately to handle millions of requests per second,
and is highly secure. CloudFront Functions is a native feature of CloudFront, which means you can build,
test, and deploy your code entirely within CloudFront.

When you associate a CloudFront function with a CloudFront distribution, CloudFront intercepts requests and
responses at CloudFront edge locations and passes them to your function. You can invoke
CloudFront Functions when the following events occur:

- When CloudFront receives a request from a viewer (viewer request)
- Before CloudFront returns the response to the viewer (viewer response)
- During TLS connection establishment (connection request) - currently available for mutual TLS (mTLS) connections
  For more information about CloudFront Functions, see the following topics:

###### Topics

- [Tutorial: Create a simple function with
  CloudFront Functions](functions-tutorial.md "functions-tutorial.md")
- [Tutorial: Create a CloudFront function that includes key
  values](functions-tutorial-kvs.md "functions-tutorial-kvs.md")
- [Write function code](writing-function-code.md "writing-function-code.md")
- [Create functions](create-function.md "create-function.md")
- [Test functions](test-function.md "test-function.md")
- [Update functions](update-function.md "update-function.md")
- [Publish functions](publish-function.md "publish-function.md")
- [Associate functions with distributions](associate-function.md "associate-function.md")
- [Amazon CloudFront KeyValueStore](kvs-with-functions.md "kvs-with-functions.md")
