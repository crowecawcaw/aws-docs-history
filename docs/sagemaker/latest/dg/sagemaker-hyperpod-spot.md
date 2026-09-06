

# Spot instances in Amazon SageMaker HyperPod
<a name="sagemaker-hyperpod-spot"></a>

Amazon SageMaker HyperPod supports Amazon EC2 Spot Instances, enabling significant cost savings for fault-tolerant and stateless AI/ML workloads. Use cases include batch inference and training jobs, hyperparameter tuning, and experimental workloads. You can also use Spot Instances to automatically scale your compute capacity when this low-cost capacity is available and scale back to On-Demand capacity when the added Spot capacity is reclaimed.

By default, Spot Instances on HyperPod work with HyperPod’s [continuous provisioning feature](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-scaling-eks.html), which enables SageMaker HyperPod to automatically provision remaining capacity in the background while workloads start immediately on available instances. When node provisioning encounters failures due to capacity constraints or other issues, SageMaker HyperPod automatically retries in the background until clusters reach their desired scale, so your autoscaling operations remain resilient and non-blocking. You can also use Spot Instances with [Karpenter-based](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling.html) autoscaling.

**Key Capabilities & Concepts to consider**
+ Capture up to 90% cost savings compared to On-Demand instances
+ Use Spot Instances for jobs that can handle interruptions and where job start and completion times are flexible
+ When using Karpenter for automatic scaling, you can configure HyperPod to automatically fallback to On-Demand when Spot capacity is interrupted or unavailable
+ Access a wide range of CPU, GPU, and accelerator instance types supported by HyperPod
+ Capacity availability depends on supply from EC2 and varies by region and instance type
+ You can perform various actions such as identifying the likelihood of obtaining desired instances or getting interrupted, using various tools such as [Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/) provided by EC2

## Getting started
<a name="sagemaker-hyperpod-spot-instance-getstart"></a>

### Prerequisites
<a name="sagemaker-hyperpod-spot-instance-getstart-prereq"></a>

Before you begin, ensure you have:

#### AWS CLI installed and configured
<a name="sagemaker-hyperpod-spot-instance-getstart-prereq-cli"></a>

Set up your AWS credentials and region:

```
aws configure
```

Refer to the [AWS credentials documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html) for detailed instructions.

#### IAM Role for SageMaker HyperPod execution
<a name="sagemaker-hyperpod-spot-instance-getstart-prereq-iam"></a>

To update the cluster, you must first create [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) permissions for Karpenter. For instructions, see [Create an IAM role for HyperPod autoscaling with Karpenter](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling-iam.html).

#### VPC and EKS Cluster Setup
<a name="sagemaker-hyperpod-spot-instance-getstart-prereq-cluster"></a>

**2.1 Create VPC and EKS Cluster**

Follow the [HyperPod EKS setup guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-install-packages-using-helm-chart.html) to:

1. Create a VPC with subnets in multiple Availability Zones

1. Create an EKS cluster

1. Install [required dependencies](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-install-packages-using-helm-chart.html) using Helm charts

**2.2 Set Environment Variables**

```
export EKS_CLUSTER_ARN="arn:aws:eks:REGION:ACCOUNT_ID:cluster/CLUSTER_NAME"
export EXECUTION_ROLE="arn:aws:iam::ACCOUNT_ID:role/SageMakerExecutionRole"
export BUCKET_NAME="your-s3-bucket-name"
export SECURITY_GROUP="sg-xxxxx"
export SUBNET="subnet-xxxxx"
export SUBNET1="subnet-xxxxx"
export SUBNET2="subnet-xxxxx"
export SUBNET3="subnet-xxxxx"
```

#### Service quotas for the Spot instances
<a name="sagemaker-hyperpod-spot-instance-getstart-prereq-quota"></a>

Verify you have the required quotas for the instances you will create in the SageMaker HyperPod cluster. To review your quotas, on the Service Quotas console, choose AWS services in the navigation pane, then choose SageMaker. For example, the following screenshot shows the available quota for c5 instances.

![An image containing cost region information.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/Screenshot-cluster-quota.png)


#### Check Spot Availability
<a name="sagemaker-hyperpod-spot-instance-getstart-prereq-availability"></a>

Before creating Spot instance groups, check availability in different Availability Zones:

