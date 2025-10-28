# Using AWS CLI

The AWS CLI provides a command-line interface for managing your Aurora DSQL clusters. The following examples demonstrate common cluster management operations.

## Create cluster

Create a cluster using the **create-cluster** command.

###### Note

Cluster creation is an asynchronous operation. Call the **GetCluster** API until the status changes to `ACTIVE`. You can connect to your cluster after it becomes active.

###### Example Command

```
aws dsql create-cluster --region us-east-1
```

###### Note

To disable deletion protection during creation, include the `--no-deletion-protection-enabled` flag.

###### Example Response

```
{
    "identifier": "abc0def1baz2quux3quuux4",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abc0def1baz2quux3quuux4",
    "status": "CREATING",
    "creationTime": "2024-05-25T16:56:49.784000-07:00",
    "deletionProtectionEnabled": true,
    "tag": {},
    "encryptionDetails": {
        "encryptionType": "AWS_OWNED_KMS_KEY",
        "encryptionStatus": "ENABLED"
    }
}
```

## Describing a cluster

Get information about a cluster using the **get-cluster** command.

###### Example Command

```
aws dsql get-cluster \
  --region us-east-1 \
  --identifier `your_cluster_id`
```

###### Example Response

```
{
    "identifier": "abc0def1baz2quux3quuux4",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abc0def1baz2quux3quuux4",
    "status": "ACTIVE",
    "creationTime": "2024-11-27T00:32:14.434000-08:00",
    "deletionProtectionEnabled": false,
    "encryptionDetails": {
        "encryptionType": "CUSTOMER_MANAGED_KMS_KEY",
        "kmsKeyArn": "arn:aws:kms:us-east-1:111122223333:key/123a456b-c789-01de-2f34-g5hi6j7k8lm9",
        "encryptionStatus": "ENABLED"
    }
}
```

## Updating a cluster

Update an existing cluster using the **update-cluster** command.

###### Note

Updates are asynchronous operations. Call the **GetCluster** API until the status changes to `ACTIVE` to see your changes.

###### Example Command

```
aws dsql update-cluster \
  --region us-east-1 \
  --no-deletion-protection-enabled \
  --identifier `your_cluster_id`
```

###### Example Response

```
{
    "identifier": "abc0def1baz2quux3quuux4",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abc0def1baz2quux3quuux4",
    "status": "UPDATING",
    "creationTime": "2024-05-24T09:15:32.708000-07:00"
}
```

## Deleting a cluster

Delete an existing cluster using the **delete-cluster** command.

###### Note

You can only delete clusters that have deletion protection disabled. By default, deletion protection is enabled when you create new clusters.

###### Example Command

```
aws dsql delete-cluster \
  --region us-east-1 \
  --identifier `your_cluster_id`
```

###### Example Response

```
{
    "identifier": "abc0def1baz2quux3quuux4",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abc0def1baz2quux3quuux4",
    "status": "DELETING",
    "creationTime": "2024-05-24T09:16:43.778000-07:00"
}
```

## Listing clusters

List your clusters using the **list-clusters** command.

###### Example Command

```
aws dsql list-clusters --region us-east-1
```

###### Example Response

```
{
    "clusters": [
        {
            "identifier": "abc0def1baz2quux3quux4quuux",
            "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abc0def1baz2quux3quux4quuux"
        },
        {
            "identifier": "abc0def1baz2quux3quux5quuuux",
            "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abc0def1baz2quux3quux5quuuux"
        }
    ]
}
```
