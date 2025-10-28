**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Managing API keys for the JS CAPTCHA API

This section provides instructions for generating and deleting API keys.

To integrate AWS WAF CAPTCHA into a a client application with the JavaScript API, you need
the JavaScript API integration tag and the encrypted API key for the client
domain where you want to run your CAPTCHA puzzle.

The CAPTCHA application integration for JavaScript uses the encrypted API keys to verify
that the client application domain has permission to use the AWS WAF CAPTCHA
API. When you call the CAPTCHA API from your JavaScript client, you provide an
API key with a domain list that includes a domain for the current client. You
can list up to 5 domains in a single encrypted key.

###### API key requirements

The API key that you use in your CAPTCHA integration must contain a
domain that applies to the client where you use the key.

- If you specify a `window.awsWafCookieDomainList` in your
  client's intelligent threat integration, then at least one domain in
  your API key must be an exact match for one of the token domains in
  `window.awsWafCookieDomainList` or it must be the apex
  domain of one of those token domains.

For example, for the token domain `mySubdomain.myApex.com`,
the API key `mySubdomain.myApex.com`
is an exact match and the API key `myApex.com` is the apex domain. Either key
matches the token domain.

For information about the setting the token domain list, see
[Providing domains for use in the
tokens](waf-js-challenge-api-set-token-domain.md "waf-js-challenge-api-set-token-domain.md").

- Otherwise, the current domain must be contained in the API key. The
  current domain is the domain that you can see in the browser address
  bar.
  The domains that you use must be ones that AWS WAF will accept, based on the
  protected host domain and the token domain list that's configured for the web
  ACL. For more information, see [AWS WAF protection pack (web ACL) token domain list configuration](waf-tokens-domains.md#waf-tokens-domain-lists "waf-tokens-domains.md#waf-tokens-domain-lists").

###### How to choose the Region for your API key

AWS WAF can generate CAPTCHA API keys in any Region where AWS WAF is available.

As a general rule, you should use the same Region for your CAPTCHA API key as you use for your protection pack (web ACL). If you expect a global audience for a regional protection pack (web ACL), however, you can obtain a CAPTCHA JavaScript integration tag that's scoped to CloudFront and an API key that's scoped to CloudFront, and use them with a regional protection pack (web ACL). This approach allows clients to load a CAPTCHA puzzle from the Region that's closest to them, which reduces latency.

CAPTCHA API keys that are scoped to Regions other than CloudFront are not supported for use across multiple Regions. They can only be used in the Region they are scoped to.

###### To generate an API key for your client domains

To obtain the integration URL and generate and retrieve the API keys
through the console.

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Application
   integration**.
3. In the pane, **protection packs (web ACLs) that are enabled for application integration**, select the Region that you want to use for your API key. You can also select the Region in the **API keys** pane of the **CAPTCHA integration** tab.
4. Choose the tab **CAPTCHA integration**. This tab provides the
   CAPTCHA JavaScript integration tag, which you can use in your
   integration, and the API keys listing. Both are scoped to the selected
   Region.
5. In the **API keys** pane, choose **Generate
   key**. The key generation dialogue appears.
6. Enter the client domains that you want to include in the key. You can
   enter up to 5. When you're finished, choose **Generate
   key**. The interface returns to the CAPTCHA integration
   tab, where your new key is listed.

Once created, an API key is immutable. If you need to make changes to
a key, generate a new key and use that instead. 7. (Optional) Copy the newly generated key for use in your integration.
You can also use the REST APIs or one of the language-specific AWS SDKs for
this work. The REST API calls are [CreateAPIKey](../APIReference/API_CreateAPIKey.md "../APIReference/API_CreateAPIKey.md") and [ListAPIKeys](../APIReference/API_ListAPIKeys.md "../APIReference/API_ListAPIKeys.md").

###### To delete an API key

To delete an API key, you must use the REST API or one of the language
specific AWS SDKs. The REST API call is [DeleteAPIKey](../APIReference/API_DeleteAPIKey.md "../APIReference/API_DeleteAPIKey.md"). You can't
use the console to delete a key.

After you delete a key, it can take up to 24 hours for AWS WAF to disallow use
of the key in all regions.
