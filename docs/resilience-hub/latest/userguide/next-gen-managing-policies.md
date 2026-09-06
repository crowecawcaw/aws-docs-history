

# Managing and updating policies
<a name="next-gen-managing-policies"></a>

You can list, update, and delete resilience policies from the the next generation of Resilience Hub console or AWS CLI.

To list all policies in your account:

```
aws resiliencehubv2 list-policies
```

To update a policy:

```
aws resiliencehubv2 update-policy \
  --policy-arn "arn:aws:resiliencehub:..." \
  --availability-slo '{"target": 99.99}'
```

Changes to a policy take effect on the next failure mode assessment for all services using that policy.

You cannot delete a policy that is currently applied to services or user journeys. Remove all associations first.