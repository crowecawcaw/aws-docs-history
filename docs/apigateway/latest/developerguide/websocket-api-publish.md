# Publish WebSocket APIs for customers to invoke

Simply creating and developing an API Gateway API doesn't automatically make it callable by your
users. To make it callable, you must deploy your API to a stage. In addition, you might want
to customize the URL that your users will use to access your API. You can give it a domain
that is consistent with your brand or is more memorable than the default URL for your
API.

In this section, you can learn how to deploy your API and customize the URL that you
provide to users to access it.

###### Note

To augment the security of your API Gateway APIs, the `execute-api.{`region`}.amazonaws.com` domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further security, we recommend that you use cookies with a `__Host-`
prefix if you ever need to set sensitive cookies in the default domain name for your API Gateway APIs. This practice will help to defend your domain against cross-site request
forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.

###### Topics

- [Create stages for WebSocket APIs in API Gateway](websocket-api-stages.md "websocket-api-stages.md")
- [Deploy WebSocket APIs in API Gateway](apigateway-set-up-websocket-deployment.md "apigateway-set-up-websocket-deployment.md")
- [Security policy for WebSocket APIs in API Gateway](websocket-api-ciphers.md "websocket-api-ciphers.md")
- [Custom domain names for WebSocket APIs in API Gateway](websocket-api-custom-domain-names.md "websocket-api-custom-domain-names.md")
