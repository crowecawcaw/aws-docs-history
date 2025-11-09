# Migrate from KCL 2.x to KCL

3.x

This topic provides step-by-step instructions to migrate your consumer from
KCL 2.x to KCL 3.x. KCL 3.x supports in-place migration of
KCL 2.x consumers. You can continue consuming the data from your Kinesis data
stream while migrating your workers in a rolling manner.

###### Important

KCL 3.x maintains the same interfaces and methods as KCL 2.x.
Therefore you don’t have to update your record processing code during the migration.
However, you must set the proper configuration and check the required steps for the
migration. We highly recommend that you follow the following migration steps for a
smooth migration experience.

## Step 1: Prerequisites

Before you start using KCL 3.x, make sure that you have the
following:

- Java Development Kit (JDK) 8 or later
- AWS SDK for Java 2.x
- Maven or Gradle for dependency management

###### Important

Do not use AWS SDK for Java version 2.27.19 to 2.27.23 with KCL 3.x. These
versions include an issue that causes an exception error related to
KCL's DynamoDB usage. We recommend that you use the AWS SDK for Java version
2.28.0 or later to avoid this issue.

## Step 2: Add dependencies

If you're using Maven, add the following dependency to your `pom.xml`
file. Make sure you replaced 3.x.x to the latest KCL version.

```
<dependency>
    <groupId>software.amazon.kinesis</groupId>
    <artifactId>amazon-kinesis-client</artifactId>
    <version>3.x.x</version> <!-- Use the latest version -->
</dependency>
```

If you're using Gradle, add the following to your `build.gradle` file.
Make sure you replaced 3.x.x to the latest KCL version.

```
implementation 'software.amazon.kinesis:amazon-kinesis-client:3.x.x'
```

