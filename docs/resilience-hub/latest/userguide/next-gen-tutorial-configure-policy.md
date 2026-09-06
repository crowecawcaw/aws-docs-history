

# Step 1: Configure a resilience policy
<a name="next-gen-tutorial-configure-policy"></a>

A resilience policy defines the resilience targets for your service, such as availability SLO targets, recovery time objectives (RTO), and recovery point objectives (RPO). In this step, you create a policy and apply it to your service.

**Console:**

1. Choose **Policies** > **Create policy**.

1. Enter a name (for example, `Standard Availability`).

1. Enable **Availability SLO** and set it to `99.9%`.

1. (Optional) Enable **Multi-Region DR** if your application spans Regions.

1. Choose **Create**.

1. Navigate to your service and apply the policy.

**AWS CLI:**

```
# Create the policy
aws resiliencehubv2 create-policy \
  --name "standard-availability" \
  --availability-slo '{"target": 99.9}'

# Apply the policy to your service
aws resiliencehubv2 update-service \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/api-service:def456" \
  --policy-arn "arn:aws:resiliencehub:us-east-1:123456789012:policy/standard-availability:ghi789"
```

For more information about policies, see [Resilience policies](next-gen-resilience-policies.md).