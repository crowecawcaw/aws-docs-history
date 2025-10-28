# Create and configure a

HyperPod cluster with Karpenter autoscaling

In the following steps, you'll create a SageMaker HyperPod cluster with continuous
provisioning enabled and configure it to use Karpenter-based autoscaling.

###### Create a HyperPod cluster

1. Load your environment configuration and extract values from CloudFormation
   stacks.

```
source .env
SUBNET1=$(cfn-output $VPC_STACK_NAME PrivateSubnet1)
SUBNET2=$(cfn-output $VPC_STACK_NAME PrivateSubnet2)
SUBNET3=$(cfn-output $VPC_STACK_NAME PrivateSubnet3)
SECURITY_GROUP=$(cfn-output $VPC_STACK_NAME NoIngressSecurityGroup)
EKS_CLUSTER_ARN=$(cfn-output $EKS_STACK_NAME ClusterArn)
EXECUTION_ROLE=$(cfn-output $SAGEMAKER_STACK_NAME ExecutionRole)
SERVICE_ROLE=$(cfn-output $SAGEMAKER_STACK_NAME ServiceRole)
BUCKET_NAME=$(cfn-output $SAGEMAKER_STACK_NAME Bucket)
HP_CLUSTER_NAME="hyperpod-eks-test-$(date +%s)"
EKS_CLUSTER_NAME=$(cfn-output $EKS_STACK_NAME ClusterName)
HP_CLUSTER_ROLE=$(cfn-output $SAGEMAKER_STACK_NAME ClusterRole)
```

2. Upload the node initialization script to your Amazon S3 bucket.

```
aws s3 cp lifecyclescripts/on_create_noop.sh s3://$BUCKET_NAME
```

3. Create a cluster configuration file with your environment variables.

```
cat > cluster_config.json << EOF
{
    "ClusterName": "$HP_CLUSTER_NAME",
    "InstanceGroups": [
        {
            "InstanceCount": 1,
            "InstanceGroupName": "system",
            "InstanceType": "ml.c5.xlarge",
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://$BUCKET_NAME",
                "OnCreate": "on_create_noop.sh"
            },
            "ExecutionRole": "$EXECUTION_ROLE"
        },
        {
            "InstanceCount": 0,
            "InstanceGroupName": "auto-c5-az1",
            "InstanceType": "ml.c5.xlarge",
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://$BUCKET_NAME",
                "OnCreate": "on_create_noop.sh"
            },
            "ExecutionRole": "$EXECUTION_ROLE"
        },
        {
            "InstanceCount": 0,
            "InstanceGroupName": "auto-c5-4xaz2",
            "InstanceType": "ml.c5.4xlarge",
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://$BUCKET_NAME",
                "OnCreate": "on_create_noop.sh"
            },
            "ExecutionRole": "$EXECUTION_ROLE",
            "OverrideVpcConfig": {
                "SecurityGroupIds": [
                    "$SECURITY_GROUP"
                ],
                "Subnets": [
                    "$SUBNET2"
                ]
            }
        },
        {
            "InstanceCount": 0,
            "InstanceGroupName": "auto-g5-az3",
            "InstanceType": "ml.g5.xlarge",
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://$BUCKET_NAME",
                "OnCreate": "on_create_noop.sh"
            },
            "ExecutionRole": "$EXECUTION_ROLE",
            "OverrideVpcConfig": {
                "SecurityGroupIds": [
                    "$SECURITY_GROUP"
                ],
                "Subnets": [
                    "$SUBNET3"
                ]
            }
        }
    ],
    "VpcConfig": {
        "SecurityGroupIds": [
            "$SECURITY_GROUP"
        ],
        "Subnets": [
            "$SUBNET1"
        ]
    },
    "Orchestrator": {
        "Eks": {
            "ClusterArn": "$EKS_CLUSTER_ARN"
        }
    },
    "ClusterRole": "$HP_CLUSTER_ROLE",
    "AutoScaling": {
        "Mode": "Enable",
        "AutoScalerType": "Karpenter"
    },
    "NodeProvisioningMode": "Continuous"
}
EOF
```

4. Run the following command to create your HyperPod cluster.

```
aws sagemaker create-cluster --cli-input-json file://./cluster_config.json
```

5. The cluster creation process takes approximately 20 minutes. Monitor the
   cluster status until both ClusterStatus and AutoScaling.Status show
   InService.
6. Save the cluster ARN for subsequent operations.

```
HP_CLUSTER_ARN=$(aws sagemaker describe-cluster --cluster-name $HP_CLUSTER_NAME \
   --output text --query ClusterArn)
```

###### Enable Karpenter autoscaling

1. Run the following command to enable Karpenter-based autoscaling on any
   pre-existing cluster that has continuous node provisioning mode.

```
aws sagemaker update-cluster \
    --cluster-name $HP_CLUSTER_NAME \
    --auto-scaling Mode=Enable,AutoScalerType=Karpenter \
    --cluster-role $HP_CLUSTER_ROLE
```

2. Verify that Karpenter has been successfully enabled:

```
aws sagemaker describe-cluster --cluster-name $HP_CLUSTER_NAME --query 'AutoScaling'
```

3. Expected output:

```
{
    "Mode": "Enable",
    "AutoScalerType": "Karpenter",
    "Status": "InService"
}
```

Wait for the `Status` to show `InService` before proceeding to
configure NodeClass and NodePool.
