**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Intelligent threat API

specification

This section lists the specification for the methods and properties of the intelligent
threat mitigation JavaScript APIs. Use these APIs for intelligent threat and
CAPTCHA integrations.

**`AwsWafIntegration.fetch()`**

Sends the HTTP `fetch` request to the server using the AWS WAF integration
implementation.

**`AwsWafIntegration.getToken()`**

Retrieves the stored AWS WAF token and stores it in a cookie on the current page with
name `aws-waf-token`, and the value set to the token
value.

**`AwsWafIntegration.hasToken()`**

Returns a boolean indicating whether the `aws-waf-token` cookie currently
holds an unexpired token.

If you're also using the CAPTCHA integration, see the specification for that
at [CAPTCHA JavaScript API
specification](waf-js-captcha-api-specification.md "waf-js-captcha-api-specification.md").
