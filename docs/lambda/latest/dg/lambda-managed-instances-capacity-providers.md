# Capacity providers

A capacity provider is the foundation for running Lambda Managed Instances. It acts as the security boundary for your functions and defines the compute resources that Lambda will provision and manage on your behalf.

When you create a capacity provider, you specify:

- **VPC configuration** - The subnets and security groups where instances will run
- **Permissions** - IAM roles for Lambda to manage EC2 resources
- **Instance requirements** (optional) - Architecture and [instance type](https://aws.amazon.com/lambda/pricing/#:~:text=EPU%20pricing%20applies.-,Management%20Fees,-Pricing%20Example%3A%20High "https://aws.amazon.com/lambda/pricing/#:~:text=EPU%20pricing%20applies.-,Management%20Fees,-Pricing%20Example%3A%20High") preferences
- **Scaling configuration** (optional) - How Lambda scales your instances

## Understanding capacity providers as security boundary

Capacity providers serve as the security boundary for Lambda functions within your VPC, replacing Firecracker-based isolation. Functions execute in containers within instances, but containers do not provide strong security isolation between functions, unlike Firecracker microVMs.

**Key security concepts:**

- **Capacity Provider:** The security boundary that defines trust levels for Lambda functions
- **Container Isolation:** Containers are NOT a security provider - do not rely on them for security between untrusted workloads
- **Trust Separation:** Separate workloads that are not mutually trusted by using different capacity providers

## Creating a capacity provider

You can create a capacity provider using the AWS CLI, AWS Management Console, or AWS SDKs.

**Using AWS CLI:**

```
aws lambda create-capacity-provider \
  --capacity-provider-name my-capacity-provider \
  --vpc-config SubnetIds=subnet-12345,subnet-67890,subnet-11111,SecurityGroupIds=sg-12345 \
  --permissions-config CapacityProviderOperatorRoleArn=arn:aws:iam::123456789012:role/MyOperatorRole \
  --instance-requirements Architectures=x86_64 \
  --capacity-provider-scaling-config ScalingMode=Auto
```

### Required parameters

**CapacityProviderName**

- A unique name for your capacity provider
- Must be unique within your AWS account

**VpcConfig**

- **SubnetIds** (required): At least one subnet, maximum of 16. Use subnets across multiple Availability Zones for resiliency
- **SecurityGroupIds** (optional): Security groups for your instances. Defaults to the VPC default security group if not specified

**PermissionsConfig**

- **CapacityProviderOperatorRoleArn** (required): IAM role that allows Lambda to manage EC2 resources in your capacity provider

### Optional parameters

**InstanceRequirements**

Specify the architecture and [instance types](https://aws.amazon.com/lambda/pricing/#:~:text=EPU%20pricing%20applies.-,Management%20Fees,-Pricing%20Example%3A%20High "https://aws.amazon.com/lambda/pricing/#:~:text=EPU%20pricing%20applies.-,Management%20Fees,-Pricing%20Example%3A%20High") for your capacity provider:

- **Architectures**: Choose `x86_64` or `arm64`. Default is `x86_64`
- **AllowedInstanceTypes**: Specify allowed instance types. Example: `m5.8xlarge`
- **ExcludedInstanceTypes**: Specify excluded instance types using wildcards. You can specify only one of AllowedInstanceTypes or ExcludedInstanceTypes

By default, Lambda chooses the best instance types for your workload. We recommend letting Lambda Managed Instances choose instance types for you, as restricting the number of possible instance types may result in lower availability.

**CapacityProviderScalingConfig**

Configure how Lambda scales your instances:

- **ScalingMode**: Set to `Auto` for automatic scaling or `Manual` for manual control. Default is `Auto`
- **MaxVCpuCount**: Maximum number of vCPUs for the capacity provider. Default is 400.
- **ScalingPolicies**: Define target tracking scaling policies for CPU and memory utilization

**KmsKeyArn**

Specify a AWS KMS key for EBS encryption. Defaults to AWS managed key if not specified.

**Tags**

Add tags to organize and manage your capacity providers.

## Managing capacity providers

### Updating a capacity provider

You can update certain properties of a capacity provider using the `UpdateCapacityProvider` API.

```
aws lambda update-capacity-provider \
  --capacity-provider-name my-capacity-provider \
  --capacity-provider-scaling-config ScalingMode=Auto
```

### Deleting a capacity provider

You can delete a capacity provider when it's no longer needed using the `DeleteCapacityProvider` API.

```
aws lambda delete-capacity-provider \
  --capacity-provider-name my-capacity-provider
```

**Note:** You cannot delete a capacity provider that has function versions attached to it.

### Viewing capacity provider details

Retrieve information about a capacity provider using the `GetCapacityProvider` API.

```
aws lambda get-capacity-provider \
  --capacity-provider-name my-capacity-provider
```

## Capacity provider states

A capacity provider can be in one of the following states:

- **Pending**: The capacity provider is being created
- **Active**: The capacity provider is ready to use
- **Failed**: The capacity provider creation failed
- **Deleting**: The capacity provider is being deleted

## Quotas

- **Maximum capacity providers per account**: 1,000
- **Maximum function versions per capacity provider**: 100 (cannot be increased)

## Best practices

1. **Separate by trust level**: Create different capacity providers for workloads with different security requirements
2. **Use descriptive names**: Name capacity providers to clearly indicate their intended use and trust level (e.g., `production-trusted`, `dev-sandbox`)
3. **Use multiple Availability Zones**: Specify subnets across multiple AZs for high availability
4. **Let Lambda choose instance types**: Unless you have specific hardware requirements, allow Lambda to select the best instance types for optimal availability
5. **Monitor usage**: Use AWS CloudTrail to monitor capacity provider assignments and access patterns

## Next steps

- Learn about [scaling Lambda Managed Instances](lambda-managed-instances-scaling.md "lambda-managed-instances-scaling.md")
- Understand [security and permissions for Lambda Managed Instances](lambda-managed-instances-security.md "lambda-managed-instances-security.md")
- Configure [VPC connectivity for your capacity providers](lambda-managed-instances-networking.md "lambda-managed-instances-networking.md")
- Review runtime-specific guides for [Java](lambda-managed-instances-java-runtime.md "lambda-managed-instances-java-runtime.md"), [Node.js](lambda-managed-instances-nodejs-runtime.md "lambda-managed-instances-nodejs-runtime.md"), and [Python](lambda-managed-instances-python-runtime.md "lambda-managed-instances-python-runtime.md")
