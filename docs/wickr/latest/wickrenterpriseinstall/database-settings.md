

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Database settings
<a name="database-settings"></a>

Wickr Enterprise requires a MySQL 8.0 database. If you are on MySQL 5.7, see [Upgrade to MySQL 8.0](#upgrade-database) to upgrade. We recommend using a database which is external to your Kubernetes cluster, such as Amazon RDS, but you also have the option of deploying an **Internal** MySQL database inside of the Kubernetes cluster as a part of the installation.

## External Database Settings
<a name="external-database-settings"></a>
+ **Hostname**: Hostname or IP address of the database server.
+ **Reader Hostname**: Hostname or IP address of a read-only endpoint for the database server (if available).
+ **Port**: The port which MySQL will be accessed on.
+ **Database Name**: The name of the database created on the server.
+ **Username**: The user which has permissions to access the database.
+ **Password**: The password for that user.
+ **CA Certificate**: A PEM certificate for connecting to the database over TLS.

**Note**  
Ensure that your MySQL installation is using the default latin1 character set with latin1\_swedish\_ci collation. This can be accomplished by verifying that your MySQL server is started with the following flags:  
`"--character-set-server latin1", "--collation-server latin1_swedish_ci"`

## Internal Database Settings
<a name="internal-database-settings"></a>

The internal database type will deploy two StatefulSets into your cluster for a MySQL primary and secondary with binary replication. The secondary does not receive any traffic and is available only for disaster recovery and backups.

**Storage Size**: Size (in gibibytes) of the Persistent Volumes for the database pods.

**Increasing MySQL Storage Size**

**Note**  
The volume type of your StorageClass must support volume expansion in order to increase the storage size. For more information, see [Volume expansion](https://kubernetes.io/docs/concepts/storage/storage-classes/#allow-volume-expansion).

The MySQL services used in Wickr Enterprise are deployed as StatefulSet resources in Kubernetes. StatefulSets make many properties of the resource immutable, including the Persistent Volume Claim templates. As a workaround for the immutability of StatefulSets, the following actions must be performed to increase the size of volumes used by MySQL.

1. Edit the Persistent Volume Claims for `data-mysql-primary-0` and `data-mysql-secondary-0`.

   1. `kubectl -n wickr edit pvc data-mysql-primary-0. Set spec.resources.requests.storage` to the desired storage size.

   1. `kubectl -n wickr edit pvc data-mysql-secondary-0. Set spec.resources.requests.storage` to the desired storage size.

1. Delete the existing StatefulSets, but leave the Pods by passing the `--cascade=orphan` flag.

   `kubectl -n wickr delete statefulset --cascade=orphan mysql-primary mysql-secondary`.

1. In the KOTS UI, update the Storage Size setting to match the value you set in Step 1. Save and deploy this configuration.

1. Restart the StatefulSets to expand the volumes and bring the MySQL services back online.

   `kubectl -n wickr rollout restart statefulset mysql-primary mysql-secondary`.

## Upgrade to MySQL 8.0
<a name="upgrade-database"></a>

**External Database (RDS)**

To take Wickr Backend offline, complete the following steps.

1. Find the namespace of ingress `kubectl get deployments --all-namespaces`

   In the example below, the namespace is Wickr and replicas is 3.

   ```
   NAMESPACE     NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
   ...
   wickr         ingress-nginx-controller   3/3     3            3           43h
   ...
   ```

1. Scale down ingress `kubectl scale deployment/ingress-nginx-controller --replicas=0 -n wickr`

1. Take a snapshot to backup DB. For more information, see [ Managing manual backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingManualBackups.html) in the *Amazon Relational Database Service User Guide*.

1. Upgrade the engine version to MySQL 8.0.x (MySQL 8.4 is not supported). For more information, see [ Upgrading a DB instance engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html) in the *Amazon Relational Database Service User Guide*.

To bring Wickr Backend online, scale back ingress `kubectl scale deployment/ingress-nginx-controller --replicas=3 -n wickr`

**Internal Database**

For more information, see [Backup and Restore MySQL](https://github.com/aws-samples/sample-packages-for-aws-wickr/blob/main/docs/mysql-backup.md).