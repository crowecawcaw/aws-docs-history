

# Getting an existing ARN for Amazon RDS
<a name="USER_Tagging.ARN.Getting"></a>

You can get the ARN of an RDS resource by using the AWS Management Console, AWS Command Line Interface (AWS CLI), or RDS API. 

## Console
<a name="USER_Tagging.ARN.CON"></a>

To get an ARN from the AWS Management Console, navigate to the resource you want an ARN for, and view the details for that resource.

For example, you can get the ARN for a DB instance from the **Configuration** tab of the DB instance details.

![DB instance ARN.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/DB-instance-arn.png)


## AWS CLI
<a name="USER_Tagging.ARN.CLI"></a>

To get an ARN from the AWS CLI for a particular RDS resource, you use the `describe` command for that resource. The following table shows each AWS CLI command, and the ARN property used with the command to get an ARN. 



| AWS CLI command | ARN property | 
| --- | --- | 
|  [describe-event-subscriptions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-event-subscriptions.html)  | EventSubscriptionArn | 
|  [describe-certificates](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-certificates.html) | CertificateArn | 
|  [describe-db-parameter-groups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameter-groups.html) | DBParameterGroupArn | 
|  [describe-db-cluster-parameter-groups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameter-groups.html) | DBClusterParameterGroupArn | 
|  [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) | DBInstanceArn | 
|  [describe-db-security-groups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-security-groups.html) | DBSecurityGroupArn | 
|  [describe-db-snapshots](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-snapshots.html) | DBSnapshotArn | 
|  [describe-events](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-events.html) | SourceArn | 
|  [describe-reserved-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-reserved-db-instances.html) | ReservedDBInstanceArn | 
|  [describe-db-subnet-groups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-subnet-groups.html) | DBSubnetGroupArn | 
|  [describe-option-groups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-option-groups.html) | OptionGroupArn | 
|  [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) | DBClusterArn | 
|  [describe-db-cluster-snapshots](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-snapshots.html) | DBClusterSnapshotArn | 

For example, the following AWS CLI command gets the ARN for a DB instance.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds describe-db-instances \
--db-instance-identifier {{DBInstanceIdentifier}} \
--region {{us-west-2}} \
--query "*[].{DBInstanceIdentifier:DBInstanceIdentifier,DBInstanceArn:DBInstanceArn}"
```
For Windows:  

```
aws rds describe-db-instances ^
--db-instance-identifier {{DBInstanceIdentifier}} ^
--region {{us-west-2}} ^
--query "*[].{DBInstanceIdentifier:DBInstanceIdentifier,DBInstanceArn:DBInstanceArn}"
```
The output of that command is like the following:  

```
[
    {
        "DBInstanceArn": "arn:aws:rds:us-west-2:{{account_id}}:db:{{instance_id}}", 
        "DBInstanceIdentifier": "{{instance_id}}"
    }
]
```

## RDS API
<a name="USER_Tagging.ARN.API"></a>

To get an ARN for a particular RDS resource, you can call the following RDS API operations and use the ARN properties shown following.



| RDS API operation | ARN property | 
| --- | --- | 
|  [DescribeEventSubscriptions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEventSubscriptions.html) | EventSubscriptionArn | 
|  [DescribeCertificates](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeCertificates.html) | CertificateArn | 
|  [DescribeDBParameterGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBParameterGroups.html) | DBParameterGroupArn | 
|  [DescribeDBClusterParameterGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterParameterGroups.html) | DBClusterParameterGroupArn | 
|  [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) | DBInstanceArn | 
|  [DescribeDBSecurityGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSecurityGroups.html) | DBSecurityGroupArn | 
|  [DescribeDBSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshots.html) | DBSnapshotArn | 
|  [DescribeEvents](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEvents.html) | SourceArn | 
|  [DescribeReservedDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeReservedDBInstances.html) | ReservedDBInstanceArn | 
|  [DescribeDBSubnetGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSubnetGroups.html) | DBSubnetGroupArn | 
|  [DescribeOptionGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeOptionGroups.html) | OptionGroupArn | 
|  [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) | DBClusterArn | 
|  [DescribeDBClusterSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterSnapshots.html) | DBClusterSnapshotArn | 