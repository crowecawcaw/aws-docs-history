

# Using an external accounting database with SageMaker HyperPod Slurm clusters
<a name="sagemaker-hyperpod-external-accounting-db-slurm"></a>

Slurm stores job history, fairshare data, user associations, and quality of service (QOS) policy in a backing SQL database. By default, SageMaker HyperPod deploys MariaDB on your cluster's controller instance, so accounting works with no database for you to manage.

You can instead use an external MySQL-compatible database that you own, such as an Amazon RDS instance. Storing accounting data outside the controller instance means:
+ Data survives controller instance failures and replacements.
+ Job records persist across cluster updates.
+ Multiple clusters can share one database, accumulating history across clusters that come and go.

HyperPod does not create, host, or manage the database. Provisioning, sizing, patching, backups, and availability remain your responsibility.

**Note**  
An external accounting database requires continuous provisioning. For more information, see [Continuous provisioning for enhanced cluster operations with Slurm](sagemaker-hyperpod-scaling-slurm.md). This feature also requires clusters to run on Amazon Machine Images (AMIs) released after August 30, 2026.

**Important**  
After you attach an external accounting database to a cluster, you cannot revert that cluster to the internal MariaDB database.

## How it works
<a name="sagemaker-hyperpod-external-accounting-db-slurm-how-it-works"></a>

You configure an external accounting database by adding an `AccountingDatabase` object to the `Orchestrator.Slurm` field of a `CreateCluster` or `UpdateCluster` request, or by using the **Accounting database** section of the SageMaker AI console. You provide two required values, the database endpoint and an AWS Secrets Manager secret Amazon Resource Name (ARN), and HyperPod writes the Slurm accounting configuration, connects the Slurm database daemon (`slurmdbd`) to your database, and validates the connection.

When you include `AccountingDatabase` in a `CreateCluster` request, HyperPod validates the configuration, then during provisioning retrieves the database credentials from Secrets Manager using the secret ARN you provided, writes the Slurm accounting configuration on the controller instance, tests connectivity to your database, and starts `slurmdbd` against it. The cluster reaches `InService` only after the accounting database connection succeeds.

Your database credentials are never passed through the API and are never stored by HyperPod. You pass only the secret ARN, and HyperPod persists only that ARN.

When you omit `AccountingDatabase`, the cluster uses the internal MariaDB database on the controller instance and behavior is unchanged.

