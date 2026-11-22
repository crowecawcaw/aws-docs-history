

# Using Scaling Profiles

With Amazon EMR Serverless, you can choose how quickly your Apache Spark jobs add and release executors. You set one configuration property, `spark.emr-serverless.scalingProfile`, instead of tuning individual Spark dynamic allocation properties. The property takes one of three profiles:
+ `performance-optimized` – Adds executors as quickly as possible, for the shortest run time.
+ `balanced` – Adds executors more slowly and uses fewer of them.
+ `cost-optimized` – Adds the fewest executors, for the lowest cost.

A scaling profile is a named set of `spark.dynamicAllocation.*` values. EMR Serverless writes the values of the profile that you choose into the job's Spark configuration when the job starts. Any `spark.dynamicAllocation.*` property that you set yourself keeps your value. Starting with release `emr-spark-8.2.0`, Spark jobs and sessions run with the `balanced` profile unless you choose a different one. For details, refer to [How EMR Serverless chooses the profile](#scaling-profiles-resolution).

## Key benefits
<a name="scaling-profiles-benefits"></a>

Scaling Profiles provide the following benefits.
+ One property instead of six – A profile sets up to six `spark.dynamicAllocation.*` properties together, so you change scaling behavior for a job or an application by changing one value.
+ Cost control for batch jobs – The `balanced` and `cost-optimized` profiles wait longer between executor requests. They also aim for half or a third of the executors that the job's tasks could use. As a result, a job with short bursts of waiting tasks runs on fewer executors and accrues less vCPU and memory usage.
+ Latency control for time-sensitive jobs – The `performance-optimized` profile requests executors 1 second after tasks start to wait. Use it for jobs where run time matters more than cost. It keeps the scaling behavior of releases earlier than `emr-spark-8.2.0`.
+ Your settings take precedence – EMR Serverless writes a profile value only for a property that you didn't set, so existing tuning in your jobs and applications keeps working.

## Available profiles
<a name="scaling-profiles-available"></a>

EMR Serverless provides three profiles. Each profile trades job run time against the number of executors that the job uses. The following table lists what each property controls and the value that each profile writes. `performance-optimized` writes the Apache Spark defaults. A dash (–) means that the profile doesn't write the property, so the property keeps its EMR Serverless default. For the defaults, refer to [Spark job properties](jobs-spark.md#spark-defaults).



| Property | What it controls | `performance-optimized` | `balanced` | `cost-optimized` | 
| --- | --- | --- | --- | --- | 
| spark.dynamicAllocation.schedulerBacklogTimeout | How long tasks wait before the job requests its first executors | 1s | 5s | 10s | 
| spark.dynamicAllocation.sustainedSchedulerBacklogTimeout | How often the job requests more executors while tasks still wait | 1s | 15s | 30s | 
| spark.dynamicAllocation.executorAllocationRatio | The share of executors that the job aims for, out of the executors needed to run all running and waiting tasks at once | 1.0 | 0.5 | 0.33 | 
| spark.dynamicAllocation.executorIdleTimeout | How long an executor stays idle before the job releases it | 60s | 60s | 30s | 
| spark.dynamicAllocation.cachedExecutorIdleTimeout | How long an executor that holds cached data stays idle before the job releases it | – | 120s | 60s | 
| spark.dynamicAllocation.maxExecutors | The most executors that the job can use | – | – | 100 | 

## How EMR Serverless chooses the profile
<a name="scaling-profiles-resolution"></a>

EMR Serverless resolves one profile for each job run or session when it starts. It uses the property value that you supply and the release label of the application.
+ You set the property – The job runs with the profile that you set, on any release label.
+ You don't set the property, with release `emr-spark-8.2.0` or higher – The job runs with the `balanced` profile.
+ You don't set the property, with a release earlier than `emr-spark-8.2.0` – EMR Serverless writes no profile values. The job runs with the Apache Spark dynamic allocation defaults, which are the same values that `performance-optimized` writes. Existing jobs on these releases don't change behavior.
+ You set `spark.dynamicAllocation.enabled` to `false` – EMR Serverless applies no profile, because the job doesn't scale its executors.

A profile that you set on the application applies to every job run and session on that application. When you set the property in more than one place, the setting closest to the job run takes precedence:

1. `--conf` in the job's `sparkSubmitParameters` overrides both of the other settings.

1. The `spark-defaults` classification in the job's or session's `configurationOverrides` overrides the application's setting.

1. The `spark-defaults` classification in the application's `runtimeConfiguration` applies only when the job run or session sets neither of the above.

