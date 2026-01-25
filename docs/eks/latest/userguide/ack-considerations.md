**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# ACK considerations for EKS

This topic covers important considerations for using the EKS Capability for ACK, including IAM configuration, multi-account patterns, and integration with other EKS capabilities.

## IAM configuration patterns

The ACK capability uses an IAM Capability Role to authenticate with AWS.
Choose the right IAM pattern based on your requirements.

### Simple: Single Capability Role

For development, testing, or simple use cases, grant all necessary permissions directly to the Capability Role.

**When to use**:

- Getting started with ACK
- Single-account deployments
- All resources managed by one team
- Development and testing environments

**Example**: Add S3 and RDS permissions to your Capability Role with resource tagging conditions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:*"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": ["us-west-2", "us-east-1"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": ["rds:*"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": ["us-west-2", "us-east-1"]
        },
      }
    }
  ]
}
```

This example limits S3 and RDS operations to specific regions and requires RDS resources to have a `ManagedBy: ACK` tag.

### Production: IAM Role Selectors

For production environments, use IAM Role Selectors to implement least-privilege access and namespace-level isolation.

**When to use**:

- Production environments
- Multi-team clusters
- Multi-account resource management
- Least-privilege security requirements
- Different services need different permissions

**Benefits**:

- Each namespace gets only the permissions it needs
- Team isolation - Team A cannot use Team B’s permissions
- Easier auditing and compliance
- Required for cross-account resource management

For detailed IAM Role Selector configuration, see [Configure ACK permissions](ack-permissions.md "ack-permissions.md").

## Integration with other EKS capabilities

### GitOps with Argo CD

Use the EKS Capability for Argo CD to deploy ACK resources from Git repositories, enabling GitOps workflows for infrastructure management.

**Considerations**:

- Store ACK resources alongside application manifests for end-to-end GitOps
- Organize by environment, service, or resource type based on your team structure
- Use Argo CD’s automated sync for continuous reconciliation
- Enable pruning to automatically remove deleted resources
- Consider hub-and-spoke patterns for multi-cluster infrastructure management

GitOps provides audit trails, rollback capabilities, and declarative infrastructure management.
For more on Argo CD, see [Working with Argo CD](working-with-argocd.md "working-with-argocd.md").

### Resource composition with kro

Use the EKS Capability for kro (Kube Resource Orchestrator) to compose multiple ACK resources into higher-level abstractions and custom APIs.

**When to use kro with ACK**:

- Create reusable patterns for common infrastructure stacks (database + backup + monitoring)
- Build self-service platforms with simplified APIs for application teams
- Manage resource dependencies and pass values between resources (S3 bucket ARN to Lambda function)
- Standardize infrastructure configurations across teams
- Reduce complexity by hiding implementation details behind custom resources

**Example patterns**:

- Application stack: S3 bucket + SQS queue + notification configuration
- Database setup: RDS instance + parameter group + security group + secrets
- Networking: VPC + subnets + route tables + security groups

kro handles dependency ordering, status propagation, and lifecycle management for composed resources.
For more on kro, see [kro concepts](kro-concepts.md "kro-concepts.md").

## Organizing your resources

Organize ACK resources using Kubernetes namespaces and AWS resource tags for better management, access control, and cost tracking.

### Namespace organization

Use Kubernetes namespaces to logically separate ACK resources by environment (production, staging, development), team (platform, data, ml), or application.

**Benefits**:

- Namespace-scoped RBAC for access control
- Set default regions per namespace using annotations
- Easier resource management and cleanup
- Logical separation aligned with organizational structure

### Resource tagging

The EKS ACK capability automatically applies default tags to all AWS resources it creates.
These tags differ from self-managed ACK and provide enhanced traceability.

**Default tags applied by the capability**:

| Tag Key                        | Description                                                   |
| ------------------------------ | ------------------------------------------------------------- |
| `eks:controller-version`       | The version of the ACK controller                             |
| `eks:kubernetes-namespace`     | The Kubernetes namespace of the ACK resource                  |
| `eks:kubernetes-resource-name` | The name of the Kubernetes resource                           |
| `eks:kubernetes-api-group`     | The Kubernetes API group (for example, `s3.services.k8s.aws`) |
| `eks:eks-capability-arn`       | The ARN of the EKS ACK capability                             |

###### Note

Self-managed ACK uses different default tags: `services.k8s.aws/controller-version` and `services.k8s.aws/namespace`.
The capability’s tags use the `eks:` prefix for consistency with other EKS features.

**Additional recommended tags**:

Add custom tags for cost allocation, ownership tracking, and organizational purposes:

- Environment (Production, Staging, Development)
- Team or department ownership
- Cost center for billing allocation
- Application or service name

## Migration from other Infrastructure-as-code tools

Many organizations are finding value in standardizing on Kubernetes beyond their workload orchestration.
Migrating infrastructure and AWS resource management to ACK allows you to standardize infrastructure management using Kubernetes APIs alongside your application workloads.

**Benefits of standardizing on Kubernetes for infrastructure**:

- **Single source of truth**: Manage both applications and infrastructure in Kubernetes, enabling an end-to-end GitOps practice
- **Unified tooling**: Teams use Kubernetes resources and tooling rather than learning multiple tools and frameworks
- **Consistent reconciliation**: ACK continuously reconciles AWS resources like Kubernetes does for workloads, detecting and correcting drift compared to imperative tools
- **Native compositions**: With kro and ACK together, reference AWS resources directly in application and resource manifests, passing connection strings and ARNs between resources
- **Simplified operations**: One control plane for deployments, rollbacks, and observability across your entire system

ACK supports adopting existing AWS resources without recreating them, enabling zero-downtime migration from CloudFormation, Terraform, or resources external to the cluster.

**Adopt an existing resource**:

```
apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: existing-bucket
  annotations:
    services.k8s.aws/adoption-policy: "adopt-or-create"
