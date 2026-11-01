

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Required permissions
<a name="tutorial-create-ami-terraform-permissions"></a>

You need the following permissions to deploy a custom AMI with Terraform:
+ assume the ParallelCluster API role, which is in charge of interacting with the ParallelCluster API
+ describe the CloudFormation stack of the ParallelCluster API, to verify it exists and retrieve its parameters and outputs

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:sts::{{111122223333}}:role/PCAPIUserRole-*",
            "Effect": "Allow",
            "Sid": "AssumePCAPIUserRole"
        },
        {
            "Action": [
                "cloudformation:DescribeStacks"
            ],
            "Resource": "arn:aws:cloudformation:{{us-east-1}}:{{111122223333}}:stack/*",
            "Effect": "Allow",
            "Sid": "CloudFormation"
        }
    ]
}
```

------