For example, if the application sets `balanced` and the job's `configurationOverrides` sets `cost-optimized`, the job runs with `cost-optimized`. For the full precedence order of Spark properties, refer to [Using Spark configurations when you run EMR Serverless jobs](jobs-spark.md).

After EMR Serverless resolves the profile, it applies the profile one property at a time. For each property in the profile, EMR Serverless writes the profile value only if you didn't set that property at any level. For example, if you choose `cost-optimized` and also set `spark.dynamicAllocation.maxExecutors=500`, the job runs with the `cost-optimized` timeouts and ratio, and with 500 as the executor cap.

## Setting a scaling profile
<a name="scaling-profiles-set"></a>

You can set a scaling profile for every job on an application, for one job run, or for one session. In each case, you set `spark.emr-serverless.scalingProfile` to `performance-optimized`, `balanced`, or `cost-optimized`. EMR Serverless ignores letter case and leading or trailing spaces in the value.

### Setting a profile for an application
<a name="scaling-profiles-set-application"></a>

The following example creates a Spark application on which every job run and session uses the `cost-optimized` profile, unless the job sets a different profile. The `--runtime-configuration` parameter carries the profile. The other parameters are the same as for creating any other application.

```bash
aws emr-serverless create-application \
    --type SPARK \
    --name {{my-application-name}} \
    --release-label emr-spark-8.2.0 \
    --runtime-configuration '[
        {
            "classification": "spark-defaults",
            "properties": {
                "spark.emr-serverless.scalingProfile": "cost-optimized"
            }
        }
    ]' \
    --region {{region}}
```

To change the profile of an existing application, update the application while it's in the `CREATED` or `STOPPED` state. If the application is `STARTED`, `update-application` rejects the change with a `ValidationException`, so stop the application first. The `--runtime-configuration` that you send replaces the application's whole runtime configuration. Include every classification and property that the application needs, not only the scaling profile. Job runs and sessions that start after the update use the new profile.

```bash
aws emr-serverless update-application \
    --application-id {{application-id}} \
    --runtime-configuration '[
        {
            "classification": "spark-defaults",
            "properties": {
                "spark.emr-serverless.scalingProfile": "performance-optimized"
            }
        }
    ]' \
    --region {{region}}
```

### Setting a profile for one job run
<a name="scaling-profiles-set-job-run"></a>

The following example runs one job with the `performance-optimized` profile by passing the property with `--conf` in `sparkSubmitParameters`. This value overrides any profile set on the application.

```bash
aws emr-serverless start-job-run \
    --application-id {{application-id}} \
    --execution-role-arn {{job-role-arn}} \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://{{amzn-s3-demo-bucket}}/scripts/my-script.py",
            "sparkSubmitParameters": "--conf spark.emr-serverless.scalingProfile=performance-optimized"
        }
    }' \
    --region {{region}}
```

You can also set the property in the `spark-defaults` classification of `applicationConfiguration` in the job's `--configuration-overrides`.

```bash
aws emr-serverless start-job-run \
    --application-id {{application-id}} \
    --execution-role-arn {{job-role-arn}} \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://{{amzn-s3-demo-bucket}}/scripts/my-script.py"
        }
    }' \
    --configuration-overrides '{
        "applicationConfiguration": [
            {
                "classification": "spark-defaults",
                "properties": {
                    "spark.emr-serverless.scalingProfile": "balanced"
                }
            }
        ]
    }' \
    --region {{region}}
```

### Setting a profile for a Spark Connect session
<a name="scaling-profiles-set-spark-connect"></a>

The following example starts a Spark Connect session with the `cost-optimized` profile. Sessions take the property in `runtimeConfiguration` inside `--configuration-overrides`. The application must have interactive sessions turned on. To turn them on, pass `--interactive-configuration '{"sessionEnabled": true}'` to `create-application` or `update-application`.

```bash
aws emr-serverless start-session \
    --application-id {{application-id}} \
    --execution-role-arn {{execution-role-arn}} \
    --configuration-overrides '{
        "runtimeConfiguration": [
            {
                "classification": "spark-defaults",
                "properties": {
                    "spark.emr-serverless.scalingProfile": "cost-optimized"
                }
            }
        ]
    }' \
    --region {{region}}
```

### Setting a profile for a Livy or notebook session
<a name="scaling-profiles-set-livy"></a>

With the Livy endpoint, pass the property in the `conf` map of the request that creates the session. The application must have the Livy endpoint turned on (`--interactive-configuration '{"livyEndpointEnabled": true}'`). The following example is the body of a `POST /sessions` request.

