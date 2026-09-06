

# Setting up your HyperPod clusters for model deployment
<a name="sagemaker-hyperpod-model-deployment-setup"></a>

This guide shows you how to enable inference capabilities on Amazon SageMaker HyperPod clusters. You'll set up the infrastructure, permissions, and operators that machine learning engineers need to deploy and manage inference endpoints.

**Note**  
To create a cluster with the inference operator pre-installed, see [Create an EKS-orchestrated SageMaker HyperPod cluster](sagemaker-hyperpod-quickstart.md#sagemaker-hyperpod-quickstart-eks). To install the inference operator on an existing cluster, continue with the following procedures.

You can install the inference operator using the SageMaker AI console for a streamlined experience, or use the AWS CLI for more control. This guide covers both installation methods.

## Method 1: Install HyperPod Inference Add-on through SageMaker AI console (Recommended)
<a name="sagemaker-hyperpod-model-deployment-setup-ui"></a>

The SageMaker AI console provides the most streamlined experience with two installation options:
+ **Quick Install:** Automatically creates all required resources with optimized defaults, including IAM roles, Amazon S3 buckets, and dependency add-ons. A new Studio domain will be created with required permissions to deploy a JumpStart model to the relevant cluster. This option is ideal for getting started quickly with minimal configuration decisions.
+ **Custom Install:** Provides flexibility to specify existing resources or customize configurations while maintaining the one-click experience. Customers can choose to reuse existing IAM roles, Amazon S3 buckets, or dependency add-ons based on their organizational requirements.

### Prerequisites
<a name="sagemaker-hyperpod-model-deployment-setup-ui-prereqs"></a>
+ An existing HyperPod cluster with Amazon EKS orchestration
+ IAM permissions for Amazon EKS cluster administration
+ kubectl configured for cluster access

### Installation steps
<a name="sagemaker-hyperpod-model-deployment-setup-ui-steps"></a>

1. Navigate to the SageMaker AI console and go to **HyperPod Clusters** → **Cluster Management**.

1. Select your cluster where you want to install the Inference Operator.

1. Navigate to the **Inference** tab. Select **Quick Install** for automated setup or **Custom Install** for configuration flexibility.

1. If choosing Custom Install, specify existing resources or customize settings as needed.

1. Choose **Install** to begin the automated installation process.

1. Verify the installation status through the console, or by running the following commands:

   ```
   kubectl get pods -n hyperpod-inference-system
   ```

   ```
   aws eks describe-addon --cluster-name CLUSTER-NAME --addon-name amazon-sagemaker-hyperpod-inference --region REGION
   ```

After the add-on is successfully installed, you can deploy models using the model deployment documentation or navigate to [Verify the inference operator is working](#sagemaker-hyperpod-model-deployment-setup-verify).

## Method 2: Installing the Inference Operator using the AWS CLI
<a name="sagemaker-hyperpod-model-deployment-setup-addon"></a>

The AWS CLI installation method provides more control over the installation process and is suitable for automation and advanced configurations.

### Prerequisites
<a name="sagemaker-hyperpod-model-deployment-setup-prereq-addon"></a>

The inference operator enables deployment and management of machine learning inference endpoints on your Amazon EKS cluster. Before installation, ensure your cluster has the required security configurations and supporting infrastructure. Complete these steps to configure IAM roles, install the AWS Load Balancer Controller, set up Amazon S3 and Amazon FSx CSI drivers, and deploy KEDA and cert-manager:

1. [Connect to your cluster and set up environment variables](#sagemaker-hyperpod-model-deployment-setup-connect-addon)

1. [Configure IAM roles for inference operator](#sagemaker-hyperpod-model-deployment-setup-prepare-addon)

1. [Create the ALB Controller role](#sagemaker-hyperpod-model-deployment-setup-alb-addon)

1. [Create the KEDA operator role](#sagemaker-hyperpod-model-deployment-setup-keda-addon)

1. [Install the dependency EKS Add-Ons](#sagemaker-hyperpod-model-deployment-setup-install-dependencies)

**Note**  
Alternatively, you can use CloudFormation templates to automate the prerequisite setup. For more information, see [Using CloudFormation templates to create the prerequisite stack](#sagemaker-hyperpod-model-deployment-setup-cfn).

### Connect to your cluster and set up environment variables
<a name="sagemaker-hyperpod-model-deployment-setup-connect-addon"></a>

Before proceeding, verify that your AWS credentials are properly configured and have the necessary permissions. Run the following steps using an IAM principal with Administrator privileges and Cluster Admin access to an Amazon EKS cluster. Ensure you've created a HyperPod cluster with [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md). Install helm, eksctl, and kubectl command line utilities.

For Kubernetes administrative access to the Amazon EKS cluster, open the Amazon EKS console and select your cluster. In the **Access** tab, select **IAM Access Entries**. If no entry exists for your IAM principal, select **Create Access Entry**. Select the desired IAM principal and associate the `AmazonEKSClusterAdminPolicy` with it.

1. Configure kubectl to connect to the newly created HyperPod cluster orchestrated by Amazon EKS cluster. Specify the Region and HyperPod cluster name.

   ```
   export HYPERPOD_CLUSTER_NAME=<hyperpod-cluster-name>
   export REGION=<region>
   
   # S3 bucket where tls certificates will be uploaded
   export BUCKET_NAME="hyperpod-tls-<your-bucket-suffix>" # Bucket should have prefix: hyperpod-tls-*
   
   export EKS_CLUSTER_NAME=$(aws --region $REGION sagemaker describe-cluster --cluster-name $HYPERPOD_CLUSTER_NAME \
   --query 'Orchestrator.Eks.ClusterArn' --output text | \
   cut -d'/' -f2)
   aws eks update-kubeconfig --name $EKS_CLUSTER_NAME --region $REGION
   ```
**Note**  
If using a custom bucket name that doesn't start with `hyperpod-tls-`, attach the following policy to your execution role:  

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "TLSBucketDeleteObjectsPermission",
               "Effect": "Allow",
               "Action": ["s3:DeleteObject"],
               "Resource": ["arn:aws:s3:::${BUCKET_NAME}/*"],
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceAccount": "${aws:PrincipalAccount}"
                   }
               }
           },
           {
               "Sid": "TLSBucketGetObjectAccess",
               "Effect": "Allow",
               "Action": ["s3:GetObject"],
               "Resource": ["arn:aws:s3:::${BUCKET_NAME}/*"]
           },
           {
               "Sid": "TLSBucketPutObjectAccess",
               "Effect": "Allow",
               "Action": ["s3:PutObject", "s3:PutObjectTagging"],
               "Resource": ["arn:aws:s3:::${BUCKET_NAME}/*"],
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceAccount": "${aws:PrincipalAccount}"
                   }
               }
           }
       ]
   }
   ```

1. Set default env variables.

   ```
   HYPERPOD_INFERENCE_ROLE_NAME="SageMakerHyperPodInference-$HYPERPOD_CLUSTER_NAME"
   HYPERPOD_INFERENCE_NAMESPACE="hyperpod-inference-system"
   ```

1. Extract the Amazon EKS cluster name from the cluster ARN, update the local kubeconfig, and verify connectivity by listing all pods across namespaces.

   ```
   kubectl get pods --all-namespaces
   ```

1. (Optional) Install the NVIDIA device plugin to enable GPU support on the cluster.

   ```
   # Install nvidia device plugin
   kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.14.5/nvidia-device-plugin.yml
   # Verify that GPUs are visible to k8s
   kubectl get nodes -o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia.com/gpu
   ```

### Configure IAM roles for inference operator
<a name="sagemaker-hyperpod-model-deployment-setup-prepare-addon"></a>

1. Gather essential AWS resource identifiers and ARNs required for configuring service integrations between Amazon EKS, SageMaker AI, and IAM components.

   ```
   %%bash -x
   
   export ACCOUNT_ID=$(aws --region $REGION sts get-caller-identity --query 'Account' --output text)
   export OIDC_ID=$(aws --region $REGION eks describe-cluster --name $EKS_CLUSTER_NAME --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5)
   export EKS_CLUSTER_ROLE=$(aws eks --region $REGION describe-cluster --name $EKS_CLUSTER_NAME --query 'cluster.roleArn' --output text)
   ```

1. Associate an IAM OIDCidentity provider with your EKS cluster.

   ```
   eksctl utils associate-iam-oidc-provider --region=$REGION --cluster=$EKS_CLUSTER_NAME --approve
   ```

1. Create the trust policy required for the HyperPod inference operator IAM role. These policies enable secure cross-service communication between Amazon EKS, SageMaker AI, and other AWS services.

   ```
   %%bash -x
   
   # Create trust policy JSON
   cat << EOF > trust-policy.json
   {
   "Version": "2012-10-17",		 	 	 
   "Statement": [
       {
           "Effect": "Allow",
           "Principal": {
               "Service": [
                   "sagemaker.amazonaws.com"
               ]
           },
           "Action": "sts:AssumeRole"
       },
       {
           "Effect": "Allow",
           "Principal": {
               "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}"
           },
           "Action": "sts:AssumeRoleWithWebIdentity",
           "Condition": {
               "StringLike": {
                   "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com",
                   "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:hyperpod-inference-system:hyperpod-inference-controller-manager"
               }
           }
       }
   ]
   }
   EOF
   ```

1. Create execution Role for the inference operator.

   ```
   aws iam create-role --role-name $HYPERPOD_INFERENCE_ROLE_NAME --assume-role-policy-document file://trust-policy.json
   aws iam attach-role-policy --role-name $HYPERPOD_INFERENCE_ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceAccess
   ```

1. Create a namespace for inference operator resources

   ```
   kubectl create namespace $HYPERPOD_INFERENCE_NAMESPACE
   ```

### Create the ALB Controller role
<a name="sagemaker-hyperpod-model-deployment-setup-alb-addon"></a>

1. Create the trust policy and permissions policy.

   ```
   # Create trust policy
   cat <<EOF > /tmp/alb-trust-policy.json
   {
   "Version": "2012-10-17",		 	 	 
   "Statement": [
       {
           "Effect": "Allow",
           "Principal": {
               "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}"
           },
           "Action": "sts:AssumeRoleWithWebIdentity",
           "Condition": {
               "StringLike": {
                   "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:hyperpod-inference-system:aws-load-balancer-controller",
                   "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com"
               }
           }
       }
   ]
   }
   EOF
   
   # Create permissions policy
   export ALBController_IAM_POLICY_NAME=HyperPodInferenceALBControllerIAMPolicy
   curl -o AWSLoadBalancerControllerIAMPolicy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.13.0/docs/install/iam_policy.json
   
   # Create the role
   aws iam create-role \
       --role-name alb-role \
       --assume-role-policy-document file:///tmp/alb-trust-policy.json 
   
   # Create the policy
   ALB_POLICY_ARN=$(aws iam create-policy \
       --policy-name $ALBController_IAM_POLICY_NAME \
       --policy-document file://AWSLoadBalancerControllerIAMPolicy.json \
       --query 'Policy.Arn' \
       --output text)
   
   # Attach the policy to the role
   aws iam attach-role-policy \
       --role-name alb-role \
       --policy-arn $ALB_POLICY_ARN
   ```

1. Apply Tags (`kubernetes.io.role/elb`) to all subnets in the Amazon EKS cluster (both public and private).

   ```
   export VPC_ID=$(aws --region $REGION eks describe-cluster --name $EKS_CLUSTER_NAME --query 'cluster.resourcesVpcConfig.vpcId' --output text)
   
   # Add Tags
   aws ec2 describe-subnets \
   --filters "Name=vpc-id,Values=${VPC_ID}" "Name=map-public-ip-on-launch,Values=true" \
   --query 'Subnets[*].SubnetId' --output text | \
   tr '\t' '\n' | \
   xargs -I{} aws ec2 create-tags --resources {} --tags Key=kubernetes.io/role/elb,Value=1
   
   # Verify Tags are added
   aws ec2 describe-subnets \
   --filters "Name=vpc-id,Values=${VPC_ID}" "Name=map-public-ip-on-launch,Values=true" \
   --query 'Subnets[*].SubnetId' --output text | \
   tr '\t' '\n' |
   xargs -n1 -I{} aws ec2 describe-tags --filters "Name=resource-id,Values={}" "Name=key,Values=kubernetes.io/role/elb" --query "Tags[0].Value" --output text
   ```

1. Create an Amazon S3 VPC endpoint.

   ```
   aws ec2 create-vpc-endpoint \
       --region ${REGION} \
       --vpc-id ${VPC_ID} \
       --vpc-endpoint-type Gateway \
       --service-name "com.amazonaws.${REGION}.s3" \
       --route-table-ids $(aws ec2 describe-route-tables --region $REGION --filters "Name=vpc-id,Values=${VPC_ID}" --query 'RouteTables[].Associations[].RouteTableId' --output text | tr ' ' '\n' | sort -u | tr '\n' ' ')
   ```

### Create the KEDA operator role
<a name="sagemaker-hyperpod-model-deployment-setup-keda-addon"></a>

1. Create the trust policy and permissions policy.

   ```
   # Create trust policy
   cat <<EOF > /tmp/keda-trust-policy.json
   {
   "Version": "2012-10-17",		 	 	 
   "Statement": [
       {
           "Effect": "Allow",
           "Principal": {
               "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}"
           },
           "Action": "sts:AssumeRoleWithWebIdentity",
           "Condition": {
               "StringLike": {
                   "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:hyperpod-inference-system:keda-operator",
                   "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com"
               }
           }
       }
   ]
   }
   EOF
   
   # Create permissions policy
   cat <<EOF > /tmp/keda-policy.json
   {
   "Version": "2012-10-17",		 	 	 
   "Statement": [
       {
           "Effect": "Allow",
           "Action": [
               "cloudwatch:GetMetricData",
               "cloudwatch:GetMetricStatistics",
               "cloudwatch:ListMetrics"
           ],
           "Resource": "*"
       },
       {
           "Effect": "Allow",
           "Action": [
               "aps:QueryMetrics",
               "aps:GetLabels",
               "aps:GetSeries",
               "aps:GetMetricMetadata"
           ],
           "Resource": "*"
       }
   ]
   }
   EOF
   
   # Create the role
   aws iam create-role \
       --role-name keda-operator-role \
       --assume-role-policy-document file:///tmp/keda-trust-policy.json
   
   # Create the policy
   KEDA_POLICY_ARN=$(aws iam create-policy \
       --policy-name KedaOperatorPolicy \
       --policy-document file:///tmp/keda-policy.json \
       --query 'Policy.Arn' \
       --output text)
   
   # Attach the policy to the role
   aws iam attach-role-policy \
       --role-name keda-operator-role \
       --policy-arn $KEDA_POLICY_ARN
   ```

1. If you're using gated models, create an IAM role to access the gated models.

   1. Create an IAM policy.

      ```
      %%bash -s $REGION
      
      JUMPSTART_GATED_ROLE_NAME="JumpstartGatedRole-${REGION}-${HYPERPOD_CLUSTER_NAME}"
      
      cat <<EOF > /tmp/trust-policy.json
      {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
                  "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}"
              },
              "Action": "sts:AssumeRoleWithWebIdentity",
              "Condition": {
                  "StringLike": {
                      "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:*:hyperpod-inference-service-account*",
                      "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com"
                  }
              }
          },
              {
              "Effect": "Allow",
              "Principal": {
                  "Service": "sagemaker.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
          }
      ]
      }
      EOF
      ```

   1. Create an IAM role.

      ```
      # Create the role using existing trust policy
      aws iam create-role \
      --role-name $JUMPSTART_GATED_ROLE_NAME \
      --assume-role-policy-document file:///tmp/trust-policy.json
      
      aws iam attach-role-policy \
      --role-name $JUMPSTART_GATED_ROLE_NAME \
      --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodGatedModelAccess
      ```

      ```
      JUMPSTART_GATED_ROLE_ARN_LIST= !aws iam get-role --role-name=$JUMPSTART_GATED_ROLE_NAME --query "Role.Arn" --output text
      JUMPSTART_GATED_ROLE_ARN = JUMPSTART_GATED_ROLE_ARN_LIST[0]
      !echo $JUMPSTART_GATED_ROLE_ARN
      ```

### Install the dependency EKS Add-Ons
<a name="sagemaker-hyperpod-model-deployment-setup-install-dependencies"></a>

Before installing the inference operator, you must install the following required EKS add-ons on your cluster. The inference operator will fail to install if any of these dependencies are missing. Each add-on has a minimum version requirement for compatibility with the Inference add-on.

**Important**  
Install all dependency add-ons before attempting to install the inference operator. Missing dependencies will cause installation failures with specific error messages.

#### Required Add-ons
<a name="sagemaker-hyperpod-model-deployment-setup-required-addons"></a>

1. **Amazon S3 Mountpoint CSI Driver** (minimum version: v1.14.1-eksbuild.1)

   Required for mounting S3 buckets as persistent volumes in inference workloads.

   ```
   aws eks create-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name aws-mountpoint-s3-csi-driver \
       --region $REGION \
       --service-account-role-arn <S3_CSI_ROLE_ARN>
   ```

   For detailed installation instructions including required IAM permissions, see [Mountpoint for Amazon S3 CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/workloads-add-ons-available-eks.html#mountpoint-for-s3-add-on).

1. **Amazon FSx CSI Driver** (minimum version: v1.6.0-eksbuild.1)

   Required for mounting FSx file systems for high-performance model storage.

   ```
   aws eks create-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name aws-fsx-csi-driver \
       --region $REGION \
       --service-account-role-arn $FSX_CSI_ROLE_ARN
   ```

   For detailed installation instructions including required IAM permissions, see [Amazon FSx for Lustre CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/workloads-add-ons-available-eks.html#add-ons-aws-fsx-csi-driver).

1. **Metrics Server** (minimum version: v0.7.2-eksbuild.4)

   Required for autoscaling functionality and resource metrics collection.

   ```
   aws eks create-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name metrics-server \
       --region $REGION
   ```

   For detailed installation instructions, see [Metrics Server](https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html).

1. **Cert Manager** (minimum version: v1.18.2-eksbuild.2)

   Required for TLS certificate management for secure inference endpoints.

   ```
   aws eks create-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name cert-manager \
       --region $REGION
   ```

   For detailed installation instructions, see [cert-manager](https://docs.aws.amazon.com/eks/latest/userguide/community-addons.html#addon-cert-manager).

#### Verify Add-on Installation
<a name="sagemaker-hyperpod-model-deployment-setup-verify-dependencies"></a>

After installing the required add-ons, verify they are running correctly:

```
# Check add-on status
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name aws-mountpoint-s3-csi-driver --region $REGION
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name aws-fsx-csi-driver --region $REGION
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name metrics-server --region $REGION
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name cert-manager --region $REGION

