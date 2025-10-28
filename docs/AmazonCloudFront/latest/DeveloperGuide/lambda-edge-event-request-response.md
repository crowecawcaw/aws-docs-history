# How Lambda@Edge works with requests

and responses

When you associate a CloudFront distribution with a Lambda@Edge function, CloudFront intercepts
requests and responses at CloudFront edge locations. You can execute Lambda functions when the
following CloudFront events occur:

- When CloudFront receives a request from a viewer (viewer request)
- Before CloudFront forwards a request to the origin (origin request)
- When CloudFront receives a response from the origin (origin response)
- Before CloudFront returns the response to the viewer (viewer response)
  If you're using AWS WAF, the Lambda@Edge viewer request is executed after any AWS WAF rules
  are applied.

For more information, see [Work with requests and
responses](lambda-generating-http-responses.md "lambda-generating-http-responses.md") and [Lambda@Edge event structure](lambda-event-structure.md "lambda-event-structure.md").