You can check for the latest version of the KCL on the [Maven Central Repository](https://search.maven.org/artifact/software.amazon.kinesis/amazon-kinesis-client "https://search.maven.org/artifact/software.amazon.kinesis/amazon-kinesis-client").

## Step 3: Set up the

migration-related configuration

To migrate from KCL 2.x to KCL 3.x, you must set the following configuration
parameter:

- CoordinatorConfig.clientVersionConfig: This configuration determines which
  KCL version compatibility mode the application will run in. When
  migrating from KCL 2.x to 3.x, you need to set this configuration to
  `CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`. To set this
  configuration, add the following line when creating your scheduler
  object:

```
configsBuilder.coordiantorConfig().clientVersionConfig(ClientVersionConfig.CLIENT_VERSION_CONFIG_COMPLATIBLE_WITH_2X)
```

The following is an example of how to set the
`CoordinatorConfig.clientVersionConfig` for migrating from
KCL 2.x to 3.x. You can adjust other configurations as needed based on your
specific requirements:

```
Scheduler scheduler = new Scheduler(
    configsBuilder.checkpointConfig(),
    configsBuilder.coordiantorConfig().clientVersionConfig(ClientVersionConfig.CLIENT_VERSION_CONFIG_COMPLATIBLE_WITH_2X),
    configsBuilder.leaseManagementConfig(),
    configsBuilder.lifecycleConfig(),
    configsBuilder.metricsConfig(),
    configsBuilder.processorConfig(),
    configsBuilder.retrievalConfig()
);
```

It's important that all workers in your consumer application use the same load
balancing algorithm at a given time because KCL 2.x and 3.x use different
load balancing algorithms. Running workers with different load balancing algorithms
can cause suboptimal load distribution as the two algorithms operate
independently.

This KCL 2.x compatibility setting allows your KCL 3.x
application to run in a mode compatible with KCL 2.x and use the load
balancing algorithm for KCL 2.x until all workers in your consumer
application have been upgraded to KCL 3.x. When the migration is complete,
KCL will automatically switch to full KCL 3.x functionality mode
and start using a new KCL 3.x load balancing algorithm for all running
workers.

###### Important

If you are not using `ConfigsBuilder` but creating a
`LeaseManagementConfig` object to set configurations, you must
add one more parameter called `applicationName` in KCL
version 3.x or later. For details, see [Compilation error with the LeaseManagementConfig constructor](troubleshooting-consumers.md#compiliation-error-leasemanagementconfig "troubleshooting-consumers.md#compiliation-error-leasemanagementconfig"). We
recommend using `ConfigsBuilder` to set KCL configurations.
`ConfigsBuilder` provides a more flexible and maintainable way to
configure your KCL application.

## Step 4: Follow best practices for

the shutdownRequested() method implementation

KCL 3.x introduces a feature called _graceful lease handoff_ to
minimize the reprocessing of data when a lease is handed over to another worker as
part of the lease reassignment process. This is achieved by checkpointing the last
processed sequence number in the lease table before the lease handoff. To ensure the
graceful lease handoff works properly, you must make sure that you invoke the
`checkpointer` object within the `shutdownRequested`
method in your `RecordProcessor` class. If you're not invoking the
`checkpointer` object within the `shutdownRequested`
method, you can implement it as illustrated in the following example.

###### Important

- The following implementation example is a minimal requirement for the
  graceful lease handoff. You can extend it to include additional logic
  related to the checkpointing if needed. If you are performing any
  asynchronous processing, make sure that all delivered records to the
  downstream were processed before invoking checkpointing.
- While graceful lease handoff significantly reduces the likelihood of
  data reprocessing during lease transfers, it does not entirely eliminate
  this possibility. To preserve data integrity and consistency, design
  your downstream consumer applications to be idempotent. This means they
  should be able to handle potential duplicate record processing without
  adverse effects on the overall system.

```
/**
 * Invoked when either Scheduler has been requested to gracefully shutdown
 * or lease ownership is being transferred gracefully so the current owner
 * gets one last chance to checkpoint.
 *
 * Checkpoints and logs the data a final time.
 *
 * @param shutdownRequestedInput Provides access to a checkpointer, allowing a record processor to checkpoint
 *                               before the shutdown is completed.
 */
public void shutdownRequested(ShutdownRequestedInput shutdownRequestedInput) {
    try {
       // Ensure that all delivered records are processed
       // and has been successfully flushed to the downstream before calling
       // checkpoint
       // If you are performing any asynchronous processing or flushing to
       // downstream, you must wait for its completion before invoking
       // the below checkpoint method.
        log.info("Scheduler is shutting down, checkpointing.");
        shutdownRequestedInput.checkpointer().checkpoint();
    } catch (ShutdownException | InvalidStateException e) {
        log.error("Exception while checkpointing at requested shutdown. Giving up.", e);
    }
}
```

## Step 5: Check the

KCL 3.x prerequisites for collecting worker metrics

KCL 3.x collects CPU utilization metrics such as CPU utilization from
workers to balance the load across workers evenly. Consumer application workers can
run on Amazon EC2, Amazon ECS, Amazon EKS, or AWS Fargate. KCL 3.x can collect CPU
utilization metrics from workers only when the following prerequisites are
met:

**Amazon Elastic Compute Cloud(Amazon EC2)**

- Your operating system must be Linux OS.
- You must enable [IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") in your EC2 instance.

**Amazon Elastic Container Service (Amazon ECS) on Amazon EC2**

- Your operating system must be Linux OS.
- You must enable [ECS task metadata endpoint version 4](../../../AmazonECS/latest/developerguide/ec2-metadata.md "../../../AmazonECS/latest/developerguide/ec2-metadata.md").
- Your Amazon ECS container agent version must be 1.39.0 or later.

**Amazon ECS on AWS Fargate**

- You must enable [Fargate task metadata endpoint version 4](../../../AmazonECS/latest/developerguide/task-metadata-endpoint-v4-fargate.md "../../../AmazonECS/latest/developerguide/task-metadata-endpoint-v4-fargate.md"). If you use Fargate
  platform version 1.4.0 or later, this is enabled by default.
- Fargate platform version 1.4.0 or later.

**Amazon Elastic Kubernetes Service (Amazon EKS) on Amazon EC2**

- Your operating system must be Linux OS.

**Amazon EKS on AWS Fargate**

- Fargate platform 1.3.0 or later.

###### Important

If KCL 3.x cannot collect CPU utilization metrics from workers
because prerequisites are not met, it will rebalance the load the throughput
level per lease. This fallback rebalancing mechanism will make sure all workers
will get similar total throughput levels from leases assigned to each worker.
For more information, see [How KCL assigns leases to workers and
balances the load](kcl-dynamoDB.md#kcl-assign-leases "kcl-dynamoDB.md#kcl-assign-leases").

## Step 6: Update IAM

permissions for KCL 3.x

You must add the following permissions to the IAM role or policy associated with
your KCL 3.x consumer application. This involves updating the existing IAM policy
used by the KCL application. For more information, see [IAM permissions required for KCL
consumer applications](kcl-iam-permissions.md "kcl-iam-permissions.md").

###### Important

Your existing KCL applications might not have the following IAM actions and
resources added in the IAM policy because they were not needed in KCL 2.x.
Make sure that you have added them before running your KCL 3.x
application:

- Actions: `UpdateTable`
  - Resources (ARNs):
    `arn:aws:dynamodb:region:account:table/KCLApplicationName`

- Actions: `Query`
  - Resources (ARNs):
    `arn:aws:dynamodb:region:account:table/KCLApplicationName/index/*`

- Actions: `CreateTable`, `DescribeTable`,
  `Scan`, `GetItem`, `PutItem`,
  `UpdateItem`, `DeleteItem`

      + Resources (ARNs):
       `arn:aws:dynamodb:region:account:table/KCLApplicationName-WorkerMetricStats`,
       `arn:aws:dynamodb:region:account:table/KCLApplicationName-CoordinatorState`

  Replace "region," "account," and "KCLApplicationName" in the ARNs with
  your own AWS Region, AWS account number, and KCL
  application name respectively. If you use configurations to customize
  names of the metadata tables created by KCL, use those
  specified table names instead of KCL application name.

## Step 7: Deploy KCL 3.x code to your workers

After you have set the configuration required for the migration and completed the
all previous migration checklists, you can build and deploy your code to your
workers.

###### Note

If you see a compilation error with the `LeaseManagementConfig`
constructor, see [Compilation error with the LeaseManagementConfig constructor](troubleshooting-consumers.md#compilation-error-leasemanagementconfig "troubleshooting-consumers.md#compilation-error-leasemanagementconfig") for
troubleshooting information.

## Step 8: Complete the

migration

During the deployment of KCL 3.x code, KCL continues using the
lease assignment algorithm from KCL 2.x. When you have successfully
deployed KCL 3.x code to all of your workers, KCL automatically
detects this and switches to the new lease assignment algorithm based on resource
utilization of the workers. For more details about the new lease assignment
algorithm, see [How KCL assigns leases to workers and
balances the load](kcl-dynamoDB.md#kcl-assign-leases "kcl-dynamoDB.md#kcl-assign-leases").

During the deployment, you can monitor the migration process with the following
metrics emitted to CloudWatch. You can monitor metrics under the `Migration`
operation. All metrics are per-KCL-application metrics and set to the
`SUMMARY` metric level. If the `Sum` statistic of the
`CurrentState:3xWorker` metric matches the total number of workers in
your KCL application, it indicates that the migration to KCL 3.x
has successfully completed.

###### Important

It takes at least 10 minutes for KCL to switch to the new leasee
assignment algorithm after all workers are ready to run it.

| CloudWatch metrics for the KCL migration process | Metrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `CurrentState:3xWorker`                          | The number of KCL workers successfully migrated to<br>KCL 3.x and running the new lease assignment<br>algorithm. If the `Sum` count of this metric matches<br>the total number of your workers, it indicates that the<br>migration to KCL 3.x has successfully<br>completed.<br>• Metric level: Summary<br>• Units: Count<br>• Statistics: The most useful statistic is<br>`Sum`                                                                                                                                                     |
| `CurrentState:2xCompatibleWorker`                | The number of KCL workers running in KCL 2.x<br>compatible mode during the migration process. A non-zero value<br>for this metric indicates that the migration is still in<br>progress.<br>• Metric level: Summary<br>• Units: Count<br>• Statistics: The most useful statistic is<br>`Sum`                                                                                                                                                                                                                                          |
| `Fault`                                          | The number of exceptions encountered during the migration<br>process. Most of these exceptions are transient errors, and KCL<br>3.x will automatically retry to complete the migration. If you<br>observe a persistent `Fault` metric value, review<br>your logs from the migration period for further troubleshooting.<br>If the issue continues, contact Support.<br>• Metric level: Summary<br>• Units: Count<br>• Statistics: The most useful statistic is<br>`Sum`                                                              |
| `GsiStatusReady`                                 | The status of the global secondary index (GSI) creation on the<br>lease table. This metric indicates whether the GSI on the lease<br>table has been created, a prerequisite to run KCL 3.x. The value<br>is 0 or 1, with 1 indicating successful creation. During a<br>rollback state, this metric will not be emitted. After you roll<br>forward again, you can resume monitoring this metric.<br>• Metric level: Summary<br>• Units: Count<br>• Statistics: The most useful statistic is<br>`Sum`                                  |
| `workerMetricsReady`                             | Status of worker metrics emission from all workers. The<br>metrics indicates whether all workers are emitting metrics like<br>CPU utilization. The value is 0 or 1, with 1 indicating all<br>workers are successfully emitting metrics and ready for the new<br>lease assignment algorithm. During a rollback state, this metric<br>will not be emitted. After you roll forward again, you can<br>resume monitoring this metric.<br>• Metric level: Summary<br>• Units: Count<br>• Statistics: The most useful statistic is<br>`Sum` |

KCL provides rollback capability to the 2.x compatible mode during
migration. After successful migration to KCL 3.x is successful, we
recommend that you remove the `CoordinatorConfig.clientVersionConfig`
setting of `CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X` if rollback is no
longer needed. Removing this configuration stops the emission of migration-related
metrics from the KCL application.

###### Note

We recommend that you monitor your application's performance and stability for
a period during the migration and after completing the migration. If you observe
any issues, you can rollback workers to use KCL 2.x compatible
functionality using the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py").
