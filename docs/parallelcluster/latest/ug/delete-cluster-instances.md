# deleteClusterInstances

Initiate the forced termination of all cluster compute nodes. This action doesn't support AWS Batch clusters.

###### Topics

- [Request syntax](#delete-cluster-instances-request "#delete-cluster-instances-request")
- [Request body](#delete-cluster-instances-request-body "#delete-cluster-instances-request-body")
- [Response body](#delete-cluster-instances-response-body "#delete-cluster-instances-response-body")
- [Example](#delete-cluster-instances-example "#delete-cluster-instances-example")

## Request syntax

```
DELETE /v3/clusters/{`clusterName`}/instances
{
  "force": boolean,
  "region": "string"
}
```

## Request body

**clusterName**

The name of the cluster.

Type: string

Required: Yes

**force**

If set to `true`, force the deletion when the cluster with the given name isn't found. The default is
`false`.

Type: boolean

Required: No

**region**

The AWS Region that the cluster is in.

Type: string

Required: No

## Response body

None

## Example

Python
Request

```
`$` `delete_cluster_instances(`cluster_name_3x`)`
```

200 Response

None
