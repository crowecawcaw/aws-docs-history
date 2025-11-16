# Listing DB cluster parameter groups

You can list the DB cluster parameter groups you've created for your AWS account.

###### Note

Default parameter groups are automatically created from a default parameter template when
you create a DB cluster for a particular DB engine and version. These default
parameter groups contain preferred parameter settings and can't be modified. When
you create a custom parameter group, you can modify parameter settings.

###### To list all DB cluster parameter groups for an AWS account

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.

The DB cluster parameter groups appear in the list with **DB cluster parameter group** for **Type**.
To list all DB cluster parameter groups for an AWS account, use the AWS CLI [`describe-db-cluster-parameter-groups`](../../../cli/latest/reference/rds/describe-db-clusterparameter-groups.md "../../../cli/latest/reference/rds/describe-db-clusterparameter-groups.md") command.

###### Example

The following example lists all available DB cluster parameter groups for an AWS account.

```
aws rds describe-db-cluster-parameter-groups
```

The following example describes the _mydbclusterparametergroup_ parameter group.

For Linux, macOS, or Unix:

```
aws rds describe-db-cluster-parameter-groups \
    --db-cluster-parameter-group-name `mydbclusterparametergroup`
```

For Windows:

```
aws rds describe-db-cluster-parameter-groups ^
    --db-cluster-parameter-group-name `mydbclusterparametergroup`
```

The command returns a response like the following:

```
{
    "DBClusterParameterGroups": [
        {
            "DBClusterParameterGroupName": "mydbclusterparametergroup2",
            "DBParameterGroupFamily": "mysql8.0",
            "Description": "My new cluster parameter group",
            "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:mydbclusterparametergroup"
        }
    ]
}

```

To list all DB cluster parameter groups for an AWS account, use the RDS API [`DescribeDBClusterParameterGroups`](../APIReference/API_DescribeDBClusterParameterGroups.md "../APIReference/API_DescribeDBClusterParameterGroups.md") action.
