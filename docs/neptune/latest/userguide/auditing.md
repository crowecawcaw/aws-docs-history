# Using Audit Logs with Amazon Neptune Clusters

To audit Amazon Neptune DB cluster activity, enable the collection of audit logs by
setting a DB cluster parameter. When audit logs are enabled, you can use it to log any
combination of supported events. You can view or download the audit logs to review them.

## Enabling Neptune Audit Logs

Use the `neptune_enable_audit_log` parameter to enable (`1`) or
disable (`0`) audit logs.

Set this parameter in the parameter group that is used by your DB cluster. You can
use the procedure shown in [Editing a DB Cluster Parameter Group or DB Parameter Group](parameter-groups.md#parameters-editgroup "parameter-groups.md#parameters-editgroup")
to modify the parameter using the AWS Management Console, or use the
[modify-db-cluster-parameter-group](../../../cli/latest/reference/neptune/modify-db-cluster-parameter-group.md "../../../cli/latest/reference/neptune/modify-db-cluster-parameter-group.md")
AWS CLI command or the [ModifyDBClusterParameterGroup](API_ModifyDBClusterParameterGroup.md "API_ModifyDBClusterParameterGroup.md")
API command to modify the parameter programatically.

You must reboot your DB instances after modifying this parameter in order to apply
the change.

## Viewing Neptune Audit Logs Using the Console

You can view and download the audit logs by using the AWS Management Console. On the
**Instances** page, choose the DB instance to show its details, and
then scroll to the **Logs** section.

To download a log file, select that file in the **Logs** section, and
then choose **Download**.

## Neptune Audit Log Details

Log files are in UTF-8 format. Logs are written in multiple files, the number of which
varies based on the instance size. To see the latest events, you might have to review
all the audit log files.

Log entries are not in sequential order. You can use the `timestamp` value
for ordering them.

Log files are rotated when they reach 100 MB in aggregate. This limit is not
configurable.

The audit log files include the following comma-delimited information in rows, in the
following order:

| Field            | Description                                                                                                                                                                                                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Timestamp        | The Unix timestamp for the logged event with<br>microsecond precision.                                                                                                                                                                                                                                                   |
| ClientHost       | The hostname or IP that the user connected from.                                                                                                                                                                                                                                                                         |
| ServerHost       | The hostname or IP of the instance that the event is logged<br>for.                                                                                                                                                                                                                                                      |
| ConnectionType   | The connection type. Can be `Websocket`,<br>`HTTP_POST`, `HTTP_GET`, or `Bolt`.                                                                                                                                                                                                                                          |
| Caller's IAM ARN | The ARN of the IAM user or IAM role used to sign the request. Empty if IAM authentication is disabled. Its format is:<br>`arn:`partition`:`service`:`region`:`account`:`resource``<br>For example:<br>`arn:aws:iam::123456789012:user/Anna`<br>`arn:aws:sts::123456789012:assumed-role/AWSNeptuneNotebookRole/SageMaker` |
| Auth Context     | Contains a serialized JSON object that has authentication<br>information. The field `authenticationSucceeded` is<br>`True` if the user was authenticated.<br>Empty if IAM authentication is disabled.                                                                                                                    |
| HttpHeader       | The HTTP header information. Can contain a query. Empty for WebSocket<br>and Bolt connections.                                                                                                                                                                                                                           |
| Payload          | The Gremlin, SPARQL, or openCypher query.                                                                                                                                                                                                                                                                                |