```
aws ec2 get-spot-placement-scores \
  --region us-west-2 \
  --instance-types c5.2xlarge \
  --target-capacity 10 \
  --single-availability-zone \
  --region-names us-west-2
```

**Tip**: Target Availability Zones with higher placement scores for better availability. You can also check Spot Instance Advisor and EC2 Spot pricing for availability. Select required Availability Zone with better availability score and configure Instance group with associated subnet to launch instance in that AZ.

### Creating a Instance Group (No Autoscaling)
<a name="sagemaker-hyperpod-spot-instance-getstart-create"></a>

**CreateCluster (Spot)**

```
aws sagemaker create-cluster \
    --cluster-name clusterNameHere \
    --orchestrator 'Eks={ClusterArn='$EKS_CLUSTER_ARN'}' \
    --node-provisioning-mode "Continuous" \
    --cluster-role 'arn:aws:iam::YOUR-ACCOUNT-ID:role/SageMakerHyperPodRole' \
    --instance-groups '[{
        "InstanceGroupName": "auto-spot-c5-2x-az1",
        "InstanceType": "ml.c5.2xlarge",
        "InstanceCount": 2,
        "CapacityRequirements: { "Spot": {} }
        "LifeCycleConfig": {
        "SourceS3Uri": "s3://'$BUCKET_NAME'",
        "OnCreate": "on_create_noop.sh"
        },
        "ExecutionRole": "'$EXECUTION_ROLE'",
        "ThreadsPerCore": 1,
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["'$SECURITY_GROUP'"],
            "Subnets": ["'$SUBNET1'"]
         }
    }]' 
    --vpc-config '{
        "SecurityGroupIds": ["'$SECURITY_GROUP'"],
        "Subnets": ["'$SUBNET'"] 
    }'
```

**Update Cluster (Spot \+ On-Demand)**

```
aws sagemaker update-cluster \
   --cluster-name "my-cluster" \
   --instance-groups '[{
        "InstanceGroupName": "auto-spot-c5-x-az3",
        "InstanceType": "ml.c5.xlarge",
        "InstanceCount": 2,
        "CapacityRequirements: { "Spot": {} },
        "LifeCycleConfig": {
            "SourceS3Uri": "s3://'$BUCKET_NAME'",
            "OnCreate": "on_create_noop.sh"
        },
        "ExecutionRole": "'$EXECUTION_ROLE'",
        "ThreadsPerCore": 1,
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["'$SECURITY_GROUP'"],
            "Subnets": ["'$SUBNET3'"]
        }
    },
    {
        "InstanceGroupName": "auto-spot-c5-2x-az2",
        "InstanceType": "ml.c5.2xlarge",
        "InstanceCount": 2,
        "CapacityRequirements: { "Spot": {} }
        "LifeCycleConfig": {
        "SourceS3Uri": "s3://'$BUCKET_NAME'",
        "OnCreate": "on_create_noop.sh"
        },
        "ExecutionRole": "'$EXECUTION_ROLE'",
        "ThreadsPerCore": 1,
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["'$SECURITY_GROUP'"],
            "Subnets": ["'$SUBNET2'"]
         }
    },
    {   
        "InstanceGroupName": "auto-ondemand-c5-2x-az1",
        "InstanceType": "ml.c5.2xlarge",
        "InstanceCount": 2,
        "LifeCycleConfig": {
        "SourceS3Uri": "s3://'$BUCKET_NAME'",
        "OnCreate": "on_create_noop.sh"
        },
        "ExecutionRole": "'$EXECUTION_ROLE'",
        "ThreadsPerCore": 1,
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["'$SECURITY_GROUP'"],
            "Subnets": ["'$SUBNET1'"]
         }
    }]'
```

`CapacityRequirements` cannot be modified once an Instance Group is created.

**Describe Cluster**

```
aws sagemaker describe-cluster --cluster-name $HP_CLUSTER_NAME --region us-west-2
```

```
## Sample Response
{
    "ClusterName": "my-cluster",
    "InstanceGroups": [
        {
            "InstanceGroupName": "ml.c5.2xlarge",
            "InstanceType": "ml.c5.xlarge",
            "InstanceCount": 5,
            "CurrentCount": 3,
            "CapacityRequirements: { "Spot": {} },
            "ExecutionRole": "arn:aws:iam::account:role/SageMakerExecutionRole",
            "InstanceStorageConfigs": [...],
            "OverrideVpcConfig": {...}
        }
        // Other IGs
    ]
}
```

