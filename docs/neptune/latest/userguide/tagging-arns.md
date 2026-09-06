

# Working with administrative ARNs in Amazon Neptune
<a name="tagging-arns"></a>

Resources that are created in Amazon Web Services are each uniquely identified with an Amazon Resource Name (ARN). For certain Amazon Neptune operations, you must uniquely identify a Neptune resource by specifying its ARN. 

**Important**  
Amazon Neptune shares the format of Amazon RDS ARNs for administrative actions that use the [Management API reference](api.md). Neptune administrative ARNs contain `rds` and not `neptune-db`. For data-plane ARNs that identify Neptune data resources, see [Specifying data resources](iam-data-resources.md).

**Topics**
+ [Constructing an ARN for Neptune](tagging-arns-constructing.md)
+ [Getting an existing ARN in Amazon Neptune](#tagging-arns-getting)

## Getting an existing ARN in Amazon Neptune
<a name="tagging-arns-getting"></a>

You can get the ARN of a Neptune resource by using the AWS Management Console, AWS Command Line Interface (AWS CLI), or Neptune API.

### Getting an existing ARN using the AWS Management Console
<a name="tagging-arns-console"></a>

To get an ARN using the console, navigate to the resource that you want an ARN for, and view the details for that resource. For example, to get the ARN for a DB instance, choose **Instances** in the navigation panel, and choose the instance that you want from the list. The ARN is in the **Instance Details** section. 

### Getting an existing ARN using the AWS CLI
<a name="tagging-arns-cli"></a>

To use the AWS CLI to get an ARN for a particular Neptune resource, use the `describe` command for that resource. The following table shows each AWS CLI command and the ARN property that is used with the command to get an ARN.



| AWS CLI Command | ARN Property | 
| --- | --- | 
|  [describe-event-subscriptions](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-event-subscriptions.html)  | EventSubscriptionArn | 
|  [describe-certificates](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-certificates.html) | CertificateArn | 
|  [describe-db-parameter-groups](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-db-parameter-groups.html) | DBParameterGroupArn | 
|  [describe-db-cluster-parameter-groups](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-db-cluster-parameter-groups.html) | DBClusterParameterGroupArn | 
|  [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-db-instances.html) | DBInstanceArn | 
|  [describe-events](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-events.html) | SourceArn | 
|  [describe-db-subnet-groups](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-db-subnet-groups.html) | DBSubnetGroupArn | 
|  [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-db-clusters.html) | DBClusterArn | 
|  [describe-db-cluster-snapshots](https://docs.aws.amazon.com/cli/latest/reference/neptune/describe-db-cluster-snapshots.html) | DBClusterSnapshotArn | 

For example, the following AWS CLI command gets the ARN for a DB instance.

**Example**  
For Linux, OS X, or Unix:  

```
1. aws neptune describe-db-instances \
2. --db-instance-identifier {{DBInstanceIdentifier}} \
3. --region {{us-west-2}}
```
For Windows:  

```
1. aws neptune describe-db-instances ^
2. --db-instance-identifier {{DBInstanceIdentifier}} ^
3. --region {{us-west-2}}
```

### Getting an existing ARN using the API
<a name="tagging-arns-api"></a>

To get an ARN for a particular Neptune resource, call the following API actions and use the ARN properties shown.



| Neptune API Action | ARN Property | 
| --- | --- | 
|  [DescribeEventSubscriptions](API_DescribeEventSubscriptions.html) | EventSubscriptionArn | 
|  [DescribeCertificates](API_DescribeCertificates.html) | CertificateArn | 
|  [DescribeDBParameterGroups](API_DescribeDBParameterGroups.html) | DBParameterGroupArn | 
|  [DescribeDBClusterParameterGroups](API_DescribeDBClusterParameterGroups.html) | DBClusterParameterGroupArn | 
|  [DescribeDBInstances](API_DescribeDBInstances.html) | DBInstanceArn | 
|  [DescribeEvents](API_DescribeEvents.html) | SourceArn | 
|  [DescribeDBSubnetGroups](API_DescribeDBSubnetGroups.html) | DBSubnetGroupArn | 
|  [DescribeDBClusters](API_DescribeDBClusters.html) | DBClusterArn | 
|  [DescribeDBClusterSnapshots](API_DescribeDBClusterSnapshots.html) | DBClusterSnapshotArn | 