

# Run your first failure mode assessment
<a name="next-gen-migration-step3"></a>

After migration, run a failure mode assessment to see the enhanced output.

```
aws resiliencehubv2 start-failure-mode-assessment \
  --service-arn "arn:aws:resiliencehub:..."
```

The failure mode findings include detailed reasoning specific to your architecture, recommendations with cost and complexity guidance, and policy mapping showing which requirements are at risk.