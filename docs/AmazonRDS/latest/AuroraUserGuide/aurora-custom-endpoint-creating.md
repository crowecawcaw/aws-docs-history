# Creating a custom endpoint

Create a custom endpoint using the AWS Management Console, AWS CLI, or the Amazon RDS API.

To create a custom endpoint with the AWS Management Console, go to the cluster detail page and
choose the `Create custom endpoint` action in the
**Endpoints** section. Choose a name for the custom endpoint,
unique for your user ID and region. To choose a list of DB instances that remains the
same even as the cluster expands, keep the check box **Attach future instances
added to this cluster** clear. When you choose that check box, the custom
endpoint dynamically adds any new instances as you add them to the cluster.

![Create custom endpoint page with fields for endpoint identifier, instance type selection, and static/exclusion options.](images/AuroraCreateCustomEndpoint.png)
You can't select the custom endpoint type in the AWS Management Console. All custom
endpoints you create through the AWS Management Console have a type of `ANY`.

To create a custom endpoint with the AWS CLI, run the [create-db-cluster-endpoint](../../../cli/latest/reference/rds/create-db-cluster-endpoint.md "../../../cli/latest/reference/rds/create-db-cluster-endpoint.md") command.

The following command creates a custom endpoint attached to a specific cluster.
Initially, the endpoint is associated with all the Aurora Replica instances in the
cluster. A subsequent command associates it with a specific set of DB instances in the
cluster.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster-endpoint --db-cluster-endpoint-identifier custom-endpoint-doc-sample \
  --endpoint-type reader \
  --db-cluster-identifier `cluster_id`

aws rds modify-db-cluster-endpoint --db-cluster-endpoint-identifier custom-endpoint-doc-sample \
  --static-members `instance_name_1` `instance_name_2`

```

For Windows:

```
aws rds create-db-cluster-endpoint --db-cluster-endpoint-identifier custom-endpoint-doc-sample ^
  --endpoint-type reader ^
  --db-cluster-identifier `cluster_id`

aws rds modify-db-cluster-endpoint --db-cluster-endpoint-identifier custom-endpoint-doc-sample ^
  --static-members `instance_name_1` `instance_name_2`

```

To create a custom endpoint with the RDS API, run the [CreateDBClusterEndpoint](../APIReference/API_CreateDBClusterEndpoint.md "../APIReference/API_CreateDBClusterEndpoint.md")
operation.
