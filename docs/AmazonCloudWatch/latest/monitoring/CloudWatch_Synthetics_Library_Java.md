

# Runtime versions using Java
<a name="CloudWatch_Synthetics_Library_Java"></a>

The following sections contain information about the CloudWatch Synthetics runtime versions for Java. These runtimes do not include a browser or framework.

The naming convention for these runtime versions is `syn-{{language}} -{{majorversion}}.{{minorversion}}`. 

## syn-java-2.0
<a name="Synthetics_runtimeversion-syn-java-2.0"></a>

**Major dependencies**:
+ AWS Lambda runtime Java 21

 **Changes in syn-java-2.0** 
+ Update the telemetry instrumentation and other bundled components to address security vulnerabilities.
+ Fix an issue that could cause HTTP status code metrics to report zero even when the canary made requests.
+ Fix an issue that could create a duplicate X-Ray trace for a canary run.
+ Improve cleanup after canary timeouts to reduce the risk of storage issues in subsequent runs.
+ Prevent file-processing tasks from a previous canary run from affecting a subsequent run.

## Previous runtime versions for Java
<a name="Previousversions-java"></a>

The following earlier runtime versions for Java are still supported.

### syn-java-1.0
<a name="Synthetics_runtimeversion-syn-java-1.0"></a>

**Major dependencies**:
+ AWS Lambda runtime Java 21

 **Features** 
+ *CloudWatch Logs integration* - You can query and filter for logs through the CloudWatch Synthetics console. Each log message contains unique ` canaryRunId`, making it easy to search for logs for a particular canary run.
+ *Metrics* - You can monitor canary run success percentage and duration through CloudWatch metrics. You can also configure alarms to alert you when canaries detect issues.
+ *Canary artifacts* - Each canary run uploads a detailed report corresponding to the run and the steps in the run which can be accessed through Amazon S3.
+ *Support for traces* - You can emit traces for all the requests made by the canary through X-Ray. Each canary run is associated with one trace Id.