If the database configuration fails, the cluster does not fall back to the internal MariaDB database. Falling back would mean that jobs run during the gap never record to your database, leaving a permanent gap in your `sacct` history and fairshare records. Instead, cluster creation fails and reports the reason. For more information, see [Troubleshooting](#sagemaker-hyperpod-external-accounting-db-slurm-troubleshooting).

### Responsibilities
<a name="sagemaker-hyperpod-external-accounting-db-slurm-responsibilities"></a>

Because the database is outside of the HyperPod control plane, two concerns remain yours:
+ **Network connectivity** – You own the security groups, subnets, VPC endpoints, and routing that let the controller instance reach the database on the configured port. HyperPod validates the connection but does not configure the network.
+ **Credential management** – You own the Secrets Manager secret, its contents, its rotation policy, and the IAM permissions that let the controller instance read it.

## Prerequisites
<a name="sagemaker-hyperpod-external-accounting-db-slurm-prerequisites"></a>

Complete the following before you create or update a cluster with an `AccountingDatabase`. Because these involve resources that you own, HyperPod cannot create them for you. For more information on the prerequisites, see [Accounting Configuration](https://slurm.schedmd.com/accounting.html#slurm-accounting-configuration-before-build) on the SchedMD website.


| Prerequisite | Detail | 
| --- | --- | 
| External database | MySQL or MariaDB is the preferred database. Slurm accounting supports only the MySQL wire protocol, so engines such as PostgreSQL and SQL Server cannot be used. | 
| Network reachability | The database security group allows inbound traffic on the database port (3306 by default) from the cluster security group. On-premises databases require AWS Direct Connect or a virtual private network (VPN). | 
| Secrets Manager secret | A secret in the same AWS Region as the cluster, containing a JSON object with username and password keys. Secrets managed by Amazon RDS are compatible. | 
| Secrets Manager VPC endpoint | Required for clusters in a custom VPC, with private DNS enabled. | 
| IAM permissions | The cluster execution role must allow secretsmanager:GetSecretValue on the secret ARN. If the secret is encrypted with a customer managed key, the role must also allow kms:Decrypt on that key. | 
| Database user and grants | A database user matching the secret, with the privileges described in [Database user privileges](#sagemaker-hyperpod-external-accounting-db-slurm-privileges) already granted. | 
| Continuous provisioning | The cluster must set NodeProvisioningMode to Continuous and define Slurm topology through the API. | 

### IAM permissions
<a name="sagemaker-hyperpod-external-accounting-db-slurm-iam"></a>

Add the following statements to your cluster execution role. Include the `kms:Decrypt` statement only if your secret is encrypted with a customer managed key.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "arn:aws:secretsmanager:us-west-2:111122223333:secret:slurm-db-credentials-AbCdEf"
        },
        {
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ]
}
```

**Note**  
Reading a secret that is encrypted with a customer managed key requires both `secretsmanager:GetSecretValue` and `kms:Decrypt`. Grant `kms:Decrypt` through an identity-based policy statement scoped to the key ARN rather than through a AWS KMS grant.

Ensure that SSL/TLS is enabled and enforced on the database instance to secure all connections between the application and the database. At minimum, set `ssl-mode=REQUIRED`. Additionally, add server-identity verification (SSL\_CA \+ VERIFY\_CA/VERIFY\_IDENTITY) for any non-loopback or off-VPC endpoint, or gate remote endpoints on verified TLS. Do not allow silent plaintext fallback for endpoints outside the cluster VPC.

Enable the appropriate server-side SSL/TLS configuration and certificates according to the database platform (for example, Amazon RDS for MySQL, Amazon RDS for MariaDB, or Aurora MySQL). For secure connections for Amazon RDS, see the following:
+ [Requiring SSL/TLS for all connections to a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-ssl-connections.require-ssl.html)
+ [Requiring SSL/TLS for all connections to a MariaDB DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-ssl-connections.require-ssl.html)

If you configure the external accounting database in the SageMaker AI console, the IAM role or user that you use to access the console also needs the following permissions. These permissions are separate from the cluster execution role.
+ `secretsmanager:ListSecrets` – Lists your secrets in **Database secret ARN**.
+ `rds:DescribeDBInstances` – Lists your Amazon RDS instances when you choose **Choose an existing RDS instance**.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:ListSecrets",
                "rds:DescribeDBInstances"
            ],
            "Resource": "*"
        }
    ]
}
```

**Note**  
The `secretsmanager:ListSecrets` and `rds:DescribeDBInstances` actions do not support resource-level permissions, so you must set `Resource` to `*` for these actions.

**Note**  
Do not use plaintext database connections in production environments.

### Secret format
<a name="sagemaker-hyperpod-external-accounting-db-slurm-secret-format"></a>

The secret must contain a JSON object with `username` and `password` keys. Additional keys are ignored.

```
{
    "username": "slurm",
    "password": "your-password-EXAMPLE"
}
```

**Important**  
SageMaker AI does not read your secret before you submit the request, so it cannot verify that the secret contains the required keys. If the secret is missing `username` or `password`, cluster creation or the database update fails. Verify the contents of the secret before you submit the request.

### Database user privileges
<a name="sagemaker-hyperpod-external-accounting-db-slurm-privileges"></a>

Grant the privileges on the accounting database (for example, `slurm_acct_db`) that you pre-created:

```
GRANT ALL ON slurm_acct_db.* TO 'username'@'%';
```

Alternatively, to let `slurmdbd` create the database itself, you can change your grant line to `*.*`. For more information, see [MySQL Configuration](https://slurm.schedmd.com/accounting.html#mysql-configuration) on the SchedMD website.

**Important**  
Granting `ALL ON *.*` is not recommended for security reasons. Use this alternative option only for convenience in testing, not production. A database user holding `ALL ON *.*` on a shared server can read, modify, or drop every other cluster's accounting tables and the shared global tables.

```
GRANT ALL ON *.* TO 'username'@'%';
```

**Note**  
The grant host must match how the controller instance connects to the database. Amazon RDS commonly uses `'username'@'%'`. A host-restricted grant that does not cover the controller instance address fails authentication.

**Note**  
The database must use a case-insensitive collation, which is the MySQL and MariaDB default. Slurm rejects case-sensitive collations, and `slurmdbd` reports an error at startup.

## AccountingDatabase reference
<a name="sagemaker-hyperpod-external-accounting-db-slurm-reference"></a>

`AccountingDatabase` is an optional object on the cluster-level `Orchestrator.Slurm` field. Include it in `CreateCluster` to create a cluster that uses an external accounting database, or in `UpdateCluster` to change the database on an existing cluster.

```
"Orchestrator": {
    "Slurm": {
        "AccountingDatabase": {
            "Endpoint": "my-cluster-db.abc123.us-west-2.rds.amazonaws.com",
            "Port": 3306,
            "Name": "slurm_acct_db",
            "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:slurm-db-credentials-AbCdEf"
        }
    }
}
```


| Field | Description | 
| --- | --- | 
| Endpoint | Required. The hostname or IP address of the database server, for example, an Amazon RDS or Aurora endpoint. Cannot be localhost or 127.0.0.1, and cannot include a scheme or port. Maximum 255 characters. | 
| SecretArn | Required. The ARN of the Secrets Manager secret containing the database username and password. The secret must be in the same Region as the cluster. | 
| Port | Optional. The port that the database listens on. Valid range 1–65535. Default: 3306 | 
| Name | Optional. The schema name for Slurm accounting data. 1 to 64 characters, and can contain letters, numbers, dollar signs ($), and underscores (\_). Cannot be a word reserved by the database engine. Use a unique name for each cluster when clusters share a database server. Default: slurm\_acct\_db\_{cluster\_id} | 

## Create a cluster with an external accounting database
<a name="sagemaker-hyperpod-external-accounting-db-slurm-create"></a>

**Important**  
If you provide lifecycle scripts with an external accounting database, you must not create a local accounting database or start `slurmdbd`. Enable it without `--now` and let HyperPod configure and start it; otherwise the setup may fail.

### Using the AWS CLI
<a name="sagemaker-hyperpod-external-accounting-db-slurm-create-cli"></a>

In your `create_cluster.json` file, add an `AccountingDatabase` object to the cluster-level `Orchestrator.Slurm` field:

```
"Orchestrator": {
    "Slurm": {
        "AccountingDatabase": {
            "Endpoint": "my-cluster-db.abc123.us-west-2.rds.amazonaws.com",
            "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:slurm-db-credentials-AbCdEf"
        }
    }
}
```

`Port` and `Name` are omitted, so the cluster uses the defaults `3306` and `slurm_acct_db_{cluster_id}`. The rest of the request is unchanged. Set `NodeProvisioningMode` to `Continuous`, define Slurm topology through `SlurmConfig` on each instance group, and include `VpcConfig` with a security group and subnets that can reach your database. For a complete `CreateCluster` request, see [Continuous provisioning for enhanced cluster operations with Slurm](sagemaker-hyperpod-scaling-slurm.md).

1. Create the cluster:

   ```
   aws sagemaker create-cluster \
       --cli-input-json file://create_cluster.json
   ```

1. Check the status:

   ```
   aws sagemaker describe-cluster --cluster-name my-training-cluster
   ```

   The response echoes the accounting database configuration under `Orchestrator.Slurm`. The secret ARN is returned, but the credentials are not.

   ```
   {
       "ClusterName": "my-training-cluster",
       "ClusterStatus": "InService",
       "Orchestrator": {
           "Slurm": {
               "AccountingDatabase": {
                   "Endpoint": "my-cluster-db.abc123.us-west-2.rds.amazonaws.com",
                   "Port": 3306,
                   "Name": "slurm_acct_db_abc123def456",
                   "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:slurm-db-credentials-AbCdEf"
               }
           }
       }
   }
   ```

   If the accounting database cannot be configured, the cluster status becomes `Failed` and `FailureMessage` describes the cause. For more information, see [Troubleshooting](#sagemaker-hyperpod-external-accounting-db-slurm-troubleshooting).

### Using the console
<a name="sagemaker-hyperpod-external-accounting-db-slurm-create-console"></a>

1. Open the SageMaker AI console and choose **HyperPod clusters**, then **Create cluster**.

1. Choose the custom setup option, and configure your instance groups, networking, and other settings as usual. You must choose an existing VPC and security group that can reach your database.

1. Expand the **Accounting database** section and choose **Use an existing external database**.

1. For **Configuration**, choose one of the following:

   1. **Choose an existing RDS instance** – choose an instance from the list of RDS instances.

   1. **Configure manually** – enter the **Database endpoint**, and optionally the **Database port** and **Database name**. If you leave these blank, HyperPod uses `3306` and `slurm_acct_db_{cluster_id}`.

1. For **Database secret ARN**, enter or choose the Secrets Manager secret that contains your database credentials.

1. Review the prerequisites in the information box, then select **I confirm that the database username and password are specified in the secret, and that all prerequisites are met**.

1. Complete the remaining steps in the wizard and choose **Create cluster**.

## Change the accounting database on an existing cluster
<a name="sagemaker-hyperpod-external-accounting-db-slurm-update"></a>

You can repoint a running cluster at a different database, or attach an external database to a cluster that is using the internal MariaDB database, with a single `UpdateCluster` call.

HyperPod retrieves the credentials from Secrets Manager, rewrites the Slurm accounting configuration, and restarts `slurmdbd` against the new database. Running jobs are not affected, but new accounting records for running jobs will be lost. We recommend that you stop running jobs and migrate the accounting data before you change the database.

**Important**  
Changing the database connection does not move your data. Accounting data in the current database is not migrated automatically. To carry job history, associations, fairshare, and QOS over to the new database, migrate the data before you update the cluster. For more information, see [Migrating accounting data](#sagemaker-hyperpod-external-accounting-db-slurm-migration).

### Using the AWS CLI
<a name="sagemaker-hyperpod-external-accounting-db-slurm-update-cli"></a>

1. Save the following as `update_cluster.json`:

   ```
   {
       "ClusterName": "my-training-cluster",
       "Orchestrator": {
           "Slurm": {
               "AccountingDatabase": {
                   "Endpoint": "new-db.xyz789.us-west-2.rds.amazonaws.com",
                   "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:new-db-credentials-GhIjKl"
               }
           }
       }
   }
   ```

1. Apply the update:

   ```
   aws sagemaker update-cluster \
       --cli-input-json file://update_cluster.json
   ```

   The cluster status changes to `Updating` while the new configuration is applied, then returns to `InService`.

1. Confirm the new configuration:

   ```
   aws sagemaker describe-cluster --cluster-name my-training-cluster
   ```

### Using the console
<a name="sagemaker-hyperpod-external-accounting-db-slurm-update-console"></a>

1. On the cluster details page, choose **Edit**.

1. Expand the **Accounting database** section. If the cluster already uses an external database, **Use the internal MariaDB database** is unavailable, because reverting to the internal MariaDB database is not supported.

1. The section opens in **Configure manually**, with the current endpoint, port, database name, and secret. Update the **Database endpoint**, **Database port**, **Database name**, or **Database secret ARN** as needed. To point the cluster at a different RDS instance, choose **Choose an existing RDS instance** and select it.

1. Review the warning: updating the database connection restarts the Slurm database daemon (`slurmdbd`), and data in the current database isn't migrated.

1. Select the confirmation checkbox, then submit the update.

### If the update fails
<a name="sagemaker-hyperpod-external-accounting-db-slurm-update-fails"></a>

HyperPod validates the new configuration before it commits to it. If validation fails, the cluster keeps running against the previous configuration.


| RollbackStatus | Result | Cluster status | What to do | 
| --- | --- | --- | --- | 
| Absent | The new configuration is applied successfully. | InService, using the new database | Nothing. | 
| NotApplicable | Validation fails before slurmdbd is modified. | InService, using the previous database | Fix the configuration and submit a new update. | 
| Reverted | Validation fails after slurmdbd is modified, and HyperPod restores the previous configuration. | InService, using the previous database | Fix the configuration and submit a new update. No accounting data is lost. | 
| RevertFailed | slurmdbd restart failed after configuration rollback. | InService, but slurmdbd is unhealthy and accounting may not be saved. | Retry with a working database configuration. If this issue persists, contact customer support. | 

Failures are reported as cluster events. For more information, see [SageMaker HyperPod Slurm cluster events](sagemaker-hyperpod-cluster-events-slurm-page.md).

## Verify the configuration
<a name="sagemaker-hyperpod-external-accounting-db-slurm-verify"></a>

To confirm which database a cluster is using, do one of the following:
+ On the cluster details page in the console, review the **Accounting database** panel. **Accounting database** shows `External`, along with the endpoint, port, database name, and secret ARN.
+ Call `describe-cluster` and review `AccountingDatabase` under `Orchestrator.Slurm`.

To verify that accounting is recording jobs, connect to a login or controller instance and run a Slurm accounting command:

```
# Show the accounting configuration that slurmctld is using
scontrol show config | grep -i accounting

# List recent job records from the accounting database
sacct
```

For more information about connecting to cluster instances, see [Getting started with SageMaker HyperPod using the AWS CLI](smcluster-getting-started-slurm-cli.md).

## Rotating database credentials
<a name="sagemaker-hyperpod-external-accounting-db-slurm-rotate"></a>

Rotating the database password is not an `UpdateCluster` operation. Rotate the secret in Secrets Manager and HyperPod applies the new password automatically, with no API call required. `slurmdbd` picks up the change automatically. Running jobs are not affected.

Keep the `username` and `password` keys in place when you rotate the secret. A secret that is missing either key causes the connection to fail.

## Sharing one database across clusters
<a name="sagemaker-hyperpod-external-accounting-db-slurm-sharing"></a>

Multiple HyperPod clusters can record accounting data to a single database. Slurm gives each cluster its own set of tables, prefixed with the cluster name, and shares a small set of global tables. Point each cluster at the same endpoint and database name, and no further configuration is required.

Note the following constraints:
+ Cluster names must be 40 characters or fewer when an external accounting database is configured. Slurm truncates longer names, which can cause two clusters to write to the same tables.
+ Slurm converts cluster names to lowercase to build table prefixes, so cluster names that differ only in capitalization collide. Choose names that differ by more than case.
+ For full isolation between clusters, give each cluster a different `Name` value so that each uses a separate schema on the same database server.

When a cluster starts against a database that already contains tables matching its name prefix, HyperPod emits an informational cluster event. The request still succeeds and the cluster reaches `InService`. This is expected when a controller instance is replaced, when you switch databases, or when you recreate a cluster with a name that was used before. Review the event to confirm that reusing the existing tables is what you intend.

**Note**  
HyperPod does not delete data from your external database when you delete a cluster. If you recreate a cluster with the same name and point it at the same database, `slurmdbd` reuses the existing tables and the earlier data remains. Cleaning up the database is your responsibility.

## Migrating accounting data
<a name="sagemaker-hyperpod-external-accounting-db-slurm-migration"></a>

HyperPod changes the database connection. Moving the data is your responsibility. The following transitions are supported:


| From | To | Supported | 
| --- | --- | --- | 
| Internal MariaDB | External database | Yes | 
| External database | A different external database | Yes | 
| External database configured through lifecycle scripts | External database configured through the API | Yes | 
| External database | Internal MariaDB | No | 

### Migrating from the internal MariaDB database
<a name="sagemaker-hyperpod-external-accounting-db-slurm-migration-mariadb"></a>

Migrating the data preserves job history, associations, fairshare data, QOS, and usage records. The `mysqldump` utility and the `mysql` client are preinstalled on the HyperPod AMI. The username and password to connect to the internal MariaDB database can be found in `/opt/slurm/etc/slurmdbd.conf`.

1. Connect to the controller instance and export the internal database:

   ```
   mysqldump --single-transaction -u slurm -p slurm_acct_db > slurm_backup.sql
   ```

1. Import the data into your external database:

   ```
   mysql -h my-cluster-db.abc123.us-west-2.rds.amazonaws.com -u slurm -p slurm_acct_db < slurm_backup.sql
   ```

1. Update the cluster with the `AccountingDatabase` configuration, as described in [Change the accounting database on an existing cluster](#sagemaker-hyperpod-external-accounting-db-slurm-update).

If you skip the migration, the cluster still works and `slurmdbd` creates the tables it needs, but earlier job history and fairshare usage are not available through `sacct`. If `AccountingStorageEnforce` is configured on your cluster, you must also recreate user associations with `sacctmgr`.

**Note**  
Retrieve the MariaDB username and password before the `UpdateCluster` call to switch the database. That operation erases the username and password.

## Monitoring slurmdbd health
<a name="sagemaker-hyperpod-external-accounting-db-slurm-monitoring"></a>

If `slurmdbd` stops or cannot reach your database, HyperPod emits a `Warn` cluster event—`Slurm component slurmdbd is unhealthy. slurmdbd is not running. Job accounting records are not being written.`—while the cluster stays `InService` and jobs keep running, though accounting records for that period are never written.

## Troubleshooting
<a name="sagemaker-hyperpod-external-accounting-db-slurm-troubleshooting"></a>

Accounting database errors are reported through cluster events for updates, and through `ClusterStatus` and `FailureMessage` for cluster creation. Accounting configuration logs are also delivered to Amazon CloudWatch for the life of the cluster.

Each error is terminal. Correct the underlying cause and submit a new request. The following table lists the error codes you might see.


| Error code | Cause | Resolution | 
| --- | --- | --- | 
| EXTERNAL\_DB\_SECRET\_ACCESS\_FAILED | The controller instance could not read the secret. | Confirm that the execution role allows secretsmanager:GetSecretValue on the secret ARN, and kms:Decrypt on the key if the secret uses a customer managed key. For clusters in a custom VPC, confirm that an Secrets Manager VPC endpoint exists with private DNS enabled. | 
| EXTERNAL\_DB\_SECRET\_FORMAT\_INVALID | The secret is not a JSON object containing username and password keys. | Correct the contents of the secret. | 
| EXTERNAL\_DB\_CONNECTION\_FAILED | The controller instance could not reach the database on the configured endpoint and port. | Confirm that the database security group allows inbound traffic on the database port from the cluster security group, that the endpoint and port are correct, and that subnet routing reaches the database. | 
| EXTERNAL\_DB\_AUTH\_FAILED | The database rejected the credentials. | Confirm that the user and password in the secret are valid, and that the grant host covers the address the controller instance connects from. | 
| EXTERNAL\_DB\_CONFIG\_INVALID | The connection details are malformed. | Correct the Endpoint, Port, Name, or SecretArn, or the content in Secrets Manager, and submit a new request. | 
| EXTERNAL\_DB\_INSUFFICIENT\_PRIVILEGE | The database accepted the credentials, but the user can't create or use the accounting database. | Grant the user the privileges in [Database user privileges](#sagemaker-hyperpod-external-accounting-db-slurm-privileges). | 
| EXTERNAL\_DB\_CLUSTER\_ID\_MISMATCH | The accounting database already records a different Slurm cluster ID for this cluster name than the one Slurm cached on the controller. | Point the cluster at a database name that no other cluster uses, or delete the local cached cluster ID. | 

The following validation errors are returned when you submit the request.


| Error | Resolution | 
| --- | --- | 
| The database endpoint must not be localhost or 127.0.0.1. | Provide the hostname or IP address of a database that is reachable from the cluster VPC. | 
| The database endpoint must not include a scheme or port. | Provide only the hostname, for example my-cluster-db.abc123.us-west-2.rds.amazonaws.com. Set the port with the Port field. | 
| The database name contains unsupported characters. | Use 1 to 64 characters consisting of letters, numbers, dollar signs ($), and underscores (\_), and avoid words reserved by the database engine. | 
| SlurmConfigStrategy is not supported with continuous provisioning. | Remove SlurmConfigStrategy from the request. | 

Database configuration logs are uploaded to the CloudWatch log group `/aws/sagemaker/Clusters/{ClusterName}/{ClusterId}`, stream `SageMakerAccountingDatabaseEvents/{InstanceGroupName}/{instanceId}`.

## Related topics
<a name="sagemaker-hyperpod-external-accounting-db-slurm-related"></a>
+ [Continuous provisioning for enhanced cluster operations with Slurm](sagemaker-hyperpod-scaling-slurm.md)
+ [Getting started with SageMaker HyperPod using the AWS CLI](smcluster-getting-started-slurm-cli.md)
+ [SageMaker HyperPod Slurm cluster operations](sagemaker-hyperpod-operate-slurm.md)
+ [SageMaker HyperPod Slurm cluster events](sagemaker-hyperpod-cluster-events-slurm-page.md)
+ [SageMaker HyperPod multi-head node support](sagemaker-hyperpod-multihead-slurm.md)