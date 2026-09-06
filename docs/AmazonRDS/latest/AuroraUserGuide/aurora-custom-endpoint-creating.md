

# Creating a custom endpoint
<a name="aurora-custom-endpoint-creating"></a>

Create a custom endpoint using the AWS Management Console, AWS CLI, or the Amazon RDS API.

## Console
<a name="aurora-create-endpoint.console"></a>

To create a custom endpoint with the AWS Management Console, go to the cluster detail page and choose the `Create custom endpoint` action in the **Endpoints** section. Choose a name for the custom endpoint, unique for your user ID and region. To choose a list of DB instances that remains the same even as the cluster expands, keep the check box **Attach future instances added to this cluster** clear. When you choose that check box, the custom endpoint dynamically adds any new instances as you add them to the cluster.

![Create custom endpoint page with fields for endpoint identifier, instance type selection, and static or exclusion options.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/AuroraCreateCustomEndpoint.png)


You can't select the custom endpoint type in the AWS Management Console. All custom endpoints you create through the AWS Management Console have a type of `ANY`.

## AWS CLI
<a name="aurora-create-endpoint.cli"></a>

To create a custom endpoint with the AWS CLI, run the [create-db-cluster-endpoint](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster-endpoint.html) command.

The following command creates a custom endpoint attached to a specific cluster. Initially, the endpoint is associated with all the Aurora Replica instances in the cluster. A subsequent command associates it with a specific set of DB instances in the cluster.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster-endpoint --db-cluster-endpoint-identifier custom-endpoint-doc-sample \
  --endpoint-type reader \
  --db-cluster-identifier {{cluster_id}}

aws rds modify-db-cluster-endpoint --db-cluster-endpoint-identifier custom-endpoint-doc-sample \
  --static-members {{instance_name_1}} {{instance_name_2}}
```

For Windows:

```
aws rds create-db-cluster-endpoint --db-cluster-endpoint-identifier custom-endpoint-doc-sample ^
  --endpoint-type reader ^
  --db-cluster-identifier {{cluster_id}}

aws rds modify-db-cluster-endpoint --db-cluster-endpoint-identifier custom-endpoint-doc-sample ^
  --static-members {{instance_name_1}} {{instance_name_2}}
```

## RDS API
<a name="aurora-create-endpoint.api"></a>

To create a custom endpoint with the RDS API, run the [CreateDBClusterEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBClusterEndpoint.html) operation.