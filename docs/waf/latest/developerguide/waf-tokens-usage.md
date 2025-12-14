**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How AWS WAF uses tokens

This section explains how AWS WAF uses tokens.

AWS WAF uses tokens to record and verify the following types of client session validation:

- **CAPTCHA** – CAPTCHA puzzles
  help distinguish bots from human users. A CAPTCHA is run only by the
  CAPTCHA rule action. Upon successful completion of the puzzle, the CAPTCHA
  script updates the token's CAPTCHA timestamp. For more information, see [CAPTCHA and Challenge in
  AWS WAF](waf-captcha-and-challenge.md "waf-captcha-and-challenge.md").
- **Challenge** – Challenges run silently to help
  distinguish regular client sessions from bot sessions and to make it more costly
  for bots to operate. When the challenge completes successfully, the challenge
  script automatically procures a new token from AWS WAF if needed, and then updates
  the token's challenge timestamp.

AWS WAF runs challenges in the following situations:

    + **Application integration SDKs** – The application
     integration SDKs run inside your client application sessions and help ensure
     that login attempts are only allowed after the client has successfully
     responded to a challenge. For more information, see [Client application
     integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md").
    + **Challenge rule action** – For more
     information, see [CAPTCHA and Challenge in
     AWS WAF](waf-captcha-and-challenge.md "waf-captcha-and-challenge.md").
    + **CAPTCHA** – When a CAPTCHA
     interstitial runs, if the client doesn't have a token yet, the script
     automatically runs a challenge first, to verify the client session
     and to initialize the token.

Tokens are required by many of the rules in the intelligent threat AWS Managed Rules rule groups. The rules use
tokens to do things like distinguish between clients at the session level, to determine
browser characteristics, and to understand the level of human interactivity on the
application web page. These rule groups invoke AWS WAF token management, which applies
token labeling that the rule groups then inspect.

- **AWS WAF Fraud Control account creation fraud prevention (ACFP)** – The ACFP rules require web
  requests with valid tokens. For more information about the rules, see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md").
- **AWS WAF Fraud Control account takeover prevention (ATP)** – The ATP rules that prevent high
  volume and long lasting client sessions require web requests that have a valid token with
  an unexpired challenge timestamp. For more information, see [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md "aws-managed-rule-groups-atp.md").
- **AWS WAF Bot Control** – The targeted rules in this rule group
  place a limit on the number of web requests that a client can send without a valid
  token, and they use token session tracking for session-level monitoring and
  management. As needed, the rules apply the Challenge and CAPTCHA
  rule actions to enforce token acquisition and valid client behavior. For more
  information, see [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md").
