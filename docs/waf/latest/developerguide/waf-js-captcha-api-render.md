**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How to render

the CAPTCHA puzzle

This section provides an example `renderCaptcha` implementation.

You can use the AWS WAF `renderCaptcha` call where you want to in your client
interface. The call retrieves a CAPTCHA puzzle from AWS WAF, renders it, and
sends the results to AWS WAF for verification. When you make the call, you provide the puzzle rendering configuration
and the callbacks that you want to run when your end users complete the puzzle.
For details about the options, see the preceding section,
[CAPTCHA JavaScript API
specification](waf-js-captcha-api-specification.md "waf-js-captcha-api-specification.md").

Use this call in conjunction with the token management functionality of the
intelligent threat integration APIs. This call gives your client a token that
verifies the successful completion of the CAPTCHA puzzle. Use the intelligent
threat integration APIs to manage the token and to provide the token in your client's
calls to the endpoints that are protected with AWS WAF protection packs (web ACLs). For information
about the intelligent threat APIs, see [Using the intelligent threat JavaScript API](waf-js-challenge-api.md "waf-js-challenge-api.md").

###### Example implementation

The following example listing shows a standard CAPTCHA implementation, including the
placement of the AWS WAF integration URL in the `<head>`
section.

This listing configures the `renderCaptcha` function with a success callback
that uses the `AwsWafIntegration.fetch` wrapper of the intelligent
threat integration APIs. For information about this function, see
[How to use the integration fetch wrapper](waf-js-challenge-api-fetch-wrapper.md "waf-js-challenge-api-fetch-wrapper.md").

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
        // Captcha completed. wafToken contains a valid WAF token. Store it for
        // use later or call AwsWafIntegration.fetch() to use it easily.
        // It will expire after a time, so calling AwsWafIntegration.getToken()
        // again is advised if the token is needed later on, outside of using the
        // fetch wrapper.

        // Use WAF token to access protected resources
        AwsWafIntegration.fetch("...WAF-protected URL...", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: "{ ... }" /* body content */
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

###### Example configuration settings

The following example listing shows the `renderCaptcha` with non-default
settings for the width and the title options.

```

        AwsWafCaptcha.renderCaptcha(container, {
            apiKey: "...API key goes here...",
            onSuccess: captchaExampleSuccessFunction,
            onError: captchaExampleErrorFunction,
            dynamicWidth: true,
            skipTitle: true
        });
```

For full information about the configuration options, see [CAPTCHA JavaScript API
specification](waf-js-captcha-api-specification.md "waf-js-captcha-api-specification.md").
