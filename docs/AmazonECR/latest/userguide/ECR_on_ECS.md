

# Using Amazon ECR images with Amazon ECS
<a name="ECR_on_ECS"></a>

You can use your Amazon ECR private repositories to host container images and artifacts that your Amazon ECS tasks may pull from. For this to work, the Amazon ECS, or Fargate, container agent must have permissions to make the `ecr:BatchGetImage`, `ecr:GetDownloadUrlForLayer`, and `ecr:GetAuthorizationToken` APIs.

## Required IAM permissions
<a name="ECR_on_ECS_iampermissions"></a>

The following table shows the IAM role to use, for each launch type, that provides the required permissions for your tasks to pull from an Amazon ECR private repository. Amazon ECS provides managed IAM policies that include the required permissions.



| Launch type | IAM role | AWS managed IAM policy | 
| --- | --- | --- | 
| Amazon ECS on Amazon EC2 instances | Use the container instance IAM role, which is associated with the Amazon EC2 instance registered to your Amazon ECS cluster. For more information, see [Container instance IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*. | `AmazonEC2ContainerServiceforEC2Role`<br />For more information, see [AmazonEC2ContainerServiceforEC2Role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role) in the *Amazon Elastic Container Service Developer Guide* | 
| Amazon ECS on Fargate | Use the task execution IAM role that you reference in your Amazon ECS task definition. For more information, see [Task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*. | `AmazonECSTaskExecutionRolePolicy`<br />For more information, see [AmazonECSTaskExecutionRolePolicy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonECSTaskExecutionRolePolicy) in the *Amazon Elastic Container Service Developer Guide*. | 
| Amazon ECS on external instances | Use the container instance IAM role, which is associated with the on-premises server or virtual machine (VM) registered to your Amazon ECS cluster. For more information, see [Container instance Amazon ECS role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*. | `AmazonEC2ContainerServiceforEC2Role`<br />For more information, see [AmazonEC2ContainerServiceforEC2Role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role) in the *Amazon Elastic Container Service Developer Guide*. | 

**Important**  
The AWS managed IAM policies contain additional permissions that you may not require for your use. In this case, these are the minimum required permissions to pull from an Amazon ECR private repository.  

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        }
    ]
}
```

## Specifying an Amazon ECR image in an Amazon ECS task definition
<a name="ECR_on_ECS_taskdef"></a>

When creating an Amazon ECS task definition, you can specify a container image hosted in an Amazon ECR private repository. In the task definition, ensure that you use the full `registry/repository:tag` naming for your Amazon ECR images. For example, `{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com``/{{my-repository}}:{{latest}}`.

The following task definition snippet shows the syntax you would use to specify a container image hosted in Amazon ECR in your Amazon ECS task definition.

```
{
    "family": "{{task-definition-name}}",
    ...
    "containerDefinitions": [
        {
            "name": "{{container-name}}",
            "image": "{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{my-repository}}:{{latest}}",
            ...
        }
    ],
    ...
}
```