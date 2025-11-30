# Amazon CloudWatch Logs concepts

The terminology and concepts that are central to your understanding and use of CloudWatch Logs
are described below.

**Log class**

CloudWatch Logs offers two classes of log groups. The Standard log class is a full-featured option
for logs that require real-time monitoring or logs that you access
frequently. The Infrequent Access log class is a lower-cost option for logs
that you access less frequently. It supports a subset of the Standard log class
capabilities.

**Log events**

A log event is a record of some activity recorded by the application or
resource being monitored. The log event record that CloudWatch Logs understands
contains two properties: the timestamp of when the event occurred, and the
raw event message. Event messages must be UTF-8 encoded.

**Log streams**

A log stream is a sequence of log events that share the same source. More
specifically, a log stream is generally intended to represent the sequence
of events coming from the application instance or resource being monitored.
For example, a log stream may be associated with an Apache access log on a
specific host. When you no longer need a log stream, you can delete it using
the [aws logs
delete-log-stream](../../../cli/latest/reference/logs/delete-log-stream.md "../../../cli/latest/reference/logs/delete-log-stream.md") command.

**Log groups**

Log groups define groups of log streams that share the same retention,
monitoring, and access control settings. Each log stream has to belong to
one log group. For example, if you have a separate log stream for the Apache access
logs from each host, you could group those log streams into a single log group called
`MyWebsite.com/Apache/access_log`.

There is no limit on the number of log streams that can belong to one log group.

**Metric filters**

You can use metric filters to extract metric
observations from ingested events and transform them to data points in a
CloudWatch metric. Metric filters are assigned to log groups, and all of the
filters assigned to a log group are applied to their log streams.

**Retention settings**

Retention settings can be used to specify how long log events are kept in
CloudWatch Logs. Expired log events get deleted automatically. Just like metric
filters, retention settings are also assigned to log groups, and the
retention assigned to a log group is applied to their log streams.

**Deletion protection**

Deletion protection is a safeguard that prevents accidental deletion of log
groups and their log streams. When enabled on a log group, deletion protection blocks
all deletion operations until it is explicitly disabled. By default, deletion protection
is not enabled. This optional feature helps protect critical operational and compliance
data from unintended removal, such as log groups that contain audit data, and production
application logs for troubleshooting and analysis.
