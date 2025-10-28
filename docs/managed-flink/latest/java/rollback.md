Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Roll back application upgrades

If you have issues with your application or find inconsistencies in your application
code between Flink versions, you can roll back using the AWS CLI, AWS CloudFormation, AWS SDK, or
the AWS Management Console. The following examples show what rolling back looks like in different
failure scenarios.

## Runtime upgrade succeeded, the application is in `RUNNING` state, but the job is failing and continuously restarting

Assume you are trying to upgrade a stateful application named
`TestApplication` from Flink 1.15 to Flink 1.18 in
US East (N. Virginia). However, the upgraded Flink 1.18 application is failing to start
or is constantly restarting, even though the application is in `RUNNING`
state. This is a common failure scenario. To avoid further downtime, we recommend
that you roll back your application immediately to the previous running version
(Flink 1.15), and diagnose the issue later.

To roll back the application to the previous running version, use the [rollback-application](../../../cli/latest/reference/kinesisanalyticsv2/rollback-application.md "../../../cli/latest/reference/kinesisanalyticsv2/rollback-application.md") AWS CLI command or the [RollbackApplication](../apiv2/API_RollbackApplication.md "../apiv2/API_RollbackApplication.md") API action. This API action rolls back the changes
you've made that resulted in the latest version. Then it restarts your application
using the latest successful snapshot.

We strongly recommend that you take a snapshot with your existing app before you
attempt to upgrade. This will help to avoid data loss or having to reprocess data.

In this failure scenario, AWS CloudFormation will not roll back the application for you. You
must update the CloudFormation template to point to the previous runtime and to the
previous code to force CloudFormation to update the application. Otherwise, CloudFormation
assumes that your application has been updated when it transitions to the
`RUNNING` state.

## Rolling back an application that is stuck in `UPDATING`

If your application gets stuck in the `UPDATING` or
`AUTOSCALING` state after an upgrade attempt, Amazon Managed Service for Apache Flink offers the
[rollback-applications](../../../cli/latest/reference/kinesisanalyticsv2/rollback-application.md "../../../cli/latest/reference/kinesisanalyticsv2/rollback-application.md") AWS CLI command, or the [RollbackApplications](../apiv2/API_RollbackApplication.md "../apiv2/API_RollbackApplication.md") API action that can roll back the application to
the version before the stuck `UPDATING` or `AUTOSCALING`
state. This API rolls back the changes that you’ve made that caused the application
to get stuck in `UPDATING` or `AUTOSCALING` transitive
state.
