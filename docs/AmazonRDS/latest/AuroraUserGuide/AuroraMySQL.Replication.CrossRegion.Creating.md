

# Creating a cross-Region read replica DB cluster for Aurora MySQL
<a name="AuroraMySQL.Replication.CrossRegion.Creating"></a>

 You can create an Aurora DB cluster that is a cross-Region read replica by using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon RDS API. You can create cross-Region read replicas from both encrypted and unencrypted DB clusters. 

 When you create a cross-Region read replica for Aurora MySQL by using the AWS Management Console, Amazon RDS creates a DB cluster in the target AWS Region, and then automatically creates a DB instance that is the primary instance for that DB cluster. 

 When you create a cross-Region read replica using the AWS CLI or RDS API, you first create the DB cluster in the target AWS Region and wait for it to become active. Once it is active, you then create a DB instance that is the primary instance for that DB cluster. 

 Replication begins when the primary instance of the read replica DB cluster becomes available. 

 Use the following procedures to create a cross-Region read replica from an Aurora MySQL DB cluster. These procedures work for creating read replicas from either encrypted or unencrypted DB clusters. 

## Console
<a name="AuroraMySQL.Replication.CrossRegion.Creating.Console"></a>

**To create an Aurora MySQL DB cluster that is a cross-Region read replica with the AWS Management Console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the AWS Management Console, select the AWS Region that hosts your source DB cluster. 

1.  In the navigation pane, choose **Databases**.

1.  Choose the DB cluster for which you want to create a cross-Region read replica.

1. For **Actions**, choose **Create cross-Region read replica**.

1.  On the **Create cross region read replica** page, choose the option settings for your cross-Region read replica DB cluster, as described in the following table.    
<a name="cross-region-read-replica-settings"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.Creating.html)

1.  Choose **Create** to create your cross-Region read replica for Aurora.

## AWS CLI
<a name="AuroraMySQL.Replication.CrossRegion.Creating.CLI"></a>

**To create an Aurora MySQL DB cluster that is a cross-Region read replica with the CLI**

1.  Call the AWS CLI [create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html) command in the AWS Region where you want to create the read replica DB cluster. Include the `--replication-source-identifier` option and specify the Amazon Resource Name (ARN) of the source DB cluster to create a read replica for. 

    For cross-Region replication where the DB cluster identified by `--replication-source-identifier` is encrypted, specify the `--kms-key-id` option and the `--storage-encrypted` option. 
**Note**  
 You can set up cross-Region replication from an unencrypted DB cluster to an encrypted read replica by specifying `--storage-encrypted` and providing a value for `--kms-key-id`. 

    You can't specify the `--master-username` and `--master-user-password` parameters. Those values are taken from the source DB cluster. 

    The following code example creates a read replica in the us-east-1 Region from an unencrypted DB cluster snapshot in the us-west-2 Region. The command is called in the us-east-1 Region. This example specifies the `--manage-master-user-password` option to generate the master user password and manage it in Secrets Manager. For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](rds-secrets-manager.md). Alternatively, you can use the `--master-password` option to specify and manage the password yourself. 

   For Linux, macOS, or Unix:

   ```
   aws rds create-db-cluster \
     --db-cluster-identifier sample-replica-cluster \
     --engine aurora-mysql \
     --engine-version 8.0.mysql_aurora.3.08.0 \
     --replication-source-identifier arn:aws:rds:us-west-2:123456789012:cluster:sample-master-cluster
   ```

   For Windows:

   ```
   aws rds create-db-cluster ^
     --db-cluster-identifier sample-replica-cluster ^
     --engine aurora-mysql ^
     --engine-version 8.0.mysql_aurora.3.08.0 ^
     --replication-source-identifier arn:aws:rds:us-west-2:123456789012:cluster:sample-master-cluster
   ```

    The following code example creates a read replica in the us-east-1 Region from an encrypted DB cluster snapshot in the us-west-2 Region. The command is called in the us-east-1 Region. 

   For Linux, macOS, or Unix:

   ```
   aws rds create-db-cluster \
     --db-cluster-identifier sample-replica-cluster \
     --engine aurora-mysql \
     --engine-version 8.0.mysql_aurora.3.08.0 \
     --replication-source-identifier arn:aws:rds:us-west-2:123456789012:cluster:sample-master-cluster \
     --kms-key-id {{my-us-east-1-key}} \
     --storage-encrypted
   ```

   For Windows:

   ```
   aws rds create-db-cluster ^
     --db-cluster-identifier sample-replica-cluster ^
     --engine aurora-mysql ^
     --engine-version 8.0.mysql_aurora.3.08.0 ^
     --replication-source-identifier arn:aws:rds:us-west-2:123456789012:cluster:sample-master-cluster ^
     --kms-key-id {{my-us-east-1-key}} ^
     --storage-encrypted
   ```

   The `--source-region` option is required for cross-Region replication between the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, where the DB cluster identified by `--replication-source-identifier` is encrypted. For `--source-region`, specify the AWS Region of the source DB cluster.

   If `--source-region` isn't specified, specify a `--pre-signed-url` value. A *presigned URL* is a URL that contains a Signature Version 4 signed request for the `create-db-cluster` command that is called in the source AWS Region. To learn more about the `pre-signed-url` option, see [ create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html) in the *AWS CLI Command Reference*.

