# Viewing custom endpoints

To view custom endpoints with the AWS Management Console, go to the cluster detail page for the
cluster and look under the **Endpoints** section. This section
contains information only about custom endpoints. The details for the built-in
endpoints are listed in the main **Details** section. To see the
details for a specific custom endpoint, select its name to bring up the detail page
for that endpoint.

The following screenshot shows how the list of custom endpoints for an Aurora
cluster is initially empty.

![Endpoints page with no custom endpoints.](images/AuroraCustomEndpointEmptyList.png)
After you create some custom endpoints for that cluster, they are shown under the
**Endpoints** section.

![Endpoints page with two custom endpoints.](images/AuroraCustomEndpointList.png)
Clicking through to the detail page shows which DB instances the endpoint is
currently associated with.

![DB instances associated with a custom endpoint.](images/AuroraCustomEndpointDetail.png)
To see the additional detail of whether new DB instances added to the cluster are
automatically added to the endpoint also, open the **Edit** page for
the endpoint.

To view custom endpoints with the AWS CLI, run the [describe-db-cluster-endpoints](../../../cli/latest/reference/rds/describe-db-cluster-endpoints.md "../../../cli/latest/reference/rds/describe-db-cluster-endpoints.md") command.

The following command shows the custom endpoints associated with a specified
cluster in a specified region. The output includes both the built-in endpoints and any
custom endpoints.

For Linux, macOS, or Unix:

```
aws rds describe-db-cluster-endpoints --region `region_name` \
  --db-cluster-identifier `cluster_id`

```

For Windows:

```
aws rds describe-db-cluster-endpoints --region `region_name` ^
  --db-cluster-identifier `cluster_id`

```

The following shows some sample output from a
`describe-db-cluster-endpoints` command. The `EndpointType` of
`WRITER` or `READER` denotes the built-in read/write and
read-only endpoints for the cluster. The `EndpointType` of
`CUSTOM` denotes endpoints that you create and choose the associated DB
instances. One of the endpoints has a non-empty `StaticMembers` field,
denoting that it is associated with a precise set of DB instances. The other endpoint
has a non-empty `ExcludedMembers` field, denoting that the endpoint is
associated with all DB instances _other than_ the ones listed under
`ExcludedMembers`. This second kind of custom endpoint grows to
accommodate new instances as you add them to the cluster.

```
{
	"DBClusterEndpoints": [
		{
			"Endpoint": "custom-endpoint-demo.cluster-c7tj4example.ca-central-1.rds.amazonaws.com",
			"Status": "available",
			"DBClusterIdentifier": "custom-endpoint-demo",
			"EndpointType": "WRITER"
		},
		{
			"Endpoint": "custom-endpoint-demo.cluster-ro-c7tj4example.ca-central-1.rds.amazonaws.com",
			"Status": "available",
			"DBClusterIdentifier": "custom-endpoint-demo",
			"EndpointType": "READER"
		},
		{
			"CustomEndpointType": "ANY",
			"DBClusterEndpointIdentifier": "powers-of-2",
			"ExcludedMembers": [],
			"DBClusterIdentifier": "custom-endpoint-demo",
			"Status": "available",
			"EndpointType": "CUSTOM",
			"Endpoint": "powers-of-2.cluster-custom-c7tj4example.ca-central-1.rds.amazonaws.com",
			"StaticMembers": [
					"custom-endpoint-demo-04",
					"custom-endpoint-demo-08",
					"custom-endpoint-demo-01",
					"custom-endpoint-demo-02"
			],
			"DBClusterEndpointResourceIdentifier": "cluster-endpoint-W7PE3TLLFNSHXQKFU6J6NV5FHU",
			"DBClusterEndpointArn": "arn:aws:rds:ca-central-1:111122223333:cluster-endpoint:powers-of-2"
		},
		{
			"CustomEndpointType": "ANY",
			"DBClusterEndpointIdentifier": "eight-and-higher",
			"ExcludedMembers": [
					"custom-endpoint-demo-04",
					"custom-endpoint-demo-02",
					"custom-endpoint-demo-07",
					"custom-endpoint-demo-05",
					"custom-endpoint-demo-03",
					"custom-endpoint-demo-06",
					"custom-endpoint-demo-01"
			],
			"DBClusterIdentifier": "custom-endpoint-demo",
			"Status": "available",
			"EndpointType": "CUSTOM",
			"Endpoint": "eight-and-higher.cluster-custom-123456789012.ca-central-1.rds.amazonaws.com",
			"StaticMembers": [],
			"DBClusterEndpointResourceIdentifier": "cluster-endpoint-W7PE3TLLFNSHYQKFU6J6NV5FHU",
			"DBClusterEndpointArn": "arn:aws:rds:ca-central-1:111122223333:cluster-endpoint:eight-and-higher"
		}
	]
}

```

To view custom endpoints with the RDS API, run the [DescribeDBClusterEndpoints.html](../APIReference/API_DescribeDBClusterEndpoints.md "../APIReference/API_DescribeDBClusterEndpoints.md") operation.