```json
{
    "kind": "pyspark",
    "conf": {
        "emr-serverless.session.executionRoleArn": "{{execution-role-arn}}",
        "spark.emr-serverless.scalingProfile": "cost-optimized"
    }
}
```

In a Jupyter notebook that connects through Livy, the `%%configure` magic sends the same `conf` map when it creates the session.

```
%%configure -f
{
    "conf": {
        "spark.emr-serverless.scalingProfile": "cost-optimized"
    }
}
```

## Checking the applied profile
<a name="scaling-profiles-check"></a>

You can check which profile a job ran with in the Spark UI. When EMR Serverless applies a profile, it passes `spark.emr-serverless.scalingProfile` with the resolved profile name to the Spark driver, together with the `spark.dynamicAllocation.*` values that took effect. To see them, open the Spark UI for the job run or session and choose the **Environment** tab. The Spark History Server shows the same values for completed jobs.

The `GetJobRun`, `GetSession`, and `GetApplication` API operations return only the configuration that you sent. A profile that comes from the release default doesn't appear in their responses. For more information, refer to [How EMR Serverless chooses the profile](#scaling-profiles-resolution).

## Considerations and limitations
<a name="scaling-profiles-considerations"></a>
+ Spark only – Scaling Profiles apply to Spark job runs and sessions. The property has no effect on Hive applications.
+ The default changes with `emr-spark-8.2.0` – When you upgrade an application that doesn't set the property to `emr-spark-8.2.0` or higher, its job runs and sessions change from the earlier dynamic allocation defaults to the `balanced` profile. They can run longer on fewer executors. To keep the earlier behavior, set the profile to `performance-optimized` on the application or job.
+ Profiles require dynamic allocation – A profile changes only `spark.dynamicAllocation.*` properties. If you set `spark.dynamicAllocation.enabled` to `false`, EMR Serverless applies no profile, and the job runs with the executor count that you configure.
+ `cost-optimized` caps the job at 100 executors – A job that needs more than 100 executors to meet its run-time target runs longer with `cost-optimized`. To raise the cap, set `spark.dynamicAllocation.maxExecutors` yourself, or choose another profile.
+ `balanced` and `cost-optimized` release executors that hold cached data – Apache Spark keeps an executor that holds cached data until the job ends, unless `spark.dynamicAllocation.cachedExecutorIdleTimeout` is set. These two profiles set it to 120 and 60 seconds, so a job that reads cached data after a longer idle period recomputes that data. To keep cached executors longer, set `spark.dynamicAllocation.cachedExecutorIdleTimeout` yourself.
+ Application capacity limits still apply – A profile doesn't change the application's `maximumCapacity`. When the application reaches its maximum capacity, the job can't add executors, regardless of the profile.
+ The profile is resolved when the job starts – A change to the application's profile applies to job runs and sessions that start after the change.

## Troubleshooting
<a name="scaling-profiles-troubleshooting"></a>

The following are symptoms that you might see when you use Scaling Profiles, and what to do about each.

### The request fails with a ValidationException about scalingProfile
<a name="scaling-profiles-ts-validation"></a>

This happens when the property value isn't one of the three profile names. The error message lists the valid values, for example `Invalid value 'fast' for scalingProfile; valid values are performance-optimized, balanced, cost-optimized`. Correct the value in the application, job, or session configuration, and retry the request.

### The Spark UI doesn't show spark.emr-serverless.scalingProfile
<a name="scaling-profiles-ts-not-shown"></a>

This happens when EMR Serverless applies no profile to the job. Check whether the job sets `spark.dynamicAllocation.enabled` to `false`, or whether the application runs a release earlier than `emr-spark-8.2.0` without the property. For more information, refer to [How EMR Serverless chooses the profile](#scaling-profiles-resolution).

### A dynamic allocation value differs from the profile table
<a name="scaling-profiles-ts-value-differs"></a>

This happens when you set that `spark.dynamicAllocation.*` property yourself at the application, job, or session level. Your value takes precedence over the profile value. To use the profile value, remove your setting.

### A job runs longer after an upgrade to emr-spark-8.2.0
<a name="scaling-profiles-ts-longer-run"></a>

This happens when the job doesn't set the property, so it moves to the `balanced` default. That profile waits longer between executor requests and aims for fewer executors. Set the profile to `performance-optimized` for that job or application, as described in [Setting a scaling profile](#scaling-profiles-set).