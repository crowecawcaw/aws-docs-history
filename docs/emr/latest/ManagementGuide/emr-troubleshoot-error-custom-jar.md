# Amazon EMR: Custom JAR cluster errors

The following errors are common to custom JAR clusters.

###### Topics

- [Is your JAR throwing an exception before creating a job?](#emr-troubleshoot-error-custom-jar-1 "#emr-troubleshoot-error-custom-jar-1")
- [Is your JAR throwing an error inside a map task?](#emr-troubleshoot-error-custom-jar-2 "#emr-troubleshoot-error-custom-jar-2")

## Is your JAR throwing an exception before creating a job?

If the main program of your custom JAR throws an exception while
creating the Hadoop job, the best place to look is the
`syslog` file of the step logs. For more information, see [View Amazon EMR log files](emr-manage-view-web-log-files.md "emr-manage-view-web-log-files.md").

## Is your JAR throwing an error inside a map task?

If your custom JAR and mapper throw an exception while processing
input data, the best place to look is the `syslog`
file of the task attempt logs. For more information, see [View Amazon EMR log files](emr-manage-view-web-log-files.md "emr-manage-view-web-log-files.md").
