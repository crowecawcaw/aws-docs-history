**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Argo CD considerations

This topic covers important considerations for using the EKS Capability for Argo CD, including planning, permissions, authentication, and multi-cluster deployment patterns.

## Planning

Before deploying Argo CD, consider the following:

**Repository strategy**: Determine where your application manifests will be stored (CodeCommit, GitHub, GitLab, Bitbucket).
Plan your repository structure and branching strategy for different environments.

**RBAC strategy**: Plan which teams or users should have admin, editor, or viewer access.
Map these to AWS Identity Center groups or Argo CD roles.

**Multi-cluster architecture**: Determine if you’ll manage multiple clusters from a single Argo CD instance.
Consider using a dedicated management cluster for Argo CD.

**Application organization**: Plan how you’ll structure Applications and ApplicationSets.
Consider using projects to organize applications by team or environment.

**Sync policies**: Decide whether applications should sync automatically or require manual approval.
Automated sync is common for development, manual for production.

## Permissions

For detailed information about IAM Capability Roles, trust policies, and security best practices, see [Amazon EKS capability IAM role](capability-role.md "capability-role.md") and [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md").

### IAM Capability Role overview

When you create an Argo CD capability resource, you provide an IAM Capability Role.
Unlike ACK, Argo CD primarily manages Kubernetes resources, not AWS resources directly.
However, the IAM Capability Role is required for:

- Accessing private Git repositories in CodeCommit
- Integrating with AWS Identity Center for authentication
- Accessing secrets in AWS Secrets Manager (if configured)
- Cross-cluster deployments to other EKS clusters

### CodeCommit integration

If you’re using CodeCommit repositories, attach a policy with read permissions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "codecommit:GitPull"
      ],
      "Resource": "*"
    }
  ]
}
```

###### Important

For production use, restrict the `Resource` field to specific repository ARNs instead of using `"*"`.

Example:

```
"Resource": "arn:aws:codecommit:us-west-2:111122223333:my-app-repo"
```

This limits the Argo CD capability’s access to only the repositories it needs to manage.

### Secrets Manager integration

If you’re storing repository credentials in Secrets Manager, attach the managed policy for read access:

```
arn:aws:iam::aws:policy/AWSSecretsManagerClientReadOnlyAccess
```

This policy includes the necessary permissions: `secretsmanager:GetSecretValue`, `secretsmanager:DescribeSecret`, and KMS decrypt permissions.

### Basic setup

For basic Argo CD functionality with public Git repositories, no additional IAM policies are required beyond the trust policy.

## Authentication

### AWS Identity Center integration

The Argo CD managed capability integrates directly with AWS Identity Center (formerly AWS SSO), enabling you to use your existing identity provider for authentication.

When you configure AWS Identity Center integration:

1. Users access the Argo CD UI through the EKS console
2. They authenticate using AWS Identity Center (which can federate to your corporate identity provider)
3. AWS Identity Center provides user and group information to Argo CD
4. Argo CD maps users and groups to RBAC roles based on your configuration
5. Users see only the applications and resources they have permission to access

### Simplifying access with Identity Center permission sets

AWS Identity Center provides two distinct authentication paths when working with Argo CD:

**Argo CD API authentication**: Identity Center provides SSO authentication to the Argo CD UI and API.
This is configured through the Argo CD capability’s RBAC role mappings.

**EKS cluster access**: The Argo CD capability uses the customer-provided IAM role to authenticate with EKS clusters through access entries.
These access entries can be manually configured to add or remove permissions.

You can use [Identity Center permission sets](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") to simplify identity management by allowing a single identity to access both Argo CD and EKS clusters.
This reduces overhead by requiring you to manage only one identity across both systems, rather than maintaining separate credentials for Argo CD access and cluster access.

### RBAC role mappings

Argo CD has built-in roles that you can map to AWS Identity Center users and groups:

**ADMIN**: Full access to all applications and settings.
Can create, update, and delete applications.
Can manage Argo CD configuration.

**EDITOR**: Can create and modify applications.
Cannot change Argo CD settings or delete applications.

**VIEWER**: Read-only access to applications.
Can view application status and history.
Cannot make changes.

###### Note

Role names are case-sensitive and must be uppercase (ADMIN, EDITOR, VIEWER).

###### Important

EKS Capabilities integration with AWS Identity Center supports up to 1,000 identities per Argo CD capability. An identity can be a user or a group.

## Multi-cluster deployments

The Argo CD managed capability supports multi-cluster deployments, enabling you to manage applications across development, staging, and production clusters from a single Argo CD instance.

### How multi-cluster works

When you register additional clusters with Argo CD:

1. You create cluster secrets that reference target EKS clusters by ARN
2. You create Applications or ApplicationSets that target different clusters
3. Argo CD connects to each cluster to deploy and watch resources
4. You view and manage all clusters from a single Argo CD UI

### Prerequisites for multi-cluster

Before registering additional clusters:

- Create an Access Entry on the target cluster for the Argo CD capability role
- Ensure network connectivity between the Argo CD capability and target clusters
- Verify IAM permissions to access the target clusters

### Register a cluster

Register clusters using Kubernetes Secrets in the `argocd` namespace.

Get the target cluster ARN. Replace `region-code` with the AWS Region that your target cluster is in and replace `target-cluster` with the name of your target cluster.

```
aws eks describe-cluster \
  --region `region-code` \
  --name `target-cluster` \
  --query 'cluster.arn' \
  --output text
