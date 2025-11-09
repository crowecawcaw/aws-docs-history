AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Calling the ECS optimized

AMI public parameter in Parameter Store

The Amazon Elastic Container Service (Amazon ECS) service publishes the name of the latest Amazon ECS optimized
Amazon Machine Images (AMIs) as public parameters. Users are encouraged to use this AMI
when creating a new Amazon Elastic Compute Cloud (Amazon EC2) cluster for Amazon ECS because the optimized
AMIs include bug fixes and feature updates.

Use the following command to view the name of the latest Amazon ECS optimized AMI for
Amazon Linux 2. To see commands for other operating systems, see [Retrieving
Amazon ECS-Optimized AMI metadata](../../../AmazonECS/latest/developerguide/retrieve-ecs-optimized_AMI.md "../../../AmazonECS/latest/developerguide/retrieve-ecs-optimized_AMI.md") in the
_Amazon Elastic Container Service Developer Guide_.

Linux & macOS

```
aws ssm get-parameters \
    --names /aws/service/ecs/optimized-ami/amazon-linux-2/recommended
```

Windows

```
aws ssm get-parameters ^
    --names /aws/service/ecs/optimized-ami/amazon-linux-2/recommended
```

The command returns information like the following.

```
{
    "Parameters": [
        {
            "Name": "/aws/service/ecs/optimized-ami/amazon-linux-2/recommended",
            "Type": "String",
            "Value": "{\"schema_version\":1,\"image_name\":\"amzn2-ami-ecs-hvm-2.0.20210929-x86_64-ebs\",\"image_id\":\"ami-0c38a2329ed4dae9a\",\"os\":\"Amazon Linux 2\",\"ecs_runtime_version\":\"Docker version 20.10.7\",\"ecs_agent_version\":\"1.55.4\"}",
            "Version": 73,
            "LastModifiedDate": "2021-10-06T16:35:10.004000-07:00",
            "ARN": "arn:aws:ssm:us-east-2::parameter/aws/service/ecs/optimized-ami/amazon-linux-2/recommended",
            "DataType": "text"
        }
    ],
    "InvalidParameters": []
}
```
