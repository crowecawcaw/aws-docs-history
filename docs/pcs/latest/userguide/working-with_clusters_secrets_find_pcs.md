# Use AWS PCS to find the cluster

secret

You can use the AWS CLI to find the ARN for an AWS PCS cluster secret. Enter the command
that follows, making the following substitutions:

- Replace `region` with the AWS Region to create
  your cluster in, such as `us-east-1`.
- Replace `my-cluster` with the name or identifier
  for your cluster.

```
aws pcs get-cluster --region `region` --cluster-identifier `my-cluster`
```

The following example output is from the `get-cluster` command. You can use
`secretArn` and `secretVersion` together to get the secret.

```
{
    "cluster": {
        "name": "get-started",
        "id": "pcs_123456abcd",
        "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_123456abcd",
        "status": "ACTIVE",
        "createdAt": "2024-12-17T21:03:52+00:00",
        "modifiedAt": "2024-12-17T21:03:52+00:00",
        "scheduler": {
            "type": "SLURM",
            "version": "25.05"
        },
        "size": "SMALL",
        "slurmConfiguration": {
            "authKey": {
                "secretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:pcs!slurm-secret-pcs_123456abcd-a12ABC",
                "secretVersion": "ef232370-d3e7-434c-9a87-ec35c1987f75"
            }
        },
        "networking": {
            "subnetIds": [
                "subnet-0123456789abcdef0"
            ],
            "securityGroupIds": [
                "sg-0123456789abcdef0"
            ]
        },
        "endpoints": [
            {
                "type": "SLURMCTLD",
                "privateIpAddress": "10.3.149.220",
                "port": "6817"
            }
        ]
    }
}

```
