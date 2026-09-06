

# IAM trust relationship issue
<a name="sagemaker-hyperpod-model-deployment-ts-trust"></a>

HyperPod inference operator fails to start with an STS AssumeRoleWithWebIdentity error, indicating an IAM trust relationship configuration problem.

**Error message:**

```
failed to enable inference watcher for HyperPod cluster *****: operation error SageMaker: UpdateClusterInference, 
get identity: get credentials: failed to refresh cached credentials, failed to retrieve credentials, 
operation error STS: AssumeRoleWithWebIdentity, https response error StatusCode: 403, RequestID: ****, 
api error AccessDenied: Not authorized to perform sts:AssumeRoleWithWebIdentity
```

**Resolution:**

Update the trust relationship of the inference operator's IAM execution role with the following configuration.

Replace the following placeholders:
+ `<ACCOUNT_ID>`: Your AWS account ID
+ `<REGION>`: Your AWS region
+ `<OIDC_ID>`: Your Amazon EKS cluster's OIDC provider ID

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
            "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/oidc.eks.<REGION>.amazonaws.com/id/<OIDC_ID>"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "oidc.eks.<REGION>.amazonaws.com/id/<OIDC_ID>:sub": "system:serviceaccount:<namespace>:<service-account-name>",
                    "oidc.eks.<REGION>.amazonaws.com/id/<OIDC_ID>:aud": "sts.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "sagemaker.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**Verification:**

After updating the trust relationship:

1. Verify the role configuration in IAM console

1. Restart the inference operator if necessary

1. Monitor operator logs for successful startup