

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Bot confidence levels

Starting with version 8.0, the targeted protection level of the Bot Control managed rule group combines the targeted detection signals on a web request into a single bot confidence level: High, Medium, or Low. The rule group adds the level to the request as a label. The confidence level indicates how strongly the targeted detections on the request point to an automated client. Requests that don't have any targeted detection signals don't receive a confidence level label. 

Several targeted rules already report their own confidence in their labels, for example `TGT_ML_CoordinatedActivity{{Low|Medium|High}}` and `TGT_TokenReuseIp{{Low|Medium|High}}`. Each of those describes the strength of a single detection. The bot confidence level combines the targeted detections into one level for the request, so you can choose one action per level instead of writing rules against many individual labels. 

The rule group adds one of the following labels to the request: 
+ `awswaf:managed:aws:bot-control:targeted:signal:bot_signal:high` – The request has a signal that by itself strongly indicates automation, or it has two or more signals that corroborate each other. 
+ `awswaf:managed:aws:bot-control:targeted:signal:bot_signal:medium` – The request has a signal that indicates automation, but no other signal corroborates it. The request might still come from a person. 
+ `awswaf:managed:aws:bot-control:targeted:signal:bot_signal:low` – The request has only weak signals of automation, for example a high request volume from a single client session. Legitimate clients can also produce these signals. 

Three rules match these labels for requests that are not from verified bots. The rules use the Count action, so by default they add their labels and metrics without affecting the request. You can see how the confidence levels classify your traffic before you decide how to act on each level. The following table lists the rules. 


**Bot confidence levels and rule actions**  

| Confidence level | Rule | Rule action | 
| --- | --- | --- | 
| High | TGT\_SignalBotHigh | Count | 
| Medium | TGT\_SignalBotMedium | Count | 
| Low | TGT\_SignalBotLow | Count | 

To act on a confidence level, override the rule's action in your protection pack (web ACL) to Block, CAPTCHA, or Challenge. We recommend CAPTCHA for High, CAPTCHA for Medium, and Challenge for Low. These actions keep the impact of a misclassification low: a person can solve the CAPTCHA puzzle, and most browsers complete the silent Challenge without any action from the user. For more information about overriding rule actions, see [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md). In the console, for protection packs (web ACLs) with the CloudFront scope, the **Targeted bot control** setting applies the recommended actions for you and lets you change the action for each level. For more information about the setting, see [Turning on Targeted bot control in the console](waf-bot-control-targeted-console.md). 

AWS WAF adds the confidence level labels alongside the other Bot Control labels. Every detection label that the rule group adds is still attached to the request, so you can inspect a request in your logs and see which signals contributed to its confidence level. You can also see the confidence level labels in Amazon CloudWatch label metrics. 

To pass the confidence level to your application, insert it into a request header with custom request handling and dynamic label interpolation. For example, a header value of `${awswaf:managed:aws:bot-control:targeted:signal:bot_signal:}` resolves to `high`, `medium`, or `low`, or to an empty string if the request has no confidence level label. For more information about dynamic label interpolation, see [Dynamic label interpolation](waf-dynamic-label-interpolation.md). 

**Note**  
Bot confidence levels require the targeted protection level and version 8.0 or later of the rule group. The `LATEST` version always meets this requirement. If you use a static version, choose 8.0 or later. For more information about the `LATEST` version, see [LATEST version for the Bot Control managed rule group](waf-managed-rule-groups-versioning-latest.md). 

**Considerations**  
Review the following when you use bot confidence levels. 
+ **Exclude known automation from bot inspection.** If legitimate automated clients that you rely on, such as monitoring tools or partner integrations, receive confidence labels and actions, add a scope-down statement to the rule group that excludes them, for example by path, header, or IP set. This also keeps you from paying to inspect traffic that you already trust. For more information about scope-down statements, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md). 
+ **Integrate the application integration SDKs.** Many targeted detections rely on the client-side signals in AWS WAF tokens. Without tokens, fewer signals are available for the confidence level. If you deliver your application through CloudFront, you can have CloudFront add the JavaScript SDK for you. For more information about tokens and the SDKs, see [Using application integration SDKs with Bot Control](waf-bot-with-tokens.md) and [Automatic SDK integration for CloudFront distributions](waf-challenge-javascript-sdk-injection.md). 
+ **Review the labels before you enforce them.** Because the rules use the Count action by default, you can review the confidence level label metrics and sampled requests first, and then override the rule actions when you're ready to enforce them. For more information about testing, see [Testing and tuning your AWS WAF protections](web-acl-testing.md). 
+ **Remember that the other targeted rules keep their own actions.** The confidence level rules are added to the other targeted rules, which continue to act on their own labels as described in [Bot Control rules listing](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules). 