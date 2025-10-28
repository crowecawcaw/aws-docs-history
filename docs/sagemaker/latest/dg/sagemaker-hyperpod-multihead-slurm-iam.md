# Creating and attaching an

IAM policy

This section explains how to create an IAM policy and attach it to the execution
role you created in [Provision
additional resources to support multiple controller nodes](sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead "sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead").

1. Download the [IAM policy example](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/1.AmazonSageMakerClustersExecutionRolePolicy.json "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/1.AmazonSageMakerClustersExecutionRolePolicy.json") to your machine from the GitHub
   repository.
2. Create an IAM policy with the downloaded example, using the [create-policy](../../../cli/latest/reference/iam/create-policy.md "../../../cli/latest/reference/iam/create-policy.md") CLI command.

```
aws --region `us-east-1` iam create-policy \
    --policy-name `AmazonSagemakerExecutionPolicy` \
    --policy-document file://`1.AmazonSageMakerClustersExecutionRolePolicy.json`
```

Example output of the command.

```
{
    "Policy": {
        "PolicyName": "AmazonSagemakerExecutionPolicy",
        "PolicyId": "ANPAXISIWY5UYZM7WJR4W",
        "Arn": "arn:aws:iam::111122223333:policy/AmazonSagemakerExecutionPolicy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2025-01-22T20:01:21+00:00",
        "UpdateDate": "2025-01-22T20:01:21+00:00"
    }
}
```

3. Attach the policy `AmazonSagemakerExecutionPolicy` to the Slurm
   execution role you created in [Provision
   additional resources to support multiple controller nodes](sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead "sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead"), using the [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") CLI command.

```
aws --region `us-east-1` iam attach-role-policy \
    --role-name `AmazonSagemakerExecutionRole` \
    --policy-arn `arn:aws:iam::111122223333:policy/AmazonSagemakerExecutionPolicy`
```

This command doesn't produce any output.

(Optional) If you use environment variables, here are the example
commands.

    * To get the role name and policy name



    ```
    POLICY=$(aws --region $REGION iam list-policies --query 'Policies[?PolicyName==AmazonSagemakerExecutionPolicy].Arn' --output text)
    ROLENAME=$(aws --region $REGION iam list-roles --query "Roles[?Arn=='${SLURM_EXECUTION_ROLE_ARN}'].RoleName" —output text)
    ```
    * To attach the policy



    ```
    aws  --region us-east-1 iam attach-role-policy \
         --role-name $ROLENAME --policy-arn $POLICY
    ```

For more information, see [IAM role for
SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod").
