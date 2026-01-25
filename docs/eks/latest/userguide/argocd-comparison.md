**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Comparing EKS Capability for Argo CD to self-managed Argo CD

The EKS Capability for Argo CD provides a fully managed Argo CD experience that runs in EKS.
For a general comparison of EKS Capabilities vs self-managed solutions, see [EKS Capabilities considerations](capabilities-considerations.md "capabilities-considerations.md").
This topic focuses on Argo CD-specific differences, including authentication, multi-cluster management, and upstream feature support.

## Differences from upstream Argo CD

The EKS Capability for Argo CD is based on upstream Argo CD but differs in how it’s accessed, configured, and integrated with AWS services.

**RBAC and authentication**: The capability comes with three RBAC roles (admin, editor, viewer) and uses AWS Identity Center for authentication instead of Argo CD’s built-in authentication. Configure role mappings through the capability’s `rbacRoleMapping` parameter to map Identity Center groups to Argo CD roles, not through Argo CD’s `argocd-rbac-cm` ConfigMap. The Argo CD UI is hosted with its own direct URL (find it in the EKS console under your cluster’s Capabilities tab), and API access uses AWS authentication and authorization through IAM.

**Cluster configuration**: The capability does not automatically configure local cluster or hub-and-spoke topologies. You configure your deployment target clusters and EKS access entries. The capability supports only Amazon EKS clusters as deployment targets using EKS cluster ARNs (not Kubernetes API server URLs). The capability does not automatically add the local cluster (`kubernetes.default.svc`) as a deployment target—to deploy to the same cluster where the capability is created, explicitly register that cluster using its ARN.

**Simplified remote cluster access**: The capability simplifies multi-cluster deployments by using EKS Access Entries to grant Argo CD access to remote clusters, eliminating the need to configure IAM Roles for Service Accounts (IRSA) or set up cross-account IAM role assumptions. The capability also provides transparent access to fully private EKS clusters without requiring VPC peering or specialized networking configuration—AWS manages connectivity between the Argo CD capability and private remote clusters automatically.

