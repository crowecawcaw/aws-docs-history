Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# System rollback best practices

With automatic system rollback and operations visibility capabilities in Amazon Managed Service for Apache Flink,
you can identify and resolve issues with your applications.

## System

rollbacks

If your application update or scaling operation fails due to a customer error,
such as a code bug or permission issue, Amazon Managed Service for Apache Flink automatically attempts to roll
back to the previous running version if you have opted in to this functionality. For
more information, see [Enable system rollbacks for your Managed Service for Apache Flink
application](how-system-rollbacks.md "how-system-rollbacks.md"). If this autorollback fails or you have
not opted in or opted out, your application will be placed into the
`READY` state. To update your application, complete the following steps:

## Manual

rollback

If the application is not progressing and is in a transient state for long, or if
the application successfully transitioned to `Running`, but you see
downstream issues like processing errors in a successfully updated Flink
application, you can manually roll it back using the
`RollbackApplication` API.

1. Call `RollbackApplication` - this will revert to the previous
   running version and restore the previous state.
2. Monitor the rollback operation using the
   `DescribeApplicationOperation` API.
3. If rollback fails, use the previous system rollback steps.

## Operations

visibility

The `ListApplicationOperations` API shows the history of all customer
and system operations on your application.

1. Get the _operationId_ of the failed
   operation from the list.
2. Call `DescribeApplicationOperation` and check the status and
   _statusDescription_.
3. If an operation failed, the description points to a potential error to
   investigate.

**Common error code bugs:** Use the rollback capabilities
to revert to the last working version. Resolve bugs and retry the update.

**Permission issues:** Use the
`DescribeApplicationOperation` to see the required permissions. Update
application permissions and retry.

**Amazon Managed Service for Apache Flink service issues:** Check the AWS Health Dashboard or open
a support case.
