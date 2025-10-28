# Considerations for custom endpoints

in Amazon Aurora

Use the following sections to manage, specify properties, and use membership rules for
custom endpoints.

###### Topics

- [Managing custom endpoints](#Aurora.Endpoints.Custom.Managing "#Aurora.Endpoints.Custom.Managing")
- [Specifying properties for custom
  endpoints](#Aurora.Endpoints.Custom.Properties "#Aurora.Endpoints.Custom.Properties")
- [Membership rules for custom
  endpoints](#Aurora.Endpoints.Custom.Membership "#Aurora.Endpoints.Custom.Membership")

## Managing custom endpoints

Because newly created Aurora clusters have no custom endpoints, you must create and
manage these objects yourself. You do so using the AWS Management Console, AWS CLI, or Amazon RDS
API.

###### Note

You must also create and manage custom endpoints for Aurora clusters restored from
snapshots. Custom endpoints are not included in the snapshot. You create them again
after restoring, and choose new endpoint names if the restored cluster is in the same
region as the original one.

To work with custom endpoints from the AWS Management Console, you navigate to the details page
for your Aurora cluster and use the controls under the **Custom
Endpoints** section.

To work with custom endpoints from the AWS CLI, you can use these operations:

- [create-db-cluster-endpoint](../../../cli/latest/reference/rds/create-db-cluster-endpoint.md "../../../cli/latest/reference/rds/create-db-cluster-endpoint.md")
- [describe-db-cluster-endpoints](../../../cli/latest/reference/rds/describe-db-cluster-endpoints.md "../../../cli/latest/reference/rds/describe-db-cluster-endpoints.md")
- [modify-db-cluster-endpoint](../../../cli/latest/reference/rds/modify-db-cluster-endpoint.md "../../../cli/latest/reference/rds/modify-db-cluster-endpoint.md")
- [delete-db-cluster-endpoint](../../../cli/latest/reference/rds/delete-db-cluster-endpoint.md "../../../cli/latest/reference/rds/delete-db-cluster-endpoint.md")

To work with custom endpoints through the Amazon RDS API, you can use the following
functions:

- [CreateDBClusterEndpoint](../APIReference/API_CreateDBClusterEndpoint.md "../APIReference/API_CreateDBClusterEndpoint.md")
- [DescribeDBClusterEndpoints](../APIReference/API_DescribeDBClusterEndpoints.md "../APIReference/API_DescribeDBClusterEndpoints.md")
- [ModifyDBClusterEndpoint](../APIReference/API_ModifyDBClusterEndpoint.md "../APIReference/API_ModifyDBClusterEndpoint.md")
- [DeleteDBClusterEndpoint](../APIReference/API_DeleteDBClusterEndpoint.md "../APIReference/API_DeleteDBClusterEndpoint.md")

## Specifying properties for custom

endpoints

The maximum length for a custom endpoint name is 63 characters. The name format is
the following:

```
`endpoint_name`.cluster-custom-`customer_DNS_identifier`.`AWS_Region`.rds.amazonaws.com
```

You can't reuse the same custom endpoint name for more than one cluster in the
same AWS Region. The custom DNS identifier is a unique identifier associated with
your AWS account in a particular AWS Region.

Each custom endpoint has an associated type that determines which DB instances are
eligible to be associated with that endpoint. Currently, the type can be
`READER` or `ANY`. The following considerations apply to the
custom endpoint types:

- You can't select the custom endpoint type in the AWS Management Console. All the custom
  endpoints you create through the AWS Management Console have a type of `ANY`.

You can set and modify the custom endpoint type using the AWS CLI or Amazon RDS
API.

- Only reader DB instances can be part of a `READER` custom
  endpoint.
- Both reader and writer DB instances can be part of an `ANY` custom
  endpoint. Aurora directs connections to cluster endpoints with type `ANY`
  to any associated DB instance with equal probability. The `ANY` type
  applies to clusters using any replication topology.
- If you try to create a custom endpoint with a type that isn't appropriate based
  on the replication configuration for a cluster, Aurora returns an error.

## Membership rules for custom

endpoints

When you add a DB instance to a custom endpoint or remove it from a custom
endpoint, any existing connections to that DB instance remain active.

You can define a list of DB instances to include in, or exclude from, a custom
endpoint. We refer to these lists as _static_ and
_exclusion_ lists, respectively. You can use the
inclusion/exclusion mechanism to further subdivide the groups of DB instances, and to
make sure that the set of custom endpoints covers all the DB instances in the cluster.
Each custom endpoint can contain only one of these list types.

In the AWS Management Console:

- The choice is represented by the check box **Attach future instances
  added to this cluster**. When you keep the check box clear, the custom
  endpoint uses a static list containing only the DB instances specified on the page.
  When you choose the check box, the custom endpoint uses an exclusion list. In this
  case, the custom endpoint represents all DB instances in the cluster (including any
  that you add in the future) except the ones not selected on the page.
- The console doesn't allow you to specify the endpoint type. Any custom endpoint
  created using the console is of type `ANY`.

Therefore, Aurora doesn't change the membership of the custom endpoint when DB
instances change roles between writer and reader due to failover or
promotion.

In the AWS CLI and Amazon RDS API:

- You can specify the endpoint type. Therefore, when the endpoint type is set to
  `READER`, endpoint membership is automatically adjusted during
  failovers and promotions.

For example, a custom endpoint with type `READER` includes an Aurora
Replica that is then promoted to be a writer DB instance. The new writer instance is
no longer part of the custom endpoint.

- You can add individual members to and remove them from the lists after they
  change their roles. Use the [modify-db-cluster-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-endpoint.html") AWS CLI command or [ModifyDBClusterEndpoint](../APIReference/API_ModifyDBClusterEndpoint.md "../APIReference/API_ModifyDBClusterEndpoint.md") API operation.

You can associate a DB instance with more than one custom endpoint. For example,
suppose that you add a new DB instance to a cluster, or that Aurora adds a DB instance
automatically through the autoscaling mechanism. In these cases, the DB instance is
added to all custom endpoints for which it is eligible. Which endpoints the DB instance
is added to is based on the custom endpoint type of `READER` or
`ANY`, plus any static or exclusion lists defined for each endpoint. For
example, if the endpoint includes a static list of DB instances, newly added Aurora
Replicas aren't added to that endpoint. Conversely, if the endpoint has an exclusion
list, newly added Aurora Replicas are added to the endpoint, if they aren't named in the
exclusion list and their roles match the type of the custom endpoint.

If an Aurora Replica becomes unavailable, it remains associated with any custom
endpoints. For example, it remains part of the custom endpoint when it is unhealthy,
stopped, rebooting, and so on. However, you can't connect to it through those
endpoints until it becomes available again.
