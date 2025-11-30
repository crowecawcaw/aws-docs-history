# Setting up your

HyperPod clusters for model deployment

This guide provides you with a comprehensive setup guide for enabling inference
capabilities on Amazon SageMaker HyperPod clusters. The following steps help you set up the
infrastructure, permissions, and operators required to support machine learning
engineers in deploying and managing inference endpoints.

###### Note

To create a cluster with the inference operator pre-installed, see [Create an EKS-orchestrated
SageMaker HyperPod cluster](sagemaker-hyperpod-quickstart.md#sagemaker-hyperpod-quickstart-eks "sagemaker-hyperpod-quickstart.md#sagemaker-hyperpod-quickstart-eks"). To install the inference
operator on an existing cluster, continue with the following procedures.

## Prerequisites

Before proceeding, verify that your AWS credentials are properly configured and
have the necessary permissions. The following steps need to be run by an IAM
principal with Administrator privileges and Cluster Admin access to an Amazon EKS cluster.
Verify that you've created a HyperPod cluster with [Creating
a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md") .
Verify you have installed helm, eksctl, and kubectl command line utilities.

For Kubernetes administrative access to the Amazon EKS cluster, go to the Amazon EKS console and
select the cluster you are using. Look in the **Access** tab and select IAM Access Entries. If there isn't an entry
for your IAM principal, select **Create Access
Entry**. Then select the desired IAM principal and associate the
`AmazonEKSClusterAdminPolicy` with it.

1. Configure kubectl to connect to the newly created HyperPod
   cluster orchestrated by Amazon EKS cluster. Specify the Region and
   HyperPod cluster name.

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

2. Set default env variables.

```
LB_CONTROLLER_POLICY_NAME="AWSLoadBalancerControllerIAMPolicy-$HYPERPOD_CLUSTER_NAME"
LB_CONTROLLER_ROLE_NAME="aws-load-balancer-controller-$HYPERPOD_CLUSTER_NAME"
S3_MOUNT_ACCESS_POLICY_NAME="S3MountpointAccessPolicy-$HYPERPOD_CLUSTER_NAME"
S3_CSI_ROLE_NAME="SM_HP_S3_CSI_ROLE-$HYPERPOD_CLUSTER_NAME"
KEDA_OPERATOR_POLICY_NAME="KedaOperatorPolicy-$HYPERPOD_CLUSTER_NAME"
KEDA_OPERATOR_ROLE_NAME="keda-operator-role-$HYPERPOD_CLUSTER_NAME"
PRESIGNED_URL_ACCESS_POLICY_NAME="PresignedUrlAccessPolicy-$HYPERPOD_CLUSTER_NAME"
HYPERPOD_INFERENCE_ACCESS_POLICY_NAME="HyperpodInferenceAccessPolicy-$HYPERPOD_CLUSTER_NAME"
HYPERPOD_INFERENCE_ROLE_NAME="HyperpodInferenceRole-$HYPERPOD_CLUSTER_NAME"
HYPERPOD_INFERENCE_SA_NAME="hyperpod-inference-operator-controller"
HYPERPOD_INFERENCE_SA_NAMESPACE="hyperpod-inference-system"
JUMPSTART_GATED_ROLE_NAME="JumpstartGatedRole-$HYPERPOD_CLUSTER_NAME"
FSX_CSI_ROLE_NAME="AmazonEKSFSxLustreCSIDriverFullAccess-$HYPERPOD_CLUSTER_NAME"
```

3. Extract the Amazon EKS cluster name from the cluster ARN, update the local
   kubeconfig, and verify connectivity by listing all pods across
   namespaces.

```
kubectl get pods --all-namespaces
```

4. (Optional) Install the NVIDIA device plugin to enable GPU support on the
   cluster.

```
#Install nvidia device plugin
kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.14.5/nvidia-device-plugin.yml
# Verify that GPUs are visible to k8s
kubectl get nodes -o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia.com/gpu

```

## Prepare your

environment for inference operator installation

Now that your HyperPod cluster is configured, the next step is to install
the inference operator. The inference operator is a Kubernetes operator that enables
deployment and management of machine learning inference endpoints on your Amazon EKS
cluster.

Complete the next critical preparation steps to ensure your Amazon EKS cluster has the
proper security configurations and supporting infrastructure components. This
involves configuring IAM roles and security policies for cross-service
authentication, installing the AWS Load Balancer Controller for ingress
management, setting up Amazon S3 and Amazon FSx CSI drivers for persistent storage access, and
deploying KEDA and cert-manager for autoscaling and certificate management
capabilities.

1. Gather essential AWS resource identifiers and ARNs required for
   configuring service integrations between Amazon EKS, SageMaker AI, and IAM
   components.

```
%%bash -x

export ACCOUNT_ID=$(aws --region $REGION sts get-caller-identity --query 'Account' --output text)
export OIDC_ID=$(aws --region $REGION eks describe-cluster --name $EKS_CLUSTER_NAME --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5)
export EKS_CLUSTER_ROLE=$(aws eks --region $REGION describe-cluster --name $EKS_CLUSTER_NAME --query 'cluster.roleArn' --output text)
```

2. Associate an IAM OIDCidentity provider with your EKS cluster.

```
eksctl utils associate-iam-oidc-provider --region=$REGION --cluster=$EKS_CLUSTER_NAME --approve
```

3. Create the trust policy and permission policy JSON documents required for
   the HyperPod inference operator IAM role. These policies enable secure
   cross-service communication between Amazon EKS, SageMaker AI, and other AWS
   services.

```
bash
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
                    "oidc.eks.${REGION}.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:*:*"
                }
            }
        }
    ]
}
EOF

# Create permission policy JSON
cat << EOF > permission-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "S3Access",
        "Effect": "Allow",
        "Action": [
            "s3:Get*",
            "s3:List*",
            "s3:Describe*",
            "s3:PutObject"
        ],
        "Resource": [
            "*"
        ]
        },
        {
        "Sid": "ECRAccess",
        "Effect": "Allow",
        "Action": [
            "ecr:GetAuthorizationToken",
            "ecr:BatchCheckLayerAvailability",
            "ecr:GetDownloadUrlForLayer",
            "ecr:GetRepositoryPolicy",
            "ecr:DescribeRepositories",
            "ecr:ListImages",
            "ecr:DescribeImages",
            "ecr:BatchGetImage",
            "ecr:GetLifecyclePolicy",
            "ecr:GetLifecyclePolicyPreview",
            "ecr:ListTagsForResource",
            "ecr:DescribeImageScanFindings"
        ],
        "Resource": [
            "*"
        ]
        },
        {
        "Sid": "EC2Access",
        "Effect": "Allow",
        "Action": [
            "ec2:AssignPrivateIpAddresses",
            "ec2:AttachNetworkInterface",
            "ec2:CreateNetworkInterface",
            "ec2:DeleteNetworkInterface",
            "ec2:DescribeInstances",
            "ec2:DescribeTags",
            "ec2:DescribeNetworkInterfaces",
            "ec2:DescribeInstanceTypes",
            "ec2:DescribeSubnets",
            "ec2:DetachNetworkInterface",
            "ec2:ModifyNetworkInterfaceAttribute",
            "ec2:UnassignPrivateIpAddresses",
            "ec2:CreateTags",
            "ec2:DescribeInstances",
            "ec2:DescribeInstanceTypes",
            "ec2:DescribeRouteTables",
            "ec2:DescribeSecurityGroups",
            "ec2:DescribeSubnets",
            "ec2:DescribeVolumes",
            "ec2:DescribeVolumesModifications",
            "ec2:DescribeVpcs",
            "ec2:CreateVpcEndpointServiceConfiguration",
            "ec2:DeleteVpcEndpointServiceConfigurations",
            "ec2:DescribeVpcEndpointServiceConfigurations",
            "ec2:ModifyVpcEndpointServicePermissions"
        ],
        "Resource": [
            "*"
        ]
        },
        {
        "Sid": "EKSAuthAccess",
        "Effect": "Allow",
        "Action": [
            "eks-auth:AssumeRoleForPodIdentity"
        ],
        "Resource": [
            "*"
        ]
        },
        {
        "Sid": "EKSAccess",
        "Effect": "Allow",
        "Action": [
            "eks:AssociateAccessPolicy",
            "eks:Describe*",
            "eks:List*",
            "eks:AccessKubernetesApi"
        ],
        "Resource": [
            "*"
        ]
        },
        {
        "Sid": "ApiGatewayAccess",
        "Effect": "Allow",
        "Action": [
            "apigateway:POST",
            "apigateway:GET",
            "apigateway:PUT",
            "apigateway:PATCH",
            "apigateway:DELETE",
            "apigateway:UpdateRestApiPolicy"
        ],
        "Resource": [
            "arn:aws:apigateway:*::/vpclinks",
            "arn:aws:apigateway:*::/vpclinks/*",
            "arn:aws:apigateway:*::/restapis",
            "arn:aws:apigateway:*::/restapis/*"
        ]
        },
        {
        "Sid": "ElasticLoadBalancingAccess",
        "Effect": "Allow",
        "Action": [
            "elasticloadbalancing:CreateLoadBalancer",
            "elasticloadbalancing:DescribeLoadBalancers",
            "elasticloadbalancing:DescribeLoadBalancerAttributes",
            "elasticloadbalancing:DescribeListeners",
            "elasticloadbalancing:DescribeListenerCertificates",
            "elasticloadbalancing:DescribeSSLPolicies",
            "elasticloadbalancing:DescribeRules",
            "elasticloadbalancing:DescribeTargetGroups",
            "elasticloadbalancing:DescribeTargetGroupAttributes",
            "elasticloadbalancing:DescribeTargetHealth",
            "elasticloadbalancing:DescribeTags",
            "elasticloadbalancing:DescribeTrustStores",
            "elasticloadbalancing:DescribeListenerAttributes"
        ],
        "Resource": [
            "*"
        ]
        },
        {
        "Sid": "SageMakerAccess",
        "Effect": "Allow",
        "Action": [
            "sagemaker:*"
        ],
        "Resource": [
            "*"
        ]
        },
        {
        "Sid": "AllowPassRoleToSageMaker",
        "Effect": "Allow",
        "Action": [
            "iam:PassRole"
        ],
        "Resource": "arn:aws:iam::*:role/*",
        "Condition": {
            "StringEquals": {
            "iam:PassedToService": "sagemaker.amazonaws.com"
            }
        }
        },
        {
        "Sid": "AcmAccess",
        "Effect": "Allow",
        "Action": [
            "acm:ImportCertificate",
            "acm:DeleteCertificate"
        ],
        "Resource": [
            "*"
        ]
        }
    ]
}
EOF
```

4. Create execution Role for the inference operator.

```
aws iam create-policy --policy-name $HYPERPOD_INFERENCE_ACCESS_POLICY_NAME --policy-document file://permission-policy.json
export policy_arn="arn:aws:iam::${ACCOUNT_ID}:policy/$HYPERPOD_INFERENCE_ACCESS_POLICY_NAME"
```

```
aws iam create-role --role-name $HYPERPOD_INFERENCE_ROLE_NAME --assume-role-policy-document file://trust-policy.json

aws iam put-role-policy --role-name $HYPERPOD_INFERENCE_ROLE_NAME --policy-name InferenceOperatorInlinePolicy --policy-document file://permission-policy.json
```

5. Download and create the IAM policy required for the AWS Load Balancer
   Controller to manage Application Load Balancers and Network Load Balancers
   in your EKS cluster.

```
%%bash -x

export ALBController_IAM_POLICY_NAME=HyperPodInferenceALBControllerIAMPolicy

curl -o AWSLoadBalancerControllerIAMPolicy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.13.0/docs/install/iam_policy.json
aws iam create-policy --policy-name $ALBController_IAM_POLICY_NAME --policy-document file://AWSLoadBalancerControllerIAMPolicy.json
```

6. Create an IAM service account that links the Kubernetes service account
   with the IAM policy, enabling the AWS Load Balancer Controller to assume
   the necessary AWS permissions through IRSA (IAM Roles for Service
   Accounts).

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

7. Apply Tags (`kubernetes.io.role/elb`) to all subnets in the Amazon EKS
   cluster (both public and private).

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

8. Create a Namespace for KEDA and the Cert Manager.

```
kubectl create namespace keda
kubectl create namespace cert-manager
```

9. Create an Amazon S3 VPC endpoint.

```
aws ec2 create-vpc-endpoint \
  --vpc-id ${VPC_ID} \
  --vpc-endpoint-type Gateway \
  --service-name "com.amazonaws.${REGION}.s3" \
  --route-table-ids $(aws ec2 describe-route-tables --filters "Name=vpc-id,Values=${VPC_ID}" --query 'RouteTables[].Associations[].RouteTableId' --output text | tr ' ' '\n' | sort -u | tr '\n' ' ')
```

10. Configure S3 storage access:
    1.  Create an IAM policy that grants the necessary S3 permissions for
        using Mountpoint for Amazon S3, which enables file system access to
        S3 buckets from within the cluster.

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
                    "Federated": "arn:aws:iam::$ACCOUNT_ID:oidc-provider/oidc.eks.$REGION.amazonaws.com/id/${OIDC_ID}"
                },
                "Action": "sts:AssumeRoleWithWebIdentity",
                "Condition": {
                    "StringEquals": {
                        "oidc.eks.$REGION.amazonaws.com/id/${OIDC_ID}:aud": "sts.amazonaws.com",
                        "oidc.eks.$REGION.amazonaws.com/id/${OIDC_ID}:sub": "system:serviceaccount:kube-system:${s3-csi-driver-sa}"
                    }
                }
            }
        ]
    }
    EOF

    aws iam create-role --role-name $S3_CSI_ROLE_NAME --assume-role-policy-document file://s3accesstrustpolicy.json

    aws iam attach-role-policy --role-name $S3_CSI_ROLE_NAME --policy-arn "arn:aws:iam::$ACCOUNT_ID:policy/S3MountpointAccessPolicy"

    ```

    2.  (Optional) Create an IAM service account for the Amazon S3 CSI
        driver. The Amazon S3 CSI driver requires an IAM service account
        with appropriate permissions to mount S3 buckets as persistent
        volumes in your Amazon EKS cluster. This step creates the necessary IAM
        role and Kubernetes service account with the required S3 access
        policy.

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

    3.  (Optional) Install the Amazon S3 CSI driver add-on. This driver
        enables your pods to mount S3 buckets as persistent volumes,
        providing direct access to S3 storage from within your Kubernetes
        workloads.

    ```
    %%bash -x

    export S3_CSI_ROLE_ARN=$(aws iam get-role --role-name $S3_CSI_ROLE_NAME  --query 'Role.Arn' --output text)
    eksctl create addon --name aws-mountpoint-s3-csi-driver --cluster $EKS_CLUSTER_NAME --service-account-role-arn $S3_CSI_ROLE_ARN --force
    ```

    4.  (Optional) Create a Persistent Volume Claim (PVC) for S3 storage.
        This PVC enables your pods to request and use S3 storage as if it
        were a traditional file system.

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

11. (Optional) Configure FSx storage access. Create an IAM service account for
    the Amazon FSx CSI driver. This service account will be used by the FSx CSI
    driver to interact with the Amazon FSx service on behalf of your cluster.

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

## Create the KEDA

operator role

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
                "Federated": "arn:aws:iam::$ACCOUNT_ID:oidc-provider/oidc.eks.$REGION.amazonaws.com/id/$OIDC_ID"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "oidc.eks.$REGION.amazonaws.com/id/$OIDC_ID:sub": "system:serviceaccount:kube-system:keda-operator",
                    "oidc.eks.$REGION.amazonaws.com/id/$OIDC_ID:aud": "sts.amazonaws.com"
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

2. If you're using gated models, create an IAM role to access the gated
   models.
   1. Create an IAM policy.

   ```
   %%bash -s $REGION

   cat <<EOF> /tmp/presignedurl-policy.json
   {
      "Version": "2012-10-17",
      "Statement": [
           {
               "Sid": "CreatePresignedUrlAccess",
               "Effect": "Allow",
               "Action": [
                   "sagemaker:CreateHubContentPresignedUrls"
               ],
               "Resource": [
                   "arn:aws:sagemaker:$1:aws:hub/SageMakerPublicHub",
                   "arn:aws:sagemaker:$1:aws:hub-content/SageMakerPublicHub/*/*"
               ]
           }
      ]
   }
   EOF

   aws iam create-policy --policy-name PresignedUrlAccessPolicy --policy-document file:///tmp/presignedurl-policy.json

   JUMPSTART_GATED_ROLE_NAME="JumpstartGatedRole-${REGION}-${HYPERPOD_CLUSTER_NAME}"

   cat <<EOF > /tmp/trust-policy.json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Federated": "arn:aws:iam::$ACCOUNT_ID:oidc-provider/oidc.eks.$REGION.amazonaws.com/id/$OIDC_ID"
               },
               "Action": "sts:AssumeRoleWithWebIdentity",
               "Condition": {
                   "StringLike": {
                       "oidc.eks.$REGION.amazonaws.com/id/$OIDC_ID:sub": "system:serviceaccount:*:$HYPERPOD_INFERENCE_SA_NAME",
                       "oidc.eks.$REGION.amazonaws.com/id/$OIDC_ID:aud": "sts.amazonaws.com"
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

   2. Create an IAM role.

   ```
   # Create the role using existing trust policy
   aws iam create-role \
       --role-name $JUMPSTART_GATED_ROLE_NAME \
       --assume-role-policy-document file:///tmp/trust-policy.json
   # Attach the existing PresignedUrlAccessPolicy to the role
   aws iam attach-role-policy \
       --role-name $JUMPSTART_GATED_ROLE_NAME \
       --policy-arn arn:aws:iam::${ACCOUNT_ID}:policy/PresignedUrlAccessPolicy
   ```

   ```
   JUMPSTART_GATED_ROLE_ARN_LIST= !aws iam get-role --role-name=$JUMPSTART_GATED_ROLE_NAME --query "Role.Arn" --output text
   JUMPSTART_GATED_ROLE_ARN = JUMPSTART_GATED_ROLE_ARN_LIST[0]
   !echo $JUMPSTART_GATED_ROLE_ARN
   ```

   3. Add `SageMakerFullAccess` policy to the execution
      role.

   ```
   aws iam attach-role-policy --role-name=$HYPERPOD_INFERENCE_ROLE_NAME --policy-arn=arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
   ```

## Install the

inference operator

1. Install the HyperPod inference operator. This step gathers the required
   AWS resource identifiers and generates the Helm installation command with
   the appropriate configuration parameters.

Access the helm chart from [https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart")
.

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

2. Configure the service account annotations for IAM integration. This
   annotation enables the operator's service account to assume the necessary
   IAM permissions for managing inference endpoints and interacting with
   AWS services.

```
%%bash -x

EKS_CLUSTER_ROLE_NAME=$(echo $EKS_CLUSTER_ROLE | sed 's/.*\///')

# Annotate service account
kubectl annotate serviceaccount hyperpod-inference-operator-controller-manager \
  -n hyperpod-inference-system \
  eks.amazonaws.com/role-arn=arn:aws:iam::${ACCOUNT_ID}:role/${EKS_CLUSTER_ROLE_NAME} \
  --overwrite
```

## Verify the

inference operator is working

1. Create a model deployment configuration file. This creates a Kubernetes
   manifest file that defines a JumpStart model deployment for the HyperPod
   inference operator. The configuration specifies how to deploy a pre-trained
   model from Amazon SageMaker JumpStart as an inference endpoint on your Amazon EKS
   cluster.

```
cat <<EOF>> simple_model_install.yaml
---
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: JumpStartModel
metadata:
  name: testing-deployment-bert
  namespace: default
spec:
  model:
    modelId: "huggingface-eqa-bert-base-cased"
  sageMakerEndpoint:
    name: "hp-inf-ep-for-testing"
  server:
    instanceType: "ml.c5.2xlarge"
  environmentVariables:
    - name: SAMPLE_ENV_VAR
      value: "sample_value"
  maxDeployTimeInSeconds: 1800
EOF
```

2. Deploy the model and clean up the configuration file. This step creates
   the JumpStart model resource and removes the temporary configuration
   file to maintain a clean workspace.

```
%%bash -x

kubectl create -f simple_model_install.yaml
rm -rfv simple_model_install.yaml
```

3. Check if the model is installed and running. This verification ensures
   that the operator can successfully assume AWS permissions for managing
   inference endpoints.

```
%%bash

# Get the service account details
kubectl get serviceaccount -n hyperpod-inference-system

# Check if the service account has the AWS annotations
kubectl describe serviceaccount hyperpod-inference-operator-controller-manager -n hyperpod-inference-system
```

4. Under **Deployment settings**, JumpStart
   will recommend an instance for deployment. You can modify these settings
   if necessary.
   1. If you modify **Instance type**,
      ensure it's compatible with the chosen **HyperPod cluster**. If there aren't any
      compatible instances, you'll need to select a new **HyperPod cluster** or contact
      your admin to add compatible instances to the cluster.
   2. If your selected instance type supports GPU partitioning and your cluster is configured with MIG, you can select a specific **GPU partition** from the available MIG profiles. This allows you to optimize GPU utilization by allocating only the required GPU resources for your model. For more information, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md "sagemaker-hyperpod-eks-gpu-partitioning.md").
   3. To prioritize the model deployment, install the task
      governance addon, create compute allocations, and set up task
      rankings for the cluster policy. Once this is done, you should
      see an option to select a priority for the model deployment
      which can be used for preemption of other deployments and tasks
      on the cluster.
   4. Enter the namespace to which your admin has provided you
      access. You may have to directly reach out to your admin to get
      the exact namespace. Once a valid namespace is provided, the
      **Deploy** button should be
      enabled to deploy the model.

## (Optional)

Set up user access through the JumpStart UI in SageMaker AI Studio Classic

For more background on setting up SageMaker HyperPod access for Studio Classic users and
configuring fine-grained Kubernetes RBAC permissions for data scientist users, read
[Setting up an Amazon EKS cluster in
Studio](sagemaker-hyperpod-studio-setup-eks.md "sagemaker-hyperpod-studio-setup-eks.md") and [Setting up Kubernetes role-based
access control](sagemaker-hyperpod-eks-setup-rbac.md "sagemaker-hyperpod-eks-setup-rbac.md").

1. Identify the IAM role that Data Scientist users will use to manage and
   deploy models to SageMaker HyperPod from SageMaker AI Studio Classic. This is typically the
   User Profile Execution Role or Domain Execution Role for the Studio Classic
   user.

```
%%bash -x

export DATASCIENTIST_ROLE_NAME="<Execution Role Name used in SageMaker Studio Classic>"

export DATASCIENTIST_POLICY_NAME="HyperPodUIAccessPolicy"
export EKS_CLUSTER_ARN=$(aws --region $REGION sagemaker describe-cluster --cluster-name $HYPERPOD_CLUSTER_NAME \
  --query 'Orchestrator.Eks.ClusterArn' --output text)

export DATASCIENTIST_HYPERPOD_NAMESPACE="team-namespace"
```

2. Attach an Identity Policy enabling Model Deployment access.

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
            "Resource": "$HYPERPOD_CLUSTER_ARN"
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
            "Resource": "$EKS_CLUSTER_ARN"
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
            "Resource": "arn:aws:sagemaker:$REGION:$ACCOUNT_ID:endpoint/*"
        }
    ]
}
EOF

aws iam put-role-policy --role-name DATASCIENTIST_ROLE_NAME --policy-name HyperPodDeploymentUIAccessInlinePolicy --policy-document file://hyperpod-deployment-ui-access-policy.json
```

3. Create an EKS Access Entry for the user mapping them to a kubernetes
   group.

```
%%bash -x

aws eks create-access-entry --cluster-name $EKS_CLUSTER_NAME \
    --principal-arn "arn:aws:iam::$ACCOUNT_ID:role/$DATASCIENTIST_ROLE_NAME" \
    --kubernetes-groups '["hyperpod-scientist-user-namespace-level","hyperpod-scientist-user-cluster-level"]'

```

4. Create Kubernetes RBAC policies for the user.

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
  verbs: ["list"]
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
  resources: [ "inferenceendpointconfig", "inferenceendpoint", "jumpstartmodel" ]
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
