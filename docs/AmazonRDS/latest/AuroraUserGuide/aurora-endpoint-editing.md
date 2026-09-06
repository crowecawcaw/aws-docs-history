

# Editing a custom endpoint
<a name="aurora-endpoint-editing"></a>

You can edit the properties of a custom endpoint to change which DB instances are associated with the endpoint. You can also change an endpoint between a static list and an exclusion list. If you need more details about these endpoint properties, see [Membership rules for custom endpoints](Aurora.Endpoints.Custom.Considerations.md#Aurora.Endpoints.Custom.Membership).

You can continue connecting to and using a custom endpoint while the changes from an edit action are in progress.

## Console
<a name="aurora-edit-endpoint.console"></a>

To edit a custom endpoint with the AWS Management Console, you can select the endpoint on the cluster detail page, or bring up the detail page for the endpoint, and choose the **Edit** action.

![Editing a custom endpoint.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/AuroraEditCustomEndpoint.png)


## AWS CLI
<a name="aurora-edit-endpoint.cli"></a>

To edit a custom endpoint with the AWS CLI, run the [modify-db-cluster-endpoint](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster-endpoint.html) command.

The following commands change the set of DB instances that apply to a custom endpoint and optionally switches between the behavior of a static or exclusion list. The `--static-members` and `--excluded-members` parameters take a space-separated list of DB instance identifiers.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-endpoint --db-cluster-endpoint-identifier {{my-custom-endpoint}} \
  --static-members {{db-instance-id-1}} {{db-instance-id-2}} {{db-instance-id-3}} \
  --region {{region_name}}

aws rds modify-db-cluster-endpoint --db-cluster-endpoint-identifier {{my-custom-endpoint}} \
  --excluded-members {{db-instance-id-4}} {{db-instance-id-5}} \
  --region {{region_name}}
```

For Windows:

```
aws rds modify-db-cluster-endpoint --db-cluster-endpoint-identifier {{my-custom-endpoint}} ^
  --static-members {{db-instance-id-1}} {{db-instance-id-2}} {{db-instance-id-3}} ^
  --region {{region_name}}

aws rds modify-db-cluster-endpoint --db-cluster-endpoint-identifier {{my-custom-endpoint}} ^
  --excluded-members {{db-instance-id-4}} {{db-instance-id-5}} ^
  --region {{region_name}}
```

## RDS API
<a name="aurora-edit-endpoint.api"></a>

To edit a custom endpoint with the RDS API, run the [ModifyDBClusterEndpoint.html](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterEndpoint.html.html) operation.