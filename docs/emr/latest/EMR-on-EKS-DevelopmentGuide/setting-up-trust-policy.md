# Update the trust policy of the job execution

role

When you use IAM Roles for Service Accounts (IRSA) to run jobs on a Kubernetes namespace,
an administrator must create a trust relationship between the job execution role and the
identity of the EMR managed service account. The trust relationship can be created by updating
the trust policy of the job execution role. Note that the EMR managed service account is
automatically created at job submission, scoped to the namespace where the job is
submitted.

Run the following command to update the trust policy.

```
 aws emr-containers update-role-trust-policy \
       --cluster-name `cluster` \
       --namespace `namespace` \
       --role-name `iam_role_name_for_job_execution`
```

For more information, see [Using job execution roles with Amazon EMR on EKS](iam-execution-role.md "iam-execution-role.md").

###### Important

The operator running the above command must have these permissions:
`eks:DescribeCluster`, `iam:GetRole`,
`iam:UpdateAssumeRolePolicy`.