**DescribeClusterNode**

```
aws sagemaker describe-cluster-node --cluster-name $HP_CLUSTER_NAME --region us-west-2
```

```
## Sample Response
{
  "NodeDetails": {
    "InstanceId": "i-1234567890abcdef1",
    "InstanceGroupName": "ml.c5.2xlarge",
    "CapacityType": "Spot",
    "InstanceStatus": {...}
  }
}
```

### Using Console
<a name="sagemaker-hyperpod-spot-instance-getstart-console"></a>

#### Create and configure a SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-spot-instance-getstart-console-create"></a>

To begin, launch and configure your SageMaker HyperPod EKS cluster and verify that continuous provisioning mode is enabled on cluster creation. Complete the following steps:

1. On the SageMaker AI console, choose HyperPod clusters in the navigation pane.

1. Choose Create HyperPod cluster and Orchestrated on Amazon EKS.

1. For Setup options, select Custom setup.

1. For Name, enter a name.

1. For Instance recovery, select Automatic.

1. For Instance provisioning mode, select Use continuous provisioning.

1. CapacityType : Select Spot 

1. Choose Submit.

Screen shot of Console : 

![An image containing the creation cluster flow.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/Screenshot-create-cluster.png)


This setup creates the necessary configuration such as virtual private cloud (VPC), subnets, security groups, and EKS cluster, and installs operators in the cluster. You can also provide existing resources such as an EKS cluster if you want to use an existing cluster instead of creating a new one. This setup will take around 20 minutes.

#### Adding new Spot Instance Group to the same cluster
<a name="sagemaker-hyperpod-spot-instance-getstart-console-add"></a>

To add an Spot IG to your existing HyperPod EKS cluster. Complete the following steps:

1. On the SageMaker AI console, choose HyperPod clusters in the navigation pane.

1. Select an existing HyperPod cluster with Amazon EKS Orchestration (Ensure continuous provisioning is enabled).

1. Click Edit.

1. On the Edit Cluster page, click Create instance group.

1. Select capacity type: Spot instance in the instance group configuration.

1. Click Create instance group. 

1. Click Submit.

**Screen shot of Console : **

![An image containing the instance group creation flow.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/Screenshot-instance-group.png)


### Using CloudFormation
<a name="sagemaker-hyperpod-spot-instance-getstart-cfn"></a>

```
Resources:
  TestCluster:
    Type: AWS::SageMaker::Cluster
    Properties:
      ClusterName: "SampleCluster"
      InstanceGroups:
        - InstanceGroupName: group1
          InstanceType: ml.c5.2xlarge
          InstanceCount: 1
          LifeCycleConfig:
            SourceS3Uri: "s3://'$BUCKET_NAME'"
            OnCreate: "on_create_noop.sh"
          ExecutionRole: "'$EXECUTION_ROLE'",
          ThreadsPerCore: 1
          CapacityRequirements:
            Spot: {}
      VpcConfig:
        Subnets:
          - "'$SUBNET1'"
        SecurityGroupIds:
          - "'$SECURITY_GROUP'"
      Orchestrator:
        Eks:
          ClusterArn:
            '$EKS_CLUSTER_ARN'
      NodeProvisioningMode: "Continuous"
      NodeRecovery: "Automatic"
```

Please see [https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-eks-console-create-cluster-cfn.html](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-eks-console-create-cluster-cfn.html) for details.

### Karpenter based Autoscaling
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter"></a>

#### Create cluster role
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter-role"></a>

**Step 1: Navigate to IAM Console**

1. Go to the **AWS Management Console** → **IAM** service

1. Click **Roles** in the left sidebar

1. Click **Create role**

**Step 2: Set up Trust Policy**

1. Select Custom trust policy (instead of AWS service)

1. Replace the default JSON with this trust policy:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "hyperpod.sagemaker.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

click Next

**Step 3: Create Custom Permissions Policy**

Since these are specific SageMaker permissions, you'll need to create a custom policy:

1. Click **Create policy** (opens new tab)

1. Click the **JSON** tab

1. Enter this policy:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "sagemaker:BatchAddClusterNodes",
           "sagemaker:BatchDeleteClusterNodes"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

