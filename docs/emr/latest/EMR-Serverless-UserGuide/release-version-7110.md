# EMR Serverless 7.11.0

The following table lists the application versions available with
EMR Serverless 7.11.0.

| Application  | Version |
| ------------ | ------- |
| Apache Spark | 3.5.6   |
| Apache Hive  | 3.1.3   |
| Apache Tez   | 0.10.2  |

###### EMR Serverless 7.11.0 release notes

- **Maximum Job execution time** – The maximum value for `executionTimeoutMinutes` in `StartJobRun` action for BATCH jobs is 7 days from this release onwards. `executionTimeoutMinutes` can no longer be set to `0` i.e. no timeout, for batch job runs.
