

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an EKS Auto Mode Cluster with the AWS CLI
<a name="automode-get-started-cli"></a>

EKS Auto Mode Clusters automate routine cluster management tasks for compute, storage, and networking. For example, EKS Auto Mode Clusters automatically detect when additional nodes are required and provision new EC2 instances to meet workload demands.

This topic guides you through creating a new EKS Auto Mode Cluster using the AWS CLI and optionally deploying a sample workload.

## Prerequisites
<a name="_prerequisites"></a>
+ The latest version of the AWS Command Line Interface (AWS CLI) installed and configured on your device. To check your current version, use `aws --version`. To install the latest version, see [Installing](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Quick configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-configure-quickstart-config) with aws configure in the AWS Command Line Interface User Guide.
  + Login to the CLI with sufficient IAM permissions to create AWS resources including IAM Policies, IAM Roles, and EKS Clusters.
+ The kubectl command line tool installed on your device. AWS suggests you use the same kubectl version as the Kubernetes version of your EKS Cluster. To install or upgrade kubectl, see [Set up `kubectl` and `eksctl`](install-kubectl.md).

## Specify VPC subnets
<a name="_specify_vpc_subnets"></a>

Amazon EKS Auto Mode deploys nodes to VPC subnets. When creating an EKS cluster, you must specify the VPC subnets where the nodes will be deployed. You can use the default VPC subnets in your AWS account or create a dedicated VPC for critical workloads.
+  AWS suggests creating a dedicated VPC for your cluster. Learn how to [Create an Amazon VPC for your Amazon EKS cluster](creating-a-vpc.md).
+ The EKS Console assists with creating a new VPC. Learn how to [Create an EKS Auto Mode Cluster with the AWS Management Console](automode-get-started-console.md).
+ Alternatively, you can use the default VPC of your AWS account. Use the following instructions to find the Subnet IDs.

### To find the Subnet IDs of your default VPC
<a name="auto-find-subnet"></a>

 **Using the AWS CLI:** 

1. Run the following command to list the default VPC and its subnets:

   ```
   aws ec2 describe-subnets --filters "Name=vpc-id,Values=$(aws ec2 describe-vpcs --query 'Vpcs[?IsDefault==`true`].VpcId' --output text)" --query 'Subnets[*].{ID:SubnetId,AZ:AvailabilityZone}' --output table
   ```

1. Save the output and note the **Subnet IDs**.

   Sample output:

   ```
   ----------------------------------------
   |             DescribeSubnets          |
   ----------------------------------------
   |   SubnetId        |   AvailabilityZone  |
   |--------------------|---------------------|
   |   subnet-012345678 |   us-west-2a        |
   |   subnet-234567890 |   us-west-2b        |
   |   subnet-345678901 |   us-west-2c        |
   ----------------------------------------
   ```

## IAM Roles for EKS Auto Mode Clusters
<a name="auto-mode-create-roles"></a>

### Cluster IAM Role
<a name="auto-roles-cluster-iam-role"></a>

EKS Auto Mode requires a Cluster IAM Role to perform actions in your AWS account, such as provisioning new EC2 instances. You must create this role to grant EKS the necessary permissions. AWS recommends attaching the following AWS managed policies to the Cluster IAM Role:
+  [AmazonEKSComputePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSComputePolicy) 
+  [AmazonEKSBlockStoragePolicyV2](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSBlockStoragePolicyV2) 
+  [AmazonEKSLoadBalancingPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy) 
+  [AmazonEKSNetworkingPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSNetworkingPolicy) 
+  [AmazonEKSClusterPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksclusterpolicy) 

### Node IAM Role
<a name="auto-roles-node-iam-role"></a>

When you create an EKS Auto Mode cluster, you specify a Node IAM Role. When EKS Auto Mode creates nodes to process pending workloads, each new EC2 instance node is assigned the Node IAM Role. This role allows the node to communicate with EKS but is generally not accessed by workloads running on the node.

If you want to grant permissions to workloads running on a node, use EKS Pod Identity. For more information, see [Learn how EKS Pod Identity grants pods access to AWS services](pod-identities.md).

