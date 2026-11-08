

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Example – Challenging clients whose token came from a different type of network
<a name="waf-bot-control-example-token-provenance"></a>

A client that passes an AWS WAF challenge receives a token, and then presents the token with its later requests. Some bots take advantage of this by solving the challenge in one place and sending their traffic from another. For example, a bot can acquire tokens from a data center and then present them from residential proxy IP addresses. Those addresses belong to the same internet providers as your real users. Each request arrives with a valid token from an IP address that looks like a real user's. Neither the token nor the address identifies the bot.

At the targeted protection level, Bot Control records the category of the IP address that acquired each token. Categories include data center, VPN, residential, and mobile. When a later request presents the token, Bot Control compares that request's IP address category with the recorded one.

When the two categories differ, Bot Control adds a token provenance label to the request. The level in the label reflects how rarely legitimate clients make that kind of change:
+ `awswaf:managed:aws:bot-control:token_provenance:ip_category_mismatch:high` – A change that legitimate clients rarely make, such as a token acquired from a data center, proxy, or VPN IP address and presented from a residential or mobile IP address.
+ `awswaf:managed:aws:bot-control:token_provenance:ip_category_mismatch:medium` and `awswaf:managed:aws:bot-control:token_provenance:ip_category_mismatch:low` – Changes that have common legitimate causes, such as a residential client that turns on a VPN or proxy.

Bot Control adds these labels only to requests that present a token. It doesn't add them to requests from verified bots. A client that acquires and presents its token from the same category of IP address doesn't receive these labels. No rule in the Bot Control managed rule group acts on these labels. Your traffic handling doesn't change until you add a rule of your own. For more information about the labels that the rule group adds, see [Bot Control labels](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-labels-rg).

To use these labels, configure the Bot Control managed rule group with the targeted protection level. Select static version 7.0 or later of the rule group. For more information about selecting a static version, see [Using versioned managed rule groups in AWS WAF](waf-managed-rule-groups-versioning.md).

**Note**  
Use the CAPTCHA or Block action in your rule. In this scenario, the client's token already contains a valid challenge solution, so the Challenge action lets the requests through. For more information about how these actions handle a request that has a valid token, see [CAPTCHA and Challenge action behavior](waf-captcha-and-challenge-actions.md).

The following rule applies the CAPTCHA action to requests that have the `high` label. The rule must run after the Bot Control managed rule group, so that the label is available to match against. A real user who has changed networks can continue after solving the puzzle. A bot operator who moves tokens between networks must solve a puzzle for each token.

```
{
    "Name": "CaptchaTokenNetworkMismatchHigh",
    "Priority": 10,
    "Statement": {
      "LabelMatchStatement": {
        "Scope": "LABEL",
        "Key": "awswaf:managed:aws:bot-control:token_provenance:ip_category_mismatch:high"
      }
    },
    "Action": {
      "Captcha": {}
    },
    "VisibilityConfig": {
      "SampledRequestsEnabled": true,
      "CloudWatchMetricsEnabled": true,
      "MetricName": "CaptchaTokenNetworkMismatchHigh"
    }
}
```

To block these clients instead of challenging them, combine the label with another Bot Control signal to increase your confidence that the client is automated. The following rule blocks requests that have the `high` label and whose token also indicates an automated browser.

```
{
    "Name": "BlockAutomatedTokenNetworkMismatch",
    "Priority": 11,
    "Statement": {
      "AndStatement": {
        "Statements": [
          {
            "LabelMatchStatement": {
              "Scope": "LABEL",
              "Key": "awswaf:managed:aws:bot-control:token_provenance:ip_category_mismatch:high"
            }
          },
          {
            "LabelMatchStatement": {
              "Scope": "LABEL",
              "Key": "awswaf:managed:aws:bot-control:targeted:signal:automated_browser"
            }
          }
        ]
      }
    },
    "Action": {
      "Block": {}
    },
    "VisibilityConfig": {
      "SampledRequestsEnabled": true,
      "CloudWatchMetricsEnabled": true,
      "MetricName": "BlockAutomatedTokenNetworkMismatch"
    }
}
```

To check the effect of a rule before you enforce it, start with the rule action set to Count. Then review the labels in your protection pack (web ACL) logs. Real users commonly produce the `medium` and `low` labels, such as when they turn on a VPN. Use these labels to narrow other rules rather than as the only reason to block a request. For example, use them in the scope-down statement of a rate-based rule. For more information about rate-based rules, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md).