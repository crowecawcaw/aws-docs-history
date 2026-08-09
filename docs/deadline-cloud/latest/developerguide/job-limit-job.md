# Submit a job requiring limits

You apply a limit by specifying it as a host requirement for the job or job step. If you
don't specify a limit in a step and that step uses an associated resource, the step's usage
isn't counted against the limit when jobs are scheduled..

Some Deadline Cloud submitters enable you to set a host requirement. You can specify the limit's
amount requirement name in the submitter to apply the limit.

If your submitter doesn't support adding host requirements, you can also apply a limit
by editing the job template for the job.

###### To apply a limit to a job step in the job bundle

1. Open the job template for the job using a text editor. The job template is located
   in the job bundle directory for the job. For more information, see [Job bundles](build-job-bundle.md "build-job-bundle.md") in the _Deadline Cloud Developer Guide_.
2. Find the step definition for the step to apply the limit to.
3. Add the following to the step definition. Replace
   `amount.name` with the amount requirement name of your limit.
   For typical use, you should set the `min` value to 1.

YAML

```
  hostRequirements:
    amounts:
    - name: amount.`name`
      min: 1
```

JSON

```
"hostRequirements": {
    "amounts": [
        {
            "name": "`amount.name`",
            "min": "1"
        }
    ]
}
```

You can add multiple limits to a job step as follows. Replace
`amount.name_1` and `amount.name_2`
with the amount requirement names of your limits.

YAML

```
  hostRequirements:
    amounts:
    - name: `amount.name_1`
      min: 1
    - name: `amount.name_2`
      min: 1
```

JSON

```
"hostRequirements": {
    "amounts": [
        {
            "name": "amount.`name_1`",
            "min": "1"
        },
        {
            "name": "amount.`name_2`",
            "min": "1"
        }
    ]
}
```

4. Save the changes to the job template.

## Automate limits with submission hooks

If you want to enforce limits across all job submissions without requiring artists to
manually edit job templates, you can use a [pre-submission hook](https://github.com/aws-deadline/deadline-cloud/blob/mainline/docs/submission-hooks.md "https://github.com/aws-deadline/deadline-cloud/blob/mainline/docs/submission-hooks.md") to automatically inject the host requirement into every job
template at submission time.

A pre-submission hook is a script that runs before the job is submitted. The hook can
modify the job bundle's `template.yaml` to add the
`hostRequirements` amounts entry for your limit. This approach ensures that
every job submitted through the Deadline Cloud CLI or DCC submitters declares its need for
the limited resource.

For a complete working example, see the [license limits submission hook sample](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/submission_hooks/license_limits "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/submission_hooks/license_limits") in the Deadline Cloud samples
repository.

## End-to-end example: Enforce V-Ray license limits

This example shows how to set up a limit for 5 V-Ray floating licenses and verify
that the scheduler enforces it.

###### To set up and test a V-Ray license limit

1. Create the limit on your farm:

```
aws deadline create-limit \
    --farm-id `farm-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` \
    --display-name "VRay License" \
    --amount-requirement-name "amount.vray" \
    --max-count 5
```

2. Associate the limit with your queue:

```
aws deadline create-queue-limit-association \
    --farm-id `farm-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` \
    --queue-id `queue-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` \
    --limit-id `limit-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
```

3. Add the host requirement to your job template:

```
specificationVersion: jobtemplate-2023-09
name: My VRay Render
steps:
  - name: Render
    hostRequirements:
      amounts:
        - name: amount.vray
          min: 1
    script:
      actions:
        onRun:
          command: vray
          args: ["-scene", "{{Param.SceneFile}}"]
```

4. Submit the job. The scheduler allows at most 5 tasks with
   `amount.vray` to run concurrently across all jobs in the queue. Additional
   tasks remain in the `READY` state until a slot becomes available.

To verify the limit is working, temporarily set `maxCount` to 1 and submit
two jobs. The first job runs while the second remains in the `READY` state
until the first completes.
