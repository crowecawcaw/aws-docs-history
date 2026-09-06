

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Using application integration SDKs with Bot Control
<a name="waf-bot-with-tokens"></a>

This section explains how to use application integration SDKs with Bot Control.

Most of the targeted protections of the Bot Control managed rule group require the challenge tokens that the application integration SDKs generate. The rules that don't require a challenge token on the request are the Bot Control common level protections and the targeted level machine learning rules. For descriptions of the protection levels and rules in the rule group, see [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md). 

We highly recommend implementing the application integration SDKs, for the most effective use of the Bot Control rule group. The challenge script must run before the Bot Control rule group in order for the rule group to benefit from the tokens that the script acquires. 

At minimum, add the JavaScript challenge script tag to your most critical pages such as login, checkout, and account creation. For the strongest detection, integrate the SDK more broadly across pages that serve dynamic content. The more behavioral data Bot Control has, the better it can distinguish real users from advanced bots. For detailed integration guidance, see [Integrating the client application integration SDKs](waf-bot-control-use-cases.md#waf-bot-control-sdk-guidance).
+ With the application integration SDKs, the script runs automatically.
+ If you're unable to use the SDKs, you can configure your protection pack (web ACL) so that it runs the Challenge or CAPTCHA rule action against all requests that will be inspected by the Bot Control rule group. Using the Challenge or CAPTCHA rule action can incur additional fees. For pricing details, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/). 

When you implement the application integration SDKs in your clients or use one of the rule actions that runs the challenge script, you expand the capabilities of the rule group and of your overall client application security. 

Tokens provide client information with each web request. This additional information enables the Bot Control rule group to separate legitimate client sessions from ill-behaved client sessions, even when both originate from a single IP address. The rule group uses information in the tokens to aggregate client session request behavior for the fine-tuned detection and mitigation that the targeted protections level provide. 

For information about the SDKs, see [Client application integrations in AWS WAF](waf-application-integration.md). For information about AWS WAF tokens, see [Token use in AWS WAF intelligent threat mitigation](waf-tokens.md). For information about the rule actions, see [CAPTCHA and Challenge in AWS WAF](waf-captcha-and-challenge.md).