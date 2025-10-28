# Job monitoring and

debugging

You can collect metrics about AWS Glue jobs and visualize them on the AWS Glue and Amazon CloudWatch
consoles to identify and fix issues. Profiling your AWS Glue jobs requires the following
steps:

1. Enable metrics:
   1. Enable the **Job metrics** option in the job definition.
      You can enable profiling in the AWS Glue console or as a parameter to the job.
      For more information see [Defining job properties for Spark jobs](add-job.md#create-job "add-job.md#create-job")
      or [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").
   2. Enable the **AWS Glue Observability metrics** option in the job definition. You can enable Observability in the
      AWS Glue console or as a parameter to the job. For more information see
      [Monitoring with AWS Glue Observability metrics](monitor-observability.md "monitor-observability.md").

2. Confirm that the job script initializes a `GlueContext`. For example, the following
   script snippet initializes a `GlueContext` and shows where profiled code is
   placed in the script. This general format is used in the debugging scenarios that
   follow.

```

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import time

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
**glueContext = GlueContext(sc)**
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

...
...
`code-to-profile`
...
...


job.commit()

```

3. Run the job.
4. Visualize the metrics:
   1. Visualize job metrics on the AWS Glue console and identify abnormal metrics for the
      driver or an executor.
   2. Check observability metrics in the Job run monitoring page, job run details page, or on
      Amazon CloudWatch. For more information, see [Monitoring with AWS Glue Observability metrics](monitor-observability.md "monitor-observability.md").

5. Narrow down the root cause using the identified metric.
6. Optionally, confirm the root cause using the log stream of the identified driver or job executor.

**Use cases for AWS Glue observability metrics**

- [Debugging OOM exceptions and job
  abnormalities](monitor-profile-debug-oom-abnormalities.md "monitor-profile-debug-oom-abnormalities.md")
- [Debugging demanding stages and
  straggler tasks](monitor-profile-debug-straggler.md "monitor-profile-debug-straggler.md")
- [Monitoring the progress of multiple
  jobs](monitor-debug-multiple.md "monitor-debug-multiple.md")
- [Monitoring for DPU capacity planning](monitor-debug-capacity.md "monitor-debug-capacity.md")
- [Using AWS Glue Observability for monitoring resource utilization to reduce cost](https://aws.amazon.com/blogs/big-data/enhance-monitoring-and-debugging-for-aws-glue-jobs-using-new-job-observability-metrics "https://aws.amazon.com/blogs/big-data/enhance-monitoring-and-debugging-for-aws-glue-jobs-using-new-job-observability-metrics")
