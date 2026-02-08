# Overriding safety rules

to reroute traffic

There are scenarios when you might want to bypass the routing control safeguards that are enforced with
safety rules that you've configured. For example, you might want to fail over quickly for disaster recovery, and one or more safety rules might be
unexpectedly preventing you from updating a routing control state to reroute traffic. In a "break glass" scenario like this,
you can override one or more safety rules to change a routing control state and fail over your application.

You can bypass safety rules when you update a routing control state (or multiple routing control states) by using the
`update-routing-control-state` or `update-routing-control-states` AWS CLI command with the
`safety-rules-to-override` parameter. Specify the parameter with the Amazon Resource Name (ARN) of
the safety rule that you want to override, or specify a comma-separated list of ARNs to override two or more safety rules.

When a safety rule blocks a routing control state update, the error message includes the ARN of the rule that blocked the update.
So you can make a note of the ARN, and then specify it in a routing control state CLI command with
the safety rule override parameter.

###### Note

Because more than one safety rule might be in place for the routing controls that you're updating, you could run the CLI
command to update your routing control state with one safety rule override but get an error that another safety rule is blocking
the update. Continue to add safety rule ARNs to the list of rules to override in the update command, separated by commas, until
the update command completes successfully.

To learn more about using the `SafetyRulesToOverride` property with the API and SDKs,
see [UpdateRoutingControlState](../../../routing-control/latest/APIReference/API_UpdateRoutingControlState.md "../../../routing-control/latest/APIReference/API_UpdateRoutingControlState.md").

The following are two examples of CLI commands to override safety rules to update routing control states.

**Override one safety rule**

```
aws route53-recovery-cluster --region us-west-2 update-routing-control-state \
				--routing-control-arn \
				arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567 \
				--routing-control-state On \
				--safety-rules-to-override arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/safetyrule/yyyyyyy8888888 \
				--endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

**Override two safety rules**

```
aws route53-recovery-cluster --region us-west-2 update-routing-control-state \
				--routing-control-arn \
				arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567 \
				--routing-control-state On \
				--safety-rules-to-override "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/safetyrule/yyyyyyy8888888" \
				"arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/safetyrule/qqqqqqq7777777"
				--endpoint-url https://host-dddddd.us-west-2.example.com/v1
```
