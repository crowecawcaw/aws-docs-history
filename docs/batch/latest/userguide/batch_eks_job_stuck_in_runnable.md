

# AWS Batch on Amazon EKS job is stuck in `RUNNABLE` status
<a name="batch_eks_job_stuck_in_runnable"></a>

An `aws-auth` `ConfigMap` is automatically created and applied to your cluster when you create a managed node group or a node group using `eksctl`. An `aws-auth` `ConfigMap` is initially created to allow nodes to join your cluster. However, you also use the `aws-auth``ConfigMap` to add role-based access control (RBAC) access to users and roles.

To verify that the `aws-auth` `ConfigMap` is configured correctly:

1. Retrieve the mapped roles in the `aws-auth` `ConfigMap`:

   ```
   $ kubectl get configmap -n kube-system aws-auth -o yaml
   ```

1. Verify that the `roleARN` is configured as follows.

   `rolearn: arn:aws:iam::{{aws_account_number}}:role/AWSServiceRoleForBatch`
**Note**  
You can also review the Amazon EKS control plane logs. For more information, see [Amazon EKS control plane logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the *Amazon EKS User Guide*.

To resolve an issue where a job is stuck in a `RUNNABLE` status, we recommend that you use `kubectl` to re-apply the manifest. For more information, see [Step 2: Prepare your Amazon EKS cluster for AWS Batch](getting-started-eks.md#getting-started-eks-step-1). Or, you can use `kubectl` to manually edit the `aws-auth` `ConfigMap`. For more information, see [Enabling IAM user and role access to your cluster](https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html) in the *Amazon EKS User Guide*.