# Verify pods are running
kubectl get pods -n kube-system | grep -E "(mountpoint|fsx|metrics-server)"
kubectl get pods -n cert-manager
```

All add-ons should show status "ACTIVE" and all pods should be in "Running" state before proceeding with inference operator installation.

**Note**  
If you created your HyperPod cluster using the quick setup or custom setup options, the FSx CSI Driver and Cert Manager may already be installed. Verify their presence using the preceding commands.

### Installing the Inference Operator with EKS add-on
<a name="sagemaker-hyperpod-model-deployment-setup-install-inference-operator-addon"></a>

The EKS add-on installation method provides a managed experience with automatic updates and integrated dependency validation. This is the recommended approach for installing the inference operator.

**Install the inference operator add-on**

1. Prepare the add-on configuration by gathering all required ARNs and creating the configuration file:

   ```
   # Gather required ARNs
   export EXECUTION_ROLE_ARN=$(aws iam get-role --role-name $HYPERPOD_INFERENCE_ROLE_NAME --query "Role.Arn" --output text)
   export HYPERPOD_CLUSTER_ARN=$(aws sagemaker describe-cluster --cluster-name $HYPERPOD_CLUSTER_NAME --region $REGION --query "ClusterArn" --output text)
   export KEDA_ROLE_ARN=$(aws iam get-role --role-name keda-operator-role --query 'Role.Arn' --output text)
   export ALB_ROLE_ARN=$(aws iam get-role --role-name alb-role --query 'Role.Arn' --output text)
   
   # Verify all ARNs are set correctly
   echo "Execution Role ARN: $EXECUTION_ROLE_ARN"
   echo "HyperPod Cluster ARN: $HYPERPOD_CLUSTER_ARN"
   echo "KEDA Role ARN: $KEDA_ROLE_ARN"
   echo "ALB Role ARN: $ALB_ROLE_ARN"
   echo "TLS S3 Bucket: $BUCKET_NAME"
   ```

1. Create the add-on configuration file with all required settings:

   ```
   cat > addon-config.json << EOF
   {
     "executionRoleArn": "$EXECUTION_ROLE_ARN",
     "tlsCertificateS3Bucket": "$BUCKET_NAME",
     "hyperpodClusterArn": "$HYPERPOD_CLUSTER_ARN",
     "jumpstartGatedModelDownloadRoleArn": "$JUMPSTART_GATED_ROLE_ARN",
     "alb": {
       "serviceAccount": {
         "create": true,
         "roleArn": "$ALB_ROLE_ARN"
       }
     },
     "keda": {
       "auth": {
         "aws": {
           "irsa": {
             "roleArn": "$KEDA_ROLE_ARN"
           }
         }
       }
     }
   }
   EOF
   
   # Verify the configuration file
   cat addon-config.json
   ```

1. Install the inference operator add-on (minimum version: v1.0.0-eksbuild.1):

   ```
   aws eks create-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --configuration-values file://addon-config.json \
       --region $REGION
   ```

1. Monitor the installation progress and verify successful completion:

   ```
   # Check installation status (repeat until status shows "ACTIVE")
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --region $REGION \
       --query "addon.{Status:status,Health:health}" \
       --output table
   
   # Verify pods are running
   kubectl get pods -n hyperpod-inference-system
   
   # Check operator logs for any issues
   kubectl logs -n hyperpod-inference-system deployment/hyperpod-inference-controller-manager --tail=50
   ```

For detailed troubleshooting of installation issues, see [HyperPod inference troubleshooting](sagemaker-hyperpod-model-deployment-ts.md).

To verify the inference operator is working correctly, continue to [Verify the inference operator is working](#sagemaker-hyperpod-model-deployment-setup-verify).

### Using CloudFormation templates to create the prerequisite stack
<a name="sagemaker-hyperpod-model-deployment-setup-cfn"></a>

As an alternative to manually configuring the prerequisites, you can use CloudFormation templates to automate the creation of required IAM roles and policies for the inference operator.

1. Set up input variables. Replace the placeholder values with your own:

   ```
   #!/bin/bash
   set -e
   
   # ===== INPUT VARIABLES =====
   HP_CLUSTER_NAME="my-hyperpod-cluster"  # Replace with your HyperPod cluster name
   REGION="us-east-1"  # Replace with your AWS region
   PREFIX="my-prefix"  # Replace with your resource prefix
   SHORT_PREFIX="12a34d56"  # Replace with your short prefix (maximum 8 characters)
   CREATE_DOMAIN="true"  # Set to "false" if you don't need a SageMaker Studio domain
   STACK_NAME="hyperpod-inference-prerequisites"  # Replace with your stack name
   TEMPLATE_URL="https://aws-sagemaker-hyperpod-cluster-setup-${REGION}-prod.s3.${REGION}.amazonaws.com/templates/main-stack-inference-operator-addon-template.yaml"
   ```

1. Derive cluster and network information:

   ```
   # ===== DERIVE EKS CLUSTER NAME =====
   EKS_CLUSTER_NAME=$(aws sagemaker describe-cluster --cluster-name $HP_CLUSTER_NAME --region $REGION --query 'Orchestrator.Eks.ClusterArn' --output text | awk -F'/' '{print $NF}')
   echo "EKS_CLUSTER_NAME=$EKS_CLUSTER_NAME"
   
   # ===== GET VPC AND OIDC =====
   VPC_ID=$(aws eks describe-cluster --name $EKS_CLUSTER_NAME --region $REGION --query 'cluster.resourcesVpcConfig.vpcId' --output text)
   echo "VPC_ID=$VPC_ID"
   
   OIDC_PROVIDER=$(aws eks describe-cluster --name $EKS_CLUSTER_NAME --region $REGION --query 'cluster.identity.oidc.issuer' --output text | sed 's|https://||')
   echo "OIDC_PROVIDER=$OIDC_PROVIDER"
   
   # ===== GET PRIVATE ROUTE TABLES =====
   ALL_ROUTE_TABLES=$(aws ec2 describe-route-tables --region $REGION --filters "Name=vpc-id,Values=$VPC_ID" --query 'RouteTables[].RouteTableId' --output text)
   EKS_PRIVATE_ROUTE_TABLES=""
   for rtb in $ALL_ROUTE_TABLES; do
       HAS_IGW=$(aws ec2 describe-route-tables --region $REGION --route-table-ids $rtb --query 'RouteTables[0].Routes[?GatewayId && starts_with(GatewayId, `igw-`)]' --output text 2>/dev/null)
       if [ -z "$HAS_IGW" ]; then
           EKS_PRIVATE_ROUTE_TABLES="${EKS_PRIVATE_ROUTE_TABLES:+$EKS_PRIVATE_ROUTE_TABLES,}$rtb"
       fi
   done
   echo "EKS_PRIVATE_ROUTE_TABLES=$EKS_PRIVATE_ROUTE_TABLES"
   
   # ===== CHECK S3 VPC ENDPOINT =====
   S3_ENDPOINT_EXISTS=$(aws ec2 describe-vpc-endpoints --region $REGION --filters "Name=vpc-id,Values=$VPC_ID" "Name=service-name,Values=com.amazonaws.$REGION.s3" --query 'VpcEndpoints[0].VpcEndpointId' --output text)
   CREATE_S3_ENDPOINT_STACK=$([ "$S3_ENDPOINT_EXISTS" == "None" ] && echo "true" || echo "false")
   echo "CREATE_S3_ENDPOINT_STACK=$CREATE_S3_ENDPOINT_STACK"
   
   # ===== GET HYPERPOD DETAILS =====
   HYPERPOD_CLUSTER_ARN=$(aws sagemaker describe-cluster --cluster-name $HP_CLUSTER_NAME --region $REGION --query 'ClusterArn' --output text)
   echo "HYPERPOD_CLUSTER_ARN=$HYPERPOD_CLUSTER_ARN"
   
   # ===== GET DEFAULT VPC FOR DOMAIN =====
   DOMAIN_VPC_ID=$(aws ec2 describe-vpcs --region $REGION --filters "Name=isDefault,Values=true" --query 'Vpcs[0].VpcId' --output text)
   echo "DOMAIN_VPC_ID=$DOMAIN_VPC_ID"
   
   DOMAIN_SUBNET_IDS=$(aws ec2 describe-subnets --region $REGION --filters "Name=vpc-id,Values=$DOMAIN_VPC_ID" --query 'Subnets[0].SubnetId' --output text)
   echo "DOMAIN_SUBNET_IDS=$DOMAIN_SUBNET_IDS"
   
   # ===== GET INSTANCE GROUPS =====
   INSTANCE_GROUPS=$(aws sagemaker describe-cluster --cluster-name $HP_CLUSTER_NAME --region $REGION --query 'InstanceGroups[].InstanceGroupName' --output json | python3 -c "import sys, json; groups = json.load(sys.stdin); print('[' + ','.join([f'\\\\\\\"' + g + '\\\\\\\"' for g in groups]) + ']')")
   echo "INSTANCE_GROUPS=$INSTANCE_GROUPS"
   ```

1. Create parameters file and deploy stack:

   ```
   # ===== CREATE PARAMETERS JSON =====
   cat > /tmp/cfn-params.json << EOF
   [
     {"ParameterKey":"ResourceNamePrefix","ParameterValue":"$PREFIX"},
     {"ParameterKey":"ResourceNameShortPrefix","ParameterValue":"$SHORT_PREFIX"},
     {"ParameterKey":"VpcId","ParameterValue":"$VPC_ID"},
     {"ParameterKey":"EksPrivateRouteTableIds","ParameterValue":"$EKS_PRIVATE_ROUTE_TABLES"},
     {"ParameterKey":"EKSClusterName","ParameterValue":"$EKS_CLUSTER_NAME"},
     {"ParameterKey":"OIDCProviderURLWithoutProtocol","ParameterValue":"$OIDC_PROVIDER"},
     {"ParameterKey":"HyperPodClusterArn","ParameterValue":"$HYPERPOD_CLUSTER_ARN"},
     {"ParameterKey":"HyperPodClusterName","ParameterValue":"$HP_CLUSTER_NAME"},
     {"ParameterKey":"CreateDomain","ParameterValue":"$CREATE_DOMAIN"},
     {"ParameterKey":"DomainVpcId","ParameterValue":"$DOMAIN_VPC_ID"},
     {"ParameterKey":"DomainSubnetIds","ParameterValue":"$DOMAIN_SUBNET_IDS"},
     {"ParameterKey":"CreateS3EndpointStack","ParameterValue":"$CREATE_S3_ENDPOINT_STACK"},
     {"ParameterKey":"TieredStorageConfig","ParameterValue":"{\"Mode\":\"Enable\",\"InstanceMemoryAllocationPercentage\":20}"},
     {"ParameterKey":"TieredKVCacheConfig","ParameterValue":"{\"KVCacheMode\":\"Enable\",\"InstanceGroup\":$INSTANCE_GROUPS,\"NVMeMode\":\"Enable\"}"}
   ]
   EOF
   
   echo -e "\n===== CREATING CLOUDFORMATION STACK ====="
   aws cloudformation create-stack \
       --region $REGION \
       --stack-name $STACK_NAME \
       --template-url $TEMPLATE_URL \
       --parameters file:///tmp/cfn-params.json \
       --capabilities CAPABILITY_NAMED_IAM
   ```

1. Monitor the stack creation status:

   ```
   aws cloudformation describe-stacks \
       --stack-name $STACK_NAME \
       --region $REGION \
       --query 'Stacks[0].StackStatus'
   ```

1. Once the stack is created successfully, retrieve the output values for use in the inference operator installation:

   ```
   aws cloudformation describe-stacks \
       --stack-name $STACK_NAME \
       --region $REGION \
       --query 'Stacks[0].Outputs'
   ```

After the CloudFormation stack is created, continue with [Installing the Inference Operator with EKS add-on](#sagemaker-hyperpod-model-deployment-setup-install-inference-operator-addon) to install the inference operator.

## Method 3: Helm chart installation
<a name="sagemaker-hyperpod-model-deployment-setup-helm"></a>

**Note**  
For the simplest installation experience, we recommend using [Method 1: Install HyperPod Inference Add-on through SageMaker AI console (Recommended)](#sagemaker-hyperpod-model-deployment-setup-ui) or [Method 2: Installing the Inference Operator using the AWS CLI](#sagemaker-hyperpod-model-deployment-setup-addon). Helm chart installation may be deprecated in a future release.

### Prerequisites
<a name="sagemaker-hyperpod-model-deployment-setup-prereq"></a>

Before proceeding, verify that your AWS credentials are properly configured and have the necessary permissions. The following steps need to be run by an IAM principal with Administrator privileges and Cluster Admin access to an Amazon EKS cluster. Verify that you've created a HyperPod cluster with [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md) . Verify you have installed helm, eksctl, and kubectl command line utilities. 

For Kubernetes administrative access to the Amazon EKS cluster, go to the Amazon EKS console and select the cluster you are using. Look in the **Access** tab and select IAM Access Entries. If there isn't an entry for your IAM principal, select **Create Access Entry**. Then select the desired IAM principal and associate the `AmazonEKSClusterAdminPolicy` with it.

1. Configure kubectl to connect to the newly created HyperPod cluster orchestrated by Amazon EKS cluster. Specify the Region and HyperPod cluster name.

   ```
   export HYPERPOD_CLUSTER_NAME=<hyperpod-cluster-name>
   export REGION=<region>
   
   # S3 bucket where tls certificates will be uploaded
   BUCKET_NAME="<Enter name of your s3 bucket>" # This should be bucket name, not URI
   
   export EKS_CLUSTER_NAME=$(aws --region $REGION sagemaker describe-cluster --cluster-name $HYPERPOD_CLUSTER_NAME \
   --query 'Orchestrator.Eks.ClusterArn' --output text | \
   cut -d'/' -f2)
   aws eks update-kubeconfig --name $EKS_CLUSTER_NAME --region $REGION
   ```

1. Set default env variables.

   ```
   LB_CONTROLLER_POLICY_NAME="AWSLoadBalancerControllerIAMPolicy-$HYPERPOD_CLUSTER_NAME"
   LB_CONTROLLER_ROLE_NAME="aws-load-balancer-controller-$HYPERPOD_CLUSTER_NAME"
   S3_MOUNT_ACCESS_POLICY_NAME="S3MountpointAccessPolicy-$HYPERPOD_CLUSTER_NAME"
   S3_CSI_ROLE_NAME="SM_HP_S3_CSI_ROLE-$HYPERPOD_CLUSTER_NAME"
   KEDA_OPERATOR_POLICY_NAME="KedaOperatorPolicy-$HYPERPOD_CLUSTER_NAME"
   KEDA_OPERATOR_ROLE_NAME="keda-operator-role-$HYPERPOD_CLUSTER_NAME"
   HYPERPOD_INFERENCE_ROLE_NAME="HyperpodInferenceRole-$HYPERPOD_CLUSTER_NAME"
   HYPERPOD_INFERENCE_SA_NAME="hyperpod-inference-operator-controller"
   HYPERPOD_INFERENCE_SA_NAMESPACE="hyperpod-inference-system"
   JUMPSTART_GATED_ROLE_NAME="JumpstartGatedRole-$HYPERPOD_CLUSTER_NAME"
   FSX_CSI_ROLE_NAME="AmazonEKSFSxLustreCSIDriverFullAccess-$HYPERPOD_CLUSTER_NAME"
   ```

1. Extract the Amazon EKS cluster name from the cluster ARN, update the local kubeconfig, and verify connectivity by listing all pods across namespaces.

   ```
   kubectl get pods --all-namespaces
   ```

1. (Optional) Install the NVIDIA device plugin to enable GPU support on the cluster.

   ```
   #Install nvidia device plugin
   kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.14.5/nvidia-device-plugin.yml
   # Verify that GPUs are visible to k8s
   kubectl get nodes -o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia.com/gpu
   ```

### Prepare your environment for inference operator installation
<a name="sagemaker-hyperpod-model-deployment-setup-prepare"></a>

1. Gather essential AWS resource identifiers and ARNs required for configuring service integrations between Amazon EKS, SageMaker AI, and IAM components.

   ```
   %%bash -x
   
   export ACCOUNT_ID=$(aws --region $REGION sts get-caller-identity --query 'Account' --output text)
   export OIDC_ID=$(aws --region $REGION eks describe-cluster --name $EKS_CLUSTER_NAME --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5)
   export EKS_CLUSTER_ROLE=$(aws eks --region $REGION describe-cluster --name $EKS_CLUSTER_NAME --query 'cluster.roleArn' --output text)
   ```

1. Associate an IAM OIDCidentity provider with your EKS cluster.

   ```
   eksctl utils associate-iam-oidc-provider --region=$REGION --cluster=$EKS_CLUSTER_NAME --approve
   ```

1. Create the trust policy required for the HyperPod inference operator IAM role. This policy enables secure cross-service communication between Amazon EKS, SageMaker AI, and other AWS services.

   ```
   %%bash -x
   
   # Create trust policy JSON
   cat << EOF > trust-policy.json
   {
   "Version": "2012-10-17",		 	 	 
   "Statement": [
   {
       "Effect": "Allow",
       "Principal": {
           "Service": [
               "sagemaker.amazonaws.com"
           ]
       },
       "Action": "sts:AssumeRole"
   },
   {
       "Effect": "Allow",
       "Principal": {
           "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}"
       },
       "Action": "sts:AssumeRoleWithWebIdentity",
       "Condition": {
           "StringLike": {
               "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com",
               "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:hyperpod-inference-system:hyperpod-inference-controller-manager"
           }
       }
   }
   ]
   }
   EOF
   ```

1. Create execution Role for the inference operator and attach the managed policy.

   ```
   aws iam create-role --role-name $HYPERPOD_INFERENCE_ROLE_NAME --assume-role-policy-document file://trust-policy.json
   aws iam attach-role-policy --role-name $HYPERPOD_INFERENCE_ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceAccess
   ```

1. Download and create the IAM policy required for the AWS Load Balancer Controller to manage Application Load Balancers and Network Load Balancers in your EKS cluster.

   ```
   %%bash -x 
   
   export ALBController_IAM_POLICY_NAME=HyperPodInferenceALBControllerIAMPolicy
   
   curl -o AWSLoadBalancerControllerIAMPolicy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.13.0/docs/install/iam_policy.json
   aws iam create-policy --policy-name $ALBController_IAM_POLICY_NAME --policy-document file://AWSLoadBalancerControllerIAMPolicy.json
   ```

1. Create an IAM service account that links the Kubernetes service account with the IAM policy, enabling the AWS Load Balancer Controller to assume the necessary AWS permissions through IRSA (IAM Roles for Service Accounts).

   ```
   %%bash -x 
   
   export ALB_POLICY_ARN="arn:aws:iam::$ACCOUNT_ID:policy/$ALBController_IAM_POLICY_NAME"
   
   # Create IAM service account with gathered values
   eksctl create iamserviceaccount \
   --approve \
   --override-existing-serviceaccounts \
   --name=aws-load-balancer-controller \
   --namespace=kube-system \
   --cluster=$EKS_CLUSTER_NAME \
   --attach-policy-arn=$ALB_POLICY_ARN \
   --region=$REGION
   
   # Print the values for verification
   echo "Cluster Name: $EKS_CLUSTER_NAME"
   echo "Region: $REGION"
   echo "Policy ARN: $ALB_POLICY_ARN"
   ```

1. Apply Tags (`kubernetes.io.role/elb`) to all subnets in the Amazon EKS cluster (both public and private).

   ```
   export VPC_ID=$(aws --region $REGION eks describe-cluster --name $EKS_CLUSTER_NAME --query 'cluster.resourcesVpcConfig.vpcId' --output text)
   
   # Add Tags
   aws ec2 describe-subnets \
   --filters "Name=vpc-id,Values=${VPC_ID}" "Name=map-public-ip-on-launch,Values=true" \
   --query 'Subnets[*].SubnetId' --output text | \
   tr '\t' '\n' | \
   xargs -I{} aws ec2 create-tags --resources {} --tags Key=kubernetes.io/role/elb,Value=1
   
   # Verify Tags are added
   aws ec2 describe-subnets \
   --filters "Name=vpc-id,Values=${VPC_ID}" "Name=map-public-ip-on-launch,Values=true" \
   --query 'Subnets[*].SubnetId' --output text | \
   tr '\t' '\n' |
   xargs -n1 -I{} aws ec2 describe-tags --filters "Name=resource-id,Values={}" "Name=key,Values=kubernetes.io/role/elb" --query "Tags[0].Value" --output text
   ```

1. Create a Namespace for KEDA and the Cert Manager.

   ```
   kubectl create namespace keda
   kubectl create namespace cert-manager
   ```

1. Create an Amazon S3 VPC endpoint.

   ```
   aws ec2 create-vpc-endpoint \
   --vpc-id ${VPC_ID} \
   --vpc-endpoint-type Gateway \
   --service-name "com.amazonaws.${REGION}.s3" \
   --route-table-ids $(aws ec2 describe-route-tables --filters "Name=vpc-id,Values=${VPC_ID}" --query 'RouteTables[].Associations[].RouteTableId' --output text | tr ' ' '\n' | sort -u | tr '\n' ' ')
   ```

1. Configure S3 storage access:

   1. Create an IAM policy that grants the necessary S3 permissions for using Mountpoint for Amazon S3, which enables file system access to S3 buckets from within the cluster.

      ```
      %%bash -x
      
      export S3_CSI_BUCKET_NAME=“<bucketname_for_mounting_through_filesystem>”
      
      cat <<EOF> s3accesspolicy.json
      {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          
          {
              "Sid": "MountpointAccess",
              "Effect": "Allow",
              "Action": [
                  "s3:ListBucket",
                  "s3:GetObject",
                  "s3:PutObject",
                  "s3:AbortMultipartUpload",
                  "s3:DeleteObject"
              ],
              "Resource": [
                      "arn:aws:s3:::${S3_CSI_BUCKET_NAME}",
                      "arn:aws:s3:::${S3_CSI_BUCKET_NAME}/*"
              ]
          }
      ]
      }
      EOF
      
      aws iam create-policy \
      --policy-name S3MountpointAccessPolicy \
      --policy-document file://s3accesspolicy.json
      
      cat <<EOF> s3accesstrustpolicy.json
      {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
                  "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}"
              },
              "Action": "sts:AssumeRoleWithWebIdentity",
              "Condition": {
                  "StringEquals": {
                      "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com",
                      "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:kube-system:${s3-csi-driver-sa}"
                  }
              }
          }
      ]
      }
      EOF
      
      aws iam create-role --role-name $S3_CSI_ROLE_NAME --assume-role-policy-document file://s3accesstrustpolicy.json
      
      aws iam attach-role-policy --role-name $S3_CSI_ROLE_NAME --policy-arn "arn:aws:iam::$ACCOUNT_ID:policy/S3MountpointAccessPolicy"
      ```

   1. (Optional) Create an IAM service account for the Amazon S3 CSI driver. The Amazon S3 CSI driver requires an IAM service account with appropriate permissions to mount S3 buckets as persistent volumes in your Amazon EKS cluster. This step creates the necessary IAM role and Kubernetes service account with the required S3 access policy.

      ```
      %%bash -x 
      
      export S3_CSI_ROLE_NAME="SM_HP_S3_CSI_ROLE-$REGION"
      export S3_CSI_POLICY_ARN=$(aws iam list-policies --query 'Policies[?PolicyName==`S3MountpointAccessPolicy`]' | jq '.[0].Arn' |  tr -d '"')
      
      eksctl create iamserviceaccount \
      --name s3-csi-driver-sa \
      --namespace kube-system \
      --cluster $EKS_CLUSTER_NAME \
      --attach-policy-arn $S3_CSI_POLICY_ARN \
      --approve \
      --role-name $S3_CSI_ROLE_NAME \
      --region $REGION 
      
      kubectl label serviceaccount s3-csi-driver-sa app.kubernetes.io/component=csi-driver app.kubernetes.io/instance=aws-mountpoint-s3-csi-driver app.kubernetes.io/managed-by=EKS app.kubernetes.io/name=aws-mountpoint-s3-csi-driver -n kube-system --overwrite
      ```

   1. (Optional) Install the Amazon S3 CSI driver add-on. This driver enables your pods to mount S3 buckets as persistent volumes, providing direct access to S3 storage from within your Kubernetes workloads.

      ```
      %%bash -x
      
      export S3_CSI_ROLE_ARN=$(aws iam get-role --role-name $S3_CSI_ROLE_NAME  --query 'Role.Arn' --output text)
      eksctl create addon --name aws-mountpoint-s3-csi-driver --cluster $EKS_CLUSTER_NAME --service-account-role-arn $S3_CSI_ROLE_ARN --force
      ```

   1. (Optional) Create a Persistent Volume Claim (PVC) for S3 storage. This PVC enables your pods to request and use S3 storage as if it were a traditional file system.

      ```
      %%bash -x 
      
      cat <<EOF> pvc_s3.yaml
      apiVersion: v1
      kind: PersistentVolumeClaim
      metadata:
      name: s3-claim
      spec:
      accessModes:
      - ReadWriteMany # supported options: ReadWriteMany / ReadOnlyMany
      storageClassName: "" # required for static provisioning
      resources:
      requests:
          storage: 1200Gi # ignored, required
      volumeName: s3-pv
      EOF
      
      kubectl apply -f pvc_s3.yaml
      ```

1. (Optional) Configure FSx storage access. Create an IAM service account for the Amazon FSx CSI driver. This service account will be used by the FSx CSI driver to interact with the Amazon FSx service on behalf of your cluster.

   ```
   %%bash -x 
   
   
   eksctl create iamserviceaccount \
   --name fsx-csi-controller-sa \
   --namespace kube-system \
   --cluster $EKS_CLUSTER_NAME \
   --attach-policy-arn arn:aws:iam::aws:policy/AmazonFSxFullAccess \
   --approve \
   --role-name FSXLCSI-${EKS_CLUSTER_NAME}-${REGION} \
   --region $REGION
   ```

### Create the KEDA operator role
<a name="sagemaker-hyperpod-model-deployment-setup-keda"></a>

1. Create the trust policy and permissions policy.

   ```
   # Create trust policy
   cat <<EOF > /tmp/keda-trust-policy.json
   {
   "Version": "2012-10-17",		 	 	 
   "Statement": [
       {
           "Effect": "Allow",
           "Principal": {
               "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}"
           },
           "Action": "sts:AssumeRoleWithWebIdentity",
           "Condition": {
               "StringLike": {
                   "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:kube-system:keda-operator",
                   "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com"
               }
           }
       }
   ]
   }
   EOF
   # Create permissions policy
   cat <<EOF > /tmp/keda-policy.json
   {
   "Version": "2012-10-17",		 	 	 
   "Statement": [
       {
           "Effect": "Allow",
           "Action": [
               "cloudwatch:GetMetricData",
               "cloudwatch:GetMetricStatistics",
               "cloudwatch:ListMetrics"
           ],
           "Resource": "*"
       },
       {
           "Effect": "Allow",
           "Action": [
               "aps:QueryMetrics",
               "aps:GetLabels",
               "aps:GetSeries",
               "aps:GetMetricMetadata"
           ],
           "Resource": "*"
       }
   ]
   }
   EOF
   # Create the role
   aws iam create-role \
   --role-name keda-operator-role \
   --assume-role-policy-document file:///tmp/keda-trust-policy.json
   # Create the policy
   KEDA_POLICY_ARN=$(aws iam create-policy \
   --policy-name KedaOperatorPolicy \
   --policy-document file:///tmp/keda-policy.json \
   --query 'Policy.Arn' \
   --output text)
   # Attach the policy to the role
   aws iam attach-role-policy \
   --role-name keda-operator-role \
   --policy-arn $KEDA_POLICY_ARN
   ```

1. If you're using gated models, create an IAM role to access the gated models.

   1. Create the trust policy and IAM role for gated model access.

      ```
      %%bash -s $REGION
      
      JUMPSTART_GATED_ROLE_NAME="JumpstartGatedRole-${REGION}-${HYPERPOD_CLUSTER_NAME}"
      
      cat <<EOF > /tmp/trust-policy.json
      {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
                  "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}"
              },
              "Action": "sts:AssumeRoleWithWebIdentity",
              "Condition": {
                  "StringLike": {
                      "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:*:hyperpod-inference-service-account*",
                      "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com"
                  }
              }
          },
              {
              "Effect": "Allow",
              "Principal": {
                  "Service": "sagemaker.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
          }
      ]
      }
      EOF
      
      # Create the role and attach the managed policy
      aws iam create-role \
      --role-name $JUMPSTART_GATED_ROLE_NAME \
      --assume-role-policy-document file:///tmp/trust-policy.json
      
      aws iam attach-role-policy \
      --role-name $JUMPSTART_GATED_ROLE_NAME \
      --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodGatedModelAccess
      ```

      ```
      JUMPSTART_GATED_ROLE_ARN_LIST= !aws iam get-role --role-name=$JUMPSTART_GATED_ROLE_NAME --query "Role.Arn" --output text
      JUMPSTART_GATED_ROLE_ARN = JUMPSTART_GATED_ROLE_ARN_LIST[0]
      !echo $JUMPSTART_GATED_ROLE_ARN
      ```

### Install the inference operator
<a name="sagemaker-hyperpod-model-deployment-setup-install"></a>

1. Install the HyperPod inference operator. This step gathers the required AWS resource identifiers and generates the Helm installation command with the appropriate configuration parameters.

   Access the helm chart from [https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm\_chart](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart) .

   ```
   git clone https://github.com/aws/sagemaker-hyperpod-cli
   cd sagemaker-hyperpod-cli
   cd helm_chart/HyperPodHelmChart
   helm dependencies update charts/inference-operator
   ```

   ```
   %%bash -x
   
   HYPERPOD_INFERENCE_ROLE_ARN=$(aws iam get-role --role-name=$HYPERPOD_INFERENCE_ROLE_NAME --query "Role.Arn" --output text)
   echo $HYPERPOD_INFERENCE_ROLE_ARN
   
   S3_CSI_ROLE_ARN=$(aws iam get-role --role-name=$S3_CSI_ROLE_NAME --query "Role.Arn" --output text)
   echo $S3_CSI_ROLE_ARN
   
   HYPERPOD_CLUSTER_ARN=$(aws sagemaker describe-cluster --cluster-name $HYPERPOD_CLUSTER_NAME --query "ClusterArn")
   
   # Verify values
   echo "Cluster Name: $EKS_CLUSTER_NAME"
   echo "Execution Role: $HYPERPOD_INFERENCE_ROLE_ARN"
   echo "Hyperpod ARN: $HYPERPOD_CLUSTER_ARN"
   # Run the the HyperPod inference operator installation. 
   
   helm install hyperpod-inference-operator charts/inference-operator \
   -n kube-system \
   --set region=$REGION \
   --set eksClusterName=$EKS_CLUSTER_NAME \
   --set hyperpodClusterArn=$HYPERPOD_CLUSTER_ARN \
   --set executionRoleArn=$HYPERPOD_INFERENCE_ROLE_ARN \
   --set s3.serviceAccountRoleArn=$S3_CSI_ROLE_ARN \
   --set s3.node.serviceAccount.create=false \
   --set keda.podIdentity.aws.irsa.roleArn="arn:aws:iam::$ACCOUNT_ID:role/keda-operator-role" \
   --set tlsCertificateS3Bucket="s3://$BUCKET_NAME" \
   --set alb.region=$REGION \
   --set alb.clusterName=$EKS_CLUSTER_NAME \
   --set alb.vpcId=$VPC_ID
   
   # For JumpStart Gated Model usage, Add
   # --set jumpstartGatedModelDownloadRoleArn=$UMPSTART_GATED_ROLE_ARN
   ```

1. Configure the service account annotations for IAM integration. This annotation enables the operator's service account to assume the necessary IAM permissions for managing inference endpoints and interacting with AWS services.

   ```
   %%bash -x 
   
   EKS_CLUSTER_ROLE_NAME=$(echo $EKS_CLUSTER_ROLE | sed 's/.*\///')
   
   # Annotate service account
   kubectl annotate serviceaccount hyperpod-inference-controller-manager \
   -n hyperpod-inference-system \
   eks.amazonaws.com/role-arn=arn:aws:iam::${ACCOUNT_ID}:role/${EKS_CLUSTER_ROLE_NAME} \
   --overwrite
   ```

## Verify the inference operator is working
<a name="sagemaker-hyperpod-model-deployment-setup-verify"></a>

Follow these steps to verify that your inference operator installation is working correctly by deploying and testing a simple model.

**Deploy a test model to verify the operator**

1. Create a model deployment configuration file. This creates a Kubernetes manifest file that defines a JumpStart model deployment for the HyperPod inference operator.

   ```
   cat <<EOF>> simple_model_install.yaml
   ---
   apiVersion: inference.sagemaker.aws.amazon.com/v1
   kind: JumpStartModel
   metadata:
     name: testing-deployment-bert
     namespace: default
   spec:
     sageMakerEndpoint:
       name: "hp-inf-ep-for-testing"
     model:
       modelId: "huggingface-eqa-bert-base-cased"
     server:
       instanceType: "ml.c5.2xlarge"
     environmentVariables:
       - name: SAMPLE_ENV_VAR
         value: "sample_value"
     maxDeployTimeInSeconds: 1800
   EOF
   ```

1. Deploy the model and clean up the configuration file.

   ```
   kubectl create -f simple_model_install.yaml
   rm -f simple_model_install.yaml
   ```

1. Verify the service account configuration to ensure the operator can assume AWS permissions.

   ```
   # Get the service account details
   kubectl get serviceaccount -n hyperpod-inference-system
   
   # Check if the service account has the AWS annotations
   kubectl describe serviceaccount hyperpod-inference-controller-manager -n hyperpod-inference-system
   ```

**Configure deployment settings (if using Studio UI)**

1. Review the recommended instance type under **Deployment settings**.

1. If modifying the **Instance type**, ensure compatibility with your HyperPod cluster. Contact your admin if compatible instances aren't available.

1. For GPU-partitioned instances with MIG enabled, select an appropriate **GPU partition** from available MIG profiles to optimize GPU utilization. For more information, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md).

1. If using task governance, configure priority settings for model deployment preemption capabilities.

1. Enter the namespace provided by your admin. Contact your admin for the correct namespace if needed.

## (Optional) Set up user access through the JumpStart UI in SageMaker AI Studio Classic
<a name="sagemaker-hyperpod-model-deployment-setup-optional-js"></a>

For more background on setting up SageMaker HyperPod access for Studio Classic users and configuring fine-grained Kubernetes RBAC permissions for data scientist users, read [Setting up an Amazon EKS cluster in Studio](sagemaker-hyperpod-studio-setup-eks.md) and [Setting up Kubernetes role-based access control](sagemaker-hyperpod-eks-setup-rbac.md).

1. Identify the IAM role that Data Scientist users will use to manage and deploy models to SageMaker HyperPod from SageMaker AI Studio Classic. This is typically the User Profile Execution Role or Domain Execution Role for the Studio Classic user.

   ```
   %%bash -x
   
   export DATASCIENTIST_ROLE_NAME="<Execution Role Name used in SageMaker Studio Classic>"
   
   export DATASCIENTIST_POLICY_NAME="HyperPodUIAccessPolicy"
   export EKS_CLUSTER_ARN=$(aws --region ${REGION} sagemaker describe-cluster --cluster-name ${HYPERPOD_CLUSTER_NAME} \
     --query 'Orchestrator.Eks.ClusterArn' --output text)
   
   export DATASCIENTIST_HYPERPOD_NAMESPACE="team-namespace"
   ```

1. Attach an Identity Policy enabling Model Deployment access.

   ```
   %%bash -x
   
   # Create access policy
   cat << EOF > hyperpod-deployment-ui-access-policy.json
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DescribeHyerpodClusterPermissions",
               "Effect": "Allow",
               "Action": [
                   "sagemaker:DescribeCluster"
               ],
               "Resource": "${HYPERPOD_CLUSTER_ARN}"
           },
           {
               "Sid": "UseEksClusterPermissions",
               "Effect": "Allow",
               "Action": [
                   "eks:DescribeCluster",
                   "eks:AccessKubernetesApi",
                   "eks:MutateViaKubernetesApi",
                   "eks:DescribeAddon"
               ],
               "Resource": "${EKS_CLUSTER_ARN}"
           },
           {
               "Sid": "ListPermission",
               "Effect": "Allow",
               "Action": [
                   "sagemaker:ListClusters",
                   "sagemaker:ListEndpoints"
               ],
               "Resource": "*"
           },
           {
               "Sid": "SageMakerEndpointAccess",
               "Effect": "Allow",
               "Action": [
                   "sagemaker:DescribeEndpoint",
                   "sagemaker:InvokeEndpoint"
               ],
               "Resource": "arn:aws:sagemaker:${REGION}:${ACCOUNT_ID}:endpoint/*"
           }
       ]
   }
   EOF
   
   aws iam put-role-policy --role-name ${DATASCIENTIST_ROLE_NAME} --policy-name HyperPodDeploymentUIAccessInlinePolicy --policy-document file://hyperpod-deployment-ui-access-policy.json
   ```

1. Create an EKS Access Entry for the user mapping them to a kubernetes group.

   ```
   %%bash -x
   
   aws eks create-access-entry --cluster-name ${EKS_CLUSTER_NAME} \
       --principal-arn "arn:aws:iam::${ACCOUNT_ID}:role/${DATASCIENTIST_ROLE_NAME}" \
       --kubernetes-groups '["hyperpod-scientist-user-namespace-level","hyperpod-scientist-user-cluster-level"]'
   ```

1. Create Kubernetes RBAC policies for the user.

   ```
   %%bash -x
   
   cat << EOF > cluster_level_config.yaml
   kind: ClusterRole
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     name: hyperpod-scientist-user-cluster-role
   rules:
   - apiGroups: [""]
     resources: ["pods"]
     verbs: ["list"]
   - apiGroups: [""]
     resources: ["nodes"]
     verbs: ["list"]
   - apiGroups: [""]
     resources: ["namespaces"]
     verbs: ["get", "list"]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRoleBinding
   metadata:
     name: hyperpod-scientist-user-cluster-role-binding
   subjects:
   - kind: Group
     name: hyperpod-scientist-user-cluster-level
     apiGroup: rbac.authorization.k8s.io
   roleRef:
     kind: ClusterRole
     name: hyperpod-scientist-user-cluster-role
     apiGroup: rbac.authorization.k8s.io
   EOF
   
   
   kubectl apply -f cluster_level_config.yaml
   
   
   cat << EOF > namespace_level_role.yaml
   kind: Role
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     namespace: $DATASCIENTIST_HYPERPOD_NAMESPACE
     name: hyperpod-scientist-user-namespace-level-role
   rules:
   - apiGroups: [""]
     resources: ["pods"]
     verbs: ["create", "get"]
   - apiGroups: [""]
     resources: ["nodes"]
     verbs: ["get", "list"]
   - apiGroups: [""]
     resources: ["pods/log"]
     verbs: ["get", "list"]
   - apiGroups: [""]
     resources: ["pods/exec"]
     verbs: ["get", "create"]
   - apiGroups: ["kubeflow.org"]
     resources: ["pytorchjobs", "pytorchjobs/status"]
     verbs: ["get", "list", "create", "delete", "update", "describe"]
   - apiGroups: [""]
     resources: ["configmaps"]
     verbs: ["create", "update", "get", "list", "delete"]
   - apiGroups: [""]
     resources: ["secrets"]
     verbs: ["create", "get", "list", "delete"]
   - apiGroups: [ "inference.sagemaker.aws.amazon.com" ]
     resources: [ "inferenceendpointconfig", "inferenceendpoint", "jumpstartmodels" ]
     verbs: [ "get", "list", "create", "delete", "update", "describe" ]
   - apiGroups: [ "autoscaling" ]
     resources: [ "horizontalpodautoscalers" ]
     verbs: [ "get", "list", "watch", "create", "update", "patch", "delete" ]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     namespace: $DATASCIENTIST_HYPERPOD_NAMESPACE
     name: hyperpod-scientist-user-namespace-level-role-binding
   subjects:
   - kind: Group
     name: hyperpod-scientist-user-namespace-level
     apiGroup: rbac.authorization.k8s.io
   roleRef:
     kind: Role
     name: hyperpod-scientist-user-namespace-level-role
     apiGroup: rbac.authorization.k8s.io
   EOF
   
   
   kubectl apply -f namespace_level_role.yaml
   ```