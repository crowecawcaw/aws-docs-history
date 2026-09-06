

# Resource: Compute environment template
<a name="compute-environment-template"></a>

The following example shows an empty compute environment template. You can use this template to create your compute environment that can then be saved to a file and used with the AWS CLI `--cli-input-json` option. For more information about these parameters, see [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) in the *AWS Batch API Reference*.

Before creating a managed Amazon EC2 compute environment, make sure you have the following prerequisites in place. These prerequisites apply when the `type` field is set to `MANAGED`.
+ **Security group** – Your compute resources require a security group that allows outbound traffic so that instances can communicate with the Amazon ECS service endpoint and pull container images. For more information, see [Create a security group](create-a-base-security-group.md).
+ **IAM roles** – AWS Batch requires an Amazon ECS instance role that allows container instances to make AWS API calls on your behalf. For more information, see [Amazon ECS instance role](instance_IAM_role.md) and [Using service-linked roles for AWS Batch](using-service-linked-roles.md).
**Note**  
The `instanceRole` field accepts an instance profile ARN, not a role ARN. The format is `arn:aws:iam::{{account_id}}:instance-profile/{{ecsInstanceRole}}`.
+ **Network access** – Compute resources must be able to reach the Amazon ECS service endpoint. If your instances are in a private subnet without a public IP address, you can use either a NAT gateway or Amazon VPC interface endpoints. For more information, see [Use an interface endpoint to Access AWS Batch](vpc-interface-endpoints.md).

**Note**  
You can generate a compute environment template with the following AWS CLI command.  

```
$ aws batch create-compute-environment --generate-cli-skeleton
```

**Important**  
Compute environments must be created in `ENABLED` state.

The following example shows a skeleton template for a **managed Amazon EC2 compute environment**. The `computeResources` block is required when `type` is `MANAGED`.

```
{
    "computeEnvironmentName": "",
    "type": "MANAGED",
    "state": "ENABLED",
    "computeResources": {
        "type": "EC2",
        "allocationStrategy": "BEST_FIT_PROGRESSIVE",
        "minvCpus": 0,
        "maxvCpus": 16,
        "desiredvCpus": 0,
        "instanceTypes": [
            "default_arm64"
        ],
        "subnets": [
            "{{subnet-a1b2c3d4}}"
        ],
        "securityGroupIds": [
            "{{sg-a1b2c3d4}}"
        ],
        "instanceRole": "arn:aws:iam::{{123456789012}}:instance-profile/{{ecsInstanceRole}}",
        "tags": {
            "KeyName": ""
        },
        "launchTemplate": {
            "launchTemplateId": "",
            "version": "$Default"
        },
        "ec2Configuration": [
            {
                "imageType": "ECS_AL2023"
            }
        ]
    },
    "serviceRole": "",
    "tags": {
        "KeyName": ""
    }
}
```

The following example shows a skeleton template for an **unmanaged Amazon EC2 compute environment**. The `computeResources` block is not used for `UNMANAGED` compute environments and should be omitted.

```
{
    "computeEnvironmentName": "",
    "type": "UNMANAGED",
    "state": "ENABLED",
    "unmanagedvCpus": 0,
    "serviceRole": "",
    "tags": {
        "KeyName": ""
    }
}
```