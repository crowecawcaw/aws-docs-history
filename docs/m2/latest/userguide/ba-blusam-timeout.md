AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Troubleshooting error: Time out while waiting for data set

name to be unlocked

This page describes how you can resolve your error when you see another application in an
environment is holding a lock on a shared data set.

- Engine: AWS Blu Age
- Component: Blusam
  If you see this error in the Amazon CloudWatch logs for a AWS Mainframe Modernization application using the AWS Blu Age engine and
  running in an environment with the High Availability pattern, it indicates that another
  application is holding a lock on a shared data set. Typically, this situation occurs if the other
  application crashes or otherwise fails and does not release the lock.

Look for a failed application and check whether it uses the same data set mentioned in the
error message. Check whether the application is running in a runtime environment with the High
Availability pattern. The application that raised the timeout exception cannot proceed and will
display the `Failed` status.

## Common cause

Application `example-app-1` tries to lock a record `example-record-1`
for a write operation. This operation creates both a lock on data set
`example-dataset-1`, which owns `example-record-1`, and a lock on
`example-record-1` itself. Now another application, `example-app-2`,
tries to lock the same record `example-record-1`. The data set and the record are
already locked, so `example-app-2` waits for the lock to release. If
`example-app-1` crashes, the held lock on dataset `example-dataset-1`
still exists, which causes `example-app-2` to cancel its write attempt and raise a
timeout exception. This deadlock situation prevents all applications from reaching
`example-dataset-1`.

## Resolution

To resolve the situation immediately, you can force the lock to release. To prevent a
similar situation from occurring in the future, you can configure two parameters that control
the Blusam auto repairing mechanism.

## Force the lock to release

The Blusam lock manager uses Amazon ElastiCache (Redis OSS) to provide shared locks between applications. To
release locks in ElastiCache, use the Redis CLI utility. You cannot delete an individual record lock.
You must remove all locks from the owning dataset. Complete the following steps:

1. Connect to your ElastiCache using the following command:

```
redis-cli -h `hostname` -p `port`
```

You can find the details of your ElastiCache in the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/"). 2. Enter your password. 3. Enter the command you want to run, as follows:

| Command                    | Purpose                                                                                                                                                                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `KEYS *`                   | Get all existing keys.                                                                                                                                                                 |
| KEYS \*`YOUR_DATASET_NAME` | Get a dataset lock key.                                                                                                                                                                |
| DEL `THE_RETURNED_KEY`     | Delete a dataset lock.                                                                                                                                                                 |
| FLUSHDB                    | Clean the entire Redis. WarningAll data in the Redis cache will be lost. If the Redis is used for other purposes, such as handling http sessions, you might not want to use `FLUSHDB`. | ## Configure the Blusam auto repairing mechanism The Blusam locks manager includes an auto repairing mechanism to prevent deadlocks on data sets or records. You can adjust the following parameters in the application definition (`application-main.yml`) to configure the auto repairing mechanism: <br>• `locksDeadTime`: refers to the maximum time an application can hold a lock. When this time passes, the lock is declared expired and released immediately. The `locksDeadTime` value is in milliseconds, and the default value is 1000. <br>• `locksCheck`: defines the Blusam locks manager strategy for checking locks. All Blusam locks in ElastiCache are timestamped and have an expiration time. The `locksCheck` parameter value determines whether expired locks are removed. + `off`: no check is executed at any time. Deadlocks might occur. (Not recommended) + `reboot`: checks are executed when an AWS Mainframe Modernization application instance running in an AWS Mainframe Modernization runtime environment is started or rebooted. All expired locks are released immediately. (Default) + `timeout`: checks are executed when an AWS Mainframe Modernization application instance running in an AWS Mainframe Modernization runtime environment is started or rebooted, or when a timeout expires during an attempt to lock a dataset. Expired locks are released immediately. For more information on the application definition for a AWS Blu Age application, see [AWS Blu Age application definition sample](applications-m2-definition.md#applications-m2-definition-ba "applications-m2-definition.md#applications-m2-definition-ba"). ## Blusam locks manager In the context of an AWS Mainframe Modernization runtime environment using the High Availability pattern, a AWS Blu Age application might be deployed multiple times. For those applications that handle Blusam data sets, concurrent access problems might occur. The Blusam locks manager ensures data integrity and manages read and write access to records and data sets by providing shared locks between applications using ElastiCache. This mechanism allows more than one application to read the record concurrently, and ensures that only one application at a time writes the record. ### Write locks To update or delete a specific record, the application must first lock the dataset that owns the record, then lock the record itself. When the record is locked, the dataset lock is released, and other records from the same data set are available for use. When the update or delete operation is complete, the held record lock is released. Only one application at a time can update the record, which blocks other applications from either reading or writing until the lock is released, if the defined application policy allows waiting for release. ### Read locks As long as no write lock is held on the record or the dataset, multiple applications can read the same records at the same time. To lock a record for a write operation, all read locks must be released. ###### Note The Blusam locks manager handles the access from multiple threads in a given application using the same locking mechanism. |
