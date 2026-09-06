

# Setting up an Amazon EKS cluster in Studio
<a name="sagemaker-hyperpod-studio-setup-eks"></a>

You do most of this setup from your HyperPod cluster details page in the SageMaker AI console. Open the SageMaker AI console, choose **HyperPod clusters**, choose your cluster, and then choose the **Configuration** tab. Under **Cluster access for SageMaker domains**, choose **Manage access**. This is where you create or view a domain and attach the cluster-access policies that let Studio users reach the cluster.

The following screenshot shows the **Cluster access for SageMaker domains** section on the **Configuration** tab.

![The Configuration tab of a HyperPod cluster, showing the EKS orchestrator details and the Cluster access for SageMaker domains section with the Create domain, View domain, and Manage access buttons.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/hyperpod/studio-cluster-access-manage-access.png)


The following instructions describe how to set up an Amazon EKS cluster in Studio.

1. Under the **Manage access** page, select an existing domain. Studio access to a HyperPod cluster runs through a domain, and the domain execution role is the IAM principal Studio uses to act on your cluster. For information on creating a domain, see [Guide to getting set up with Amazon SageMaker AI](gs.md).

1. Attach the following permissions to your execution role from the IAM console.

   For information on SageMaker AI execution roles and how to edit them, see [Understanding domain space permissions and execution roles](execution-roles-and-spaces.md). 

   To learn how to attach policies to an IAM user or group, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

   Before you attach the policy, replace both example ARNs with your own:
   + Replace `arn:aws:sagemaker:us-east-1:111122223333:cluster/hyperpod-cluster-name` with your HyperPod cluster ARN.
   + Replace `arn:aws:eks:us-east-1:111122223333:cluster/eks-cluster-name` with your Amazon EKS cluster ARN. It appears twice, in `UseEksClusterPermissions` and in `DescribeSpacesAddon`, where it carries a trailing `/*`.

   These are two different resources with two different ARNs. Find the HyperPod cluster ARN in the SageMaker AI console and the Amazon EKS cluster ARN in the Amazon EKS console. If you leave the example values in place, Studio cannot describe your cluster and the **Tasks** tab does not load.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "DescribeHyperpodClusterPermissions",
               "Effect": "Allow",
               "Action": [
                   "sagemaker:DescribeCluster"
               ],
               "Resource": "arn:aws:sagemaker:us-east-1:111122223333:cluster/hyperpod-cluster-name"
           },
           {
               "Effect": "Allow",
               "Action": "ec2:Describe*",
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "ecr:CompleteLayerUpload",
                   "ecr:GetAuthorizationToken",
                   "ecr:UploadLayerPart",
                   "ecr:InitiateLayerUpload",
                   "ecr:BatchCheckLayerAvailability",
                   "ecr:PutImage"
               ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "cloudwatch:PutMetricData",
                   "cloudwatch:GetMetricData"
               ],
               "Resource": "*"
           },
           {
               "Sid": "UseEksClusterPermissions",
               "Effect": "Allow",
               "Action": [
                   "eks:DescribeCluster",
                   "eks:AccessKubernetesApi",
                   "eks:MutateViaKubernetesApi"
               ],
               "Resource": "arn:aws:eks:us-east-1:111122223333:cluster/eks-cluster-name"
           },
           {
               "Sid": "DescribeSpacesAddon",
               "Effect": "Allow",
               "Action": "eks:DescribeAddon",
               "Resource": "arn:aws:eks:us-east-1:111122223333:cluster/eks-cluster-name/*"
           },
           {
               "Sid": "ListClustersPermission",
               "Effect": "Allow",
               "Action": [
                   "sagemaker:ListClusters"
               ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "ssm:StartSession",
                   "ssm:TerminateSession"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

1. Attach cluster-access policies to the execution role. The IAM policy in the previous step lets the execution role call the AWS APIs. It does not give the role any permissions inside the Kubernetes cluster. Cluster-access policies do that, and only a role with the right ones attached reaches the cluster. Attach them from **Manage access**, on the domain or the user profile.

   Select the execution role for the domain or user profile you are granting access to, then select the policies your users need. Choose whether to scope access to a namespace or to the whole cluster, scoping to a namespace when teams share a cluster, and then save. Scoping to a namespace also restricts which tasks those users can see in Studio. For what each policy allows, how to scope access, and how to grant a custom set of permissions instead, see [Restrict task view in Studio for EKS clusters](#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view).

   Granting access this way creates the Amazon EKS access entry for the execution role for you, so there is no separate step in the Amazon EKS console. For the concepts behind the access model, see [Grant IAM users access to Kubernetes with EKS access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html).

1. (Optional) To ensure a more smooth experience, we recommend that you add tags to your clusters. For information on how to add tags, see [Edit a SageMaker HyperPod cluster](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters) to update your cluster using the SageMaker AI console.

   Tag your [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) workspace to your Studio domain. Use this tag to link to your Grafana workspace directly from your cluster in Studio. Add the following tag to your cluster to identify it with your Grafana workspace ID, `ws-id`.

   Tag Key = “`grafana-workspace`”, Tag Value = “`ws-id`”.

## Restrict task view in Studio for EKS clusters
<a name="sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view"></a>

You can restrict users’ visibility to specified Kubernetes namespaces, ensuring that users can access the resources they need while maintaining strict access controls.

There are two ways to do this. Scoping a cluster-access policy to a namespace is done entirely in the console and is the simpler option. A custom Kubernetes RBAC role gives you control over the exact verbs and resources a user gets, at the cost of managing the role yourself.

### Restrict with a cluster-access policy
<a name="sagemaker-hyperpod-studio-setup-eks-restrict-policy"></a>

HyperPod provides cluster-access policies that you attach from **Manage access** on the **Configuration** tab. Attach only the policies a set of users needs, and scope the access to a namespace rather than to the whole cluster. This is the same flow as the third step above.

We recommend that you attach all of the policies to the role for the full HyperPod in Studio experience. Each policy covers a different part of the experience, so leaving one off removes the capability it grants. Attach a subset only when you intend to withhold a capability from that set of users.


| Policy | What it allows | 
| --- | --- | 
| AmazonSagemakerHyperpodTrainingPolicy | Submit and manage training workloads. Full access to RayCluster, RayJob, and RayCronJob, to HyperPodPyTorchJob, to Kubeflow PyTorchJob, MPIJob, and TFJob, and to Kubernetes jobs and pods. Read access to pod logs, config maps, events, services, service accounts, resource quotas, limit ranges, deployments, stateful sets, replica sets, and Kueue local queues and workloads. Can create a RayDashboardConnection. | 
| AmazonSagemakerHyperpodInferencePolicy | Deploy and manage inference workloads. Full access to RayCluster and RayService, to JumpStartModel, InferenceEndpointConfig, and SageMakerEndpointRegistration, and to pods. Read access to pod logs, config maps, events, services, service accounts, resource quotas, limit ranges, deployments, stateful sets, replica sets, horizontal pod autoscalers, ingresses, and Kueue local queues and workloads. Can create a RayDashboardConnection. | 
| AmazonSagemakerHyperpodSpacePolicy | Use spaces for interactive development. Full access to Workspace resources, and read access to workspace templates, access strategies, and integration templates. Read access to pods, services, service accounts, persistent volume claims, events, resource quotas, bindings, daemon sets, deployments, and replica sets. Can create a WorkspaceConnection, which is what opens a space. | 
| AmazonSagemakerHyperpodSpaceTemplatePolicy | Read the shared space templates. Attach it scoped to the jupyter-k8s-shared namespace, where the templates live, rather than to the namespace your users work in. | 
| AmazonSagemakerHyperpodUserClusterPolicy | See cluster-wide resources, which the Studio UI needs to render. Read access to namespaces and nodes, get access to custom resource definitions, read access to Kueue cluster queues, resource flavors, and workload priority classes, and permission to check the user’s own access. Attach it scoped to the cluster rather than to a namespace. | 

Full access means get, list, watch, create, update, patch, and delete.

These are Amazon EKS cluster-access policies, not IAM managed policies. Their ARNs take the form `arn:<partition>:eks::aws:cluster-access-policy/<name>`. Attaching one through **Manage access** creates the Amazon EKS access entry for the execution role, which is what applies the policy to the role.

### Restrict with a custom Kubernetes RBAC role
<a name="sagemaker-hyperpod-studio-setup-eks-restrict-rbac"></a>

Use a custom role when you want to grant a custom set of permissions instead of the ones a cluster-access policy provides. The following configuration allows administrators to grant specific, limited access to data scientists for viewing tasks within the cluster. This configuration grants the following permissions:
+ List and get pods
+ List and get events
+ Get Custom Resource Definitions (CRDs)

YAML Configuration

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pods-events-crd-cluster-role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["events"]
  verbs: ["get", "list"]
- apiGroups: ["apiextensions.k8s.io"]
  resources: ["customresourcedefinitions"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: pods-events-crd-cluster-role-binding
subjects:
- kind: Group
  name: pods-events-crd-cluster-level
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: pods-events-crd-cluster-role
  apiGroup: rbac.authorization.k8s.io
```

1. Save the YAML configuration to a file named `cluster-role.yaml`.

1. Apply the configuration using [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) from the Kubernetes website:

   ```
   kubectl apply -f cluster-role.yaml
   ```

1. Verify the configuration:

   ```
   kubectl get clusterrole pods-events-crd-cluster-role
   kubectl get clusterrolebinding pods-events-crd-cluster-role-binding
   ```

1. Assign users to the `pods-events-crd-cluster-level` group through your identity provider or IAM.