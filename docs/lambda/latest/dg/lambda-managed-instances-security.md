# Security and permissions

Lambda Managed Instances use **capacity providers as trust boundaries**. Functions execute in containers within these instances, but containers do not provide security isolation between workloads. All functions assigned to the same capacity provider must be mutually trusted.

## Key Security Concepts

- **Capacity Provider**: The security boundary that defines trust levels for Lambda functions
- **Container Isolation**: Containers are not a security boundary - do not rely on them for security between untrusted workloads
- **Trust Separation**: Separate workloads that are not mutually trusted by using different capacity providers

## Required Permissions

### PassCapacityProvider Action

Users need the `lambda:PassCapacityProvider` permission to assign functions to capacity providers. This permission acts as a security gate, ensuring only authorized users can place functions in specific capacity providers.

Account administrators control which functions can use specific capacity providers through the `lambda:PassCapacityProvider` IAM action. This action is required when:

- Creating functions that use Lambda Managed Instances
- Updating function configurations to use a capacity provider
- Deploying functions via infrastructure as code

**Example IAM Policy**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "lambda:PassCapacityProvider",
      "Resource": "arn:aws:lambda:*:*:capacity-provider:trusted-workloads-*"
    }
  ]
}
```

### Service-Linked Role

AWS Lambda uses the `AWSServiceRoleForLambda` service-linked role to manage Lambda Managed Instances ec2 resources in your capacity providers.

## Best Practices

1. **Separate by Trust Level**: Create different capacity providers for workloads with different security requirements
2. **Use Descriptive Names**: Name capacity providers to clearly indicate their intended use and trust level (e.g., `production-trusted`, `dev-sandbox`)
3. **Apply Least Privilege**: Grant `PassCapacityProvider` permissions only for necessary capacity providers
4. **Monitor Usage**: Use AWS CloudTrail to monitor capacity provider assignments and access patterns

## Next steps

- Learn about [capacity providers for Lambda Managed Instances](lambda-managed-instances-capacity-providers.md "lambda-managed-instances-capacity-providers.md")
- Understand [scaling for Lambda Managed Instances](lambda-managed-instances-scaling.md "lambda-managed-instances-scaling.md")
- Configure [VPC connectivity for your capacity providers](lambda-managed-instances-networking.md "lambda-managed-instances-networking.md")
- Review runtime-specific guides for [Java](lambda-managed-instances-java-runtime.md "lambda-managed-instances-java-runtime.md"), [Node.js](lambda-managed-instances-nodejs-runtime.md "lambda-managed-instances-nodejs-runtime.md"), and [Python](lambda-managed-instances-python-runtime.md "lambda-managed-instances-python-runtime.md")