You must create this role and attach the following AWS managed policy:
+  [AmazonEKSWorkerNodeMinimalPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSWorkerNodeMinimalPolicy) 
+  [AmazonEC2ContainerRegistryPullOnly](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly) 

EKS Auto Mode also requires a Service-Linked Role, which is automatically created and configured by AWS. For more information, see [AWSServiceRoleForAmazonEKS](using-service-linked-roles-eks.md).

## Create an EKS Auto Mode Cluster IAM Role
<a name="_create_an_eks_auto_mode_cluster_iam_role"></a>

### Step 1: Create the Trust Policy
<a name="_step_1_create_the_trust_policy"></a>

Create a trust policy that allows the Amazon EKS service to assume the role. Save the policy as `trust-policy.json`:

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow", 
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
```

### Step 2: Create the IAM Role
<a name="_step_2_create_the_iam_role"></a>

Use the trust policy to create the Cluster IAM Role:

```
aws iam create-role \
    --role-name AmazonEKSAutoClusterRole \
    --assume-role-policy-document file://trust-policy.json
```

### Step 3: Note the Role ARN
<a name="_step_3_note_the_role_arn"></a>

Retrieve and save the ARN of the new role for use in subsequent steps:

```
aws iam get-role --role-name AmazonEKSAutoClusterRole --query "Role.Arn" --output text
```

### Step 4: Attach Required Policies
<a name="_step_4_attach_required_policies"></a>

Attach the following AWS managed policies to the Cluster IAM Role to grant the necessary permissions:

 **AmazonEKSClusterPolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy
```

 **AmazonEKSComputePolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSComputePolicy
```

 **AmazonEKSBlockStoragePolicyV2**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSBlockStoragePolicyV2
```

 **AmazonEKSLoadBalancingPolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSLoadBalancingPolicy
```

 **AmazonEKSNetworkingPolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSNetworkingPolicy
```

## Create an EKS Auto Mode Node IAM Role
<a name="_create_an_eks_auto_mode_node_iam_role"></a>

### Step 1: Create the Trust Policy
<a name="_step_1_create_the_trust_policy_2"></a>

Create a trust policy that allows the Amazon EKS service to assume the role. Save the policy as `node-trust-policy.json`:

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

#### Step 2: Create the Node IAM Role
<a name="_step_2_create_the_node_iam_role"></a>

Use the **node-trust-policy.json** file from the previous step to define which entities can assume the role. Run the following command to create the Node IAM Role:

```
aws iam create-role \
    --role-name AmazonEKSAutoNodeRole \
    --assume-role-policy-document file://node-trust-policy.json
```

#### Step 3: Note the Role ARN
<a name="_step_3_note_the_role_arn_2"></a>

After creating the role, retrieve and save the ARN of the Node IAM Role. You will need this ARN in subsequent steps. Use the following command to get the ARN:

```
aws iam get-role --role-name AmazonEKSAutoNodeRole --query "Role.Arn" --output text
```

#### Step 4: Attach Required Policies
<a name="_step_4_attach_required_policies_2"></a>

Attach the following AWS managed policies to the Node IAM Role to provide the necessary permissions:

 **AmazonEKSWorkerNodeMinimalPolicy**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoNodeRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodeMinimalPolicy
```

 **AmazonEC2ContainerRegistryPullOnly**:

```
aws iam attach-role-policy \
    --role-name AmazonEKSAutoNodeRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly
