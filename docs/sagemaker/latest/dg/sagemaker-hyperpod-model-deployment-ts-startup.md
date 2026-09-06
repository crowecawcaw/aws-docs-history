

# Inference operator fails to start
<a name="sagemaker-hyperpod-model-deployment-ts-startup"></a>

Inference operator pod failed to start and is causing the following error message. This error is due to permission policy on the operator execution role not being authorized to perform `sts:AssumeRoleWithWebIdentity`. Due to this, the operator part running on the control plane is not started.

**Error message:**

```
Warning Unhealthy 5m46s (x22 over 49m) kubelet Startup probe failed: Get "http://10.1.100.59:8081/healthz": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
```

**Root cause:**
+ Permission policy of the inference operator execution role is not set to access authorization token for resources.

**Resolution:**

Set the following policy of the execution role of `EXECUTION_ROLE_ARN` for the HyperPod inference operator:

```
HyperpodInferenceAccessPolicy-ml-cluster to include all resources
```

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        }
    ]
}
```

------

**Verification steps:**

1. Change the policy.

1. Terminate the HyperPod inference operator pod.

1. The pod will be restarted without throwing any exceptions.