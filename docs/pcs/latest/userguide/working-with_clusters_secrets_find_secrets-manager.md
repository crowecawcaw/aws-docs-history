# Use AWS Secrets Manager to find the

cluster secret

AWS Management Console

1. Navigate to the [Secrets Manager
   console](https://console.aws.amazon.com/secretsmanager "https://console.aws.amazon.com/secretsmanager").
2. Choose **Secrets**, then search for the `pcs!`
   prefix.

###### Note

A AWS PCS cluster secret has a name in the form
`pcs!slurm-secret-`cluster-id`where
`cluster-id`` is the AWS PCS cluster ID.

AWS CLI
Each AWS PCS cluster secret is also tagged with
`aws:pcs:`cluster-id``. You can get the secret ID for a
cluster with the command that follows. Make these substitutions before running the
command:

- Replace `region` with the AWS Region to create
  your cluster in, such as `us-east-1`.
- Replace `cluster-id` with the ID of the
  AWS PCS cluster to find the cluster secret for.

```
aws secretsmanager list-secrets \
    --region `region`  \
    --filters Key=tag-key,Values=aws:pcs:`cluster-id` \
            Key=tag-value,Values=`cluster-id`
```
