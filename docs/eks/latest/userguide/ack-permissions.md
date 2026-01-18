**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure ACK permissions

ACK requires IAM permissions to create and manage AWS resources on your behalf.
This topic explains how IAM works with ACK and provides guidance on configuring permissions for different use cases.

## How IAM works with ACK

ACK uses IAM roles to authenticate with AWS and perform actions on your resources.
There are two ways to provide permissions to ACK:

**Capability Role**: The IAM role you provide when creating the ACK capability.
This role is used by default for all ACK operations.

**IAM Role Selectors**: Additional IAM roles that can be mapped to specific namespaces or resources.
These roles override the Capability Role for resources in their scope.

When ACK needs to create or manage a resource, it determines which IAM role to use:

1. Check if an IAMRoleSelector matches the resource’s namespace
2. If a match is found, assume that IAM role
3. Otherwise, use the Capability Role

This approach enables flexible permission management from simple single-role setups to complex multi-account, multi-team configurations.

## Getting started: Simple permission setup

For development, testing, or simple use cases, you can add all necessary service permissions directly to the Capability Role.

This approach works well when:

- You’re getting started with ACK
- All resources are in the same AWS account
- A single team manages all ACK resources
- You trust all ACK users to have the same permissions

## Production best practice: IAM Role Selectors

For production environments, use IAM Role Selectors to implement least-privilege access and namespace-level isolation.

When using IAM Role Selectors, the Capability Role only needs `sts:AssumeRole` permission to assume the service-specific roles.
You don’t need to add any AWS service permissions (like S3 or RDS) to the Capability Role itself—those permissions are granted to the individual IAM roles that the Capability Role assumes.

**Choosing between permission models**:

Use **direct permissions** (adding service permissions to the Capability Role) when:

- You’re getting started and want the simplest setup
- All resources are in the same account as your cluster
- You have administrative, cluster-wide permission requirements
- All teams can share the same permissions

Use **IAM Role Selectors** when:

- Managing resources across multiple AWS accounts
- Different teams or namespaces need different permissions
- You need fine-grained access control per namespace
- You want to follow least-privilege security practices

You can start with direct permissions and migrate to IAM Role Selectors later as your requirements grow.

**Why use IAM Role Selectors in production:**

- **Least privilege**: Each namespace gets only the permissions it needs
- **Team isolation**: Team A cannot accidentally use Team B’s permissions
- **Easier auditing**: Clear mapping of which namespace uses which role
- **Cross-account support**: Required for managing resources in multiple accounts
- **Separation of concerns**: Different services or environments use different roles

### Basic IAM Role Selector setup

**Step 1: Create a service-specific IAM role**

Create an IAM role with permissions for specific AWS services:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": "*"
    }
  ]
}
```

Configure the trust policy to allow the Capability Role to assume it:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ACKCapabilityRole"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Step 2: Grant AssumeRole permission to Capability Role**

Add permission to the Capability Role to assume the service-specific role:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::111122223333:role/ACK-S3-Role"
    }
  ]
}
```

**Step 3: Create IAMRoleSelector**

Map the IAM role to a namespace:

```
 apiVersion: services.k8s.aws/v1alpha1
kind: IAMRoleSelector
metadata:
  name: s3-namespace-config
spec:
  arn: arn:aws:iam::111122223333:role/ACK-S3-Role
  namespaceSelector:
    names:
      - s3-resources
```

**Step 4: Create resources in the mapped namespace**

Resources in the `s3-resources` namespace automatically use the specified role:

```
 apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: my-bucket
  namespace: s3-resources
spec:
  name: my-production-bucket
```

## Multi-account management

Use IAM Role Selectors to manage resources across multiple AWS accounts.

**Step 1: Create cross-account IAM role**

In the target account (444455556666), create a role that trusts the source account’s Capability Role:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ACKCapabilityRole"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Attach service-specific permissions to this role.

**Step 2: Grant AssumeRole permission**

In the source account (111122223333), allow the Capability Role to assume the target account role:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::444455556666:role/ACKTargetAccountRole"
    }
  ]
}
```

**Step 3: Create IAMRoleSelector**

Map the cross-account role to a namespace:

```
 apiVersion: services.k8s.aws/v1alpha1
kind: IAMRoleSelector
metadata:
  name: production-account-config
spec:
  arn: arn:aws:iam::444455556666:role/ACKTargetAccountRole
  namespaceSelector:
    names:
      - production
```

**Step 4: Create resources**

Resources in the `production` namespace are created in the target account:

```
 apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: my-bucket
  namespace: production
spec:
  name: my-cross-account-bucket
```

## Advanced IAM Role Selector patterns

For advanced configuration including label selectors, resource-specific role mapping, and additional examples, see [ACK IRSA Documentation](https://aws-controllers-k8s.github.io/community/docs/user-docs/irsa/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/irsa/").

## Next steps

- [ACK concepts](ack-concepts.md "ack-concepts.md") - Understand ACK concepts and resource lifecycle
- [ACK concepts](ack-concepts.md "ack-concepts.md") - Learn about resource adoption and deletion policies
- [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md") - Understand security best practices for capabilities
