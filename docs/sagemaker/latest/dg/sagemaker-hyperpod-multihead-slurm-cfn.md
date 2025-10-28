# Provisioning resources using

AWS CloudFormation stacks

To set up multiple controller nodes in a HyperPod Slurm cluster, provision AWS
resources through two AWS CloudFormation stacks: [Provision basic
resources](#sagemaker-hyperpod-multihead-slurm-cfn-basic "#sagemaker-hyperpod-multihead-slurm-cfn-basic") and [Provision
additional resources to support multiple controller nodes](#sagemaker-hyperpod-multihead-slurm-cfn-multihead "#sagemaker-hyperpod-multihead-slurm-cfn-multihead").

## Provision basic

resources

Follow these steps to provision basic resources for your Amazon SageMaker HyperPod Slurm cluster.

1. Download the [sagemaker-hyperpod.yaml](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/sagemaker-hyperpod.yaml "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/sagemaker-hyperpod.yaml") template file to your machine.
   This YAML file is an AWS CloudFormation template that defines the following
   resources to create for your Slurm cluster.
   - An execution IAM role for the compute node instance group
   - An Amazon S3 bucket to store the lifecycle scripts
   - Public and private subnets (private subnets have internet
     access through NAT gateways)
   - Internet Gateway/NAT gateways
   - Two Amazon EC2 security groups
   - An Amazon FSx volume to store configuration files

2. Run the following CLI command to create a AWS CloudFormation stack named
   `sagemaker-hyperpod`. Define the Availability Zone
   (AZ) IDs for your cluster in `PrimarySubnetAZ` and
   `BackupSubnetAZ`. For example,
   `use1-az4` is an AZ ID for an
   Availability Zone in the `us-east-1` Region. For more
   information, see [Availability Zone IDs](../../../ram/latest/userguide/working-with-az-ids.md "../../../ram/latest/userguide/working-with-az-ids.md") and [Setting
   up SageMaker HyperPod clusters across multiple AZs](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-multiple-availability-zones "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-multiple-availability-zones").

```
aws cloudformation deploy \
--template-file `/path_to_template/sagemaker-hyperpod.yaml` \
--stack-name `sagemaker-hyperpod` \
--parameter-overrides PrimarySubnetAZ=`use1-az4` BackupSubnetAZ=`use1-az1` \
--capabilities `CAPABILITY_IAM`
```

For more information, see [deploy](../../../cli/latest/reference/cloudformation/deploy.md "../../../cli/latest/reference/cloudformation/deploy.md") from the AWS Command Line Interface Reference. The stack creation
can take a few minutes to complete. When it's complete, you will see
the following in your command line interface.

```
Waiting for changeset to be created..
Waiting for stack create/update to complete
Successfully created/updated stack - sagemaker-hyperpod
```

3. (Optional) Verify the stack in the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home "https://console.aws.amazon.com/cloudformation/home").
   - From the left navigation, choose
     **Stack**.
   - On the **Stack** page, find and choose
     **sagemaker-hyperpod**.
   - Choose the tabs like **Resources** and
     **Outputs** to review the resources and
     outputs.

