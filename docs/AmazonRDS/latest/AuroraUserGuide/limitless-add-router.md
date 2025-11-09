# Adding a router to a DB shard group

You can add a router to a DB shard group.

###### Topics

- [Prerequisites](#limitless-add-router.prereqs "#limitless-add-router.prereqs")
- [Adding a router](#limitless-add-router.proc "#limitless-add-router.proc")
- [Tracking router additions](#limitless-add-router.track "#limitless-add-router.track")
- [Canceling a router addition](#limitless-add-router.cancel "#limitless-add-router.cancel")

## Prerequisites

Adding a router has the following prerequisites:

- You must have a DB shard group.
- A user must have the `rds_aurora_limitless_cluster_admin` privilege. The `rds_superuser` has this privilege;
  therefore the master user also has it. The `rds_superuser` can grant the privilege to other users:

```
/* Logged in as the master user or a user with rds_superuser privileges */
CREATE USER `username`;
GRANT rds_aurora_limitless_cluster_admin to `username`;
```

###### Note

If you change your AWS account's default CA certificate after the DB shard group is created, the new router will use the new CA
certificate, which is different from the existing router's CA certificate. Depending on your trust store, some connections might
fail.

- To enable system-initiated router addition, set the following DB cluster parameters in a custom DB cluster parameter group associated
  with your DB cluster:

| Parameter                                 | Value                                           |
| ----------------------------------------- | ----------------------------------------------- |
| `rds_aurora.limitless_enable_auto_scale`  | `on`                                            |
| `rds_aurora.limitless_auto_scale_options` | Either `add_router` or `add_router,split_shard` |

For more information, see [DB cluster parameter groups for Amazon Aurora DB clusters](USER_WorkingWithDBClusterParamGroups.md "USER_WorkingWithDBClusterParamGroups.md").

## Adding a router

To add a router, use the `rds_aurora.limitless_add_router` function. This function starts a router-addition job that runs
asynchronously.

```
SELECT rds_aurora.limitless_add_router();
```

Wait for the return of a job ID upon successful submission of the job, for example:

```
    job_id
---------------
 1691300000000
(1 row)
```

###### Note

Concurrent router addition operations are not supported. Execute operations sequentially and
complete each operation before initiating another addition operation.

## Tracking router additions

You can use the job ID to track a router-addition job. To describe a particular job and get more details about it, run the following
query:

```
SELECT * FROM rds_aurora.limitless_list_router_scale_jobs(`job_id`);
```

For example:

```
SELECT * FROM rds_aurora.limitless_list_router_scale_jobs(1691300000000);

    job_id     |   action   |        job_details       | status  |    submission_time     |                   message
---------------+------------+--------------------------+---------+------------------------+-------------------------------------------
 1691300000000 | ADD_ROUTER | Add 1 new Router by User | SUCCESS | 2023-08-06 05:33:20+00 | Scaling job succeeded.                  +
               |            |                          |         |                        | New router instance with ID 7 was created.
(1 row)
```

The query returns an error when you pass a nonexistent job as the input.

```
SELECT * from rds_aurora.limitless_list_router_scale_jobs(1691300000001);

ERROR:  no job found with the job ID provided
```

You can track the status of all router-addition jobs by using the same query without a job ID, for example:

```
SELECT * FROM rds_aurora.limitless_list_router_scale_jobs();

    job_id     |   action   |        job_details       |   status    |    submission_time     |                  message
---------------+------------+--------------------------+-------------+------------------------+-------------------------------------------
 1691200000000 | ADD_ROUTER | Add 1 new Router by User | IN_PROGRESS | 2023-08-05 01:46:40+00 |
 1691300000000 | ADD_ROUTER | Add 1 new Router by User | SUCCESS     | 2023-08-06 05:33:20+00 | Scaling job succeeded.                +
               |            |                          |             |                        | New router instance with ID 7 was created.
 1691400000000 | ADD_ROUTER | Add 1 new Router by User | FAILED      | 2023-08-07 09:20:00+00 | Error occurred for the add router job 1691400000000.
               |            |                          |             |                        | Retry the command. If the issue persists, contact AWS Support.
 1691500000000 | ADD_ROUTER | Add 1 new Router by User | CANCELED    | 2023-08-07 09:20:00+00 | Scaling job was cancelled.
(4 rows)
```

The job status can be one of the following:

- `IN_PROGRESS` – The router-addition job has been submitted and is in progress. You can have only one job in progress
  at a time.
- `CANCELLATION_IN_PROGRESS` – The router-addition job is being canceled by the user.
- `CANCELED` – The router-addition job has been successfully canceled by the user or by the system.
- `SUCCESS` – The router-addition job completed successfully. The `message` field contains the instance ID
  of the new router.
- `FAILED` – The router-addition job failed. The `message` field contains the details of the failure and
  any actions that can be taken as a followup to the failed job.

###### Note

There's no `PENDING` status because router additions don't need to be finalized. They incur no downtime.

## Canceling a router addition

You can cancel a router addition that's `IN_PROGRESS`. You need the job ID to cancel it.

```
SELECT * from rds_aurora.limitless_cancel_router_scale_jobs(`job_id`);
```

No output is returned unless there's an error. You can track the cancellation using a job-tracking query.
