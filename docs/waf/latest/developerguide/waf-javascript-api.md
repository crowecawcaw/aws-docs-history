**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF JavaScript integrations

This section explains how to use the AWS WAF JavaScript integrations.

You can use the JavaScript integration APIs to implement AWS WAF application integrations in
your browsers and other devices that execute JavaScript.

CAPTCHA puzzles and silent
challenges can only run when browsers are accessing HTTPS endpoints. Browser
clients must be running in secure contexts in order to acquire tokens.

- The intelligent threat APIs let you
  manage token authorization through a silent client-side browser challenge, and to include the tokens in the requests that you send to
  your protected resources.
- The CAPTCHA integration API adds to the intelligent threat APIs, and lets you customize the
  placement and characteristics of the CAPTCHA puzzle in your client
  applications. This API leverages the intelligent threat APIs to acquire AWS WAF
  tokens for use in the page after the end user successfully completes the
  CAPTCHA puzzle.
  By using these integrations, you ensure that the remote procedure calls by your client
  contain a valid token. When these integration APIs are in place on your application's pages,
  you can implement mitigating rules in your protection pack (web ACL), such as blocking requests that don't
  contain a valid token. You can also implement rules that enforce the use of the
  tokens that your client applications obtain, by using the Challenge or
  CAPTCHA actions in your rules.

###### Example implementation of intelligent threat APIs

The following listing shows basic components of a typical implementation of the
intelligent threat APIs in a web application page.

```
<head>
<script type="text/javascript" src="`protection pack (web ACL) integration URL`/challenge.js" defer></script>
</head>
<script>
const login_response = await AwsWafIntegration.fetch(login_url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: login_body
  });
</script>
```

###### Example implementation of CAPTCHA JavaScript API

The CAPTCHA integration API lets you customize your end users' CAPTCHA puzzle experience.
The CAPTCHA integration leverages the JavaScript intelligent threat
integration, for browser verification and token management, and adds a function for
configuring and rendering the CAPTCHA puzzle.

The following listing shows basic components of a typical implementation of the
CAPTCHA JavaScript API in a web application page.

```
<head>
    <script type="text/javascript" src="*<Integration URL>*/jsapi.js" defer></script>
</head>

<script type="text/javascript">
    function showMyCaptcha() {
        var container = document.querySelector("#my-captcha-container");

        AwsWafCaptcha.renderCaptcha(container, {
            apiKey: "...API key goes here...",
            onSuccess: captchaExampleSuccessFunction,
            onError: captchaExampleErrorFunction,
            ...other configuration parameters as needed...
        });
    }

    function captchaExampleSuccessFunction(wafToken) {
        // Use WAF token to access protected resources
        AwsWafIntegration.fetch("...WAF-protected URL...", {
            method: "POST",
            ...
        });
    }

    function captchaExampleErrorFunction(error) {
        /* Do something with the error */
    }
</script>

<div id="my-captcha-container">
    <!-- The contents of this container will be replaced by the captcha widget -->
</div>
```

###### Topics

- [Providing domains for use in the
  tokens](waf-js-challenge-api-set-token-domain.md "waf-js-challenge-api-set-token-domain.md")
- [Using the JavaScript API with content security policies](waf-javascript-api-csp.md "waf-javascript-api-csp.md")
- [Using the intelligent threat JavaScript API](waf-js-challenge-api.md "waf-js-challenge-api.md")
- [Using the CAPTCHA JavaScript API](waf-js-captcha-api.md "waf-js-captcha-api.md")