spec:
  name: my-existing-bucket-name
```

Once adopted, the resource is managed by ACK and can be updated through Kubernetes manifests.
You can migrate incrementally, adopting resources as needed while maintaining existing IaC tools for other resources.

ACK also supports read-only resources. For resources managed by other teams or tools that you want to reference but not modify, combine adoption with the `retain` deletion policy and grant only read IAM permissions.
This allows applications to discover shared infrastructure (VPCs, IAM roles, KMS keys) through Kubernetes APIs without risking modifications.

For more on resource adoption, see [ACK concepts](ack-concepts.md "ack-concepts.md").

## Deletion policies

Deletion policies control what happens to AWS resources when you delete the corresponding Kubernetes resource.
Choose the right policy based on the resource lifecycle and your operational requirements.

### Delete (default)

The AWS resource is deleted when you delete the Kubernetes resource.
This maintains consistency between your cluster and AWS, ensuring resources don’t accumulate.

**When to use delete**:

- Development and testing environments where cleanup is important
- Ephemeral resources tied to application lifecycle (test databases, temporary buckets)
- Resources that should not outlive the application (SQS queues, ElastiCache clusters)
- Cost optimization - automatically clean up unused resources
- Environments managed with GitOps where resource removal from Git should delete the infrastructure

The default delete policy aligns with Kubernetes' declarative model: what’s in the cluster matches what exists in AWS.

### Retain

The AWS resource is kept when you delete the Kubernetes resource.
This protects critical data and allows resources to outlive their Kubernetes representation.

**When to use retain**:

- Production databases with critical data that must survive cluster changes
- Long-term storage buckets with compliance or audit requirements
- Shared resources used by multiple applications or teams
- Resources being migrated to different management tools
- Disaster recovery scenarios where you want to preserve infrastructure
- Resources with complex dependencies that require careful decommissioning

```
apiVersion: rds.services.k8s.aws/v1alpha1
kind: DBInstance
metadata:
  name: production-db
  annotations:
    services.k8s.aws/deletion-policy: "retain"
spec:
  dbInstanceIdentifier: prod-db
  # ... configuration
```

###### Important

Retained resources continue to incur AWS costs and must be manually deleted from AWS when no longer needed.
Use resource tagging to track retained resources for cleanup.

For more on deletion policies, see [ACK concepts](ack-concepts.md "ack-concepts.md").

## Upstream documentation

For detailed information on using ACK:

- [ACK usage guide](https://aws-controllers-k8s.github.io/community/docs/user-docs/usage/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/usage/") - Creating and managing resources
- [ACK API reference](https://aws-controllers-k8s.github.io/community/reference/ "https://aws-controllers-k8s.github.io/community/reference/") - Complete API documentation for all services
- [ACK documentation](https://aws-controllers-k8s.github.io/community/docs/ "https://aws-controllers-k8s.github.io/community/docs/") - Comprehensive user documentation

## Next steps

- [Configure ACK permissions](ack-permissions.md "ack-permissions.md") - Configure IAM permissions and multi-account patterns
- [ACK concepts](ack-concepts.md "ack-concepts.md") - Understand ACK concepts and resource lifecycle
- [Troubleshoot issues with ACK capabilities](ack-troubleshooting.md "ack-troubleshooting.md") - Troubleshoot ACK issues
- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") - Deploy ACK resources with GitOps
- [kro concepts](kro-concepts.md "kro-concepts.md") - Compose ACK resources into higher-level abstractions
