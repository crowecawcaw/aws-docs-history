**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using the JavaScript API with content security policies

This section provides an example configuration to allowlist the AWS WAF apex domain.

If you apply content security policies (CSP) to your resources, for your JavaScript
implementation to work, you need to allowlist the AWS WAF apex domain
`awswaf.com`. The JavaScript SDKs make calls to different AWS WAF
endpoints, so allowlisting this domain provides the permissions that the SDKs need
to operate.

The following shows an example configuration to allowlist the AWS WAF apex domain:

```
connect-src 'self' https://*.awswaf.com;
script-src 'self' https://*.awswaf.com;
script-src-elem 'self' https://*.awswaf.com;
```

If you try to use the JavaScript SDKs with resources that use CSP, and you haven't
allowlisted the AWS WAF domain, you'll receive errors like the following:

```
Refused to load the script ...awswaf.com/<> because it violates the following Content Security Policy directive: “script-src ‘self’
```
