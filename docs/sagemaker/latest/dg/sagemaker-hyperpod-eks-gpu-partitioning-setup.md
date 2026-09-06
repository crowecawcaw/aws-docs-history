

# Setting up GPU partitions on Amazon SageMaker HyperPod
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup"></a>

**Topics**
+ [Prerequisites](#sagemaker-hyperpod-eks-gpu-partitioning-setup-prerequisites)
+ [Creating a Cluster with MIG Configuration](#sagemaker-hyperpod-eks-gpu-partitioning-setup-create-cluster)
+ [Adding GPU operator to an existing cluster](#sagemaker-hyperpod-eks-gpu-partitioning-setup-add-operator)
+ [Updating MIG Configuration](#sagemaker-hyperpod-eks-gpu-partitioning-setup-update)
+ [Verifying MIG Configuration](#sagemaker-hyperpod-eks-gpu-partitioning-setup-verify)
+ [Common Commands for Debugging MIG Configuration](#sagemaker-hyperpod-eks-gpu-partitioning-setup-debug-commands)
+ [Using SageMaker AI Console](#sagemaker-hyperpod-eks-gpu-partitioning-setup-console)

## Prerequisites
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-prerequisites"></a>
+ HyperPod Amazon EKS cluster with supported GPU instances
+ NVIDIA GPU Operator installed
+ Appropriate IAM permissions for cluster management

## Creating a Cluster with MIG Configuration
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-create-cluster"></a>

### Using AWS CLI
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-create-cluster-cli"></a>

```
aws sagemaker create-cluster \
  --cluster-name my-mig-cluster \
  --orchestrator 'Eks={ClusterArn=arn:aws:eks:{{region}}:{{account}}:cluster/{{cluster-name}}}' \
  --instance-groups '{
    "InstanceGroupName": "gpu-group",
    "InstanceType": "ml.p4d.24xlarge",
    "InstanceCount": 1,
    "LifeCycleConfig": {
       "SourceS3Uri": "s3://{{my-bucket}}",
       "OnCreate": "on_create_script.sh"
    },
    "KubernetesConfig": {
       "Labels": {
          "nvidia.com/mig.config": "all-1g.5gb"
       }
    },
    "ExecutionRole": "arn:aws:iam::{{account}}:role/{{execution-role}}",
    "ThreadsPerCore": 1
  }' \
  --vpc-config '{
     "SecurityGroupIds": ["{{sg-12345}}"],
     "Subnets": ["{{subnet-12345}}"]
  }' \
  --node-provisioning-mode Continuous
```

### Using CloudFormation
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-create-cluster-cfn"></a>

```
{
  "ClusterName": "my-mig-cluster",
  "InstanceGroups": [
    {
      "InstanceGroupName": "gpu-group",
      "InstanceType": "ml.p4d.24xlarge",
      "InstanceCount": 1,
      "KubernetesConfig": {
        "Labels": {
          "nvidia.com/mig.config": "all-2g.10gb"
        }
      },
      "ExecutionRole": "arn:aws:iam::{{account}}:role/{{execution-role}}"
    }
  ],
  "Orchestrator": {
    "Eks": {
      "ClusterArn": "arn:aws:eks:{{region}}:{{account}}:cluster/{{cluster-name}}"
    }
  },
  "NodeProvisioningMode": "Continuous"
}
```

## Adding GPU operator to an existing cluster
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-add-operator"></a>

### Install GPU Operator
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-add-operator-install"></a>

Replace `{$AWS_REGION}` with your cluster region (e.g., us-east-1, us-west-2).

```
helm install gpuo helm_chart/HyperPodHelmChart/charts/gpu-operator \
-f helm_chart/HyperPodHelmChart/charts/gpu-operator/regional-values/values-{$AWS_REGION}.yaml \
-n kube-system
```

### Verify Installation (Wait 2-3 minutes)
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-add-operator-verify"></a>

Check all GPU operator pods are running:

```
kubectl get pods -n kube-system | grep -E "(gpu-operator|nvidia-)"
```

**Expected pods:**
+ gpu-operator-\* - 1 instance (cluster controller)
+ nvidia-device-plugin-daemonset-\* - 1 per GPU node (all GPU instances)
+ nvidia-mig-manager-\* - 1 per MIG-capable node (A100/H100)

### Remove Old Device Plugin
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-add-operator-remove"></a>

Disable the existing nvidia-device-plugin:

```
helm upgrade dependencies helm_chart/HyperPodHelmChart \
--set nvidia-device-plugin.devicePlugin.enabled=false \
-n kube-system
```

### Verify GPU Resources
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-add-operator-verify-gpu"></a>

Confirm nodes show GPU capacity. It should display: nvidia.com/gpu: 8 (or your actual GPU count).

```
kubectl describe nodes | grep "nvidia.com/gpu"
```

## Updating MIG Configuration
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-update"></a>

**Preparing Nodes Before MIG Updates**  
Before updating MIG configurations on your instance group, you must prepare the nodes to prevent workload disruption. Follow these steps to safely drain workloads from the nodes that will be reconfigured.

### Step 1: Identify Nodes in the Instance Group
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-update-identify"></a>

First, identify all nodes that belong to the instance group you want to update:

```
# List all nodes in the instance group
kubectl get nodes -l sagemaker.amazonaws.com/instance-group-name={{INSTANCE_GROUP_NAME}}

# Example:
kubectl get nodes -l sagemaker.amazonaws.com/instance-group-name=p4d-group
```

This command returns a list of all nodes in the specified instance group. Make note of each node name for the following steps.

### Step 2: Cordon and Drain Each Node
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-update-drain"></a>

For each node identified in Step 1, perform the following actions:

#### Cordon the Node
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-update-drain-cordon"></a>

Cordoning prevents new pods from being scheduled on the node:

```
# Cordon a single node
kubectl cordon {{NODE_NAME}}

# Example:
kubectl cordon hyperpod-i-014a41a7001adca60
```

#### Drain Workload Pods from the Node
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-update-drain-evict"></a>

Drain the node to evict all workload pods while preserving system pods:

```
# Drain the node (ignore DaemonSets and evict pods)
kubectl drain {{NODE_NAME}} \
  --ignore-daemonsets \
  --delete-emptydir-data \
  --force \
  --grace-period=300

# Example:
kubectl drain hyperpod-i-014a41a7001adca60 \
  --ignore-daemonsets \
  --delete-emptydir-data \
  --force \
  --grace-period=300
```

**Command Options Explained:**
+ `--ignore-daemonsets` - Allows the drain operation to proceed even if DaemonSet pods are present
+ `--delete-emptydir-data` - Deletes pods using emptyDir volumes (required for draining to succeed)
+ `--force` - Forces deletion of pods not managed by a controller (use with caution)
+ `--grace-period=300` - Gives pods 5 minutes to terminate gracefully

**Important**  
The drain operation may take several minutes depending on the number of pods and their termination grace periods
System pods in the following namespaces will remain running: `kube-system`, `cert-manager`, `kubeflow`, `hyperpod-inference-system`, `kube-public`, `mpi-operator`, `gpu-operator`, `aws-hyperpod`, `jupyter-k8s-system`, `hyperpod-observability`, `kueue-system`, and `keda`
DaemonSet pods will remain on the node (they are ignored by design)

### Step 3: Verify No Workload Pods are Running
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-update-verify"></a>

After draining, verify that no workload pods remain on the nodes (excluding system namespaces):

```
# Check for any remaining pods outside system namespaces
kubectl get pods --all-namespaces --field-selector spec.nodeName={{NODE_NAME}} \
  | grep -v "kube-system" \
  | grep -v "cert-manager" \
  | grep -v "kubeflow" \
  | grep -v "hyperpod-inference-system" \
  | grep -v "kube-public" \
  | grep -v "mpi-operator" \
  | grep -v "gpu-operator" \
  | grep -v "aws-hyperpod" \
  | grep -v "jupyter-k8s-system" \
  | grep -v "hyperpod-observability" \
  | grep -v "kueue-system" \
  | grep -v "keda"

# Example:
kubectl get pods --all-namespaces --field-selector spec.nodeName=hyperpod-i-014a41a7001adca60 \
  | grep -v "kube-system" \
  | grep -v "cert-manager" \
  | grep -v "kubeflow" \
  | grep -v "hyperpod-inference-system" \
  | grep -v "kube-public" \
  | grep -v "mpi-operator" \
  | grep -v "gpu-operator" \
  | grep -v "aws-hyperpod" \
  | grep -v "jupyter-k8s-system" \
  | grep -v "hyperpod-observability" \
  | grep -v "kueue-system" \
  | grep -v "keda"
```

**Expected Output:** If the node is properly drained, this command should return no results (or only show the header row). If any pods are still running, investigate why they weren't evicted and manually delete them if necessary.

### Step 4: Verify Node Readiness Status
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-update-readiness"></a>

Before proceeding with the MIG update, confirm that all nodes are cordoned:

```
# Check node status - should show "SchedulingDisabled"
kubectl get nodes -l sagemaker.amazonaws.com/instance-group-name={{INSTANCE_GROUP_NAME}}
```

Nodes should show `SchedulingDisabled` in the STATUS column, indicating they are cordoned and ready for the MIG update.

### Update MIG Profile on Existing Cluster
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-update-change"></a>

You can change MIG profiles on existing clusters:

```
aws sagemaker update-cluster \
  --cluster-name my-mig-cluster \
  --instance-groups '{
    "InstanceGroupName": "gpu-group",
    "InstanceType": "ml.p4d.24xlarge",
    "InstanceCount": 1,
    "KubernetesConfig": {
       "Labels": {
          "nvidia.com/mig.config": "all-3g.20gb"
       }
    },
    "ExecutionRole": "arn:aws:iam::{{account}}:role/{{execution-role}}"
  }'
```

**Note**  
If jobs are already running on a node, the MIG partitioning will fail. User will get error message to drain the nodes before re-attempting the MIG partitioning.

## Verifying MIG Configuration
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-verify"></a>

After cluster creation or update, verify the MIG configuration:

```
# Update kubeconfig
aws eks update-kubeconfig --name {{your-eks-cluster}} --region {{us-east-2}}

# Check MIG labels
kubectl get node {{NODE_NAME}} -o=jsonpath='{.metadata.labels}' | grep mig

# Check available MIG resources
kubectl describe node {{NODE_NAME}} | grep -A 10 "Allocatable:"
```

## Common Commands for Debugging MIG Configuration
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-debug-commands"></a>

Use the following commands to troubleshoot and validate MIG configuration in your cluster:

```
# Check GPU Operator status
kubectl get pods -n gpu-operator-resources

# View MIG configuration
kubectl exec -n gpu-operator-resources nvidia-driver-XXXXX -- nvidia-smi mig -lgi

# Check device plugin configuration
kubectl logs -n gpu-operator-resources nvidia-device-plugin-XXXXX

# Monitor node events
kubectl get events --field-selector involvedObject.name={{NODE_NAME}}
```

**Note**  
Replace `nvidia-driver-XXXXX` and `nvidia-device-plugin-XXXXX` with the actual pod names from your cluster, and `NODE_NAME` with your node's name.

## Using SageMaker AI Console
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-console"></a>

### Creating a New Cluster with MIG
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-console-create"></a>

1. Navigate to **Amazon SageMaker AI** > **HyperPod Clusters** > **Cluster Management** > **Create HyperPod cluster**

1. Select **Orchestrated by EKS**

1. Choose **Custom setup** and verify **GPU Operator** is enabled by default

1. Under **Instance groups** section, click **Add group**

1. Configure the instance group and navigate to **Advanced Configuration** to enable **Use GPU partition** toggle and choose your desired **MIG configuration** from the dropdown

1. Click **Add Instance group** and complete the remaining cluster configuration

1. Click **Submit** to create the cluster

### Updating MIG Configuration on Existing Cluster
<a name="sagemaker-hyperpod-eks-gpu-partitioning-setup-console-update"></a>

1. Navigate to **Amazon SageMaker AI** > **HyperPod Clusters** > **Cluster Management**

1. Select your existing cluster and click **Edit** on the instance group you want to modify

1. In **Advanced configuration**, toggle **Use GPU partition** if not already enabled and select a different **MIG configuration** from the dropdown

1. Click **Save changes**