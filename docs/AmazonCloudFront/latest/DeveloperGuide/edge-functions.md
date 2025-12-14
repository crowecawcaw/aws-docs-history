# Customize at the edge with functions

With Amazon CloudFront, you can write your own code to customize how your CloudFront distributions
process HTTP requests and responses. The code runs close to your viewers (users) to minimize
latency, and you don’t have to manage servers or other infrastructure. You can write code to
manipulate the requests and responses that flow through CloudFront, perform basic authentication
and authorization, generate HTTP responses at the edge, and more.

The code that you write and attach to your CloudFront distribution is called an _edge function_. CloudFront provides two ways to write and manage edge
functions:

**CloudFront Functions**

You can write lightweight functions in JavaScript for high-scale,
latency-sensitive CDN customizations. The CloudFront Functions runtime environment
offers submillisecond startup times, scales immediately to handle millions of
requests per second, and is highly secure. CloudFront Functions is a native feature of
CloudFront, which means you can build, test, and deploy your code entirely within
CloudFront.

**Lambda@Edge**

Lambda@Edge is an extension of [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") that offers powerful and flexible computing for complex
functions and full application logic closer to your viewers, and is highly
secure. Lambda@Edge functions run in a Node.js or Python runtime environment. You
publish them to a single AWS Region, but when you associate the function with
a CloudFront distribution, Lambda@Edge automatically replicates your code around the
world.

If you run AWS WAF on CloudFront, you can use AWS WAF inserted headers for both CloudFront Functions and
Lambda@Edge. This works for viewer and origin requests and responses.

###### Topics

- [Differences between CloudFront Functions and
  Lambda@Edge](edge-functions-choosing.md "edge-functions-choosing.md")
- [Customize at the edge with CloudFront Functions](cloudfront-functions.md "cloudfront-functions.md")
- [Customize with CloudFront Connection Functions](customize-connections-validation-with-connection-functions.md "customize-connections-validation-with-connection-functions.md")
- [Customize at the edge with Lambda@Edge](lambda-at-the-edge.md "lambda-at-the-edge.md")
- [Restrictions on edge functions](edge-functions-restrictions.md "edge-functions-restrictions.md")
