# Using AWS CLI

The AWS CLI provides a command-line interface for managing your multi-Region Aurora DSQL clusters. The following examples demonstrate how to create, configure, and delete multi-Region clusters.

## Connect to your multi-Region

cluster

Multi-Region peered clusters provide two regional endpoints, one in each peered cluster
AWS Region. Both endpoints present a single logical database that supports concurrent
read and write operations with strong data consistency. In addition to peered clusters, a multi-Region cluster also has a witness Region that stores a limited window of encrypted transaction logs, which is used to improve multi-Region durability and availability. Multi-Region witness Regions do not have endpoints.

## Create multi-Region clusters

To create multi-Region clusters, you first create a cluster with a witness Region. Then
you peer this cluster with a second cluster that shares the same witness Region as your
first cluster. The following example shows how to create clusters in US East (N. Virginia)
and US East (Ohio) with US West (Oregon) as the witness Region.

### Step 1: Create cluster one in US East (N. Virginia)

To create a cluster in the US East (N. Virginia) AWS Region with multi-Region properties, use
the command below.

```
aws dsql create-cluster \
--region us-east-1 \
--multi-region-properties '{"witnessRegion":"us-west-2"}'
```

###### Example Response:

```
{
    "identifier": "abc0def1baz2quux3quuux4",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abc0def1baz2quux3quuux4",
    "status": "UPDATING",
    "encryptionDetails": {
        "encryptionType": "AWS_OWNED_KMS_KEY",
        "encryptionStatus": "ENABLED"
   }
   "creationTime": "2024-05-24T09:15:32.708000-07:00"
}
```

###### Note

When the API operation succeeds, the cluster enters the `PENDING_SETUP`
state. Cluster creation remains in the `PENDING_SETUP` until you
update the cluster with the ARN of its peer cluster.

### Step 2: Create cluster two in US East (Ohio)

To create a cluster in the US East (Ohio) AWS Region with multi-Region properties, use
the command below.

```
aws dsql create-cluster \
--region us-east-2 \
--multi-region-properties '{"witnessRegion":"us-west-2"}'
```

###### Example Response:

```
{
    "identifier": "foo0bar1baz2quux3quuxquux5",
    "arn": "arn:aws:dsql:us-east-2:111122223333:cluster/foo0bar1baz2quux3quuxquux5",
    "status": "PENDING_SETUP",
    "creationTime": "2025-05-06T06:51:16.145000-07:00",
    "deletionProtectionEnabled": true,
    "multiRegionProperties": {
        "witnessRegion": "us-west-2",
        "clusters": [
            "arn:aws:dsql:us-east-2:111122223333:cluster/foo0bar1baz2quux3quuxquux5"
        ]
    }
}
```

When the API operation succeeds, the cluster transitions to `PENDING_SETUP`
state. The cluster creation remains in the `PENDING_SETUP` state until
you update it with the ARN of another cluster for peering.

### Step 3: Peer cluster in US East (N. Virginia) with US East (Ohio)

To peer your US East (N. Virginia) cluster with your US East (Ohio) cluster, use the
`update-cluster` command. Specify your US East (N. Virginia) cluster name and a
JSON string with the ARN of the US East (Ohio) cluster.

```
aws dsql update-cluster \
--region us-east-1 \
--identifier 'foo0bar1baz2quux3quuxquux4' \
--multi-region-properties '{"witnessRegion": "us-west-2","clusters": ["arn:aws:dsql:us-east-2:111122223333:cluster/foo0bar1baz2quux3quuxquux5"]}'
```

###### Example Response

```
{
    "identifier": "foo0bar1baz2quux3quuxquux4",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/foo0bar1baz2quux3quuxquux4",
    "status": "UPDATING",
    "creationTime": "2025-05-06T06:46:10.745000-07:00"
}
```

### Step 4: Peer cluster in US East (Ohio) with

US East (N. Virginia)

To peer your US East (Ohio) cluster with your US East (N. Virginia) cluster, use the
`update-cluster` command. Specify your US East (Ohio) cluster name and a
JSON string with the ARN of the US East (N. Virginia) cluster.

###### Example

```
aws dsql update-cluster \
--region us-east-2 \
--identifier 'foo0bar1baz2quux3quuxquux5' \
--multi-region-properties '{"witnessRegion": "us-west-2", "clusters": ["arn:aws:dsql:us-east-1:111122223333:cluster/foo0bar1baz2quux3quuxquux4"]}'
```

###### Example Response

