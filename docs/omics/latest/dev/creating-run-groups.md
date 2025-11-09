# Using HealthOmics run groups

You can optionally create a run group to cap the compute resources for the runs that you add to the group. Run
groups can help you:

- Queue your runs so that you don’t exceed service limits.
- Catch run-away tasks by setting a maximum run duration.
- Manage the priority of each run so that the most important runs complete first.
  If you set the maximum concurrent vCPU, GPU, or runs, run tasks will queue when the maximum is reached. If you
  set a maximum run duration, the run fails if it exceeds the maximum duration.

Use the run priority setting to establish priority within a run group.

Service limits take precedence over run group limits. For instance, if you set a run group maximum to a higher
value than your service maximum in a region, HealthOmics applies the service maximum.

###### Topics

- [Run priority](#run-priority "#run-priority")
- [Create a run group using the console](#console-create-run-group "#console-create-run-group")
- [Create a run group using the CLI](#api-create-run-group "#api-create-run-group")
- [Delete a run group using the console](#console-delete-run-group "#console-delete-run-group")
- [Delete a run group using the CLI](#api-delete-run-group "#api-delete-run-group")

## Run priority

You can use run priority to establish the priority of runs in a run group.

If multiple runs have the same priority, the run that started first has the higher priority.

You can also set a priority for a run that isn't in a run group. The priority is compared with the
priorities of all other runs that aren't in a run group

You set run priority when you start the run. For more information, see
[Start a run in HealthOmics](starting-a-run.md "starting-a-run.md").

## Create a run group using the console

###### To create a run group

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Run groups**.
3. On the **Run groups** page, choose **Create
   run group**.
4. On the **Create run group details** page, provide the
   following information
   - **Run group name** - A unique name for this
     run group.
   - **Max vCPU for concurrent runs** - The maximum number of vCPUs that can run
     concurrently across all active runs in the run group.
   - **Max GPUs** - The maximum number of GPUs that can run concurrently across all active
     runs in the run group.
   - **Max run time (mins) per run** - The maximum time for each run (in minutes). If a run exceeds
     the maximum run time, the run fails automatically.
   - **Max concurrent runs** - The maximum number of runs that can be running at the
     same time.

5. (optional) You can add up to 50 **tags** to the run group.
6. Choose **Create run group**.

## Create a run group using the CLI

To create a run group, use the **create-run-group** API operation to create a run group
named `TestRunGroup`. The following example sets a maximum of 20 CPUs, 10 GPUs, 5 runs, and a maximum
run duration of 600 minutes.

```
aws omics create-run-group --name TestRunGroup \
--max-cpus 20 \
--max-gpus 10 \
--max-duration 600 \
--max-runs 5
```

The response from this API operation includes the ID of the newly created `RunGroup`.

```
{
    "arn": "arn:aws:omics:us-west-2:12345678901:runGroup/2839621",
    "id": "2839621",
    "tags": {}
}
```

To get additional information about the run group, use this ID with the **get-run-group** API operation, as shown
in the following example.

```
aws omics get-run-group --id ``run group id``
```

The response includes the limit settings for the run group and the assigned tags.

```
{
    "arn": "arn:aws:omics:us-west-2:776893852117:runGroup/2839621",
    "id": "2839621",
    "name": "TestRunGroup",
    "maxCpus": 20,
    "maxRuns": 5,
    "maxDuration": 600,
    "creationTime": "2024-06-12T15:35:39.191730+00:00",
    "tags": {},
    "maxGpus": 10
}
```

You can also use the **list-run-group** API operation to view all
created run groups.

```
aws omics list-run-groups
```

## Delete a run group using the console

You can delete a run group if there are no
runs associated with that run group with the status of `PENDING`,
`STARTING`, `RUNNING`, or `STOPPING`.

To delete a run group, follow these steps.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Run groups**.
3. On the **Run groups** page, choose the run group
   to delete and choose **Delete** in the xx.

## Delete a run group using the CLI

You can delete a run group if there are no
runs associated with that run group with the status of `PENDING`,
`STARTING`, `RUNNING`, or `STOPPING`.

The following example shows how you can use the AWS CLI to delete a run group. You
will not receive a response. To run the example, replace the `run group id` with the ID of the run group you want to delete.

```
aws omics delete-run-group --id `run group id`
```