1. Click **Next**

1. Give it a name like `SageMakerHyperPodRolePolicy`

1. Click **Create policy**

**Step 4: Attach the Policy to Role**

1. Go back to your role creation tab

1. Refresh the policies list

1. Search for and select your newly created policy

1. Click **Next**

**Step 5: Name and Create Role**

1. Enter a role name (e.g., `SageMakerHyperPodRole`)

1. Add a description if desired

1. Review the trust policy and permissions

1. Click **Create role**

#### Verification
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter-verify"></a>

After creation, you can verify by:
+ Checking the Trust relationships tab shows the hyperpod service
+ Checking the Permissions tab shows your custom policy
+ The role ARN will be available for use with HyperPod

The role ARN format will be:

```
 arn:aws:iam::YOUR-ACCOUNT-ID:role/SageMakerHyperPodRole
```

#### Create Cluster with AutoScaling:
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter-create-cluster"></a>

For better availability, create IGs in multiple AZs by configuring Subnets. You can also include onDemand IGs for fallback.

```
aws sagemaker create-cluster \
    --cluster-name clusterNameHere \
    --orchestrator 'Eks={ClusterArn='$EKS_CLUSTER_ARN'}' \
    --node-provisioning-mode "Continuous" \
    --cluster-role 'arn:aws:iam::YOUR-ACCOUNT-ID:role/SageMakerHyperPodRole' \
    --instance-groups '[{
        "InstanceGroupName": "auto-spot-c5-2x-az1",
        "InstanceType": "ml.c5.2xlarge",
        "InstanceCount": 0, // For Auto scaling keep instance count as 0
        "CapacityRequirements: { "Spot": {} }
        "LifeCycleConfig": {
        "SourceS3Uri": "s3://'$BUCKET_NAME'",
        "OnCreate": "on_create_noop.sh"
        },
        "ExecutionRole": "'$EXECUTION_ROLE'",
        "ThreadsPerCore": 1,
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["'$SECURITY_GROUP'"],
            "Subnets": ["'$SUBNET1'"]
         }
    }]' 
--vpc-config '{
    "SecurityGroupIds": ["'$SECURITY_GROUP'"],
    "Subnets": ["'$SUBNET'"] 
}'
--auto-scaling ' {
    "Mode": "Enable",
    "AutoScalerType": "Karpenter"
}'
```

#### Update Cluster (Spot \+ On-Demand)
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter-update-cluster"></a>

```
aws sagemaker update-cluster \
   --cluster-name "my-cluster" \
   --instance-groups '[{
        "InstanceGroupName": "auto-spot-c5-x-az3",
        "InstanceType": "ml.c5.xlarge",
        "InstanceCount": 2,
        "CapacityRequirements: { "Spot": {} },
        "LifeCycleConfig": {
            "SourceS3Uri": "s3://'$BUCKET_NAME'",
            "OnCreate": "on_create_noop.sh"
        },
        "ExecutionRole": "'$EXECUTION_ROLE'",
        "ThreadsPerCore": 1,
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["'$SECURITY_GROUP'"],
            "Subnets": ["'$SUBNET3'"]
        }
    },
    {
        "InstanceGroupName": "auto-spot-c5-2x-az2",
        "InstanceType": "ml.c5.2xlarge",
        "InstanceCount": 2,
        "CapacityRequirements: { "Spot": {} }
        "LifeCycleConfig": {
        "SourceS3Uri": "s3://'$BUCKET_NAME'",
        "OnCreate": "on_create_noop.sh"
        },
        "ExecutionRole": "'$EXECUTION_ROLE'",
        "ThreadsPerCore": 1,
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["'$SECURITY_GROUP'"],
            "Subnets": ["'$SUBNET2'"]
         }
    },
    {   
        "InstanceGroupName": "auto-ondemand-c5-2x-az1",
        "InstanceType": "ml.c5.2xlarge",
        "InstanceCount": 2,
        "LifeCycleConfig": {
        "SourceS3Uri": "s3://'$BUCKET_NAME'",
        "OnCreate": "on_create_noop.sh"
        },
        "ExecutionRole": "'$EXECUTION_ROLE'",
        "ThreadsPerCore": 1,
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["'$SECURITY_GROUP'"],
            "Subnets": ["'$SUBNET1'"]
         }
    }]'
```

