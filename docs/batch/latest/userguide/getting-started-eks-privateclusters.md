# Getting started with AWS Batch on Amazon EKS

Private Clusters

AWS Batch is a managed service that orchestrates batch workloads in your Amazon Elastic Kubernetes Service (Amazon EKS)
clusters. This includes queuing, dependency tracking, managed job retries and priorities,
pod management, and node scaling. This feature connects your existing private Amazon EKS cluster
with AWS Batch to run your jobs at scale. You can use [`eksctl`](https://eksctl.io/usage/eks-private-cluster/ "https://eksctl.io/usage/eks-private-cluster/") (a
command line interface for Amazon EKS), the AWS console, or the [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") to create a private Amazon EKS cluster
with all the other necessary resources.

[Amazon EKS private only clusters](../../../eks/latest/userguide/cluster-endpoint.md#private-access "../../../eks/latest/userguide/cluster-endpoint.md#private-access") by default have no
inbound/outbound internet access, and you can only access the API server from within your
VPC or a connected network. Amazon VPC endpoints are used to enable private access to other AWS
services. `eksctl` supports creating fully private clusters using a pre-existing Amazon VPC and
subnets. `eksctl` also creates Amazon VPC endpoints in the supplied Amazon VPC and
modifies route tables for the supplied subnets.

Each subnet should have an explicit route table associated with it because
`eksctl` does not modify the main route table. Your cluster must pull images from a
container registry that's in your Amazon VPC. As well, you can create an Amazon Elastic Container Registry in your Amazon VPC
and copy container images to it for your nodes to pull from. For more information, see
[Copy a container image from one repository to another repository](../../../eks/latest/userguide/copy-image-to-repository.md "../../../eks/latest/userguide/copy-image-to-repository.md"). To get
started with Amazon ECR private repositories, see [Amazon ECR private
repositories](../../../AmazonECR/latest/userguide/Repositories.md "../../../AmazonECR/latest/userguide/Repositories.md").

You can optionally create a [pull through cache rule](../../../AmazonECR/latest/userguide/pull-through-cache.md "../../../AmazonECR/latest/userguide/pull-through-cache.md")
with Amazon ECR. Once a pull through cache rule is created for an external public registry, you
can pull an image from that external public registry using your Amazon ECR private registry
uniform resource identifier (URI). Then Amazon ECR creates a repository and caches the image.
When a cached image is pulled using the Amazon ECR private registry URI, Amazon ECR checks the remote
registry to see if there is a new version of the image and updates your private registry up
to once every 24 hours.

###### Contents

- [Overview](getting-started-eks-privateclusters.md#getting-started-eks-context "getting-started-eks-privateclusters.md#getting-started-eks-context")
- [Prerequisites](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-prerequisites "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-prerequisites")
- [Step 1: Create your EKS
  cluster for AWS Batch](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-0 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-0")
- [Step 2: Prepare your EKS
  cluster for AWS Batch](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-1 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-1")
- [Step 3: Create an Amazon EKS
  compute environment](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-2 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-2")
- [Step 4: Create a job queue
  and attach the compute environment](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-3 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-3")
- [Step 5: Create an Amazon ECR
  with pull through cache](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-ecr "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-ecr")
- [Step 6: Register a job
  definition](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-4 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-4")
- [Step 7: Submit a job to
  run](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-5 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-5")
- [Step 8: View the Job's output](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-7 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-7")
- [Step 9: (Optional) Submit a
  job with overrides](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-6 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-6")
- [Step 10: Clean up your tutorial resources](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-8 "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-step-8")
- [Additional resources](getting-started-eks-privateclusters.md#getting-started-eks-additional-resources "getting-started-eks-privateclusters.md#getting-started-eks-additional-resources")
- [Troubleshooting](getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-troubleshooting "getting-started-eks-privateclusters.md#getting-started-eks-privateclusters-troubleshooting")

## Overview

This tutorial demonstrates how to setup AWS Batch with a private Amazon EKS using the
AWS CloudShell, `kubectl` and `eksctl`.

**Intended Audience**

This tutorial is designed for system administrators and developers
responsible for setting up, testing, and deploying AWS Batch.

**Features Used**

This tutorial shows you how to use the AWS CLI, to:

- Use Amazon Elastic Container Registry (Amazon ECR) to store container images
- Create and configure an Amazon EKS compute environment
- Create a job queue.
- Create a job definition
- Create and submit a job to run
- Submit a job with overrides

**Time Required**

It should take about 40–50 minutes to complete this tutorial.

**Regional Restrictions**

There are no country or regional restrictions associated with using this
solution.

**Resource Usage Costs**

There's no charge for creating an AWS account. However, by implementing
this solution, you might incur some or all of the costs that are listed in
the following table.

| Description                         | Cost (US dollars)                                                                                                                                                                                 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You are charged by the cluster hour | Varies depending on Instance, see [Amazon EKS<br>pricing](https://aws.amazon.com/eks/pricing/ "https://aws.amazon.com/eks/pricing/")                                                              |
| Amazon EC2 instance                 | You pay for each Amazon EC2 instance that is created. For more<br>information about pricing, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/"). |

## Prerequisites

This tutorial uses AWS CloudShell which is a browser-based, pre-authenticated shell that you
launch directly from the AWS Management Console. This allows for access to the cluster once it no
longer has public internet access. The AWS CLI, `kubectl`, and `eksctl` may already be
installed as part of AWS CloudShell. For more information on AWS CloudShell, see the [AWS CloudShell*User Guide*](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"). An alternative to AWS CloudShell is to
connect to your cluster's VPC or a [connected network](../../../whitepapers/latest/aws-vpc-connectivity-options/introduction.md "../../../whitepapers/latest/aws-vpc-connectivity-options/introduction.md").

To run kubectl commands, you will need private access to your Amazon EKS cluster. This
means all traffic to your cluster API server must come from within your cluster's VPC or
a connected network.

- AWS CLI – A command line tool for working
  with AWS services, including Amazon EKS. This guide requires that you use version
  2.8.6 or later or 1.26.0 or later. For more
  information, see [Installing, updating, and
  uninstalling the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the _AWS Command Line Interface User Guide_.
  After installing the AWS CLI, we recommend that you also configure it. For more
  information, see [Quick configuration with `aws configure`](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the
  _AWS Command Line Interface User Guide_.
- `kubectl` – A command line tool for
  working with Kubernetes clusters. This guide requires that you use version
  `1.23` or later. For more information, see [Installing or updating `kubectl`](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md") in the _Amazon EKS User Guide_.
- `eksctl` – A command line
  tool for working with Amazon EKS clusters that automates many individual tasks. This
  guide requires that you use version `0.115.0` or later.
  For more information, see [Installing or updating `eksctl`](https://eksctl.io/installation/ "https://eksctl.io/installation/") in the
  **Amazon EKS User Guide**.
- Permissions – Users calling the [CreateComputeEnvironment](../APIReference/API_CreateComputeEnvironment.md "../APIReference/API_CreateComputeEnvironment.md") API operation to create a compute
  environment that uses Amazon EKS resources require permissions to the
  `eks:DescribeCluster` and `eks:ListClusters` API
  operation. You can attach the [AWSBatchFullAccess](batch_managed_policies.md#batch_managed_policies.title "batch_managed_policies.md#batch_managed_policies.title") managed policy to your user account by following
  the directions [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in
  the _IAM User Guide_.
- InstanceRole – You need to create an
  `InstanceRole` for your Amazon EKS nodes that has the
  `AmazonEKSWorkerNodePolicy` and
  `AmazonEC2ContainerRegistryPullOnly` polices. For directions on
  how to create the `InstanceRole` see [Creating the Amazon EKS node IAM role](../../../eks/latest/userguide/create-node-role.md#create-worker-node-role "../../../eks/latest/userguide/create-node-role.md#create-worker-node-role"). You will
  need the ARN of the `InstanceRole`.
- AWS account ID – You need to know your
  AWS account ID. Follow the directions in [Viewing your AWS account ID](../../../IAM/latest/UserGuide/console-account-id.md "../../../IAM/latest/UserGuide/console-account-id.md").
- (Optional) CloudWatch – To examine the details
  of [(Optional) Submit a job with
  overrides](getting-started-eks.md#getting-started-eks-step-6 "getting-started-eks.md#getting-started-eks-step-6"), logging must be configured. For more information, see
  [Use CloudWatch Logs to monitor AWS Batch on Amazon EKS jobs](batch-eks-cloudwatch-logs.md "batch-eks-cloudwatch-logs.md").

## Step 1: Create your EKS

cluster for AWS Batch

###### Important

To get started as simply and quickly as possible, this tutorial includes steps
with default settings. Before creating for production use, we recommend that you
familiarize yourself with all settings and deploy with the settings that meet your
requirements.

We recommend you use `eksctl` and the following config file to create
your cluster. To manually setup your cluster follow the directions in [Deploy private
clusters with limited internet access](../../../eks/latest/userguide/private-clusters.md "../../../eks/latest/userguide/private-clusters.md") in the _Amazon EKS User
Guide_.

1. Open the [AWS CloudShell console](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home")
   and set the region to `us-east-1`. For the rest of the tutorial make
   sure you are using `us-east-1`.
2. Create a private EKS cluster in the `us-east-1` region using the
   sample `eksctl` config file. Save the yaml file to your AWS CloudShell
   environment and name it `clusterConfig.yaml` .You can change
   `my-test-cluster` with the name you want to use for
   your cluster.

```
`kind: ClusterConfig
apiVersion: eksctl.io/v1alpha5
metadata:
 name: `my-test-cluster`
 region: us-east-1
availabilityZones:
 - us-east-1a
 - us-east-1b
 - us-east-1c
managedNodeGroups:
 - name: ng-1
 privateNetworking: true
privateCluster:
 enabled: true
 skipEndpointCreation: false`
```

3. Create your resources using the command: `eksctl create cluster -f
clusterConfig.yaml`. Cluster creation can take between 10–15
   minutes.
4. Once the cluster has finished being created you have to add your AWS CloudShell IP
   address to the allow list. To find your AWS CloudShell IP address run the following
   command:

```
`curl http://checkip.amazonaws.com`
```

Once you have the public IP address you have to create an allow list
rule:

```
`aws eks update-cluster-config \
 --name `my-test-cluster` \
 --region us-east-1 \
 --resources-vpc-config endpointPublicAccess=true,endpointPrivateAccess=true,publicAccessCidrs=["<Public IP>/32"]`
```

Then apply the update to the kubectl config file:

```
`aws eks update-kubeconfig --name `my-test-cluster` --region us-east-1`
```

5. To test that you have access to the nodes run the following command:

```
`kubectl get nodes`
```

The output of command is:

```
NAME                              STATUS   ROLES    AGE     VERSION
ip-192-168-107-235.ec2.internal   Ready    none     1h   v1.32.3-eks-473151a
ip-192-168-165-40.ec2.internal    Ready    none     1h   v1.32.3-eks-473151a
ip-192-168-98-54.ec2.internal     Ready    none     1h   v1.32.1-eks-5d632ec
```

## Step 2: Prepare your EKS

cluster for AWS Batch

All steps are required and must be done in AWS CloudShell.

1. ###### Create a dedicated namespace for AWS Batch jobs

Use `kubectl` to create a new namespace.

```
`$` `namespace=`my-aws-batch-namespace``
```

```
`$` `cat - <<EOF | kubectl create -f -
{
 "apiVersion": "v1",
 "kind": "Namespace",
 "metadata": {
 "name": "${namespace}",
 "labels": {
 "name": "${namespace}"
 }
 }
}
EOF`
```

Output:

```
`namespace/my-aws-batch-namespace created`
```

2. ###### Enable access via role-based access control (RBAC)

Use `kubectl` to create a Kubernetes role for the cluster to allow
AWS Batch to watch nodes and pods, and to bind the role. You must do this once
for each Amazon EKS cluster.

```
`$` `cat - <<EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: `aws-batch-cluster-role`
rules:
 - apiGroups: [""]
 resources: ["namespaces"]
 verbs: ["get"]
 - apiGroups: [""]
 resources: ["nodes"]
 verbs: ["get", "list", "watch"]
 - apiGroups: [""]
 resources: ["pods"]
 verbs: ["get", "list", "watch"]
 - apiGroups: [""]
 resources: ["events"]
 verbs: ["list"]
 - apiGroups: [""]
 resources: ["configmaps"]
 verbs: ["get", "list", "watch"]
 - apiGroups: ["apps"]
 resources: ["daemonsets", "deployments", "statefulsets", "replicasets"]
 verbs: ["get", "list", "watch"]
 - apiGroups: ["rbac.authorization.k8s.io"]
 resources: ["clusterroles", "clusterrolebindings"]
 verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 name: `aws-batch-cluster-role-binding`
subjects:
- kind: User
 name: `aws-batch`
 apiGroup: rbac.authorization.k8s.io
roleRef:
 kind: ClusterRole
 name: `aws-batch-cluster-role`
 apiGroup: rbac.authorization.k8s.io
EOF`
```

Output:

```
`clusterrole.rbac.authorization.k8s.io/aws-batch-cluster-role created
clusterrolebinding.rbac.authorization.k8s.io/aws-batch-cluster-role-binding created`
```

Create namespace-scoped Kubernetes role for AWS Batch to manage and lifecycle pods
and bind it. You must do this once for each unique namespace.

```
`$` `namespace=`my-aws-batch-namespace``
```

```
`$` `cat - <<EOF | kubectl apply -f - --namespace "${namespace}"
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
 name: `aws-batch-compute-environment-role`
 namespace: ${namespace}
rules:
 - apiGroups: [""]
 resources: ["pods"]
 verbs: ["create", "get", "list", "watch", "delete", "patch"]
 - apiGroups: [""]
 resources: ["serviceaccounts"]
 verbs: ["get", "list"]
 - apiGroups: ["rbac.authorization.k8s.io"]
 resources: ["roles", "rolebindings"]
 verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
 name: `aws-batch-compute-environment-role-binding`
 namespace: ${namespace}
subjects:
- kind: User
 name: `aws-batch`
 apiGroup: rbac.authorization.k8s.io
roleRef:
 kind: Role
 name: `aws-batch-compute-environment-role`
 apiGroup: rbac.authorization.k8s.io
EOF`

```

Output:

```
`role.rbac.authorization.k8s.io/aws-batch-compute-environment-role created
rolebinding.rbac.authorization.k8s.io/aws-batch-compute-environment-role-binding created`
```

Update Kubernetes `aws-auth` conﬁguration map to map the preceding RBAC
permissions to the AWS Batch service-linked role.

```
`$` `eksctl create iamidentitymapping \
 --cluster `my-test-cluster` \
 --arn "arn:aws:iam::`<your-account-ID>`:role/AWSServiceRoleForBatch" \
 --username `aws-batch``

```

Output:

```
`2022-10-25 20:19:57 [ℹ] adding identity "arn:aws:iam::`<your-account-ID>`:role/AWSServiceRoleForBatch" to auth ConfigMap`
```

###### Note

The path `aws-service-role/batch.amazonaws.com/` has been
removed from the ARN of the service-linked role. This is because of an issue
with the `aws-auth` configuration map. For more information, see
[Roles with paths don't work when the path is included in their ARN in
the aws-authconfigmap](https://github.com/kubernetes-sigs/aws-iam-authenticator/issues/268 "https://github.com/kubernetes-sigs/aws-iam-authenticator/issues/268").

## Step 3: Create an Amazon EKS

compute environment

AWS Batch compute environments define compute resource parameters to meet your batch
workload needs. In a managed compute environment, AWS Batch helps you to manage the
capacity and instance types of the compute resources (Kubernetes nodes) within your Amazon EKS
cluster. This is based on the compute resource specification that you define when you
create the compute environment. You can use EC2 On-Demand Instances or EC2 Spot
Instances.

Now that the **AWSServiceRoleForBatch**
service-linked role has access to your Amazon EKS cluster, you can create AWS Batch resources.
First, create a compute environment that points to your Amazon EKS cluster.

- For `subnets` run `eksctl get cluster
`my-test-cluster`` to get the subnets
  used by the cluster.
- For `securityGroupIds` parameter you can use the same security
  group as the Amazon EKS cluster. This command retrieves the security group ID for the
  cluster.

```
`$` `aws eks describe-cluster \
 --name `my-test-cluster` \
 --query cluster.resourcesVpcConfig.clusterSecurityGroupId`
```

- Use the ARN of the `instanceRole` you created in the
  Prerequisites.

```
`$` `cat <<EOF > ./batch-eks-compute-environment.json
{
 "computeEnvironmentName": "`My-Eks-CE1`",
 "type": "MANAGED",
 "state": "ENABLED",
 "eksConfiguration": {
 "eksClusterArn": "arn:aws:eks:`us-east-1`:``<your-account-ID>``:cluster/`my-test-cluster`",
 "kubernetesNamespace": "`my-aws-batch-namespace`"
 },
 "computeResources": {
 "type": "EC2",
 "allocationStrategy": "BEST_FIT_PROGRESSIVE",
 "minvCpus": 0,
 "maxvCpus": 128,
 "instanceTypes": [
 "m5"
 ],
 "subnets": [
 "`<eks-cluster-subnets-with-access-to-the-image-for-image-pull>`"
 ],
 "securityGroupIds": [
 "`<eks-cluster-sg>`"
 ],
 "instanceRole": "`<eks-instance-profile>`"
 }
}
EOF`

```

```
`$` `aws batch create-compute-environment --cli-input-json file://./batch-eks-compute-environment.json`
```

###### Notes

- Maintenance of an Amazon EKS compute environment is a shared responsibility. For
  more information, see [Security in Amazon
  EKS](../../../eks/latest/userguide/security.md "../../../eks/latest/userguide/security.md").

## Step 4: Create a job queue

and attach the compute environment

###### Important

It's important to confirm that the compute environment is healthy before
proceeding. The [DescribeComputeEnvironments](../APIReference/API_DescribeComputeEnvironments.md "../APIReference/API_DescribeComputeEnvironments.md") API operation can be used to do
this.

```
`$` `aws batch describe-compute-environments --compute-environments `My-Eks-CE1``
```

Confirm that the `status` parameter is not `INVALID`. If it
is, look at the `statusReason` parameter for the cause. For more
information, see [Troubleshooting AWS Batch](troubleshooting.md "troubleshooting.md").

Jobs submitted to this new job queue are run as pods on AWS Batch managed nodes that
joined the Amazon EKS cluster that's associated with your compute environment.

```
`$` `cat <<EOF > ./batch-eks-job-queue.json
 {
 "jobQueueName": "`My-Eks-JQ1`",
 "priority": 10,
 "computeEnvironmentOrder": [
 {
 "order": 1,
 "computeEnvironment": "`My-Eks-CE1`"
 }
 ]
 }
EOF`
```

```
`$` `aws batch create-job-queue --cli-input-json file://./batch-eks-job-queue.json`
```

## Step 5: Create an Amazon ECR

with pull through cache

Because the cluster doesn't have public internet access you have to create an Amazon ECR
for container images. The following directions create an Amazon ECR with a pull-through cache
rule to store the image.

1. The following command create the pull-through cache rule. You can replace
   `tutorial-prefix` with a different prefix.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix "`my-prefix`" \
 --upstream-registry-url "public.ecr.aws" \
 --region us-east-1`
```

2. Authenticate with the public ECR.

```
`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin `<your-account-ID>`.dkr.ecr.us-east-1.amazonaws.com`
```

Now you can pull an image.

```
`docker pull `<your-account-ID>`.dkr.ecr.us-east-1.amazonaws.com/`my-prefix`/amazonlinux/amazonlinux:2`
```

3. You can verify the repositry and image by running the following
   commands:

```
`aws ecr describe-repositories`
```

```
`aws ecr describe-images --repository-name `my-prefix`/amazonlinux/amazonlinux`
```

4. The image string to use for pulling the container is in the following
   format:

```
`<your-account-ID>`.dkr.ecr.us-east-1.amazonaws.com/`my-prefix`/amazonlinux/amazonlinux:2
```

## Step 6: Register a job

definition

The following Job definition instructs the pod to sleep for 60 seconds.

In the image field of the job definition, instead of providing a link to image in a
public ECR repository, provide the link to the image stored in our private ECR
repository. See the following sample job definition:

```
`$` `cat <<EOF > ./batch-eks-job-definition.json
{
 "jobDefinitionName": "`MyJobOnEks_Sleep`",
 "type": "container",
 "eksProperties": {
 "podProperties": {
 "hostNetwork": true,
 "containers": [
 {
 "image": "`<your-account-ID>`.dkr.ecr.us-east-1.amazonaws.com/`my-prefix`/amazonlinux/amazonlinux:2",
 "command": [
 "sleep",
 "60"
 ],
 "resources": {
 "limits": {
 "cpu": "1",
 "memory": "1024Mi"
 }
 }
 }
 ],
 "metadata": {
 "labels": {
 "environment": "`test`"
 }
 }
 }
 }
}
EOF`
```

```
`$` `aws batch register-job-definition --cli-input-json file://./batch-eks-job-definition.json`
```

###### Notes

- There are considerations for the `cpu` and `memory`
  parameters. For more information, see [Memory and vCPU considerations for AWS Batch on Amazon EKS](memory-cpu-batch-eks.md "memory-cpu-batch-eks.md").

## Step 7: Submit a job to

run

Run the following AWS CLI command in AWS CloudShell to submit a new Job and returns the unique
JobID.

```
`$` `aws batch submit-job --job-queue `My-Eks-JQ1` \
 --job-definition `MyJobOnEks_Sleep` - -job-name `My-Eks-Job1``
```

###### Notes

- For more information about running jobs on Amazon EKS resources, see [Amazon EKS jobs](eks-jobs.md "eks-jobs.md").

## Step 8: View the Job's output

To check the status of a Job:

```
`$` `aws batch describe-jobs --job `<JobID-from-submit-response>``
```

The `startedAt` and `stoppedAt` should be one minute apart.

## Step 9: (Optional) Submit a

job with overrides

This job overrides the command passed to the container.

```
`$` `cat <<EOF > ./submit-job-override.json
{
 "jobName": "`EksWithOverrides`",
 "jobQueue": "`My-Eks-JQ1`",
 "jobDefinition": "`MyJobOnEks_Sleep`",
 "eksPropertiesOverride": {
 "podProperties": {
 "containers": [
 {
 "command": [
 "/bin/sh"
 ],
 "args": [
 "-c",
 "echo hello world"
 ]
 }
 ]
 }
 }
}
EOF`

```

```
`$` `aws batch submit-job - -cli-input-json file://./submit-job-override.json`
```

###### Notes

- For improved visibility into the details of the operations, enable Amazon EKS
  control plane logging. For more information, see [Amazon EKS control plane
  logging](../../../eks/latest/userguide/control-plane-logs.md "../../../eks/latest/userguide/control-plane-logs.md") in the **Amazon EKS User Guide**.
- Daemonsets and kubelets overhead affects
  available vCPU and memory resources, specifically scaling and job placement. For
  more information, see [Memory and vCPU considerations for AWS Batch on Amazon EKS](memory-cpu-batch-eks.md "memory-cpu-batch-eks.md").

## Step 10: Clean up your tutorial resources

You are charged for the Amazon EC2 instance while it is enabled. You can delete the instance to
stop incurring charges.

To delete the resources you created, do the following:

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. In the navigation pane choose **Job queue**.
3. In the **Job queue** table choose the Job queue you created for the
   tutorial.
4. From **Actions** choose **Disable**. Once
   the Job queue **State** is Disabled you can choose
   **Delete**.
5. Once the Job queue is deleted, in the navigation pane choose **Compute
   environments**.
6. Choose the compute environment you created for this tutorial and then choose
   **Disable** from **Actions**. It may take
   1–2 minuets for the compute environment to complete being disabled.
7. Once the compute environment’s **State** is Disabled, choose
   **Delete**. It may take 1–2 minuets for the compute environment
   to be deleted.

## Additional resources

After you complete the tutorial, you might want to explore the following topics::

- Learn more about the [Best
  practices](best-practices.md#best-practices.title "best-practices.md#best-practices.title").
- Explore the AWS Batch core components. For more information, see [Components of AWS Batch](batch_components.md "batch_components.md").
- Learn more about the different [Compute
  Environments](compute_environments.md#compute_environments.title "compute_environments.md#compute_environments.title") available in AWS Batch.
- Learn more about [Job queues](job_queues.md#job_queues.title "job_queues.md#job_queues.title") and their
  different scheduling options.
- Learn more about [Job definitions](job_definitions.md#job_definitions.title "job_definitions.md#job_definitions.title") and the
  different configuration options.
- Learn more about the different types of [Jobs](jobs.md#jobs.title "jobs.md#jobs.title").

## Troubleshooting

If nodes launched by AWS Batch don't have access to the Amazon ECR repository (or any other
repository) that stores your image, then your jobs could remain in the STARTING state.
This is because the pod will not be able to download the image and run your AWS Batch job.
If you click on the pod name launched by AWS Batch you should be able to see the error
message and confirm the issue. The error message should look similar to the
following:

```
Failed to pull image "public.ecr.aws/amazonlinux/amazonlinux:2": rpc error: code =
Unknown desc = failed to pull and unpack image
"public.ecr.aws/amazonlinux/amazonlinux:2": failed to resolve reference
"public.ecr.aws/amazonlinux/amazonlinux:2": failed to do request: Head
"https://public.ecr.aws/v2/amazonlinux/amazonlinux/manifests/2": dial tcp: i/o timeout
```

For other common troubleshooting scenarios, see [Troubleshooting AWS Batch](batch-eks-troubleshooting.md "batch-eks-troubleshooting.md"). For troubleshooting based on pod status, see
[_How do I troubleshoot the pod status in Amazon
EKS?_](https://repost.aws/knowledge-center/eks-pod-status-troubleshooting "https://repost.aws/knowledge-center/eks-pod-status-troubleshooting").