4. Create environment variables from the stack
   (`sagemaker-hyperpod`) outputs. You will use values
   of these variables to [Provision
   additional resources to support multiple controller nodes](#sagemaker-hyperpod-multihead-slurm-cfn-multihead "#sagemaker-hyperpod-multihead-slurm-cfn-multihead").

```
source .env
PRIMARY_SUBNET=$(aws --region $REGION cloudformation describe-stacks --stack-name $SAGEMAKER_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`PrimaryPrivateSubnet`].OutputValue' --output text)
BACKUP_SUBNET=$(aws --region $REGION cloudformation describe-stacks --stack-name $SAGEMAKER_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`BackupPrivateSubnet`].OutputValue' --output text)
EMAIL=$(bash -c 'read -p "INPUT YOUR SNSSubEmailAddress HERE: " && echo $REPLY')
DB_USER_NAME=$(bash -c 'read -p "INPUT YOUR DB_USER_NAME HERE: " && echo $REPLY')
SECURITY_GROUP=$(aws --region $REGION cloudformation describe-stacks --stack-name $SAGEMAKER_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`SecurityGroup`].OutputValue' --output text)
ROOT_BUCKET_NAME=$(aws --region $REGION cloudformation describe-stacks --stack-name $SAGEMAKER_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`AmazonS3BucketName`].OutputValue' --output text)
SLURM_FSX_DNS_NAME=$(aws --region $REGION cloudformation describe-stacks --stack-name $SAGEMAKER_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`FSxLustreFilesystemDNSname`].OutputValue' --output text)
SLURM_FSX_MOUNT_NAME=$(aws --region $REGION cloudformation describe-stacks --stack-name $SAGEMAKER_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`FSxLustreFilesystemMountname`].OutputValue' --output text)
COMPUTE_NODE_ROLE=$(aws --region $REGION cloudformation describe-stacks --stack-name $SAGEMAKER_STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`AmazonSagemakerClusterExecutionRoleArn`].OutputValue' --output text)
```

When you see prompts asking for your email address and database user
name, enter values like the following.

```
INPUT YOUR SNSSubEmailAddress HERE: `Email_address_to_receive_SNS_notifications`
INPUT YOUR DB_USER_NAME HERE: `Database_user_name_you_define`
```

To verify variable values, use the `print
 `$variable`` command.

```
print $REGION
us-east-1
```

## Provision

additional resources to support multiple controller nodes

Follow these steps to provision additional resources for your Amazon SageMaker HyperPod
Slurm cluster with multiple controller nodes.

1. Download the [sagemaker-hyperpod-slurm-multi-headnode.yaml](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/sagemaker-hyperpod-slurm-multi-headnode.yaml "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/sagemaker-hyperpod-slurm-multi-headnode.yaml") template
   file to your machine. This second YAML file is an AWS CloudFormation template
   that defines the additional resources to create for multiple
   controller nodes support in your Slurm cluster.
   - An execution IAM role for the controller node instance
     group
   - An Amazon RDS for MariaDB instance
   - An Amazon SNS topic and subscription
   - AWS Secrets Manager credentials for Amazon RDS for MariaDB

2. Run the following CLI command to create a AWS CloudFormation stack named
   `sagemaker-hyperpod-mh`. This second stack uses the
   AWS CloudFormation template to create additional AWS resources to support the
   multiple controller nodes architecture.

```
aws cloudformation deploy \
--template-file `/path_to_template/slurm-multi-headnode.yaml` \
--stack-name `sagemaker-hyperpod-mh` \
--parameter-overrides \
SlurmDBSecurityGroupId=$SECURITY_GROUP \
SlurmDBSubnetGroupId1=$PRIMARY_SUBNET \
SlurmDBSubnetGroupId2=$BACKUP_SUBNET \
SNSSubEmailAddress=$EMAIL \
SlurmDBUsername=$DB_USER_NAME \
--capabilities `CAPABILITY_NAMED_IAM`
```

For more information, see [deploy](../../../cli/latest/reference/cloudformation/deploy.md "../../../cli/latest/reference/cloudformation/deploy.md") from the AWS Command Line Interface Reference. The stack creation
can take a few minutes to complete. When it's complete, you will see
the following in your command line interface.

```
Waiting for changeset to be created..
Waiting for stack create/update to complete
Successfully created/updated stack - sagemaker-hyperpod-mh
```

3. (Optional) Verify the stack in the [AWS
   Cloud Formation console](https://console.aws.amazon.com/cloudformation/home "https://console.aws.amazon.com/cloudformation/home").
   - From the left navigation, choose
     **Stack**.
   - On the **Stack** page, find and choose
     **sagemaker-hyperpod-mh**.
   - Choose the tabs like **Resources** and
     **Outputs** to review the resources and
     outputs.

4. Create environment variables from the stack
   (`sagemaker-hyperpod-mh`) outputs. You will use
   values of these variables to update the configuration file
   (`provisioning_parameters.json`) in [Preparing and uploading
   lifecycle scripts](sagemaker-hyperpod-multihead-slurm-scripts.md "sagemaker-hyperpod-multihead-slurm-scripts.md").

```
source .env
SLURM_DB_ENDPOINT_ADDRESS=$(aws --region us-east-1 cloudformation describe-stacks --stack-name $MULTI_HEAD_SLURM_STACK --query 'Stacks[0].Outputs[?OutputKey==`SlurmDBEndpointAddress`].OutputValue' --output text)
SLURM_DB_SECRET_ARN=$(aws --region us-east-1 cloudformation describe-stacks --stack-name $MULTI_HEAD_SLURM_STACK --query 'Stacks[0].Outputs[?OutputKey==`SlurmDBSecretArn`].OutputValue' --output text)
SLURM_EXECUTION_ROLE_ARN=$(aws --region us-east-1 cloudformation describe-stacks --stack-name $MULTI_HEAD_SLURM_STACK --query 'Stacks[0].Outputs[?OutputKey==`SlurmExecutionRoleArn`].OutputValue' --output text)
SLURM_SNS_FAILOVER_TOPIC_ARN=$(aws --region us-east-1 cloudformation describe-stacks --stack-name $MULTI_HEAD_SLURM_STACK --query 'Stacks[0].Outputs[?OutputKey==`SlurmFailOverSNSTopicArn`].OutputValue' --output text)
```
