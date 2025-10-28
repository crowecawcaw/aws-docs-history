**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# CAPTCHA and Challenge action behavior

This section explains what the CAPTCHA and Challenge actions do.

When a web request matches the inspection criteria of a rule with CAPTCHA or
Challenge action, AWS WAF determines how to handle the request according to
the state of its token and immunity time configuration. AWS WAF also considers whether
the request can handle the CAPTCHA puzzle or challenge script interstitials. The scripts are
designed to be handled as HTML content, and they can only be handled properly by a
client that's expecting HTML content.

###### Note

You are charged additional fees when you use the CAPTCHA or Challenge rule action in one of your rules or as a rule action override in a rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### How the action handles the web request

AWS WAF applies the CAPTCHA or Challenge action to a web request
as follows:

- **Valid token** – AWS WAF handles this similar to a
  Count action. AWS WAF applies any labels and request customizations
  that you've configured for the rule action, and then continues evaluating
  the request using the remaining rules in the protection pack (web ACL).
- **Missing, invalid, or expired token** – AWS WAF discontinues the protection pack (web ACL) evaluation
  of the request and blocks it from going to its intended destination.

AWS WAF generates a response that it sends back to the client, according to the rule action type:

    + **Challenge** – AWS WAF
     includes the following in the response:




    	- The header `x-amzn-waf-action` with a value of
    	 `challenge`.


    	###### Note

    	For Javascript applications running in the client browser, this header is only available within the
    	 application's domain. The header isn't available for cross-domain retrieval. For details, see the section that follows.
    	- The HTTP status code `202 Request
    	 Accepted`.
    	- If the request contains an `Accept` header with
    	 a value of `text/html`, the response includes a
    	 JavaScript page interstitial with a challenge script.
    + **CAPTCHA** – AWS WAF includes the following
     in the response:




    	- The header `x-amzn-waf-action` with a value of
    	 `captcha`.


    	###### Note

    	For Javascript applications running in the client browser, this header is only available within the
    	 application's domain. The header isn't available for cross-domain retrieval. For details, see the section that follows.
    	- The HTTP status code `405 Method Not Allowed`.
    	- If the request contains an `Accept` header with a value of
    	 `text/html`, the response includes a
    	 JavaScript page interstitial with a CAPTCHA script.

To configure the timing of token expiration at the protection pack (web ACL) or rule level, see [Setting timestamp expiration and token immunity times in AWS WAF](waf-tokens-immunity-times.md "waf-tokens-immunity-times.md").

###### Headers are unavailable to JavaScript applications that run in the client

browser

When AWS WAF responds to a client request with a CAPTCHA or challenge
response, it doesn't include cross-origin resource sharing (CORS) headers. CORS
headers are a set of access control headers that tell the client web browser
which domains, HTTP methods, and HTTP headers can be used by JavaScript
applications. Without CORS headers, JavaScript applications running in a client
browser are not granted access to HTTP headers and so are unable to read the
`x-amzn-waf-action` header that's provided in the CAPTCHA
and Challenge responses.

###### What the challenge and CAPTCHA interstitials do

When a challenge interstitial runs, after the client responds successfully, if
it doesn't already have a token, the interstitial initializes one for it. Then
it updates the token with the challenge solve timestamp.

When a CAPTCHA interstitial runs, if the client doesn't have a token yet, the
CAPTCHA interstitial invokes the challenge script first to challenge the browser
and initialize the token. Then the interstitial runs its CAPTCHA puzzle. When the
end user successfully completes the puzzle, the interstitial updates the token with
the CAPTCHA solve timestamp.

In either case, after the client responds successfully and the script updates the
token, the script resubmits the original web request using the updated token.

You can configure how AWS WAF handles tokens. For information, see [Token use in AWS WAF intelligent threat mitigation](waf-tokens.md "waf-tokens.md").