```

Create a cluster secret using the cluster ARN:

```
apiVersion: v1
kind: Secret
metadata:
  name: target-cluster
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: target-cluster
  server: arn:aws:eks:us-west-2:111122223333:cluster/target-cluster
  project: default
```

###### Important

Use the EKS cluster ARN in the `server` field, not the Kubernetes API server URL.
The managed capability requires ARNs to identify target clusters.

Apply the secret:

```
kubectl apply -f cluster-secret.yaml
```

### Configure Access Entry on target cluster

The target cluster must have an Access Entry that grants the Argo CD capability role permission to deploy applications. Replace `region-code` with the AWS Region that your target cluster is in, replace `target-cluster` with the name of your target cluster, and replace the ARN with your Argo CD capability role ARN.

```
aws eks create-access-entry \
  --region `region-code` \
  --cluster-name `target-cluster` \
  --principal-arn arn:aws:iam::[.replaceable]`111122223333`:role/`ArgoCDCapabilityRole` \
  --type STANDARD \
  --kubernetes-groups system:masters
```

###### Note

For production use, consider using more restrictive Kubernetes groups instead of `system:masters`.

### Private cluster access

The Argo CD managed capability can deploy to fully private EKS clusters without requiring VPC peering or specialized networking configuration.
AWS manages connectivity between the Argo CD capability and private remote clusters automatically.
Ensure your repository access controls and Argo CD RBAC policies are properly configured.

### Cross-account deployments

For cross-account deployments, add the Argo CD IAM Capability Role from the source account to the target cluster’s EKS Access Entry:

1. In the target account, create an Access Entry on the target EKS cluster
2. Use the Argo CD IAM Capability Role ARN from the source account as the principal
3. Configure appropriate Kubernetes RBAC permissions for the Access Entry
4. Register the target cluster in Argo CD using its EKS cluster ARN

No additional IAM role creation or trust policy configuration is required—EKS Access Entries handle cross-account access.

## Best practices

**Use declarative sources as the source of truth**: Store all your application manifests in declarative sources (Git repositories, Helm registries, or OCI images), enabling version control, audit trails, and collaboration.

**Implement proper RBAC**: Use AWS Identity Center integration to control who can access and manage applications in Argo CD.
Argo CD supports fine-grained access control to resources within Applications (Deployments, Pods, ConfigMaps, Secrets).

**Use ApplicationSets for multi-environment deployments**: Use ApplicationSets to deploy applications across multiple clusters or namespaces with different configurations.

## Lifecycle management

### Application sync policies

Control how Argo CD syncs applications:

**Manual sync**: Applications require manual approval to sync changes.
Recommended for **production** environments.

**Automatic sync**: Applications automatically sync when Git changes are detected.
Common for development and staging environments.

**Self-healing**: Automatically revert manual changes made to the cluster.
Ensures cluster state matches Git.

**Pruning**: Automatically delete resources removed from Git.
Use with caution as this can delete resources.

### Application health

Argo CD continuously monitors application health:

- **Healthy**: All resources are running as expected
- **Progressing**: Resources are being created or updated
- **Degraded**: Some resources are not healthy
- **Suspended**: Application is paused
- **Missing**: Resources are missing from the cluster

### Sync windows

Configure sync windows to control when applications can be synced:

- Allow syncs only during maintenance windows
- Block syncs during business hours
- Schedule automatic syncs for specific times
- Use sync windows in situations where you need to make changes and stop any syncs (break-glass scenarios)

## Webhook configuration for faster sync

By default, Argo CD polls Git repositories every 6 minutes to detect changes.
For more responsive deployments, configure Git webhooks to trigger immediate syncs when changes are pushed.

Webhooks provide several benefits:

- Immediate sync response when code is pushed (seconds vs minutes)
- Reduced polling overhead and improved system performance
- More efficient use of API rate limits
- Better user experience with faster feedback

### Webhook endpoint

The webhook URL follows the pattern `${serverUrl}/api/webhook`, where `serverUrl` is your Argo CD server URL.

For example, if your Argo CD server URL is `https://abc123.eks-capabilities.us-west-2.amazonaws.com`, the webhook URL is:

```
https://abc123.eks-capabilities.us-west-2.amazonaws.com/api/webhook
```

### Configure webhooks by Git provider

**GitHub**: In your repository settings, add a webhook with the Argo CD webhook URL.
Set the content type to `application/json` and select "Just the push event".

**GitLab**: In your project settings, add a webhook with the Argo CD webhook URL.
Enable "Push events" and optionally "Tag push events".

**Bitbucket**: In your repository settings, add a webhook with the Argo CD webhook URL.
Select "Repository push" as the trigger.

**CodeCommit**: Create an Amazon EventBridge rule that triggers on CodeCommit repository state changes and sends notifications to the Argo CD webhook endpoint.

For detailed webhook configuration instructions, see [Argo CD Webhook Configuration](https://argo-cd.readthedocs.io/en/stable/operator-manual/webhook/ "https://argo-cd.readthedocs.io/en/stable/operator-manual/webhook/").

###### Note

Webhooks complement polling—they don’t replace it.
Argo CD continues to poll repositories as a fallback mechanism in case webhook notifications are missed.

## Next steps

- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") - Learn how to create and manage Argo CD Applications
- [Troubleshoot issues with Argo CD capabilities](argocd-troubleshooting.md "argocd-troubleshooting.md") - Troubleshoot Argo CD issues
- [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md") - Manage your Argo CD capability resource
