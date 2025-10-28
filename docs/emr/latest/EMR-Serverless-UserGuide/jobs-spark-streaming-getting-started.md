# Getting started streaming

jobs

See the following instructions to learn how to get started with streaming jobs.

1. Follow [Getting started with Amazon EMR Serverless to create an application.](getting-started.md "getting-started.md") Note that your application
   must run [Amazon EMR release 7.1.0](../ReleaseGuide/emr-710-release.md "../ReleaseGuide/emr-710-release.md") or higher.
2. Once your application is ready, set the `mode` parameter to `STREAMING` to submit a streaming job, similar to the following AWS CLI example.

```
aws emr-serverless start-job-run \
--application-id `<APPPLICATION_ID>` \
--execution-role-arn `<JOB_EXECUTION_ROLE>` \
--mode 'STREAMING' \
--job-driver '{
    "sparkSubmit": {
        "entryPoint": "s3://`<streaming script>`",
        "entryPointArguments": ["s3://`<DOC-EXAMPLE-BUCKET-OUTPUT>`/output"],
        "sparkSubmitParameters": "--conf spark.executor.cores=4
            --conf spark.executor.memory=16g
            --conf spark.driver.cores=4
            --conf spark.driver.memory=16g
            --conf spark.executor.instances=3"
    }
}'
```
