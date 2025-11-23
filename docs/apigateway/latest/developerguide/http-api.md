# API Gateway HTTP APIs

REST APIs and HTTP APIs are both RESTful API products. REST APIs support more features
than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower
price. For more information, see [Choose between REST APIs and HTTP APIs](http-api-vs-rest.md "http-api-vs-rest.md").

You can use HTTP APIs to send requests to AWS Lambda functions or
to any routable HTTP endpoint. For example, you can create an HTTP API that integrates with a Lambda function on the
backend. When a client calls your API, API Gateway sends the request to the Lambda function and
returns the function's response to the client.

HTTP APIs support [OpenID Connect](https://openid.net/developers/how-connect-works/ "https://openid.net/developers/how-connect-works/") and
[OAuth 2.0](https://oauth.net/2/ "https://oauth.net/2/") authorization. They come with
built-in support for cross-origin resource sharing (CORS) and automatic deployments.

You can create HTTP APIs by using the AWS Management Console, the AWS CLI, APIs,
CloudFormation, or SDKs.

###### Topics

- [Develop HTTP APIs in API Gateway](http-api-develop.md "http-api-develop.md")
- [Publish HTTP APIs for customers to invoke](http-api-publish.md "http-api-publish.md")
- [Protect your HTTP APIs in API Gateway](http-api-protect.md "http-api-protect.md")
- [Monitor HTTP APIs in API Gateway](http-api-monitor.md "http-api-monitor.md")
- [Troubleshooting issues with HTTP APIs in API Gateway](http-api-troubleshooting.md "http-api-troubleshooting.md")