#### Create HyperpodNodeClass
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter-create-class"></a>

`HyperpodNodeClass` is a custom resource that maps to pre-created instance groups in SageMaker HyperPod, defining constraints around which instance types and Availability Zones are supported for Karpenter’s auto scaling decisions. To use `HyperpodNodeClass`, simply specify the names of the `InstanceGroups` of your SageMaker HyperPod cluster that you want to use as the source for the AWS compute resources to use to scale up your pods in your NodePools. The `HyperpodNodeClass` name that you use here is carried over to the NodePool in the next section where you reference it. This tells the NodePool which `HyperpodNodeClass` to draw resources from. To create a `HyperpodNodeClass`, complete the following steps:

1. Create a YAML file (for example, nodeclass.yaml) similar to the following code. Add `InstanceGroup` names that you used at the time of the SageMaker HyperPod cluster creation. You can also add new instance groups to an existing SageMaker HyperPod EKS cluster.

1. Reference the `HyperPodNodeClass` name in your NodePool configuration.

The following is a sample `HyperpodNodeClass` :

```
apiVersion: karpenter.sagemaker.amazonaws.com/v1
kind: HyperpodNodeClass
metadata:
  name: multiazg6
spec:
  instanceGroups:
    # name of InstanceGroup in HyperPod cluster. InstanceGroup needs to pre-created
    # before this step can be completed.
    # MaxItems: 10
    - auto-spot-c5-2x-az1
    - auto-spot-c5-2x-az2
    - auto-spot-c5-x-az3
    - auto-ondemand-c5-2x-az1
```

Karpenter prioritizes Spot instance groups over On-Demand instances, using On-Demand as a fallback when specified in the configuration. Instance selection is sorted by EC2 Spot Placement Scores associated with each subnet's availability zone.

**Apply the configuration to your EKS cluster using `kubectl`:**

```
kubectl apply -f nodeclass.yaml
```

The HyperPod cluster must have AutoScaling enabled and the AutoScaling status must change to `InService` before the `HyperpodNodeClass` can be applied. It also shows Instance Groups capacities as Spot or OnDemand. For more information and key considerations, see [Autoscaling on SageMaker HyperPod EKS](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling.html).

**For example**

```
apiVersion: karpenter.sagemaker.amazonaws.com/v1
kind: HyperpodNodeClass
metadata:
  creationTimestamp: "2025-11-30T03:25:04Z"
  name: multiazc6
  uid: ef5609be-15dd-4700-89ea-a3370e023690
spec:
  instanceGroups:
  -spot1
status:
  conditions:
  // true when all IGs in the spec are present in SageMaker cluster, false otherwise
  - lastTransitionTime: "2025-11-20T03:25:04Z"
    message: ""
    observedGeneration: 3
    reason: InstanceGroupReady
    status: "True"
    type: InstanceGroupReady
  // true if subnets of IGs are discoverable, false otherwise
  - lastTransitionTime: "2025-11-20T03:25:04Z"
    message: ""
    observedGeneration: 3
    reason: SubnetsReady
    status: "True"
    type: SubnetsReady
  // true when all dependent resources are Ready [InstanceGroup, Subnets]
  - lastTransitionTime: "2025-11-30T05:47:55Z"
    message: ""
    observedGeneration: 3
    reason: Ready
    status: "True"
    type: Ready
  instanceGroups:
  - instanceTypes:
    - ml.c5.2xlarge
    name:auto-spot-c5-2x-az2
    subnets:
    - id: subnet-03ecc649db2ff20d2
      zone: us-west-2a
      zoneId: usw2-az2
  - capacities: {"Spot": {}}
```

#### Create NodePool
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter-create-nodepool"></a>

The NodePool sets constraints on the nodes that can be created by Karpenter and the pods that can run on those nodes. The NodePool can be set to perform various actions, such as: 
+ Define labels and taints to limit the pods that can run on nodes Karpenter creates
+ Limit node creation to certain zones, instance types, and computer architectures, and so on

