# Setting up an Amazon EKS cluster in

Studio

The following instructions describe how to set up an Amazon EKS cluster in Studio.

1. Create a domain or have one ready. For information on creating a domain, see
   [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md").
2. Add the following permission to your execution role.

For information on SageMaker AI execution roles and how to edit them, see [Understanding domain space permissions and
execution roles](execution-roles-and-spaces.md "execution-roles-and-spaces.md").

To learn how to attach policies to an IAM user or group, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DescribeHyerpodClusterPermissions",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeCluster"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:cluster/`cluster-name`"
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
 "eks:DescribeAddon"
 ],
 "Resource": "arn:aws:eks:`us-east-1`:`111122223333`:cluster/`cluster-name`"
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
}`

```

3. [Grant
   IAM users access to Kubernetes with EKS access entries](../../../eks/latest/userguide/access-entries.md "../../../eks/latest/userguide/access-entries.md").
   1. Navigate to the Amazon EKS cluster associated with your HyperPod cluster.
   2. Choose the **Access** tab and [create an access entry](../../../eks/latest/userguide/creating-access-entries.md "../../../eks/latest/userguide/creating-access-entries.md") for
      the execution role you created.
      1. In step 1, Select the execution role you created above in the
         **IAM** principal dropdown.
      2. In step 2, select a policy name and select an access scope that you want the users to
         have access to.

4. (Optional) To ensure a more smooth experience, we recommend that you add tags to your
   clusters. For information on how to add tags, see [Edit a
   SageMaker HyperPod cluster](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters "sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters") to update your cluster
   using the SageMaker AI console.
   1. Tag your [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md")
      workspace to your Studio domain. This will be used to quickly link to your Grafana
      workspace directly from your cluster in Studio. To do so, add the following tag to your
      cluster to identify it with your Grafana workspace ID, `ws-id`.

   Tag Key = “`grafana-workspace`”, Tag Value = “`ws-id`”.

5. (Optional) [Restrict task view in
   Studio for EKS clusters](#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view "#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view"). For information on
   viewable tasks in Studio, see [Tasks](sagemaker-hyperpod-studio-tabs.md#sagemaker-hyperpod-studio-tabs-tasks "sagemaker-hyperpod-studio-tabs.md#sagemaker-hyperpod-studio-tabs-tasks").

## Restrict task view in

Studio for EKS clusters

You can restrict Kubernetes namespace permissions for users, so that they will only have
access to view tasks belonging to a specified namespace. The following provides information on
how to restrict the task view in Studio for EKS clusters. For information on viewable
tasks in Studio, see [Tasks](sagemaker-hyperpod-studio-tabs.md#sagemaker-hyperpod-studio-tabs-tasks "sagemaker-hyperpod-studio-tabs.md#sagemaker-hyperpod-studio-tabs-tasks").

Users will have visibility to all EKS cluster tasks by default. You can restrict users’
visibility for EKS cluster tasks to specified namespaces, ensuring that users can access the
resources they need while maintaining strict access controls. You will need to provide the
namespace for the user to display jobs of that namespace once the following is set up.

Once the restriction is applied, you will need to provide the namespace to the users
assuming the role. Studio will only display the jobs of the namespace once the user
provides inputs namespace they have permissions to view in the **Tasks** tab.

The following configuration allows administrators to grant specific, limited access to
data scientists for viewing tasks within the cluster. This configuration grants the following
permissions:

- List and get pods
- List and get events
- Get Custom Resource Definitions (CRDs)

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
2. Apply the configuration using [`kubectl`](https://kubernetes.io/docs/reference/kubectl/ "https://kubernetes.io/docs/reference/kubectl/"):

```
kubectl apply -f cluster-role.yaml
```

3. Verify the configuration:

```
kubectl get clusterrole pods-events-crd-cluster-role
kubectl get clusterrolebinding pods-events-crd-cluster-role-binding
```

4. Assign users to the `pods-events-crd-cluster-level` group through your
   identity provider or IAM.
