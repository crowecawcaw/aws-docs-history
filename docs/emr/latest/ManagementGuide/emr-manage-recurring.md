# Automate recurring Amazon EMR clusters with

AWS Data Pipeline

###### Note

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue
to use the service as normal.

AWS Data Pipeline is a service that automates the movement and transformation of data. You
can use it to schedule moving input data into Amazon S3 and to schedule launching clusters to
process that data. For example, consider the case where you have a web server recording
traffic logs. If you want to run a weekly cluster to analyze the traffic data, you can
use AWS Data Pipeline to schedule those clusters. AWS Data Pipeline is a data-driven workflow, so that one
task (launching the cluster) can be dependent on another task (moving the input data to
Amazon S3). It also has robust retry functionality.

For more information about AWS Data Pipeline, see the [AWS Data Pipeline Developer Guide](../../../datapipeline/latest/DeveloperGuide/what-is-datapipeline.md "../../../datapipeline/latest/DeveloperGuide/what-is-datapipeline.md"), especially the
tutorials regarding Amazon EMR:

- [Tutorial: Launch an Amazon
  EMR job flow](../../../datapipeline/latest/DeveloperGuide/dp-launch-emr-jobflow.md "../../../datapipeline/latest/DeveloperGuide/dp-launch-emr-jobflow.md")
- [Getting started: Process web logs
  with AWS Data Pipeline, Amazon EMR, and Hive](../../../datapipeline/latest/DeveloperGuide/dp-process-logs.md "../../../datapipeline/latest/DeveloperGuide/dp-process-logs.md")
- [Tutorial: Amazon DynamoDB
  import and export using AWS Data Pipeline](../../../datapipeline/latest/DeveloperGuide/dp-importexport-ddb.md "../../../datapipeline/latest/DeveloperGuide/dp-importexport-ddb.md")
