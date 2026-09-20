

# Sharing a policy across your organization
<a name="next-gen-policy-sharing"></a>

If you use AWS Organizations, you can share a resilience policy with the member accounts in your organization. Service owners in those accounts can then apply the shared policy to their own services. Your organization measures resilience against the same requirements, without each account maintaining a separate copy of the policy.

Only the delegated administrator or the management account can enable cross-account sharing. For more information about designating a delegated administrator, see [AWS Organizations integration](next-gen-organizations.md).

**Sharing a policy**

Enable cross-account sharing when you create the policy:

```
aws resiliencehubv2 create-policy \
  --name "Tier 1 DR Policy" \
  --multi-region '{"rtoInMinutes": 15, "rpoInMinutes": 5, "disasterRecoveryApproach": "WARM_STANDBY"}' \
  --sharing-enabled
```

You can also enable it on an existing policy:

```
aws resiliencehubv2 update-policy \
  --policy-arn "arn:aws:resiliencehub:us-east-1:111122223333:policy/tier-1-dr:abc123" \
  --sharing-enabled
```

Member accounts see shared policies alongside the policies they own. Each policy reports whether the account owns it or received it through organization sharing, so service owners can tell the two apart.

**Stopping sharing**

To stop sharing a policy, disable cross-account sharing:

```
aws resiliencehubv2 update-policy \
  --policy-arn "arn:aws:resiliencehub:us-east-1:111122223333:policy/tier-1-dr:abc123" \
  --no-sharing-enabled
```

Next generation Resilience Hub immediately stops evaluating services in member accounts against the policy. It then clears the policy from the member services that were using it, so those services no longer show an attachment that has no effect.

Service owners can apply a different policy at any time.

The policy's timeline records changes to sharing, and the account that owns the policy can review it. For more information, see [Tracking changes to a shared policy](next-gen-org-policy-timeline.md).