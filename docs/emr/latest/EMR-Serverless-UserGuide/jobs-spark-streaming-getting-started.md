

# Getting started streaming jobs
<a name="jobs-spark-streaming-getting-started"></a>

See the following instructions to learn how to get started with streaming jobs.

1. Follow [Getting started with Amazon EMR Serverless to create an application.](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html) Note that your application must run [Amazon EMR release 7.1.0 ](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-710-release.html)or higher.

1. Once your application is ready, set the `mode` parameter to `STREAMING` to submit a streaming job, similar to the following AWS CLI example.

   ```
   aws emr-serverless start-job-run \
   --application-id {{<APPPLICATION_ID>}} \
   --execution-role-arn {{<JOB_EXECUTION_ROLE>}} \
   --mode 'STREAMING' \
   --job-driver '{
       "sparkSubmit": {
           "entryPoint": "s3://{{<streaming script>}}",
           "entryPointArguments": ["s3://{{<DOC-EXAMPLE-BUCKET-OUTPUT>}}/output"],
           "sparkSubmitParameters": "--conf spark.executor.cores=4
               --conf spark.executor.memory=16g 
               --conf spark.driver.cores=4
               --conf spark.driver.memory=16g 
               --conf spark.executor.instances=3"
       }
   }'
   ```