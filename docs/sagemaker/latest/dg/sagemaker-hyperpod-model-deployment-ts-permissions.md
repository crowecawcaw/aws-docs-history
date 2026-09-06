

# VPC ENI permission issue
<a name="sagemaker-hyperpod-model-deployment-ts-permissions"></a>

SageMaker AI endpoint creation fails due to insufficient permissions for creating network interfaces in VPC.

**Error message:**

```
Please ensure that the execution role for variant AllTraffic has sufficient permissions for creating an endpoint variant within a VPC
```

**Root cause:**

The inference operator's execution role lacks the required Amazon EC2 permission to create network interfaces (ENI) in VPC.

**Resolution:**

Add the following IAM permission to the inference operator's execution role:

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterfacePermission"
     ],
    "Resource": "*"
}
```

**Verification:**

After adding the permission:

1. Delete the failed endpoint (if exists)

1. Retry the endpoint creation

1. Monitor the deployment status for successful completion

**Note**  
This permission is essential for SageMaker AI endpoints running in VPC mode. Ensure the execution role has all other necessary VPC-related permissions as well.