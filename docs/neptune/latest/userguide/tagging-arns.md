# Working with administrative ARNs in Amazon Neptune

Resources that are created in Amazon Web Services are each uniquely identified with an Amazon
Resource Name (ARN). For certain Amazon Neptune operations, you must uniquely identify a
Neptune resource by specifying its ARN.

###### Important

Amazon Neptune shares the format of Amazon RDS ARNs for administrative actions
that use the [Management API reference](api.md "api.md"). Neptune administrative
ARNs contain `rds` and not `neptune-db`. For data-plane ARNs that
identify Neptune data resources, see [Specifying
data resources](iam-data-resources.md "iam-data-resources.md").

###### Topics

- [Constructing an ARN for Neptune](tagging-arns-constructing.md "tagging-arns-constructing.md")
- [Getting an existing ARN in Amazon Neptune](#tagging-arns-getting "#tagging-arns-getting")

## Getting an existing ARN in Amazon Neptune

You can get the ARN of a Neptune resource by using the AWS Management Console, AWS Command Line Interface (AWS CLI),
or Neptune API.

### Getting an existing ARN using the AWS Management Console

To get an ARN using the console, navigate to the resource that you want an ARN for, and
view the details for that resource. For example, to get the ARN for a DB
instance, choose **Instances** in the navigation panel, and
choose the instance that you want from the list. The ARN is in the
**Instance Details** section.

### Getting an existing ARN using the AWS CLI

To use the AWS CLI to get an ARN for a particular Neptune resource, use the
`describe` command for that resource. The following table shows
each AWS CLI command and the ARN property that is used with the command to get an
ARN.

| AWS CLI Command                                                                                                                                                                                       | ARN Property               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [describe-event-subscriptions](../../../cli/latest/reference/neptune/describe-event-subscriptions.md "../../../cli/latest/reference/neptune/describe-event-subscriptions.md")                         | EventSubscriptionArn       |
| [describe-certificates](../../../cli/latest/reference/neptune/describe-certificates.md "../../../cli/latest/reference/neptune/describe-certificates.md")                                              | CertificateArn             |
| [describe-db-parameter-groups](../../../cli/latest/reference/neptune/describe-db-parameter-groups.md "../../../cli/latest/reference/neptune/describe-db-parameter-groups.md")                         | DBParameterGroupArn        |
| [describe-db-cluster-parameter-groups](../../../cli/latest/reference/neptune/describe-db-cluster-parameter-groups.md "../../../cli/latest/reference/neptune/describe-db-cluster-parameter-groups.md") | DBClusterParameterGroupArn |
| [describe-db-instances](../../../cli/latest/reference/neptune/describe-db-instances.md "../../../cli/latest/reference/neptune/describe-db-instances.md")                                              | DBInstanceArn              |
| [describe-events](../../../cli/latest/reference/neptune/describe-events.md "../../../cli/latest/reference/neptune/describe-events.md")                                                                | SourceArn                  |
| [describe-db-subnet-groups](../../../cli/latest/reference/neptune/describe-db-subnet-groups.md "../../../cli/latest/reference/neptune/describe-db-subnet-groups.md")                                  | DBSubnetGroupArn           |
| [describe-db-clusters](../../../cli/latest/reference/neptune/describe-db-clusters.md "../../../cli/latest/reference/neptune/describe-db-clusters.md")                                                 | DBClusterArn               |
| [describe-db-cluster-snapshots](../../../cli/latest/reference/neptune/describe-db-cluster-snapshots.md "../../../cli/latest/reference/neptune/describe-db-cluster-snapshots.md")                      | DBClusterSnapshotArn       |

For example, the following AWS CLI command gets the ARN for a DB instance.

###### Example

For Linux, OS X, or Unix:

```
aws neptune describe-db-instances \
--db-instance-identifier `DBInstanceIdentifier` \
--region `us-west-2`
```

For Windows:

```
aws neptune describe-db-instances ^
--db-instance-identifier `DBInstanceIdentifier` ^
--region `us-west-2`
```

### Getting an existing ARN using the API

To get an ARN for a particular Neptune resource, call the following API actions
and use the ARN properties shown.

| Neptune API Action                                                                                                    | ARN Property               |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [DescribeEventSubscriptions](API_DescribeEventSubscriptions.md "API_DescribeEventSubscriptions.md")                   | EventSubscriptionArn       |
| [DescribeCertificates](API_DescribeCertificates.md "API_DescribeCertificates.md")                                     | CertificateArn             |
| [DescribeDBParameterGroups](API_DescribeDBParameterGroups.md "API_DescribeDBParameterGroups.md")                      | DBParameterGroupArn        |
| [DescribeDBClusterParameterGroups](API_DescribeDBClusterParameterGroups.md "API_DescribeDBClusterParameterGroups.md") | DBClusterParameterGroupArn |
| [DescribeDBInstances](API_DescribeDBInstances.md "API_DescribeDBInstances.md")                                        | DBInstanceArn              |
| [DescribeEvents](API_DescribeEvents.md "API_DescribeEvents.md")                                                       | SourceArn                  |
| [DescribeDBSubnetGroups](API_DescribeDBSubnetGroups.md "API_DescribeDBSubnetGroups.md")                               | DBSubnetGroupArn           |
| [DescribeDBClusters](API_DescribeDBClusters.md "API_DescribeDBClusters.md")                                           | DBClusterArn               |
| [DescribeDBClusterSnapshots](API_DescribeDBClusterSnapshots.md "API_DescribeDBClusterSnapshots.md")                   | DBClusterSnapshotArn       |
