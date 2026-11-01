

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Automatic SDK integration for CloudFront distributions
<a name="waf-challenge-javascript-sdk-injection"></a>

Several AWS WAF protections rely on client-side signals that the AWS WAF JavaScript SDK collects in the browser. These protections include the targeted protection level of Bot Control and the AWS WAF Fraud Control managed rule groups.

You typically add the SDK to your application by adding a script tag to your web pages, as described in [Client application integrations in AWS WAF](waf-application-integration.md).

For applications that you deliver through Amazon CloudFront, you can have CloudFront insert that script tag for you. This is called **automatic SDK integration**. When you turn it on for a CloudFront web ACL, CloudFront inserts the SDK script tag into your HTML at the edge. You don't change your application code or your build process.

Turning on automatic SDK integration also changes how CloudFront requests every object for the distributions that the web ACL protects, not only HTML pages. Before you turn it on, review [When pages don't receive the tag](#waf-challenge-javascript-sdk-injection-not-inserted) and [Considerations and limitations](#waf-challenge-javascript-sdk-injection-considerations).

**Note**  
This setting inserts the AWS WAF SDK script tag only. It doesn't insert the CAPTCHA JavaScript API or the mobile SDKs. If your application needs those, integrate them as described in [Client application integrations in AWS WAF](waf-application-integration.md).

## Requirements
<a name="waf-challenge-javascript-sdk-injection-requirements"></a>

To use automatic SDK integration, all of the following must be true:
+ **The web ACL uses the CloudFront scope** – This setting isn't available for regional resources. It applies only to web ACLs that use the CloudFront scope, which appear under **Global (CloudFront)** in the console. For more information, see [Using AWS WAF with Amazon CloudFront](cloudfront-features.md).
+ **The web ACL contains a qualifying managed rule group** – The SDK provides signals that only some protections use. The web ACL must contain at least one of the following:
  + The Bot Control managed rule group `AWSManagedRulesBotControlRuleSet`, with the inspection level set to targeted. The common inspection level doesn't qualify, because it doesn't use client-side signals.
  + The AWS WAF Fraud Control account takeover prevention (ATP) managed rule group `AWSManagedRulesATPRuleSet`.
  + The AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group `AWSManagedRulesACFPRuleSet`.

  The version of the Bot Control rule group doesn't affect qualification, as long as the inspection level is targeted.

  AWS WAF checks only that a qualifying rule group is present in the web ACL. Overriding the rule group's actions to count doesn't affect qualification, so you can add the SDK while you evaluate the rule group, before you enforce it.

**Important**  
Keep a qualifying rule group in the web ACL while this setting is on. If you remove the last qualifying rule group, or change the Bot Control inspection level to common, remove this setting in the same update. Otherwise, AWS WAF rejects the update.

## When pages don't receive the tag
<a name="waf-challenge-javascript-sdk-injection-not-inserted"></a>

In the following cases, pages might not receive the script tag, even when a response meets the other conditions in this topic.
+ **Uncached requests at high request rates** – When your origin receives a high rate of requests from CloudFront, CloudFront might return some responses without inserting the script tag. This applies only to requests that CloudFront doesn't cache, such as `POST` requests or requests to a cache behavior with a maximum time to live (TTL) of 0. Those responses work normally, but the SDK isn't inserted into them. If your application depends on the SDK to attach tokens to its own API calls, such as a single-page application, integrate the SDK directly into your pages. For more information, see [Using the intelligent threat JavaScript API](waf-js-challenge-api.md).
+ **Origin Shield** – Automatic SDK integration doesn't support CloudFront Origin Shield. When an origin has Origin Shield turned on, the script tag isn't inserted consistently into responses from that origin, and a cached response without the tag continues to be served until it expires. For these origins, integrate the SDK directly into your pages. For more information, see [Using the intelligent threat JavaScript API](waf-js-challenge-api.md).
+ **Lambda@Edge functions on origin events** – Automatic SDK integration doesn't support cache behaviors that have a Lambda@Edge function on the origin request or origin response event. Functions on viewer events don't affect insertion into responses from your origin. For these cache behaviors, integrate the SDK directly into your pages. For more information, see [Using the intelligent threat JavaScript API](waf-js-challenge-api.md).
+ **Embedded POPs** – If your distribution is opted in to CloudFront embedded points of presence (POPs), CloudFront doesn't insert the script tag into uncached responses that embedded POPs serve. For these distributions, integrate the SDK directly into your pages. For more information, see [Using the intelligent threat JavaScript API](waf-js-challenge-api.md).
+ **Browser and downstream caches** – Browsers and other caches between CloudFront and the viewer keep the copy of a page that they already hold. If a page hasn't changed at your origin, a conditional request for it can return a `304` status, and the viewer keeps a copy that was stored before you turned the setting on. Invalidating the CloudFront cache doesn't clear these caches.

Those pages work normally, but they don't run the SDK. Without the SDK, a page doesn't acquire or refresh a token, so requests from it might not carry one. Rules that act on a missing token can then match requests from legitimate users.

No metric or log field records whether CloudFront inserted the tag into a response. To confirm that the tag is present, view the page source in a private browsing window, or after you clear your browser cache and cookies, so that you don't see a copy that your browser stored earlier. To confirm that the SDK runs, check that your browser receives the `aws-waf-token` cookie. Before you enforce rules that act on a missing token, set their actions to count and review the results. For pages that must always include the SDK, integrate the SDK directly into those pages. You can do this alongside automatic SDK integration.

## Enabling automatic SDK integration
<a name="waf-challenge-javascript-sdk-injection-enabling"></a>

In the console, you turn this on from any qualifying managed rule group. Add or edit the rule group in a CloudFront web ACL. Then, under **Automatic SDK integration**, select **Enable automatic SDK integration**. For Bot Control, the setting is in the same panel where you set the inspection level and machine learning.

Through the API, add the `ChallengeJavascriptSdkInjection` setting to the `AssociationConfig` of the web ACL, using the `CLOUDFRONT` map key. The configuration object is empty. The following example shows the setting in a `CreateWebACL` or `UpdateWebACL` request.

```
"AssociationConfig": {
    "ChallengeJavascriptSdkInjection": {
        "CLOUDFRONT": {}
    }
}
```

To turn automatic SDK integration off for a web ACL that uses it, remove the setting and update the web ACL. An `UpdateWebACL` request that doesn't include the setting turns automatic SDK integration off. This applies even if you turned the setting on in the console.

**Important**  
The starting state depends on how you create the web ACL:  
Automatic SDK integration is turned on by default when you create a new CloudFront web ACL with a qualifying rule group in the console. To turn it off, clear **Enable automatic SDK integration** before you save the web ACL.
When you create a web ACL programmatically, for example through the AWS WAF API, automatic SDK integration is off. Omitting the `ChallengeJavascriptSdkInjection` setting leaves it off.
When you add a qualifying rule group to an existing web ACL, automatic SDK integration stays off. This includes web ACLs that you created before this feature was introduced. Turn the setting on yourself when you're ready to use it.

After you turn the setting on, load one of your pages in a private browsing window and view the page source to confirm that the script tag is present. To confirm that the SDK runs, check that your browser receives the `aws-waf-token` cookie. A private window keeps your browser from showing you a copy that it stored before the change. If your distribution caches HTML, you might also see a copy that CloudFront cached before the change. To see the change right away, invalidate the cached paths.

CloudFront inserts the same script tag that you add for a manual integration. The tag currently has the following form:

```
<script type="text/javascript" src="{{protection pack (web ACL) integration URL}}/challenge.js" defer></script>
```

The tag points to your web ACL's integration URL. You can find this URL on the **Application integration** page of the AWS WAF console, or in the `ApplicationIntegrationURL` field that `GetWebACL` returns. The `defer` attribute means that the script doesn't block the browser from parsing the rest of the page.

**Note**  
This example describes current behavior and can change. Don't write application logic, tests, or security policy that depends on the exact attributes, host, or path. To allow the script under a Content Security Policy, allowlist `https://*.awswaf.com` as described in [Using the JavaScript API with content security policies](waf-javascript-api-csp.md), rather than matching the full URL.

For the API specifications, see [AssociationConfig](https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociationConfig.html) in the *AWS WAF API Reference*.

## Considerations and limitations
<a name="waf-challenge-javascript-sdk-injection-considerations"></a>

Review the following before you turn on automatic SDK integration, so that you know when it applies to a response and when it doesn't.

Only successful, uncompressed HTML responses are modified  
CloudFront inserts the script tag only into responses that it serves with an HTTP `200` status and a `Content-Type` of `text/html`. Responses for images, style sheets, scripts, JSON, and other content types don't receive the tag. Custom error responses that CloudFront serves with a `200` status are modified like any other page. This includes the fallback page that many single-page applications use for deep links.  
To insert the tag, CloudFront requests objects from your origin uncompressed. This applies to every request that AWS WAF allows, not only to requests for HTML pages. To keep serving compressed objects to viewers, turn on compression in the cache behavior so that CloudFront compresses objects before it serves them. For more information, see [Serving compressed files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html) in the *Amazon CloudFront Developer Guide*.  
If your origin returns compressed content anyway, CloudFront doesn't insert the SDK. This includes HTML that's stored compressed at your origin, such as files that you upload to Amazon S3 with `Content-Encoding: gzip`.

The response must have a head element near the top  
CloudFront inserts the script tag inside the `head` element, immediately after the opening `head` tag. It scans only the first few kilobytes of the response body to find that tag. Insertion doesn't happen if the response has no `head` element, or if the `head` element appears too far into the document.  
Detection is a fast byte scan rather than a full HTML parse. A commented-out or otherwise invalid `head` earlier in the document can therefore cause the tag to be placed there instead. When this happens, the browser doesn't run the inserted tag, so the page doesn't get a token. Only ASCII-compatible encodings are supported. Documents in encodings such as UTF-16 or UTF-32 aren't modified.

Responses that opt out of transformation aren't modified  
If a response includes the `Cache-Control: no-transform` header, CloudFront leaves it unchanged and doesn't insert the SDK. Use this header to keep the tag off specific pages.  
Other `Cache-Control` directives don't have this effect. For example, responses marked `no-store` or `private`, which are common on sign-in and account pages, still receive the tag.

Cached responses keep the version they were stored with  
If your cache behavior caches HTML responses, CloudFront serves the copy that's already in the cache. Copies stored before you turned the setting on don't contain the script tag, and copies stored before you turned it off still do. Each copy is replaced when it expires or is evicted, so the change takes effect over time without any action from you.  
To make the change take effect right away, invalidate the cached HTML paths in your distribution. For information about invalidation, see [Invalidating files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) in the *Amazon CloudFront Developer Guide*.

Only responses from your origin are modified  
Insertion happens on responses to requests that AWS WAF lets through. Requests that match rules set to count are allowed through and are handled like any other allowed request.  
A request that a rule blocks doesn't reach your origin, so there's no page to insert the SDK into. The same applies to a request that receives a `CAPTCHA` or `Challenge` action. The viewer receives the CAPTCHA puzzle or challenge response instead of your page. After the viewer completes it, the pages that follow receive the tag as usual.  
Responses that AWS WAF or CloudFront generates in place of your origin aren't modified either. These include custom responses for block actions, even when they're HTML, and responses that CloudFront Functions generate.

Insertion applies across the web ACL  
The setting applies to the whole web ACL, and you can't limit it to specific paths. When it's on, CloudFront inserts the tag into eligible responses for any request that AWS WAF allows.  
Insertion doesn't depend on whether a qualifying rule group evaluated the request. For example, scope-down statements on the rule group, and rules that allow a request before the rule group runs, don't prevent insertion. To keep the tag off specific pages, have your origin send `Cache-Control: no-transform` for them.

Range requests return the whole object  
When the setting is on, CloudFront removes the `Range` and `If-Range` headers from requests that AWS WAF allows, for every content type, and returns the complete object with an HTTP `200` status. This affects video and audio players, download managers, and other clients that request objects in parts, and it increases data transfer for those requests.  
For HTML pages, a tool might start a download while the setting is on, and resume it after you turn the setting off. The result can combine content from before and after the change. To get a correct copy, request the page again in full.

Content Security Policy must allow the SDK  
Your pages might set a Content Security Policy in a `Content-Security-Policy` response header or in a `meta` element. Either way, the policy must allow the SDK to load and to make its requests. Allowlist `https://*.awswaf.com`, which covers the domains that the challenge and CAPTCHA scripts use. Add it to each directive shown in [Using the JavaScript API with content security policies](waf-javascript-api-csp.md). Otherwise, the browser blocks the script, or loads it and blocks its requests, and the SDK can't get a token.  
Automatic SDK integration doesn't support policies that use `'strict-dynamic'` with nonces or hashes. Under these policies, browsers ignore allowlisted hosts, and the inserted tag doesn't carry your nonce, so the browser blocks it. For pages that use such a policy, add the script tag yourself with your nonce. The inserted copy is still blocked and might appear in your policy's violation reports.

Applications that attach tokens to their own API calls  
The inserted SDK acquires a token shortly after the page loads, and then keeps it refreshed. Requests that your application sends before the first token exists don't carry one.  
Your application might depend on the SDK to attach tokens to its own API calls, such as a single-page application. If it does, continue using your existing SDK integration. If you don't have one, integrate the SDK as described in [Using the intelligent threat JavaScript API](waf-js-challenge-api.md).

Insertion fails open  
If the SDK can't be inserted for any reason, CloudFront returns the response body as your origin sent it. The feature never blocks a response.

Adding the SDK manually is still safe  
The SDK runs once, even if a page includes it more than once. Enabling this setting for an application that already includes the SDK doesn't break the application.

Some response headers change after insertion  
After CloudFront inserts the script tag, it updates the `Content-Length` header to match the new body, or omits the header for chunked responses. It also replaces the `ETag` header with a weak validator that differs from the value your origin sent. Clients and tools that compare a response's `ETag` with the origin's value see the difference.  
CloudFront doesn't recompute body-integrity headers such as `Content-MD5`, `Digest`, `Content-Digest`, or `Repr-Digest`. Their values continue to reflect the response before insertion.

Proxied token endpoints aren't supported  
If you proxy the SDK's requests through your own domain instead of letting the browser call `awswaf.com` directly, the proxy isn't used. The inserted tag references the AWS WAF domain rather than your proxy.