# Service execution role (SER)

MSK Replicator uses a service execution role (SER) to read from your source cluster and write to your target cluster. You specify this role when creating the Replicator.

You can either let the MSK console create the role automatically, or provide your own IAM role. If you provide your own role, we recommend attaching the [`AWSMSKReplicatorExecutionRole`](security-iam-awsmanpol-AWSMSKReplicatorExecutionRole.md "security-iam-awsmanpol-AWSMSKReplicatorExecutionRole.md") managed IAM policy to it.

The service execution role must have a trust policy that allows the `kafka.amazonaws.com` service principal to assume the role. The following is an example trust policy. Replace `<yourAccountID>` with your actual account ID.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "kafka.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<yourAccountID>"
        }
      }
    }
  ]
}
```

If you want to restrict `kafka-cluster:WriteData` permission, refer to the _Create authorization policies_ section of [How IAM access control for Amazon MSK works](iam-access-control.md#how-to-use-iam-access-control "iam-access-control.md#how-to-use-iam-access-control"). You need to add `kafka-cluster:WriteDataIdempotently` permission to both the source and target cluster.

If you reuse a service execution role between multiple MSK Replicators, they are all subject to the same Kafka quotas. If you want to maintain separate quotas per Replicator, use separate service execution roles.
