# Runtime versions using

Java

The following section contain information about the CloudWatch Synthetics runtime versions for Java. This runtime does not have any browser or framework included.

The naming convention for these runtime versions is
`syn-`language`-`majorversion`.`minorversion``.

##

syn-java-1.0

**Major dependencies**:

- AWS Lambda runtime Java 21

**Features**

- _CloudWatch Logs integration_ – You can query and filter for logs through the CloudWatch Synthetics console. Each log message contains unique `canaryRunId`, making it easy to search for logs for a particular canary run.
- _Metrics_ – You can monitor canary run success percentage and duration through CloudWatch metrics. You can also configure alarms to alert you when canaries detect issues.
- _Canary artifacts_ - Each canary run uploads a detailed report corresponding to the run and the steps in the run which can be accessed through Amazon S3.
- _Support for traces_ - You can emit traces for all the requests made by the canary through X-Ray. Each canary run is associated with one trace Id.
