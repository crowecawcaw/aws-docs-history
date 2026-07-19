# Create a service

A service represents a deployable component. When you create a service, you associate it
with your system and specify where the next generation of Resilience Hub should look for your AWS resources (input
sources).

**Console:**

1. Choose **Services** > **Create
   service**.
2. Enter a name (for example, `api-service`).
3. Select your system.
4. Under **Permission model**, do one of the
   following:

   - To let the console create the required role automatically, choose
     **Create new role**.
   - If you already have a role, choose **Use an existing service
     role** and choose it from the list.

5. Under **Input sources**, add your AWS CloudFormation stack ARN,
   resource tags, or Terraform state file location.
6. Choose **Create**.
   **AWS CLI:**

```
aws resiliencehubv2 create-service \
  --name "api-service" \
  --regions '["us-east-1"]' \
  --associated-systems '[{"systemArn": "arn:aws:resiliencehub:us-east-1:123456789012:system/my-application:abc123"}]' \
  --permission-model '{"invokerRoleName": "AWSResilienceHubAssessmentRole"}'
```
