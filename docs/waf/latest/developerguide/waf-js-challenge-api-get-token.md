**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How to use

the integration `getToken`

This section explains how to use the `getToken` operation.

AWS WAF requires your requests to protected endpoints to include the cookie named
`aws-waf-token` with the value of your current token.

The `getToken` operation is an asynchronous API call that retrieves the
AWS WAF token and stores it in a cookie on the current page with name
`aws-waf-token`, and the value set to the token value. You can use
this token cookie as needed in your page.

When you call `getToken`, it does the following:

- If an unexpired token is already available, the call returns it
  immediately.
- Otherwise, the call retrieves a new token from the token provider, waiting for up to 2
  seconds for the token acquisition workflow to complete before timing out. If
  the operation times out, it throws an error, which your calling code must
  handle.
  The `getToken` operation has an accompanying `hasToken`
  operation, which indicates whether the `aws-waf-token` cookie currently
  holds an unexpired token.

`AwsWafIntegration.getToken()` retrieves a valid token and stores
it as a cookie. Most client calls automatically attach this cookie, but some
don't. For example, calls made across host domains don't attach the cookie. In
the implementation details that follow, we show how to work with both types of
client calls.

###### Basic `getToken` implementation, for calls that attach the

`aws-waf-token` cookie

The following example listing shows standard code for implementing the
`getToken` operation with a login request.

```
const login_response = await AwsWafIntegration.getToken()
	    .catch(e => {
	        // Implement error handling logic for your use case
	    })
	    // The getToken call returns the token, and doesn't typically require special handling
	    .then(token => {
	        return loginToMyPage()
	    })

	async function loginToMyPage() {
	    // Your existing login code
	}
```

###### Submit form only after token is available from `getToken`

The following listing shows how to register an event listener to intercept
form submissions until a valid token is available for use.

```
<body>
	  <h1>Login</h1>
	  <p></p>
	  <form id="login-form" action="/web/login" method="POST" enctype="application/x-www-form-urlencoded">
	    <label for="input_username">USERNAME</label>
	    <input type="text" name="input_username" id="input_username"><br>
	    <label for="input_password">PASSWORD</label>
	    <input type="password" name="input_password" id="input_password"><br>
	    <button type="submit">Submit<button>
	  </form>

	<script>
	  const form = document.querySelector("#login-form");

	  // Register an event listener to intercept form submissions
	  form.addEventListener("submit", (e) => {
	      // Submit the form only after a token is available
	      if (!AwsWafIntegration.hasToken()) {
	          e.preventDefault();
	          AwsWafIntegration.getToken().then(() => {
	              e.target.submit();
	          }, (reason) => { console.log("Error:"+reason) });
	        }
	    });
	</script>
	</body>
```

###### Attaching the token when your client doesn't attach the `aws-waf-token`

cookie by default

`AwsWafIntegration.getToken()` retrieves a valid token and stores it as a cookie, but not all client calls attach this cookie by default. For example, calls made across host domains don't attach the cookie.

The `fetch` wrapper handles these cases automatically, but if you aren't able to use the `fetch` wrapper, you can handle this by using a custom `x-aws-waf-token` header. AWS WAF reads tokens from this header, in addition to reading them from the `aws-waf-token` cookie. The following code shows an example of setting the header.

```
const token = await AwsWafIntegration.getToken();
const result = await fetch('/url', {
    headers: {
        'x-aws-waf-token': token,
    },
});
```

By default, AWS WAF only accepts tokens that contain the same domain as the requested host domain. Any cross-domain tokens require corresponding entries in the protection pack (web ACL) token domain list. For more information, see [AWS WAF protection pack (web ACL) token domain list configuration](waf-tokens-domains.md#waf-tokens-domain-lists "waf-tokens-domains.md#waf-tokens-domain-lists").

For additional information about cross-domain token use, see
[aws-samples/aws-waf-bot-control-api-protection-with-captcha](https://github.com/aws-samples/aws-waf-bot-control-api-protection-with-captcha "https://github.com/aws-samples/aws-waf-bot-control-api-protection-with-captcha").
