

# Tracking changes to a shared policy
<a name="next-gen-org-policy-timeline"></a>

A shared policy keeps a timeline of the events that affected it. The account that owns the policy can see how member accounts used it and what changed. Use the `ListPolicyEvents` API operation to retrieve the timeline:

```
aws resiliencehubv2 list-policy-events \
  --policy-arn "arn:aws:resiliencehub:us-east-1:111122223333:policy/tier-1-dr:abc123"
```

The timeline records the following events.


| Event | Description | 
| --- | --- | 
| Policy attached to service | The event records the service that started using the policy, and the AWS account that owns the service. | 
| Policy detached from service | The event records the service that stopped using the policy, and the reason it stopped. | 
| Policy sharing revoked | The event records that the policy owner turned off cross-account sharing, and the number of services using the policy at that moment. | 
| Policy deleted | The event records that the policy owner deleted the policy, and the number of services using it at that moment. | 

A service stops using a policy for one of three reasons. The service owner applied a different policy, the policy owner turned off cross-account sharing, or the policy owner deleted the policy.

You can filter the timeline by time range and by event type. Only the account that owns the policy can read its timeline. A member account that uses a shared policy cannot read it.

The last two events report a point-in-time count. Next generation Resilience Hub captures the number of services at the moment of the change, so the count does not update afterward.