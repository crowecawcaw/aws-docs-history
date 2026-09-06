

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Choosing and configuring Bot Control for your use case
<a name="waf-bot-control-use-cases"></a>

Bot Control protects against a range of automated threats. The right configuration depends on what you're protecting and what threats you face. Use this topic to choose the right protection level and configure Bot Control for common application scenarios.

## Matching Bot Control to your application
<a name="waf-bot-control-use-cases-scenarios"></a>

Bot threats generally fall into three categories:
+ **Fraud threats** – Credential stuffing, fake accounts, and automated purchasing.
+ **Content threats** – Scraping of pricing data, product catalogs, and published content.
+ **Availability threats** – Bot traffic volume that degrades performance or increases infrastructure costs.

For most of these threats, we recommend the targeted protection level with the client application integration SDKs. The following scenarios describe how to configure Bot Control for each.

**Protecting login and account pages**  
Credential stuffing and account takeover attacks use automated tools to test stolen credentials against your login endpoints. Account creation fraud uses bots to create fake accounts at scale. Integrate the application integration SDK across your site, and pair Bot Control with the AWS WAF Fraud Control managed rule groups for login and account creation protection.

**Protecting product catalogs and pricing data**  
If your application displays product information, pricing, inventory levels, or other competitive data, bots may scrape this content to feed competitor intelligence, build comparison sites, or undercut your pricing. These scrapers often mimic real browsers and rotate through residential IP addresses to avoid detection. Apply Bot Control across your product and catalog pages, not just checkout. This way Bot Control can detect the behavioral patterns of automated scraping even when the bot appears to be a normal browser.

**Protecting published content**  
Content publishers, news sites, and media platforms face bots that copy articles, images, and other original content. This content theft can dilute your search rankings, reduce ad revenue, and undermine your competitive position. Apply Bot Control across your content pages. Use the Bot Control dashboard to monitor which bots are accessing your content and decide how to handle each category. For more information, see [AWS WAF Bot Control components](waf-bot-control-components.md).

**Reducing infrastructure costs from unwanted crawlers**  
Scrapers, crawlers, and automated tools can generate high traffic volume, increasing your compute and data transfer costs without providing business value. Bot Control identifies self-declaring bots by category, such as scrapers, HTTP libraries, and crawling frameworks. You can then block or rate-limit each category independently using labels. For evasive scraping, targeted protection detects bots that disguise their identity, including those using residential proxies and headless browsers.

**Protecting high-value transactions**  
Checkout flows, limited-inventory purchases, and ticket sales are targets for automated purchasing bots that compete with legitimate customers. Bot Control detects automated browsers such as Selenium and Puppeteer, and applies session-level rate limiting to prevent a single client from monopolizing inventory. Integrate the SDKs on your transaction pages for the strongest detection accuracy.