1.  Check that the DB cluster has become available to use by using the AWS CLI [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) command, as shown in the following example. 

   ```
   aws rds describe-db-clusters --db-cluster-identifier sample-replica-cluster
   ```

    When the **`describe-db-clusters`** results show a status of `available`, create the primary instance for the DB cluster so that replication can begin. To do so, use the AWS CLI [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) command as shown in the following example. 

   For Linux, macOS, or Unix:

   ```
   aws rds create-db-instance \
     --db-cluster-identifier sample-replica-cluster \
     --db-instance-class db.r5.large \
     --db-instance-identifier sample-replica-instance \
     --engine aurora-mysql
   ```

   For Windows:

   ```
   aws rds create-db-instance ^
     --db-cluster-identifier sample-replica-cluster ^
     --db-instance-class db.r5.large ^
     --db-instance-identifier sample-replica-instance ^
     --engine aurora-mysql
   ```

    When the DB instance is created and available, replication begins. You can determine if the DB instance is available by calling the AWS CLI [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command. 

## RDS API
<a name="AuroraMySQL.Replication.CrossRegion.Creating.API"></a>

**To create an Aurora MySQL DB cluster that is a cross-Region read replica with the API**

1.  Call the RDS API [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) operation in the AWS Region where you want to create the read replica DB cluster. Include the `ReplicationSourceIdentifier` parameter and specify the Amazon Resource Name (ARN) of the source DB cluster to create a read replica for. 

    For cross-Region replication where the DB cluster identified by `ReplicationSourceIdentifier` is encrypted, specify the `KmsKeyId` parameter and set the `StorageEncrypted` parameter to `true`. 
**Note**  
 You can set up cross-Region replication from an unencrypted DB cluster to an encrypted read replica by specifying `StorageEncrypted` as **true** and providing a value for `KmsKeyId`. In this case, you don't need to specify `PreSignedUrl`. 

    You don't need to include the `MasterUsername` and `MasterUserPassword` parameters, because those values are taken from the source DB cluster. 

    The following code example creates a read replica in the us-east-1 Region from an unencrypted DB cluster snapshot in the us-west-2 Region. The action is called in the us-east-1 Region. 

   ```
   https://rds.us-east-1.amazonaws.com/
     ?Action=CreateDBCluster
     &ReplicationSourceIdentifier=arn:aws:rds:us-west-2:123456789012:cluster:sample-master-cluster
     &DBClusterIdentifier=sample-replica-cluster
     &Engine=aurora-mysql
     &SignatureMethod=HmacSHA256
     &SignatureVersion=4
     &Version=2014-10-31
     &X-Amz-Algorithm=AWS4-HMAC-SHA256
     &X-Amz-Credential=AKIADQKE4SARGYLE/20161117/us-east-1/rds/aws4_request
     &X-Amz-Date=20160201T001547Z
     &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
     &X-Amz-Signature=a04c831a0b54b5e4cd236a90dcb9f5fab7185eb3b72b5ebe9a70a4e95790c8b7
   ```

    The following code example creates a read replica in the us-east-1 Region from an encrypted DB cluster snapshot in the us-west-2 Region. The action is called in the us-east-1 Region. 

   ```
   https://rds.us-east-1.amazonaws.com/
     ?Action=CreateDBCluster
     &KmsKeyId=my-us-east-1-key
     &StorageEncrypted=true
     &PreSignedUrl=https%253A%252F%252Frds.us-west-2.amazonaws.com%252F
            %253FAction%253DCreateDBCluster
            %2526DestinationRegion%253Dus-east-1
            %2526KmsKeyId%253Dmy-us-east-1-key
            %2526ReplicationSourceIdentifier%253Darn%25253Aaws%25253Ards%25253Aus-west-2%25253A123456789012%25253Acluster%25253Asample-master-cluster
            %2526SignatureMethod%253DHmacSHA256
            %2526SignatureVersion%253D4
            %2526Version%253D2014-10-31
            %2526X-Amz-Algorithm%253DAWS4-HMAC-SHA256
            %2526X-Amz-Credential%253DAKIADQKE4SARGYLE%252F20161117%252Fus-west-2%252Frds%252Faws4_request
            %2526X-Amz-Date%253D20161117T215409Z
            %2526X-Amz-Expires%253D3600
            %2526X-Amz-SignedHeaders%253Dcontent-type%253Bhost%253Buser-agent%253Bx-amz-content-sha256%253Bx-amz-date
            %2526X-Amz-Signature%253D255a0f17b4e717d3b67fad163c3ec26573b882c03a65523522cf890a67fca613
     &ReplicationSourceIdentifier=arn:aws:rds:us-west-2:123456789012:cluster:sample-master-cluster
     &DBClusterIdentifier=sample-replica-cluster
     &Engine=aurora-mysql
     &SignatureMethod=HmacSHA256
     &SignatureVersion=4
     &Version=2014-10-31
     &X-Amz-Algorithm=AWS4-HMAC-SHA256
     &X-Amz-Credential=AKIADQKE4SARGYLE/20161117/us-east-1/rds/aws4_request
     &X-Amz-Date=20160201T001547Z
     &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
     &X-Amz-Signature=a04c831a0b54b5e4cd236a90dcb9f5fab7185eb3b72b5ebe9a70a4e95790c8b7
   ```

   For cross-Region replication between the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, where the DB cluster identified by `ReplicationSourceIdentifier` is encrypted, also specify the `PreSignedUrl` parameter. The presigned URL must be a valid request for the `CreateDBCluster` API operation that can be performed in the source AWS Region that contains the encrypted DB cluster to be replicated. The KMS key identifier is used to encrypt the read replica, and must be a KMS key valid for the destination AWS Region. To automatically rather than manually generate a presigned URL, use the AWS CLI [create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html) command with the `--source-region` option instead. 

1.  Check that the DB cluster has become available to use by using the RDS API [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) operation, as shown in the following example. 

   ```
   https://rds.us-east-1.amazonaws.com/
     ?Action=DescribeDBClusters
     &DBClusterIdentifier=sample-replica-cluster
     &SignatureMethod=HmacSHA256
     &SignatureVersion=4
     &Version=2014-10-31
     &X-Amz-Algorithm=AWS4-HMAC-SHA256
     &X-Amz-Credential=AKIADQKE4SARGYLE/20161117/us-east-1/rds/aws4_request
     &X-Amz-Date=20160201T002223Z
     &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
     &X-Amz-Signature=84c2e4f8fba7c577ac5d820711e34c6e45ffcd35be8a6b7c50f329a74f35f426
   ```

    When `DescribeDBClusters` results show a status of `available`, create the primary instance for the DB cluster so that replication can begin. To do so, use the RDS API [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) action as shown in the following example. 

   ```
   https://rds.us-east-1.amazonaws.com/
     ?Action=CreateDBInstance
     &DBClusterIdentifier=sample-replica-cluster
     &DBInstanceClass=db.r5.large
     &DBInstanceIdentifier=sample-replica-instance
     &Engine=aurora-mysql
     &SignatureMethod=HmacSHA256
     &SignatureVersion=4
     &Version=2014-10-31
     &X-Amz-Algorithm=AWS4-HMAC-SHA256
     &X-Amz-Credential=AKIADQKE4SARGYLE/20161117/us-east-1/rds/aws4_request
     &X-Amz-Date=20160201T003808Z
     &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
     &X-Amz-Signature=125fe575959f5bbcebd53f2365f907179757a08b5d7a16a378dfa59387f58cdb
   ```

    When the DB instance is created and available, replication begins. You can determine if the DB instance is available by calling the AWS CLI [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) command. 

## Viewing Amazon Aurora MySQL cross-Region replicas
<a name="AuroraMySQL.Replication.CrossRegion.Viewing"></a>

 You can view the cross-Region replication relationships for your Amazon Aurora MySQL DB clusters by calling the [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) AWS CLI command or the [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) RDS API operation. In the response, refer to the `ReadReplicaIdentifiers` field for the DB cluster identifiers of any cross-Region read replica DB clusters. Refer to the `ReplicationSourceIdentifier` element for the ARN of the source DB cluster that is the replication source. 