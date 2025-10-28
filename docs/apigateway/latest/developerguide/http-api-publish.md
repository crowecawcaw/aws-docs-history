# Publish HTTP APIs for customers to invoke

You can use stages and custom domain names to publish your API for clients to
invoke.

An API stage is a logical reference to a lifecycle state of your API (for example,
`dev`, `prod`, `beta`, or `v2`). Each stage
is a named reference to a deployment of the API and is made available for client
applications to call. You can configure different integrations and settings for each stage
of an API.

You can use custom domain names to provide a simpler, more intuitive URL for clients to
invoke your API than the default URL,
`https://`api-id`.execute-api.`region`.amazonaws.com/`stage``.

###### Note

To augment the security of your API Gateway APIs, the `execute-api.{`region`}.amazonaws.com` domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further security, we recommend that you use cookies with a `__Host-`
prefix if you ever need to set sensitive cookies in the default domain name for your API Gateway APIs. This practice will help to defend your domain against cross-site request
forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.

###### Topics

- [Stages for HTTP APIs in API Gateway](http-api-stages.md "http-api-stages.md")
- [Security policy for HTTP APIs in API Gateway](http-api-ciphers.md "http-api-ciphers.md")
- [Custom domain names for HTTP APIs in API Gateway](http-api-custom-domain-names.md "http-api-custom-domain-names.md")
