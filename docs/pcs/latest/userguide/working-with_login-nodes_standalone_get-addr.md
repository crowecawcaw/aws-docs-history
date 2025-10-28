# Step 1 – Retrieve the

address and secret for the target AWS PCS cluster

Retrieve details about the target AWS PCS cluster using the AWS CLI with the command that
follows. Before running the command, make the following replacements:

- Replace `region-code` with the AWS Region where the target
  cluster is running.
- Replace `cluster-ident` with the name or identifier for the
  target cluster

```
aws pcs get-cluster --region `region-code` --cluster-identifier `cluster-ident`
```

The command will return output similar to this example.

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

In this sample, the cluster Slurm controller endpoint has an IP address of
`10.3.149.220` and it is running on port `6817`. The
`secretArn` will be used in later steps to retrieve the cluster secret. The IP
address and port will be used in later steps to configure the `sackd` service.
