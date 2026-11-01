

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Using the Argo CD CLI with the managed capability
<a name="argocd-cli-configuration"></a>

The Argo CD command line interface (CLI) works the same with the managed capability as it does with upstream Argo CD for most operations, but authentication and cluster registration differ.

## Prerequisites
<a name="_prerequisites"></a>

Install the Argo CD CLI following the [upstream installation instructions](https://argo-cd.readthedocs.io/en/stable/cli_installation/) on the Argo CD website.

## Configuration
<a name="_configuration"></a>

Configure the CLI using environment variables:

1. Get the Argo CD server URL from the Amazon EKS console (under your cluster’s **Capabilities** page), or using the AWS CLI. The `https://` prefix must be removed:

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

## Key differences
<a name="_key_differences"></a>

The managed capability has the following CLI limitations:
+  `argocd admin` commands are not supported (they require direct pod access)
+  `argocd login` is not supported (use account or project tokens instead)
+  `argocd cluster add` requires the `--aws-cluster-name` flag with the EKS cluster ARN

## Example: Register a cluster
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

For more information about the Argo CD CLI, see the [Argo CD CLI reference](https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/) on the Argo CD website.