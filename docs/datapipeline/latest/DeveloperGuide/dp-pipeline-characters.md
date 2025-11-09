AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Special Characters

AWS Data Pipeline uses certain characters that have a special meaning in pipeline definitions, as shown in the following table.

| Special Character | Description                                                                                                                                                                                                                    | Examples                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| @                 | Runtime field. This character is a field name prefix for a field that is only available when a<br>pipeline runs.                                                                                                               | @actualStartTime @failureReason @resourceStatus                                |
| #                 | Expression. Expressions are delimited by: "#{" and "}" and the contents of the braces are<br>evaluated by AWS Data Pipeline. For more information, see [Expressions](dp-pipeline-expressions.md "dp-pipeline-expressions.md"). | #{format(myDateTime,'YYYY-MM-dd hh:mm:ss')} s3://amzn-s3-demo-bucket/#{id}.csv |
| \*                | Encrypted field. This character is a field name prefix to indicate that AWS Data Pipeline should encrypt the contents of this field in transit between the console or CLI and the AWS Data Pipeline service.                   | \*password                                                                     |
