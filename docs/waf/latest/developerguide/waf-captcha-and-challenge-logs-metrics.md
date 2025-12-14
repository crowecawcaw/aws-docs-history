**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# CAPTCHA and Challenge actions in the logs and metrics

This section explains how AWS WAF handles logging and metrics for the CAPTCHA and Challenge actions.

The CAPTCHA and Challenge actions can be non-terminating, like
Count, or terminating, like Block. The outcome depends on whether
the request has a valid token with an unexpired timestamp for the action type.

- **Valid token** – When the
  action finds a valid token and doesn't block the request, AWS WAF captures
  metrics and logs as follows:
  - Increments the metrics for either `CaptchaRequests` and `RequestsWithValidCaptchaToken` or `ChallengeRequests` and `RequestsWithValidChallengeToken`.
  - Logs the match as a `nonTerminatingMatchingRules` entry with action of CAPTCHA or Challenge. The following listing shows the section of a log for this type of match with the CAPTCHA action.

  ```
      "nonTerminatingMatchingRules": [
      {
        "ruleId": "captcha-rule",
        "action": "CAPTCHA",
        "ruleMatchDetails": [],
        "captchaResponse": {
          "responseCode": 0,
          "solveTimestamp": 1632420429
        }
      }
    ]
  ```

- **Missing, invalid, or expired token** – When the action blocks the request due to
  a missing or invalid token, AWS WAF captures metrics and logs as follows:

      + Increments the metric for `CaptchaRequests` or `ChallengeRequests`.
      + Logs the match as a `CaptchaResponse` entry with HTTP `405`
       status code or as a `ChallengeResponse` entry with HTTP
       `202` status code. The log indicates whether the
       request was missing the token or had an expired timestamp. The log
       also indicates whether AWS WAF sent a CAPTCHA interstitial page to
       the client or a silent challenge to the client browser. The
       following listing shows the sections of a log for this type of match
       with the CAPTCHA action.



      ```
          "terminatingRuleId": "captcha-rule",
          "terminatingRuleType": "REGULAR",
          "action": "CAPTCHA",
          "terminatingRuleMatchDetails": [],
          ...
          "responseCodeSent": 405,
          ...
          "captchaResponse": {
            "responseCode": 405,
            "solveTimestamp": 0,
            "failureReason": "TOKEN_MISSING"
          }
      ```

  For information about the AWS WAF logs, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").

For information about AWS WAF metrics, see [AWS WAF metrics and dimensions](waf-metrics.md "waf-metrics.md").

For general information about rule action options, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

###### Requests with no token seem to show up twice in logs and metrics

Based on the [CAPTCHA and Challenge action behavior](waf-captcha-and-challenge-actions.md "waf-captcha-and-challenge-actions.md") and the logging and metrics described in this section, a request with no token will
generally be represented twice in the logs and metrics. This is because the one intended request is
actually sent twice by the client.

- The first request, with no token, receives the logging and metrics handling
  described above for missing, invalid, or expired token. The CAPTCHA or Challenge
  action terminates this first request, and then responds back to the client with either a silent challenge or CAPTCHA puzzle.
- The client evaluates the challenge or puzzle and, if the client browser or end user responds successfully,
  sends the request a second time with the newly
  acquired token. This second request receives the logging and metrics handling described above for a request with a valid token.
