**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Security considerations for EKS Capabilities

This topic covers important security considerations for EKS Capabilities, including IAM role configuration, Kubernetes permissions, and architectural patterns for multi-cluster deployments and cross-account AWS resource management.

EKS Capabilities use a combination of IAM roles, EKS access entries, and Kubernetes RBAC to provide secure access to AWS services, in-cluster Kubernetes resources, and integrations with AWS CodeConnections, AWS Secrets Manager, and other AWS services.

## Capability IAM role

When you create a capability, you provide an IAM capability role that EKS uses to perform actions on your behalf. This role must:

- Be in the same AWS account as the cluster and capability resource
- Have a trust policy allowing the `capabilities.eks.amazonaws.com` service principal to assume the role
- Have IAM permissions appropriate for the capability type and use case, depending on your requirements. For detailed information about required IAM permissions, see [Connect to Git repositories with AWS CodeConnections](integration-codeconnections.md "integration-codeconnections.md"), [Manage application secrets with AWS Secrets Manager](integration-secrets-manager.md "integration-secrets-manager.md"), and [Configure ACK permissions](ack-permissions.md "ack-permissions.md")

It is a best practice to consider the scope of privileges required for your specific use case and grant only those permissions necessary to meet your requirements.
For example, when using the EKS Capability for Kube Resource Orchestrator, no IAM permissions may be required, while when using the EKS Capability for AWS Controllers for Kubernetes you may grant full access to one or more AWS services.

###### Important

While some use cases may warrant the use of broad administrative privileges, follow the principle of least privilege by granting only the minimum IAM permissions required for your specific use case, restricting access to specific resources using ARNs and condition keys rather than using wildcard permissions.

For detailed information about creating and configuring capability IAM roles, see [Amazon EKS capability IAM role](capability-role.md "capability-role.md").

## EKS access entries

When you create a capability with an IAM role, Amazon EKS automatically creates an access entry for that role on your cluster.
This access entry grants the capability baseline Kubernetes permissions to function.

###### Note

Access entries are created for the cluster where the capability is created.
For Argo CD deployments to remote clusters, you must create access entries on those clusters with appropriate permissions for the Argo CD capability to deploy and manage applications.

The access entry includes:

- The IAM role ARN as the principal
- Capability-specific access entry policies that grant baseline Kubernetes permissions
- Appropriate scope (cluster-wide or namespace-scoped) based on the capability type

###### Note

For Argo CD, namespace-scoped permissions are granted to the namespace specified in the capability configuration (defaults to `argocd`).

**Default access entry policies by capability**

Each capability type grants the capability role the required permissions, setting different default access entry policies as follows:

**kro**

- `arn:aws:eks::aws:cluster-access-policy/AmazonEKSKROPolicy` (cluster-scoped)

Grants permissions to watch and manage ResourceGraphDefinitions and create instances of custom resources defined by RGDs.

**ACK**

- `arn:aws:eks::aws:cluster-access-policy/AmazonEKSACKPolicy` (cluster-scoped)

Grants permissions to create, read, update, and delete ACK custom resources across all namespaces.

**Argo CD**

- `arn:aws:eks::aws:cluster-access-policy/AmazonEKSArgoCDClusterPolicy` (cluster-scoped)

Grants cluster-level permissions for Argo CD to discover resources and manage cluster-scoped objects.

- `arn:aws:eks::aws:cluster-access-policy/AmazonEKSArgoCDPolicy` (namespace-scoped)

Grants namespace-level permissions for Argo CD to deploy and manage applications. Scoped to the namespace specified in the capability configuration (defaults to `argocd`).

See [Review access policy permissions](access-policy-permissions.md "access-policy-permissions.md") for more detailed information.

## Additional Kubernetes permissions

Some capabilities may require additional Kubernetes permissions beyond the default access entry policies. You can grant these permissions using either:

- **Access entry policies**: Associate additional managed policies to the access entry
- **Kubernetes RBAC**: Create `Role` or `ClusterRole` bindings for the capability’s Kubernetes user

**ACK secret reader permissions**

Some ACK controllers need to read Kubernetes secrets to retrieve sensitive data like database passwords. The following ACK controllers require secret read access:

- `acm`, `acmpca`, `documentdb`, `memorydb`, `mq`, `rds`, `secretsmanager`

To grant secret read permissions:

1. Associate the `arn:aws:eks::aws:cluster-access-policy/AmazonEKSSecretReaderPolicy` access entry policy to the capability’s access entry
2. Scope the policy to specific namespaces where ACK resources will reference secrets, or grant cluster-wide access

###### Important

Secret read permissions are scoped to the namespaces you specify when associating the access entry policy. This allows you to limit which secrets the capability can access.

**kro arbitrary resource permissions**

kro requires permissions to create and manage the resources defined in your ResourceGraphDefinitions. By default, kro can only watch and manage RGDs themselves.

To grant kro permissions to create resources:

**Option 1: Access entry policies**

Associate pre-defined access entry policies like `AmazonEKSAdminPolicy` or `AmazonEKSEditPolicy` to the capability’s access entry.

**Option 2: Kubernetes RBAC**

