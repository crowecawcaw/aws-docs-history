# Configure Java version for Oozie

Oozie runs multiple Java Virtual Machine (JVM) processes. This page explains how to
configure the Java version for each process.

- **Oozie Server**: Set `JAVA_HOME` in
  the `oozie-env` classification to update the Java version for the
  `EmbeddedOozieServer`.
- **Oozie Launcher AM**: _Oozie Launcher
  AM_ is a single-mapper MR job that invokes the appropriate
  application client libraries such as Hadoop and Hive. Unless otherwise
  configured, the runtime versions for Oozie Launcher AM are the same as the Java
  runtimes for Hadoop in the EMR cluster. To configure the Java runtime for
  Oozie Launcher AM, set the following property in the `workflow.xml`
  for the job:

```
<property>
     <name>mapred.child.env</name>
     <value>JAVA_HOME=/path/to/JAVA_HOME</value>
 </property>
```

This property ensures that the Oozie Launcher AM for the Oozie job runs on the
Java version that you specify, rather than the Java version that is set in
Hadoop.

- **Application Client Executable**: Because Oozie
  Launcher AM invokes the application client by default, the Java runtime for the
  client executable is the same as the Oozie Launcher AM.
- **Applications launched by an Oozie job**: Unless
  otherwise specified, the runtime versions for the actual application JVMs that
  are launched by an Oozie job are the same as the Java runtimes for Hadoop in the
  EMR cluster. Depending on the type of Oozie Workflow Action used to launch the
  application in an Oozie job (Spark or Hive action), you can update the default
  Java runtime for the actual application JVMs in the `workflow.xml`
  for the Oozie job.
