# Step 6: Run your first resilience test (optional)

Resilience testing helps validate that your service operates and recovers as expected
by injecting controlled faults using AWS Fault Injection Service (AWS FIS). In this step, you
choose a test template, create a test for your service, and start a test run.

###### Console

1. Navigate to your service and choose the Testing tab. You will see recommended resilience
   tests based on your service's architecture and resilience policy.
2. Select a test template (for example, **Availability Zone:
   recovery**). Choose **View details** to learn more about the recommended test.
3. Choose Edit test configuration, provide any required parameters, and save. This creates
   your test from the template - your configuration is saved and reused for future runs. You can
   edit your test configuration anytime.
4. Choose Start test to start a test run.
5. Monitor the run and review whether your recovery objectives were met.

###### AWS CLI

```
# List the available test templates
aws resiliencehubv2 list-test-templates --region us-east-1

# Create a test for your service from a template
aws resiliencehubv2 create-test \
  --test-template-arn "arn:aws:resiliencehub:us-east-1:aws:test-template/aws-az-recovery:rtaz001" \
  --target-identifier "arn:aws:resiliencehub:us-east-1:123456789012:service/api-service:def456" \
  --parameters '{"availabilityZone": ["us-east-1a"]}'

# Start a test run
aws resiliencehubv2 start-test-run --test-id "`test-id`"

# Check the status and results of the test run
aws resiliencehubv2 get-test-run --test-run-id "`test-run-id`"
```

For more information, see
[Resilience testing](next-gen-resilience-testing.md "next-gen-resilience-testing.md").
