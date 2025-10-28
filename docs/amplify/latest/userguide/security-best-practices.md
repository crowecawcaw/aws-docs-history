# Security best practices for Amplify

Amplify provides a number of security features to consider as you develop and implement your own
security policies. The following best practices are general guidelines and don't represent a complete security
solution. Because these best practices might not be appropriate or sufficient for your
environment, treat them as helpful recommendations rather than prescriptions.

## Using cookies with the Amplify default domain

When you use Amplify to deploy a web app, Amplify hosts it for you on the default
`amplifyapp.com` domain. You can view your app on a URL formatted as
`https://branch-name.d1m7bkiki6tdw1.amplifyapp.com`.

To augment the security of your Amplify applications, the _amplifyapp.com_ domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further security, we recommend that you use cookies with a `__Host-`
prefix if you ever need to set sensitive cookies in the default domain name for your Amplify applications. This practice will help to defend your domain against cross-site request
forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.