```

## Create an EKS Auto Mode Cluster
<a name="_create_an_eks_auto_mode_cluster"></a>

### Overview
<a name="_overview"></a>

To create an EKS Auto Mode Cluster using the AWS CLI, you will need the following parameters:
+  `cluster-name`: The name of the cluster.
+  `k8s-version`: The Kubernetes version (e.g., 1.31).
+  `subnet-ids`: Subnet IDs identified in the previous steps.
+  `cluster-role-arn`: ARN of the Cluster IAM Role.
+  `node-role-arn`: ARN of the Node IAM Role.

#### Default Cluster Configurations
<a name="_default_cluster_configurations"></a>

Review these default values and features before creating the cluster:
+  `nodePools`: EKS Auto Mode includes general-purpose and system default Node Pools. Learn more about [Node Pools](create-node-pool.md).

 **Note:** Node Pools in EKS Auto Mode differ from Amazon EKS Managed Node Groups but can coexist in the same cluster.
+  `computeConfig.enabled`: Automates routine compute tasks, such as creating and deleting EC2 instances.
+  `kubernetesNetworkConfig.elasticLoadBalancing.enabled`: Automates load balancing tasks, including creating and deleting Elastic Load Balancers.
+  `storageConfig.blockStorage.enabled`: Automates storage tasks, such as creating and deleting Amazon EBS volumes.
+  `accessConfig.authenticationMode`: Requires EKS access entries. Learn more about [EKS authentication modes](grant-k8s-access.md).

#### Set Environment Variables
<a name="_set_environment_variables"></a>

Before running the `create-cluster` command, set the following environment variables. Replace the placeholder values with your own:

```
export AWS_REGION=us-east-1
export CLUSTER_NAME=my-auto-cluster
export K8S_VERSION=1.35
export CLUSTER_ROLE_ARN=arn:aws:iam::111122223333:role/AmazonEKSAutoClusterRole
export NODE_ROLE_ARN=arn:aws:iam::111122223333:role/AmazonEKSAutoNodeRole
export SUBNETS_JSON='["subnet-ExampleID1","subnet-ExampleID2","subnet-ExampleID3"]'
```

**Note**  
Set the `SUBNETS_JSON` variable with the subnet IDs from the previous step. You must wrap the value in single quotes to prevent the shell from interpreting the brackets and quotes as special characters.

#### Verify Variables (Optional)
<a name="_verify_variables_optional"></a>

Confirm your variables are set correctly:

```
echo "Region: ${AWS_REGION}"
echo "Cluster Name: ${CLUSTER_NAME}"
echo "K8s Version: ${K8S_VERSION}"
echo "Cluster Role ARN: ${CLUSTER_ROLE_ARN}"
echo "Node Role ARN: ${NODE_ROLE_ARN}"
echo "Subnets JSON: ${SUBNETS_JSON}"
```

#### Run the Command
<a name="_run_the_command"></a>

Use the following command to create the cluster:

```
aws eks create-cluster \
  --region ${AWS_REGION} \
  --cli-input-json \
  "{
      \"name\": \"${CLUSTER_NAME}\",
      \"version\": \"${K8S_VERSION}\",
      \"roleArn\": \"${CLUSTER_ROLE_ARN}\",
      \"resourcesVpcConfig\": {
        \"subnetIds\": ${SUBNETS_JSON},
        \"endpointPublicAccess\": true,
        \"endpointPrivateAccess\": true
      },
      \"computeConfig\": {
        \"enabled\": true,
        \"nodeRoleArn\":\"${NODE_ROLE_ARN}\",
        \"nodePools\": [\"general-purpose\", \"system\"]
      },
      \"kubernetesNetworkConfig\": {
        \"elasticLoadBalancing\": {
          \"enabled\": true
        }
      },
      \"storageConfig\": {
        \"blockStorage\": {
          \"enabled\": true
        }
      },
      \"accessConfig\": {
        \"authenticationMode\": \"API\"
      }
    }"
```

### Check Cluster Status
<a name="_check_cluster_status"></a>

#### Step 1: Verify Cluster Creation
<a name="_step_1_verify_cluster_creation"></a>

Run the following command to check the status of your cluster. Cluster creation typically takes about 15 minutes:

```
aws eks describe-cluster --name "${CLUSTER_NAME}" --output json
```

#### Step 2: Update kubeconfig
<a name="_step_2_update_kubeconfig"></a>

Once the cluster is ready, update your local kubeconfig file to enable `kubectl` to communicate with the cluster. This configuration uses the AWS CLI for authentication.

```
aws eks update-kubeconfig --name "${CLUSTER_NAME}"
```

#### Step 3: Verify Node Pools
<a name="_step_3_verify_node_pools"></a>

List the Node Pools in your cluster using the following command:

```
kubectl get nodepools
```

## Next Steps
<a name="_next_steps"></a>
+ Learn how to [deploy a sample workload](automode-workload.md) to your new EKS Auto Mode cluster.