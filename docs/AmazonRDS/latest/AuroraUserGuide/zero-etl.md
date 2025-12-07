# Getting started with Aurora zero-ETL integrations

Before you create a zero-ETL integration, configure your Aurora DB cluster and your data warehouse with
the required parameters and permissions. During setup, you'll complete the following
steps:

1. [Create a custom DB cluster parameter group](#zero-etl.parameters "#zero-etl.parameters").
2. [Create a source DB cluster](#zero-etl.create-cluster "#zero-etl.create-cluster").
3. [Create a target data warehouse
   for Amazon Redshift](#zero-etl-setting-up.data-warehouse "#zero-etl-setting-up.data-warehouse") or [Create a
   target Amazon SageMaker AI lakehouse](#zero-etl-setting-up.sagemaker "#zero-etl-setting-up.sagemaker").
   After you complete these tasks, continue to [Creating Aurora zero-ETL integrations with Amazon Redshift](zero-etl.md "zero-etl.md") or [Creating Aurora zero-ETL integrations with an Amazon SageMaker lakehouse](zero-etl.md "zero-etl.md").

You can use the AWS SDKs to automate the setup process for you. For
more information, see [Set up an integration using the AWS SDKs](#zero-etl.setup-sdk "#zero-etl.setup-sdk").

###### Tip

You can have RDS complete these setup steps for you while you're creating the
integration, rather than performing them manually. To immediately start creating an
integration, see [Creating Aurora zero-ETL integrations with Amazon Redshift](zero-etl.md "zero-etl.md").

For Step 3, you can choose to create either a target data warehouse (Step 3a) or a target
lakehouse (Step 3b) depending on your needs:

- Choose a data warehouse if you need traditional data warehousing capabilities with
  SQL-based analytics.
- Choose an Amazon SageMaker AI lakehouse if you need machine learning
  capabilities and want to use lakehouse features for data science and ML
  workflows.

## Step 1: Create a custom DB cluster parameter group

Aurora zero-ETL integrations require specific values for the DB cluster
parameters that control replication. Specifically, Aurora MySQL requires
_enhanced binlog_ (`aurora_enhanced_binlog`), and
Aurora PostgreSQL requires _enhanced logical replication_
(`aurora.enhanced_logical_replication`).

To configure binary logging or logical replication, you must first
create a custom DB cluster parameter group, and then associate it with the source
DB cluster.

**Aurora MySQL (aurora-mysql8.0
family)**:

- `aurora_enhanced_binlog=1`
- `binlog_backup=0`
- `binlog_format=ROW`
- `binlog_replication_globaldb=0`
- `binlog_row_image=full`
- `binlog_row_metadata=full`

In addition, make sure that the
`binlog_transaction_compression` parameter is _not_
set to `ON`, and that the `binlog_row_value_options` parameter is
_not_ set to `PARTIAL_JSON`.

For more information about Aurora MySQL enhanced binlog, see [Setting up enhanced binlog for Aurora MySQL](AuroraMySQL.Enhanced.md "AuroraMySQL.Enhanced.md").

**Aurora PostgreSQL (aurora-postgresql16
family):**

- `rds.logical_replication=1`
- `aurora.enhanced_logical_replication=1`
- `aurora.logical_replication_backup=0`
- `aurora.logical_replication_globaldb=0`

Enabling enhanced logical replication
(`aurora.enhanced_logical_replication`) will always write all column
values to the write ahead log (WAL) even if `REPLICA IDENTITY FULL` isn't
enabled. This might increase the IOPS for your source DB cluster.

###### Important

If you enable or disable the `aurora.enhanced_logical_replication` DB
cluster parameter, the primary DB instance invalidates all logical replication
slots. This stops replication from the source to the target, and you must recreate
replication slots on the primary DB instance. To prevent interruptions, keep the
parameter state consistent during replication.

## Step 2: Select or create a source DB cluster

After you create a custom DB cluster parameter
group, choose or create an
Aurora DB cluster. This cluster will be the source of
data replication to the target data warehouse. You can
specify a DB cluster that uses provisioned DB instances or Aurora Serverless v2 DB instances as the
source. For instructions to create a DB cluster, see
[Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md") or
[Creating a DB cluster that uses Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

The database must be running a supported DB engine version. For a list of supported
versions, see [Supported
Regions and Aurora DB engines for zero-ETL integrations](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

When you create the database, under **Additional configuration**,
change the default **DB cluster parameter
group** to the custom parameter group that you created in the previous
step.

###### Note

If you associate the parameter group with the DB cluster
_after_ the cluster is already
created, you must reboot the primary DB instance in the cluster to apply the
changes before you can create a zero-ETL integration. For instructions, see [Rebooting an Amazon Aurora DB cluster or Amazon Aurora DB instance](USER_RebootCluster.md "USER_RebootCluster.md").

## Step 3a: Create a target data

warehouse

After you create your source DB cluster, you must create and configure a target data
warehouse. The data warehouse must meet the following requirements:

- Using an RA3 node type with at least two nodes, or Redshift Serverless.
- Encrypted (if using a provisioned cluster). For more information, see [Amazon Redshift database
  encryption](../../../redshift/latest/mgmt/working-with-db-encryption.md "../../../redshift/latest/mgmt/working-with-db-encryption.md").

For instructions to create a data warehouse, see [Creating a cluster](../../../redshift/latest/mgmt/create-cluster.md "../../../redshift/latest/mgmt/create-cluster.md") for provisioned
clusters, or [Creating a workgroup with a namespace](../../../redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.md "../../../redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.md") for Redshift Serverless.

### Enable case sensitivity on

the data warehouse

For the integration to be successful, the case sensitivity parameter ([`enable_case_sensitive_identifier`](../../../redshift/latest/dg/r_enable_case_sensitive_identifier.md "../../../redshift/latest/dg/r_enable_case_sensitive_identifier.md")) must be enabled for
the data warehouse. By default, case sensitivity is disabled on all provisioned
clusters and Redshift Serverless workgroups.

To enable case sensitivity, perform the following steps depending on your data
warehouse type:

- **Provisioned cluster** – To enable
  case sensitivity on a provisioned cluster, create a custom parameter group
  with the `enable_case_sensitive_identifier` parameter enabled.
  Then, associate the parameter group with the cluster. For instructions, see
  [Managing parameter groups using the console](../../../redshift/latest/mgmt/managing-parameter-groups-console.md "../../../redshift/latest/mgmt/managing-parameter-groups-console.md") or [Configuring parameter values using the AWS CLI](../../../redshift/latest/mgmt/working-with-parameter-groups.md#configure-parameters-using-the-clil "../../../redshift/latest/mgmt/working-with-parameter-groups.md#configure-parameters-using-the-clil").

###### Note

Remember to reboot the cluster after you associate the custom
parameter group with it.

- **Serverless workgroup** – To enable
  case sensitivity on a Redshift Serverless workgroup, you must use the AWS CLI. The Amazon Redshift
  console doesn't currently support modifying Redshift Serverless parameter values. Send the
  following [update-workgroup](../../../cli/latest/reference/redshift-serverless/update-workgroup.md "../../../cli/latest/reference/redshift-serverless/update-workgroup.md") request:

```
aws redshift-serverless update-workgroup \
  --workgroup-name `target-workgroup` \
  --config-parameters parameterKey=enable_case_sensitive_identifier,parameterValue=true
```

You don't need to reboot a workgroup after you modify its parameter
values.

### Configure authorization for the data

warehouse

After you create a data warehouse, you must configure the source Aurora DB cluster as an authorized integration source. For instructions, see [Configure authorization for your Amazon Redshift data warehouse](../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-using.redshift-iam "../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-using.redshift-iam").

## Set up an integration using the AWS SDKs

Rather than setting up each resource manually, you can run the following Python script
to automatically set up the required resources for you. The code example uses the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html") to create a source Amazon Aurora
DB cluster and target
data warehouse, each with the required parameter values. It then waits for the databases
to be available before creating a zero-ETL integration between them. You can comment out
different functions depending on which resources you need to set up.

To install the required dependencies, run the following commands:

```
pip install boto3
pip install time
```

Within the script, optionally modify the names of the source, target, and parameter
groups. The final function creates an integration named `my-integration`
after the resources are set up.

Aurora MySQL

```
import boto3
import time

# Build the client using the default credential configuration.
# You can use the CLI and run 'aws configure' to set access key, secret
# key, and default Region.

rds = boto3.client('rds')
redshift = boto3.client('redshift')
sts = boto3.client('sts')

source_cluster_name = 'my-source-cluster' # A name for the source cluster
source_param_group_name = 'my-source-param-group' # A name for the source parameter group
target_cluster_name = 'my-target-cluster' # A name for the target cluster
target_param_group_name = 'my-target-param-group' # A name for the target parameter group

def create_source_cluster(*args):
    """Creates a source Aurora MySQL DB cluster"""

    response = rds.create_db_cluster_parameter_group(
        DBClusterParameterGroupName=source_param_group_name,
        DBParameterGroupFamily='aurora-mysql8.0',
        Description='For Aurora MySQL binary logging'
    )
    print('Created source parameter group: ' + response['DBClusterParameterGroup']['DBClusterParameterGroupName'])

    response = rds.modify_db_cluster_parameter_group(
        DBClusterParameterGroupName=source_param_group_name,
        Parameters=[
            {
                'ParameterName': 'aurora_enhanced_binlog',
                'ParameterValue': '1',
                'ApplyMethod': 'pending-reboot'
            },
            {
                'ParameterName': 'binlog_backup',
                'ParameterValue': '0',
                'ApplyMethod': 'pending-reboot'
            },
            {
                'ParameterName': 'binlog_format',
                'ParameterValue': 'ROW',
                'ApplyMethod': 'pending-reboot'
            },
            {
                'ParameterName': 'binlog_replication_globaldb',
                'ParameterValue': '0',
                'ApplyMethod': 'pending-reboot'
            },
            {
                'ParameterName': 'binlog_row_image',
                'ParameterValue': 'full',
                'ApplyMethod': 'pending-reboot'
            },
            {
                'ParameterName': 'binlog_row_metadata',
                'ParameterValue': 'full',
                'ApplyMethod': 'pending-reboot'
            }
        ]
    )
    print('Modified source parameter group: ' + response['DBClusterParameterGroupName'])

    response = rds.create_db_cluster(
        DBClusterIdentifier=source_cluster_name,
        DBClusterParameterGroupName=source_param_group_name,
        Engine='aurora-mysql',
        EngineVersion='8.0.mysql_aurora.3.05.2',
        DatabaseName='myauroradb',
        MasterUsername='`username`',
        MasterUserPassword='`Password01**`'
    )
    print('Creating source cluster: ' + response['DBCluster']['DBClusterIdentifier'])
    source_arn = (response['DBCluster']['DBClusterArn'])
    create_target_cluster(target_cluster_name, source_arn, target_param_group_name)

    response = rds.create_db_instance(
        DBInstanceClass='db.r6g.2xlarge',
        DBClusterIdentifier=source_cluster_name,
        DBInstanceIdentifier=source_cluster_name + '-instance',
        Engine='aurora-mysql'
    )
    return(response)

def create_target_cluster(target_cluster_name, source_arn, target_param_group_name):
    """Creates a target Redshift cluster"""

    response = redshift.create_cluster_parameter_group(
        ParameterGroupName=target_param_group_name,
        ParameterGroupFamily='redshift-1.0',
        Description='For Aurora MySQL zero-ETL integrations'
    )
    print('Created target parameter group: ' + response['ClusterParameterGroup']['ParameterGroupName'])

    response = redshift.modify_cluster_parameter_group(
        ParameterGroupName=target_param_group_name,
        Parameters=[
            {
                'ParameterName': 'enable_case_sensitive_identifier',
                'ParameterValue': 'true'
            }
        ]
    )
    print('Modified target parameter group: ' + response['ParameterGroupName'])

    response = redshift.create_cluster(
        ClusterIdentifier=target_cluster_name,
        NodeType='ra3.4xlarge',
        NumberOfNodes=2,
        Encrypted=True,
        MasterUsername='`username`',
        MasterUserPassword='`Password01**`',
        ClusterParameterGroupName=target_param_group_name
    )
    print('Creating target cluster: ' + response['Cluster']['ClusterIdentifier'])

    # Retrieve the target cluster ARN
    response = redshift.describe_clusters(
        ClusterIdentifier=target_cluster_name
    )
    target_arn = response['Clusters'][0]['ClusterNamespaceArn']

    # Retrieve the current user's account ID
    response = sts.get_caller_identity()
    account_id = response['Account']

    # Create a resource policy specifying cluster ARN and account ID
    response = redshift.put_resource_policy(
        ResourceArn=target_arn,
        Policy='''
        {
            \"Version\":\"2012-10-17\",
            \"Statement\":[
                {\"Effect\":\"Allow\",
                \"Principal\":{
                    \"Service\":\"redshift.amazonaws.com\"
                },
                \"Action\":[\"redshift:AuthorizeInboundIntegration\"],
                \"Condition\":{
                    \"StringEquals\":{
                        \"aws:SourceArn\":\"%s\"}
                    }
                },
                {\"Effect\":\"Allow\",
                \"Principal\":{
                    \"AWS\":\"arn:aws:iam::%s:root\"},
                \"Action\":\"redshift:CreateInboundIntegration\"}
            ]
        }
        ''' % (source_arn, account_id)
    )
    return(response)

def wait_for_cluster_availability(*args):
    """Waits for both clusters to be available"""

    print('Waiting for clusters to be available...')

    response = rds.describe_db_clusters(
        DBClusterIdentifier=source_cluster_name
    )
    source_status = response['DBClusters'][0]['Status']
    source_arn = response['DBClusters'][0]['DBClusterArn']

    response = rds.describe_db_instances(
        DBInstanceIdentifier=source_cluster_name + '-instance'
    )
    source_instance_status = response['DBInstances'][0]['DBInstanceStatus']

    response = redshift.describe_clusters(
        ClusterIdentifier=target_cluster_name
    )
    target_status = response['Clusters'][0]['ClusterStatus']
    target_arn = response['Clusters'][0]['ClusterNamespaceArn']

    # Every 60 seconds, check whether the clusters are available.
    if source_status != 'available' or target_status != 'available' or  source_instance_status != 'available':
        time.sleep(60)
        response = wait_for_cluster_availability(
            source_cluster_name, target_cluster_name)
    else:
        print('Clusters available. Ready to create zero-ETL integration.')
        create_integration(source_arn, target_arn)
        return

def create_integration(source_arn, target_arn):
    """Creates a zero-ETL integration using the source and target clusters"""

    response = rds.create_integration(
        SourceArn=source_arn,
        TargetArn=target_arn,
        IntegrationName='`my-integration`'
    )
    print('Creating integration: ' + response['IntegrationName'])

def main():
    """main function"""
    create_source_cluster(source_cluster_name, source_param_group_name)
    wait_for_cluster_availability(source_cluster_name, target_cluster_name)

if __name__ == "__main__":
    main()
```

Aurora PostgreSQL

```
import boto3
import time

# Build the client using the default credential configuration.
# You can use the CLI and run 'aws configure' to set access key, secret
# key, and default Region.

rds = boto3.client('rds')
redshift = boto3.client('redshift')
sts = boto3.client('sts')

source_cluster_name = 'my-source-cluster' # A name for the source cluster
source_param_group_name = 'my-source-param-group' # A name for the source parameter group
target_cluster_name = 'my-target-cluster' # A name for the target cluster
target_param_group_name = 'my-target-param-group' # A name for the target parameter group

def create_source_cluster(*args):
    """Creates a source Aurora PostgreSQL DB cluster"""

    response = rds.create_db_cluster_parameter_group(
        DBClusterParameterGroupName=source_param_group_name,
        DBParameterGroupFamily='aurora-postgresql16',
        Description='For Aurora PostgreSQL logical replication'
    )
    print('Created source parameter group: ' + response['DBClusterParameterGroup']['DBClusterParameterGroupName'])

    response = rds.modify_db_cluster_parameter_group(
        DBClusterParameterGroupName=source_param_group_name,
        Parameters=[
            {
                'ParameterName': 'rds.logical_replication',
                'ParameterValue': '1',
                'ApplyMethod': 'pending-reboot'
            },
            {
                'ParameterName': 'aurora.enhanced_logical_replication',
                'ParameterValue': '1',
                'ApplyMethod': 'pending-reboot'
            },
            {
                'ParameterName': 'aurora.logical_replication_backup',
                'ParameterValue': '0',
                'ApplyMethod': 'pending-reboot'
            },
            {
                'ParameterName': 'aurora.logical_replication_globaldb',
                'ParameterValue': '0',
                'ApplyMethod': 'pending-reboot'
            }
        ]
    )
    print('Modified source parameter group: ' + response['DBClusterParameterGroupName'])

    response = rds.create_db_cluster(
        DBClusterIdentifier=source_cluster_name,
        DBClusterParameterGroupName=source_param_group_name,
        Engine='aurora-postgresql',
        EngineVersion='16.4.aurora-postgresql',
        DatabaseName='mypostgresdb',
        MasterUsername='`username`',
        MasterUserPassword='`Password01`**'
    )
    print('Creating source cluster: ' + response['DBCluster']['DBClusterIdentifier'])
    source_arn = (response['DBCluster']['DBClusterArn'])
    create_target_cluster(target_cluster_name, source_arn, target_param_group_name)

    response = rds.create_db_instance(
        DBInstanceClass='db.r6g.2xlarge',
        DBClusterIdentifier=source_cluster_name,
        DBInstanceIdentifier=source_cluster_name + '-instance',
        Engine='aurora-postgresql'
    )
    return(response)

def create_target_cluster(target_cluster_name, source_arn, target_param_group_name):
    """Creates a target Redshift cluster"""

    response = redshift.create_cluster_parameter_group(
        ParameterGroupName=target_param_group_name,
        ParameterGroupFamily='redshift-1.0',
        Description='For Aurora PostgreSQL zero-ETL integrations'
    )
    print('Created target parameter group: ' + response['ClusterParameterGroup']['ParameterGroupName'])

    response = redshift.modify_cluster_parameter_group(
        ParameterGroupName=target_param_group_name,
        Parameters=[
            {
                'ParameterName': 'enable_case_sensitive_identifier',
                'ParameterValue': 'true'
            }
        ]
    )
    print('Modified target parameter group: ' + response['ParameterGroupName'])

    response = redshift.create_cluster(
        ClusterIdentifier=target_cluster_name,
        NodeType='ra3.4xlarge',
        NumberOfNodes=2,
        Encrypted=True,
        MasterUsername='`username`',
        MasterUserPassword='`Password01**`',
        ClusterParameterGroupName=target_param_group_name
    )
    print('Creating target cluster: ' + response['Cluster']['ClusterIdentifier'])

    # Retrieve the target cluster ARN
    response = redshift.describe_clusters(
        ClusterIdentifier=target_cluster_name
    )
    target_arn = response['Clusters'][0]['ClusterNamespaceArn']

    # Retrieve the current user's account ID
    response = sts.get_caller_identity()
    account_id = response['Account']

    # Create a resource policy specifying cluster ARN and account ID
    response = redshift.put_resource_policy(
        ResourceArn=target_arn,
        Policy='''
        {
            \"Version\":\"2012-10-17\",
            \"Statement\":[
                {\"Effect\":\"Allow\",
                \"Principal\":{
                    \"Service\":\"redshift.amazonaws.com\"
                },
                \"Action\":[\"redshift:AuthorizeInboundIntegration\"],
                \"Condition\":{
                    \"StringEquals\":{
                        \"aws:SourceArn\":\"%s\"}
                    }
                },
                {\"Effect\":\"Allow\",
                \"Principal\":{
                    \"AWS\":\"arn:aws:iam::%s:root\"},
                \"Action\":\"redshift:CreateInboundIntegration\"}
            ]
        }
        ''' % (source_arn, account_id)
    )
    return(response)

def wait_for_cluster_availability(*args):
    """Waits for both clusters to be available"""

    print('Waiting for clusters to be available...')

    response = rds.describe_db_clusters(
        DBClusterIdentifier=source_cluster_name
    )
    source_status = response['DBClusters'][0]['Status']
    source_arn = response['DBClusters'][0]['DBClusterArn']

    response = rds.describe_db_instances(
        DBInstanceIdentifier=source_cluster_name + '-instance'
    )
    source_instance_status = response['DBInstances'][0]['DBInstanceStatus']

    response = redshift.describe_clusters(
        ClusterIdentifier=target_cluster_name
    )
    target_status = response['Clusters'][0]['ClusterStatus']
    target_arn = response['Clusters'][0]['ClusterNamespaceArn']

    # Every 60 seconds, check whether the clusters are available.
    if source_status != 'available' or target_status != 'available' or  source_instance_status != 'available':
        time.sleep(60)
        response = wait_for_cluster_availability(
            source_cluster_name, target_cluster_name)
    else:
        print('Clusters available. Ready to create zero-ETL integration.')
        create_integration(source_arn, target_arn)
        return

def create_integration(source_arn, target_arn):
    """Creates a zero-ETL integration using the source and target clusters"""

    response = rds.create_integration(
        SourceArn=source_arn,
        TargetArn=target_arn,
        IntegrationName='`my-integration`'
    )
    print('Creating integration: ' + response['IntegrationName'])

def main():
    """main function"""
    create_source_cluster(source_cluster_name, source_param_group_name)
    wait_for_cluster_availability(source_cluster_name, target_cluster_name)

if __name__ == "__main__":
    main()
```

## Step 3b: Create an AWS Glue catalog for

Amazon SageMaker AI zero-ETL integration

When creating a zero-ETL integration with an Amazon SageMaker AI lakehouse, you
must create an AWS Glue managed catalog in AWS Lake Formation. The target catalog must be an Amazon Redshift
managed catalog. To create an Amazon Redshift managed catalog, first create the
`AWSServiceRoleForRedshift` service-linked role. In the Lake Formation console, add
the `AWSServiceRoleForRedshift` as a read-only administrator.

For more information about the previous tasks, see the following topics.

- For information about creating an Amazon Redshift managed catalog, see [Creating an Amazon Redshift managed catalog in the AWS Glue Data Catalog](../../../lake-formation/latest/dg/create-rms-catalog.md "../../../lake-formation/latest/dg/create-rms-catalog.md") in the
  _AWS Lake Formation Developer Guide_.
- For information about the service-linked role for Amazon Redshift, see [Using
  service-linked roles for Amazon Redshift](../../../redshift/latest/mgmt/using-service-linked-roles.md "../../../redshift/latest/mgmt/using-service-linked-roles.md") in the
  _Amazon Redshift Management Guide_.
- For information about read-only administrator permissions for Lake Formation, see [Lake Formation personas and
  IAM permissions reference](../../../lake-formation/latest/dg/permissions-reference.md "../../../lake-formation/latest/dg/permissions-reference.md") in the
  _AWS Lake Formation Developer Guide_.

### Configure permissions

for the target AWS Glue catalog

Before creating a target catalog for zero-ETL integration, you must create the Lake Formation
target creation role and the AWS Glue data transfer role. Use the Lake Formation target creation
role to create the target catalog. When creating the target catalog, enter the Glue
data transfer role in the **IAM role** field in the
**Access from engines section**.

The target creation role must be a Lake Formation administrator and requires the
following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "lakeformation:RegisterResource",
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "s3:PutEncryptionConfiguration",
 "iam:PassRole",
 "glue:CreateCatalog",
 "glue:GetCatalog",
 "s3:PutBucketTagging",
 "s3:PutLifecycleConfiguration",
 "s3:PutBucketPolicy",
 "s3:CreateBucket",
 "redshift-serverless:CreateNamespace",
 "s3:DeleteBucket",
 "s3:PutBucketVersioning",
 "redshift-serverless:CreateWorkgroup"
 ],
 "Resource": [
 "arn:aws:glue:*:`111122223333`:catalog",
 "arn:aws:glue:*:`111122223333`:catalog/*",
 "arn:aws:s3:::*",
 "arn:aws:redshift-serverless:*:`111122223333`:workgroup/*",
 "arn:aws:redshift-serverless:*:`111122223333`:namespace/*",
 "arn:aws:iam::`111122223333`:role/GlueDataCatalogDataTransferRole"
 ]
 }
 ]
}`

```

The target creation role must have the following trust
relationship.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Username"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The Glue data transfer role is required for MySQL catalog operations and
must have the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DataTransferRolePolicy",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt",
 "glue:GetCatalog",
 "glue:GetDatabase"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The Glue data transfer role must have the following trust
relationship.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "glue.amazonaws.com",
 "redshift.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Next steps

With a source Aurora DB cluster and either an Amazon Redshift target data warehouse or
Amazon SageMaker AI lakehouse, you can create a zero-ETL integration and
replicate data. For instructions, see [Creating Aurora zero-ETL integrations with Amazon Redshift](zero-etl.md "zero-etl.md").
