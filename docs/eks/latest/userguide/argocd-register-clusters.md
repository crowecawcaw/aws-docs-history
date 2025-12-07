**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Register target clusters

Register clusters to enable Argo CD to deploy applications to them.
You can register the same cluster where Argo CD is running (local cluster) or remote clusters in different accounts or regions.

## Prerequisites

- An EKS cluster with the Argo CD capability created
- `kubectl` configured to communicate with your cluster
- For remote clusters: appropriate IAM permissions and access entries

## Register the local cluster

To deploy applications to the same cluster where Argo CD is running, register it as a deployment target.

###### Note

The Argo CD capability does not automatically register the local cluster.
You must explicitly register it to deploy applications to the same cluster.

**Using the Argo CD CLI**:

```
argocd cluster add <cluster-context-name> \
  --aws-cluster-name arn:aws:eks:us-west-2:111122223333:cluster/my-cluster \
  --name local-cluster
```

**Using a Kubernetes Secret**:

```
apiVersion: v1
kind: Secret
metadata:
  name: local-cluster
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: cluster
stringData:
  name: local-cluster
  server: arn:aws:eks:us-west-2:111122223333:cluster/my-cluster
  project: default
```

Apply the configuration:

```
kubectl apply -f local-cluster.yaml
```

###### Note

Use the EKS cluster ARN in the `server` field, not the Kubernetes API server URL.
The managed capability requires ARNs to identify clusters.
The default `kubernetes.default.svc` is not supported.

## Register remote clusters

To deploy to remote clusters, you must:

1. Create an access entry on the remote cluster for your Argo CD IAM Capability Role
2. Associate an access policy with appropriate permissions
3. Register the cluster in Argo CD

**Step 1: Create the access entry on the remote cluster**

Replace `region-code` with the AWS Region that your remote cluster is in, replace `remote-cluster` with the name of your remote cluster, and replace the ARN with your Argo CD capability role ARN.

```
aws eks create-access-entry \
  --region `region-code` \
  --cluster-name `remote-cluster` \
  --principal-arn arn:aws:iam::[.replaceable]`111122223333`:role/`ArgoCDCapabilityRole` \
  --type STANDARD
```

**Step 2: Associate an access policy**

```
aws eks associate-access-policy \
  --region `region-code` \
  --cluster-name `remote-cluster` \
  --principal-arn arn:aws:iam::[.replaceable]`111122223333`:role/`ArgoCDCapabilityRole` \
  --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy \
  --access-scope type=cluster
```

###### Note

For production environments, consider using more restrictive access policies.
See [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md") for least-privilege configurations.

**Step 3: Register the cluster in Argo CD**

**Using the Argo CD CLI**:

```
argocd cluster add <cluster-context-name> \
  --aws-cluster-name arn:aws:eks:us-west-2:111122223333:cluster/remote-cluster \
  --name remote-cluster
```

**Using a Kubernetes Secret**:

```
apiVersion: v1
kind: Secret
metadata:
  name: remote-cluster
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: cluster
stringData:
  name: remote-cluster
  server: arn:aws:eks:us-west-2:111122223333:cluster/remote-cluster
  project: default
```

Apply the configuration:

```
kubectl apply -f remote-cluster.yaml
```

## Cross-account and cross-region clusters

To deploy to clusters in different AWS accounts or regions:

1. Add the Argo CD Capability Role as an access entry on the remote cluster
2. Associate the appropriate access policy (typically `AmazonEKSClusterAdminPolicy`)
3. Register the cluster using its full ARN (which includes the region)

The cluster ARN format includes the region, so there’s no difference between cross-account and cross-region registration—both use the same process.

For detailed cross-account configuration including trust policies and IAM permissions, see [Argo CD considerations](argocd-considerations.md "argocd-considerations.md").

## Verify cluster registration

View registered clusters:

```
kubectl get secrets -n argocd -l argocd.argoproj.io/secret-type=cluster
```

Or check cluster status in the Argo CD UI under Settings → Clusters.

## Private clusters

The Argo CD capability provides transparent access to fully private EKS clusters without requiring VPC peering or specialized networking configuration.

AWS manages connectivity between the Argo CD capability and private remote clusters automatically.

Simply register the private cluster using its ARN—no additional networking setup required.

## Restrict cluster access with Projects

Use Projects to control which clusters Applications can deploy to:

```
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: production
  namespace: argocd
spec:
  destinations:
  - server: arn:aws:eks:us-west-2:111122223333:cluster/prod-cluster
    namespace: '*'
  - server: arn:aws:eks:eu-west-1:111122223333:cluster/prod-eu-cluster
    namespace: '*'
  sourceRepos:
  - 'https://github.com/example/production-apps'
```

For details, see [Working with Argo CD Projects](argocd-projects.md "argocd-projects.md").

## Additional resources

- [Working with Argo CD Projects](argocd-projects.md "argocd-projects.md") - Organize applications and enforce security boundaries
- [Create Applications](argocd-create-application.md "argocd-create-application.md") - Deploy your first application
- [Use ApplicationSets](argocd-applicationsets.md "argocd-applicationsets.md") - Deploy to multiple clusters with ApplicationSets
- [Argo CD considerations](argocd-considerations.md "argocd-considerations.md") - Multi-cluster patterns and cross-account setup
- [Declarative Cluster Setup](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#clusters "https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#clusters") - Upstream cluster configuration reference
