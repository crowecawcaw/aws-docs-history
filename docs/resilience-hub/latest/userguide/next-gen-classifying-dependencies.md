

# Classifying dependencies as hard or soft
<a name="next-gen-classifying-dependencies"></a>

After reviewing discovered dependencies, classify each one to indicate its failure impact:

```
aws resiliencehubv2 update-dependency \
  --service-arn "arn:aws:resiliencehub:..." \
  --dependency-id "{{dependency-id}}" \
  --criticality "HARD" \
  --comment "Payment processing fails completely without Stripe"
```

Use the following guidelines to classify dependencies:


| Classify as | When | Example | 
| --- | --- | --- | 
| Hard | Your service fails completely if this dependency is unavailable | Primary database, payment gateway, authentication service | 
| Soft | Your service degrades but continues operating without this dependency | Analytics API, feature flags, recommendation engine | 