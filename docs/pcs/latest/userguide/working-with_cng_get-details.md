# Get compute node group details in

AWS PCS

You can use the AWS Management Console or AWS CLI to get details about a compute node group, such as its
compute node group ID, Amazon Resource Name (ARN), and Amazon Machine Image (AMI) ID. These
details are often required values for AWS PCS API actions and configurations.

AWS Management Console

###### To get compute node group details

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters").
2. Select the cluster.
3. Choose **Compute node groups**.
4. Choose a compute node group from the list pane.

AWS CLI

###### To get compute node group details

1. Use the [ListClusters](../APIReference/API_ListClusters.md "../APIReference/API_ListClusters.md")
   API action to find your cluster name or ID.

```
aws pcs list-clusters
```

**Example output:**

```
{
    "clusters": [
        {
            **"name": "get-started-cfn",
 "id": "pcs\_abc1234567",**
            "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_abc1234567",
            "createdAt": "2025-04-01T20:11:22+00:00",
            "modifiedAt": "2025-04-01T20:11:22+00:00",
            "status": "ACTIVE"
        }
    ]
}
```

2. Use the [ListComputeNodeGroups](../APIReference/API_ListComputeNodeGroups.md "../APIReference/API_ListComputeNodeGroups.md")
   API action to list the compute node groups in a cluster.

```
aws pcs list-compute-node-groups --cluster-identifier `cluster-name-or-id`
```

**Example call:**

```
aws pcs list-compute-node-groups --cluster-identifier get-started-cfn
```

**Example output:**

```
{
    "computeNodeGroups": [
        {
            "name": "compute-1",
            "id": "pcs_abc123abc1",
            "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_abc1234567/computenodegroup/pcs_abc123abc1",
            "clusterId": "pcs_abc1234567",
            "createdAt": "2025-04-01T20:19:25+00:00",
            "modifiedAt": "2025-04-01T20:19:25+00:00",
            "status": "ACTIVE"
        },
        {
            "name": "login",
            "id": "pcs_abc456abc7",
            "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_abc1234567/computenodegroup/pcs_abc456abc7",
            "clusterId": "pcs_abc1234567",
            "createdAt": "2025-04-01T20:19:31+00:00",
            "modifiedAt": "2025-04-01T20:19:31+00:00",
            "status": "ACTIVE"
        }
    ]
}
```

3. Use the [GetComputeNodeGroup](../APIReference/API_GetComputeNodeGroup.md "../APIReference/API_GetComputeNodeGroup.md")
   API action to get additional details for a compute node group.

```
aws pcs get-compute-node-group --cluster-identifier `cluster-name-or-id` --compute-node-group-identifier `compute-node-group-name-or-id`
```

**Example call:**

```
aws pcs get-compute-node-group --cluster-identifier get-started-cfn --compute-node-group-identifier compute-1
```

**Example output:**

```
{
    "computeNodeGroup": {
        "name": "compute-1",
        "id": "pcs_abc123abc1",
        "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_abc1234567/computenodegroup/pcs_abc123abc1",
        "clusterId": "pcs_abc1234567",
        "createdAt": "2025-04-01T20:19:25+00:00",
        "modifiedAt": "2025-04-01T20:19:25+00:00",
        "status": "ACTIVE",
        "amiId": "ami-0123456789abcdef0",
        "subnetIds": [
            "subnet-abc012345789abc12"
        ],
        "purchaseOption": "ONDEMAND",
        "customLaunchTemplate": {
            "id": "lt-012345abcdef01234",
            "version": "1"
        },
        "iamInstanceProfileArn": "arn:aws:iam::111122223333:instance-profile/AWSPCS-get-started-cfn-us-east-1",
        "scalingConfiguration": {
            "minInstanceCount": 0,
            "maxInstanceCount": 4
        },
        "instanceConfigs": [
            {
                "instanceType": "c6i.xlarge"
            }
        ]
    }
}
```
