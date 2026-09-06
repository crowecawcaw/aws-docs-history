

# Use the migration API
<a name="next-gen-migration-step2"></a>

Next generation Resilience Hub provides migration APIs that handle the transition for you. The `import-app` API creates the service automatically – you don't need to manually create a system or service first.

```
# Import a v1 application to a next generation Resilience Hub service
aws resiliencehubv2 import-app \
  --v1-app-arn "arn:aws:resiliencehub:us-east-1:123456789012:app/my-app:..."

# Import a v1 policy to a next generation Resilience Hub policy
aws resiliencehubv2 import-policy \
  --v1-policy-arn "arn:aws:resiliencehub:us-east-1:123456789012:resiliency-policy/..."
```

The migration API performs the following actions:
+ Creates a service from your v1 application (within a new or existing system)
+ Preserves your input sources and resource configuration
+ Converts your v1 policy to a resilience policy with modular conditions
+ Maintains assessment history for continuity