For more information about NodePool, refer to [NodePools](https://karpenter.sh/docs/concepts/nodepools/). SageMaker HyperPod managed Karpenter supports a limited set of well-known Kubernetes and Karpenter requirements, which we explain in this post.

To create a NodePool, complete the following steps:

Create a YAML file named `nodepool.yaml` with your desired NodePool configuration. The following code is a sample configuration to create a sample NodePool. We specify the NodePool to include our ml.g6.xlarge SageMaker instance type, and we additionally specify it for one zone. Refer to [NodePools](https://karpenter.sh/docs/concepts/nodepools/) for more customizations.

```
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
 name: gpunodepool
spec:
 template:
   spec:
     nodeClassRef:
      group: karpenter.sagemaker.amazonaws.com
      kind: HyperpodNodeClass
      name: multiazg6
     expireAfter: Never
     requirements:
        - key: node.kubernetes.io/instance-type
          operator: Exists
        - key: "node.kubernetes.io/instance-type" // Optional otherwise Karpenter will decide based on Job config resource requirements
          operator: In
          values: ["ml.c5.2xlarge"]
        - key: "topology.kubernetes.io/zone"
          operator: In
          values: ["us-west-2a"]
```

**Tip**: On EC2 Spot interruption, Hyperpod taints node to trigger pod eviction. Karpenter’s **consolidation** process respects pod disruption budgets and performs normal Kubernetes eviction, but if you set consolidateAfter: 0, then consolidation can happen **immediately**, giving very little time for graceful pod eviction. Set it to non zero upto 2 min to allow graceful pod eviction for any checkpointing needs.

**Apply the NodePool to your cluster:**

```
kubectl apply -f nodepool.yaml
```

**Monitor the NodePool status to ensure the Ready condition in the status is set to True:**

```
kubectl get nodepool gpunodepool -oyaml
```

This example shows how a NodePool can be used to specify the hardware (instance type) and placement (Availability Zone) for pods.

**Launch a simple workload**

The following workload runs a Kubernetes deployment where the pods in deployment are requesting for 1 CPU and 256 MB memory per replica, per pod. The pods have not been spun up yet.

```
kubectl apply -f https://raw.githubusercontent.com/aws/karpenter-provider-aws/refs/heads/main/examples/workloads/inflate.yaml
```

When we apply this, we can see a deployment and a single node launch in our cluster, as shown in the following screenshot.

**To scale this component, use the following command:**

```
kubectl scale deployment inflate --replicas 10
```

See [https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling.html](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling.html) for more details.

### Managing Node Interruption
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter-interrupt"></a>

Spot Instances can be reclaimed at any time. EC2 provides a best-effort 2-minute interruption notice in most cases, but this notice is not guaranteed. In some situations, EC2 may terminate Spot Instances immediately without any advance warning.HyperPod automatically handles both scenarios:
+ With 2-minute notice: Automatically reattempts graceful pod eviction and controlled capacity replacement when Spot capacity becomes available.
+ Without notice (immediate termination): Automatically reattempts node replacement (when Spot capacity becomes available) without graceful eviction 

**How it works**

When EC2 sends a Spot interruption notice, HyperPod automatically:

1. Detects interruption signal 

1. Taints the node: Prevents new pods from being scheduled on the interrupted instance

1. Gracefully evicts pods: Gives running pods time to complete or checkpoint their work (respecting Kubernetes `terminationGracePeriodSeconds`)

1. Replaces capacity: Automatically attempts to provision the replacement instances (Spot or On-Demand based on availability). 

   Capacity replacement works by automatically provisioning replacement instances. When capacity is not immediately available, the system continues checking until resources become accessible. In the case of non-autoscaling instance groups, HyperPod attempts to scale up within the same instance group until the required capacity becomes available. For Karpenter-based instance groups, Karpenter implements a fallback mechanism to other instance groups configured in the Node class when the primary group cannot accommodate the demand. Additionally, you can configure On-Demand as a fallback option, allowing Karpenter to automatically switch to On-Demand instances if it cannot successfully scale up Spot instance groups.

1. Reschedules workloads: Kubernetes automatically reschedules evicted pods on healthy nodes

### Finding your Usage and Bill
<a name="sagemaker-hyperpod-spot-instance-getstart-karpenter-bill"></a>

To check your usage and billing for Spot Instances on HyperPod you can use the AWS Cost Explorer Console. Go to Billing and Cost Management > Bill

![An image containing cost region information.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/Screenshot-cost-region.png)


**To explore usage and billing on Console, go to Billing and Cost Management > Cost Explorer**

![An image containing cost and usage.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/Screenshot-cost-usage.png)
