Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Enable system rollbacks for your Managed Service for Apache Flink

application

With system-rollback capability, you can achieve higher availability of your
running Apache Flink application on Amazon Managed Service for Apache Flink. Opting into this configuration
enables the service to automatically revert the application to the previously
running version when an action such as `UpdateApplication` or
`autoscaling` runs into code or configurations bugs.

###### Note

To use the system rollback feature, you must opt in by updating your application.
Existing applications will not automatically use system rollback by default.

## How it works

When you initiate an application operation, such as an update or scaling action,
the Amazon Managed Service for Apache Flink first attempts to run that operation. If it detects issues that
prevent the operation from succeeding, such as code bugs or insufficient
permissions, the service automatically initiates a `RollbackApplication`
operation.

The rollback attempts to restore the application to the previous version that ran
successfully, along with the associated application state. If the rollback is
successful, your application continues processing data with minimal downtime using
the previous version. If the automatic rollback also fails, Amazon Managed Service for Apache Flink
transitions the application to the `READY` status, so that you can take
further actions, including fixing the error and retrying the operation.

You must opt in to use automatic system rollbacks. You can enable it using the
console or API for all operations on your application from this point forward.

The following example request for the `UpdateApplication` action
enables system rollbacks for an application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 1,
   "ApplicationConfigurationUpdate": {
      "ApplicationSystemRollbackConfigurationUpdate": {
         "RollbackEnabledUpdate": "true"
       }
    }
}
```

## Review common scenarios for automatic system

rollback

The following scenarios illustrate where automatic system rollbacks are
beneficial:

- **Application updates:** If you update your application with new
  code that has bugs when initializing the Flink job through the main method,
  the automatic rollback allows the previous working version to be restored.
  Other update scenarios where system rollbacks are helpful include:
  - If your application is updated to run with a parallelism higher than
    [maxParallelism](how-scaling.md#how-scaling-auto "how-scaling.md#how-scaling-auto").
  - If your application is updated to run with incorrect subnets for a VPC
    application that results in a failure during the Flink job startup.

- **Flink version upgrades:** When you upgrade to a new Apache
  Flink version and the upgraded application encounters a snapshot
  compatibility issue, system rollback lets you revert to the prior Flink
  version automatically.
- **AutoScaling:** When the application scales up but runs into
  issues restoring from a savepoint, due to operator mismatch between the
  snapshot and the Flink job graph.

## Use operation APIs for system rollbacks

To provide better visibility, Amazon Managed Service for Apache Flink has two APIs related to application
operations that can help you track failures and related system rollbacks.

`**ListApplicationOperations**`

This API lists all operations performed on the application, including
`UpdateApplication`, `Maintenance`,
`RollbackApplication`, and others in reverse chronological order. The
following example request for the `ListApplicationOperations` action
lists the first 10 application operations for the application:

```
{
   "ApplicationName": "MyApplication",
   "Limit": 10
}
```

This following example request for `ListApplicationOperations` helps
filter the list to previous updates on the application:

```
{
   "ApplicationName": "MyApplication",
   "operation": "UpdateApplication"
}
```

`**DescribeApplicationOperation**`

This API provides detailed information about a specific operation listed by
`ListApplicationOperations`, including the reason for failure, if
applicable. The following example request for the
`DescribeApplicationOperation` action lists details for a specific
application operation:

```
{
   "ApplicationName": "MyApplication",
   "OperationId": "xyzoperation"
}
```

For troubleshooting information, see
[System rollback best practices](troubleshooting-system-rollback.md "troubleshooting-system-rollback.md").