```
{
    "identifier": "foo0bar1baz2quux3quuxquux5",
    "arn": "arn:aws:dsql:us-east-2:111122223333:cluster/foo0bar1baz2quux3quuxquux5",
    "status": "UPDATING",
    "creationTime": "2025-05-06T06:51:16.145000-07:00"
}
```

###### Note

After successful peering, both clusters transition from "PENDING_SETUP" to
"CREATING" and finally to "ACTIVE" status when ready for use.

#### View multi-Region cluster

properties

When you describe a cluster, you can view multi-Region properties for clusters
in different AWS Regions.

###### Example

```
aws dsql get-cluster \
--region us-east-1 \
--identifier 'foo0bar1baz2quux3quuxquux4'
```

###### Example Response

```
{
    "identifier": "foo0bar1baz2quux3quuxquux4",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/foo0bar1baz2quux3quuxquux4",
    "status": "PENDING_SETUP",
    "encryptionDetails": {
    "encryptionType": "AWS_OWNED_KMS_KEY",
    "encryptionStatus": "ENABLED"
},
    "creationTime": "2024-11-27T00:32:14.434000-08:00",
    "deletionProtectionEnabled": false,
    "multiRegionProperties": {
       "witnessRegion": "us-west-2",
       "clusters": [
          "arn:aws:dsql:us-east-1:111122223333:cluster/foo0bar1baz2quux3quuxquux4",
          "arn:aws:dsql:us-east-2:111122223333:cluster/foo0bar1baz2quux3quuxquux5"
       ]
    }
}
```

#### Peer clusters during creation

You can reduce the number of steps by including peering information during cluster creation. After creating your first cluster in US East (N. Virginia) (Step 1), you can create your second cluster in US East (Ohio) while simultaneously initiating the peering process by including the ARN of the first cluster.

###### Example

```
aws dsql create-cluster \
--region us-east-2 \
--multi-region-properties '{"witnessRegion":"us-west-2","clusters": ["arn:aws:dsql:us-east-1:111122223333:cluster/foo0bar1baz2quux3quuxquux4"]}'
```

This combines Steps 2 and 4, but you still need to complete Step 3 (updating the first cluster with the ARN of the second cluster) to establish the peering relationship. After all steps are completed, both clusters will transition through the same states as in the standard process: from **PENDING_SETUP** to **CREATING**, and finally to **ACTIVE** when ready for use.

## Delete multi-Region clusters

To delete a multi-Region cluster, you need to complete two steps.

1. Turn off deletion protection for each cluster.
2. Delete each peered cluster separately in their respective AWS Region

### Update and delete cluster in US East (N. Virginia)

1. Turn off deletion protection using the `update-cluster`
   command.

```
aws dsql update-cluster \
  --region us-east-1 \
  --identifier 'foo0bar1baz2quux3quuxquux4' \
  --no-deletion-protection-enabled
```

2. Delete the cluster using the `delete-cluster` command.

```
aws dsql delete-cluster \
  --region us-east-1 \
  --identifier 'foo0bar1baz2quux3quuxquux4'
```

The command returns the following response.

```
{
    "identifier": "foo0bar1baz2quux3quuxquux4",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/foo0bar1baz2quux3quuxquux4",
    "status": "PENDING_DELETE",
    "creationTime": "2025-05-06T06:46:10.745000-07:00"
}
```

###### Note

The cluster transitions to `PENDING_DELETE` status. The deletion isn't complete until you delete the peered cluster in US East (Ohio).

### Update and delete cluster in

US East (Ohio)

1. Turn off deletion protection using the `update-cluster`
   command.

```
aws dsql update-cluster \
--region us-east-2 \
--identifier 'foo0bar1baz2quux3quux4quuux' \
--no-deletion-protection-enabled
```

2. Delete the cluster using the `delete-cluster` command.

```
aws dsql delete-cluster \
--region us-east-2 \
--identifier 'foo0bar1baz2quux3quuxquux5'
```

The command returns the following response:

```
{
    "identifier": "foo0bar1baz2quux3quuxquux5",
    "arn": "arn:aws:dsql:us-east-2:111122223333:cluster/foo0bar1baz2quux3quuxquux5",
    "status": "PENDING_DELETE",
    "creationTime": "2025-05-06T06:46:10.745000-07:00"
}
```

###### Note

The cluster transitions to `PENDING_DELETE` status. After a
few seconds, the system automatically transitions both peered clusters
to `DELETING` status after validation.
