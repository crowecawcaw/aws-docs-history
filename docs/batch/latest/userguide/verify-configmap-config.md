# Verify that the `aws-auth ConfigMap` is

configured correctly

To verify that the `aws-auth`
`ConfigMap` is configured correctly:

1. Retrieve the mapped roles in the `aws-auth`
   `ConfigMap`.

```
`$` `kubectl get configmap -n kube-system aws-auth -o yaml`
```

2. Verify that the `roleARN` is configured as follows.

`rolearn:
 arn:aws:iam::`aws_account_number`:role/AWSServiceRoleForBatch`

###### Note

The path `aws-service-role/batch.amazonaws.com/` has been removed from the
ARN of the service-linked role. This is because of an issue with the `aws-auth`
configuration map. For more information, see [Roles with paths
do not work when the path is included in their ARN in the aws-authconfigmap](https://github.com/kubernetes-sigs/aws-iam-authenticator/issues/268 "https://github.com/kubernetes-sigs/aws-iam-authenticator/issues/268").

###### Note

You can also review the Amazon EKS control plane logs. For more information, see [Amazon EKS control plane
logging](../../../eks/latest/userguide/control-plane-logs.md "../../../eks/latest/userguide/control-plane-logs.md") in the _Amazon EKS User Guide_.
To resolve an issue where a job is stuck in a `RUNNABLE` status, we recommend
that you use `kubectl` to re-apply the manifest. For more information, see [Step 2: Prepare your Amazon EKS cluster for
AWS Batch](getting-started-eks.md#getting-started-eks-step-1 "getting-started-eks.md#getting-started-eks-step-1"). Or, you can
use `kubectl` to manually edit the `aws-auth`
`ConfigMap`. For more information, see [Enabling IAM user and role access to your
cluster](../../../eks/latest/userguide/add-user-role.md "../../../eks/latest/userguide/add-user-role.md") in the _Amazon EKS User Guide_.
