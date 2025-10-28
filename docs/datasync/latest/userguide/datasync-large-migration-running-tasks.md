# Running your DataSync transfer tasks

During each of your migration waves, your data transfer usually follows the same
general process:

1. Run an initial full transfer of your data.
2. Verify the data in the destination.
3. Run incremental transfers for any data that might have changed since the
   initial transfer.
4. Cut over operations to your destination location.
5. Review cutover results.

## Running your

tasks

You likely will need to run your DataSync transfer tasks during business hours to
minimize your overall migration time. It's common in these situations to run an
initial full transfer followed by incremental transfers that account for changes
to your source location from users and applications.

To avoid network-related issues during business hours, you can limit the
amount of bandwidth that your tasks use. For more information, see [Setting bandwidth limits for your AWS DataSync
task](configure-bandwidth.md "configure-bandwidth.md").

1. Run an initial full transfer:
   1. [Start your DataSync task](run-task.md "run-task.md") (or tasks if
      you’re running tasks in parallel).
   2. Monitor the progress and performance of your task
      executions.
   3. Verify that your data transferred the way you expect (for example,
      file metadata is preserved).

2. Run incremental transfers:
   1. [Schedule your tasks](task-scheduling.md "task-scheduling.md") to run
      periodically.
   2. Monitor your task executions and fix errors if encountered.

## Performing a

cutover

After your initial and incremental transfers, you can start the process of
cutting over operations to your destination location.

1. Start the scheduled maintenance window.
2. Update your source storage system to be read only for applications and
   users.
3. Run final incremental transfers to copy remaining deltas between your
   source and destination locations.
4. Conduct a thorough data validation (for example, by reviewing CloudWatch
   logs and [task reports](task-reports.md "task-reports.md")).
5. Switch your applications and users to the new environment of your
   destination location.
6. Test application functionality and make sure that users can access
   data in your destination location.
7. Schedule a retrospective meeting to review the transfer with the
   migration teams. Ask the following probing sample questions:
   - Was the cutover successful? If not, what was the issue?
   - Did we use all available bandwidth?
   - Was the source and destination storage fully
     utilized?
   - Can
     we get more data throughput with additional
     tasks?
   - Do we need to plan for a longer maintenance window?

8. If needed, update your migration plan before starting the next
   wave.