Create a `ClusterRoleBinding` that grants the capability’s Kubernetes user the necessary permissions:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kro-cluster-admin
subjects:
- kind: User
  name: arn:aws:sts::111122223333:assumed-role/my-kro-role/KRO
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

###### Note

The Kubernetes user name for kro follows the pattern: `arn:aws:sts::ACCOUNT_ID:assumed-role/ROLE_NAME/KRO`

The session name `/KRO` (uppercase) is automatically set by the EKS kro capability.

## IAM permissions required by capability

**kro (Kube Resource Orchestrator)**

No IAM permissions required. You can create a capability role with no attached policies. kro only requires Kubernetes RBAC permissions.

**ACK (AWS Controllers for Kubernetes)**

Requires permissions to manage the AWS resources that ACK will create and manage. You should scope permissions to specific services, actions, and resources based on your requirements. For detailed information about configuring ACK permissions, including production best practices with IAM Role Selectors, see [Configure ACK permissions](ack-permissions.md "ack-permissions.md").

**Argo CD**

No IAM permissions are required by default. Optional permissions may be needed for:

- AWS Secrets Manager: If storing Git repository credentials in Secrets Manager
- AWS CodeConnections: If using CodeConnections for Git repository authentication
- Amazon ECR: If using Helm charts stored in OCI format in Amazon ECR

## Security best practices

### IAM least privilege

Grant your capability resources only the permissions required for your use case.
This does not mean you cannot grant broad administrative permissions to your capabilities if required.
In such cases, you should govern access to those resources appropriately.

**Capability roles**:

- **ACK**: When possible, limit IAM permissions to specific AWS services and resources your teams need, based on use case and requirements
- **Argo CD**: Restrict access to specific Git repositories and Kubernetes namespaces
- **kro**: Requires a capability role for the trust policy, but no IAM permissions are needed (uses cluster RBAC only)

**Example**: Instead of `"Resource": "*"`, specify patterns for specific resources or groups of resources.

```
 "Resource": [
  "arn:aws:s3:::my-app-*",
  "arn:aws:rds:us-west-2:111122223333:db:prod-*"
]
```

Use IAM condition keys to further restrict access:

```
 "Condition": {
  "StringEquals": {
    "aws:ResourceTag/Environment": "production"
  }
}
```

For additional IAM configuration information, see the considerations section for each capability.

### Namespace isolation for Argo CD secrets

The managed Argo CD capability has access to all Kubernetes secrets within its configured namespace (default: `argocd`).
To maintain optimal security posture, follow these namespace isolation practices:

- Keep only Argo CD-relevant secrets within the Argo CD namespace
- Avoid storing unrelated application secrets in the same namespace as Argo CD
- Use separate namespaces for application secrets that are not required for Argo CD operations

This isolation ensures that Argo CD’s secret access is limited to only the credentials it needs for Git repository authentication and other Argo CD-specific operations.

### Kubernetes RBAC

Control which users and service accounts can create and manage capability resources.
It is a best practice to deploy capability resources in dedicated namespaces with appropriate RBAC policies.

Example: RBAC Role to work with ACK, allowing for S3 Bucket resource management in the `app-team` namespace:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: ack-s3-manager
  namespace: app-team
rules:
- apiGroups: ["s3.services.k8s.aws"]
  resources: ["buckets"]
  verbs: ["get", "list", "create", "update", "delete"]
```

### Audit logging

**CloudTrail**: All EKS Capability API operations (create, update, delete) are logged to AWS CloudTrail.

Enable CloudTrail logging to track:

- Who created or modified capabilities
- When capability configurations changed
- What capability roles are in use

### Network access and VPC endpoints

#### Private Argo CD API access

You can restrict access to the Argo CD API server by associating one or more VPC endpoints with the hosted Argo CD endpoint.
This enables private connectivity from within your VPC without traversing the public internet.
The VPC endpoint provides access to both the Argo CD web UI and the Argo CD API (including CLI access).

###### Note

VPC endpoints connected to hosted Argo CD API endpoints (using eks-capabilities.`region`.amazonaws.com) do not support VPC endpoint policies.

#### Deploying to private clusters

The Argo CD capability can deploy applications to fully private EKS clusters, providing a significant operational benefit by eliminating the need for VPC peering or complex networking configurations.
However, when designing this architecture, consider that Argo CD will pull configuration from Git repositories (which may be public) and apply it to your private clusters.

Ensure you:

- Use private Git repositories for sensitive workloads
- Implement proper Git repository access controls and authentication
- Review and approve changes through pull requests before merging
- Consider using Argo CD’s sync windows to control when deployments can occur
- Monitor Argo CD audit logs for unauthorized configuration changes

### Compliance

EKS Capabilities are fully managed and have the compliance certifications of Amazon EKS.

For current compliance information, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

## Next steps

- [Configure ACK permissions](ack-permissions.md "ack-permissions.md") - Configure IAM permissions for ACK
- [Configure kro permissions](kro-permissions.md "kro-permissions.md") - Configure Kubernetes RBAC for kro
- [Configure Argo CD permissions](argocd-permissions.md "argocd-permissions.md") - Configure Identity Center integration for Argo CD
- [Troubleshooting EKS Capabilities](capabilities-troubleshooting.md "capabilities-troubleshooting.md") - Troubleshoot security and permission issues
