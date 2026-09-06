

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Changing the action used for automatic application layer DDoS mitigation
<a name="change-action-of-automatic-app-layer-response"></a>

You can change the action that Shield Advanced uses for its application layer automatic response in multiple locations in the console:
+ **Automatic mitigation configuration** – Change the action when you configure automatic mitigation for your resource. For the procedure, see the preceding section [Enabling and disabling automatic application layer DDoS mitigation](enable-disable-automatic-app-layer-response.md).
+ **Event details page** – Change the action in the event details page, when you're viewing the event information in the console. For information, see [Viewing AWS Shield Advanced event details](ddos-event-details.md).

If you have two protected resources that share a web ACL, and you set the action to Count for one and Block for the other, Shield Advanced sets the action for the rule group's rate-based rule `ShieldKnownOffenderIPRateBasedRule` to Block.