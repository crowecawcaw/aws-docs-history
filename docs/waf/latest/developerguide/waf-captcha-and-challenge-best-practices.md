**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Best practices for using the

CAPTCHA and Challenge actions

Follow the guidance in this section to plan and implement AWS WAF CAPTCHA or
challenge.

###### Plan your CAPTCHA and challenge implementation

Determine where to place CAPTCHA puzzles or silent challenges based on your website
usage, the sensitivity of the data that you want to protect, and the type of
requests. Select the requests where you'll apply CAPTCHA so that you present the
puzzles as needed, but avoid presenting them where they wouldn't be useful and might
degrade the user experience. Use the Challenge action to run silent
challenges that have less impact on the end user, but still help verify that the
request is coming from a JavaScript enabled browser.

CAPTCHA puzzles and silent
challenges can only run when browsers are accessing HTTPS endpoints. Browser
clients must be running in secure contexts in order to acquire tokens.

###### Decide where to run CAPTCHA puzzles and silent challenges on your

clients

Identify requests that you don't want to have impacted by CAPTCHA, for example,
requests for CSS or images. Use CAPTCHA only when necessary. For example, if you
plan to have a CAPTCHA check at login, and the user is always taken directly from
the login to another screen, requiring a CAPTCHA check at the second screen would
probably not be needed and might degrade your end user experience.

Configure your Challenge and CAPTCHA use so that AWS WAF only sends CAPTCHA
puzzles and silent challenges in response to `GET`
`text/html` requests. You can't run either the puzzle or the challenge in
response to `POST` requests, Cross-Origin Resource Sharing (CORS) preflight `OPTIONS` requests, or any
other non-`GET` request types. Browser behavior
for other request types can vary and might not be able to handle the interstitials properly.

It's possible for a client to accept HTML but still not be able to handle the
CAPTCHA or challenge interstitial. For example, a widget on a webpage with a small
iFrame might accept HTML but not be able to display a CAPTCHA or process it. Avoid
placing the rule actions for these types of requests, the same as for requests that
don't accept HTML.

###### Use CAPTCHA or Challenge to verify prior token acquisition

You can use the rule actions solely to verify the existence of a valid token, at locations
where legitimate users should always have one. In these situations, it doesn't
matter whether the request can handle the interstitials.

For example, if you implement the JavaScript client application CAPTCHA API, and run
the CAPTCHA puzzle on the client immediately before you send the first request to your
protected endpoint, your first request should always include a token that's valid for
both challenge and CAPTCHA. For information about JavaScript client application
integration, see [AWS WAF JavaScript integrations](waf-javascript-api.md "waf-javascript-api.md").

For this situation, in your protection pack (web ACL), you can add a rule that matches against this first call
and configure it with the Challenge or CAPTCHA rule action. When the
rule matches for a legitimate end user and browser, the action will find a valid token,
and therefore will not block the request or send a challenge or CAPTCHA puzzle in
response. For more information about how the rule actions work, see [CAPTCHA and Challenge action behavior](waf-captcha-and-challenge-actions.md "waf-captcha-and-challenge-actions.md").

###### Protect your sensitive non-HTML data with CAPTCHA and Challenge

You can use CAPTCHA and Challenge protections for sensitive non-HTML data, like
APIs, with the following approach.

1. Identify requests that take HTML responses and that are run in close
   proximity to the requests for your sensitive, non-HTML data.
2. Write CAPTCHA or Challenge rules that match against the requests for HTML
   and that match against the requests for your sensitive data.
3. Tune your CAPTCHA and Challenge immunity time settings so that, for
   normal user interactions, the tokens that clients obtain from the HTML requests
   are available and unexpired in their requests for your sensitive data. For
   tuning information, see [Setting timestamp expiration and token immunity times in AWS WAF](waf-tokens-immunity-times.md "waf-tokens-immunity-times.md").
   When a request for your sensitive data matches a CAPTCHA or Challenge rule,
   it won't be blocked if the client still has a valid token from the prior puzzle or
   challenge. If the token isn't available or the timestamp is expired, the request to
   access your sensitive data will fail. For more information about how the rule actions
   work, see [CAPTCHA and Challenge action behavior](waf-captcha-and-challenge-actions.md "waf-captcha-and-challenge-actions.md").

###### Use CAPTCHA and Challenge to tune your existing rules

Review your existing rules, to see if you want to alter or add to them. The
following are some common scenarios to consider.

- If you have a rate-based rule that blocks traffic, but you keep the rate limit relatively
  high to avoid blocking legitimate users, consider adding a second rate-based
  rule after the blocking rule. Give the second rule a lower limit than the blocking rule
  and set the rule action to CAPTCHA or Challenge. The blocking rule will still block
  requests that are coming at too high a rate, and the new rule will block most automated traffic
  at an even lower rate. For information about rate-based rules, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md").
- If you have a managed rule group that blocks requests, you can switch the behavior for
  some or all of the rules from Block to CAPTCHA or
  Challenge. To do this, in the managed rule group configuration, override
  the rule action setting. For information about overriding rule actions, see
  [Rule group rule action overrides](web-acl-rule-group-override-options.md#web-acl-rule-group-override-options-rules "web-acl-rule-group-override-options.md#web-acl-rule-group-override-options-rules").

###### Test your CAPTCHA and challenge implementations before you deploy them

As for all new functionality, follow the guidance at [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

During testing, review your token timestamp expiration requirements and set your web
ACL and rule level immunity time configurations so that you achieve a good balance
between controlling access to your website and providing a good experience for your
customers. For information, see [Setting timestamp expiration and token immunity times in AWS WAF](waf-tokens-immunity-times.md "waf-tokens-immunity-times.md").