**Managing AI crawlers and training data scrapers**  
AI bots collect content from your application to train models or surface data in AI applications. Bot Control categorizes known AI bots. Write custom rules to allow specific AI bots you want to permit, such as verified search engine crawlers, and block or rate-limit others. For AI agents that use browser automation frameworks to interact with your application, Bot Control detects and challenges these automated sessions. With Web Bot Authentication (WBA), legitimate AI agents can cryptographically prove their identity. This gives you a reliable signal to distinguish authorized agents from unauthorized ones. For more information about WBA, see [Web bot authentication for AI agents](waf-bot-control.md#waf-bot-ai-agents).

**Protecting mobile applications**  
Mobile applications face bot threats similar to web applications, but their traffic has different characteristics. Mobile clients use non-browser user agents. HTTP requests from native mobile application frameworks are excluded from the Bot Control `SignalNonBrowserUserAgent` rule, but non-standard HTTP libraries and in-app browsers are not. Integrate the AWS WAF Mobile SDK into your iOS or Android application to provide the client-side tokens that targeted protection uses for accurate detection.

## Choosing between common and targeted protection
<a name="waf-bot-control-choosing-level"></a>

Bot Control offers two protection levels. The following guidance helps you choose the right level for your application.

**Common protection level**  
Common protection detects bots that identify themselves through their user-agent strings, IP addresses, and other request characteristics. It verifies that bots claiming to be from known organizations (such as search engines) actually originate from those organizations. Common protection gives you visibility into who is visiting your application and lets you control each bot category independently. It does not require the SDKs and has a lower per-request cost. Common protection is a good starting point when you primarily need to manage known bot traffic, such as blocking unwanted scrapers while allowing search engine crawlers.

**Targeted protection level**  
The targeted protection level detects everything that the common protection level detects, and adds detection for bots that don't self-identify. It uses browser interrogation, TLS fingerprinting, behavioral heuristics, and machine learning to distinguish automated clients from humans. The machine learning analyzes your specific website's traffic patterns, including timestamps, browser characteristics, and navigation behavior. It updates its detection as your traffic changes and as bot tactics change. Targeted protection is recommended for applications facing credential stuffing, advanced scraping, automated purchasing, or any bot activity where the attacker actively tries to evade detection.

For most production web applications, we recommend targeted protection. For guidance on configuring targeted protection for specific scenarios, see [Matching Bot Control to your application](#waf-bot-control-use-cases-scenarios). For guidance on managing costs at high traffic volumes, see [Managing costs](#waf-bot-control-cost-strategies).


|  | Common | Targeted | 
| --- | --- | --- | 
| Detects self-identifying bots | Yes | Yes | 
| Verifies legitimate bots (search engines, monitoring services) | Yes | Yes | 
| Detects bots that hide their identity | No | Yes | 
| Machine learning adapted to your traffic | No | Yes | 
| Session-level rate limiting | No | Yes | 
| Detects browser automation tools | Yes (self-identifying) | Yes (including evasive) | 
| Client application integration SDKs | Not required | Strongly recommended | 

**Checking your rule group version**  
The Bot Control managed rule group is updated over time with new detection capabilities. Check which version you are currently using and whether a newer static version is available. Newer versions include additional detections that can increase your coverage against new bot threats. You can review the available versions and their changes in the [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md).

## How Bot Control detection works
<a name="waf-bot-control-how-it-protects"></a>

Bot Control labels every request it evaluates with granular classification: bot name, category, organization, and verification status. You write rules that match on these labels to decide what action to take for each type of bot. This gives you full control rather than a single allow-or-block decision for all bot traffic.

At the targeted protection level, Bot Control combines multiple detection techniques. These include signature matching, browser interrogation, TLS fingerprinting, behavioral heuristics, and machine learning tuned to your website's traffic patterns. A bot that evades one technique may be caught by another. The machine learning also detects coordinated bot activity: patterns where multiple clients work together in ways that individual request analysis would miss. For a detailed description of all Bot Control components, see [AWS WAF Bot Control components](waf-bot-control-components.md). For a walkthrough of how the Challenge and CAPTCHA interactions work between the client and AWS WAF, see [CAPTCHA and Challenge in AWS WAF](waf-captcha-and-challenge.md).

## Managing costs
<a name="waf-bot-control-cost-strategies"></a>

Your costs for using the Bot Control managed rule group increase with the number of web requests that AWS WAF evaluates with it. For most applications, the cost of Bot Control is justified by the protection it provides. Blocking bot traffic reduces your compute, bandwidth, and data transfer costs, often by more than the cost of the inspection itself. If you need to optimize costs further, the following strategies can help.

**Exclude static assets**  
The simplest cost optimization is to exclude requests for static file types such as `.css`, `.png`, `.jpg`, and `.svg` from Bot Control inspection. Bots that target your application data and functionality hit dynamic endpoints, not your stylesheets or images. This reduces inspected requests without reducing detection effectiveness. For an example, see [Bot Control example: Using Bot Control only for dynamic content](waf-bot-control-example-scope-down-dynamic-content.md).

**Order rules for efficiency**  
Place less expensive rules before the Bot Control managed rule group in your protection pack (web ACL). Rules such as IP reputation lists, geographic restrictions, and rate-based rules can block clearly unwanted traffic before it reaches the paid Bot Control inspection. Requests that are blocked by earlier rules are never evaluated by Bot Control, so you don't incur the additional per-request fee for them.

**Scope to specific endpoints when appropriate**  
For some applications, you may want to apply Bot Control only to specific parts of your site. For example, if your application has a public informational section that doesn't contain sensitive data or valuable content, you can exclude it from inspection. Be careful not to exclude pages that contain content worth protecting, such as product catalogs, pricing data, or published articles. For an example, see [Bot Control example: Using Bot Control only for the login page](waf-bot-control-example-scope-down-login.md).

## Integrating the client application integration SDKs
<a name="waf-bot-control-sdk-guidance"></a>

Use the JavaScript and Mobile SDKs to maximize the effectiveness of targeted protection. The SDKs provide browser fingerprinting, challenge token management, and behavioral telemetry that targeted rules use for session-level detection. A session here is identified by the client token that the SDK acquires, which represents a specific browser or device. Without the SDKs, targeted protection has much less context to work with, and cannot reliably distinguish advanced bots from legitimate users.

**Integrate the SDK from the start**  
When you deploy targeted protection, integrate the SDKs at the same time. This applies whether you are deploying to production or evaluating Bot Control in a test environment. Evaluating targeted protection without the SDKs does not give you an accurate picture of its detection capabilities, because many of the targeted rules depend on the client-side signals that only the SDKs provide.

**Broad integration recommended**  
For the strongest detection, integrate the JavaScript SDK across all pages that serve dynamic content, not just login or checkout. Bot Control builds behavioral profiles from how clients navigate your application, including request timing, page sequences, and interaction patterns. When the SDK is present on only a single page, Bot Control has limited behavioral context to distinguish a real user from a bot that has learned to mimic one page load. Broader integration gives Bot Control a richer picture of each client session, which improves detection of advanced bots such as residential proxy botnets. At minimum, integrate the SDK on your most critical pages, but treat this as a starting point rather than the end state.

**Mobile applications**  
For iOS and Android applications, use the AWS WAF Mobile SDK. The Mobile SDK handles token acquisition and renewal within your app. For more information about the SDKs, see [Client application integrations in AWS WAF](waf-application-integration.md).

## Common configuration adjustments
<a name="waf-bot-control-common-adjustments"></a>

Most Bot Control deployments require some configuration adjustments to match the specific characteristics of your application traffic. The following are the most common adjustments.

**Allowing monitoring and health-check tools**  
Internal monitoring tools, uptime checkers, and load balancer health checks generate automated traffic that Bot Control may identify as bot activity. Exclude these requests from Bot Control inspection using a scope-down statement that matches on the source IP address range or a custom header that your monitoring tools include.

**Excluding in-app browsers and non-standard HTTP libraries**  
If users access your site through in-app browsers, such as links opened from social media apps, or if your mobile app uses a non-standard HTTP library, these clients may trigger the `SignalNonBrowserUserAgent` rule. Standard native mobile frameworks are excluded from this rule, but other non-browser user agents are not. Configure a user-agent exception in the Bot Control rule group for these clients. For an example, see [Bot Control example: Creating an exception for a blocked user agent](waf-bot-control-example-user-agent-exception.md).

**Managing verified bot crawlers**  
Bot Control allows verified bots by default. If you want to rate-limit even verified crawlers, for example to reduce the load from aggressive but legitimate search engine crawling, use the bot labels to write custom rate-based rules that limit the request rate for specific verified bot categories. For an example, see [Bot Control example: Explicitly allowing verified bots](waf-bot-control-example-allow-verified-bots.md).

**Forwarding bot signals to your origin**  
You can pass Bot Control classification labels to your application as custom request headers. Your origin can then use the labels to serve simplified content to suspected scrapers, log bot activity in your own analytics, or include a request identifier in block pages for false positive reporting. Use the AWS WAF custom request header feature to insert headers based on label matches. For more information about dynamic label values in headers, see [Customized web requests and responses in AWS WAF](waf-custom-request-response.md).

**Triggering step-up authentication**  
Instead of blocking suspicious traffic outright, you can forward Bot Control signals to your application and use them to trigger additional verification. For example, if Bot Control labels a session as suspicious, your application can require multi-factor authentication or present an additional verification step before completing a sensitive action. Step-up authentication reduces the impact of false positives while still protecting against automated threats. Use custom request headers to pass the relevant Bot Control labels to your origin.

**Testing before enforcing**  
Always deploy Bot Control in count mode first. In count mode, Bot Control labels all requests but does not block any traffic. Review the labels in your AWS WAF logs to understand what Bot Control detects in your traffic, verify that legitimate traffic is not being mislabeled, and then switch to block mode once you are confident in the detection accuracy. For detailed guidance on testing and deployment, see [Testing and deploying AWS WAF Bot Control](waf-bot-control-deploying.md).

**Deploying behind a CDN or reverse proxy**  
If your application sits behind a third-party CDN, by default AWS WAF sees the CDN's IP address as the client. The Bot Control managed rule group recognizes traffic from Amazon CloudFront, Cloudflare, and Fastly automatically and uses the originating client IP from the CDN's standard client IP header instead. Both the common protection level and the targeted protection level use this detection, including session-level rate limiting and the targeted bot detection rules that depend on accurate client identity. You don't need additional forwarded IP configuration on the Bot Control rule group for these CDNs. For other rule statements in your protection pack (web ACL) that use IP addresses, such as your custom IP set match, geo match, ASN match, and rate-based rules, configure them with a forwarded IP configuration if you want them to evaluate the upstream client IP. For information about forwarded IP addresses, see [Using forwarded IP addresses in AWS WAF](waf-rule-statement-forwarded-ip-address.md). If your application is behind a different reverse proxy or a CDN that Bot Control doesn't recognize automatically, configure your reverse proxy to forward the client IP in a header such as `X-Forwarded-For` and use a forwarded IP configuration on the rule statements that evaluate IP addresses.