**Direct AWS service integration**: The capability provides direct integration with AWS services through the Capability Role’s IAM permissions. You can reference CodeCommit repositories, ECR Helm charts, and CodeConnections directly in Application resources without creating Repository configurations. This simplifies authentication and eliminates the need to manage separate credentials for AWS services. See [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md") for details.

**Namespace support**: The capability requires you to specify a single namespace where Argo CD Application, ApplicationSet, and AppProject custom resources must be created.

###### Note

This namespace restriction only applies to Argo CD’s own custom resources (Application, ApplicationSet, AppProject).
Your application workloads can be deployed to any namespace in any target cluster.
For example, if you create the capability with namespace `argocd`, all Application CRs must be created in the `argocd` namespace, but those Applications can deploy workloads to `default`, `production`, `staging`, or any other namespace.

###### Note

The managed capability has specific requirements for CLI usage and AppProject configuration:

- When using the Argo CD CLI, specify applications with the namespace prefix: `argocd app sync namespace/appname`
- AppProject resources must specify `.spec.sourceNamespaces` to define which namespaces the project can watch for Applications (typically set to the namespace you specified when creating the capability)
- Resource tracking annotations use the format: `namespace_appname:group/kind:namespace/name`

**Unsupported features**: The following features are not available in the managed capability:

- Config Management Plugins (CMPs) for custom manifest generation
- Custom Lua scripts for resource health assessment (built-in health checks for standard resources are supported)
- The Notifications controller
- Custom SSO providers (only AWS Identity Center is supported, including third-party federated identity through AWS Identity Center)
- UI extensions and custom banners
- Direct access to `argocd-cm`, `argocd-params`, and other configuration ConfigMaps
- Modifying the sync timeout (fixed at 120 seconds)

**Compatibility**: Applications and ApplicationSets work identically to upstream Argo CD with no changes to your manifests. The capability uses the same Kubernetes APIs and CRDs, so tools like `kubectl` work the same way. The capability fully supports Applications and ApplicationSets, GitOps workflows with automatic sync, multi-cluster deployments, sync policies (automated, prune, self-heal), sync waves and hooks, health assessment for standard Kubernetes resources, rollback capabilities, Git repository sources (HTTPS and SSH), Helm, Kustomize, and plain YAML manifests, GitHub app credentials, projects for multi-tenancy, and resource exclusions and inclusions.

## Using the Argo CD CLI with the managed capability

The Argo CD CLI works the same as upstream Argo CD for most operations, but authentication and cluster registration differ.

### Prerequisites

Install the Argo CD CLI following the [upstream installation instructions](https://argo-cd.readthedocs.io/en/stable/cli_installation/ "https://argo-cd.readthedocs.io/en/stable/cli_installation/").

### Configuration

Configure the CLI using environment variables:

1. Get the Argo CD server URL from the EKS console (under your cluster’s **Capabilities** tab), or using the AWS CLI.
   The `https://` prefix must be removed:

```
export ARGOCD_SERVER=$(aws eks describe-capability \
  --cluster-name `my-cluster` \
  --capability-name `my-argocd` \
  --query 'capability.configuration.argoCd.serverUrl' \
  --output text \
  --region `region-code` | sed 's|^https://||')
```

2. Generate an account token from the Argo CD UI (**Settings** → **Accounts** → **admin** → **Generate New Token**), then set it as an environment variable:

```
export ARGOCD_AUTH_TOKEN="your-token-here"
```

###### Important

This configuration uses the admin account token for initial setup and development workflows.
For production use cases, use project-scoped roles and tokens to follow the principle of least privilege.
For more information about configuring project roles and RBAC, see [Configure Argo CD permissions](argocd-permissions.md "argocd-permissions.md").

1. Set the required gRPC option:

```
export ARGOCD_OPTS="--grpc-web"
```

With these environment variables set, you can use the Argo CD CLI without the `argocd login` command.

### Key differences

The managed capability has the following CLI limitations:

- `argocd admin` commands are not supported (they require direct pod access)
- `argocd login` is not supported (use account or project tokens instead)
- `argocd cluster add` requires the `--aws-cluster-name` flag with the EKS cluster ARN

### Example: Register a cluster

Register an EKS cluster for application deployment:

```
# Get the cluster ARN
CLUSTER_ARN=$(aws eks describe-cluster \
  --name `my-cluster` \
  --query 'cluster.arn' \
  --output text)

# Register the cluster
argocd cluster add $CLUSTER_ARN \
  --aws-cluster-name $CLUSTER_ARN \
  --name in-cluster \
  --project default
```

For complete Argo CD CLI documentation, see the [Argo CD CLI reference](https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/ "https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/").

## Migration Path

You can migrate from self-managed Argo CD to the managed capability:

1. Review your current Argo CD configuration for unsupported features (Notifications controller, CMPs, custom health checks, UI extensions)
2. Scale your self-managed Argo CD controllers to zero replicas to prevent conflicts
3. Create an Argo CD capability resource on your cluster
4. Export your existing Applications, ApplicationSets, and AppProjects
5. Migrate repository credentials, cluster secrets, and repository credential templates (repocreds)
6. If using GPG keys, TLS certificates, or SSH known hosts, migrate these configurations as well
7. Update `destination.server` fields to use cluster names or EKS cluster ARNs
8. Apply them to the managed Argo CD instance
9. Verify applications are syncing correctly
10. Decommission your self-managed Argo CD installation

The managed capability uses the same Argo CD APIs and resource definitions, so your existing manifests work with minimal modification.

## Next steps

- [Create an Argo CD capability](create-argocd-capability.md "create-argocd-capability.md") - Create an Argo CD capability resource
- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") - Deploy your first application
- [Argo CD considerations](argocd-considerations.md "argocd-considerations.md") - Configure AWS Identity Center integration
