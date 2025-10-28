**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Handling a CAPTCHA

response from AWS WAF

This section provides an example of handling a CAPTCHA
response.

An AWS WAF rule with a CAPTCHA action terminates the evaluation of a matching web
request if the request doesn't have a token with a valid CAPTCHA timestamp. If
the request is a `GET` text/html call, the CAPTCHA action
then serves the client an interstitial with a CAPTCHA puzzle. When you don't
integrate the CAPTCHA JavaScript API, the interstitial runs the puzzle and, if
the end user successfully solves it, automatically resubmits the request.

When you integrate the CAPTCHA JavaScript API and customize your CAPTCHA handling, you
need to detect the terminating CAPTCHA response, serve your custom CAPTCHA,
and then if the end user successfully solves the puzzle, resubmit the client's
web request.

The following code example shows how to do this.

###### Note

The AWS WAF CAPTCHA action response has a status code of HTTP 405,
which we use to recognize the CAPTCHA response in this code. If your
protected endpoint uses an HTTP 405 status code to communicate any other
type of response for the same call, this example code will render a
CAPTCHA puzzle for those responses as well.

```
<!DOCTYPE html>
<html>
<head>
    <script type="text/javascript" src="<Integration URL>/jsapi.js" defer></script>
</head>
<body>
    <div id="my-captcha-box"></div>
    <div id="my-output-box"></div>

    <script type="text/javascript">
    async function loadData() {
        // Attempt to fetch a resource that's configured to trigger a CAPTCHA
        // action if the rule matches. The CAPTCHA response has status=HTTP 405.
        const result = await AwsWafIntegration.fetch("/protected-resource");

        // If the action was CAPTCHA, render the CAPTCHA and return

        // NOTE: If the endpoint you're calling in the fetch call responds with HTTP 405
        // as an expected response status code, then this check won't be able to tell the
        // difference between that and the CAPTCHA rule action response.

        if (result.status === 405) {
            const container = document.querySelector("#my-captcha-box");
            AwsWafCaptcha.renderCaptcha(container, {
                apiKey: "...API key goes here...",
                onSuccess() {
                    // Try loading again, now that there is a valid CAPTCHA token
                    loadData();
                },
            });
            return;
        }

        const container = document.querySelector("#my-output-box");
        const response = await result.text();
        container.innerHTML = response;
    }

    window.addEventListener("load", () => {
        loadData();
    });
    </script>
</body>
</html>
```
