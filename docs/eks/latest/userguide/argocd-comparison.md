

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Comparing EKS Capability for Argo CD to self-managed Argo CD
<a name="argocd-comparison"></a>

The EKS Capability for Argo CD provides a fully managed Argo CD experience that runs in EKS. For a general comparison of EKS Capabilities vs self-managed solutions, see [EKS Capabilities considerations](capabilities-considerations.md). This topic focuses on Argo CD-specific differences, including authentication, multi-cluster management, and upstream feature support.

## Differences from upstream Argo CD
<a name="_differences_from_upstream_argo_cd"></a>

The EKS Capability for Argo CD is based on upstream Argo CD but differs in how it’s accessed, configured, and integrated with AWS services.

 **RBAC and authentication**: The capability comes with three RBAC roles (admin, editor, viewer) and uses AWS Identity Center for authentication instead of Argo CD’s built-in authentication. Configure role mappings through the capability’s `rbacRoleMapping` parameter to map Identity Center groups to Argo CD roles, not through Argo CD’s `argocd-rbac-cm` ConfigMap. The Argo CD UI is hosted with its own direct URL (find it in the EKS console under your cluster’s Capabilities page), and API access uses AWS authentication and authorization through IAM.

 **Cluster configuration**: The capability does not automatically configure local cluster or hub-and-spoke topologies. You configure your deployment target clusters and EKS access entries. The capability supports only Amazon EKS clusters as deployment targets using EKS cluster ARNs (not Kubernetes API server URLs). The capability does not automatically add the local cluster (`kubernetes.default.svc`) as a deployment target—to deploy to the same cluster where the capability is created, explicitly register that cluster using its ARN.

 **Simplified remote cluster access**: The capability simplifies multi-cluster deployments by using EKS Access Entries to grant Argo CD access to remote clusters, eliminating the need to configure IAM Roles for Service Accounts (IRSA) or set up cross-account IAM role assumptions. The capability also provides transparent access to fully private EKS clusters without requiring VPC peering or specialized networking configuration—AWS manages connectivity between the Argo CD capability and private remote clusters automatically.

 **Direct AWS service integration**: The capability provides direct integration with AWS services through the Capability Role’s IAM permissions. You can reference CodeCommit repositories, ECR Helm charts, and CodeConnections directly in Application resources without creating Repository configurations. This simplifies authentication and eliminates the need to manage separate credentials for AWS services. See [Configure repository access](argocd-configure-repositories.md) for details.

 **Source hydrator**: Upstream Argo CD disables the source hydrator by default. To use it with the capability, add `hydrator.enabled: "true"` to `argocd-cmd-params-cm`, and then configure `spec.sourceHydrator` in your Application. The source hydrator renders manifests (for example, from Helm charts or Kustomize overlays) and pushes the rendered output to Git before syncing to the cluster. For instructions on using the source hydrator, see [Push hydrated manifests with the source hydrator](argocd-create-application.md#argocd-source-hydrator).

 **Namespace support**: You specify a primary Argo CD namespace when you create the capability. AppProject resources, Argo CD configuration, and repository and cluster credentials remain in this namespace. You can configure additional namespaces for Application and ApplicationSet resources by using the `argocd-cmd-params-cm` ConfigMap. For instructions on configuring additional namespaces, see [Configure namespaces for Applications and ApplicationSets](argocd-configure-settings.md#argocd-configure-resource-namespaces).

**Note**  
The namespace that contains an Application or ApplicationSet is separate from the destination namespace where the generated workload runs. For example, an Application stored in `team-a-gitops` can deploy workloads to `default`, `production`, `staging`, or another namespace in a target cluster.

**Note**  
The managed capability has specific requirements for CLI usage, AppProject configuration, resource tracking, and ApplicationSet generators:  
When using the Argo CD CLI, specify resources outside the primary namespace with a namespace prefix, such as `argocd app sync team-a-gitops/my-app`.
AppProject resources must specify `.spec.sourceNamespaces` to allow Applications and ApplicationSets from each additional namespace.
Resource tracking annotations use the format: `namespace_appname:group/kind:namespace/name`.
ApplicationSets in additional namespaces don’t support the Plugin (`plugin`), Pull Request (`pullRequest`), or Source Code Management (SCM) Provider (`scmProvider`) generators. To use one of these generators, create the ApplicationSet in the primary Argo CD namespace.

 **Unsupported features**: The following features are not available in the managed capability:
+ Config Management Plugins (CMPs) for custom manifest generation
+ Notifications controller
+ Custom SSO providers (only AWS Identity Center is supported, including third-party federated identity through AWS Identity Center)
+ UI extensions and custom banners
+ Argo CD configuration ConfigMaps and keys other than the supported `argocd-cm` fields and the `hydrator.enabled`, `application.namespaces`, and `applicationsetcontroller.namespaces` keys in `argocd-cmd-params-cm`. See [Configure Argo CD settings](argocd-configure-settings.md).
+ Modifying the sync timeout (fixed at 120 seconds)

 **Compatibility**: The capability uses the same Kubernetes APIs and CRDs as upstream Argo CD, so existing Application and ApplicationSet manifests generally require no changes. Tools like `kubectl` work the same way. Except for the limitations described in this topic, the capability supports Applications and ApplicationSets, GitOps workflows with automatic sync, multi-cluster deployments, sync policies (automated, prune, self-heal), sync waves and hooks, health assessment for standard Kubernetes resources, rollback capabilities, Git repository sources (HTTPS and SSH), Helm, Kustomize, and plain YAML manifests, GitHub app credentials, projects for multi-tenancy, and resource exclusions and inclusions.

## Using the Argo CD CLI with the managed capability
<a name="argocd-cli-configuration"></a>

The Argo CD CLI works the same as upstream Argo CD for most operations, but authentication and cluster registration differ.

### Prerequisites
<a name="_prerequisites"></a>

Install the Argo CD CLI following the [upstream installation instructions](https://argo-cd.readthedocs.io/en/stable/cli_installation/).

### Configuration
<a name="_configuration"></a>

Configure the CLI using environment variables:

1. Get the Argo CD server URL from the EKS console (under your cluster’s **Capabilities** page), or using the AWS CLI. The `https://` prefix must be removed:

   ```
   export ARGOCD_SERVER=$(aws eks describe-capability \
     --cluster-name {{my-cluster}} \
     --capability-name {{my-argocd}} \
     --query 'capability.configuration.argoCd.serverUrl' \
     --output text \
     --region {{region-code}} | sed 's|^https://||')
   ```

1. Generate an account token from the Argo CD UI (**Settings** → **Accounts** → **admin** → **Generate New Token**), then set it as an environment variable:

   ```
   export ARGOCD_AUTH_TOKEN="your-token-here"
   ```

**Important**  
This configuration uses the admin account token for initial setup and development workflows. For production use cases, use project-scoped roles and tokens to follow the principle of least privilege. For more information about configuring project roles and RBAC, see [Configure Argo CD permissions](argocd-permissions.md).

1. Set the required gRPC option:

   ```
   export ARGOCD_OPTS="--grpc-web"
   ```

With these environment variables set, you can use the Argo CD CLI without the `argocd login` command.

### Key differences
<a name="_key_differences"></a>

The managed capability has the following CLI limitations:
+  `argocd admin` commands are not supported (they require direct pod access)
+  `argocd login` is not supported (use account or project tokens instead)
+  `argocd cluster add` requires the `--aws-cluster-name` flag with the EKS cluster ARN

### Example: Register a cluster
<a name="_example_register_a_cluster"></a>

Register an EKS cluster for application deployment:

```
# Get the cluster ARN
CLUSTER_ARN=$(aws eks describe-cluster \
  --name {{my-cluster}} \
  --query 'cluster.arn' \
  --output text)

# Register the cluster
argocd cluster add $CLUSTER_ARN \
  --aws-cluster-name $CLUSTER_ARN \
  --name in-cluster \
  --project default
```

For complete Argo CD CLI documentation, see the [Argo CD CLI reference](https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/).

## Migration path
<a name="_migration_path"></a>

You can migrate from self-managed Argo CD to the managed capability:

1. Review your current Argo CD configuration for unsupported features (Notifications controller, CMPs, custom health checks, UI extensions)

1. Scale your self-managed Argo CD controllers to zero replicas to prevent conflicts

1. Create an Argo CD capability resource on your cluster

1. Export your existing Applications, ApplicationSets, and AppProjects

1. Migrate repository credentials, cluster secrets, and repository credential templates (repocreds)

1. If using GPG keys, TLS certificates, or SSH known hosts, migrate these configurations as well

1. Update `destination.server` fields to use cluster names or EKS cluster ARNs

1. Apply them to the managed Argo CD instance

1. Verify applications are syncing correctly

1. Decommission your self-managed Argo CD installation

The managed capability uses the same Argo CD APIs and resource definitions, so your existing manifests work with minimal modification.

## Next steps
<a name="_next_steps"></a>
+  [Create an Argo CD capability](create-argocd-capability.md) - Create an Argo CD capability resource
+  [Working with Argo CD](working-with-argocd.md) - Deploy your first application
+  [Argo CD considerations](argocd-considerations.md) - Configure AWS Identity Center integration